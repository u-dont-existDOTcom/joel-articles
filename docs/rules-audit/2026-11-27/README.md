# The rules audit of 2026-11-27

Joel, 2026-11-27 22:48 UTC, after lesson bad-trips-2026-11-27j drew the wrong lesson from his "smooth": "go over all your
rules with fable double checking, and see if any of them look sus and then ask me about the ones that look sus. make sure
your sus checker first finds this rule you made that's def sus." Lessons: `docs/lessons/2026-11-27-2248-bad-trips.md`
(l, m, n).

**His questions: [QUESTIONS.md](QUESTIONS.md)** (37 cards; the interactive page with Approve / Revise / Reject is
https://claude.ai/artifact/VcUmGfK8DfxM1yp9KoTY96, built from [SPEC.json](SPEC.json) by
`tools/humanization/decision_page.py`).

## What ran

1. **The rules, as they stood** at commit 742a4f72 (turn 74 pushed, before any correction), split into 2,087 units by
   [scripts/extract_rules.py](scripts/extract_rules.py): his saved preferences, AGENTS.md, SKILL.md, the briefs in
   tools/humanization, the docs, all 110 lesson files, the old gate (docs/HUMANIZATION-GATE.md) and the 223 tells
   ([units.json](units.json)); packed into 35 batches of about 52 KB (rebuild them with the script; they aren't kept).
2. **The checker** ([CHECKER-BRIEF.md](CHECKER-BRIEF.md); kept for every lane as
   `tools/humanization/rules_check_brief.md`), one Fable agent a batch. **Calibrated first**, on the two batches that hold
   the smooth rule (B19, lesson j; B04, way 30), told nothing about it: both flagged it for his reason ("A word the
   passage already has merely happened to be true of his fix; he said more accurate"; "nothing he says is about reusing
   the passage's words. The rule's own replay shows the failure was a less exact word"), and B19 flagged lesson k too ("A
   word-length count stands in for a judgment of meaning"). Then the other 33 batches: **404 flags** in all
   ([flags/](flags/)).
3. **Consolidation** ([CONSOLIDATE-BRIEF.md](CONSOLIDATE-BRIEF.md)), one Fable agent: the same rule in several files
   merged, rules that fail the same way grouped, active told from historical: **34 clusters and 8 stale items**, 3 flags
   dropped with reasons ([CLUSTERS.md](CLUSTERS.md), [CLUSTERS.json](CLUSTERS.json)).
4. **The double check** ([VERIFY-BRIEF.md](VERIFY-BRIEF.md)), five Fable agents: each cluster against its rule's own
   text and his words in context, with file and line, and each proposed fix against what he said later; 14 confirmed,
   20 partly, fixes that would undo his later words rewritten ([verify/](verify/)).
5. **The lead's check of the double check**: one correction (C30: the every-turn mailbox check and lane pull requests
   merging themselves are his own words, so neither is a question); the cards addressed to him
   ([scripts/build_questions.py](scripts/build_questions.py)).
6. **The new lessons through the same checker** before they went to main: five flags on this turn's three lessons, all
   taken ([selfcheck/L75-flags.md](selfcheck/L75-flags.md)); then three on lesson l's addition after the blind test, all
   taken, among them my own inference that a writer should infer what a thing does from a larger dose
   ([selfcheck/L75b-flags.md](selfcheck/L75b-flags.md)).

## What comes next

His answers come back as the page's JSON. Each approved fix goes into every file its rule lives in (the card's "Where it
lives"), in one pass, with a lesson file naming the answers; a revised one as he says; a rejected one stays and is
marked as checked with him, so no later audit flags it again.

## His answers (2026-11-28)

His answers came on 2026-11-28 at 10:24 UTC ([the export](ANSWERS-20261128-1024.json)): 33 approved, 4 to revise, with notes, and with them a message asking for a rule tree with a human view ([word for word](MESSAGE-20261128-1025.md)). What happened to each card: [RESULTS.md](RESULTS.md) (`scripts/results.py`). Each fix is a rule of [the rule tree](../../../rules/README.md), which now holds every rule once. The questions his answers left open: [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) (`scripts/open_questions.py`; his page is a view of it).
