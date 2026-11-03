# Bad Trips guide: current state

Updated: 2026-11-03 (turn 2, his answers of 18:59 UTC). Registered 2026-11-03 at Joel's message of 15:45 UTC ("start working on humanizing my
badtrips guide at badtrips.u-dont-exist.com"; `experiments/t01-answers/JOEL-MESSAGE-20261103-1545.md`).

## Goal

A guide with a quick version and a long version that says each thing once, with the call-for-help lines in one place
(his message: "this article has a big duplication issue ... too much safety language spread everywhere rather than in
one spot"), then every paragraph and section reading Human in Pangram, with the meaning kept and every remedy, compound,
dose, unit, timing and warning exactly as it went in, and his post updated with the changes he approves.

## Authority / baseline

- `master.md`: his post as of 2026-11-03 (`IMPORT-RECEIPT-20261103.md`): the Markdown of his pasted editor HTML
  (`source/owner-editor-20261103.html`), which matches the published post block for block. `original.md` is the same
  text; `original-blocks.json` numbers its blocks B0 to B438; `original-page.md` is the review pages' form of it.
- `OWNER-LOCKS.json`: no passages locked; protected functions: the remedies' fidelity (`humanize/FIDELITY-KEYS.json`)
  and call-for-help thresholds staying where the reader acts on them.
- The shared rules: `AGENTS.md`, `docs/FIXING-AN-ARTICLE.md`, `docs/HUMANIZATION-GATE.md`,
  `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`, `tools/humanization/`.

## Completed

- 2026-11-03 (turn 1): registered; fidelity keys extracted; the published post compared with his paste (402 of 402
  blocks the same); baseline free check on the live post (his extension's label: AI; full analysis pending, his task 1);
  two fresh readers' repeats reads and a third reader's safety-line map (`experiments/t01-repeats/`); the round-1
  marking page (`review/r01/`). 17:15 UTC: reader A's and B's reports and the first half of C's (B4 to B207) checked
  quote by quote against the article; 13 new cards (nine repeats, two safety lines, four questions where the guide says
  two things that don't fit together) added to round 1's page; then reader B's final report (17:30 UTC): three more
  (two repeats, the charcoal question), 35 cards; then reader C's final safety map (17:40 UTC): five more (three
  safety lines, a repeat, the question of moving the support lines) and two cards revised, 40 cards (version 6 of the
  page). Repeats and safety lines the readers found that stay, with what each copy carries:
  `experiments/t01-repeats/NOTE.md`.
- 2026-11-03 (turn 2, his message of 18:59 UTC): pull request 280's conflicts with main resolved (main's Emulate wording,
  gate E333; both lanes' mailbox records); the baseline's full analysis read (his link: AI Detected, 82% AI, 189
  windows, recorded with each window's confidence in `humanize/baseline-20261103/` and the ledger); his 40 answers
  recorded and applied (30 change cards, his RP-4 line, Q-1, Q-4, Q-5, Q-7; 14,504 to 13,808 words); his three new
  rules in the shared files (gate, `tells_lint.py` O46 and X1, the tells registry); round 2's page built.

## Current checkpoint

- **In progress:** Turn 2: his round-1 answers are in (`review/r01/ANSWERS-R01-20261103-1859.json`; every card's fate recorded) and applied (`GUIDE-SO-FAR.md`, by `review/r01/apply_r01.py`); round 2's marking page (`review/r02/`, 25 cards: the checklist step by step per his answer A, the Longer Triage folded in, four lines drafted from his answers) is with Joel.
- **Next step (updated on every push, so another account can pick up here):** Put his round-2 answers in with a `review/r02/apply_r02.py` like round 1's (its "More:" lines take their links from each insert's href; CL-14 links "love" in step 14's heading to http://love.u-dont-exist.com/); then the humanize pass on the guide as it then stands: AI quips (gate J15), "one ordinary" (O46), "X does not Y" (X1, 65 candidates after round 1), the baseline's AI windows (`humanize/baseline-20261103/`), the gate's own writers (no Emulate), then the overcompletion read (E328) and the word-for-sense read (E331).
- **Waiting on Joel:** his answers on round 2's page.

## Remaining

His round-2 answers put in; an overcompletion read (gate E328); the
humanizing of every section that reads AI or below High, by the gate's own writers (Emulate is no longer used on his writing, Joel 2026-11-03); the word-for-sense read
(gate E331); his post updated, with the title's version and date (gate E323).

## Blockers / unresolved

None.

## Evidence / artifacts

`experiments/t01-repeats/` (prompts, the three reports, NOTE.md), `review/r01/` (build script, cards, page, its cards
as Markdown, his answers, the apply script), `review/r02/` (round 2's page), `GUIDE-SO-FAR.md` (the guide after round
1) with its blocks and page form, `OWNER-EDITS.json`, `humanize/baseline-20261103/` (the checked text, the badge note,
the full analysis's windows), `humanize/pangram-ledger.jsonl`.

## Next safe action

`HANDOFF-bad-trips.md`, START HERE.
