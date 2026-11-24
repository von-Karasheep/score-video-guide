# Score-to-recording synchronization workbook

Optional precision workflow: apply the exhaustive event/beat/frame audits only when precision is explicitly requested or a bounded diagnostic is necessary. The default target, permitted approximation, and immediate report-and-wait rule are in [production-policy.md](production-policy.md); do not make this workbook a default completion gate.

The target is the correct score event and beat at the time it sounds. Change the display, not performance speed. Never stretch audio, reset an arbitrary metronome each measure, or distribute the total duration evenly. More work is acceptable; fabricated approval is not.

## 0. Inputs and evidence tables

Record original media and score hashes, edition/page order, audio rate, and precision target. Analyze a separate copy without changing delivery audio. Use replay/slow playback, waveform/spectrum inspection, frame stepping, and score-coordinate inspection. If actual listening or reliable alignment is unavailable, state that capability gap.

Keep separate score_events, performance_path, anchors, and reviews. Preserve evidence and unresolved state in each; OCR, filenames, and duration are not approval.

## 1. Read the score and actual route

For every system, identify page, staves, clefs, keys, meters, boundaries, and rehearsal marks. Check pickups, compound/additive meter, repeats, endings, cuts, cadenzas, and changes within a staff. Printed measures and performed occurrences are separate identities.

Determine beat unit/grouping from meter, beaming, accents, and musical context. For example, 2/2 uses a different primary unit from 4/4; 6/8 can have two primary beats and six eighth-note subdivisions. Unknown grouping remains unresolved.

Choose identifiable anchors and read their written and sounding pitch, transposition/octave, duration, and beat/subdivision. Full-work OMR is optional; the selected events themselves must be correct.

## 2. Establish coarse landmarks

Use opening, theme/solo entries, attacks after rests, tempo changes, rehearsal marks, and the ending. Locate them in this recording with pitch, rhythm, timbre, and neighboring events rather than only a large peak. Save score and audible excerpts on both sides.

CQT/chroma, reviewed symbolic data, or another score recording proposes candidates. Similar repetitions can select the wrong occurrence. Confirm order across landmarks. A PDF page duration is not a beat map.

## 3. Resolve local beats and attacks

Work in roughly 4–8 measures, narrowing to 1–2 for dense/free passages. Replay from a known attack, count against the score, and verify both ends with multiple voices; a syncopated melody can hide the downbeat.

For an audible beat attack, locate the onset in waveform/spectrum and verify instrument/event identity in context. Reverb peaks are not new attacks. A silent/tied/resting beat is inferred from surrounding confirmed events and accompaniment; retain its uncertainty and do not describe it as heard.

Check tuplets, dotted rhythms, ornaments, trills, cross-voice offsets, and rolled chords. A chord can have an onset interval rather than one physically exact instant. Preparatory conducting motions often precede sound and cannot establish the audio beat.

## 4. Locate real score positions

Record head/rest x and system/staff y in the original scan. The target is the event's printed time column, not the stem, beam, or barline. Clefs, keys, and meters occupy width before the first head. When voices have slightly different x positions, choose and consistently state the governing voice/time column; one line cannot exactly cover all asynchronous attacks.

Use one transform for every overlay:

    x_screen = x_panel + (x_scan - crop_left) * scale

Apply its y counterpart as well. Confirm a known head before and after cropping. An inferred silent beat without a printed column cannot be advertised as an exact head position.

## 5. Diagnose tempo and interpolate

Compute beat intervals, tempo using the correct beat unit, and measure durations. A sudden jump inside a steady passage is a review flag, not automatically rubato or an error to smooth away. Separate pickups, changed meters, fermatas, and free passages from normal-duration comparisons.

For orientation, a stable quarter-note tempo of 120 gives 0.5 s per quarter and 2 s per full 4/4 measure. A candidate with one unexplained 0.2 s interval needs investigation. Do not force real variations into this example.

Use linear interpolation between verified time/score anchors. Beat-only anchors support beat-level positioning; exact note-level claims require note/subdivision evidence. Holds can stop the cursor. New systems switch without a reverse scan.

In a requested event-anchored precision view, derive the playhead and beat boxes from the same performance time map. Follow printed event columns while keeping the clef and key signature visible. For default measure-linear playback, use the [measure-linear cursor rule](alignment.md#cursor-motion) and keep the independently established beat display on its musical clock. A layout revision can reuse the adopted alignment.

## 6. Review the complete route

First, follow the entire musical path against audio, checking boundaries, counts, omissions, repeats, meter changes, and ambiguity. Record actually reviewed time ranges, not just a boolean.

Second, check every motif activity change, tempo/meter transition, repeated entry, free hold, system/page switch, and ending, then fixed-seed random points in reviewed ranges. An error requires checking both sides to the nearest reliable anchors.

Third, review the encoded video with sound, not only pre-render PNG/JSON. Check time conversion, source-picture timing, and frame-rate differences through PTS. Include full attack-group/frame-label consistency using `check_event_schedule.py` where its normalized input applies.

For an explicitly requested frame-accurate audit only, the engineering target for a distinguishable attack is at most one output frame (about 33 ms at 30 fps). It is a target, not a guarantee. Preserve observable intervals for ambiguous attacks. A wrong adjacent note fails even with a small time error.

## 7. Approval boundary

Each anchor retains verification status, evidence, method, date, and uncertainty. `check_alignment.py` and `check_event_schedule.py` cannot replace listening. Their success must not turn estimated anchors into verified ones.

Real x coordinates may be uneven while beat times are uniform; varying pixel speed is then correct. Conversely, a moving time map with an unchanged score position needs a real hold or acoustic explanation.

Never announce complete precision while unresolved ranges remain. A review export can expose progress, but cannot substitute a disclaimer for the requested precision work. Keep the capability gap and remaining actions concrete; do not promise autonomous work after the turn ends.
