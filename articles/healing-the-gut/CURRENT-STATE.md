# Healing the Gut: current state

## Goal

Joel, 2026-11-03 16:15 UTC (`experiments/t01-answers/joel-20261103-1615-messages.txt`): humanize his gut article ("Healing the Gut Naturally"), and line up its two parts better: the first part includes research he and his friends did themselves, the second is a recipe based on books.

## Authority / baseline

`master.html` is his Substack editor HTML as pasted on 2026-11-03 (`IMPORT-RECEIPT-20261103.md`). Shared rules: `docs/FIXING-AN-ARTICLE.md`, `docs/HUMANIZATION-GATE.md`, `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`. Protected functions: `OWNER-LOCKS.json` (protocol fidelity via `humanize/FIDELITY-KEYS.json`; his and his friends' findings stay his).

## Completed

- 2026-11-03: imported and registered; fidelity keys extracted; his messages saved word for word.
- 2026-11-03: paragraph-alone Pangram 4.1 baseline (27 units, `humanize/fix-20261103/baseline/RESULTS.json`): his first part Human (High) except the mitochondrial-fuels stretch in Leaky gut; Phases 1, 2, 4, 5, 6 and the stacks section AI; Phase 3 87% Human.
- 2026-11-03 18:01 UTC: Joel answered the structure page (`experiments/t02-answers/`): S1 B (two parts, phases stay the Gem's, phases point back to his notes, explainer), S2, S5, S6 approved; S3 fuels stay in Leaky gut, Phase 5 only points back; S4 the stacks section is Gemini's; S7 he moves the Gem prompt to a doc.
- 2026-11-03: r01 marking page (`humanize/fix-20261103/r01/`, 14 cards) and a clean Gem prompt (`GEM-PROMPT-CLEAN.md`, `.docx`) delivered.
- 2026-11-03 19:12 UTC: his r01 answers (`experiments/t03-answers/`) applied as `humanize/fix-20261103/r01/r01.html` (G1-G12, G14; G13 goes into the stacks section's humanizing). His Gem prompt is now a link to his Google Doc.
- 2026-11-03: batch 1, the protocol section (`humanize/fix-20261103/b1-protocol/`): three writers (two from his fixes catalogue, one mine), a blind step-by-step meaning check (14 PASS), predictions frozen before every check. The intro and Phases 2-6 each have a version reading 100% Human alone; Phase 1 read AI in three materially different faithful versions (stop rule). Polish (`b1-protocol/polish/`): Phase 2 D (High, one 12-word Medium window), Phase 5 without its nickname (High apart from 1- and 3-word windows split at "Dr." and "L."), and his NOTE with the G1 explainer (High throughout).
- 2026-11-03 20:08 UTC: batch-1 marking page published (https://claude.ai/artifact/L2vQW2Z6GsNiPaDTYCZnLq, cards in `b1-protocol/REVIEW-CARDS.md`), with Phase 1 asking for his help and the nickname question.

## Current checkpoint

Batch-1 page out for his decisions (store collection `decisions`). Batch 2 (`humanize/fix-20261103/b2-stacks/`: the fuels stretch under Leaky gut, the stacks section with his G13 answer) has three writers' versions and a blind meaning check running; predictions are frozen for writer A.

## Remaining

1. Batch 2: meaning check, Pangram checks (A first, then B or C only where A is not 100% Human at High), a marking page.
2. Phase 1 with his help; the nickname answer (Phase 5's no-nickname version is already checked).
3. Apply his approved text to `r01.html`, then one whole-article check the free way (a temporary Substack draft's secret preview link, or the GUI bridge if he prefers), and give him the final HTML.

## Blockers / unresolved

- Phase 1: three faithful versions read AI; his diagnosis or his own words needed.
- Phase headings' nicknames: drop all or keep all (his answer).

## Evidence / artifacts

- `source/substack-editor-20261103.html` (= `master.html`), `humanize/MASTER-VISIBLE.md`, `humanize/FIDELITY-KEYS.json`, `DETECTOR-EVIDENCE.json` (his extension share: 59% AI).

## Next safe action

Score batch 2's meaning check, then check writer A's batch-2 texts through the API on the laptop (`TEXTS-A-to-check.json`, output folder `gut-api`).
