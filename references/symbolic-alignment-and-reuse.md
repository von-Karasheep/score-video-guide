# Symbolic events, layered alignment, and frozen reuse

Optional precision workflow: apply the exhaustive event/beat/frame audits only when precision is explicitly requested or a bounded diagnostic is necessary. The default target, permitted approximation, and immediate report-and-wait rule are in [production-policy.md](production-policy.md); do not make this workbook a default completion gate.

Use this reference when establishing or revising precision synchronization, together with the actual-listening workflow in [the workbook](sync-workbook.md). The original score, specified performance, and this skill's approved design remain authoritative. Use trustworthy MusicXML/MXL when available; scans can use reviewed local transcription without forcing an XML acquisition merely to run an algorithm.

## 1. Musical semantics before fitting

- Represent score positions/durations as rational quarter-note units. Read divisions, backup/forward, chord, voice/staff, dots, and tuplet durations correctly; XML element order is not necessarily musical time.
- Preserve source_id, source_measure, occurrence_id, and event_id. Repeat expansion creates distinct performed events that still refer to the original notation. Never deduplicate the route by printed measure number.
- Separate written from sounding pitch. Check transposition, ottava, octave-transposing instruments, mid-staff clef/key changes, and accidentals. OMR beam/clef/flag false heads require image review before fitting.
- Distinguish attacks, tie continuations, ornaments, rests, cue notes, and hidden auxiliary events. Tie-stop does not add an attack. A chord's attack set contains only notes actually rearticulated at that moment. Visibility alone does not determine performance identity.
- Preserve ornament ownership, voice, source order, and evidence. Known before/after ownership does not establish an exact onset. Trill endings, stolen time, and masked ornaments need separate evidence, not a fixed millisecond placeholder.
- With native engraving, bind source events to native SVG objects and check them against PDF. With scans, retain real image/pixel geometry. Symbolic parsing does not authorize an unreviewed replacement engraving.

## 2. Input identity and caches

Bind candidates, feature caches, and reviews to hashes of original/revised score, event table, geometry, expanded route, original recording, and actual prepared PCM. Also retain crop bounds, sample rate/count, channels, precision, and feature version. A matching title, duration, or matrix shape does not establish identity.

Save clocks in the prepared PCM's integer sample domain, with explicit conversion to original source PTS and output time. Retain trimming/resampling recipes. Changed inputs invalidate affected caches and reviews; editing a hash does not renew musical review.

An identity-matched previous candidate can be a search corridor, not inherited approval. New recordings require new candidates. Approved frozen replay and fresh analysis are different tasks.

## 3. Optional multistage candidate strategy

1. Extract full-range and low/middle/high register features to reduce octave confusion. Combine channel spectra by power where appropriate rather than averaging potentially opposite-phase waveforms. Analysis processing does not alter delivery audio.
2. Establish a coarse route, then use state-plus-attack evidence for dense DTW within a recorded corridor. Save resolution, steps, real memory budget, and connected backtracking. Do not interpolate across a broken path and call it successful.
3. Jointly select an ordered chain of attack-pitch groups using neighboring sequence evidence and local route slopes. Do not independently snap each note to the nearest/strongest peak or use pitch classes as a substitute for absolute pitch.
4. Estimate tempo priors separately across source tempo boundaries. Inspect corridor-edge contact, step saturation, collapsed segments, and competing paths. If justified, create a new wider-corridor candidate between at least two independently checked boundaries. Put parameters in configuration/functions, not an imported CLI parser.
5. Propose the first attack using expected pitches, ambient sound, and actual onset evidence; neither file zero nor a coarse-DTW endpoint is the first note by definition. Separate last attack, acoustic decay, ordinary rest, fermata rest, and file tail.
6. Retain coarse, dense, and ordered-chain candidates and their differences. A local correction preserves nearest approved boundary samples and data outside its justified open interval. Reproject affected events/motifs/labels. Conflicting boundaries require review, not silent adjustment.

Upstream examples such as 24 kHz analysis, 10 ms feature hops, and particular cost weights are starting implementations, not universal accuracy guarantees. This skill documents the approach; it does not claim that the upstream full alignment engine has been ported and production-tested here.

## 4. Independent diagnostics and held-out evidence

Fitting features cannot also establish independent accuracy. Retain every attack node's residual, missing peak, candidate change, and duplicate detection, then inspect suspect continuous sequences using raw PCM separately from the fitted cache.

- Fundamental bandpass/Hilbert-envelope positive changes can support a hypothesis. Record filters, smoothing, windows, and edge effects. A peak in a mixture is not an isolated instrument's physical onset truth.
- Competing neighboring pitches can be jointly fitted with sine/cosine components, retaining the matrix condition number. Tuning, vibrato, harmonics, and unison doubling can remain ambiguous.
- Compare a sequence's common shift as well as individual outliers. A strong single peak or threshold residual cannot justify moving an entire beat map.
- Tag fitting/locked landmarks as fit; evaluate accuracy with separate holdout evidence. Keep actual listening, raw-PCM diagnostics, fitted-feature self-checks, and encoded-frame inspection distinct.

## 5. Full attack/frame-label audit

Import `audit` from `scripts/check_event_schedule.py`. Its inputs are:

- events: event_id, occurrence_id, and kind. sample is an integer position in prepared musical PCM, or null when unknown. Kinds are attack, grace, continuation, rest, and cue. Optional fields include expected_pitches/detected_pitches (absolute sounding MIDI integers), system_id, evidence, anchor_method, and onset_interval_samples.
- schedule: occurrence_id, start_frame, end_frame as half-open output-frame windows, optionally system_id. Use the actual rounded frame schedule, not idealized pre-rounding seconds.
- sample_rate, fps, and intro_samples. Frame rate may be an integer or rational string such as 30000/1001. The opening offset uses the musical PCM sample rate.

Group simultaneous attacks at their governing score position. List only rearticulated pitches, and retain repeat occurrences separately. The checker inspects the first output frame not earlier than each candidate onset and reports wrong measure/system labels, missing attacks, absolute-pitch/chord deficits, uncertainty wider than one frame, missing evidence fields, and continuations incorrectly counted as physical attacks.

Example call: `audit(events, schedule, sample_rate=48000, fps=30, intro_samples=288000)`. These numbers only illustrate a 6 s opening. The report always has music_verified=false. Zero label conflicts, complete candidate coverage, or synthetic test success cannot establish acoustic synchronization.

## 6. Frozen replay and material identity

Archive the actual adopted revised score, geometry, final clock, route, structure, per-event material assignments, labels, cover recipe, and font/runtime fingerprints. Large original media may remain external with precise hashes, specifications, and acquisition instructions. Builders alone do not replace final human decisions.

- Verify source and frozen data, then replay the saved geometry/clock. Do not automatically re-engrave or realign over an approved snapshot.
- Record static completeness, restore execution, full render, and acoustic validation separately. An unexecuted restore is not proven one-command reproducibility. A missing final material map cannot be replaced by an approximate reconstruction claimed as the original.
- Material identity, sounding activity, cursor, and voice colors are distinct. Restore the material base color after an activity highlight. Save event membership and prototype/variant relationships, not only a palette.
- If a vocal project needs it, consider full phrase chains and stable lyric slots. Do not impose vocal panels, whole-staff tinting, or a second navigation level on every instrumental work.

## Sources and adoption limits

Studied on 2026-11-05 at fixed revisions:

- [score-sync-video, ac112f87800a](https://github.com/tofucurd/score-sync-video/tree/ac112f87800af9ffb244416d6d72989a2792c412): entry skill; alignment, advanced-alignment, score-and-structure, project, reference-packs, presentation-layers, delivery, validation records; and score.py, alignment_pipeline.py, refinement_graces.py, refinement_diagnostics.py, bindings.py.
- [music-score-guide-archive, cab0b9cacada](https://github.com/tofucurd/music-score-guide-archive/tree/cab0b9cacada7f23dacd33495115e40e3125e790): root and Beethoven VII/IX/Mahler IX project descriptions, Beethoven VII configuration/source/delivery records, and Mahler IX restore inventory. Complete frozen datasets were not downloaded.

The archive explicitly reports no fresh end-to-end reproduction in that release; Mahler IX also lacks its final display-material map. Treat these as documented engineering examples, not independent accuracy proof.

Adopt the general methods and preservation principles. Do not inherit work-specific anchors, review approvals, 60 fps, Source Han Serif, a fixed-blue-line scrolling layout, HEVC 4:4:4, removal of analysis modules, mandatory three-agent review, repeated user confirmation, or a fixed disk threshold. This skill's output and existing user authorization govern production.

Upstream code/original documentation is MIT, Copyright 2026 tofucurd. This is an adapted methodological summary; the new event-schedule checker does not copy the upstream alignment implementation. Fonts, scores, and recordings retain their separate rights.
