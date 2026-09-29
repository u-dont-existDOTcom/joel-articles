# Preliminary quality review — 2026-09-29

Status: **No article candidate accepted.** This is a review of saved website captures, not a publication or clinical validation. The browser/exec environment went offline before 15 charged captures could be committed and before three prepared neuro inputs were sent. Exact recovery inventory: [RECOVERY-20260929-2319.md](RECOVERY-20260929-2319.md).

## Coverage and gates

| Article | Revised eligible inputs | A/B captures committed | Completed but stranded | Never sent |
|---|---:|---:|---:|---:|
| Intentional communities | 49 | 49 | 0 | 0 |
| Hypnosis guide | 97 | 94 | 3 | 0 |
| Neuro-de-armoring | 26 | 11 | 12 | 3 |

The 56 prepared sentence checks and 52 article baselines were recorded before the website rewrites. Pangram last observed 1,382 credits, with a stop floor of 300. Section-context checks and final candidate checks are still pending. Emulate last observed 17,314 words, with a 2,000-word reserve. These counts exclude seven earlier original community first-pass runs and the 449-word medicine first pass; those are retained in the Emulate ledger. The medicine first pass ended mid-thought in both options, so a second pass divided the same span into three nonoverlapping chunks. One hypnosis passage (1001-s06) was accidentally submitted twice after a queue-pointer fault; the two runs have separate records, and no third run is allowed.

## Fidelity findings requiring rejection or repair

- The first linked community chunk failed D6 link preservation in both website runs. One option moved/truncated the anchor and the other dropped it. See `runs/articles/intentional-communities/D6-LINKS.md`.
- Several short community options scored Human 100% in Pangram but changed autobiographical details or timing. Examples in `LEDGER.md`: 0102 invents a memory claim; 0103 changes a quoted meeting thought or adds a founder detail; 0201 alters the film/advisory timeline; 0202 drops stewardship consequences. A Human detector result is not an editorial acceptance decision.
- The 449-word community 0501 A/B options both ended mid-sentence. In the guide, 1001-s01 A ended after “seeding”; 1201-s01 A ended after “To that end,”; 1301-s01 A ended after “deepen it by”. These are not complete replacements. Some other option endings are intentionally headings that continue into the next chunk and need context checks.
- Emulate’s rendered `innerText` can omit ordered-list markers that its Copy output retains. This was observed in community 0403 and later guide/neuro list passages. Selected A `.txt` captures use exact Copy where verified; unselected B is rendered page text with HTML provenance, so its list-number bytes are not proven exact.
- In the saved neuro opening 0101-s01, option A omits the source’s “below 90 BPM” threshold and the explicit instruction not to push through numbness or grayness. Option B retains 90 BPM but still compresses or changes warnings and mechanisms. Neither is accepted.
- In neuro 0201-s05, option A rewrites a 150–300 mg range as “150mg-300mg” and both versions change safety language. Every compound, dose, unit, timing, interaction, stop sign, and study claim needs a source-level comparison before use.
- In neuro 0201-s06, option B turns Scott’s genetic data, response, and personal dosing into first person (“I”); option A preserves Scott as speaker but omits some caution. Neither is accepted as an exact source-faithful replacement.
- A guide option in 1301-s03 changes the meaning of a consent/silence statement. Guide exit, grounding, help-seeking, and stop instructions require especially close review.

The uncommitted neuro outputs cannot be assessed from GitHub until their browser shared-workspace files are recovered. No protected Human baseline paragraph was sent as part of the revised queue; 21 original held spans/groups remain recorded in the preparation manifest. Links, emphasis, headings, and media must be restored from the source article during any assembly; stripped reader text sent to Emulate is not itself the final Markdown.

## Next editorial work

1. Recover the 15 paid captures without resubmission; submit only the three never-sent neuro tail inputs if the cloud browser reconnects.
2. Compare both options for every eligible span against its source, rejecting invented or dropped claims, reversals, incoherent seams, stock phrases and truncations. Apply the exact neuro protocol gate.
3. Restore source links/media and preserve protected Human paragraphs byte-for-byte in candidate Markdown/HTML; run Pangram on option, paragraph, section, and assembled candidate where credits permit.
4. Produce per-article final quality reports and candidate files only after the above gates. No source authority or publication changes are authorized by these captures.
