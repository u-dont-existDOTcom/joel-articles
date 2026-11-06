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
| community article | 1 | 0 (0%) | 0% | 100% | 0% | 0.865 (base 0.000, 1) |
| hypnosis guide | 46 | 38 (83%) | 78% | 22% | 9% | 0.126 (base 0.170, 46) |
| nibbana article | 8 | 7 (88%) | 88% | 12% | 0% | 0.086 (base 0.109, 8) |
| healing the gut article | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |
| **all lanes** | 56 | 46 (82%) | 77% | 23% | 9% | 0.135 (base 0.178, 56) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 1 | 0 (0%) | 0% | 100% | 0% | 0.865 (base 0.000, 1) |
| hypnosis guide | 46 | 38 (83%) | 78% | 22% | 9% | 0.126 (base 0.170, 46) |
| nibbana article | 8 | 7 (88%) | 88% | 12% | 0% | 0.086 (base 0.109, 8) |
| healing the gut article | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 44 | 36 (82%) | 77% | 23% | 9% | 0.129 (base 0.176, 44) |
| stretch | 12 | 10 (83%) | 75% | 25% | 8% | 0.155 (base 0.188, 12) |

## pangram API (model pangram-4), answered 4.1

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 5 | 3 (60%) | 20% | 80% | 80% | 0.233 (base 0.160, 5) |
| **all lanes** | 5 | 3 (60%) | 20% | 80% | 80% | 0.233 (base 0.160, 5) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 5 | 3 (60%) | 20% | 80% | 80% | 0.233 (base 0.160, 5) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 4 | 3 (75%) | 0% | 100% | 75% | 0.089 (base 0.000, 4) |
| pair | 1 | 0 (0%) | 100% | 0% | 100% | 0.810 (base 0.000, 1) |

## Pangram 4.1 (web app)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 13 | 10 (77%) | 15% | 85% | 92% | 0.169 (base 0.130, 13) |
| hypnosis guide | 124 | 103 (83%) | 24% | 76% | 78% | 0.183 (base 0.183, 124) |
| healing the gut article | 10 | 5 (50%) | 70% | 30% | 80% | 0.224 (base 0.210, 10) |
| **all lanes** | 147 | 118 (80%) | 27% | 73% | 80% | 0.185 (base 0.195, 147) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 13 | 10 (77%) | 15% | 85% | 92% | 0.169 (base 0.130, 13) |
| hypnosis guide | 100 | 83 (83%) | 26% | 74% | 75% | 0.183 (base 0.192, 100) |
| healing the gut article | 10 | 5 (50%) | 70% | 30% | 80% | 0.224 (base 0.210, 10) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 130 | 104 (80%) | 22% | 78% | 82% | 0.185 (base 0.173, 130) |
| paragraph | 12 | 11 (92%) | 42% | 58% | 67% | 0.181 (base 0.243, 12) |
| pair | 5 | 3 (60%) | 100% | 0% | 40% | 0.197 (base 0.000, 5) |

## pangram 4.1, the API (Joel's key, run on his laptop; E218)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 3 | 3 (100%) | 0% | 100% | 100% | 0.115 (base 0.000, 3) |
| hypnosis guide | 68 | 42 (62%) | 40% | 60% | 87% | 0.208 (base 0.239, 68) |
| nibbana article | 21 | 10 (48%) | 67% | 33% | 67% | 0.225 (base 0.222, 21) |
| **all lanes** | 92 | 55 (60%) | 45% | 55% | 83% | 0.209 (base 0.247, 92) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| community article | 3 | 3 (100%) | 0% | 100% | 100% | 0.115 (base 0.000, 3) |
| hypnosis guide | 68 | 42 (62%) | 40% | 60% | 87% | 0.208 (base 0.239, 68) |
| nibbana article | 21 | 10 (48%) | 67% | 33% | 67% | 0.225 (base 0.222, 21) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 32 | 21 (66%) | 28% | 72% | 94% | 0.208 (base 0.202, 32) |
| pair | 27 | 16 (59%) | 44% | 56% | 81% | 0.197 (base 0.247, 27) |
| paragraph | 23 | 13 (57%) | 57% | 43% | 70% | 0.205 (base 0.246, 23) |
| stretch | 10 | 5 (50%) | 70% | 30% | 80% | 0.250 (base 0.210, 10) |

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

## pangram API (model pangram-4, expect 4.1), Joel's key, run on the laptop

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |
| **all lanes** | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 5 | 4 (80%) | 20% | 80% | 100% | 0.187 (base 0.160, 5) |
| pair | 2 | 2 (100%) | 0% | 100% | 100% | 0.181 (base 0.000, 2) |

## pangram 4.1, the API (Joel's key, run on his laptop; E218, E325)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |
| **all lanes** | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| hypnosis guide | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |

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
| inner child guide | 104 | 76 (73%) | 40% | 60% | 62% | 0.183 (base 0.241, 104) |
| **all lanes** | 104 | 76 (73%) | 40% | 60% | 62% | 0.183 (base 0.241, 104) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 100 | 74 (74%) | 38% | 62% | 62% | 0.183 (base 0.236, 100) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 51 | 29 (57%) | 43% | 57% | 53% | 0.242 (base 0.245, 51) |
| section | 31 | 28 (90%) | 10% | 90% | 100% | 0.140 (base 0.087, 31) |
| stretch | 22 | 19 (86%) | 77% | 23% | 27% | 0.104 (base 0.176, 22) |

## pangram-4.1-api

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 213 | 167 (78%) | 31% | 69% | 85% | 0.192 (base 0.214, 213) |
| **all lanes** | 213 | 167 (78%) | 31% | 69% | 85% | 0.192 (base 0.214, 213) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 100 | 85 (85%) | 18% | 82% | 97% | 0.175 (base 0.148, 100) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 113 | 88 (78%) | 32% | 68% | 85% | 0.186 (base 0.217, 113) |
| section | 80 | 62 (78%) | 29% | 71% | 89% | 0.202 (base 0.205, 80) |
| stretch | 20 | 17 (85%) | 35% | 65% | 70% | 0.182 (base 0.227, 20) |

## Pangram 4.1 (API)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 5 | 3 (60%) | 60% | 40% | 40% | 0.232 (base 0.240, 5) |
| **all lanes** | 5 | 3 (60%) | 60% | 40% | 40% | 0.232 (base 0.240, 5) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| inner child guide | 5 | 3 (60%) | 60% | 40% | 40% | 0.232 (base 0.240, 5) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 3 | 2 (67%) | 67% | 33% | 0% | 0.247 (base 0.222, 3) |
| section | 2 | 1 (50%) | 50% | 50% | 100% | 0.211 (base 0.250, 2) |

## Pangram 4.1 extension (free, live post; Joel's check of 2026-10-18, the same text as his 2026-11-03 paste by SHA-256)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| bad trips guide | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |
| **all lanes** | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| bad trips guide | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |

## Pangram web app (his account, Pangram Professional)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| bad trips guide | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |
| **all lanes** | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| bad trips guide | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 2 | 2 (100%) | 100% | 0% | 0% | 0.106 (base 0.000, 2) |
| section | 1 | 1 (100%) | 100% | 0% | 0% | 0.062 (base 0.000, 1) |

## Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| bad trips guide | 41 | 34 (83%) | 71% | 29% | 46% | 0.167 (base 0.207, 41) |
| **all lanes** | 41 | 34 (83%) | 71% | 29% | 46% | 0.167 (base 0.207, 41) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| bad trips guide | 41 | 34 (83%) | 71% | 29% | 46% | 0.167 (base 0.207, 41) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 29 | 26 (90%) | 62% | 38% | 48% | 0.160 (base 0.235, 29) |
| pair | 8 | 6 (75%) | 100% | 0% | 25% | 0.182 (base 0.000, 8) |
| section | 4 | 2 (50%) | 75% | 25% | 75% | 0.185 (base 0.188, 4) |

## pangram 4.1, the web app: Joel's account, run by the lane in the desktop app's browser pane (E356)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| bad trips guide | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |
| **all lanes** | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| bad trips guide | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |

## pangram API 4.1

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| healing the gut article | 97 | 71 (73%) | 55% | 45% | 47% | 0.173 (base 0.248, 97) |
| **all lanes** | 97 | 71 (73%) | 55% | 45% | 47% | 0.173 (base 0.248, 97) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| healing the gut article | 97 | 71 (73%) | 55% | 45% | 47% | 0.173 (base 0.248, 97) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 88 | 63 (72%) | 56% | 44% | 45% | 0.180 (base 0.247, 88) |
| section | 9 | 8 (89%) | 44% | 56% | 67% | 0.106 (base 0.247, 9) |

## pangram 4.1, the web app (Joel's account, GUI credits)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| healing the gut article | 51 | 43 (84%) | 16% | 84% | 96% | 0.156 (base 0.132, 51) |
| **all lanes** | 51 | 43 (84%) | 16% | 84% | 96% | 0.156 (base 0.132, 51) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| healing the gut article | 51 | 43 (84%) | 16% | 84% | 96% | 0.156 (base 0.132, 51) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 25 | 21 (84%) | 16% | 84% | 92% | 0.147 (base 0.134, 25) |
| stretch | 14 | 12 (86%) | 14% | 86% | 100% | 0.168 (base 0.122, 14) |
| pair | 9 | 7 (78%) | 22% | 78% | 100% | 0.174 (base 0.173, 9) |
| paragraph | 3 | 3 (100%) | 0% | 100% | 100% | 0.128 (base 0.000, 3) |

## pangram 4.1, his Pangram extension on the live post (free, Joel's account)

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| healing the gut article | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |
| **all lanes** | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

The latest 100 calls of each lane:

| lane | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| healing the gut article | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

The boundary mix over all lanes:

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

## What the misses say (since the ledger)

| cause | misses | lanes |
|---|---|---|
| not explained yet | 50 | bad trips guide, community article, healing the gut article, hypnosis guide, inner child guide |
| too pessimistic about a cut | 12 | inner child guide |
| a tell I did not name | 11 | inner child guide |
| a Low window came back | 8 | inner child guide |
| a paragraph alone is harsher than the article | 8 | inner child guide, nibbana article |
| context | 7 | healing the gut article |
| balanced closer kept | 4 | healing the gut article, hypnosis guide |
| model-over-pessimism | 4 | healing the gut article |
| context: red in the whole guide, Human in the pair | 3 | healing the gut article, hypnosis guide |
| an added move read AI | 3 | inner child guide |
| the section read differently from the paragraph alone | 3 | inner child guide |
| too pessimistic about a rewrite | 3 | inner child guide |
| explainer structure | 3 | healing the gut article |
| pessimism | 2 | community article, nibbana article |
| parallel list kept | 2 | hypnosis guide |
| six versions, same reading: the method is spent | 2 | hypnosis guide |
| the fix made its stretch worse | 2 | hypnosis guide |
| pessimism about cuts | 2 | hypnosis guide |
| a window moved onto his line | 2 | inner child guide |
| a second cut of the same kind | 2 | inner child guide |
| a repeat made adjacent by a move | 2 | inner child guide |
| his paragraph reads AI alone under 4.1 | 2 | inner child guide |
| one-sentence-stuck | 2 | healing the gut article |
| one step a sentence not applied | 2 | healing the gut article |
| tells | 2 | healing the gut article |
| the unchanged neighbour | 1 | community article |
| a window the test made | 1 | community article |
| parallel list kept; light green turned red | 1 | hypnosis guide |
| fix underrated | 1 | hypnosis guide |
| tells overweighted | 1 | hypnosis guide |
| a red window read as its first section's | 1 | hypnosis guide |
| the same skeleton reworded | 1 | hypnosis guide |
| tidy closers at both paragraphs' ends | 1 | hypnosis guide |
| tidy closer | 1 | hypnosis guide |
| a linter fix that read worse | 1 | hypnosis guide |
| pessimism about Emulate's whole-stretch re-run | 1 | hypnosis guide |
| context: Human in the whole guide, red alone | 1 | hypnosis guide |
| pessimism about red moving onto unchanged text | 1 | hypnosis guide |
| pessimism about the whole text, again | 1 | hypnosis guide |
| a rewrite of the words, not the shape | 1 | hypnosis guide |
| an opening generalization kept | 1 | hypnosis guide |
| a line restored untested from his inner child guide, without the example that follows it there | 1 | hypnosis guide |
| his opening read Human (Low) beside the lettered steps; Mostly Human Written at 5.8% with no AI window | 1 | hypnosis guide |
| the approved script reads AI in the section; my prediction took his own check of a longer passage as the base | 1 | hypnosis guide |
| pessimism: his Patterns 3 to 7 (Human High by themselves) carried a long section | 1 | hypnosis guide |
| pessimism about the list numbers | 1 | hypnosis guide |
| the script reads AI (Low) after his rewrite; his check of this passage had other words | 1 | hypnosis guide |
| my fix put a new list of three in place of the old one ('Maybe your fingers..., or your breath..., or your attention...') | 1 | hypnosis guide |
| the questions said as a run of instructions in our voice ('Then find out ... check whether ... And ask ...') | 1 | hypnosis guide |
| the three echoes as three steps still read as a list, and the plainer climb read AI (Medium) beside them | 1 | hypnosis guide |
| the Meta Model's list of questions, unchanged, read AI (Low and Medium) in this stretch; in the section it read Human (Low and Medium) | 1 | hypnosis guide |
| ten short windows read AI in the whole half that read Human in their sections or pairs (E319): the guards questions, the sober induction's directions, two maxims | 1 | hypnosis guide |
| two windows of his forgiveness text read AI in the whole half; by itself it read Human (High) for him | 1 | hypnosis guide |
| my rewrites F-11 and F-16 read AI (High) themselves: the minds said as a run of short declaratives, one per sentence ('Your inner child still wants... The guards are bracing... Meanwhile your body remembers... Intuition speaks up...'), and the asides folded into 'because ... I also borrow ... since ..., since ...'; the original read Human by itself | 1 | hypnosis guide |
| cutting F-218 left the heading running straight into 'Indirect suggestions can bypass the subject's skeptical guard.', which read Human (Low); the section with the sentence read Human by itself | 1 | hypnosis guide |
| my F-251 ('Just don't get poetic ... as plain as a fire exit sign.') read AI (Low): a joke-shaped closer is still a closer | 1 | hypnosis guide |
| my F-253 read AI (High and three Low): the anchor options split into short sentences ('Pick one thing to anchor yourself with. It could be ... The two-hand practice from above is another good one.') are the same instructions in a tidier row; F-255 and F-265 were not flagged | 1 | hypnosis guide |
| my F-527 ('pin it back down ... which is how you keep the first one honest') read AI (Medium) and F-528's workshop leader example Human (Low): an explaining clause in place of the closer is still a closer, and the example sat in front of six questions | 1 | hypnosis guide |
| his own inner child guide's line (C-626, 'No warmth today? Then rest your hands there and notice what you find, no faking required.') read AI (High) here, after 'Make sure you're actually talking to your inner child, not just repeating a script.' (AI Low); his line is not offered as a card | 1 | hypnosis guide |
| pessimism about a run of questions | 1 | hypnosis guide |
| a tell I left in | 1 | inner child guide |
| his questions are the tell | 1 | inner child guide |
| the list was not the only tell | 1 | inner child guide |
| the half varies | 1 | inner child guide |
| Low windows with no AI window | 1 | inner child guide |
| a Human result above 0.0000 | 1 | inner child guide |
| a cut took out what read human | 1 | inner child guide |
| an old AI window carried over | 1 | inner child guide |
| too pessimistic about his words | 1 | inner child guide |
| a Low window read Human | 1 | nibbana article |
| underrated a plain split | 1 | nibbana article |
| a neutral signpost reads AI where his casual frame read Human | 1 | nibbana article |
| a misread page: the caution never read Human | 1 | nibbana article |
| shape echo | 1 | bad trips guide |
| parallel frames kept | 1 | bad trips guide |
| a flaw of sense left in the ending | 1 | bad trips guide |
| rewording without a sense fix | 1 | bad trips guide |
| summary-voice-around-owner-lines | 1 | healing the gut article |
| owner-voice-carries-neighbours | 1 | healing the gut article |
| opener-and-attribution-asides | 1 | healing the gut article |
| owner-lines-human-gemini-lines-ai | 1 | healing the gut article |
| owner-line-human-kit-run-ai | 1 | healing the gut article |
| plain-conditional-warning-human | 1 | healing the gut article |
| panel-overflags | 1 | healing the gut article |
| panel-overflags-labels-were-the-tell | 1 | healing the gut article |
| reader-question-did-not-carry | 1 | healing the gut article |
| links stated as a glossary | 1 | healing the gut article |
| every sentence a so-chain | 1 | healing the gut article |
| my new claims in an explainer's frame | 1 | healing the gut article |
| term explained after its first use, and a note splitting a sentence before its point (gates E368, E369) | 1 | healing the gut article |
| the point after the names, and a note splitting his sentence (gate E368) | 1 | healing the gut article |

A cause that repeats becomes a check that runs before Pangram (a linter rule, a gate step or a predictor feature); a miss nobody can explain goes to Joel with the passage.

