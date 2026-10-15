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
- 2026-10-15: his answers 27 to 29 (section 10 v4; section 4's diagram rebuilt, waiting for his Substack upload) and, at 11:04, his two section 4 paragraphs (section 4 v11.3, 100% Human in batch 287g). Section 13 started: baseline all AI (batch 286g), drafts v1 to v6 through four gate rounds; 2 of 10 checked v5 paragraphs read Human (287g); not in the article yet. After his 13:10 answers (30 b: the visitor and founder lines stay as published; 31 a: paragraph by paragraph), Emulate rounds b to f, drafts v7 to v13 and gate rounds r5 to r9: 20 of its 27 paragraphs read Human alone or beside a neighbor that does (batches 289g to 292g, 23 of 28 checks Human).
- 2026-10-15, after his 18:28 answer (32 b: his research sentence stays as published): section 13 drafts v14 to v22, Emulate rounds g to i, gate rounds r10 to r15. Every part of v21 read Human on its own text and the whole section read 56% AI (298g); v22 rebuilds the two stretches that read AI everywhere (the land subsection; H4-P9 to H5-P2) from Emulate, and its review round r15 is done, its fixes next. Not in the article yet.
- Owner edits: 60 of 60 pass.

## Current checkpoint

Section 13, "Your Little Forming Group Already Is the Community", is the published text in the article (except one line fixed on 2026-10-12); its draft is `candidate/s13/v22.md` (and `v22b.md`, the other way of H5-P2), in review. The lane's notes are `STATUS.md` (newest entry on top) and `candidate/STATUS.md`.

## Remaining

- Sections 13 to 16 and the appendix.
- Joel's acceptance of the candidate sections, then promotion of the humanized article to the registered master with a promotion receipt.
- Claim-level citation review (`CITATIONS.json`, pending) when Joel asks for it.

## Blockers / unresolved

- Open items for Joel are on the lane's questions page (`candidate/OWNER-QUESTIONS.md`): 33 (the 😜 in section 13's provisional-membership hint); the rebuilt section 4 diagram waits for his Substack upload.
- Pangram checks run in the desktop app's browser pane, signed in to Joel's account; the API key is out of credits.

## Evidence / artifacts

- `IMPORT-RECEIPT-20261013.md`: what was imported, from where, and why the rules don't fork.
- `candidate/sN/`: each section's predictions, parts, batch files, review rounds and install scripts; `candidate/in-context/`: the side-by-side page maps; `candidate/prediction-review/`: the prediction scorecard data.
- `DETECTOR-EVIDENCE.json`, `EDITORIAL-STATUS.json`, `CITATIONS.json`, `SOURCE-EVIDENCE.json`, `OWNER-LOCKS.json`, `ARCHITECTURE.md`.

## Next safe action

Work on a branch from `main` in this folder (on `claude/community-joel-1015b` until its pull request merges). Continue section 13 from `candidate/s13/v22.md` with the handoff's next step (`candidate/HANDOFF-community-article.md`): the dispositions of gate round r15 (`candidate/s13/review-r15/`), draft v23, gate round r16, then Pangram for the rebuilt paragraphs, their stretches and the whole section through `tools/humanization/pangram_gate.py`. Before every push, run `python3 scripts/register_article_artifacts.py --article intentional-communities --write` and the repository's checks.
