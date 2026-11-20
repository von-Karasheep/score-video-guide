"""Generate full-card animation loops from the same renderer as the production overlay."""
from pathlib import Path
from baton import ROOT, frame, pattern


def preview(key, frames_per_stroke=None):
    master=pattern(key)
    step=frames_per_stroke or (11 if key=="in-3-sub2" else 20)
    frames=[frame(master["meter_example"],key,j,k/step) for j in range(len(master["strokes"])) for k in range(step)]
    times=[round((j+1)*1000/30)-round(j*1000/30) for j in range(len(frames))]
    path=ROOT/"previews"/(key+".webp")
    path.parent.mkdir(exist_ok=True)
    frames[0].save(path,save_all=True,append_images=frames[1:],loop=0,lossless=True,duration=times,method=4)
    return path


if __name__=="__main__":
    for path in sorted((ROOT/"patterns").glob("*.json")):
        print(preview(path.stem))
