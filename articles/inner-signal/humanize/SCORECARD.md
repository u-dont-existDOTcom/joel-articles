# Pangram prediction scorecard: hypnosis guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-signal/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 944 | 803 (85%) | 22% | 78% | 89% | 0.120 (base 0.174, 944) |
| pangram 4.1, Pangram's check of the Substack draft (free, Joel's account) | 38 | 32 (84%) | 84% | 16% | 5% | 0.119 (base 0.133, 38) |
| pangram 4.1, web app | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |
| pangram 4.1, the API (Joel's key, run on his laptop; E218) | 52 | 34 (65%) | 33% | 67% | 87% | 0.193 (base 0.220, 52) |
| pangram API (model pangram-4, expect 4.1), Joel's key, run on the laptop | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |
| Pangram 4.1 (web app) | 124 | 103 (83%) | 24% | 76% | 78% | 0.183 (base 0.183, 124) |

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
| the latest 50 | 50 | 33 (66%) | 32% | 68% | 90% | 0.190 (base 0.218, 50) |
| the latest 100 | 52 | 34 (65%) | 33% | 67% | 87% | 0.193 (base 0.220, 52) |
| all | 52 | 34 (65%) | 33% | 67% | 87% | 0.193 (base 0.220, 52) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pair | 23 | 15 (65%) | 39% | 61% | 78% | 0.187 (base 0.238, 23) |
| paragraph | 5 | 3 (60%) | 40% | 60% | 100% | 0.188 (base 0.240, 5) |
| stretch | 6 | 3 (50%) | 50% | 50% | 100% | 0.255 (base 0.250, 6) |
| section | 18 | 13 (72%) | 17% | 83% | 89% | 0.180 (base 0.139, 18) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 1 | 0.15 | 0% |
| 0.2 to 0.4 | 2 | 0.28 | 50% |
| 0.4 to 0.6 | 28 | 0.54 | 61% |
| 0.6 to 0.8 | 19 | 0.65 | 79% |
| 0.8 to 1.0 | 12 | 0.85 | 92% |

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
| the latest 50 | 50 | 43 (86%) | 28% | 72% | 74% | 0.171 (base 0.202, 50) |
| the latest 100 | 100 | 83 (83%) | 26% | 74% | 75% | 0.183 (base 0.192, 100) |
| all | 124 | 103 (83%) | 24% | 76% | 78% | 0.183 (base 0.183, 124) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 114 | 93 (82%) | 21% | 79% | 82% | 0.185 (base 0.166, 114) |
| paragraph | 8 | 8 (100%) | 50% | 50% | 50% | 0.170 (base 0.250, 8) |
| pair | 2 | 2 (100%) | 100% | 0% | 0% | 0.163 (base 0.000, 2) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 5 | 0.27 | 40% |
| 0.4 to 0.6 | 91 | 0.55 | 73% |
| 0.6 to 0.8 | 91 | 0.64 | 89% |

## Misses since the ledger (52)

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
| a rewrite of the words, not the shape | 1 |
| an opening generalization kept | 1 |
| a line restored untested from his inner child guide, without the example that follows it there | 1 |
| his opening read Human (Low) beside the lettered steps; Mostly Human Written at 5.8% with no AI window | 1 |
| the approved script reads AI in the section; my prediction took his own check of a longer passage as the base | 1 |
| pessimism: his Patterns 3 to 7 (Human High by themselves) carried a long section | 1 |
| pessimism about the list numbers | 1 |
| the script reads AI (Low) after his rewrite; his check of this passage had other words | 1 |
| my fix put a new list of three in place of the old one ('Maybe your fingers..., or your breath..., or your attention...') | 1 |
| the questions said as a run of instructions in our voice ('Then find out ... check whether ... And ask ...') | 1 |
| the three echoes as three steps still read as a list, and the plainer climb read AI (Medium) beside them | 1 |
| the Meta Model's list of questions, unchanged, read AI (Low and Medium) in this stretch; in the section it read Human (Low and Medium) | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [s1101-95](https://www.pangram.com/history/8be96f9e-57b6-41f4-86ec-808c276c90f8) | HG1101-95, 1 | AI | Human | **not explained yet** |
| [s1101-96](https://www.pangram.com/history/78cb97fc-9eb9-44a6-9de3-2988a428ebd1) | HG1101-96, 1 | AI | Human | **not explained yet** |
| [s1101-99](https://www.pangram.com/history/2122b7a5-8950-4926-9037-81d41cfbf928) | HG1101-99, 1 | Human | AI or mixed | **not explained yet** |
| [r1101-59](https://www.pangram.com/history//34180952-89c5-44bb-8abe-521269bff5e2) | HG1101-59, 2 | Human | AI or mixed | a rewrite of the words, not the shape |
| [r1101-93](https://www.pangram.com/history//814667a4-d788-4dd1-a0d9-f941a0cf8ea5) | HG1101-93, 2 | Human | AI or mixed | an opening generalization kept |
| [r1102-15](https://www.pangram.com/history/1050793a-1f08-47d0-aac9-098afd0e5408) | HG1101-15, 2 | Human | AI or mixed | a line restored untested from his inner child guide, without the example that follows it there |
| [r1102-27](https://www.pangram.com/history/03338373-12c4-41ab-bbda-694159cd0d2e) | HG1101-27, 2 | Human | AI or mixed | his opening read Human (Low) beside the lettered steps; Mostly Human Written at 5.8% with no AI window |
| [r1102-40](https://www.pangram.com/history/93ac0152-0715-4cde-b8ff-d6544781099d) | HG1101-40, 2 | Human | AI or mixed | the approved script reads AI in the section; my prediction took his own check of a longer passage as the base |
| [r1102-69](https://www.pangram.com/history/b6b3ac4c-810e-4d4f-a2db-15d7bd4125fe) | HG1101-69, 2 | AI | Human | pessimism: his Patterns 3 to 7 (Human High by themselves) carried a long section |
| [r1102-99](https://www.pangram.com/history/980437b6-2192-4223-afef-d79c3b68486b) | HG1101-99, 2 | AI | Human | pessimism about the list numbers |
| [r1102b-B0](https://www.pangram.com/history/1087d1e2-6e20-41b5-8b2e-81d64be3b2cf) | HG1102-W282, 1 | Human | AI or mixed | the script reads AI (Low) after his rewrite; his check of this passage had other words |
| [r1102b-B3](https://www.pangram.com/history/c6990553-fb90-4cc5-ae42-42fd1e0caa26) | HG1102-40-S, 1 | Human | AI or mixed | my fix put a new list of three in place of the old one ('Maybe your fingers..., or your breath..., or your attention...') |
| [r1102b-D2](https://www.pangram.com/history/a68f6b1e-1ea6-4c31-b9a7-33ba058c8e2b) | HG1102-69-P10, 1 | Human | AI or mixed | the questions said as a run of instructions in our voice ('Then find out ... check whether ... And ask ...') |
| [r1102b-B4](https://www.pangram.com/history/ecf802cd-e675-4bf6-9845-87870cddf8b4) | HG1102-40-S, 2 | Human | AI or mixed | the three echoes as three steps still read as a list, and the plainer climb read AI (Medium) beside them |
| [r1102b-D1](https://www.pangram.com/history/cebaccad-d951-4faf-8f36-282f80d44271) | HG1102-69-P10, 2 | Human | AI or mixed | the Meta Model's list of questions, unchanged, read AI (Low and Medium) in this stretch; in the section it read Human (Low and Medium) |

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
| HG1101-15 | section | 2 of 2 | Mixed |
| HG1101-17 | section | 2 of 2 | AI |
| HG1101-27 | section | 2 of 2 | Mixed |
| HG1101-40 | section | 2 of 2 | Mixed |
| HG1101-44 | section | 2 of 2 | Mixed |
| HG1101-53 | section | 2 of 2 | AI |
| HG1101-59 | section | 2 of 2 | Mixed |
| HG1101-93 | section | 2 of 2 | Mixed |
| HG1101-17-P23 | pair | 1 of 6 | Mixed |
| HG1101-44-P5 | paragraph | 1 of 6 | AI |
| HG1101-44-P6 | paragraph | 1 of 6 | AI |
| HG1101-53-P1 | paragraph | 1 of 6 | AI |
| HG1101-53-P12 | pair | 1 of 6 | AI |
| HG1101-59-P1 | paragraph | 1 of 6 | AI |
| HG1102-40-S | pair | 2 of 6 | Mixed |
| HG1102-69-P10 | stretch | 2 of 2 | Mixed |

