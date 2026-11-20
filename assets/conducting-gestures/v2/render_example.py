"""Rebuild a silent full-card excerpt from archived rows at the movie frame rate."""
from bisect import bisect_right
from pathlib import Path
import csv
from baton import frame

HERE = Path(__file__).resolve().parent
BERLIN_BEATS = HERE.parent / "videos/beethoven-op125-iv-berlin-2000-op60/beats.csv"


def render_excerpt(table, first_frame, stop_frame, destination, fps=30):
    with Path(table).open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    starts = [float(row["start"]) for row in rows]
    frames = []
    for n in range(first_frame, stop_frame):
        t = n / fps
        index = bisect_right(starts, t + 1e-8) - 1
        if index < 0 or t >= float(rows[index]["end"]) + 1e-8:
            raise ValueError(f"Frame {n} has no archived stroke")
        row = rows[index]
        elapsed = min(1, max(0, (t - starts[index]) / (float(row["end"]) - starts[index])))
        p, q = float(row["phase_from"]), float(row["phase_to"])
        phase = round(p + (q-p)*elapsed, 6)
        frames.append(frame(row["meter"], row["pattern"], int(row["stroke"]), phase, row["mode"]))
    if not frames:
        raise ValueError("The excerpt must include at least one frame")
    durations = [round((j+1)*1000/fps)-round(j*1000/fps) for j in range(len(frames))]
    frames[0].save(destination, format="WEBP", save_all=True, append_images=frames[1:],
                   duration=durations, lossless=True, loop=0, method=4)


if __name__ == "__main__":
    render_excerpt(BERLIN_BEATS, 38469, 38514, Path.cwd()/"Op125-890-891.webp")

