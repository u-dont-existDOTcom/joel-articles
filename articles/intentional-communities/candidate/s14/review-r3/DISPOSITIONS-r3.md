# Round r3 on v2: what each finding got (2026-10-16)

Reports: `trace-T1.md` (P1, P2), `trace-T2.md` (P3, P4), `trace-T3.md` (P5, P6), `SENSE-a.md`, `SENSE-b.md`, `STANCE-pub.md`, `STANCE-sofar.md`, `REPEATS.md`. Trace T4 (P7) was built and not run: P6 and P7 read AI together on Pangram (batch 301g, AI likelihood 0.92; with P5, batch 302g, 0.67), so v3 gives them four endings (`../make_v3.py`), and the ending that reads Human gets its own trace. The fixes are exact old -> new pairs in `../make_v3.py` (`../v3-fixes.json`).

Rules: the lane's (fix what two reviewers raise, or one when the fix loses nothing; a finding that the published meaning was lost gets the published words back). A break the march needs that a trace calls ADDED is kept when it is a published claim said again as a reaction, a question or an exclamation, or a remark about the text itself, and cutting it would leave the paragraph without a break (docs/HUMANIZATION-GATE.md, E176). `tools/humanization/pause_tally.py` on both cold reads: every phrase both readers paused at is answered below.

## Fixed (v3)

- **P1, "founders probably don't want to talk about" (trace T1: SHIFT, the published pattern made a guess).** Now "founders rarely want to talk about", the published "rarely" (the trace's own fix).
- **P2, "If the commune dissolves" (trace T1: SHIFT, "commune" narrower than the published "community").** Now "If the community dissolves".
- **P2, "Who takes responsibility for bridging gaps in food, housing, care, external income/benefits, etc., if applicable?" (trace T1: ADDED "etc."; both cold reads paused at "bridging gaps in food, housing, care"; repeats item 2: food, housing and care asked about twice in one list).** Now "Who takes responsibility for tiding people over until they're housed and settled again, including with outside cash or benefits, if relevant?": the published "bridges ... outside cash or benefits if relevant" said plainly, with "housed" (key U4) and without the second list of three (linter E125).
- **P2, "for ensuring obligations to the land are met" (trace T1: SHIFT, duties owed to the land; both cold reads paused at "obligations to the land").** Now "for making sure land obligations are met", the published term (taxes, leases and covenants too).
- **P5, "Institutions and the relationships that make them up don't have to die at the same time." (trace T3: two SHIFTs).** Now "Institutions and relationships don't die at the same time.", the published claim.
- **P5, "American Commune follows two sisters" (both cold reads paused: v2 lost the published italics, so it read as a group).** Now "The film *American Commune* follows two sisters"; "film" from the reading list at the end, which links it on YouTube.
- **P5, "The communal economy they were born into" (trace T3: ADDED, a new fact, and "they" could be the former members).** Now "The communal economy".
- **P7, "the legal entity" (both cold reads paused: after P6, it could be the Bruderhof's).** Every ending of v3 has "the community ends as a legal entity" (W3: "The community can end as a legal entity"), and the published "may" is back.

## Kept, with the reason

- **Trace T1, P1's "Who would?" (ADDED, an opinion).** P1's break in both march readings of rounds r2 and r4; the published "rarely want to discuss" said again as a question. Cutting it leaves P1 without a break.
- **Trace T1, P2's "That's a lot of loose ends!" (ADDED, an evaluation).** P2's only break in both march readings, a remark about the list itself, the kind that passed march and trace in section 13 ("That's a lot of deciding, I realize.").
- **Trace T2, P4's "Who wants that?" (ADDED, an opinion).** P4's break in both march readings; the published "without turning every friendship into evidence" said again as a question.
- **Repeated pauses on his published words:** "Think of it like a living will" (his published analogy, "Design this like a living will") and "turning every friendship into evidence" (his published words, key U9). Both readers read both paragraphs OK.
- **Repeats item 1 (the ending talk belongs at the happy start: "The Four Parts", "Resources, Land, and Exit Terms", and P1).** P1 is the published opener for a whole community ending, where the earlier passages are about one member leaving, and its question list follows.
- **Repeats item 3 (P5's first sentence and P7 say the institution can die while something goes on).** Both are his published sentences; P7 adds what people learned to give one another (practice, not only ties). A cut of either is his: on the questions page, with my opinion (keep both: P7 is where the father's case lands).
- **Repeats item 4 (*American Commune* in P5 and in the appendix).** The appendix entry is a citation, with the year and the link, where a reader expects a short description.
- **Repeats item 5 (P6's list and "What to Do This Month": "He made a film, founded a research organization, and carried me through communal experiments.").** Both published. The later one is in a section not rewritten yet; when it is, its draft must not list the three again (in the handoff).
- **Repeats item 6 (P7 and the closing "The transmission does not require one institution, one founder, or one official version.").** A theme developed, each in its place, as the repeats check itself reads it.

## Clean

Trace T2's P3 and trace T3's P6 OK. Both cold reads read every paragraph OK. Both stance checks found no conflicts in the rewrite and no contradictions in the published section.

## Counts for this cycle

Traces: 9 items on v2 (6 fixed, 3 kept as breaks). Cold reads: no findings, 6 repeated pauses (4 fixed, 2 his published words). Stance: 0. Repeats: 6 (1 fixed, 5 answered); 3 callbacks, all to first mentions.
