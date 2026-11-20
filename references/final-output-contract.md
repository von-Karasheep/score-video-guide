# Output contract and reproducibility

Read [production-policy.md](production-policy.md) first. It is the current default quality and delivery authority.

## Scope

The skill provides specifications, data conventions, checks, and visual references. Original media, scores, fonts, and FFmpeg binaries are external inputs. Verify legitimate, readable copies before use. Layout is reproducible from configuration; musical analysis, gesture interpretation, and synchronization require evidence from the actual work and performance.

## Established layout

Use the 1920×1080 logical canvas, scaled uniformly by 2 to 3840×2160 at 30 fps. Read exact regions, type sizes, colors, and opening durations from [layout.json](../assets/layout.json). Use MiSans Regular/Medium, paper background #f3f3ef, text #243a34, secondary #71817a, cursor #397f75, divider #cbd5ce.

| Area | Purpose |
|---|---|
| Header | Work then smaller movement name on an aligned baseline; recording below; motif legend at right |
| Left score | Preserve real notation, original instrument labels, verified Chinese labels, current measure/meter/beat, and cursor |
| Right analysis | Name the current material and voice concretely |
| Motif card | Authentic excerpt fitted inside the card on one coordinate scale; every staff of the named figure remains complete; distinguish a current passage from prototype recollection |
| Listening/citation | Short listening cue and a nearby source/page reference |
| Performance | Matching-performance PiP, aspect preserved; default logical box 1320,656,500,281 |
| Gesture | Evidence-based visible actions only; otherwise blank |
| Timeline | Continuous left-to-right elapsed-time color fill on a pale track; permanent section ticks and section/measure range/start-time labels; no moving arrow substitute; default output-time basis |

Do not add a header output-time counter and its isolated dash, redundant “complete score guide” slogan, or explanatory label about bright motif markings. Dividers may not cross text; the header rule sits below the credit ink. The performance caption sits between the picture and the timeline and follows the visible shot: section name alone, or 乐器：人名 / 指挥：人名 when the person's identity in this performance is verified. General views read 乐队全景. Follow the shot-caption evidence rules in layout-and-render.md. Keep score, analysis, motif, and performance together; adjust paging or content density rather than quietly deleting modules. All movements share the same design system. Type follows the explicit sizes in layout.json and the packaged Bruckner I example identified in production-policy.md; no old chat or movie is required.

The opening is identity/version/recording/edition/instrumentation for 3 s, then form overview for another 3 s. A combined work has one opening and final bibliography, preserving actual live intervals between movements. Independent movement files can have their own opening/end pages. Choose reference-page count/duration by actual reading volume, not an inherited number.

Movement count follows the score, live intervals follow the recording, and file splitting follows the user's delivery request. Do not automatically split a work or insert title/reference pages between movements and describe them as original pauses.

Deliver one English cover design for the work, in both 16:9 and 4:3. Share this pair across movements as specified in the [cover specification](cover.md). Cut people out of verified frames before composing; do not paste rectangular photographs onto the cover. Credit only the real maker. Existing work keeps its previous credit (including historical model names); revisions add software/model/date separately. Companion notes identify maker, date, and new/revised status.

## Single-page presentation and review notes

Show one actual score page at a time in the full left score area. A source video that displays two pages does not justify shrinking two pages into the established single-page layout. Split those source spreads into separate files and maintain the page sequence. Do not print source-page ranges, page arrows, or production-status messages such as pending review, unapproved beat timing, or unfinished instrument labels on the musical canvas or timeline. Put uncertainty, actual review scope, timing-estimation methods, and pending work in the reply and companion record. The same applies to production-status end cards; retain real bibliography pages. Analytical prose must discuss the music, not unfinished implementation work.

The user's 2026-11-09 correction removes on-screen workflow notices; it does not approve an unverified map. A review file keeps its review classification in its filename and records. Do not fabricate beats or exact score positions to fill unverified fields. Reuse the verified parts and explain the remaining limitations outside the video.

## Musical clocks and evidence

Declare output versus music timeline basis in configuration and notes. The default is output time for player navigation, including the 6 s opening. Track source timestamps separately. Once the first score appears, keep the playhead visible and stationary at the first sounding event until the recording actually begins that event. Only then start its movement and verified beat highlighting. The title-page boundary is not an onset anchor; see the opening-sound rule in alignment.md.

Precision anchors must contain actual time, real score coordinates, verification state, and evidence. `check_alignment.py` is a structural gate; `cursor.py` interpolates verified anchors without an equal-width fallback. `check_event_schedule.py` audits normalized candidate groups and rounded output labels without granting musical approval.

Inspect beat/measure-duration curves, stable-tempo anomalies, complete route, and encoded audiovisual excerpts. Do not smooth true performance variation or move the audio clock to match preparatory gestures. A still verifies posture; motions such as a stroke, bow direction, or arm movement require continuous same-performance evidence. Do not infer musical intention solely from an image.

Follow the synchronization workbook, applicable checks, layout recipe, render diagnostics, then layered delivery checks. Later successes do not override earlier failures.

## Rendering, preservation, and delivery

Prefer a tested streaming whole-movement pipeline. Four-second chunks and a 3 GiB limit were historical fallback choices, not universal requirements. Diagnose persistent growth before deciding on chunks.

Report source/score/analysis, technical decode, PCM, music synchronization, visuals, cross-movement consistency, and delivery independently. Unchecked items remain not_checked. The default practical measure-level deliverable is already user-authorized. Missing exact beat verification does not block it; never label it precision-approved. Failure to meet the practical floor requires immediate assessment/report and waiting for the user.

Produce locally outside cloud sync. For future production, transfer the movie, all companion outputs, editable engineering and the retained inputs plus documented source-reacquisition dependencies to the user-designated OneDrive concert workspace, following the current rule and verification/cleanup sequence in production-policy.md. Remove redundant local production copies after successful verification; existing deliveries are not automatically migrated.

Cloud-folder delivery requires real byte writes, flush/fsync, atomic rename, full SHA-256 readback, non-dataless checks, and reopening actual media. Filenames and logical sizes are insufficient. Do not use APFS clones or temporary-file symlinks as media delivery. Clean only rebuildable caches after the verified independent delivery exists; preserve unique or unresolved originals, score, data, scripts, references, and review records. Downloadable original media may be removed under the latest source-retention rule, after saving readable restoration instructions.

The 2026-11-09 filled-timeline correction applies to future renders. Do not rerender already delivered videos solely for this change. Check an encoded middle frame: the elapsed portion must form a continuous filled segment, with section ticks still visible.

## Latest mandatory display checks (2026-11-09)

Use distinct colors for structural sections and matching elapsed fills; label every displayed staff in Chinese beside its real row; explain meaningful notation at first occurrence with a brief callout or leader in vacant space. Follow [recovery and display checks](recovery-and-display-checks.md) for the registry, per-page verification and troubleshooting stop rule. Use the explicit cursor modes in [alignment](alignment.md); measure-linear progress must not be described as event-accurate notehead tracking.

## Work-level chapter TXT

Deliver one UTF-8 TXT per work and performance. Append or revise individual movement blocks in numeric order using the [chapter writer](../scripts/chapters_txt.py). Include completed movements only.

- Use times from the encoded movement, including its opening cards and the performed repeats. Keep up to ten rows per movement, including the fixed opening row. Each label fits within 16 characters and neighboring markers are at least 6 s apart. When nearby cues compete for a slot, combine the descriptions at the significant verified boundary or leave the smaller cue in the engineering index.
- Give each marker the formal position and a brief description of the music. In sonata form, use labels such as `呈示部：八六拍主部`, `呈示部：属调段落` and `展开部：附点动机变形`. For lettered forms, name the section after the letter, as in `A：谐谑曲`, `B：三声中部` and `A：谐谑曲再现`. Reuse the same letter for returning material and name the repeat or return where it helps. Follow the actual form and keep important internal entries visible.
- Keep the title and movement headings in the format shown. Put one ASCII space after each timestamp. Use full-width colons within labels and after movement headings, and full-width semicolons in the fixed opening row. Keep longer analytical notes and sources in the engineering index.

```text
【乐谱同步+分段与动机提示版】贝多芬《A大调第七交响曲》-阿巴多+BPO@2001
第一乐章：
00:00 引言；制作说明；总览
00:12 引子：全奏与双簧管
03:33 呈示部：八六拍主部
04:53 呈示部：属调段落
05:49 呈示部反复：主部
07:10 呈示部反复：属调段落
08:06 展开部：附点动机变形
10:06 再现部：主部回归
12:25 尾声：低弦与终止

第三乐章：
00:00 引言；制作说明；总览
00:07 A：谐谑曲
02:30 B：三声中部
04:24 A：谐谑曲再现
05:47 B：三声中部再现
07:44 A：谐谑曲末次再现
08:53 尾声：三声中部回响
```
