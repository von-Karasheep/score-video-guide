# Layout, encoding, and performance PiP

## Visual hierarchy

Share one design configuration across movements: work/movement and legend above; clear score left; concise analysis and motif comparison right; structural timeline below; matching-performance PiP at lower right. Keep analysis, motif, and PiP visible together.

Keep the body upper-right thematic legend; do not fill that region with maker credit. Place tonal status and concrete score-reading evidence between analytical prose and the authentic motif. Reserve readable height for all three, shortening prose before shrinking notation. See the 2026-11-10 thematic/tonal requirements in production-policy.md.

The tonal panel has fixed bounds and a visible top/bottom boundary, followed by a separately bounded authentic motif card. Keep the same boundaries throughout a movement. Show score-page metadata once at the left, never again under the performance. The performance caption has its own row below the image, at least 12 logical px from image to glyph ink and clear of the timeline. See the correction table in production-policy.md and the current numeric regions in assets/layout.json.

Use Bruckner-style theme chips (letter, name and identity color), matching thin boxes and tags at actual score phrases, and matching right-hand excerpts. Pale inactive chips keep their own hue. Activation comes from a checked motif occurrence, not the current prose card's theme field; a prototype recollection does not activate a score box. Keep tags in vacant margins rather than covering staff names. Read the occurrence schema and visual checks in production-policy.md.

Keep the clef and the key signature in the picture. Start the playhead at the first notehead so it does not sprint across that header. A request to start the line later, or to keep the line off the empty header, is only about the playhead. Do not crop the staff header out to achieve it. The user had to correct that misreading on 2026-11-07.

Compare rendered type with assets/layout.json and the packaged Bruckner I contact sheet linked in production-policy.md before delivery; the original film is not required. If the title, credit, staff labels, beat labels, analysis, timeline, or performance caption is visibly smaller, raise it to that relative hierarchy. Measure glyph ink afterward. The header rule goes below the credit with a clear gap; a text anchor is not the bottom of the glyphs. Larger type must stay out of the motif card and the timeline.

Place the motif excerpt inside the white card, using one scale for the card rectangle and the paste. The named figure's staves, noteheads, and ledger lines stay complete, with padding inside the card and a gap above the listening line. A crop that hangs out of the card, or a vertical slot whose height is not in the same pixels as the image, fails. Set vertical crop margins per actual staff/page: retain that part’s dynamics and expression text without admitting a severed fragment of the adjacent staff. Increasing padding for one espressivo marking must not enlarge every violin excerpt. On 2026-11-07 the Shostakovich right-hand card still cut off the lower staff. That film was not rerendered after the user postponed the fix. Check this card on the next revision before encoding.

Add the translated staff labels beside the crop after checking the actual staves; do not copy a preceding page's omitted voices. Keep motif letters off abbreviations such as Vla. Use names/letters as well as colors; overlays must preserve black notation. Inactive motifs remain faint but readable. Reduce prose before making dense notation indefinitely smaller. Inspect at actual 4K and common reduced playback sizes.

## Left-panel beat display without information loss

User correction, 2026-11-11, for future videos only: the existing `6/8 拍` text gives the meter but not the current beat. Add a clearly readable beat-position display that follows the adopted musical timing; a vertical column of beat positions with the current position highlighted is an allowed layout. Merely stacking the numerator and denominator of the time signature does not supply current-beat information.

Keep the existing score heading, meter, current measure number, original tempo wording, Chinese tempo explanation, edition/source and page information, translated staff labels and relevant notation explanations. The beat display is additional: reserve unused space or adjust spacing while preserving readable type and all those fields. Do not replace the meter or tempo text, cover a staff/label, or delete existing information to fit it. Check the longest tempo text and the largest beat/subdivision count in a composed frame before full encoding; do not invent a universally safe fixed rectangle without measuring the actual layout.

Distinguish beat level from subdivision. For compound meter such as 6/8, identify the adopted principal-beat grouping and label subdivisions separately where shown; do not silently call six eighth-note subdivisions six principal beats. Keep beat numbers, grouping and changes consistent with the score and the adopted performance map. A bar-linear cursor does not by itself certify accurate beat instants. Before the first musical onset, do not cycle the highlights; handle pickup bars, meter changes and final holds explicitly. If supported beat timing cannot be established at the agreed practical standard, report the specific gap and remedy before export and wait for direction, rather than inventing precision or silently omitting this requested module.

This correction does not authorize changes to the already generated Dvořák movies or archived rendering data.

## Timeline, opening, and references

Draw background track, played track, permanent ticks, then labels. Color each section name with its theme color, using the same palette as the legend, so the first theme, second theme, introduction, development, and coda stay distinct. Show each section's name, measure range, and true start, not repeated end times. Under the performance window, above the timeline, show the current shot caption defined below. Size it with the other secondary labels, and keep it out of the timeline names. Scale by actual elapsed time rather than measure count. Add smaller theme-entry ticks when useful; abbreviate crowded labels and put full explanations in accompanying material.

The default clock is output time for player navigation. A music-time alternative must be declared; source-video navigation requires separate source times. Do not conceal the 6 s opening offset. Record whether the selected musical duration includes the decay.

Use separate 3 s identity and 3 s form pages, retaining the original version information. A form overview without a settled classification should be labeled as a broad listening division. Align the body movement name with the work title. Put maker credit at the opening's lower right.

Reference pages follow the preserved musical decay. Their count and duration follow text volume. Do not invent DOI values or claim all search results were read. All movements share both sizes of the same English [work cover](cover.md).

## Performance picture-in-picture

Use the same source_time for image and sound from the same original. For separately obtained same-event audio/video, follow production-policy.md: event information establishes identity, and a few recognizable landmarks establish offsets/edits; no mandatory exhaustive audio/frame matching. Check whether the source itself has audiovisual offset: matching container clocks do not prove original synchronization. Preparatory conducting gestures naturally precede attacks.

Preserve source aspect ratio, including 4:3 media; letterbox within the region when needed. A 4K output canvas does not make a low-resolution source native 4K. Check legibility during soloist shots, conductor cuts, and lighting changes. Avoid decorative frames that obstruct the picture.

### Shot captions and verified identities

For this and future videos (user requirement, 2026-11-09), the caption follows the visible performance shot, not the currently sounding instrument or the score's leading voice. Use the specific section when visually supported: `小号`, `钢琴`, `低音提琴`, or `指挥`. Use `乐队全景` for a general view and a concise multi-section label for a mixed close view. If the instrument itself cannot be identified, leave the caption blank rather than guess.

Append a person's name only with evidence linking that visible person to this exact performance: for example `指挥：克劳迪奥·阿巴多` or `小号：{verified name}`. Actively research every featured principal or exposed soloist before freezing captions, including flute and cello principals; once the exact-event identity is verified, include the name rather than leaving a generic instrument caption. Do not wait for the user to flag each missing name. A seat, apparent age, face resemblance, or the orchestra's present roster alone does not establish the historical player's identity. If only the section is known, show just the section, without an empty colon, a guessed name, or a question mark.

User correction, 2026-11-11, after the completed Dvořák set: use the score's specific part names in captions, motif labels and analysis. When the pictured violin section is established as the score's first violins, write `第一小提琴`; for second violins write `第二小提琴`, never collapse either verified part into `小提琴`. Likewise preserve numbered/divided parts where the score and shot correspondence support them. Identify the visible section using the shot context, documented orchestral layout and the corresponding score passage together; the sounding lead alone must not relabel a different pictured section. If a mixed shot includes both violin sections, use `第一、第二小提琴`; if the division remains unresolved, record that uncertainty and verify it before choosing a more specific label rather than inventing one.

The user's flute and cello screenshots demonstrate missing featured-player name research; they are not written name confirmations. Use same-event written credits, contemporary role-specific documentation or explicit user confirmation. A prior waiver for one unresolved clarinet player applies only to that player and event, not to flute/cello principals or all future captions. Preserve confirmed identities for reuse within that performance and avoid asking again. Do not use facial resemblance as identification evidence. The user explicitly excluded all currently generated Dvořák films from this correction: update future production rules only, without rerendering or changing their media or archived caption data.

Store `source_start`, `source_end`, `visible_part`, `score_part_name`, `part_mapping_evidence`, optional `person_name`, `identity_source`, `name_search_status`, `evidence_frame`, and `review_status` per shot. Scene detection can propose cuts; inspect the actual frames around each cut and any pan or zoom within a shot. Map these intervals through the same source/output edit map as the PiP. Captions change with the displayed shot, even when the music or motif has not changed; a conductor close-up must not inherit the preceding trumpet caption. Check caption transitions in the encoded video. This evidence does not approve score/audio synchronization or justify assertions about a gesture's musical effect.

## Implementation and encoding

Pillow/SVG/Canvas and FFmpeg/PyAV are possible implementations. Reuse a verified layout. Cache bounded static pages/fonts/excerpts and update only changing elements. Save configuration, exact font files, rates, source hashes, encoder command, and environment.

Preserve audio channels, sample rate, and precision. Avoid unjustified resampling, gain, noise reduction, compression, fades, or channel reordering. ALAC/MP4 or a suitable FLAC container can retain decoded PCM; check playback compatibility. Lossless re-encoding of a lossy source does not restore a master. Generate title/end silence and trims on the same sample grid; any fade is an edit that changes the expected PCM comparison.

Do not silently quantize 32-bit integer or floating-point PCM to ALAC's supported precision. Choose a compatible PCM container or explicitly record and validate the conversion.

Choose video quality after testing representative encoded passages: staff lines, text edges, moving PiP, size, and elapsed time. Use appropriate pixel/color formats, and scale scans without losing thin lines. Estimate bytes from total bitrate × seconds ÷ 8 plus overhead; motion can dominate an otherwise static score. Inspect the actual full encoded result, not only PNGs.

If subtitles are requested, use output-time start/end and an appropriately named sidecar; do not add another document system by default. Final coordinates and streaming requirements follow [the output contract](final-output-contract.md).
