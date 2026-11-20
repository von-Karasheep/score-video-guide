"""Write the single work-level UTF-8 chapter sheet from completed movement blocks."""
from pathlib import Path
import re
import os
import tempfile

PREFIX="【乐谱同步+分段与动机提示版】"
FIRST="00:00 引言；制作说明；总览"
MAX_TITLE_UNITS = 16
MIN_GAP_SECONDS = 6
NUMBER="一 二 三 四 五 六 七 八 九 十 十一 十二 十三 十四 十五 十六 十七 十八 十九 二十".split()


def update_work(path, composer, title, conductor, orchestra, year, movement, lines):
    path=Path(path)
    if not (1<=movement<=len(NUMBER) and 1<=len(lines)<=10 and lines[0]==FIRST):
        raise ValueError("Invalid movement, number of rows or opening marker")
    header=f"{PREFIX}{composer}《{title}》-{conductor}+{orchestra}@{year}"
    values=[]
    for line in lines:
        m=re.fullmatch(r"(\d{2,}):([0-5]\d) ([^\s].*)",line)
        if not m or "\n" in line:raise ValueError(f"Invalid timestamp row: {line!r}")
        label = m[3]
        if len(label.encode("utf-16-le")) // 2 > MAX_TITLE_UNITS:
            raise ValueError(f"Chapter title exceeds {MAX_TITLE_UNITS} characters: {label!r}")
        if re.fullmatch(r"[A-Z]\s*[：:。.]?", label.strip()):
            raise ValueError(f"Name the formal section after its letter: {label!r}")
        values.append(int(m[1])*60+int(m[2]))
    if any(b - a < MIN_GAP_SECONDS for a, b in zip(values, values[1:])):
        raise ValueError(f"Chapter markers must be at least {MIN_GAP_SECONDS} seconds apart")
    blocks={}
    if path.exists():
        existing=path.read_text(encoding="utf-8").splitlines()
        if not existing or existing[0]!=header:raise ValueError("Work or recording does not match the existing sheet")
        current=None
        for row in existing[1:]:
            if not row:continue
            m=re.fullmatch("第([一二三四五六七八九十]+)乐章：",row)
            if m:
                current=NUMBER.index(m[1])+1
                if current in blocks:raise ValueError("Duplicate movement heading")
                blocks[current]=[]
            elif current is None:raise ValueError("Expected a movement heading")
            else:blocks[current].append(row)
    blocks[movement]=list(lines)
    text=header+"\n"+"\n\n".join(f"第{NUMBER[k-1]}乐章：\n"+"\n".join(v) for k,v in sorted(blocks.items()))+"\n"
    with tempfile.NamedTemporaryFile("w",dir=path.parent,delete=False,encoding="utf-8") as f:f.write(text)
    os.replace(f.name,path)
