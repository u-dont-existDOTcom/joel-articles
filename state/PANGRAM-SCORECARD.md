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
| hypnosis guide | 15 | 13 (87%) | 80% | 20% | 7% | 0.125 (base 0.160, 15) |
| **all lanes** | 15 | 13 (87%) | 80% | 20% | 7% | 0.125 (base 0.160, 15) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 15 | 13 (87%) | 80% | 20% | 7% | 0.125 (base 0.160, 15) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 12 | 10 (83%) | 75% | 25% | 8% | 0.155 (base 0.188, 12) |
| article | 3 | 3 (100%) | 100% | 0% | 0% | 0.004 (base 0.000, 3) |

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
| hypnosis guide | 14 | 6 (43%) | 64% | 36% | 64% | 0.228 (base 0.230, 14) |
| nibbana article | 19 | 8 (42%) | 74% | 26% | 63% | 0.227 (base 0.194, 19) |
| **all lanes** | 33 | 14 (42%) | 70% | 30% | 64% | 0.227 (base 0.211, 33) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 14 | 6 (43%) | 64% | 36% | 64% | 0.228 (base 0.230, 14) |
| nibbana article | 19 | 8 (42%) | 74% | 26% | 63% | 0.227 (base 0.194, 19) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 17 | 7 (41%) | 76% | 24% | 59% | 0.227 (base 0.180, 17) |
| pair | 16 | 7 (44%) | 62% | 38% | 69% | 0.228 (base 0.234, 16) |

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
| inner child guide | 52 | 31 (60%) | 58% | 42% | 40% | 0.209 (base 0.244, 52) |
| **all lanes** | 52 | 31 (60%) | 58% | 42% | 40% | 0.209 (base 0.244, 52) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 52 | 31 (60%) | 58% | 42% | 40% | 0.209 (base 0.244, 52) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 41 | 22 (54%) | 49% | 51% | 44% | 0.243 (base 0.250, 41) |
| stretch | 10 | 8 (80%) | 100% | 0% | 20% | 0.088 (base 0.000, 10) |
| section | 1 | 1 (100%) | 0% | 100% | 100% | 0.040 (base 0.000, 1) |

## pangram-4.1-api

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 10 | 9 (90%) | 80% | 20% | 10% | 0.127 (base 0.160, 10) |
| **all lanes** | 10 | 9 (90%) | 80% | 20% | 10% | 0.127 (base 0.160, 10) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 10 | 9 (90%) | 80% | 20% | 10% | 0.127 (base 0.160, 10) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 8 | 7 (88%) | 75% | 25% | 12% | 0.128 (base 0.188, 8) |
| paragraph | 2 | 2 (100%) | 100% | 0% | 0% | 0.122 (base 0.000, 2) |

## What the misses say (since the ledger)

| cause | misses | lanes |
|---|---|---|
| too pessimistic about a cut | 12 | inner child guide |
| a paragraph alone is harsher than the article | 7 | nibbana article |
| balanced closer kept | 3 | hypnosis guide |
| not explained yet | 3 | inner child guide |
| context: red in the whole guide, Human in the pair | 2 | hypnosis guide |
| six versions, same reading: the method is spent | 2 | hypnosis guide |
| a second cut of the same kind | 2 | inner child guide |
| parallel list kept | 1 | hypnosis guide |
| parallel list kept; light green turned red | 1 | hypnosis guide |
| fix underrated | 1 | hypnosis guide |
| tells overweighted | 1 | hypnosis guide |
| a red window read as its first section's | 1 | hypnosis guide |
| the same skeleton reworded | 1 | hypnosis guide |
| tidy closers at both paragraphs' ends | 1 | hypnosis guide |
| tidy closer | 1 | hypnosis guide |
| a linter fix that read worse | 1 | hypnosis guide |
| a tell I did not name | 1 | inner child guide |
| a window moved onto his line | 1 | inner child guide |
| a tell I left in | 1 | inner child guide |
| an added move read AI | 1 | inner child guide |
| his questions are the tell | 1 | inner child guide |
| the list was not the only tell | 1 | inner child guide |
| a Low window read Human | 1 | nibbana article |
| underrated a plain split | 1 | nibbana article |
| a neutral signpost reads AI where his casual frame read Human | 1 | nibbana article |
| a misread page: the caution never read Human | 1 | nibbana article |

A cause that repeats becomes a check that runs before Pangram (a linter rule, a gate step or a predictor feature); a miss nobody can explain goes to Joel with the passage.

