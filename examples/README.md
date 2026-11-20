# Worked exercises

Run the commands from the repository root with the environment described in the [README](../README.md).

## 1. Build a score-following video

```sh
python -B examples/rhythm_study.py
```

The exercise uses written bars 1–4. Its played order is 1, 2, 3, 4, 1, 2. There are 24 attacks in the synthesized audio. The two gray-green opening cards take 6 s. Playback then shows a stationary cursor at the first note for 0.3 s before the first sound.

1. Open `rhythm-study-output/score.png`. The two staff systems show the A and B phrases. In [the script](rhythm_study.py), `ROUTE` lists the six occurrences, `BOUNDARIES` lists their positions in body frames, and `X` contains each beat's actual x coordinate on this engraving.
2. Inspect `rhythm-study-output/alignment.json`. Compare the first and fifth entries of `bars`. Both display printed bar 1, with different `occurrence_id` and `start` values. `events[].sample` uses the source WAV clock. The frame windows in `schedule` use the encoded movie clock. Add 180 frames to the body frame index at 30 fps.
3. Play `rhythm-study-output/rhythm-study.mov`. At **00:06.30**, the first attack starts and the cursor moves on the upper staff. At **00:13.00** the cursor jumps to the lower staff. At **00:20.00** the A phrase returns to the upper staff. The inset highlights the high or low synthesized sound. The clip ends at **00:26.80**.
4. Open `rhythm-study-output/chapters.txt`. The integer timestamps are `00:06 A：交替音型`, `00:13 B：成组音型`, and `00:20 A：交替音型再现`. The fixed opening row starts at `00:00`.
5. Inspect `rhythm-study-output/qa.json`. Expect 804 H.264 frames, `24` matched attack groups, `coverage_complete: true`, and `pcm_matches: true`. The writer compares every decoded audio sample against the source WAV and the intended opening silence. `music_verified` stays `false` because the schedule checks data and the audio was synthesized from this exercise.

To see how the schedule audit catches errors, run `python -B scripts/test_event_schedule.py`. Its test cases include mismatched frame labels and grouped attacks.

## 2. Replay a real conducting excerpt

This example comes from the finale of Beethoven's Ninth Symphony, performed by Claudio Abbado and the Berliner Philharmoniker in Berlin in 2000. The [beat table](../assets/conducting-gestures/videos/beethoven-op125-iv-berlin-2000-op60/beats.csv), [source and checksums](../assets/conducting-gestures/videos/beethoven-op125-iv-berlin-2000-op60/index.json), [rendered comparison](../assets/conducting-gestures/v2/Op125-890-891.webp), and [stroke diagrams](../assets/conducting-gestures/指挥手势.html#example) are included.

```sh
python -B assets/conducting-gestures/check.py
```

Open the stroke diagrams from the local checkout in a browser. Examine bars 890 and 891. The two strokes cover frame windows [38469, 38490) and [38490, 38514), or 21 and 24 frames. Both use the same path. The renderer takes the phase and beat pattern from the active archived row on the movie clock. To see the rows, open the CSV and look up measures 890 and 891.

To render it again, supply the original font files in `assets/conducting-gestures/v2/fonts/` or, on macOS, `~/Library/Fonts/`. The [drawing module](../assets/conducting-gestures/v2/op60_drawing.py) lists the expected names. The archived preview and the asset check work with Pillow alone.

```sh
mkdir -p rhythm-study-output
(cd rhythm-study-output && python -B ../assets/conducting-gestures/v2/render_example.py)
```

The output `rhythm-study-output/Op125-890-891.webp` is a 788 × 232 silent animation with 45 frames. Compare its first frame, the change at index 21, and the last frame against the packaged comparison. The exercise reproduces the conducting card using a small archived excerpt of the timing data.

## Transfer the method to a full movement

1. Obtain the same-performance picture and audio plus the score edition. Save the provenance, clip boundaries, and page inventory together. Record the first note and recurring entries on the actual audio clock.
2. Replace the exercise's bar table with the real printed bar coordinates, playing route, and evidence-backed time anchors. Mark the first sound, page turns, transitions, and ending. Use the [workbook](../references/sync-workbook.md) to separate source and output clocks. Review a return or repeated passage against both audio and score.
3. Use the [layout recipe](../references/layout-recipe.md) and, for Beethoven, the [series profile](../references/beethoven-series.md). Prepare actual motif crops and notation explanations, set the inset to the corresponding recording, and validate one representative passage with the real fonts and score.
4. Run the project renderer over the full movement. Save its commands, score and source identities, analysis inputs and timing tables. Check opening, repeats, transitions, and ending on the encoded film. Then write its chapter TXT using the encoded output times and follow the [delivery checks](../references/quality-and-delivery.md).
