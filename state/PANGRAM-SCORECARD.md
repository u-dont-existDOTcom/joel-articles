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
| hypnosis guide | 4 | 3 (75%) | 75% | 25% | 0% | 0.226 (base 0.188, 4) |
| **all lanes** | 4 | 3 (75%) | 75% | 25% | 0% | 0.226 (base 0.188, 4) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 4 | 3 (75%) | 75% | 25% | 0% | 0.226 (base 0.188, 4) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 2 | 2 (100%) | 100% | 0% | 0% | 0.001 (base 0.000, 2) |
| stretch | 2 | 1 (50%) | 50% | 50% | 0% | 0.451 (base 0.250, 2) |

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
| inner child guide | 6 | 4 (67%) | 100% | 0% | 33% | 0.602 (base 0.000, 6) |
| **all lanes** | 6 | 4 (67%) | 100% | 0% | 33% | 0.602 (base 0.000, 6) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 6 | 4 (67%) | 100% | 0% | 33% | 0.602 (base 0.000, 6) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 6 | 4 (67%) | 100% | 0% | 33% | 0.602 (base 0.000, 6) |

## What the misses say (since the ledger)

| cause | misses | lanes |
|---|---|---|
| balanced closer kept | 3 | hypnosis guide |
| not explained yet | 3 | inner child guide |
| parallel list kept | 1 | hypnosis guide |
| parallel list kept; light green turned red | 1 | hypnosis guide |
| fix underrated | 1 | hypnosis guide |
| verdict threshold misread | 1 | hypnosis guide |

A cause that repeats becomes a check that runs before Pangram (a linter rule, a gate step or a predictor feature); a miss nobody can explain goes to Joel with the passage.

