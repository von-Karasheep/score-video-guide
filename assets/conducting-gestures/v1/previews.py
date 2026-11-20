"""Rebuild a neutral-tempo WebP from the production vector renderer (Pillow and FFmpeg/libass)."""
import math
import subprocess
import tempfile
from pathlib import Path
from PIL import Image
from baton import ROOT, draw_guides, draw_motion, pattern

HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: 166
PlayResY: 112
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Body,MiSans,24,&H00303820,&H00303820,&H00303820,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def preview(key, ffmpeg="ffmpeg"):
    frames_per_stroke = 9 if key == "in-3-sub2" else 18
    strokes = len(pattern(key)["strokes"])
    count = frames_per_stroke * strokes
    duration = count / 30
    events = []

    def stamp(seconds):
        n = round(seconds * 100)
        return f"{n//360000}:{n//6000%60:02}:{n//100%60:02}.{n%100:02}"

    def event(a, b, layer, tags, content):
        events.append(f"Dialogue: {layer},{stamp(a)},{stamp(b)},Body,,0,0,0,,{{{tags}}}{content}")

    def bgr(c):
        return "&H" + c[5:7] + c[3:5] + c[1:3] + "&"

    def poly(a,b,x,y,path,col,move="",layer=2):
        pos = move or rf"\pos({x:.2f},{y:.2f})"
        event(a,b,layer,rf"\an7{pos}\bord0\shad0\p1\1c{bgr(col)}",path)

    def line(a,b,x,y,dx,dy,col,width,layer):
        length=math.hypot(dx,dy)
        nx,ny=-dy/length*width/2,dx/length*width/2
        path=f"m {nx:.2f} {ny:.2f} l {dx+nx:.2f} {dy+ny:.2f} {dx-nx:.2f} {dy-ny:.2f} {-nx:.2f} {-ny:.2f}"
        poly(a,b,x,y,path,col,layer=layer)

    def text(a,b,x,y,label,size,col,anchor,layer):
        event(a,b,layer,rf"\an{anchor}\pos({x:.1f},{y:.1f})\fs{size}\fnMiSans Medium\1c{bgr(col)}",label)

    draw_guides(line, text, key, 0, duration, (15,10))
    for i in range(strokes):
        draw_motion(poly, key, i, i*frames_per_stroke/30, (i+1)*frames_per_stroke/30, (15,10))
    with tempfile.TemporaryDirectory() as folder:
        Path(folder,"loop.ass").write_text(HEADER+"\n".join(events)+"\n")
        raw=subprocess.check_output([str(ffmpeg),"-v","error","-f","lavfi","-i","color=c=0xf3f7f2:s=332x224:r=30",
            "-vf","ass=loop.ass","-frames:v",str(count),"-pix_fmt","rgb24","-f","rawvideo","-"],cwd=folder)
    w,h=332,224
    stride=w*h*3
    assert len(raw)==count*stride
    frames=[Image.frombytes("RGB",(w,h),raw[k:k+stride]) for k in range(0,len(raw),stride)]
    dest=ROOT/"previews"/(key+".webp")
    dest.parent.mkdir(exist_ok=True)
    delays=[round((i+1)*1000/30)-round(i*1000/30) for i in range(count)]
    frames[0].save(dest,save_all=True,append_images=frames[1:],duration=delays,loop=0,lossless=True,method=5)
    return dest


if __name__ == "__main__":
    for master in sorted((ROOT/"patterns").glob("*.json")):
        preview(master.stem)
