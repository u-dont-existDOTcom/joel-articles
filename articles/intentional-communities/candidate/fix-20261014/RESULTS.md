# 2026-10-14: Joel's scoring answers and the sweep's fixes, results

Joel's message of 03:04 UTC: his Rule Scoring Sheet answers (`joel-20261014/joel-20261014-attachment.txt`), "pangram is logged in now also", the merge he tried ("it said conflicts"), and "continue". Pangram: the dashboard in the desktop app's browser pane, Joel's Pro account. Every result below is from Pangram's History, matched by the text's SHA-256 (`PREDICTIONS.md` has each batch's predictions, written before its call, and every link).

## The merges

Pull request 169 conflicted with main after his inner-child merge (#171): both had added an entry at the end of `tools/humanization/JOEL-FIXES-CATALOGUE-20260928.md`. Kept both, oldest first; the repository's checks passed; merged 169, then 170 (it had no conflict). This turn's work is on `claude/community-joel-1014`, from main.

## Installed in `HUMANIZED-SO-FAR.md`

| Section | What changed | Pangram |
|---|---|---|
| 2 v3.2 | his F4 sentence and F6 clause | his two paragraphs Human alone; the section 100% Human (275g, first try) |
| 3 v12 | P4: "whose turn it is to talk about the hatred, and whether a motion about it needs somebody to second it"; P10: "somebody who's earned authority in one role can use it in all their other roles", "gifted" back | both Human alone; the section 100% Human (276g, first try) |
| 4 v11.1 | his I1 answer: "And inner pl/ork is built on somatic regulation first." | the section 100% Human (276g, first try). The paragraph reads AI beside the reparenting paragraph, in his own wording too (278g's control) |
| 6 v22 | P8: "more human independence from the technosphere, all the machines and systems modern life runs on", "a way out of the technosphere" | P8 Human alone; the section 100% Human (277g, first try) |
| 7 v4 | "ZEGG, a community near Berlin, and Tamera, another in Portugal" | P6 Human alone; the section 100% Human (276g, first try) |
| 8 v29 | his F10 answer (my v22 sentence, with his "what happened"); "the usual promo video"; the Ye'kuana and the Island Pond raid explained; "When adults panic like that, kids can lose all those grownups without the panic actually preventing abuse"; "A surprise has an end date." | every changed paragraph Human alone; the section 100% Human (277g, first try) |
| 9 v15 | the caracoles explained; P18's closing disclaimer cut as a repeat of his P14 (E172) | both Human alone; the section 100% Human (276g, first try) |
| 11 v14 | P9: "no real way ... no matter how many meetings it holds"; P10: "the daily signs of founderism" | both Human alone; the section 100% Human on the fourth section try (282g) |
| 12 v13 | his W1 P2 and P3 | each Human alone and as a pair; the section 100% Human (274g, first try) |

Owner edits: 52 of 52 pass (`check_owner_edits.py`). Facts added: `SOURCES.md`.

## Not installed: questions for Joel

- **Section 10, P9** ("a collision of two principles", 4 reads: none named). A first sentence naming the pair from P8 read AI alone (276g, 103 words, medium), and so did the pair named inside the opening (279g, low); a third wording narrowed P8's solidarity limit (trace and stance). This opening failed in most wordings on 2026-10-10 too. The installed P9 stays.
- **Section 11, P2, P4, P6.** A definition of founderism in P2 ("When that influence goes unchecked, I call it founderism.") moves an AI window onto P4's run of questions in the section (281g against 282g), and so do P4's fixes (whose prediction, and the cut of "Can it replace the founder?", which the four questions ask again) with P6's new lead-in (282g). P4 passes alone in both wordings. P8's "who picks the reviewers" (9 reads) has no wording a trace accepts: "the people who review the founder" and "the people who handle complaints" each narrow the published "chooses reviewers".
- **Section 8, P13 under "Children Need Freedom Inside Real Protection"** ("the research corpus", 2 reads): his words of 2026-10-07; my suggestion is "all the research I'd gathered".
- **Section 4, P10 under "4. The container"** ("If one of them gets skipped", 2 reads): his words; my suggestion is "If one of the four gets skipped".
- **Repeats in his words** (`repeats/REPEATS-DISPOSITIONS.md`).

## The gate

Three rounds of meaning traces, section cold reads, march reads and stance checks, and a fourth for section 10's and section 11's wordings (`gate/`). Fixes the traces or the stance check sent back: "a gifted teacher" back; "I'd rather" kept as his earlier OK of "It's better ... right?"; "a way out of the technosphere" (its "it" could be the community); "a religious community" (the sources say church); the blanket request back; "A surprise has an end date." without its new "because"; "if the community is meant to spread"; P8's reviewers (above). Two fixes came out because the words were his (section 8, P27) or needed his ruling (section 11, P8).

The march read gave 15 of the 20 changed paragraphs no break, and gave their installed versions the same labels (`gate/MARCH2-labels.txt`), though each installed version had read Human alone. `pangram_gate.py` now has an "edit" kind for that case (E173): the march blocks an edit only when the installed version had a break and the edit has none.
