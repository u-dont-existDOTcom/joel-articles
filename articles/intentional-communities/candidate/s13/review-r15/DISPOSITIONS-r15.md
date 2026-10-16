# Round r15 on v22 and v22b: what each finding got (2026-10-16)

Reports: `trace-T1.md` (H3-P1, H3-P2), `trace-T2.md` (H3-P3), `trace-T3.md` (H3-P4, H3-P5), `trace-T4.md` (H4-P9, H5-P1), `trace-T5.md` (H5-P2 way A), `trace-T6.md` (H5-P2 way B), `SENSE-a.md`, `SENSE-b.md`, `SENSE-B-a.md`, `SENSE-B-b.md`, `STANCE-pub.md`, `STANCE-sofar.md`, `STANCE-B-pub.md`, `STANCE-B-sofar.md`, `MARCH-labels-a.txt`, `MARCH-labels-b.txt` (way B: `MARCH-labels-variants-a.txt`, `-b.txt`), and the repeats check on the article with v22 in place (`REPEATS.md`, E172). Same rule as round r6 (`../review-r6/DISPOSITIONS-r6.md`): fix what two reviewers raise, or one when the fix loses nothing; a reader's finding that the published meaning was lost gets the published words back. `tools/humanization/link_flags.py` on v22 and every report: no flag touches a linked phrase. New this round, Joel's answer of 2026-10-16 18:22 UTC and `tools/humanization/pause_tally.py` (below). The fixes are exact old -> new pairs in `../make_v23.py` (`../v23-fixes.json`).

This is section 13's last repair cycle in this turn. Under the convergent-review rule (UDA `patterns/convergent-review-acceptance-gates.md`, rules 2 and 5), the section's leftover flags don't hold up section 14: whatever still reads AI after batch 300g is marked for review on the questions page with the per-round counts, and work moves on.

## Joel's answers (2026-10-16 18:22 UTC)

- **33 a: the 😜 stays** in H4-P5's hint, "(Hint: not the person who recruited them! 😜)" (`OWNER-EDITS.json`, `s13-joel-20261016-1822-33a`, pending until the install).
- **"How do you know?" is cut** from the head of H4-P6: "i would cut the first sentence "How do you know?" ... why did the reviewer not cut that, what's that? know what? doesn't seem to follow..." (`s13-joel-20261016-1822-cut`). The question was mine, added in an earlier round as the paragraph's break, and it was the only break both march readings of r15 found there (T20). v23 gives H4-P6 a break that follows from the sentence before it: "...don't go by that. What do they actually do?"

## Why no reviewer cut it, and what changed

- **Four cold reads in three rounds paused at it and left it out**: r9 reader a, r11 reader C-b ("P20 "How do you know?" read as how to judge a newcomer"), r14 readers a and b ("the next sentence supplies the object"). The prompt told them that "a reader who pauses and then gets it isn't lost", and a pause they settled from the next sentence wasn't a finding. Dispositions answered findings only, so nothing counted the four pauses.
- **The traces listed it as an added "lead-in", "frame" or "hook"** (r6 T4, r7 T4, r9 T4) and asked for no fix, as their brief says of additions: they check that the published meaning survives, not that an added sentence follows.
- **The fix, in the shared files:**
  - `tools/humanization/reviewer/sense_section.txt`: a paragraph's first sentence has to follow from what comes before it; when it asks or answers something the paragraph before doesn't set up, it gets its line even when the next sentence lets the reader work it out. Every cold read now ends with a "Paused:" line.
  - `tools/humanization/pause_tally.py`: counts the phrases two or more cold reads paused at, across rounds, leaving out Joel's own sentences (the author marks of `meaning_sweep.py`); with `--dispositions`, each one needs an answer here. On section 13's reports it lists "How do you know?" (4 reports), and with the reports up to r11 only, it would have listed it at r11 (2).
  - Validation (`tools/humanization/reviewer/sense-validation/20261016/`): the new prompt on v22, two fresh Sonnet readers, see `RESULTS.md` there; on section 12 with a planted opener ("How much is enough?" before P15), the reader flagged it with the reason; on section 11, Joel's text, see `RESULTS.md`.

## Fixed (v23)

- **H3-P1, "If it's in the names of three out of twelve members" and "despite what your literature says about everyone being equal" (trace T1: LOST "own everything", SHIFT "despite").** Now "If three out of twelve members own everything, then whether or not your literature says everyone is equal, there are two classes of members." The published words back in Emulate's sentence.
- **H3-P2, "outside debt (can an owner borrow money outside the community, and what happens if they do?)" (trace T1 and three stance checks: STANCE-pub, STANCE-B-pub, STANCE-B-sofar).** The parenthesis made the community's outside debt an owner's private borrowing; the essay uses "outside debts" for the community's own (section 14, the capacity budget). Now "what about outside debt". Trace T1's "etc., etc." (it opened the published closed list) is out, with "and" before the last item.
- **H4-P9, "aren't "in"", "like pay and access to common resources", "Equality is for everybody, not just members" (trace T4; the last also STANCE-pub and STANCE-B-pub).** Now "aren't fully "in"", "when decisions really affect their pay or access to common resources", and "Equality that stops at the membership line can end up recreating a servant class that moves from commune to commune." (the published "Egalitarianism that stops at the membership boundary can recreate a servant class").
- **H5-P1, "possible to do restorative work", "if the person is dangerous", "essential community boundaries" (trace T4).** Now "If restorative work can work", "if the person is endangering everyone else", "essential boundaries".
- **H5-P2 way A, "Who will recuse themselves?" and "and outside funds" (trace T5).** Now "Who will be recused?" and "or outside funds (if any)".
- **H5-P2 way B, "without creating danger", "collect and", "to the charges against them", "etc." (trace T6).** Now "without endangering others", "Who will preserve evidence?", "How will the person be able to reply?", and the list closed.

## Kept, with the reason

- **H3-P1 "Very important!" and H3-P2 "Lots of decisions to make!" (trace T1, added, "minor").** Each is its paragraph's break in both march readings (T10, T11); the published power claim and the published list carry them, and neither adds a claim a reader would take as new.
- **H5-P1 "Yeah, that's pretty tough" (trace T4, added: the author's feeling).** The paragraph's break in both readings (T24); "sometimes somebody's gotta go" echoes his heading, "When Somebody Has to Go".
- **H3-P5 "(on the reading list at the end)" (trace T3, added: "a new fact about the article").** His appendix lists the book ("start here for sequencing, membership, money, land, and agreements"); the tracer can't see the appendix. As in rounds r13 and r14.
- **H5-P2 "(More on that next.)" (traces T5 and T6).** Both called it a true signpost; no fix asked.
- **The published contradiction C3, "already a community" against "a circle of promising strangers" (STANCE-B-pub).** His published text, kept since round r6; H1-P1's "even if it's still an untested one" carries the reconciliation.

## The march (breaks)

- H3-P3 had no break in either reading (T12): v23 adds "Could anyone in your group answer all of that today?", a question made from the paragraph's own list, right after it.
- H3-P5 had none either (T14). A break at its end made the land subsection's landing rate fail the linter (three of five paragraphs ending on a short line), so it stays as it was; it goes to Pangram with H3-P4, as before.
- H4-P9 had one in reading a only (T23): v23 adds "That's only fair." after the list of decisions, before the last sentence.
- H4-P6: Joel's cut took its only break; see above.

## The linter, subsection by subsection (the 2026-10-15 lesson)

v22's H1 and H2 failed B7/B13 as wholes (two of four and three of five paragraphs ending on a short line). v23 drops H1-P2's last line, "Until then, what's it worth?" (its other break, "But really, truly dealt with it.", stays: T2, both readings), and turns H2-P2's "Where are you still unsure? Mark those places too." into one sentence, "Mark the places on your list where you're still unsure, too." (H2-P2 had no break, T6; the published "Mark where you are unsure" kept). Every subsection of v23 and v23b now lints REVIEW; the section lints REVIEW (`../LINT-v23.txt`, `../LINT-v23b.txt`); keys PASS (65 units).

## Repeats (E172): each one

All 18 are the published article's own, or his words in two places: each of section 13's instances says something the published section 13 says (`../../../original.md`), in Emulate's or my wording. The same answers as round r12 (`../review-r12/DISPOSITIONS-r12.md`):

- **Kept, the published article's own: repeats 4, 5, 6, 8, 9, 10, 13, 14, 15, 16, 17, 18.** Each later instance adds its own part in the published text, and cutting one is his call. Repeat 14 (land after a real conflict, seven instances) and repeat 18 (time gives evidence, not certainty) are his published sentences; round r12 already put back his own phrase in the second of 18.
- **Kept, his own words in two places, listed for him:** repeat 1 (his "Founded on Freedom" text in section 4, "When agreements get frozen ... doctrine", and the published "experimenting ended in 1978 and anything that came from it is doctrine now"), repeat 2 (his section 4 line "Even in a moneyless community, someone can control what's scarce." and the published money-free line), repeat 3 (his section 12 well and the published well), repeat 7 (his sentence "So work out the process before it's about anyone in particular." and section 8's "Decide on the response process ahead of time"), repeat 11 (his section 11 divorce line and the published prenup), repeat 12 (his section 11 "impossible to live with" and the draft's words for the published "makes ordinary shared life impossible").
- **Callbacks** (The Farm, section 3; the Zapatistas' 2023 restructuring, section 9): kept, as in rounds r8 to r12.
- **Contradictions:** C1 (visitors' terms): his 30 b, kept. C2 (removal decided case by case, or the process in advance): both his, kept and listed for him. C3: above.

`"repeats"` for the section check: 0, every item being answered here.

## Repeated pauses (`pause_tally.py`, new this round)

`python3 tools/humanization/pause_tally.py articles/intentional-communities/candidate/s13/review-r*/SENSE*.md --draft articles/intentional-communities/candidate/s13/v22.md --ledger articles/intentional-communities/candidate/OWNER-EDITS.json --dispositions articles/intentional-communities/candidate/s13/review-r15/DISPOSITIONS-r15.md`:

- "How do you know?" (4 reports): cut, Joel's answer of 2026-10-16 18:22 UTC (above).

## Counts for this cycle

Traces: 20 items needing a fix or a decision (16 fixed in v23, 4 kept above); stance: 2 conflicts in v22 and 2 in v22b, all from the two fixed sentences; cold reads: 0; march: 3 paragraphs without a break both readings see (2 given one, 1 kept). Round r14 had 2 trace items and 0 elsewhere on v21; r15's rise is v22's rebuilt stretches (Emulate round i), not the old ones coming back.
