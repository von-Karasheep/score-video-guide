from pathlib import Path
from functools import lru_cache
import math
import subprocess
import tempfile
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
S = 2
W, H = 1920, 1080
FONTS = ROOT/"fonts" if (ROOT/"fonts/MiSans-Regular.ttf").exists() else Path.home() / "Library/Fonts"
BG, PAPER = "#F1F3EE", "#FFFFFF"
INK, MUTED, RULE = "#203830", "#536A60", "#CCD6CE"
GREEN, GREEN_BG = "#246B5A", "#EBF3EC"
INTRO, A, B = "#77688F", "#4B879C", "#A77A57"
SANS, MED, BOLD = "MiSans-Regular.ttf", "MiSans-Medium.ttf", "MiSans-Semibold.ttf"
ITALIC, ROMAN = "MinionPro-It.otf", "MinionPro-Regular.otf"
img = Image.new("RGB", (788,232), "white")
dr = ImageDraw.Draw(img)

@lru_cache(None)
def font(face, size):
    return ImageFont.truetype(str(FONTS/face), round(size*S))

def pt(x,y):
    return (round(x*S),round(y*S))

def txt(x,y,words,size=20,fill=INK,face=SANS,anchor="lm"):
    dr.text(pt(x,y),words,font=font(face,size),fill=fill,anchor=anchor)

def rect(x1,y1,x2,y2,fill=None,outline=None,width=1,radius=0):
    p=(*pt(x1,y1),*pt(x2,y2))
    if radius: dr.rounded_rectangle(p,radius=round(radius*S),fill=fill,outline=outline,width=round(width*S))
    else: dr.rectangle(p,fill=fill,outline=outline,width=round(width*S))

def line(points,color,width=1):
    dr.line([pt(x,y) for x,y in points],fill=color,width=max(1,round(width*S)),joint="curve")

def disk(x,y,r,fill,outline=None,width=1):
    dr.ellipse((*pt(x-r,y-r),*pt(x+r,y+r)),fill=fill,outline=outline,width=round(S*width))

def bezier(p0,p1,p2,p3):
    return [tuple((1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t*t*c+t**3*d for a,b,c,d in zip(p0,p1,p2,p3)) for t in [i/60 for i in range(61)]]
