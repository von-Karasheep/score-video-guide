# Layered quality checks and delivery

Report passed, failed, not_checked, or estimated for the actual scope of each dimension. A single overall pass must not hide missing musical work.

## A. Materials and analysis

Check work/movement, performance, score edition/forces, complete pages, route, and claims against sources actually read. Keep form/motif terminology consistent. Complete-score identity cannot pass when only samples were obtained. Avoid unsupported assertions about every note, absolute provenance, or the conductor's physical score.

## B. Technical integrity

Check actual dimensions/aspect/rate/duration, stream codecs/channels/rate/precision, full decode return/log, continuous timestamps, missing frames/unexpected black frames/audio gaps, opening/music/decay/end-page boundaries, and subtitles if present. A decodable file need not be musically correct.

## C. PCM fidelity

Align the true musical range of source and output on the same sample grid, format, and channel order. An unprocessed path can compare sample count/hash or samplewise differences. Verify opening/end silence separately. Resampling, gain, and fades require comparison with the expected processed reference and explicit disclosure. The tested precision must cover the source precision claimed. When a previous file was already sample-compared, copy that audio on a rebuild. A millisecond delay filter is not a sample delay.

Use the precise conclusion: decoded PCM from the selected source interval matches the output. This does not prove a never-lossy master or cursor synchronization.

## D. Music synchronization

Default acceptance uses the practical, bounded checks in [production-policy.md](production-policy.md). The exhaustive attack/beat procedure in the next paragraphs is only for a separately requested precision audit; it is not a condition for delivering the default complete guide.

Use fixed-seed random checks (8–12 can be a starting set, not a guarantee) plus every major entry, exposed solo, tempo/meter change, repeat, hold, system/page change, and ending. For each, retain source/output time, occurrence/beat, expected voice/event, frame and audible excerpt, method, measured error/uncertainty, and actual listening scope.

A correct-looking screenshot is not listening approval. Separate fitted-feature checks, independent PCM diagnostics, and auditory review. Diagnose global offset, local DTW confusion, score-coordinate mistakes, and source edits before correcting. Sampling a few excerpts cannot establish whole-work note-by-note listening.

Also audit the complete attack set against the rounded frame schedule. Exclude tie continuations from new-attack counts; retain missing events, absolute-pitch/chord deficits, uncertain intervals, and absent evidence fields. Data consistency and coverage are not accuracy rates. See [symbolic alignment and reuse](symbolic-alignment-and-reuse.md).

## E. Encoded visuals

Inspect actual encoded representative frames: translated staff labels, a crop that keeps the clef and key signature, with the playhead starting at the first notehead, clear measure/meter/cursor and supported beat display, type at the relative size of the accepted Bruckner 8 movement I, a header rule clear of the credit, authentic excerpts that sit inside the motif card with the named staves complete, unobscured motif boxes with consistent colors, inactive readable legends, permanent timeline ticks/start labels in distinct theme colors, a verified section caption, with :人名 only when identified sitting between the picture and the timeline, readable nonoverflowing analysis/citations, aspect-correct same-performance PiP, and readable 3 s opening pages. A lower staff cut by the card edge fails. The 2026-11-07 Shostakovich film still has that cut; do not cite it as an approved right-hand placement. Check the form page and one bar inside a long section against the packaged baseline images and explicit policy: one card must not cover the whole zone, and the motif crop must show the named figure rather than an empty staff. Check extreme ledger notes and fermatas after cropping. Verify both work-level PNGs, 16:9 and 4:3, and that all movements reuse that pair. Inspect the actual score image, verified portrait cutout, work-level title, spelling, dimensions and thumbnail readability for each ratio. A flat-color JPEG is keyed and cropped before it is placed, and the credit stays clear of the hands.

At playback size, inspect encoded frames around form transitions. Verify that adjacent pale and filled spans are immediately distinguishable, that each divider remains visible after the fill crosses it, and that the actual form names are aligned with their start ticks. In a single full-work video, check the common clock and cumulative fill across the joins. See the [form timeline rules](layout-and-render.md#timeline-opening-and-references).

## F. Cross-movement consistency

Compare canvas/margins/fonts/type hierarchy/colors/labels/motif identities; opening pages/credits/version format; cursor/beat rules/time basis; bibliography/encoding/audio; names/numbers/durations/completeness. Shared rules do not imply identical meter, text density, motif count, or reference-page duration.

## Archive and deliver

Preserve source inventory, geometry, route, time map, motifs/sections, encoder settings, actual media metadata, bibliography/reading scope, review evidence, and unresolved issues. Frozen replay needs final adopted mappings and material assignments, not only builders. Distinguish static archive completeness from tested end-to-end recovery.

Test a portable bundle outside the original working directory. The Rome continuation bundles regenerated the adopted ASS tracks byte for byte from an independent extraction. Record that specific result, along with the archived score, maps, timing, fonts and renderer. Record source reacquisition and a full fresh render separately when either is required and performed.

Follow the [direct OneDrive delivery and relocation checks](production-policy.md#current-future-delivery-rule-onedrive-2026-11-11). Check content and current provider status separately and keep the only readable local export until both are verified. Use the documented source-retention and recovery scope. Keep cleanup of existing deliveries within the user's requested scope. Return absolute links to the actual video, covers, chapter TXT, references and report. State version, duration, dimensions, size, recording/edition, audio provenance, checks performed and remaining limits.

When a required input/capability prevents the practical target, report what is complete, the difficulty, feasibility and proposed solution; preserve work and wait for the user. Do not launch dependent fixes/experiments while awaiting direction.

## Final placement check

Before delivery check full-route playhead coverage, performance-derived measure times, page order, representative transitions and the ending. After the technical checks pass, verify that the requested movements, cover pair, chapter TXT, time indexes and technical reports sit directly together in the final work directory. Account for every expected file before reporting completion.
