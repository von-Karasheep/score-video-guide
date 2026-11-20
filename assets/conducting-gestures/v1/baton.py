"""Shared ASS baton geometry. Distances are logical pixels, times are output seconds."""
import json
import math
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORIGIN = (1078, 130)
SHAFT = ("#203830", "m 0 0 l 24 -26 25 -24 2 2", 4)
HAND = ("#C7B49F", "m 22 -25 l 24 -30 32 -33 37 -29 40 -26 37 -22 31 -22 27 -20 23 -21", 5)
CUFF = ("#486959", "m 37 -29 l 42 -29 46 -25 41 -21 36 -23", 5)
GUIDE_INK = "#BECCC1"
NUMBER_INK = "#86998A"


@lru_cache
def pattern(key):
    if not key or Path(key).name != key:
        raise ValueError("Expected a pattern ID")
    return json.loads((ROOT / "patterns" / f"{key}.json").read_text())


def position(key, stroke, phase, origin=ORIGIN):
    segments = pattern(key)["strokes"]
    if not 0 <= stroke < len(segments) or not 0 <= phase <= 1:
        raise ValueError("Stroke or phase outside the master")
    points = segments[stroke]
    step = phase * (len(points) - 1)
    i = min(int(step), len(points) - 2)
    left, right = points[i:i + 2]
    return tuple(o + a + (b - a) * (step - i) for o, a, b in zip(origin, left, right))


def guides(key, origin=ORIGIN):
    return [(origin[0] + x, origin[1] + y) for x, y in pattern(key)["number_positions"]]


def draw_motion(poly, key, stroke, start, end, origin=ORIGIN, phases=(0.0, 1.0)):
    """Emit the shared baton into an ASS polygon sink. Equal phases hold one pose."""
    first, last = phases
    if not (math.isfinite(start) and math.isfinite(end) and start < end and 0 <= first <= last <= 1):
        raise ValueError("Invalid time or phase interval")
    steps = len(pattern(key)["strokes"][stroke]) - 1
    if first == last:
        x, y = position(key, stroke, first, origin)
        spans = [(start, end, rf"\pos({x:.2f},{y:.2f})")]
    else:
        phases = [first, *(j / steps for j in range(1, steps) if first < j / steps < last), last]
        spans = []
        for a, b in zip(phases, phases[1:]):
            x, y = position(key, stroke, a, origin)
            u, v = position(key, stroke, b, origin)
            one = start + (end - start) * (a - first) / (last - first)
            two = start + (end - start) * (b - first) / (last - first)
            spans.append((one, two, rf"\move({x:.2f},{y:.2f},{u:.2f},{v:.2f})"))
    for a, b, move in spans:
        for colour, path, layer in (SHAFT, HAND, CUFF):
            poly(a, b, 0, 0, path, colour, move, layer)


def draw_guides(line, text, key, start, end, origin=ORIGIN):
    points = guides(key, origin)
    for i, (x, y) in enumerate(points):
        u, v = points[(i + 1) % len(points)]
        if len(points) > 1:
            line(start, end, x, y, u - x, v - y, GUIDE_INK, 1, 1)
        text(start, end, x, y, str(i + 1), 14, NUMBER_INK, 5, layer=2)
