# Rendering and memory diagnostics

Long duration does not inherently require a large working set. Reuse a verified whole-movement streaming pipeline and record its environment/command. Four-second chunks and a 3 GiB cap are not universal rules.

Historical Bruckner composition shifted PiP with setpts=PTS-STARTPTS+6/TB, used overlay eof_action=pass, and ran the background at 30 fps. Other experiments changed padding, inputs, and filters. Those differences are diagnostic leads, not proof of a single cause for an old large-memory run.

These diagnostic options do not authorize repeated trials: apply the immediate report-and-wait rule in [production-policy.md](production-policy.md) before attempting an uncertain recovery.

1. When authorized and necessary, fix one representative source (up to 60 s) and layout. Record FFmpeg version, input codec/resolution/rate/time_base/start_time, graph, and sampled RSS. Compare background only, PiP only, their combination, ASS added, then audio. Identify where sustained growth begins.
2. Check monotonic PTS, consistent units, trimmed origins, and finite still-image durations/rates. Do not expand all movement frames into an in-memory list.
3. Check multi-input frame synchronization, EOF, repeat-last-frame, and padding behavior. Inputs and outputs need finite ends. Investigate one input decoding while another waits; infinite apad/tpad can conceal queues.
4. Bound caches, close unused images, and write frames as generated. Inspect encoder buffers and thread counts; compare a short software-encoded control when isolating hardware behavior.
5. Compare roughly 1 min, 5 min, and full-movement memory trends as needed. A short pass does not prove long-run stability. Stop abnormal sustained growth before exhausting the machine; choose a stopping threshold from actual available resources.
6. Chunk only for measured encoder accumulation or useful recovery points. Test practical lengths such as 30–120 s and shorten only as needed. Musical timing is unchanged. Bind chunks to input fingerprints, exact clocks, and clipped subtitle/overlay events; reject stale chunks.
7. Build one continuous audio track and mux it with the video to avoid accumulating per-chunk audio delay. Verify full decode and PCM before delivery.

Check the installed FFmpeg's filter help for overlay, tpad, and apad. The [FFmpeg filter documentation](https://ffmpeg.org/ffmpeg-filters.html) is a reference; parameter availability is version-specific. These steps are a diagnostic procedure, not a claim that a particular root cause has been established.
