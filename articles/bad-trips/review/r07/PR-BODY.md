Bad Trips guide, turn 11 (Joel's round-6 answers, exported 2026-11-05 15:14 UTC, and his message of 15:15 UTC).

**Two sessions, one result.** His round-6 answers reached two sessions: this lane's chat, and the neuro de-armoring chat
at 15:20 UTC. The other session's work merged first (#304). This branch merges main and puts the two together:
- The guide holds his round-6 words as he wrote them. The other session had also put its two fixes (Y-B, Y-C), its fourth
  forums try and a "[this vid]" link into the guide; all of those are now proposals.
- Round 7, version 2 has every proposal from both sessions, one card a paragraph, each Human, High in his account. The
  other session's files are kept beside this branch's: its page in `articles/bad-trips/review/r07/v1/`, its apply script
  in `articles/bad-trips/review/r06/from-claude-bad-trips-20261103/`, its checks in `humanize/h06-checks-20261105/`.
- Both sessions' ledger lines are kept.
- Its lesson E362 (a check that takes away a point's payoff takes the point) stands, and this branch's lessons follow it
  as E363 to E365.

**His round 6.** His three versions and his placement are in (`articles/bad-trips/review/r06/apply_r06.py`):
- the warning stage with his humic line sits after the rescue medicine and before the CBD paragraph;
- his cannabis paragraphs follow it;
- his topical CBD paragraph drops 7-OH-CBD;
- his merged first-five-minutes paragraph replaces my two.

KEEP-AS-IS (K13 to K17, cuts C9 and C10) and three OWNER-EDITS entries hold his rulings.

**"fix the way you work" (gate E363, enforcing E362).** The making-sense read now leaves a receipt,
`tools/humanization/sense_receipt.py`. For every sentence I write it records the sentence's payoff for the reader's
actual case and why the sentence sits where it does. A point I checked against a source and that lost its reason for
being there must be cut.
- `pangram_ledger.py predict` and `suggestion_review.py` refuse my text without a passing receipt.
- `predict` refuses a retry that rewrites more than 40% of the last try unless a reason is given (E361).
- `predict` hashes the text the way Pangram reads it, without the file's final newline.
- Tests for these are in `tests/test_sense_receipt.py`, `tests/test_pangram_ledger.py` and `tests/test_suggestion_review.py`.

**"merge lessons with main" (gate E365).** `lane_push.py` now refuses to push a branch that changes shared rules or tools
unless it's given `--merge` or `--no-merge "why"`. With `--merge`, the pull request merges into main once the checks on
the pushed commit pass. Tests are in `tests/test_lane_push.py`, and `AGENTS.md` has the rule. This pull request is pushed
with `--merge`.

**Lessons.** E363 to E365 are in `docs/HUMANIZATION-GATE.md`, after the other session's E362. The next lesson is E366.
`docs/MAKING-SENSE.md` now has both sessions' round-6 pairs and the receipt.

**Pangram, in his account (predictions first, 8 of 9 right).** His warning-stage, cannabis and topical CBD paragraphs read
Human, High. Each card's new words read Human, High (`articles/bad-trips/humanize/h06-r07-20261105/RESULTS.md`), with a
receipt and two fresh reads. The forums paragraph took a tell panel and three tries. The page's browser test passed 78 of 78.

**Overlaps.**
- #293 changes AGENTS.md's marking-page paragraph; this changes its workflow paragraph.
- #198 and #199 change other entries of docs/INDEX.md than the one this changes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01QAY8FUZDTAj8NLkkWxD5ih
