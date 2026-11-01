# Pangram prediction scorecard: hypnosis guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-signal/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 944 | 803 (85%) | 22% | 78% | 89% | 0.120 (base 0.174, 944) |
| pangram 4.1, Pangram's check of the Substack draft (free, Joel's account) | 38 | 32 (84%) | 84% | 16% | 5% | 0.119 (base 0.133, 38) |
| pangram 4.1, web app | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |
| pangram 4.1, the API (Joel's key, run on his laptop; E218) | 20 | 12 (60%) | 45% | 55% | 75% | 0.216 (base 0.247, 20) |
| pangram API (model pangram-4, expect 4.1), Joel's key, run on the laptop | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |
| Pangram 4.1 (web app) | 103 | 84 (82%) | 18% | 82% | 83% | 0.186 (base 0.150, 103) |

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
| the latest 50 | 38 | 32 (84%) | 84% | 16% | 5% | 0.119 (base 0.133, 38) |
| the latest 100 | 38 | 32 (84%) | 84% | 16% | 5% | 0.119 (base 0.133, 38) |
| all | 38 | 32 (84%) | 84% | 16% | 5% | 0.119 (base 0.133, 38) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 26 | 22 (85%) | 88% | 12% | 4% | 0.101 (base 0.102, 26) |
| stretch | 12 | 10 (83%) | 75% | 25% | 8% | 0.155 (base 0.188, 12) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 24 | 0.04 | 8% |
| 0.2 to 0.4 | 9 | 0.31 | 22% |
| 0.4 to 0.6 | 5 | 0.47 | 40% |

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

## pangram 4.1, the API (Joel's key, run on his laptop; E218)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 20 | 12 (60%) | 45% | 55% | 75% | 0.216 (base 0.247, 20) |
| the latest 100 | 20 | 12 (60%) | 45% | 55% | 75% | 0.216 (base 0.247, 20) |
| all | 20 | 12 (60%) | 45% | 55% | 75% | 0.216 (base 0.247, 20) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pair | 15 | 9 (60%) | 47% | 53% | 67% | 0.214 (base 0.249, 15) |
| paragraph | 4 | 2 (50%) | 50% | 50% | 100% | 0.229 (base 0.250, 4) |
| stretch | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 1 | 0.15 | 0% |
| 0.2 to 0.4 | 2 | 0.28 | 50% |
| 0.4 to 0.6 | 13 | 0.52 | 54% |
| 0.6 to 0.8 | 3 | 0.60 | 100% |
| 0.8 to 1.0 | 4 | 0.85 | 75% |

## pangram API (model pangram-4, expect 4.1), Joel's key, run on the laptop

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |
| the latest 100 | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |
| all | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 5 | 4 (80%) | 20% | 80% | 100% | 0.187 (base 0.160, 5) |
| pair | 2 | 2 (100%) | 0% | 100% | 100% | 0.181 (base 0.000, 2) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 5 | 0.58 | 80% |
| 0.6 to 0.8 | 5 | 0.63 | 80% |

## Pangram 4.1 (web app)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 43 (86%) | 16% | 84% | 82% | 0.163 (base 0.134, 50) |
| the latest 100 | 100 | 81 (81%) | 19% | 81% | 82% | 0.186 (base 0.154, 100) |
| all | 103 | 84 (82%) | 18% | 82% | 83% | 0.186 (base 0.150, 103) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 103 | 84 (82%) | 18% | 82% | 83% | 0.186 (base 0.150, 103) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 4 | 0.25 | 50% |
| 0.4 to 0.6 | 77 | 0.56 | 81% |
| 0.6 to 0.8 | 83 | 0.64 | 88% |

## Misses since the ledger (40)

| cause | misses |
|---|---|
| not explained yet | 19 |
| balanced closer kept | 3 |
| parallel list kept | 2 |
| context: red in the whole guide, Human in the pair | 2 |
| six versions, same reading: the method is spent | 2 |
| parallel list kept; light green turned red | 1 |
| fix underrated | 1 |
| tells overweighted | 1 |
| a red window read as its first section's | 1 |
| the same skeleton reworded | 1 |
| tidy closers at both paragraphs' ends | 1 |
| tidy closer | 1 |
| a linter fix that read worse | 1 |
| pessimism about Emulate's whole-stretch re-run | 1 |
| context: Human in the whole guide, red alone | 1 |
| pessimism about red moving onto unchanged text | 1 |
| pessimism about the whole text, again | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [s1101-36](https://www.pangram.com/history/c1a63da5-511e-46f5-879a-9dda4d958002) | HG1101-36, 1 | AI | Human | **not explained yet** |
| [s1101-37](https://www.pangram.com/history/00960ecb-3db9-4988-ad9b-cbe6e650b7c8) | HG1101-37, 1 | AI | Human | **not explained yet** |
| [s1101-38](https://www.pangram.com/history/0009f224-bec6-450c-a1d6-c3697413778a) | HG1101-38, 1 | AI | Human | **not explained yet** |
| [s1101-40](https://www.pangram.com/history/c601f371-9603-4327-8b11-45a1f9c0293a) | HG1101-40, 1 | Human | AI or mixed | **not explained yet** |
| [s1101-44](https://www.pangram.com/history/489391bc-5f75-4088-897d-a9e907e9e0f4) | HG1101-44, 1 | Human | AI or mixed | **not explained yet** |
| [s1101-46](https://www.pangram.com/history/0c0710c1-c0a9-4ba7-b99e-c166cd5eb1d2) | HG1101-46, 1 | Human | AI or mixed | **not explained yet** |
| [s1101-51](https://www.pangram.com/history/532027b0-d9b1-499b-99e7-27a4cc34ba40) | HG1101-51, 1 | AI | Human | **not explained yet** |
| [s1101-53](https://www.pangram.com/history/35f8fc73-3636-4e8f-9634-70828c7e1e5f) | HG1101-53, 1 | Human | AI or mixed | **not explained yet** |
| [s1101-73](https://www.pangram.com/history/c0512630-d9d3-4041-9fa0-86d109c13636) | HG1101-73, 1 | AI | Human | **not explained yet** |
| [s1101-74](https://www.pangram.com/history/5f67ddd1-1c49-4f16-afef-51b5d129e17c) | HG1101-74, 1 | Human | AI or mixed | **not explained yet** |
| [s1101-81](https://www.pangram.com/history/47aae1f8-55f3-4362-a3ee-2ef055601a37) | HG1101-81, 1 | AI | Human | **not explained yet** |
| [s1101-93](https://www.pangram.com/history/98e84a1c-0bf1-46a8-990e-3a93792d874e) | HG1101-93, 1 | Human | AI or mixed | **not explained yet** |
| [s1101-95](https://www.pangram.com/history/8be96f9e-57b6-41f4-86ec-808c276c90f8) | HG1101-95, 1 | AI | Human | **not explained yet** |
| [s1101-96](https://www.pangram.com/history/78cb97fc-9eb9-44a6-9de3-2988a428ebd1) | HG1101-96, 1 | AI | Human | **not explained yet** |
| [s1101-99](https://www.pangram.com/history/2122b7a5-8950-4926-9037-81d41cfbf928) | HG1101-99, 1 | Human | AI or mixed | **not explained yet** |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| HG-whole | article | 15 of unlimited (Substack) | Mixed |
| HG-rest-B | article | 13 of unlimited (Substack) | Mixed |
| HG15-p9 | paragraph | 2 of 6 | Mixed |
| HG15 | section | 1 of 2 | Mixed |
| HG35 | section | 1 of 2 | Mixed |
| HG35-p15 | paragraph | 1 of 6 | Mixed |
| HG17-emu-bc | stretch | 1 of unlimited (Substack) | Mixed |
| HG17-emu-be | stretch | 1 of unlimited (Substack) | Mixed |
| HG32-emu-bg | stretch | 1 of unlimited (Substack) | Mixed |
| HG32-emu-bh | stretch | 1 of unlimited (Substack) | Mixed |
| HG32-469g | stretch | 1 of unlimited (Substack) | AI |
| HG32-c1 | stretch | 1 of unlimited (Substack) | Mixed |
| HG32-c2 | stretch | 1 of unlimited (Substack) | Mixed |
| HG16-B209 | pair | 3 of 6 | Mixed |
| HG-parent-script-P1 | paragraph | 1 of 6 | Mixed |
| HG1101-14 | section | 1 of 2 | Mixed |
| HG1101-17 | section | 1 of 2 | Mixed |
| HG1101-20 | section | 1 of 2 | Mixed |
| HG1101-23 | section | 1 of 2 | Mixed |
| HG1101-27 | section | 1 of 2 | Mixed |
| HG1101-39 | section | 1 of 2 | Mixed |
| HG1101-40 | section | 1 of 2 | AI |
| HG1101-41 | section | 1 of 2 | Mixed |
| HG1101-44 | section | 1 of 2 | Mixed |
| HG1101-46 | section | 1 of 2 | Mixed |
| HG1101-53 | section | 1 of 2 | Mixed |
| HG1101-59 | section | 1 of 2 | Mixed |
| HG1101-69 | section | 1 of 2 | Mixed |
| HG1101-71 | section | 1 of 2 | Mixed |
| HG1101-72 | section | 1 of 2 | Mixed |
| HG1101-74 | section | 1 of 2 | AI |
| HG1101-84 | section | 1 of 2 | Mixed |
| HG1101-93 | section | 1 of 2 | Mixed |
| HG1101-99 | section | 1 of 2 | Mixed |

