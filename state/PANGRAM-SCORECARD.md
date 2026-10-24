# Pangram prediction scorecard: every lane

Built by `tools/humanization/pangram_ledger.py build --universal` from each lane's ledger and older records (`tools/humanization/pangram_lanes.json` lists the lanes; each lane's own page has the detail). Rows are pooled only within one detector version, and the boundary mix is shown beside every pooled number, as the budget rule asks (`docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`).

## Pangram 4.0 (before the ledger)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 1905 | 1397 (73%) | 44% | 56% | 66% | - |
| hypnosis guide | 944 | 803 (85%) | 22% | 78% | 89% | 0.120 (base 0.174, 944) |
| inner child guide | 3085 | 1395 (45%) | 57% | 43% | 96% | - |
| **all lanes** | 5934 | 3595 (61%) | 47% | 53% | 85% | 0.120 (base 0.174, 944) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 100 | 81 (81%) | 21% | 79% | 96% | - |
| hypnosis guide | 100 | 83 (83%) | 25% | 75% | 90% | 0.148 (base 0.188, 100) |
| inner child guide | 100 | 63 (63%) | 37% | 63% | 100% | - |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 2241 | 961 (43%) | 59% | 41% | 96% | - |
| unrecorded | 1398 | 913 (65%) | 51% | 49% | 69% | - |
| emulate | 846 | 723 (85%) | 17% | 83% | 95% | 0.119 (base 0.141, 846) |
| section | 616 | 349 (57%) | 44% | 56% | 93% | - |
| screen | 516 | 386 (75%) | 41% | 59% | 69% | - |
| edit | 125 | 100 (80%) | 30% | 70% | 78% | 0.180 (base 0.248, 61) |
| draft | 87 | 63 (72%) | 28% | 72% | 72% | - |
| owner | 68 | 64 (94%) | 43% | 57% | 60% | - |
| baseline | 37 | 36 (97%) | 92% | 8% | 11% | 0.026 (base 0.075, 37) |

## pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 20 | 16 (80%) | 80% | 20% | 10% | 0.155 (base 0.160, 20) |
| nibbana article | 8 | 7 (88%) | 88% | 12% | 0% | 0.086 (base 0.109, 8) |
| **all lanes** | 28 | 23 (82%) | 82% | 18% | 7% | 0.135 (base 0.147, 28) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 20 | 16 (80%) | 80% | 20% | 10% | 0.155 (base 0.160, 20) |
| nibbana article | 8 | 7 (88%) | 88% | 12% | 0% | 0.086 (base 0.109, 8) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 16 | 13 (81%) | 88% | 12% | 6% | 0.120 (base 0.109, 16) |
| stretch | 12 | 10 (83%) | 75% | 25% | 8% | 0.155 (base 0.188, 12) |

## pangram 4.1, web app

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |
| **all lanes** | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 10 | 6 (60%) | 40% | 60% | 80% | 0.195 (base 0.240, 10) |
| section | 4 | 2 (50%) | 50% | 50% | 100% | 0.214 (base 0.250, 4) |

## pangram 4.1, the API (Joel's key, run on his laptop; E218)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 20 | 12 (60%) | 45% | 55% | 75% | 0.216 (base 0.247, 20) |
| nibbana article | 21 | 10 (48%) | 67% | 33% | 67% | 0.225 (base 0.222, 21) |
| **all lanes** | 41 | 22 (54%) | 56% | 44% | 71% | 0.220 (base 0.246, 41) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 20 | 12 (60%) | 45% | 55% | 75% | 0.216 (base 0.247, 20) |
| nibbana article | 21 | 10 (48%) | 67% | 33% | 67% | 0.225 (base 0.222, 21) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 21 | 11 (52%) | 62% | 38% | 67% | 0.220 (base 0.236, 21) |
| pair | 19 | 10 (53%) | 53% | 47% | 74% | 0.222 (base 0.249, 19) |
| stretch | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |

## Pangram 4.1 GUI (dashboard)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| **all lanes** | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |

## pangram-4.1-substack

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 66 | 41 (62%) | 53% | 47% | 48% | 0.203 (base 0.249, 66) |
| **all lanes** | 66 | 41 (62%) | 53% | 47% | 48% | 0.203 (base 0.249, 66) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 66 | 41 (62%) | 53% | 47% | 48% | 0.203 (base 0.249, 66) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 47 | 25 (53%) | 47% | 53% | 49% | 0.246 (base 0.249, 47) |
| stretch | 12 | 10 (83%) | 100% | 0% | 17% | 0.079 (base 0.000, 12) |
| section | 7 | 6 (86%) | 14% | 86% | 100% | 0.128 (base 0.122, 7) |

## pangram-4.1-api

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 101 | 76 (75%) | 40% | 60% | 75% | 0.203 (base 0.239, 101) |
| **all lanes** | 101 | 76 (75%) | 40% | 60% | 75% | 0.203 (base 0.239, 101) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 100 | 75 (75%) | 39% | 61% | 76% | 0.203 (base 0.238, 100) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 50 | 37 (74%) | 40% | 60% | 78% | 0.202 (base 0.240, 50) |
| section | 33 | 24 (73%) | 42% | 58% | 73% | 0.212 (base 0.244, 33) |
| stretch | 18 | 15 (83%) | 33% | 67% | 72% | 0.189 (base 0.222, 18) |

## What the misses say (since the ledger)

| cause | misses | lanes |
|---|---|---|
| too pessimistic about a cut | 12 | inner child guide |
| a tell I did not name | 9 | inner child guide |
| a Low window came back | 7 | inner child guide |
| a paragraph alone is harsher than the article | 7 | nibbana article |
| balanced closer kept | 3 | hypnosis guide |
| not explained yet | 3 | inner child guide |
| an added move read AI | 3 | inner child guide |
| parallel list kept | 2 | hypnosis guide |
| context: red in the whole guide, Human in the pair | 2 | hypnosis guide |
| six versions, same reading: the method is spent | 2 | hypnosis guide |
| a window moved onto his line | 2 | inner child guide |
| a second cut of the same kind | 2 | inner child guide |
| the section read differently from the paragraph alone | 2 | inner child guide |
| too pessimistic about a rewrite | 2 | inner child guide |
| a repeat made adjacent by a move | 2 | inner child guide |
| his paragraph reads AI alone under 4.1 | 2 | inner child guide |
| parallel list kept; light green turned red | 1 | hypnosis guide |
| fix underrated | 1 | hypnosis guide |
| tells overweighted | 1 | hypnosis guide |
| a red window read as its first section's | 1 | hypnosis guide |
| the same skeleton reworded | 1 | hypnosis guide |
| tidy closers at both paragraphs' ends | 1 | hypnosis guide |
| tidy closer | 1 | hypnosis guide |
| a linter fix that read worse | 1 | hypnosis guide |
| pessimism about Emulate's whole-stretch re-run | 1 | hypnosis guide |
| a tell I left in | 1 | inner child guide |
| his questions are the tell | 1 | inner child guide |
| the list was not the only tell | 1 | inner child guide |
| the half varies | 1 | inner child guide |
| Low windows with no AI window | 1 | inner child guide |
| a Low window read Human | 1 | nibbana article |
| underrated a plain split | 1 | nibbana article |
| a neutral signpost reads AI where his casual frame read Human | 1 | nibbana article |
| a misread page: the caution never read Human | 1 | nibbana article |
| pessimism | 1 | nibbana article |

A cause that repeats becomes a check that runs before Pangram (a linter rule, a gate step or a predictor feature); a miss nobody can explain goes to Joel with the passage.

