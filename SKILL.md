---
name: score-video-guide
description: "Create, analyze, or revise complete classical score-guide videos and matching covers: practical measure synchronization, verified source identity, score/motif analysis, same-performance picture-in-picture and 4K delivery. Also use when learning methods for this workflow or maintaining this skill. Concert-preview notes alone and media downloads alone use their own skills."
---

# Score Video Guide

Produce a video whose musical claims, score positions, recording times, and visual annotations can be traced to evidence. Use this skill as the basis for future study, production, and maintenance in this workflow.

For installation and a reproducible first run, see the [README](README.md). The [worked exercises](examples/README.md) cover an original score-following video and an archived conducting excerpt.

## Canonical source and language

Use the maintained checkout as SKILL_ROOT and resolve packaged resources relative to it. Point local discovery aliases at this checkout. Follow [AGENTS.md](AGENTS.md) when maintaining the skill.

Write skill instructions, references, metadata, and code comments in English. Preserve necessary source quotations, proper names, real filesystem paths, and product-facing text literals. This preference does not change the user's response language or the established output: Chinese video analysis in MiSans, English standalone covers in Minion Pro.

Read the [current production policy](references/production-policy.md) and [output contract](references/final-output-contract.md) first. They govern the practical quality standard, source identity, recovery and direct OneDrive delivery. Use the [general layout](assets/layout.json) for shared defaults. For Beethoven score guides, start with the [series profile](references/beethoven-series.md) and its [layout data](assets/beethoven-layout.json) for regions, typography, palette and timeline. Use reference frames for appearance and this recording for timing. Follow the current user's instructions when adapting inherited scripts.

Before implementing a stage, consult [Reuse-first tool selection](references/tool-selection.md) for existing skills/software, their input limits, local audit status, and required pilot checks. Do not recreate a core engine before testing a suitable maintained implementation.

## Select the relevant workflow

| Task | Read |
|---|---|
| Start, lay out or revise any Beethoven score guide, including later movements | [Beethoven series profile and musical review](references/beethoven-series.md) |
| Produce a conducting animation for any work | Use the [Op. 60 full-card masters, performance timing and per-film archive](references/conducting-gestures.md). The Beethoven 4 card in v2 is the visual standard. Preserve the outlined hand, cuff, green tip, curved guides, numbered rings and beat captions. Read the illustrated stroke-by-stroke construction and timed replay in the gesture archive before rendering. Document the route and rebound beside each new master. Fit visible landings to the recording. For a preview request, show the animation before encoding the full film. |
| Select a recording, obtain a score, research the work | [Sources and research](references/sources-and-research.md) |
| Build measure, beat, cursor, or motif mappings | [Alignment](references/alignment.md), [synchronization workbook](references/sync-workbook.md) |
| Use symbolic events, multistage candidates, independent diagnostics, or frozen snapshots | [Symbolic alignment and reuse](references/symbolic-alignment-and-reuse.md) |
| Lay out or encode the video | [Layout and rendering](references/layout-and-render.md), [layout recipe](references/layout-recipe.md) |
| Apply the two Dvořák screenshot-feedback rounds to revisions or later movements | [Requirements, remedies and acceptance evidence](references/dvorak-feedback-rounds.md) |
| Create or revise covers | [Covers](references/cover.md) |
| Diagnose memory or timestamp problems | [Render diagnostics](references/render-diagnostics.md) |
| Verify and deliver | [Quality and delivery](references/quality-and-delivery.md) |
| Review complete Dvořák production lessons, storage failures or work-folder regrouping | [Completion lessons](references/dvorak-completion-lessons.md) |

For a new work, inventory existing inputs and applicable instructions first. For a revision, inspect the actual project and change only affected parts. A request to study or update the skill does not authorize new media downloads, video rerendering, or publication. Do not reuse sources or recordings the user excluded.

## Established output defaults

Keep only the latest verified full-length export of each movement and performance. Follow the [revision cleanup and compact delivery rule](references/production-policy.md#current-future-delivery-rule-onedrive-2026-11-11).

For every completed movement, update the single work-level UTF-8 chapter TXT using the encoded movement clock. Follow the [chapter naming, spacing and formatting rules](references/final-output-contract.md#work-level-chapter-txt). Write its formal position and a short description, such as `A：谐谑曲` or `呈示部：八六拍主部`.

- Video: 3840×2160, 16:9, 30 fps. Explain any task-driven change.
- Opening: a 3 s identity/version page, followed by a separate 3 s form overview. Keep work, recording, score edition, and instrumentation information. In the body header, place the slightly smaller movement name after the work title with aligned text baselines.
- Body: MiSans Regular/Medium; full score on the left; analysis and a real-score motif card on the right; matching-performance picture-in-picture at lower right; a structural timeline below. Preserve instrument labels. Keep analysis, motif, and performance visible together. Show one score page at a time, enlarged in the established left panel. Split double-page source images into separate page assets rather than changing the video to a two-page overview. Keep production warnings, review-status banners, provisional-page-range labels, and pending-work notes out of the video; report them in the chat and companion review record. This user correction applies to future videos (2026-11-09). Unknown synchronization must remain unapproved in data and reports; removing warnings never authorizes invented timing or a claim of completion.
- The left score keeps the clef and the key signature. Starting the playhead later means the line begins on the first notehead and does not sprint across that empty header. It does not mean cropping the header away. The user corrected that misreading on 2026-11-07. From the first visible score frame until the verified first musical sound, keep that line visible and stationary at the first sounding event. Start motion only at the corresponding recording onset, never at the end of the title pages or a preparatory gesture. Do not advance beat highlighting during this waiting interval. Apply this to subsequent productions; the user explicitly excluded the existing Firebird export from this change on 2026-11-09.
- Match type with the accepted Bruckner 8 movement I on this canvas. Title, credit, staff labels, beat labels, analysis, timeline, and the performance caption share that relative size. After enlarging type, measure the ink: the header rule stays below the credit with a clear gap, and the glyphs stay out of the motif card and the timeline.
- Under the performance picture, identify the part actually visible in the current shot, changing the caption at the source-video cut. Use the actual score-part name when the shot correspondence supports it, including `第一小提琴` versus `第二小提琴` rather than generic `小提琴`; actively research featured principals/soloists and include verified names. Use `小号`, `钢琴`, `指挥`, or another verified section; add `：人名` only when that person's identity in this performance is verified. An unidentified player keeps only the section name; a general view reads `乐队全景`. Do not infer a principal's identity from seating or a current roster. Follow the shot-caption evidence rules in [layout and rendering](references/layout-and-render.md). Keep the caption above the timeline without colliding with its labels.
- The right-hand motif excerpt sits wholly inside the white card, on the same coordinate scale as the card. Every staff of the named figure stays complete, clear of the listening line and the picture. The 2026-11-07 Shostakovich film still cuts the lower staff on the card's bottom edge. The user postponed that fix. The next revision of that film starts there; the other corrections do not approve this placement. A layout correction does not reopen a finished alignment and does not authorize a listening review that was not done.
- Use one English cover design per work, shared across movements. Deliver two independently composed PNGs, 3840×2160 (16:9) and 3840×2880 (4:3). Reuse the pair for later movements. See the [cover specification](references/cover.md). Open the accepted series example first. The work title is the largest line; cut-out people overlap a readable score page. Use English, Minion Pro, and no decorative border. Do not paste a rectangular still or invent a different poster.
- Body-header correction (2026-11-10): retain a thematic legend at upper right, with first/second themes or work-appropriate identities; maker credit belongs on opening/end pages and covers. Every analytical section needs tonal status and concrete score-reading evidence; sonata guides must trace thematic/tonal opposition and return, with internal thematic divisions on the timeline. Read the detailed requirements in [production-policy.md](references/production-policy.md).
- Analysis cards follow the inner modules of the adopted form, not one card for a whole zone. The motif crop shows the figure named on that card; the staff after the piano can be empty, so check the crop. The form page states the large parts; the timeline may split a part so a returning theme stays visible. Cite a page only after reading it.
- Show the current measure, meter and cursor clearly. For subsequent videos, also include a supported current-beat indicator in the left information area; vertical arrangement is allowed. Preserve all existing left-panel information. A static meter label alone does not satisfy this beat-display request; see layout-and-render.md. Default acceptance is practical measure following, not frame-accurate note tracking. A visible, recording-synchronized vertical score playhead is a mandatory deliverable, not an optional decoration. Do not finish a requested full production by omitting it and appending a disclaimer. Complete and check the measure/time/geometry map at the practical standard before export; never draw an arbitrary line or divide the whole work into equal-duration bars. Distinguish metric hierarchy from dynamics and measured acoustic energy. Unverified beat activity must remain unverified.
- A motif keeps one letter/name/color across the Bruckner-style header chip, actual score-phrase outline, right-hand excerpt and relevant timeline labels. Inactive chips retain their own pale hue; activity requires a checked motif occurrence, not just an analytical section. Use a fixed, bounded tonal panel, a separately bounded motif card, one left-side score-page caption and a clear gap below the performance before its caption. Read the portable correction table in [production-policy.md](references/production-policy.md).
- Use the [form timeline rules](references/layout-and-render.md#timeline-opening-and-references). Choose immediately distinguishable colors for adjacent form sections and draw a visible divider at each boundary. Keep a continuous clock and cumulative fill across a single full-work export.
- Cite sources actually used, near analytical claims and in readable final reference pages. Supply full clickable references and the actual reading scope separately.
- Credit only the actual maker: `AI 辅助制作：{software} · {model}` in the Chinese video and the English equivalent on covers. Preserve previous makers' credits when revising their work; add a dated revision credit. Never prefill a particular maker in a new project. Companion notes record maker, date, and whether the work is new or revised.

## Optional preparation and export delegation

When starting video production, the lead may enable `preparation_delegation: sol` (user-authorized option added 2026-11-08); use `off` for lead-only execution. Read [Preparation delegation](references/preparation-delegation.md) before dispatch. GPT-6.1 Sol may acquire and inventory materials; the lead owns score analysis, measure segmentation, synchronization, and musical approval. This option does not start production during a skill-maintenance request. After the lead freezes reviewed musical data and layout, `export_delegation: sol` may assign encoding, technical validation and authorized delivery to GPT-6.1 Sol. Read [Export delegation](references/export-delegation.md). The lead retains musical approval; successful encoding does not establish synchronization accuracy.

## Recovery and latest production corrections

Before implementing a missing capability, and whenever blocked, read [Recovery, MIDI comparison, and display checks](references/recovery-and-display-checks.md). Search installed tools and GitHub skills or web/plugin documentation before writing another engine. Use the [blocker rule](references/production-policy.md#reuse-tools-and-stop-promptly-on-a-real-blocker) when a real obstacle prevents the requested practical standard.

For new videos, inspect each score page or displayed system for [notation that needs a Chinese explanation](references/recovery-and-display-checks.md#first-occurrence-notation-explanations), including familiar dynamics, small expression words and combinations of the two. Show the printed mark and its brief explanation at the first relevant performed occurrence. Confirm the source mark and its callout are both readable in the encoded video. Keep distinct structural colors and Chinese labels for every displayed staff. Default to the user-requested measure-linear visual cursor unless the user requests event-accurate motion; its real measure timestamps must not be replaced by equal-duration bars.

## Production and verification

1. Verify the specified performance, obtainable audio, complete score edition, instrumentation, page order, and performance route. Search the machine and public libraries for the score before asking where it is. A catalog entry is not an obtained source.
2. Research claims against the score and appropriate literature. Separate published analysis, score observations, and interpretation of this performance.
3. Maintain separate score events, geometry, performance occurrences, time maps, motifs, sections, analysis text, references, and review evidence. Start from [the project manifest](assets/project-manifest.json); unknown values remain null or not_checked.
4. Inspect representative passages covering dense notation, entries, transitions, changed meter/tempo, and the ending. Existing authorization for a full video does not create another preview-approval requirement.
5. Check the full route/page sequence and representative opening, transitions, holds and ending against the practical standard. Preserve actual review scope and localized uncertainty. Full attack-group/frame audits are optional for a separately requested precision target, not the default export gate.
6. Report source identity, analysis, decoding, PCM fidelity, musical synchronization, visual layout, cross-movement consistency, and delivery readback separately. Success in one dimension cannot approve another.
7. Deliver actual files with absolute links, format/duration/size, recording and edition identity, and remaining limitations. Do not substitute a sample or render log for a requested full video.

Use recording-derived measure anchors and real score positions. Limited isolated timing differences are accepted by the user; systematic drift or missing modules are not. Never fabricate beat precision. A complete guide meeting the documented practical floor is deliverable without a new simplification approval. If it cannot meet that floor, report and wait; do not use a disclaimer to conceal the failure. Exact-note certification applies only when separately requested.

## Workspace, tools, and authority

Produce in a persistent local directory outside cloud synchronization. Use the [OneDrive delivery and path checks](references/production-policy.md#current-future-delivery-rule-onedrive-2026-11-11). As soon as technical checks pass, put the verified movies, cover pair, work-level UTF-8 chapter TXT and viewing/verification records directly together in `成片/<work-id>/`. Put editable engineering and source-recovery records in `工程/<work-id>/`. Complete destination and upload checks before removing redundant local copies. Apply the documented input-retention and cleanup rules.

Reuse verified local media for the same upload and part. For a needed Bilibili download, use `bilibili-video-download` and follow the [mandatory direct-routing checks](references/production-policy.md#mandatory-domestic-download-routing) for the page, API, redirects and media CDN. Follow project authorization and retain credential-free evidence. Use research and citation skills where relevant. Use the image tool for generated or edited portraits and real verified notation for the score.

Use a locally tested streaming whole-movement renderer first; preserve existing successful pipelines and the tool-selection routes. Record progress, environment, finite input/output clocks, and memory trends. Four-second chunks and a 3 GiB cap are not universal rules; chunk only when measured behavior or recovery needs justify it.

Follow applicable AGENTS instructions. Prefix actual shell commands with the available rtk; omit it from user-facing code. New scripts use configuration blocks or explicit function arguments, never command-line argument parsers. Inspect inherited code before reusing its measure counts, durations, rates, meters, end pages, or approval fields.

Learning another skill does not authorize external messages, account registration, purchases, publisher access, or video publication. Do not import its approval rituals, fixed reviewers, encoding defaults, or visual template over this user's established workflow.
