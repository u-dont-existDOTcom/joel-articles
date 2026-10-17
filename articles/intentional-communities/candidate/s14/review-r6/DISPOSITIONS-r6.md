# Round r6 on v6 and v7: what each finding got (2026-10-17)

Reports: `MARCH-labels-a.txt`, `-b.txt` (v6), `-2a.txt`, `-2b.txt` and `-3a.txt`, `-3b.txt` (v7's P2 as rebuilt, before and after the list closed); `trace-T1.md` (v6: P2; P5 with the last paragraph), `trace-T2.md` (v7's P2), `trace-T3.md` (v7: P2; P5); `SENSE-a.md` (v6 in the article); `REPEATS.md` (v6 in the article, with section 13 at v32). v6 is v5 deduplicated at Joel's word (2026-10-16 23:38 UTC: "let's merge/dedup section 14 without losing important things pls"): P2's second food-housing-care question cut to its outside cash or benefits, and the last paragraph's point moved into P5's first sentence (`../make_v6.py`). v7 rebuilt P2 after v6's read AI alone (313g); v8 is v7 with v5's P2 after v7's read AI alone too (315g). Rules: as round r5's (`../review-r5/DISPOSITIONS-r5.md`); an item no round changed keeps its verdict.

## Marches

- **Every reading finds a break in every paragraph** (six readings). P2's only break is "That's a lot of loose ends!" in all three versions.

## Traces

- **P5 with the last paragraph (T1, T3): OK.** "Institutions and relationships don't die at the same time, and some of what people learned to give one another may go on too." carries the last paragraph's point; the section ends on his father.
- **v7's P2, ADDED ", etc." (T2).** Fixed in v7 ("and any unresolved claims", the published closed list); v8's P2, v5's, closes the list too.
- **P2, ADDED "That's a lot of loose ends!" (T1, T2, T3).** Kept, as in rounds r3 and r5: it's the paragraph's only break, a reaction to the list, not a claim about the community. Whether the four short breaks are Joel's voice is question 37 on the questions page.
- **P2 in v8.** v5's text, traced in rounds r3 to r5; unchanged since, so it keeps their verdict.

## Cold read (v6)

- Every paragraph OK. Single pauses, each from one reader: "bridging any outside cash or benefits people depend on" (v6's wording, gone with v5's P2), "Think of it like a living will", "a bridge or successor", "Dissolution terms", "turning every friendship into evidence" (all unchanged since v5, read without a pause in rounds r3 and r5), and "The communal economy had changed dramatically" (fixed in v7: "The Farm's communal economy", a pause two rounds had now made).

## Repeats (v6 in the article)

- **Repeat 1: plan the ending at the start** (section 11's "be more conscious about the process and less romantic", section 13's exit terms "like a pre-nup when you're planning the wedding", section 14's "But that's exactly when it needs to be talked about."). Kept: section 13's is about one member leaving, section 14's about the whole community ending, and its opening sentence sets the section's subject. The questions page lists it with the other repeats kept.
- **Repeat 2: the Bruderhof shaped his father** (section 14's last paragraph and "What to Do This Month" under "Practice Comes Before Property"). Deferred: that section's draft says it once when it comes up (questions page, "Coming up"). Section 14's version is the one tied to leaving ("long after he left it").
- **No contradictions.** The callbacks (the film, the foundation, The Farm) rely on the opening and on section 13, as the report says.

## Pangram

- v6's P2 read AI alone (313g, 0.78) and v7's (315g, 0.96); v5's P2 reads Human alone (305g-x, 0.11). v8 keeps v5's P2 with its repeated food-housing-care question: question 38 asks Joel. v8 reads 100% Human as a whole (316g, 0.17), and every paragraph Human alone (`tools/humanization/paragraphs_alone.py`: PASS).

## Counts

Marches: 6 readings, a break in every paragraph. Traces: 5 pairs, 2 OK; 2 items: 1 fixed, 1 kept (question 37). Cold read: no finding; 1 pause fixed. Repeats: 2, 1 kept, 1 deferred.
