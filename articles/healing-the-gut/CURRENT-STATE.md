# Healing the Gut: current state

## Goal

Joel, 2026-11-03 16:15 UTC (`experiments/t01-answers/joel-20261103-1615-messages.txt`): humanize his gut article ("Healing the Gut Naturally"), and line up its two parts better: the first part includes research he and his friends did themselves, the second is a recipe based on books.

## Authority / baseline

`master.html` is his Substack editor HTML as pasted on 2026-11-03 (`IMPORT-RECEIPT-20261103.md`). Shared rules: `docs/FIXING-AN-ARTICLE.md`, `docs/HUMANIZATION-GATE.md`, `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`. Protected functions: `OWNER-LOCKS.json` (protocol fidelity via `humanize/FIDELITY-KEYS.json`; his and his friends' findings stay his).

## Completed

- 2026-11-03: imported and registered; fidelity keys extracted; his messages saved word for word.

## Current checkpoint

Imported. Nothing in his post has changed.

## Remaining

1. Check each paragraph alone through the API (one check per paragraph lineage) to map what reads AI.
2. Structure page for Joel: block map, ways to line up his findings with the book recipe, contradictions and repeats between the parts, a recommended pick.
3. After his pick: humanize on a marking page, paragraph by paragraph, under the production budget.

## Blockers / unresolved

- Whether the paid Gem instructions (a prompt written for Gemini) should be humanized at all: a question for Joel on the structure page.

## Evidence / artifacts

- `source/substack-editor-20261103.html` (= `master.html`), `humanize/MASTER-VISIBLE.md`, `humanize/FIDELITY-KEYS.json`, `DETECTOR-EVIDENCE.json` (his extension share: 59% AI).

## Next safe action

Run the paragraph-alone API baseline.
