# Pangram prediction scorecard: hypnosis guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-signal/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 944 | 803 (85%) | 22% | 78% | 89% | 0.120 (base 0.174, 944) |

## Pangram 4.0 (before the ledger)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 42 (84%) | 26% | 74% | 86% | 0.137 (base 0.192, 50) |
| the latest 100 | 100 | 83 (83%) | 25% | 75% | 90% | 0.148 (base 0.188, 100) |
| all | 944 | 803 (85%) | 22% | 78% | 89% | 0.120 (base 0.174, 944) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| baseline | 37 | 36 (97%) | 92% | 8% | 11% | 0.026 (base 0.075, 37) |
| emulate | 846 | 723 (85%) | 17% | 83% | 95% | 0.119 (base 0.141, 846) |
| edit | 61 | 44 (72%) | 54% | 46% | 61% | 0.180 (base 0.248, 61) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 36 | 0.08 | 3% |
| 0.2 to 0.4 | 31 | 0.31 | 10% |
| 0.4 to 0.6 | 106 | 0.51 | 42% |
| 0.6 to 0.8 | 361 | 0.72 | 84% |
| 0.8 to 1.0 | 427 | 0.94 | 91% |

## Since the ledger

No checks recorded in the ledger yet.

