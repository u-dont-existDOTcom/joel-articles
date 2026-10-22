# Pangram prediction scorecard: hypnosis guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-signal/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 944 | 803 (85%) | 22% | 78% | 89% | 0.120 (base 0.174, 944) |
| pangram 4.1, Pangram's check of the Substack draft (free, Joel's account) | 4 | 3 (75%) | 75% | 25% | 0% | 0.226 (base 0.188, 4) |
| pangram 4.1, web app | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |

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

## pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 4 | 3 (75%) | 75% | 25% | 0% | 0.226 (base 0.188, 4) |
| the latest 100 | 4 | 3 (75%) | 75% | 25% | 0% | 0.226 (base 0.188, 4) |
| all | 4 | 3 (75%) | 75% | 25% | 0% | 0.226 (base 0.188, 4) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 2 | 2 (100%) | 100% | 0% | 0% | 0.001 (base 0.000, 2) |
| stretch | 2 | 1 (50%) | 50% | 50% | 0% | 0.451 (base 0.250, 2) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 4 | 0.03 | 25% |

## pangram 4.1, web app

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |
| the latest 100 | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |
| all | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 10 | 6 (60%) | 40% | 60% | 80% | 0.195 (base 0.240, 10) |
| section | 4 | 2 (50%) | 50% | 50% | 100% | 0.214 (base 0.250, 4) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 9 | 0.49 | 44% |
| 0.6 to 0.8 | 3 | 0.67 | 67% |
| 0.8 to 1.0 | 2 | 0.82 | 100% |

## Misses since the ledger (7)

| cause | misses |
|---|---|
| balanced closer kept | 3 |
| parallel list kept | 1 |
| parallel list kept; light green turned red | 1 |
| fix underrated | 1 |
| verdict threshold misread | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [HG15-p9e](https://www.pangram.com/history/6e97d63f-765f-4e8d-aecc-39ca783c05fa) | HG15-p9, 1 | Human | AI or mixed | balanced closer kept |
| [HG35-forgive-e2](https://www.pangram.com/history/25833096-c587-4602-b24d-ba7affdfbcf3) | HG35-p13, 1 | Human | AI or mixed | parallel list kept |
| [HG15-w467](https://www.pangram.com/history/9cfccd99-95ce-49b0-a65a-47216c218f42) | HG15, 1 | Human | AI or mixed | balanced closer kept |
| [HG35-w467](https://www.pangram.com/history/74763536-ab88-4ec2-b347-0e186b0208ad) | HG35, 1 | Human | AI or mixed | parallel list kept; light green turned red |
| [HG15-p9e2](https://www.pangram.com/history/b252243a-a20d-4f01-8643-7551ffcb5d56) | HG15-p9, 2 | Human | AI or mixed | balanced closer kept |
| [HG35-forgive-e3](https://www.pangram.com/history/637e6fb4-3a47-4fe6-899f-b5ff0923e7f3) | HG35-p13, 2 | AI | Human | fix underrated |
| [HG-rest-41r2-b](https://www.pangram.com/feed/558d14f6-625d-46aa-8495-adf9141cb3a4) | HG-rest-B, 2 | AI | Human | verdict threshold misread |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| HG-whole | article | 2 of unlimited (Substack) | Mixed |
| HG15-p9 | paragraph | 2 of 6 | Mixed |
| HG15 | section | 1 of 2 | Mixed |
| HG35 | section | 1 of 2 | Mixed |
| HG35-p15 | paragraph | 1 of 6 | Mixed |
| HG17-emu-bc | stretch | 1 of unlimited (Substack) | pending |
| HG17-emu-bd | stretch | 1 of unlimited (Substack) | pending |
| HG17-emu-be | stretch | 1 of unlimited (Substack) | pending |
| HG17-emu-bf | stretch | 1 of unlimited (Substack) | pending |
| HG32-emu-bg | stretch | 1 of unlimited (Substack) | pending |
| HG32-emu-bh | stretch | 1 of unlimited (Substack) | pending |

