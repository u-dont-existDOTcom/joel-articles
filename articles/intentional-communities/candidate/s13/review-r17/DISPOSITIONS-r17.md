# Round r17 on v24, with r17b: what each finding got (2026-10-16)

Reports: `trace-T1.md` (H1-P1, H1-P2), `trace-T2.md` (H3-P3 as first written in v24), `trace-T3.md` (H3-P5, H4-P2), `trace-T4.md` (H4-P6 and H4-P7, H4-P9), `trace-T5.md` (H5-P1), `trace-T6.md` (H5-P2 way B), `SENSE-a.md`, `SENSE-b.md` (the refined opener rule), `MARCH-labels-a.txt`, `MARCH-labels-b.txt` (way B: `MARCH-labels-variants-a.txt`, `-b.txt`). Round r17b (`../review-r17b/`) read the two paragraphs v24 broke again after r17's march: `trace-T1.md` (H3-P3, H3-P5) and `MARCH-labels-a.txt`, `-b.txt` (H3-P3 to H3-P5). The fixes are exact old -> new pairs in `../make_v24.py` and `../make_v25.py` (`../v25-fixes.json`).

Rules: as round r16's (`../review-r16/DISPOSITIONS-r16.md`), with UDA `patterns/convergent-review-acceptance-gates.md`: an item no round changed keeps the verdict earlier rounds gave it, and a new finding on unchanged words is fixed only when the fix puts back the published words or makes the sentence plain and loses nothing. `tools/humanization/pause_tally.py` on every cold read of section 13 (rounds r1 to r17 and the three validation reads of v22) against v25, Joel's own sentences left out: every repeated pause is answered below. `tools/humanization/link_flags.py`: one flag touches a linked phrase, cold read b's pause at "the full sequence", whose sentence links the book (answered below).

## Fixed

- **H3-P3, "Who's keeping track of all that?" (both r17 march readings: a step, T12).** In v24: the break is "Sorry!" after "scarce resources and bottlenecks.", the writer reacting to the claim just made. Round r17b: a break in both readings, and the trace OK ("no new belief").
- **H3-P5, no break in either r17 march reading (T14).** In v24: "It's the first book I'd hand to any group starting out." Round r17b: a break in both readings (kept below against its trace).
- **H4-P2, "First, correspond with them for a while." (trace T3: ADDED, a length).** In v24: "First, correspond with them."
- **H4-P6, "Even giving it six months will give you more data" (trace T4: SHIFT, "it" has no noun in reach).** In v25: "Six months will give you more data", the published subject ("Six months gives you a larger sample").
- **H1-P4, "budget for what the group can provide" (a repeated pause: cold reads r16 a and r17 b).** "Budget for" reads as setting money aside; the published "capacity budget" is a tally of what the group has. In v25: "a budget of what the group can provide".
- **H4-P9, "They should have clear terms" (a repeated pause: validation read V1 and cold read r17 b).** After "(yes, even interns!)" and "Why wouldn't they be?", "They" could be the interns alone. In v25: "All of them should have clear terms", the published "they" over all five groups.

## Kept, with the reason

- **Traces T3 and r17b, H3-P5's "(on the reading list at the end)" (ADDED fact).** Unchanged since v21 and kept in round r14. The article's reading list does end with it: "Diana Leafe Christian, *Creating a Life Together* — start here for sequencing, membership, money, land, and agreements."
- **Trace r17b, H3-P5's "It's the first book I'd hand to any group starting out." (ADDED opinion).** The paragraph's break in both r17b readings, and his reading list's "start here" said in his voice. Cutting it leaves H3-P5 with no break.
- **Trace T3, H4-P2's "(Not everyone does!)" (ADDED).** Unchanged; kept since round r7: it says what the question before it implies, and it is the paragraph's break.
- **Trace T4, "I wouldn't hand someone the van keys just because they're great with kids!" (ADDED).** The trace itself: an example of the published conduct-specificity, "no new rule". H4-P7's break in both readings.
- **Trace T5, "Yeah, that's pretty tough, but sometimes somebody's gotta go." (ADDED).** As in rounds r15 and r16: the paragraph's break in both march readings, and "sometimes somebody's gotta go" says his heading again.
- **Repeated pauses on his published words:** "promising strangers" (10 reports) and "already a community" (3): the published contradiction C3, reconciled by "even if it's still an untested one" and listed for him since round r12. "1978" (8): his published "the folks next to you may think experimenting ended in 1978". "ombud" (7): his "a mediator or ombud". "a competent layer" (2): his "a competent layer that is not reviewing its own conduct", and the next sentence lists what it can be.
- **"the full sequence" (8 reports, 2 of them since v24).** His published opening ("For the full sequence—vision before membership, ..."); v24 put the sequence right after it, where the published has it, and every reader read H3-P5 OK. The link on the book's title takes a reader to the book itself (a PDF in the United Diversity library), where the full sequence is laid out.
- **"spare money" (3 reports).** Answered in round r16: "but also" makes the right to leave a right to more than cash, which still depends on spare money.
- **"Don't worry about getting land yet" (2 reports).** The published "Land can wait." said plainly as the section's first line; the next sentence says why, and both readers read H1-P1 OK.

## Clean

Traces T1, T2 and T6 OK; T4's H4-P9 OK; r17b's H3-P3 OK. Both cold reads read every paragraph OK and flagged no opener. Way B's H5-P2 has a break in both readings.

The march read gives H2-P2 no break (S S in both readings), as rounds r14 to r16 did; its v21 version read S S S in r14 and r15 and passed Pangram with H2-P1 (batch 299g), so v24's few words there go to Pangram as an edit (E173), with no break before or after. H4-P5 reads all steps in both readings; unchanged since v21, it passed Pangram alone (297g) and keeps that verdict.

## Counts for this cycle

Traces: 8 items (2 fixed, 6 kept: 3 unchanged words earlier rounds passed, 3 breaks). Cold reads: no findings; 11 repeated pauses (2 fixed in v25, 1 answered in r16, 8 kept: his published words, or the published sentence's own order). Round r16 had 9 trace items and r15 had 20.
