# Round r21 on v32: what each finding got (2026-10-17)

Reports: `MARCH-labels-a.txt`, `-b.txt` (v32 as first written), `-2a.txt`, `-2b.txt` (with the breaks put back in H3-P3, H3-P5 and H4-P3), `-3a.txt`, `-3b.txt`, `-4a.txt`, `-4b.txt` (the visitor subsection after the short visit's fix and the splitter's); `trace-T1.md` (H1-P4; H3-P3 with H3-P4), `trace-T2.md` (H3-P5; H4-P1), `trace-T3.md` (H4-P3; H4-P4); `SENSE-a.md`; `STANCE-sofar.md`; `REPEATS.md`. v32 is v31 with Joel's "if the community uses them" back, the short visit fixed (the one paragraph that read AI alone in 312g), the book line no longer leaning on the book's order, and the dedup he asked for (Joel, 2026-10-16 23:38 UTC; `../make_v32.py`, `../v32-fixes.json`).

Rules: as round r19's (`../review-r19/DISPOSITIONS-r19.md`), with UDA `patterns/convergent-review-acceptance-gates.md`: an item no round changed keeps the verdict earlier rounds gave it. A cut made for the dedup went to the traces with a note saying where the point is said, and the trace checked that claim.

## Marches

- **H3-P3, H3-P5 and H4-P3 had no break in read b of the first v32.** The dedup had taken H3-P3's "Sorry!" with the money-free sentence, and the book line and the short visit were one sentence each. Fixed: H3-P3 keeps "There will be bottlenecks, sorry!" (the bottlenecks without the money-free repeat), H3-P5 ends "Honestly, it's where I'd start for those!", and the short visit has "Not exactly a high bar! 😅". Reads 2a and 2b found breaks in H3-P3 and H3-P5; reads 4a and 4b in the short visit.
- **The splitter joined two sentences across an emoji.** "...charming for two weeks! 😅 So that's ..." and "(Hint: not the person who recruited them! 😜) What rights ..." reached the readers as one sentence each, so they gave one label and saw no break (reads 2a, 2b and 3b found none in H4-P5, whose hint had been its break since round r9). `tools/humanization/reviewer/reviewer.py` now ends a sentence after the emoji (test `MarchPrompt`); read 4b finds the hint's break again.
- **H5-P2 had no break in reads 2a and 2b.** Unchanged since v31; its break "(More on that next.)" was read in round r19 (read 5, both readings), and an unchanged paragraph keeps its march.

## Traces

- **T1, H1-P4, LOST "capacity".** Kept, as in round r19 (T1-2): his rule O40, "capacity" reads AI unless tied to "free resource"; "a budget of what you have in the way of resources" names the same tally.
- **T1, H3-P3 with H3-P4, SHIFT "That's coercive".** Fixed: moving the exit resources had put them between "You don't want them to lose everything they've put in!" and "That's coercive", so "That" read as the paper right. "That's coercive" follows the forfeiting again, and the exit resources come after it.
- **T1, SHIFT "once everybody's furious".** Fixed: "once anybody's furious" (the published "before anybody is furious").
- **T1, ADDED "bottlenecks" in the list of what people need to see.** That was the first v32; the bottlenecks are now said as a fact ("There will be bottlenecks, sorry!"), as published.
- **T2, H3-P5, ADDED "(on the reading list at the end)".** Kept, as in rounds r14, r17 and r20: the article's reading list does end with the book.
- **T2, H3-P5, ADDED "money" and "agreements".** Fixed to "(members, resources, land, agreements, etc.)": "resources" is the section's word; "agreements" is his reading list's ("start here for sequencing, membership, money, land, and agreements").
- **T2, H4-P1; T3, H4-P3 and H4-P4.** OK; each dedup note's claim checked (the promising-too-much point in sections 5 and 12; "more evidence, not certainty" in H4-P6).
- The changes after the traces (the breaks above; the pause fixes below) are checked by round r22's confirming trace.

## Cold read

- **P8 (H2-P3b), "Are you willing to experiment?" opens with nothing setting up "experiment with what".** Unchanged since v29, read OK in rounds r19 and r20; the reader settled it on reading on. Kept.
- **Repeated pauses** (`pause_tally.py` over every round's cold reads, r11 to r21, not only this round's): seven had neither a fix nor a reason, because round r19 answered only its own reports. Each is plainer in v32: "before you need a land surveyor" (r19 b, r21 a), "You don't want them to lose everything they've put in!" (r17 a, r19 a), "it only works when the community happens to have spare money" (r16 a, r19 b), "think someone's safe just because they're going along with everyone else" (r19 b, r21 a), "Six months with someone" (r19 a, r21 a), "before anybody sells their house to move in" (r17 b, r19 b), "ombudsperson" (six reports, r16 to r21). The others are answered in round r19: "promising strangers", "1978", "correspond with them", "All of them should have clear terms", "Don't worry about getting land yet", and "Both of them!" (fixed then).

## Stance (against the article so far)

- **"How long will your cash reserves last, if the community uses them?" against sections 15 and 16 (moneyless only as a late stage; outside bills still come in money).** Kept: his published words, which he asked to have back (2026-10-16 23:38 UTC); section 4 lays out the staged path for communities that do and don't use money, and the qualifier is about the community's own use of cash, not about outside bills.
- **The book's order against "Practice Comes Before Property".** Gone from the rewrite with Joel's fix. The reading list's "start here for sequencing" gets the same fix when that section comes up (questions page, "Coming up").

## Repeats

See the end of this file (the repeats check of v32 in the article).

## Counts

Marches: 4 rounds of reads for 3 paragraphs that lost or lacked a break, all fixed; one splitter bug fixed. Traces: 6 pairs, 3 OK; 7 items: 4 fixed, 3 kept (on words earlier rounds passed, or a fact the article states). Cold read: no findings on changed text; 7 repeated pauses fixed. Stance: 1 conflict kept (his words, his decision), 1 published contradiction resolved.
