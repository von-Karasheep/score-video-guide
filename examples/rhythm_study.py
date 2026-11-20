"""Build and verify a small score-following lesson from an original rhythm study."""

from bisect import bisect_right
from hashlib import sha256
from pathlib import Path
import json
import math
import shutil
import struct
import subprocess
import sys
import wave

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from chapters_txt import FIRST, update_work
from check_alignment import check
from check_event_schedule import audit
from cursor import position

FPS = 30
RATE = 48_000
INTRO = 6
SIZE = (960, 540)
OUTPUT = Path.cwd() / "rhythm-study-output"
ROUTE = (0, 1, 2, 3, 0, 1)
BOUNDARIES = (9, 105, 210, 306, 420, 516, 624)  # Body frame clock, with initial room time.
SOUNDS = ((0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 1, 0), (1, 0, 1, 1))
X = ((145, 174, 245, 291), (353, 408, 463, 532),
     (145, 215, 255, 303), (361, 406, 473, 536))
BARS = ((114, 320), (320, 568), (114, 332), (332, 568))
STAFF_Y = (188, 334)
INK, BG, GREEN = "#243a33", "#eef3ef", "#256654"
A, B = "#4b879c", "#a77a57"
EVIDENCE = "Authored notation coordinates and synthesized PCM attack samples."


def plan():
    bars, attacks, windows = [], [], []
    for i, printed in enumerate(ROUTE):
        start, end = BOUNDARIES[i:i + 2]
        occurrence = f"occ-{i + 1}"
        system = printed // 2
        left, right = BARS[printed]
        beats = []
        for j, (x, sound) in enumerate(zip(X[printed], SOUNDS[printed], strict=True)):
            sample = (start * 4 + (end - start) * j) * (RATE // FPS) // 4
            beats.append(dict(time=sample / RATE, x=x, system=system,
                              verified=True, evidence=EVIDENCE))
            attacks.append(dict(event_id=f"{occurrence}-beat-{j + 1}", kind="attack",
                                sample=sample, occurrence_id=occurrence, system_id=system,
                                sound=sound, evidence=EVIDENCE))
        bars.append(dict(printed_bar=printed + 1, occurrence_id=occurrence,
                         start=start / FPS, end=end / FPS, left=left, right=right,
                         position_method="score_anchors", beats=beats))
        windows.append(dict(start_frame=INTRO * FPS + start, end_frame=INTRO * FPS + end,
                            occurrence_id=occurrence, system_id=system))
    return bars, attacks, windows


def render_score():
    page = Image.new("RGB", (582, 374), "white")
    draw = ImageDraw.Draw(page)
    draw.text((20, 14), "Rhythm study  /  two percussion sounds", font=ImageFont.load_default(size=21), fill=INK)
    draw.text((20, 44), "Upper notes = high. Lower notes = low. Play A, B, then A.", font=ImageFont.load_default(size=15), fill=INK)
    for system, page_y in enumerate(STAFF_Y):
        y = page_y - 98
        draw.text((20, y-25), "A" if system == 0 else "B", font=ImageFont.load_default(size=21), fill=A if system == 0 else B)
        for line in range(5):
            draw.line((20, y+8*line, 568, y+8*line), fill=INK)
        for offset in (0, 6):
            draw.rectangle((53+offset, y+6, 55+offset, y+26), fill=INK)
        for digit_y in (y-2, y+14):
            draw.text((75, digit_y), "4", font=ImageFont.load_default(size=17), fill=INK)
        for printed in range(system*2, system*2+2):
            left, right = BARS[printed]
            draw.line((right, y, right, y+32), fill=INK, width=2)
            draw.text((left+1, y-21), str(printed+1), font=ImageFont.load_default(size=12), fill=INK)
            for x, sound in zip(X[printed], SOUNDS[printed], strict=True):
                ny = y + (8 if sound else 24)
                draw.ellipse((x-6, ny-4, x+5, ny+4), fill=INK)
                draw.line((x+5, ny, x+5, ny-26), fill=INK, width=2)
    return page


def text(draw, xy, label, size=16, color=INK):
    draw.text(xy, label, font=ImageFont.load_default(size=size), fill=color)


def scene_base(page):
    scene = Image.new("RGB", SIZE, BG)
    draw = ImageDraw.Draw(scene)
    text(draw, (20, 18), "Rhythm study", 32)
    text(draw, (20, 63), "Original exercise for two percussion sounds", 16)
    scene.paste(page, (20, 98))
    draw.rounded_rectangle((620, 98, 940, 304), 12, fill="white")
    draw.rounded_rectangle((620, 320, 940, 470), 12, fill="white")
    text(draw, (637, 332), "Synthesized audio", 20)
    text(draw, (637, 361), "Sound active at this beat", 15)
    return scene


def title_cards():
    cards = []
    for title, detail in (
        ("Rhythm study", "Original teaching score  /  synthesized audio  /  4/4"),
        ("Form overview", "A  Alternating sounds   /   B  Grouped sounds   /   A  Return"),
    ):
        image = Image.new("RGB", SIZE, BG)
        draw = ImageDraw.Draw(image)
        draw.rectangle((60, 183, 122, 187), fill=GREEN)
        text(draw, (60, 210), title, 52)
        text(draw, (62, 295), detail, 23)
        cards.append(image)
    return cards


def frame(base, page, cards, bars, anchors, starts, n):
    if n < INTRO * FPS:
        return cards[n // (3 * FPS)]
    t = (n - INTRO * FPS) / FPS
    occurrence = max(0, bisect_right(starts, t) - 1)
    bar = bars[occurrence]
    printed = bar["printed_bar"] - 1
    system, x = position(t, anchors)
    beat = bisect_right([q["time"] for q in bar["beats"]], t) - 1
    image = base.copy()
    draw = ImageDraw.Draw(image)
    y = STAFF_Y[system]
    draw.line((20+x, y-32, 20+x, y+46), fill=GREEN, width=2)
    subtitle = ("A  Alternating sounds" if occurrence < 2 else
                "B  Grouped sounds" if occurrence < 4 else "A  Return")
    listening_cue = ("Four alternating hits open the phrase." if occurrence < 2 else
                     "Three high hits introduce the contrast." if occurrence < 4 else
                     "Bars 1–2 return on the first staff.")
    color = B if system else A
    text(draw, (637, 113), subtitle, 22, color)
    text(draw, (637, 147), listening_cue, 15)
    motif_y = STAFF_Y[system] - 98
    motif = page.crop((114, motif_y-24, 312, motif_y+46))
    image.paste(motif, (665, 195))
    text(draw, (635, 65), f"Bar {printed + 1}   |   4/4   |   Beat {beat + 1 if beat >= 0 else '-'}", 18)
    for sound, label in enumerate(("Low", "High")):
        left = 637 + sound*133
        active = beat >= 0 and SOUNDS[printed][beat] == sound
        draw.rounded_rectangle((left, 392, left+112, 438), 8, fill=GREEN if active else BG)
        text(draw, (left+17, 403), label, 18, "white" if active else INK)
    segment_edges = [20 + int(920 * q / BOUNDARIES[-1]) for q in (0, BOUNDARIES[2], BOUNDARIES[4], BOUNDARIES[-1])]
    for i, (left, right) in enumerate(zip(segment_edges, segment_edges[1:])):
        draw.rectangle((left, 487, right-2, 495), fill=B if i == 1 else A)
        text(draw, (left+1, 506), ("A  Alternating", "B  Grouped", "A  Return")[i], 14)
    px = 20 + 920*t/(BOUNDARIES[-1]/FPS)
    draw.line((px, 483, px, 501), fill=INK, width=3)
    return image


def make_audio(path, attacks):
    pcm = bytearray(2 * BOUNDARIES[-1] * (RATE // FPS))
    tones = []
    for hz in (355, 610):
        samples = [round(11_000 * math.cos(2*math.pi*hz*i/RATE) * math.exp(-28*i/RATE))
                   for i in range(RATE//4)]
        tones.append(struct.pack(f"<{len(samples)}h", *samples))
    for event in attacks:
        start = 2*event["sample"]
        tone = tones[event["sound"]]
        pcm[start:start+len(tone)] = tone
    with wave.open(str(path), "wb") as output:
        output.setparams((1, 2, RATE, 0, "NONE", "not compressed"))
        output.writeframes(pcm)
    return bytes(pcm)


def build(destination=OUTPUT):
    destination = Path(destination)
    for binary in ("ffmpeg", "ffprobe"):
        if not shutil.which(binary):
            raise RuntimeError(f"{binary} must be on PATH")
    destination.mkdir(parents=True, exist_ok=True)
    bars, attacks, windows = plan()
    alignment = check(bars)
    schedule_audit = audit(attacks, windows, sample_rate=RATE, fps=FPS, intro_samples=INTRO*RATE)
    if not alignment["structural_pass"] or not schedule_audit["structural_pass"] or not schedule_audit["coverage_complete"]:
        raise RuntimeError((alignment, schedule_audit))

    page = render_score()
    page.save(destination / "score.png")
    body_audio = destination / "source.wav"
    pcm = make_audio(body_audio, attacks)
    movie = destination / "rhythm-study.mov"
    anchors = [beat for bar in bars for beat in bar["beats"]]
    starts = [bar["start"] for bar in bars]
    base, cards = scene_base(page), title_cards()
    frame_total = INTRO*FPS + BOUNDARIES[-1]
    command = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pixel_format", "rgb24",
               "-video_size", f"{SIZE[0]}x{SIZE[1]}", "-framerate", str(FPS), "-i", "-",
               "-i", str(body_audio), "-af", f"adelay={INTRO*1_000}:all=1",
               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast",
               "-c:a", "pcm_s16le", "-movflags", "+faststart", str(movie)]
    with subprocess.Popen(command, stdin=subprocess.PIPE) as encoder:
        for n in range(frame_total):
            encoder.stdin.write(frame(base, page, cards, bars, anchors, starts, n).tobytes())
        encoder.stdin.close()
        if encoder.wait():
            raise RuntimeError("FFmpeg did not finish the training encode")

    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "14", "-i", str(movie),
                    "-frames:v", "1", "-update", "1", str(destination/"preview.png")], check=True)
    decoded = subprocess.check_output(["ffmpeg", "-v", "error", "-i", str(movie),
                                      "-map", "0:a:0", "-f", "s16le", "-"])
    if decoded != bytes(2*INTRO*RATE) + pcm:
        raise RuntimeError("Decoded PCM differs from the synthesized source plus opening silence")
    record = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
                           "-show_entries", "stream=width,height,r_frame_rate,nb_frames,codec_name",
                           "-of", "json", str(movie)]))["streams"][0]
    if (record["codec_name"], record["width"], record["height"], record["r_frame_rate"], int(record["nb_frames"])) != (
        "h264", *SIZE, f"{FPS}/1", frame_total
    ):
        raise RuntimeError(f"Unexpected video stream: {record}")
    times = [INTRO + BOUNDARIES[i] // FPS for i in (0, 2, 4)]
    rows = [f"{t//60:02d}:{t%60:02d} {label}" for t, label in zip(
        times, ("A：交替音型", "B：成组音型", "A：交替音型再现"), strict=True)]
    update_work(destination / "chapters.txt", "原创节奏练习", "二音色三段式", "合成音频", "DEMO", 2026, 1, [FIRST, *rows])
    (destination/"alignment.json").write_text(json.dumps(
        dict(bars=bars, events=attacks, schedule=windows, intro_seconds=INTRO, sample_rate=RATE),
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (destination/"qa.json").write_text(json.dumps(dict(
        alignment=alignment, schedule_audit=schedule_audit, video=record, decoded_pcm_sha256=sha256(decoded).hexdigest(),
        frames=frame_total, pcm_matches=True), indent=2) + "\n", encoding="utf-8")
    print(f"{movie} · {frame_total} frames · {len(attacks)} authored attacks · decoded PCM matches")
    return destination


if __name__ == "__main__":
    build()
