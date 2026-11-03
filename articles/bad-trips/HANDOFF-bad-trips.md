# Handoff: Bad Trips guide

Joel's guide "Trip-Sitting: Medical Triage, Shadow Work, Therapy (v 5.5, updated 3 Oct, 2026)"
(https://ibogaqueen.substack.com/p/shadow-work-and-tripsitting-yourself, opened by badtrips.u-dont-exist.com, post
170920118, 14,168 words), deduplicated (a quick checklist and a long guide, each point said once, safety lines in one
place) and then humanized so every paragraph and section reads Human in Pangram, with every compound, dose, unit, timing
and warning exactly as it went in (the same rule as the neuro de-armoring protocol). Started 2026-11-03 at his message of
15:45 UTC (`experiments/t01-answers/JOEL-MESSAGE-20261103-1545.md`).

**Resume line (paste into any Claude account; the repository is public):**
> Continue my bad trips guide work: read https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261103/articles/bad-trips/HANDOFF-bad-trips.md and carry on from its next step.

If that branch is gone (merged), the same file is on main:
https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/HANDOFF-bad-trips.md

## START HERE

- **2026-11-03, turn 2 (his message of 18:59 UTC).** His 40 answers to round 1 are recorded
  (`review/r01/ANSWERS-R01-20261103-1859.json`) and applied: `GUIDE-SO-FAR.md` is the guide after round 1 (made by
  `review/r01/apply_r01.py`; `OWNER-EDITS.json` checks his own edits are in it). His structure answer is A. Round 2's
  page (Bad Trips Guide, Round 2, https://claude.ai/artifact/DkeaxjjJ6QcHzs558YGhKT; cards as text in
  `review/r02/REVIEW-R02.md`) carries A out step by step, folds the Longer Triage into the long part, and drafts four
  lines from his answers (Q-3 twice, Q-6, Q-1). **First:** put his round-2 answers in with an `apply_r02.py` like round
  1's (the "More:" lines take their links from each insert's href; CL-14 links "love" in step 14's heading). **Next:**
  the humanize pass with his three new rules (AI quips, "one ordinary", "X does not Y": gate, `tells_lint.py` O46 and
  X1), the baseline's AI windows (`humanize/baseline-20261103/RESULT-20261018.json`: 82% AI), the gate's own writers
  (no Emulate), then the overcompletion read (E328) and the word-for-sense read (E331). His curly apostrophes are an AI
  tell in his writing (his words, 2026-11-03: "yes the curly apostrophes are an AI tell i know that"); his new words in
  round 2 keep the straight ones he typed. He'd like the quick triage in his web app if the GPT-made app gives the
  advice: test it once round 2 is in (`OWNER-QUESTIONS.md`, item 2).
- **2026-11-03, turn 1 (his message of 15:45 UTC).** Set up and round 1 (`review/r01/`); his paste is
  `source/owner-editor-20261103.html`, equal to the published post block for block.

## Where things are

- State: `CURRENT-STATE.md`; questions: `OWNER-QUESTIONS.md`; Pangram ledger: `humanize/pangram-ledger.jsonl` (lane "bad
  trips guide").
- The working order for any fix: `docs/FIXING-AN-ARTICLE.md`; Pangram spending: `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`.
- Push with `tools/humanization/lane_push.py --article bad-trips --mailbox "<turn's first clock reading>"` after
  `tools/humanization/lane_mailbox.py record`.
