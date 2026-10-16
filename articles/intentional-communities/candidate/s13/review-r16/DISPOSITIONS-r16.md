# Round r16 on v23 and v23b: what each finding got (2026-10-16)

Reports: `trace-T1.md` (H1-P2, H2-P2), `trace-T2.md` (H3-P1, H3-P2), `trace-T3.md` (H3-P3), `trace-T4.md` (H4-P6, H4-P9), `trace-T5.md` (H5-P1), `trace-T6.md` (H5-P2 way A), `trace-T7.md` (H5-P2 way B), `SENSE-a.md`, `SENSE-b.md` (the opener rule's first wording), `MARCH-labels-a.txt`, `MARCH-labels-b.txt` (way B: `MARCH-labels-variants-a.txt`, `-b.txt`), `STANCE-pub.md`, `STANCE-sofar.md`. The fixes are exact old -> new pairs in `../make_v24.py` (`../v24-fixes.json`).

Rules: the lane's (fix what two reviewers raise, or one when the fix loses nothing; a finding that the published meaning was lost gets the published words back), with UDA `patterns/convergent-review-acceptance-gates.md` rule 1: an item no round changed keeps the verdict earlier rounds gave it. `tools/humanization/link_flags.py`: no flag touches a linked phrase except "that way" (below). `tools/humanization/pause_tally.py` on every cold read of section 13 (rounds r1 to r16 and the three validation reads of v22): every repeated pause is answered below.

## Fixed (v24)

- **H3-P3, "(whether it's cash, if you use it, or tools," (trace T3: SHIFT).** "Or" made the other things alternatives to cash; the published "Cash if the community uses it, but also tools". Now "(cash, if you use it, but also tools,". Readers a, V1 and V2 paused at "spare money" in the sentence after it, which this settles: a cash-only right still depends on spare money.
- **H3-P3, "Could anyone in your group answer all of that today?" (trace T3: ADDED, it implies the group can't answer now).** The paragraph's break in both march readings; now "Who's keeping track of all that?", a question about the list itself.
- **H3-P3's opener, "How will you handle VISIBILITY of what you have?" (cold read b: it doesn't follow from the paragraph before; a repeated pause, 3 reports).** Now "And how will you handle the VISIBILITY of what the community has?": the next decision after H3-P2's, with whose.
- **H3-P2, "what happens when an owner dies" (STANCE-sofar: it narrowed inheritance to an owner's death).** Now "how inheritance works", the published word; made after round r17's reviews were built.
- **H3-P5, "For the full sequence, see ... -- vision, then members, ..." (a repeated pause, 6 reports).** The sequence goes right after the phrase, as in the published sentence.
- **H4-P2, "There's some correspondence first." (a repeated pause, 2 reports).** Now "First, correspond with them for a while." (key U40 "correspond").
- **H4-P6, "mistake people just doing what everyone else is doing for safety" (a repeated pause, 5 reports).** Now "take people doing what everyone else is doing as a sign of safety" (key U47 kept).
- **H4-P7, "asking if you've seen them do this thing before" (a repeated pause, 4 reports).** Now "checking whether you've seen them do this thing before".
- **H4-P9's opener, "What about people who aren't fully "in" the commune politically?" (cold read b: after the trial run with candidates, it first reads as being about them).** Now "Then there are the people who aren't fully "in" the commune politically."
- **H4-P9, "That's only fair." (trace T4: ADDED, a new justification).** Out. The paragraph's break is now "Why wouldn't they be?" after the rights sentence, a question about the claim just made.
- **H5-P1, "a serious danger to others (or to everyone in general)" (trace T5: SHIFT, "serious" came to cover both cases).** Now "a serious or generalized danger to others", the published words.
- **H5-P2 way B, "What might call for immediate action" (trace T7: LOST "conduct").** Now "What conduct might call for immediate action".
- **H1-P2 back to v22's, with "Until then, what's it worth?" (march r16 reading a: no break once that line was gone).** H1's landing rate is fixed in H1-P1 instead: "It sounds cheesy but it's true." becomes "It may sound cheesy, but it's true all the same.", the same aside, no longer a short line. Every subsection of v24 lints REVIEW.

## Kept, with the reason

- **Trace T3, "ahead of time" (ADDED).** Unchanged since v22; round r15's tracer: "ADDED, no new belief". The next paragraph's "when it's only theoretical" carries the same timing.
- **Trace T5, "impossible to live with" (LOST "ordinary shared life").** Unchanged since v20; round r12 kept it (his section 11 words, "impossible to live with") and round r15's tracer called it equivalent.
- **Trace T5, "Yeah, that's pretty tough, but sometimes somebody's gotta go" (ADDED).** The paragraph's break in both march readings (T24); "sometimes somebody's gotta go" says his heading again. As in round r15.
- **Cold read a, H4-P8's opener, "Do stuff together prior to making them provisional members."** The published subsection has this step in the same place, after the conduct paragraph ("Before provisional membership, do more than hang out."), and "them" is the subsection's candidates. One reader.
- **Cold read a, H5-P3's "that way".** His sentence, "My research initially leaned too far that way.", with its link to his research report (his 32 b; `link_flags.py`: the link tells a reader which way his report leans).
- **Repeated pauses on his published words:** "promising strangers" and "already a community" (8 and 3 reports: the published contradiction C3, reconciled by "even if it's still an untested one" and listed for him since round r12), "1978" (6: his published "the folks next to you may think experimenting ended in 1978"), "ombud" (5: his published "a mediator or ombud", which "mediator" glosses).
- **STANCE-sofar, the published contradiction C3.** As above.

## Clean

Traces T1, T2 and T6 OK; T4's H4-P6 OK, with the new break ("What do they actually do?") read as carrying the published "concrete". The stance check against the published essay found nothing in v23. Both cold reads read every other paragraph OK.

## Counts for this cycle

Traces: 9 items on v23 (6 fixed, 3 kept: unchanged words that earlier rounds passed); cold reads: 4 openers (2 fixed, 2 kept) and 9 repeated pauses (6 fixed, 3 his published words); stance: 1 conflict (fixed). Round r15 had 20 trace items. The fall is the convergent-review rule at work: unchanged items kept their verdicts.
