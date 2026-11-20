# Optional GPT-6.1 Sol preparation

## Enable and dispatch

At the beginning of an authorized video project, record `preparation_delegation: sol` or `off` in the project manifest. The user authorizes the lead to choose `sol` for routine preparation; do not repeatedly ask permission. With `off`, the lead performs preparation too. This option changes task allocation, not quality requirements.

Use a real child agent when supported: `spawn_agent` with `model: "gpt-6.1-sol"`, `fork_turns: "none"`, and an explicit task brief. Supply the canonical skill path, project path, specified performance URL, movement scope, excluded materials, download preferences, applicable AGENTS instructions, and permitted output paths. Do not assume the child inherited context. If model selection or child agents are unavailable, say so and use lead-only preparation; never claim a particular model ran without evidence.

The user identified `codex://threads/01a1a50f-6727-76e1-887b-eab2eebcac43` (video preparation / 6.1 Sol) as an alternative place to perform preparation. Inspect its current status before using it. An existing user chat is not a child agent: use the host's thread messaging tools for an explicitly scoped preparation assignment when appropriate, and verify its actual model if available. Its title alone is not proof of its model. Do not create a new user-owned chat, reconfigure that chat, or send it duplicate work merely because this option exists. Select one execution route for each assignment.

## Sol's permitted preparation

- Search local files and public sources for the correct full orchestral score; download accessible candidates; record edition, instrumentation, publisher, page count, page order, source URL, access date and file hash. Distinguish complete score, sample, reduction and catalog-only entry. Uncertain identity stays uncertain.
- Download the specified performance using the installed download skill. Mainland downloads must bypass Clash, including system/TUN routing. Work in the assigned local directory, outside cloud sync. Search for lossless audio and clean same-event footage; identify the event from reliable information, not mandatory audio/frame matching. Report missing/conflicting sources to the lead rather than accepting a fallback. Record actual codecs, sample rate, bit depth where known, dimensions, duration and provenance. Never infer lossless history from a file extension. Authentication and paid access retain their normal authorization requirements.
- Find literature and obtain accessible documents; inventory bibliographic metadata and relevant candidate pages without presenting an unreviewed interpretation as fact.
- Perform deterministic preparation: file inventory, hash calculation, media probing, PDF page rendering, and documented corruption/missing-page checks.

Do not delegate musical analysis, theme/motif identification, score-to-performance correspondence, measure boundaries or numbering, beat segmentation, note/attack interpretation, synchronization fitting or approval to the preparation worker. OMR or model outputs, if separately requested by the lead as mechanical processing, remain raw candidates; they do not constitute segmentation or analysis.

## Handoff and lead takeover

Use project-local `素材/待核验/` or another explicitly assigned staging directory. Give each worker exclusive outputs. Do not edit final videos, approved timing maps, shared skill files, or another worker's files; do not clean up source material or overwrite unique files.

Return one compact handoff containing:

1. Absolute paths and source URLs for every obtained file, sizes and SHA-256 hashes.
2. Recording identity evidence and actual media metadata.
3. Score edition/instrumentation evidence, completeness and page-order findings, plus unresolved doubts.
4. Literature metadata and available full-text paths; distinguish publisher publication, thesis, preprint and web note.
5. Failed or blocked acquisitions, remaining alternatives, and exact work performed. Do not report a search result as a downloaded file.

The lead reads the handoff and opens representative score pages, edition/contents pages, media metadata and identity evidence. Reject or resolve wrong versions and incomplete sources before dependent analysis. Acquisition completion is not musical approval. The lead then performs the score analysis, measure/system segmentation, actual note-position mapping, onset and beat alignment, independent diagnostics, visual inspection, and final synchronization decisions under the existing alignment and delivery rules. Waiting time is not verification. The lead may continue independent planning while acquisition runs, but must not build musical conclusions from unchecked materials.

Record who acquired, who checked, model identity when known, and unresolved fields separately. A failed acquisition does not justify invented data or relaxed synchronization thresholds. Limit parallel downloads and PDF rendering according to actual resource use; avoid multiple agents racing on the same files.

## Later export work

Preparation restrictions apply to the preparation assignment. A separate [export assignment](export-delegation.md) may authorize Sol to render, validate technically and archive frozen inputs. It does not transfer musical analysis or synchronization approval.
