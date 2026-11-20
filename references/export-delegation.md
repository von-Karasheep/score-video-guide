# GPT-6.1 Sol export delegation

User-authorized extension, 2026-11-09; current practical acceptance, blocker handling and destinations are defined in [production-policy.md](production-policy.md). Record `export_delegation: sol` or `off` independently of preparation delegation. Use an actual GPT-6.1 Sol child with `fork_turns: none`; if unavailable, report the fallback without pretending that model ran. This skill-maintenance option does not itself start a video job.

## Responsibility boundary

The lead owns recording/edition verification, source reading, form and theme/motif analysis, measure/system geometry, instrument interpretation, score-note correspondence, performance route, onset/beat fitting, uncertain passages, and musical acceptance. These are the core work, not duties that an encoder completes afterward.

Sol may execute the supplied renderer, encode/mux, monitor progress/resource use, resume failed encoding, perform technical checks, extract inspection frames, and copy approved deliverables to the assigned work folder. It may fix purely mechanical command/path failures without changing musical or visual semantics. It must return issues involving timing, music, crops, missing voices, motif identity, or layout to the lead. Never silently change beat timing, stretch audio, omit modules, lower quality, replace the recording, or promote candidate anchors to approved ones.

## Frozen handoff

Give the worker the canonical skill path, applicable AGENTS instructions, one exclusive output directory and:

1. Recording/score identities, exact input paths and SHA-256 fingerprints.
2. Versioned, frozen measure/beat/note geometry and time maps, motif intervals, captions, analytical text, citations and review status. Unknown or unapproved fields remain explicit.
3. Renderer and environment, fonts, layout configuration, expected duration and frame rate, audio trim/delay, codec/pixel/sample formats, and approved representative frames. Supply an executable command or explicit function configuration; do not make the worker reconstruct settings from chat history.
4. Acceptance checks, final/review output classification, destination paths, and the exact disposable intermediates, if any. Protect active caches, original inputs and other workers' files. Never use a sole temporary copy for editable data.

A frozen handoff records whether it meets the default practical guide standard or is still below it. Approximate measure timing is already authorized and does not itself force an unapproved-review classification. Precision status requires its separately requested checks. A change invalidates only affected checks, which the lead must repeat before promotion. Freezing unreviewed data is not approval.

## Execution and return

Verify fingerprints and space before encoding. Run a representative composition check when the pipeline or inputs changed, then stream the full requested duration. Prefer one export worker per film; parallel films must use separate outputs and respect measured CPU/GPU/disk capacity. Do not duplicate entire videos unnecessarily. Keep checkpoints and concise per-film progress; report failure or stalled output rather than an unsupported ETA. If recovery is uncertain, stop retries and inform the lead; the lead must report difficulty/remedy/feasibility and wait for user direction.

Check full decoding, duration/frame schedule, source/output audio fidelity with the declared trim and silence offsets, streams and codecs, and representative beginning/transition/ending frames including references. Audio sample equality proves preservation, not score synchronization. A still-frame check cannot certify all note positions or all shots.

Return exact command/configuration, input fingerprints, output path/hash/size/duration/streams, logs, technical results, and extracted inspection frames. Keep musical, visual, technical and delivery acceptance separate. The lead reviews the actual encoded result for timing offsets, missing/cropped elements and consistency, then authorizes its final classification internally; this is not an extra user-confirmation ritual.

After lead acceptance, move only the completed movie to Desktop, engineering to Nutstore `工程文件/<work>/`, and other deliverables to Nutstore `最终成片/<work>/`; verify destination readback. Work remains local until complete. Do not create a cloud movie duplicate by default. Cleanup requires the existing user authorization and a precise file list, and follows successful verification; never delete unique source or final files merely to free space.
