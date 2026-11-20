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

## F. Cross-movement consistency

Compare canvas/margins/fonts/type hierarchy/colors/labels/motif identities; opening pages/credits/version format; cursor/beat rules/time basis; bibliography/encoding/audio; names/numbers/durations/completeness. Shared rules do not imply identical meter, text density, motif count, or reference-page duration.

## Archive and deliver

Preserve source inventory, geometry, route, time map, motifs/sections, encoder settings, actual media metadata, bibliography/reading scope, review evidence, and unresolved issues. Frozen replay needs final adopted mappings and material assignments, not only builders. Distinguish static archive completeness from tested end-to-end recovery.

For a new copy into the cloud folder, write real bytes to a temporary sibling, flush/fsync, atomically rename, fully hash/read back, check non-dataless state, and reopen media. For regrouping already verified files on the same volume, follow the rename/identity/provider evidence exception in production-policy.md; do not unnecessarily rehydrate unchanged media. Do not deliver APFS clones or links to temporary media. Never delete the only readable export when the alleged cloud replacement is only a placeholder.

Use the current OneDrive future-delivery rule in production-policy.md. Archive completed outputs under `成片/<work-id>` and editable reconstruction materials/reacquisition records under `工程/<work-id>`, verify content and upload, then remove redundant local production copies. Follow the original-source retention rule: a documented externally downloadable dependency need not be retained as source bytes, but cannot be called offline recovery. The user is migrating existing files; do not perform that migration. Existing Dvořák locations remain historical until separately authorized for migration. Return absolute links to the actual video, covers, references, and report. State version, duration, dimensions, size, recording/edition, audio provenance, checks performed, and remaining limits. Show completed images. Do not deliver only a plan or logs.

When a required input/capability prevents the practical target, report what is complete, the difficulty, feasibility and proposed solution; preserve work and wait for the user. Do not launch dependent fixes/experiments while awaiting direction.

## Mandatory playhead and final placement (2026-11-09)

Before delivery require full-route playhead coverage, performance-derived measure times, correct page order and representative transition/ending checks. Limited isolated timing differences do not prevent delivery at the user-authorized practical standard. Persistent drift or missing modules do. Once this standard and technical checks pass, deliver the movie and all other outputs/rebuild materials to the configured OneDrive locations, then clean verified redundant local production copies; no extra approval gate is needed. On a real blocker, report and wait instead of relabeling incomplete work.
