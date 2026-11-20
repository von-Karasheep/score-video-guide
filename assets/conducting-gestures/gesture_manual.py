"""Render human-readable production notes alongside the pinned animated masters."""
import base64
import html
import io
import json
from PIL import Image

esc = html.escape


def xy(point):
    return f"({point[0]:g}, {point[1]:g})"


def pose_buttons(path, master, notes):
    with Image.open(path) as loop:
        step, remainder = divmod(loop.n_frames, len(master["strokes"]))
        if remainder or step < 1:
            raise ValueError(f"Preview frames and strokes disagree: {path}")
        if "split_return" in master:
            poses = [("落点", 0), ("上提途中", step//4),
                     ("转向附近", round(master["split_return"]*step)), ("回落途中", round(.8*step))]
        else:
            poses = [(label, i*step) for i, (label, _) in enumerate(notes["strokes"])]
        parts = ['<button type="button" aria-pressed="true" data-loop>循环播放</button>']
        for label, index in poses:
            loop.seek(index)
            buf = io.BytesIO()
            loop.convert("RGB").save(buf, format="PNG", optimize=True)
            uri = "data:image/png;base64,"+base64.b64encode(buf.getvalue()).decode("ascii")
            parts.append(f'<button type="button" aria-pressed="false" data-pose="{uri}" '
                         f'data-frame="{index}">{esc(label)}</button>')
    return "".join(parts)


def master_cards(root):
    if not (root/"v2/patterns").is_dir():
        return ""
    notes = json.loads((root/"v2/gesture-notes.zh.json").read_text())
    masters = [(p, json.loads(p.read_text())) for p in (root/"v2/patterns").glob("*.json")]
    cards, nav = [], []
    for path, master in sorted(masters, key=lambda item: (len(item[1]["strokes"]),item[0].stem)):
        key, title = path.stem, master["name_zh"]
        spec = notes[key]
        strokes = master["strokes"]
        if len(spec["strokes"]) != len(strokes):
            raise ValueError(f"Each performed stroke needs its own explanation: {key}")
        preview = f"v2/previews/{key}.webp"
        nav.append(f'<a href="#{esc(key)}">{esc(title)}</a>')
        descriptions = []
        for (label, motion), pts in zip(spec["strokes"], strokes):
            descriptions.append(f'<li><strong>{esc(label)}</strong>　{esc(motion)} '
                                f'<small>{xy(pts[0])} → {xy(pts[-1])}</small></li>')
        buttons = pose_buttons(root/preview, master, spec)
        cards.append(f'''<article class="master" id="{esc(key)}"><h3>{esc(title)}</h3>
<p>{esc(spec["use"])}</p>
<div class="columns"><figure><a href="{esc(preview)}"><img width="788" height="232" src="{esc(preview)}" alt="{esc(title)}循环动画"></a>
<figcaption>{esc(spec["cue"])}</figcaption><div class="controls" role="group" aria-label="{esc(title)}动作定位">{buttons}</div></figure>
<ul class="motion">{"".join(descriptions)}</ul></div>
<p class="source"><a href="v2/patterns/{esc(key)}.json">查看这条轨迹的采样坐标</a></p></article>''')
    return '<nav class="master-nav" aria-label="选择拍型">'+"".join(nav)+'</nav>'+"".join(cards)


DRAWING = """<section id="drawing"><h2>一帧里的棒尖、手与指挥棒怎样画</h2>
<p>这套动画用 Python 和 Pillow 逐帧绘制。每帧读入拍号、手势、当前挥次和已经走过的比例，先算出棒尖，再由棒尖带动整只手。绘图用 394 × 116 的逻辑画布，左上角是原点，向右为 x 增大，向下为 y 增大。按两倍尺寸输出 788 × 232 像素；贝九末乐章的 4K 成片将整张卡贴在 (1636, 252)。</p>
<ol>
<li><strong>先画卡面和路标。</strong>铺浅绿圆角底，左栏用 MiSans 写谱面拍号与音符单位，中栏写当前拍位。右边先画完整的灰绿导向弧，再画编号圈。一小节一挥只在低处画一个实心落点。切换到后半拍时，慢三拍的三个主拍圈仍留在原处。</li>
<li><strong>在曲线上取棒尖的位置。</strong>每段三次贝塞尔曲线按参数从 0 到 1 等分成 60 段，存下 61 个点。取当前这一下已经走过的比例 p，用 60p 找到相邻两个点，按小数部分在两点间插值。棒尖后方沿当前弧段取最多 12 个采样间隔和当前小段，画出深绿色短尾迹。</li>
<li><strong>让手握住棒。</strong>先确定棒尖 (x, y)，再把手形原点定在 (x + 26, max(14, y − 39))。从棒尖向手形原点右 2、上 2 的位置画深色棒身；在棒尖画白边绿点，然后叠上米色手形的外轮廓、两道手指折线和深绿袖口。手与袖口随同一原点平移，上限使抬手时仍能看见袖口。</li>
</ol><details><summary>展开建线参数与颜色，复画同一条弧</summary>
<p>普通二、三、四拍的每一段从 A=(x, y) 到下一落点 B=(u, v)，两个控制点依次为 (x+4, y−23) 和 (u−16, v−25)。浅色导线和棒尖共用这条曲线。下列两种动作有自己的回弹。</p>
<ul class="motion"><li><strong>整小节一挥。</strong>上提的四个点依次为 (284,92)、(271,66)、(313,30)、(306,17)。回落依次为 (306,17)、(301,37)、(291,82)、(284,92)。先用全段时间的 53% 走完第一条，再用 47% 走完第二条。</li>
<li><strong>慢三拍分拍。</strong>在每个主落点 A 的右 8、上 5 设分拍点 M。A → M 的控制点为 (x−4, y−22)、(x+8, y−20)；M → B 的控制点为 (x+8, y−29)、(u−15, v−22)。每半拍都取一段完整曲线。浅色背景仍画三条主拍弧线。</li></ul>
<p>卡底 #F3F7F2，导线 #A9BDAE、宽 2，尾迹 #246B5A、宽 3；棒身 #203830、宽 2.4。棒尖半径 3.7，手形填色 #EBE3D5，袖口 #49695A。尺寸均为逻辑像素。手的多边形顶点和字形位置可直接查看绘图函数。</p>
<p><a href="v2/baton.py">整卡与手形的绘图函数</a>　<a href="v2/op60_drawing.py">画笔、字体与曲线采样</a>　<a href="v2/previews.py">循环动图生成脚本</a></p>
</details></section>"""

TIMING = """<section id="timing"><h2>怎样让每一拍跟上现场</h2>
<ol><li><strong>选拍型，记落点。</strong>左栏保留总谱拍号，按指挥实际给出的主拍或分拍选择母版。逐帧看清楚的右手或棒尖，在转折处结合乐队起音确认第几小节、第几拍，把落点换算到成片时间。分别标记看得见的落点、仅从声音核实的进入和推算的中间拍。</li>
<li><strong>在两个锚点之间调速。</strong>沿已经对齐的总谱与演奏时钟，按各拍在这段演奏中的相对位置分配到两个已知落点之间。遇到明显换速或再起，加一个可核对的锚点。每一帧按当前拍的实际起止时间沿原轨迹取位置。</li>
<li><strong>弱起、延长和换拍。</strong>弱起从实际挥到的那一下或半途接入。延长时把一拍拆开，把停住这一行的起止进度写成同一个值，直到再起才继续。换拍型时在实际第一下切换；末次收拍按现场余响保留静止姿势。表中的 <code>mode</code> 控制文字，<code>phase_from</code> 和 <code>phase_to</code> 决定棒尖是否移动。</li></ol>
<p>在每个区间 <code>[start, end)</code> 内，先算 <code>f = (t − start) / (end − start)</code>，再算 <code>p = phase_from + f × (phase_to − phase_from)</code>。调用 <code>frame(meter, pattern, stroke, p, mode)</code>。<code>stroke</code> 从 0 数起；到了区间末端，改读下一行。正常一挥的 p 从 0 到 1。</p></section>"""

def berlin_example(root):
    directory = "videos/beethoven-op125-iv-berlin-2000-op60"
    if not (root/directory/"beats.csv").is_file():
        return ""
    return f'''<section id="example"><h2>照着做一次 · 贝九末乐章第 890–891 小节</h2>
<p>柏林 2000 年这场演出，阿巴多在尾声把 2/2 合成一小节一挥。右手三个连续落点在成片 21:22.300、21:23.000、21:23.800。第一小节用 21 帧走完，下一小节同样的路径用 24 帧走完。</p>
<div class="columns example"><figure><img width="788" height="232" src="v2/Op125-890-891.webp" alt="按两小节实际时长播放的拍号卡"><figcaption>两小节连播 · 30 帧/秒 · 共 45 帧</figcaption></figure>
<div><p>在逐拍表里，两行都写 <code>2/2 · in-1 · stroke 0 · conduct</code>。第 890 小节的成片区间是 <code>[1282.3, 1283.0)</code> 秒，第 891 小节是 <code>[1283.0, 1283.8)</code> 秒，两行的进度都是 0 → 1。</p>
<p>帧号从零算起。第 38469 帧的绿点在最低处。到第 38480 帧，这一挥已用去 11/21 的时间，棒尖接近上方转折。第 38490 帧落回原点，下一小节从这里起算。第 38514 帧属于第 892 小节。</p></div></div>
<details><summary>用档案里的拍点表生成这 45 帧</summary><p>在希望保存动图的目录执行下列命令。脚本需要 Python 3、Pillow 及 MiSans Regular、Medium、Semibold。默认读取本档案中的贝九拍点表，输出 <code>Op125-890-891.webp</code>。</p>
<pre><code>python3 -B "$HOME/.codex/skills/score-video-guide/assets/conducting-gestures/v2/render_example.py"</code></pre>
<p>复用到别处时，调用 <code>render_excerpt(table, first_frame, stop_frame, destination)</code>，传入该场演出的拍点表与帧区间。母版的固定速度预览由 <code>previews.py</code> 单独生成，普通一挥 20 帧，慢三拍每半挥 11 帧。</p>
<p><a href="v2/render_example.py">查看可运行的逐帧示例</a>　<a href="{directory}/beats.csv">成片逐拍表</a>　<a href="{directory}/index.json">查看现场落点与所用母版</a></p></details></section>'''


CONTROLS = """<script>
document.querySelectorAll('.controls').forEach(group=>{
  const img=group.closest('figure').querySelector('img');
  const loop=img.getAttribute('src'), title=img.alt;
  group.addEventListener('click',event=>{
    const button=event.target.closest('button');
    if(!button)return;
    img.src=button.hasAttribute('data-loop')?loop:button.dataset.pose;
    img.alt=button.hasAttribute('data-loop')?title:title.replace('循环动画','')+' · '+button.textContent;
    group.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
  });
});
</script>"""

