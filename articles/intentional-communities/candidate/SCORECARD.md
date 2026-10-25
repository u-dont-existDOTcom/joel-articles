# Pangram prediction scorecard: community article

Built by `tools/humanization/pangram_ledger.py build` from `articles/intentional-communities/candidate/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 1905 | 1397 (73%) | 44% | 56% | 66% | - |
| pangram 4.1, Pangram's check of the Substack draft (free, Joel's account) | 1 | 0 (0%) | 0% | 100% | 0% | 0.865 (base 0.000, 1) |

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

## pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 1 | 0 (0%) | 0% | 100% | 0% | 0.865 (base 0.000, 1) |
| the latest 100 | 1 | 0 (0%) | 0% | 100% | 0% | 0.865 (base 0.000, 1) |
| all | 1 | 0 (0%) | 0% | 100% | 0% | 0.865 (base 0.000, 1) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 1 | 0 (0%) | 0% | 100% | 0% | 0.865 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 1 | 0.07 | 100% |

## Misses since the ledger (1)

| cause | misses |
|---|---|
| pessimism | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [IC-whole-r1](https://www.pangram.com/feed/954042b6-e624-4c7f-87d7-db15c547d5c8) | IC-whole, 1 | AI | Human | pessimism |

