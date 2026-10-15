# Intentional Communities: current state

Registered 2026-10-13 from the community humanization lane (branch `claude/emulate-lessons-20260930`, commit `6775ed15`), at Joel's answer to question 20: "yes register the article but i don't want to separate it from the rules co-developed in inner child lane... so don't register if it would cause that to fork..."

## Goal

Humanize Joel's published intentional-communities Substack article section by section, so that every paragraph and every section reads Human in Pangram's web app and the meaning stays the published one, except where Joel changes it himself.

## Authority / baseline

- Registered working source master: `original.md`, the published Substack text (97,920 UTF-8 bytes, SHA-256 `5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6`). Like Inner Child Therapy's raw Substack master, it is the baseline, not the humanized article.
- The humanized article: `candidate/HUMANIZED-SO-FAR.md`, the working candidate (role `active_humanized_article`). Nothing in it is accepted until Joel says so.
- Joel's edits and rulings: `candidate/OWNER-EDITS.json`, checked by `tools/humanization/check_owner_edits.py` on every render.
- Rules: the repository's shared rules only (`AGENTS.md`, `SKILL.md`, `docs/HUMANIZATION-GATE.md`, `tools/humanization/`), the same ones the Inner Child lane runs and adds to. This folder holds the article's rulings and records, not a copy of the rules.

## Completed

- Sections 1 to 12 are humanized candidates in `candidate/HUMANIZED-SO-FAR.md`. Sections 4 and 12 are Joel's own texts of 2026-10-13 (with his answers of 2026-10-14); section 5 is his of 2026-10-06; the others carry his edits and answers where he gave them. Every candidate section read 100% Human in Pangram's web app when it was installed (`DETECTOR-EVIDENCE.json`; for the changes of 2026-10-14, `candidate/fix-20261014/RESULTS.md`).
- 2026-10-14: Joel's Rule Scoring Sheet answers and 13 fixes from the sweep of 2026-10-13 are in (sections 2, 3, 4, 6, 7, 8, 9, 11, 12), each changed paragraph Human alone and each section 100% Human in Pangram's web app. His answers of 21:19 UTC (questions 22 to 26) are in too: his own section 11 text and section 10 paragraph, and small cuts in sections 4, 9 and 11; sections 4, 9, 10 and 11 read 100% Human.
- 2026-10-15: his answers 27 to 29 (section 10 v4; section 4's diagram rebuilt, waiting for his Substack upload). Section 13 started: baseline all AI (batch 286g), Emulate round a, stance ledger, key file, v1 (linter FAIL, not yet gated).
- Owner edits: 58 of 58 pass.

## Current checkpoint

Section 13, "Your Little Forming Group Already Is the Community", is the published text except one line fixed on 2026-10-12. The lane's notes are `STATUS.md` (newest entry on top) and `candidate/STATUS.md`.

## Remaining

- Sections 13 to 16 and the appendix.
- Joel's acceptance of the candidate sections, then promotion of the humanized article to the registered master with a promotion receipt.
- Claim-level citation review (`CITATIONS.json`, pending) when Joel asks for it.

## Blockers / unresolved

- Open items for Joel are on the lane's questions page (`candidate/OWNER-QUESTIONS.md`): none open; the rebuilt section 4 diagram waits for his Substack upload.
- Pangram checks run in the desktop app's browser pane, signed in to Joel's account; the API key is out of credits.

## Evidence / artifacts

- `IMPORT-RECEIPT-20261013.md`: what was imported, from where, and why the rules don't fork.
- `candidate/sN/`: each section's predictions, parts, batch files, review rounds and install scripts; `candidate/in-context/`: the side-by-side page maps; `candidate/prediction-review/`: the prediction scorecard data.
- `DETECTOR-EVIDENCE.json`, `EDITORIAL-STATUS.json`, `CITATIONS.json`, `SOURCE-EVIDENCE.json`, `OWNER-LOCKS.json`, `ARCHITECTURE.md`.

## Next safe action

Work on a branch from `main` in this folder (on `claude/community-joel-1015` until its pull request merges). The old lane branch is frozen as history at `f4d24d2c`, whose last commit only adds the note that the work moved here. Continue section 13 from `candidate/s13/v1.md` (v2 for the linter, then the gate and Pangram); the steps for a section as the lane's notes describe (stance ledger, key-word file, a baseline batch, Emulate rounds on the published paragraphs, meaning fixes, the gate), with Pangram batches through `tools/humanization/pangram_gate.py`. Before merging any lane branch into `main`, run `python3 scripts/register_article_artifacts.py --article intentional-communities --write` and the repository's checks.
