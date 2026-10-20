# Pangram prediction scorecard: community article

Built by `tools/humanization/pangram_ledger.py build` from `articles/intentional-communities/candidate/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 1905 | 1397 (73%) | 44% | 56% | 66% | - |

## Pangram 4.0 (before the ledger)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 39 (78%) | 24% | 76% | 94% | - |
| the latest 100 | 100 | 81 (81%) | 21% | 79% | 96% | - |
| all | 1905 | 1397 (73%) | 44% | 56% | 66% | - |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| unrecorded | 1092 | 773 (71%) | 49% | 51% | 62% | - |
| draft | 87 | 63 (72%) | 28% | 72% | 72% | - |
| section | 78 | 55 (71%) | 27% | 73% | 82% | - |
| owner | 68 | 64 (94%) | 43% | 57% | 60% | - |
| screen | 516 | 386 (75%) | 41% | 59% | 69% | - |
| edit | 64 | 56 (88%) | 8% | 92% | 95% | - |

## Since the ledger

No checks recorded in the ledger yet.

