# Pangram prediction scorecard: hypnosis guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-signal/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 944 | 803 (85%) | 22% | 78% | 89% | 0.120 (base 0.174, 944) |
| pangram 4.1, Pangram's check of the Substack draft (free, Joel's account) | 18 | 15 (83%) | 83% | 17% | 11% | 0.129 (base 0.139, 18) |
| pangram 4.1, web app | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |
| pangram 4.1, the API (Joel's key, run on his laptop; E218) | 20 | 12 (60%) | 45% | 55% | 75% | 0.216 (base 0.247, 20) |

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
| the latest 50 | 18 | 15 (83%) | 83% | 17% | 11% | 0.129 (base 0.139, 18) |
| the latest 100 | 18 | 15 (83%) | 83% | 17% | 11% | 0.129 (base 0.139, 18) |
| all | 18 | 15 (83%) | 83% | 17% | 11% | 0.129 (base 0.139, 18) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 6 | 5 (83%) | 100% | 0% | 17% | 0.075 (base 0.000, 6) |
| stretch | 12 | 10 (83%) | 75% | 25% | 8% | 0.155 (base 0.188, 12) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 6 | 0.06 | 0% |
| 0.2 to 0.4 | 7 | 0.33 | 14% |
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

## Misses since the ledger (17)

| cause | misses |
|---|---|
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

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [HG15-w467](https://www.pangram.com/history/9cfccd99-95ce-49b0-a65a-47216c218f42) | HG15, 1 | Human | AI or mixed | balanced closer kept |
| [HG35-w467](https://www.pangram.com/history/74763536-ab88-4ec2-b347-0e186b0208ad) | HG35, 1 | Human | AI or mixed | parallel list kept; light green turned red |
| [HG15-p9e2](https://www.pangram.com/history/b252243a-a20d-4f01-8643-7551ffcb5d56) | HG15-p9, 2 | Human | AI or mixed | balanced closer kept |
| [HG35-forgive-e3](https://www.pangram.com/history/637e6fb4-3a47-4fe6-899f-b5ff0923e7f3) | HG35-p13, 2 | AI | Human | fix underrated |
| [screen-S2](https://www.pangram.com/feed/e836ef9c-c964-4012-a5af-994ef88658eb) | HG17-emu-bd, 1 | AI | Human | tells overweighted |
| [screen2-B0](https://www.pangram.com/feed/5af06c6a-8f56-4bd7-9c86-5e9813f7a97e) | HG31-nlp-tail, 1 | AI | Human | a red window read as its first section's |
| [b472_s1_base](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md#b472_s1_base) | HG16-B209, 1 | AI | Human | context: red in the whole guide, Human in the pair |
| [b472_s3_base](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md#b472_s3_base) | HG18-B311, 1 | AI | Human | context: red in the whole guide, Human in the pair |
| [b472_s2d](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md#b472_s2d) | HG18-B308, 3 | Human | AI or mixed | the same skeleton reworded |
| [b472_s2e](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md#b472_s2e) | HG18-B308, 4 | Human | AI or mixed | tidy closers at both paragraphs' ends |
| [b472_s2e_alone](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md#b472_s2e_alone) | HG17-B306, 2 | Human | AI or mixed | tidy closer |
| [b472_s2f](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md#b472_s2f) | HG18-B308, 5 | Human | AI or mixed | six versions, same reading: the method is spent |
| [b472_s2f_alone](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md#b472_s2f_alone) | HG17-B306, 3 | Human | AI or mixed | six versions, same reading: the method is spent |
| [b472_s1c](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md#b472_s1c) | HG16-B209, 3 | Human | AI or mixed | a linter fix that read worse |
| [HG-rest-41r4-b](https://www.pangram.com/feed/1db9825e-5fed-4528-aca5-9d4272b54f83) | HG-rest-B, 3 | Human | AI or mixed | parallel list kept |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| HG-whole | article | 5 of unlimited (Substack) | Mixed |
| HG-rest-B | article | 3 of unlimited (Substack) | Mixed |
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

