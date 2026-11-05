Bad Trips guide, turn 11 (Joel's round-6 answers, exported 2026-11-05 15:14 UTC, and his message of 15:15 UTC).

**His round 6.** His three versions and his placement are in the guide (`articles/bad-trips/review/r06/apply_r06.py`): the
warning-stage paragraph with his humic line sits after the rescue medicine and before the CBD paragraph, his cannabis
paragraphs follow it, his topical CBD paragraph drops 7-OH-CBD, and his merged first-five-minutes paragraph replaces my
two. KEEP-AS-IS K13 to K17 and cuts C9 and C10 hold his rulings, and OWNER-EDITS gets three round-6 entries.

**"fix the way you work" (gate E362).** The making-sense read now leaves a receipt, `tools/humanization/sense_receipt.py`.
For every sentence I write, the receipt records its payoff for the reader's actual case and why it sits where it does.
Any point I checked against a source and found has lost its reason for being there gets cut. `pangram_ledger.py predict`
and `suggestion_review.py` refuse text of mine that has no passing receipt. `predict` also refuses a retry that rewrites
more than 40% of the last try unless a reason is given (E361). It now hashes the text the way Pangram reads it, without
the file's final newline. Tests for all of this are in `tests/test_sense_receipt.py`, `tests/test_pangram_ledger.py` and
`tests/test_suggestion_review.py`.

**"merge lessons with main" (gate E365).** If a branch changes shared rules or tools, `lane_push.py` now refuses to push
it without `--merge` or `--no-merge "why"`. `--merge` merges the pull request into main once the checks on the pushed
commit pass. Tests are in `tests/test_lane_push.py`. `AGENTS.md` has the rule. This pull request is the first one pushed
with `--merge`.

**Lessons.** E362 to E365 are in `docs/HUMANIZATION-GATE.md`. `docs/MAKING-SENSE.md` gets his round-6 pairs under
questions 2, 3, 6 and 7, plus the receipt. `docs/FIXING-AN-ARTICLE.md` item 9 and `docs/INDEX.md` point to the receipt.

**Pangram, in his account (predictions first, 8 of 9 right).** His warning-stage, cannabis and topical CBD paragraphs
all read Human, High. His forums paragraph read AI in the two sentences of mine he kept. Round 7's page has 4 cards, and
every new text read Human, High (`articles/bad-trips/humanize/h06-r07-20261105/RESULTS.md`). Each card's new words have
a receipt and two fresh reads. The page's browser test passed 78 of 78.

Overlaps: #293 changes AGENTS.md's marking-page paragraph and this changes its workflow paragraph. #303 changes a
numbering note in docs/HUMANIZATION-GATE.md, and this adds the bad trips section's E362 to E365 after main's E361, so its
next lesson would be E366. #198 and #199 change other entries of docs/INDEX.md than the one this changes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01QAY8FUZDTAj8NLkkWxD5ih
