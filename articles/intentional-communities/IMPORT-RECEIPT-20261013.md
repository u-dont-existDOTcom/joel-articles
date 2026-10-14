# Import receipt: Intentional Communities, 2026-10-13

## What Joel decided

Question 20 on the lane's questions page asked whether to register the community article now. Joel, 2026-10-13 21:00 UTC: "yes register the article but i don't want to separate it from the rules co-developed in inner child lane... so don't register if it would cause that to fork..." (his message is kept in `candidate/joel-20261013/joel-20261013-attachment.txt`).

## Why registering doesn't fork the rules

- The humanization rules live on `main` for every article: `AGENTS.md` ("One set of humanization rules for every article"), `SKILL.md`, `docs/HUMANIZATION-GATE.md` and `tools/humanization/`. The Inner Child lane and this lane have both been adding to those same files through pull requests (this lane's latest: #151, #166 and #169). Registering an article adds its authority and records, never rules.
- Before registration, the lane's work lived on a branch 424 commits behind `main` (`claude/emulate-lessons-20260930`), inside the Inner Child article's Emulate experiment folder. That branch was the one place the community work could drift from the shared rules. From now on the community work happens on branches from `main`, next to the same rules the Inner Child lane uses.
- The registration follows the Inner Child article's own pattern: the published Substack text is the registered working source master, the humanized article is a working artifact promoted when Joel accepts it, and his edits are an owner-edits ledger checked on every render.

## What was imported

- Source: branch `claude/emulate-lessons-20260930`, commit `6775ed15`, folder `articles/inner-child-therapy/experiments/emulate-20260929/runs/articles/intentional-communities/` (4,205 files), copied with `git archive` into `articles/intentional-communities/` with its inner layout unchanged, so the lane's relative paths (`candidate/` reading `../original.md`) still work.
- Nothing was edited in the import. New at the article's top level: `CURRENT-STATE.md`, `OWNER-LOCKS.json`, `SOURCE-EVIDENCE.json`, `UNINCORPORATED-IDEAS.md`, `CITATIONS.json`, `DETECTOR-EVIDENCE.json`, `EDITORIAL-STATUS.json`, `ARCHITECTURE.md` and this receipt.
- Roles: `candidate/HUMANIZED-SO-FAR.md` is `active_humanized_article`, `candidate/OWNER-EDITS.json` is `owner_edits_ledger`, `candidate/OWNER-QUESTIONS.md` is `owner_questions_page`; every other imported file is a working record, registered by `scripts/register_article_artifacts.py`.

## History

The lane branch is kept, with its full history, and frozen at `f4d24d2c`, whose only change after `6775ed15` is a note at the top of its two status files saying where the work moved. Older records inside the imported files name paths under the old folder; they are history and stay as written.
