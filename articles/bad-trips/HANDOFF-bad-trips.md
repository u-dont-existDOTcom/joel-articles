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

- **2026-11-03, turn 1 (his message of 15:45 UTC).** Set up: his paste is `source/owner-editor-20261103.html`, equal to
  the published post block for block; `original.md` is its Markdown and `original-blocks.json` its block map (B0 to
  B438). Baseline: his extension labels the published post AI; the full analysis is his task 1 on `OWNER-QUESTIONS.md`.
  Three fresh readers mapped the repeats and the safety lines (`experiments/t01-repeats/`); their finds are on the
  page (40 cards, 17:40 UTC). The marking page
  (`review/r01/`, built by `build_r01.py` from `cards_r01.py`) asks the structure question (ST-1) and proposes the
  repeats inside the long part (Bad Trips Guide, Round 1, https://claude.ai/artifact/GB83uPzEFyLVGkQD9cQC97).
  The readers' finds that stay, with what each copy carries, are in `experiments/t01-repeats/NOTE.md`; any later
  card goes on the same page with the same ids kept, so his answers stay. **First:** put his answers in (record each card's fate), then, if he picks A, build round 2:
  the new checklist step by step from his own headings and first lines, the Longer Triage's paragraphs moved where they
  belong, and the checklist's copies cut with the place that says each point. After the structure, an overcompletion read
  (gate E328) before any rewording, then the gate's own writers on the flagged paragraphs (no Emulate: Joel, 2026-11-03, `AGENTS.md`). His curly apostrophes are an AI tell in his writing (his words, 2026-11-03: "yes the curly apostrophes are an AI tell i know that"): settle with him how the humanized text treats them.

## Where things are

- State: `CURRENT-STATE.md`; questions: `OWNER-QUESTIONS.md`; Pangram ledger: `humanize/pangram-ledger.jsonl` (lane "bad
  trips guide").
- The working order for any fix: `docs/FIXING-AN-ARTICLE.md`; Pangram spending: `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`.
- Push with `tools/humanization/lane_push.py --article bad-trips --mailbox "<turn's first clock reading>"` after
  `tools/humanization/lane_mailbox.py record`.
