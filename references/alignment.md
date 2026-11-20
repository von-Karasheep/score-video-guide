# Measures, beats, and score positions

Default: [complete practical score guide](production-policy.md), with limited isolated timing differences accepted. Exact-note/beat checks below apply only to an explicitly requested precision task.

## Time coordinates and identities

Keep source_time (original media), music_time (selected music), and output_time (including title pages) explicit. For a single continuous excerpt without time edits:

    source_time = source_start + music_time
    output_time = intro_seconds + music_time

The default opening is 6 s. Multiple source excerpts require a segment map, not one offset. Reference pages are outside musical progress. Treat sample rates, first-audio-sample offsets, and video PTS origins separately. Source 29.97 fps and output 30 fps do not share frame indices.

Each performed measure needs an occurrence_id, printed number, pickup/repeat identity, page/system, score boundaries, real event/beat x anchors, staff regions, meter/grouping/beat unit, start/end, alignment method, confidence, and review status. Store beat starts separately from the measure end; explicitly adapt older formats that mixed them. Six eighth notes in 6/8 do not automatically mean six primary beats. Record additive groupings only when supported.

Declare original scan pixels versus normalized coordinates. Use the same crop/scale/translation for score, cursor, motif boxes, and labels.

## Candidate routes

With matching MusicXML/MIDI, verify notes, meter, repeats, pickups, transposition, version, and missing staves. Expand the actual performance route before alignment. CQT/chroma or a reviewed symbolic/synthesized reference can supply coarse DTW candidates. Constrain drift with verified musical landmarks; check monotonicity, step sizes, collapsed passages, excessive stretching, and confusion between similar repetitions.

With only scans, read systems, measures, meters, and selected identifiable events first. OMR/OCR is unapproved input, especially for ties, dots, tuplets, clefs, bar numbers, transposition, and polyphonic layout. Use reviewed local transcription or manually established landmarks. If evidence is insufficient for beats, omit unsupported beat activity while keeping measure, meter and the performance-derived measure cursor. This default is already accepted. Do not silently downgrade a separately requested precision task; report and wait if its target is unavailable.

For a different recording, preserve applicable score/analysis data but rebuild timing and media edits. Audio-to-audio matching can propose a route only after repeat/cut/edit compatibility is checked. Old seconds, average tempo, and metronome marks cannot be transferred as verified anchors.

For symbolic semantics, multistage candidates, input binding, independent diagnostics, and frozen replay, read [symbolic alignment and reuse](symbolic-alignment-and-reuse.md).

## Cursor motion

### Waiting for the opening sound

Record the verified first musical onset in source time and convert it through the actual segment map to output time. When the score is already visible before that onset, show the cursor at the real x coordinate of the first sounding event and keep it stationary. Do not hide it, sweep through the clef/key signature, or advance it because the opening cards have ended. Beat highlighting remains inactive until the verified musical clock starts. Applause, room noise, a breath, and a conductor's preparatory gesture are not onset anchors; a genuinely soft opening or pickup must not be discarded by an arbitrary amplitude threshold.

Use the existing cursor interpolator's pre-first-anchor clamp; do not insert an earlier moving anchor. The first anchor must correspond to the verified sounding event rather than an estimated video start. Preserve source audio/video synchronization and any score-rest information separately; this display hold does not authorize trimming silence or changing the musical map. Inspect the first score frame, immediately before onset, the onset frame, and the following event. The first two cursor positions must match, and subsequent motion must follow verified anchors. This is the default for subsequent productions, including Barber. The user requested no Firebird re-export for this change (2026-11-09).


### Explicit cursor modes (user revision, 2026-11-09)

Default `cursor_mode=measure_linear`: use each performed measure's actual start/end time and its printed left/right boundaries. Interpolate x linearly for that interval. Different measures may have different durations and widths. Preserve the initial pre-onset wait; at a new system start after the clef/key-signature header, and switch systems cleanly. Sustains, tremolo and timpani rolls do not freeze this measure-progress cursor. Remove inherited event-level hold flags and collapsed internal x anchors from this mode. Do not infer equal beat times from the line's uniform pixel velocity. Beat indicators retain independently established performance times.

Optional `cursor_mode=event_anchored`, for a user request for exact note-position following: interpolate between trustworthy real event-time/x anchors. Printed spacing is not proportional to time. Local velocity may vary; do not use arbitrary easing or identical beat spacing to hide uncertain timing. A sounding roll or long note alone is not permission to freeze an entire measure. Any event-level hold needs an explicit reviewed interval and reason. Keep the initial wait distinct from musical holds.

Both modes use x(t)=x0+(x1-x0)*(t-t0)/(t1-t0) on their respective intervals, updated every frame. Measure-linear motion reports progress within a bar, not exact alignment to every engraved notehead. Neither mode validates its underlying timing merely by looking smooth. See [recovery and display checks](recovery-and-display-checks.md) for regression checks.

## Metric and motif semantics

Keep metric hierarchy, syncopation/accent/sfz, written dynamics, and measured energy separate. A conventional 4/4 hierarchy is not a loudness claim. Do not mechanically straighten swing or syncopation. Unknown beat positions stay unapproved.

Each motif has a stable ID, color, short name, authentic prototype excerpt, and source. Each occurrence records measures/beats, staff/region, transformation or fragment relationship, sounding state, confidence, and evidence. Label a prototype recollection explicitly. Compare sounding and written pitches before asserting transposed identity. A sustained event may remain active; do not highlight only its first frame. Keep boxes and letters off instrument abbreviations, clefs, notes, and dynamics.

## Evidence and precision

A still image proves what was drawn, not what sounded. Save source/output time, occurrence/beat, expected acoustic event, frame, audible neighboring excerpt, method, measured error or uncertainty, and actual listening scope. For default production use the bounded representative checks in production-policy.md. Exhaustive event/frame checks belong to an explicitly requested precision task. Correct the map, not a single screenshot.

Investigate abnormal measure/beat durations in stable tempo before attributing them to rubato. Past Scythian examples used estimated/equal-width beats and are unsuitable as precision implementations. `check_alignment.py` checks structural conditions; it does not establish that the evidence or musical correspondence is true.

## Required completion: vertical score playhead (2026-11-09)

For a requested final score video, implement a visible vertical line following the selected cursor mode and real performance clock through the entire musical route, including page/system changes. The line and any supported beat display share the same performance clock; approximate measure timings are explicitly allowed under the default standard. A page-only slideshow or a missing line is unfinished work, even when the source audio, export, and typography pass. Do not substitute a disclaimer or a review-folder name for completing this requirement.

Use short-time Fourier/CQT pitch energy, onset flux, and pitch-sequence matching as evidence alongside the actual score. Fourier bins are not instrument stems: unisons, overlapping harmonics, reverberation, and transposing instruments prevent unique voice separation. Validate salient multi-event patterns and alternative matches; retain uncertainty instead of declaring an automatic fit verified. Never assign evenly spaced printed beats, spread duration divided by bar count, or nominal metronome durations as verified timing. Resolve remaining ranges, then check encoded output against those anchors. If a capability/input gap prevents the practical floor, immediately assess, report the difficulty/remedy/feasibility, and wait for the user. Do not pursue precision experiments as an unrequested prerequisite or call approximate timings precision-verified.
