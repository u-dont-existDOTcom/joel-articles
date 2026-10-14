# 2026-10-14 21:19 UTC: Joel's answers to questions 22 to 26, results

His message and attachment: `joel-20261014-2119/`. Installed by `joel-20261014-2119/install_joel_20261014_2119.py`; owner edits 57 of 57 pass. Pangram: the dashboard in the desktop app's browser pane, his Pro account; predictions before each call and every result with its History link in `PREDICTIONS.md` and `gui/b283-results.json`, `gui/b284-results.json`.

## Installed in `HUMANIZED-SO-FAR.md`

| Section | What changed | Pangram |
|---|---|---|
| 4 v11.2 | "If one of the four gets skipped" (24); "and don't freeze into doctrine" out (26) | each paragraph Human with its neighbor (283g); the section 100% Human (1,550 words, 284g) |
| 9 v16 | "The useful thing is how they learn:" (26) | Human alone (283g); the section 100% Human (1,032 words, 284g) |
| 10 v3 | his last paragraph, as written (25) | Human alone (283g); the section 100% Human (736 words, 284g) |
| 11 v15 | his text of "Founderism: The Four Questions" through "Friends who come to visit", as pasted (22, 23: his P2 definition, P3 and P4; my P6 lead-in; P8's "the people who review the founder"); R15 without its "living balance" sentence (26) | every changed paragraph Human alone (P2 with P3; 283g); the section 100% Human (1,673 words, 284g) |

Not changed: section 8's "the research corpus" (24: it's a link); section 12's "free resource/capacity" (26: its first mention already reads that way).

Predictions: 12 of 12 right (283g, 284g).

## The gate

His texts, so no meaning traces. Cold reads (`gate/SENSE-*.md`, the new link-aware reader view): section 11, no breaks (one read; the second ran out of output and wasn't rerun, since with the first read clean no flag could reach two reads); section 10, both reads flag his last paragraph as a jump (question 28). Stance check (`gate/STANCE.md`): no conflict in his paragraphs; its Q1 and C3 are about "The boundary is simple", which his 10-11 rewrite already cut; C1 is section 4's diagram (question 29). Repeats (`gate/REPEATS.md`, one whole-article run, 77 minutes): nothing inside sections 4, 9, 10 or 11 that doesn't add a step (`gate/REPEATS-DISPOSITIONS.md`).

## Tools and rules

- `reviewer.py`: the cold reader sees a link as its words plus "[a link to ...]", and the section prompt says what that means (E174; tests in `SectionColdReadPrompt`).
- `docs/HUMANIZATION-GATE.md`: "What Joel's answers of 2026-10-14 21:19 UTC taught"; J56 in `tools/humanization/tells_registry.json`.
- The Prediction Scorecard's data builds again: `prediction-review/scorecard.py` had been reading the old lane's folder path from `parse_preds.py` and found 0 calls; `prediction-review/fix_preds.py` turns the fix folders' predictions into its rows. All calls: 1,056, 742 right; since the 10-10 review: 654, 487 right (74%; always saying AI would be 40%). Data: `prediction-review/prediction-calls.json`, for the publishing account to upload.
