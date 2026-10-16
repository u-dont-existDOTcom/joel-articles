# Round r5 on v3: what each finding got (2026-10-16)

Reports: `trace-T1.md` (P1, P2), `trace-T2.md` (P5, and P6 and P7 with ending W2), `trace-T3.md` (ending W3's P6 and P7), `SENSE-a.md`, `SENSE-b.md` (v3 with ending W2). Batch 303g read endings W2 and W3 Human in every group (`../b303/PREDICTIONS.md`); v4 is v3 with W2, the ending whose trace found less added. The fixes are exact old -> new pairs in `../make_v4.py` (`../v4-fixes.json`).

Rules: as round r3's (`../review-r3/DISPOSITIONS-r3.md`), with UDA `patterns/convergent-review-acceptance-gates.md`: an item no round changed keeps the verdict earlier rounds gave it. `tools/humanization/pause_tally.py` on the cold reads of rounds r3 and r5 against v4: every repeated pause is answered below or in round r3's dispositions.

## Fixed (v4)

- **P2, "Who keeps childcare going and makes sure the kids continue to go to school?" (trace T1: SHIFT, schooling of any kind narrowed to attending a school).** Now "Who keeps childcare and schooling going?", the published words.
- **P2, "tiding people over until they're housed and settled again, including with outside cash or benefits" (trace T1: LOST, food, housing and care no longer named as what is bridged, and "bridges", which P3's bridge leans on; ADDED, an end point).** Now "bridging people's food, housing and care, and any outside cash or benefits, if relevant", the published words as the trace's fix has them, with "people's" and "any" so the paragraph doesn't carry two lists of three (linter E125). Round r3's repeated pause at "bridging gaps in food, housing, care" (Emulate's "gaps") and its repeats item 2 (food, housing and care asked about twice in the list) give way to the published meaning: the published asks both who keeps people housed and fed and who bridges them.
- **P3, "assign a bridge/successor" (a repeated pause, both cold reads of this round).** Now "assign a bridge or successor", the published words without the slash.

## Kept, with the reason

- **Trace T1, P1's "Who would?" and P2's "That's a lot of loose ends!" (ADDED).** Unchanged since v2; kept in round r3 as each paragraph's break.
- **Trace T2, P6's "(as you may have noticed!)" (ADDED: a wink at the reader about the questions in this article).** A remark about the text itself, and true: the article asks its readers a great many questions, this section's P2 most of all. P6's break in both march readings of round r4.
- **Trace T2, P7's "I hope so, anyway." (ADDED: the author's hope).** The writer's own hedge on the published "may continue", no claim about how things are; P7's break in both readings. v2's "That gives me hope." added the same kind of thing.
- **Repeated pauses on his published words:** "Think of it like a living will" (4 reports), "turning every friendship into evidence" (4), "Dissolution terms" (3; key U9, his "A group with dissolution terms") and "carried the Bruderhof with him" (2; his "carried the Bruderhof long after leaving it"). Every reader read those paragraphs OK.
- **"American Commune follows two sisters" (2 reports, both of round r3).** Fixed in v3 ("The film *American Commune*"); the readers of round r5 didn't pause there.

## Not used

Ending W3 (trace T3: the film's name, "as you've probably noticed by now!" and "I like to think so, anyway." all ADDED). It read Human too (303g), and stays in `../v3-W3.md` in case W2 has to go.

## Clean

Trace T2's P5 OK. Both cold reads read every paragraph OK.

## Counts for this cycle

Traces: 9 items on v3 (2 fixed, 4 kept as breaks, 3 on ending W3, which isn't used). Cold reads: no findings; 1 new repeated pause (fixed).
