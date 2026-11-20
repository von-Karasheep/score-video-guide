# Shared conducting gestures

Use the [gesture library and filmed examples](../assets/conducting-gestures/指挥手势.html) whenever a score guide shows a conducting gesture. The library lives under the installed skill at `assets/conducting-gestures/`. The active Op. 60 release `v2/` owns the hand, sleeve, baton, viewer orientation, tip paths, numbered landing positions and their drawing order. Each project owns its performance clock and its score-to-screen mapping. Keep a frozen copy of the used renderer and pattern files with the editable project for offline rebuilding. Maintain the masters in the skill.

## Choose by the way the music is conducted

| What the performance shows | Master | Timing for a complete bar |
|---|---|---|
| One sweep spanning a whole bar | `in-1` | One interval, including its rebound |
| Two distinct pulses | `in-2` | Two intervals; applies to simple duple or compound duple grouped 3+3 |
| Three distinct pulses | `in-3` | Three intervals |
| Four distinct pulses | `in-4` | Four intervals |
| Slow triple time with a rebound on each half-beat | `in-3-sub2` | Six intervals in the order 1, 1-and, 2, 2-and, 3, 3-and |

Use the user's Beethoven Fourth screenshots and the actual Op. 60 implementation as the visual reference. The two-beat geometry comes from the Op. 60 finale, the three-beat and divided three from its Adagio, and the one-in-a-bar path from the first movement's Allegro. The four-beat path extends the same drawing conventions. The original Op. 60 hand, cuff, moving tip, trail and the rounded card with its two text columns are rendered together in every meter. The previous Op. 125 triangle-and-polygon draft in v1 is retained only to reproduce that historical export. The [side-by-side film](../assets/conducting-gestures/v2/Op60-comparison.mp4) compares the new master with the user's real Op. 60 screenshots. The loops in the gallery are demonstration tempi. Label the written meter and unit independently of the number of gestures. For instance, two performances of 3/4 may use different masters; two different written meters conducted in two may use the same one. In changing or asymmetric meters, record the order of the groups and the durations of the actual pulses. An unequal two-pulse group can use the two-pulse master if the observed gesture order agrees.

## How to draw and replay the actual Op. 60 animation

Open the [illustrated Chinese manual](../assets/conducting-gestures/指挥手势.html#masters). Each master has a full-card loop, individually selectable landing poses and a stroke-by-stroke route in screen coordinates (origin at top left). The screenshots and loops are backed by [the Chinese motion descriptions](../assets/conducting-gestures/v2/gesture-notes.zh.json) and the numeric samples in the pinned pattern. The positions below are logical pixels.

| Master | Landing order, including the return to the next bar |
|---|---|
| One in a bar | (284,92) to the upper turn (306,17) in 53% of the interval, then back to (284,92) in 47%. Only the low point is a beat. |
| Two | (277,94) → (323,57) → (277,94). The outward arc lifts toward the right pulse; its return approaches the downbeat from the left. |
| Three | (279,94) → (326,66) → (285,34) → (279,94). Low, right, upper, then down into the next bar. |
| Four | (282,94) → (259,65) → (325,65) → (293,33) → (282,94). Low, left, right, upper and back to low. This is an extension of the Op. 60 drawing conventions. |
| Divided three | (279,94) → (287,89) → (326,66) → (334,61) → (285,34) → (293,29) → (279,94). Each principal beat makes a small rebound to its half-beat, then travels to the next principal beat. The three printed rings mark the principal beats. |

For regular two-, three- and four-beat gestures, construct each cubic from A=(x,y) to B=(u,v) with successive controls (x+4,y−23) and (u−16,v−25). Divided three retains those background guides, but its actual motion uses two cubics per beat. For M=(x+8,y−5), the A→M controls are (x−4,y−22) and (x+8,y−20). The M→B controls are (x+8,y−29) and (u−15,v−22). For one in a bar, the upward controls are (271,66), (313,30); the return controls are (301,37), (291,82). The released recipes already contain 61 sampled points per cubic. Use those samples for rendering. In a pulse interval, use fractional position on the current sample list, interpolating linearly between adjacent points. In one-in-a-bar, remap the phase separately to each branch at 0.53.

Paint the card and type, fixed pale guides and rings first. Draw the active green trail (up to 12 preceding sample intervals plus the current partial segment). At a tip position (px,py), set the hand origin to (px+26,max(14,py−39)). Draw the baton to the grip at origin+(2,−2), the green tip with white rim, then the outlined hand, finger creases and cuff. The [renderer](../assets/conducting-gestures/v2/baton.py) pins the vertices, colours, width and draw order. Apply the established 2× scale once.

The [worked Berlin example](../assets/conducting-gestures/指挥手势.html#example) replays measures 890 and 891 from the [accepted v2 beat table](../assets/conducting-gestures/videos/beethoven-op125-iv-berlin-2000-op60/beats.csv). At 30 fps, [38469,38490) and [38490,38514) give 21 and 24 frames of the same path. The [runnable example](../assets/conducting-gestures/v2/render_example.py) reads the active row on the unshifted movie clock and computes phase_from + (phase_to − phase_from) × (t − start)/(end − start). A hold uses equal phases. To reproduce the stored demonstration loops at fixed speed, use previews.py instead.

## Map to a performance

1. Read the printed meter, pickups, repeats, alternate endings and meter changes in played order. On the source clock mark visible landings and restarts with measure and beat. Check the associated attack or phrase entrance by ear; a preparation may precede the sound. In the project keep observed, audible and interpolated anchors distinguishable. Convert source times through the actual edit map, including the title cards.
2. Set the start and end of each performed stroke on the **output** clock. Align the loop's phase zero to that stroke's landing, and phase one to the next landing. Interpolate only within the locally checked tempo span. Add an audible anchor at a tempo change. A pickup starts on its actual stroke or part of a stroke. A repeat gets new times. Keep the written count advancing separately when the conductor takes a bar in one.
3. Before the first entrance show the preparation state. For a fermata, split the current stroke at the held phase, hold that exact pose for the observed interval, then resume from the same pose on the real cue. Switch masters at a checked musical boundary. Finish on the release and retain the musical decay. The prior Berlin film used text-only preparation and release; its record identifies those spans.
4. Render the [Op. 60 card](../assets/conducting-gestures/v2/baton.py) at the original logical size of 394 × 116; the renderer returns 788 × 232 RGB pixels at final 4K scale. Its Op. 60 logical origin is (818,126). Place the complete card (including the pale background and border) at (1636,252) in the 4K Beethoven frame. Keep the written meter/unit in the left column and the current beat, direction or half-beat in the middle. The right side carries the curved guides, circled beat numbers, outlined hand with cuff and moving green tip. The unified one-in-a-bar path applies to both 2/2 and 3/4. Use one stable font set and aspect ratio. In a baton-only revision preserve the original edit map, audio stream, score, captions and every region outside the card. Compare decoded frames outside that rectangular region and the audio against the approved film.
5. For a review request deliver a playable full-card loop or excerpt first. Show the supplied Op. 60 reference at equal scale and the new card beside it. For the concert check, show the actual conductor and card together in real time with the same-event audio. Re-read a contact sequence around several visible lower turning points. Use only the selected primary gestures when the conductor also makes smaller intermediate motions. Record which interval was visually checked.

```python
# Add the pinned master directory to the project import path first.
from baton import frame

phase = (output_time - this_landing) / (next_landing - this_landing)
card = frame("6/8", "in-2", stroke, phase)
canvas.paste(card, (1636, 252))
# A held pose keeps the same stroke/phase across the actual pause.
held = frame("3/4", "in-3", stroke, held_phase, mode="hold")
```

Index strokes from zero. The renderer owns the printed Chinese captions. Use the [preview builder](../assets/conducting-gestures/v2/previews.py) to regenerate loops from this same renderer. For an offline rebuild also freeze its [drawing primitives](../assets/conducting-gestures/v2/op60_drawing.py), the used JSONs and the MiSans faces.

## Archive every film

After encoding, call [archive_video](../assets/conducting-gestures/archive.py) in the canonical library. Pass a stable ID for work, movement, performance and revision, the title, event, source, timing provenance/anchor details, and the actual encoded movie. A row covers one full or partial stroke. Its fields are `measure, meter, grouping, pattern, stroke, start, end, phase_from, phase_to, mode`. The two times are output seconds. Grouping is explicit (for instance `3+3` in 6/8); `mode` is one of `conduct, pickup, hold, prepare, release`. A held stroke uses equal phases. Record text-only lead-in/release spans as metadata. The historical [Berlin finale record](../assets/conducting-gestures/videos/beethoven-op125-iv-berlin-2000/index.json) and [its beat table](../assets/conducting-gestures/videos/beethoven-op125-iv-berlin-2000/beats.csv) illustrate the archive format; use v2 for new work.

```python
from archive import archive_video

record = archive_video(video_id, metadata, rows, finished_mp4,
                       widget_crop=(x, y, width, height), version="v2")
```

Supply crop coordinates in **encoded pixels**, enclosing only the baton card. The archiver saves the beat table, verified file identities and a short, silent, actual-size clip from the encoded film for each written-meter/master combination. Every new film gets its own record under `videos/`; the shared loops remain in the version folder. It refreshes the Chinese gallery, and an identical repeat reuses the existing record. Record the returned relative directory, version and IDs in the project manifest. Recheck the encoded samples at a clear gesture, a tempo change, a meter or grouping change, a pickup and any hold/return. Look at the active written count, baton and score together. Refresh the skill's release file listing after archiving new assets.

## Add a missing pattern

First compare the conducted group order and subdivision with the gallery. If the physical path is already represented, select its ID and put the new meter, group lengths and local tempo in the beat table. If a genuinely different stroke sequence occurs, add a descriptively named JSON in `v2/patterns/` following [the three-pulse master](../assets/conducting-gestures/v2/patterns/in-3.json). Set the written-meter example, the complete curved guides and two caption lines for each gesture in the recipe. Its stroke lists are successive tip positions at equally spaced fractions of each stroke; the next stroke starts at the previous one's endpoint and the last reconnects to the first. Set the principal number positions and the label for every stroke, and record its source. Use the shared hand, viewpoint and palette. Render the WebP with `preview(key)` and rebuild the gallery with `gallery()`. Compare the numbered landings, halfway positions and loop wrap on a complete bar, then render at two different tempos and check the same phases coincide. Check the first encoded occurrence against the recording and archive it with the film.

For each new master, add its use case, visible route and one movement explanation per stroke to v2/gesture-notes.zh.json. Regenerate the Chinese gallery from gallery.py and verify that each landing control corresponds to the actual WebP frame. Keep explanatory text outside the pinned geometry JSON: adding descriptions must preserve the master hashes used by previous films.

Preserve already-used IDs and their saved geometry. An intentional revision to an existing master or to the shared drawing behaviour goes in a new version directory. Keep the prior version for existing films. A new master with a distinct ID may be added without changing existing files. Run the [library check](../assets/conducting-gestures/check.py) after adding or revising a master or a film record. It checks loop closure, numbered landings, animated previews and the consistency of old records with their pinned masters.
