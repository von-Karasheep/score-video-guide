"""Archive the timing table and one actual encoded widget sample per meter and pattern."""
import csv
import hashlib
import json
import math
import os
import re
import subprocess
import tempfile
from pathlib import Path
from gallery import gallery

LIBRARY = Path(__file__).resolve().parent
FIELDS = ("measure","meter","grouping","pattern","stroke","start","end","phase_from","phase_to","mode")
MODES = {"conduct","pickup","hold","prepare","release"}


def sha(path):
    digest=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024),b""):
            digest.update(block)
    return digest.hexdigest()


def archive_video(video_id, metadata, rows, movie, widget_crop, version="v2", ffmpeg="ffmpeg"):
    """Times are absolute output seconds. crop is x,y,width,height in encoded pixels."""
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*",video_id) or not re.fullmatch(r"v[1-9]\d*",version):
        raise ValueError("Invalid video or master version ID")
    rows=list(rows)
    if not rows or not all(metadata.get(k) for k in ("title","recording","timing_basis")):
        raise ValueError("The film, recording and timing provenance are required")
    root=LIBRARY/version
    recipes={}
    examples={}
    end=None
    for row in rows:
        key=row["pattern"]
        if not row["grouping"] or not re.fullmatch(r"[a-z0-9-]+",key) or not re.fullmatch(r"\d+/\d+",row["meter"]):
            raise ValueError(f"Invalid pattern or meter in {row}")
        if key not in recipes:
            master=root/"patterns"/(key+".json")
            recipes[key]=json.loads(master.read_text())
        mode=row["mode"]
        a,b=float(row["start"]),float(row["end"])
        p,q=float(row["phase_from"]),float(row["phase_to"])
        stroke=int(row["stroke"])
        if (not all(map(math.isfinite,(a,b))) or not 0<=a<b or end is not None and a < end-1e-6
                or mode not in MODES or not 0<=stroke<len(recipes[key]["strokes"]) or not 0<=p<=q<=1):
            raise ValueError(f"Invalid timing or gesture in {row}")
        if mode=="hold" and p!=q:
            raise ValueError("A fermata must hold a single pose")
        end=b
        if mode in {"conduct","pickup"}:
            identity=(row["meter"],row["grouping"],key)
            if identity not in examples or (mode=="conduct" and stroke==0 and not examples[identity][1]):
                examples[identity]=(a,mode=="conduct" and stroke==0)
    parent=LIBRARY/"videos"
    parent.mkdir(exist_ok=True)
    target=parent/video_id
    x,y,w,h=widget_crop
    if min(x,y)<0 or min(w,h)<=0 or not examples:
        raise ValueError("A valid encoded card crop and timed strokes are required")
    # Keep samples inside the chosen run when a meter or grouping changes.
    with tempfile.TemporaryDirectory(dir=parent) as tmp:
        folder=Path(tmp)/video_id
        folder.mkdir()
        clock=folder/"beats.csv"
        with clock.open("w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        data={**metadata,"version":version,"movie_sha256":sha(movie),"renderer_sha256":sha(root/"baton.py"),
              "patterns":{k:sha(root/"patterns"/(k+".json")) for k in sorted(recipes)},
              "clock_sha256":sha(clock),"widget_crop":list(widget_crop),"examples":[]}
        if (root/"op60_drawing.py").exists():
            data["drawing_sha256"]=sha(root/"op60_drawing.py")
        for (meter,grouping,key),(begin,_) in examples.items():
            stop=begin
            cycle_end=None
            for row in rows:
                a,b=float(row["start"]),float(row["end"])
                if b<=begin: continue
                if a-stop>1e-5 or (row["meter"],row["grouping"],row["pattern"])!=(meter,grouping,key) or row["mode"] not in {"conduct","pickup"}: break
                stop=b
                if cycle_end is None and int(row["stroke"])==len(recipes[key]["strokes"])-1 and float(row["phase_to"])==1:
                    cycle_end=b
                if cycle_end is not None and stop>=begin+4: break
            seconds=min(stop,max(begin+4,cycle_end or stop))-begin
            name=f"{meter.replace('/','-')}_{key}.mp4"
            if any(item["file"]==name for item in data["examples"]):
                name=f"{meter.replace('/','-')}_{key}_{len(data['examples'])+1}.mp4"
            data["examples"].append(dict(meter=meter,grouping=grouping,pattern=key,start=begin,duration=round(seconds,6),file=name))
        index=folder/"index.json"
        index.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
        def same_record():
            return ((target/"index.json").read_bytes()==index.read_bytes() and sha(target/"beats.csv")==sha(clock)
                    and all((target/item["file"]).stat().st_size for item in data["examples"]))
        if target.exists():
            if same_record():
                gallery()
                return target
            raise FileExistsError(f"{target} already has a different record; assign the revision a new ID")
        for item in data["examples"]:
            subprocess.run([str(ffmpeg),"-nostdin","-v","error","-ss",str(item["start"]),"-i",str(Path(movie).resolve()),
                "-t",str(item["duration"]),"-an","-vf",f"crop={w}:{h}:{x}:{y},setsar=1",
                "-c:v","libx264","-crf","17","-pix_fmt","yuv420p","-movflags","+faststart",str(folder/item["file"])],check=True)
        try:
            os.rename(folder,target)
        except OSError:
            if not target.is_dir() or not same_record(): raise
    gallery()
    return target
