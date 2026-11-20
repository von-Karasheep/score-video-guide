"""Check loop closure, animated masters and archived film dependencies after library edits."""
import csv
import json
from pathlib import Path
from PIL import Image
from archive import LIBRARY, sha


def check(root=LIBRARY):
    for item in sorted(root.glob("v*/patterns/*.json")):
        data=json.loads(item.read_text())
        strokes=data["strokes"]
        assert strokes and len(strokes)==len(data["count_labels"]), item
        assert data["number_positions"] and data["source"], item
        for i,stroke in enumerate(strokes):
            assert len(stroke)>=2 and all(len(pt)==2 for pt in stroke), item
            assert stroke[-1]==strokes[(i+1)%len(strokes)][0], item
        for point in data["number_positions"]:
            assert any(stroke[0]==point for stroke in strokes), item
        with Image.open(item.parents[1]/"previews"/(item.stem+".webp")) as im:
            assert im.is_animated and im.info.get("loop")==0, item
            for frame in range(im.n_frames):
                im.seek(frame)
                im.load()
    for index in sorted(root.glob("videos/*/index.json")):
        record=json.loads(index.read_text())
        version=root/record["version"]
        assert sha(version/"baton.py")==record["renderer_sha256"], index
        if "drawing_sha256" in record:
            assert sha(version/"op60_drawing.py")==record["drawing_sha256"],index
        for key,digest in record["patterns"].items():
            assert sha(version/"patterns"/(key+".json"))==digest,index
        clock=index.parent/"beats.csv"
        assert sha(clock)==record["clock_sha256"],index
        with clock.open(newline="") as f:
            used={(r["meter"],r["grouping"],r["pattern"]) for r in csv.DictReader(f) if r["mode"] in {"conduct","pickup"}}
        assert used=={(c["meter"],c["grouping"],c["pattern"]) for c in record["examples"]},index
        for sample in record["examples"]:
            assert (index.parent/sample["file"]).stat().st_size>0,index
    print("Gesture loops and archived dependencies verified.")


if __name__=="__main__":
    check()
