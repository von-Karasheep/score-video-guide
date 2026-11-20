"""Op. 60 card in a 394 x 116 logical box, rendered at 2x. Phases follow performance time."""
from functools import lru_cache
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
from PIL import Image, ImageDraw
import op60_drawing as g

NUM = {"2":"二","3":"三","4":"四","5":"五","6":"六","7":"七","8":"八","9":"九","12":"十二","16":"十六"}


@lru_cache(None)
def pattern(key):
    if not key or Path(key).name!=key: raise ValueError("Invalid pattern ID")
    return json.loads((ROOT/"patterns"/(key+".json")).read_text())


def frame(meter,key,stroke,phase,mode="conduct",unit_text=None):
    if not 0<=phase<=1: raise ValueError("phase must be in [0,1]")
    num,den=meter.split("/")
    master=pattern(key); points=master["number_positions"]; motion=master["strokes"]; guides=master["guides"]
    if not 0<=stroke<len(motion): raise ValueError("stroke outside its pattern")
    g.img=Image.new("RGB",(788,232),"white");g.dr=ImageDraw.Draw(g.img)
    g.rect(0,0,393.5,115.5,"#F3F7F2","#D5E2D8",1,13)
    g.txt(17,22,NUM[den]+NUM[num]+"拍",18,g.MUTED,g.MED)
    g.txt(15,58,meter,41,g.GREEN,g.MED)
    if unit_text is None:
        unit_text=NUM[den]+"分音符一拍"
        if num=="6" and key=="in-2":unit_text="附点"+NUM[str(int(den)//2)]+"分音符一拍"
    font_size=17
    while g.font(g.SANS,font_size).getlength(unit_text)>231: font_size-=.5
    g.txt(17,93,unit_text,font_size,g.MUTED)
    g.line([(139,15),(139,101)],"#D6E3D9")
    word,sub=master["captions"][stroke]
    states={"prepare":("预备","等候起拍"),"hold":("延长","等候再起"),"release":("收拍","乐句结束"),"pickup":("弱起","向上预备")}
    word,sub=states.get(mode,(word,sub))
    g.txt(154,34,word,22,g.GREEN,g.BOLD);g.txt(154,74,sub,16,g.GREEN,g.MED)
    for curve in guides:g.line(curve,"#A9BDAE",2)
    for i,(x,y) in enumerate(points):
        if len(points)==1:g.disk(x,y,4.5,g.GREEN)
        else:
            g.disk(x,y,7,"#F3F7F2",g.GREEN,1);g.txt(x,y,str(i+1),10,g.GREEN,g.MED,"mm")
    arr=motion[stroke]
    if master.get("split_return"):
        arr=guides[0] if phase<master["split_return"] else guides[1]
        phase=phase/master["split_return"] if phase<master["split_return"] else (phase-master["split_return"])/(1-master["split_return"])
    pos=phase*(len(arr)-1);j=min(int(pos),len(arr)-2);frac=pos-j
    px,py=(arr[j][i]+(arr[j+1][i]-arr[j][i])*frac for i in (0,1))
    g.line(arr[max(0,j-12):j+1]+[(px,py)],g.GREEN,3)
    hand(px,py)
    return g.img


def hand(px,py):
 bx,by=px+26,max(14,py-39)
 g.line([(px,py),(bx+2,by-2)],g.INK,2.4);g.disk(px,py,3.7,g.GREEN,'white',.7)
 shape=[(0,0),(1,-5),(7,-9),(15,-8),(21,-8),(28,-3),(25,5),(19,6),(13,9),(8,8),(4,6),(1,6),(0,0)]
 g.dr.polygon([g.pt(bx+a,by+b) for a,b in shape],fill='#EBE3D5');g.line([(bx+a,by+b) for a,b in shape],g.INK,1.3)
 for pts in [[(3,4),(8,0),(13,0)],[(8,7),(13,3)]]:g.line([(bx+a,by+b) for a,b in pts],'#706F64',1)
 g.dr.polygon([g.pt(bx+a,by+b) for a,b in [(22,-7),(31,-4),(27,8),(20,5)]],fill='#49695A')

