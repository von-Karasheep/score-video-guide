"""Generate a self-contained Chinese index of installed masters and filmed examples."""
import html
import json
import os
import tempfile
from gesture_manual import master_cards, berlin_example, DRAWING, TIMING, CONTROLS
from pathlib import Path

LIBRARY = Path(__file__).resolve().parent


def gallery():
    esc = html.escape
    records = []
    for manifest in sorted(LIBRARY.glob("videos/*/index.json")):
        data = json.loads(manifest.read_text())
        if data["version"]=="v1":
            continue
        directory = manifest.parent.relative_to(LIBRARY).as_posix()
        links = []
        for sample in data["examples"]:
            key=sample["pattern"]
            title=json.loads((LIBRARY/data["version"]/"patterns"/(key+".json")).read_text())["name_zh"]
            links.append(f'<li><a href="{esc(directory)}/{esc(sample["file"])}">{esc(sample["meter"])} · {esc(title)}（{esc(sample["grouping"])}）</a></li>')
        records.append(f'<article><h3>{esc(data["title"])}</h3><p>{esc(data["recording"])}</p><ul>{"".join(links)}</ul>'
                       f'<p><a href="{esc(directory)}/beats.csv">逐拍拍点表</a>　<a href="{esc(directory)}/index.json">演出与母版记录</a></p></article>')
    body = """<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>指挥手势动画档案</title><style>
*{box-sizing:border-box} body{margin:0;background:#f3f5f1;color:#203830;font:16px/1.7 MiSans,system-ui,sans-serif}
main{max-width:1060px;margin:auto;padding:48px 24px} h1{font-size:clamp(30px,5vw,50px);line-height:1.2;margin:0 0 .4em}
h2{margin:1.5em 0 .35em;font-size:26px}h3{margin:0} p{margin:.35em 0}a{color:#245c4e;text-underline-offset:.17em}
.master-nav,.controls{display:flex;flex-wrap:wrap;gap:7px 10px}
.master-nav{margin:16px 0}.master-nav a{border-bottom:1px solid #a5bbaf;text-decoration:none;padding:2px 0;margin-right:12px}
article,.example{border:1px solid #cad7cc;background:#fbfcf8;border-radius:10px}
.columns{display:grid;grid-template-columns:minmax(0,394px) minmax(0,1fr);gap:14px 26px;align-items:start;margin-top:15px}
figure{margin:0;min-width:0}figure img{display:block;width:100%;height:auto}figcaption{margin:7px 0;font-size:.91rem}
h3{font-size:1.23rem}.controls button{font:inherit;font-size:.82rem;color:#234d40;background:white;border:1px solid #b5c9bc;padding:3px 9px;border-radius:5px;cursor:pointer}
.controls button[aria-pressed="true"]{background:#245c4e;border-color:#245c4e;color:white}
.master .motion,.motion{display:block;margin:0;line-height:1.6}.motion li+li{margin-top:.5em}.motion small{white-space:nowrap;color:#52675d;font-variant-numeric:tabular-nums}
.source{font-size:.86rem}.example{padding:16px}.master{scroll-margin:1em}
details{margin:.8rem 0;padding:.55rem 1rem;border-left:3px solid #bdcfc1;background:#f9faf7}
summary{cursor:pointer;font-weight:600}code,pre{font-family:ui-monospace,monospace;font-size:.9em}pre{white-space:pre-wrap;overflow-wrap:anywhere}
@media(max-width:780px){.columns{grid-template-columns:1fr}main{padding:24px 15px}figure{max-width:394px}.motion small{display:inline-block}}
article{padding:15px 20px;margin:12px 0}ul{display:flex;flex-wrap:wrap;gap:6px 20px;padding:0;list-style:none}
ol{padding-left:1.5em}ol li{margin:.4em 0}footer{margin-top:24px;border-top:1px solid #cbd6ce;padding-top:12px}
</style><main><h1>指挥手势动画档案</h1><p>同一拍型共用一条棒尖轨迹。下方母版按固定速度循环，实片样例保留演出速度。</p>
<h2 id="masters">贝四手势母版</h2><p>以下方向都按观看卡片时的左右来读。棒尖到达编号圈的瞬间算这一拍；随后的小弧把手带到下一落点。点拍位按钮可停在相应姿势，点“循环播放”继续看整小节。括号中是棒尖在卡片上的起止坐标。</p>
<p><a href="v2/Op60-comparison.mp4">播放贝四原图与动画对照</a>　<a href="#drawing">查看逐帧画法</a>　<a href="#timing">查看现场对拍方法</a></p>""" + master_cards(LIBRARY) + DRAWING + TIMING + berlin_example(LIBRARY) + """
<h2 id="archive">新片用哪一版手势</h2><p>先按指挥实际挥出的拍数和分拍方式选上面的一条路径，把分组、起止时间、起始挥次和停顿写入这场演出的逐拍表。新片沿用同一套手形、落点与轨迹。遇到新的挥法，先做完整一小节，记录每一下从哪落到哪、怎样回弹，连同轨迹文件与循环预览一起登记。每部成片归档所用母版版本、逐拍拍点，以及从成片裁下的每种拍号与挥法的无声片段。</p>
<h2>贝多芬系列的其余版式</h2><ol>
<li><strong>演出与总谱。</strong>用节目单或发行资料核实日期、地点、乐团、指挥、合唱团和独唱者。确认总谱版本，按现场演奏顺序展开反复、跳房子和弱起。将总谱小节、现场时间和成片时间对应起来。</li>
<li><strong>片头与正文。</strong>片头约三秒交代作品、乐章和演出，再用约三秒给出曲式。按 1920 × 1080 排版，导出为 3840 × 2160、30 帧/秒。左栏显示一个完整谱表系统，保留谱号、调号和声部名。游标从第一个发声音符开始走。</li>
<li><strong>记号、主题和调性。</strong>砖红框圈出谱上正在解释的记号，左侧用中文说明。主题用固定字母和颜色，右侧谱例与左侧对应乐句同色。调性说明写出可听见的依据，例如低音走向或终止式。</li>
<li><strong>演出小窗与唱词。</strong>在小窗左缘下方用 MiSans 写声部、中文姓名和括号内的外文名。先按实唱核对原文，再在顶部中央框内上排用霞鹜文楷写中文、下排写这场演出实际唱的原文。待唱部分用浅色，唱到的原词或音节与对应中文词组加深。纯器乐段收起歌词框。</li>
<li><strong>时间轴与声音。</strong>用上下两层显示曲式和主题，段宽按实演时长分配，当前段从左向右填充。原片时间码放工程索引。优先保留可核实的同场无损音轨，记录音轨格式和来源。</li>
<li><strong>分段 TXT。</strong>每部作品、同场演出共用一份 UTF-8 纯文本。首行写“【乐谱同步+分段与动机提示版】作曲家《曲名》-指挥+乐团英文简称@年份”。按“第一乐章：”等标题分组，每乐章最多十行时间标记，首条为“00:00 引言；制作说明；总览”。每个时间后接一个半角空格和段名，用“呈示部：主部”等全角标点。按实际成片取时间；终乐章有宣叙、变奏或赋格时写实际曲式。做完新乐章后更新同一份 TXT。</li>
<li><strong>交付与复核。</strong>看成片里的起拍、换速、换拍、翻页、声部进入和收束，听到最后的余响，检查完整解码。同一作品各乐章共用一套封面，分别排 16:9 和 4:3 两张图。</li></ol>
""" + ('<h2>成片里的手势</h2>'+"".join(records) if records else '')+'</main>'+CONTROLS+'</html>\n'
    with tempfile.NamedTemporaryFile("w",prefix=".gallery-",dir=LIBRARY,delete=False) as f:
        f.write(body)
    os.replace(f.name,LIBRARY/"指挥手势.html")


if __name__=="__main__":
    gallery()
