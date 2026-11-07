# Pangram prediction scorecard: hypnosis guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-signal/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 944 | 803 (85%) | 22% | 78% | 89% | 0.120 (base 0.174, 944) |
| pangram 4.1, Pangram's check of the Substack draft (free, Joel's account) | 46 | 38 (83%) | 78% | 22% | 9% | 0.126 (base 0.170, 46) |
| pangram 4.1, web app | 14 | 8 (57%) | 43% | 57% | 86% | 0.201 (base 0.245, 14) |
| pangram 4.1, the API (Joel's key, run on his laptop; E218) | 68 | 42 (62%) | 40% | 60% | 87% | 0.208 (base 0.239, 68) |
| pangram API (model pangram-4, expect 4.1), Joel's key, run on the laptop | 7 | 6 (86%) | 14% | 86% | 100% | 0.185 (base 0.122, 7) |
| Pangram 4.1 (web app) | 124 | 103 (83%) | 24% | 76% | 78% | 0.183 (base 0.183, 124) |
| pangram 4.1, the API (Joel's key, run on his laptop; E218, E325) | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |

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
| the latest 50 | 46 | 38 (83%) | 78% | 22% | 9% | 0.126 (base 0.170, 46) |
| the latest 100 | 46 | 38 (83%) | 78% | 22% | 9% | 0.126 (base 0.170, 46) |
| all | 46 | 38 (83%) | 78% | 22% | 9% | 0.126 (base 0.170, 46) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 34 | 28 (82%) | 79% | 21% | 9% | 0.115 (base 0.163, 34) |
| stretch | 12 | 10 (83%) | 75% | 25% | 8% | 0.155 (base 0.188, 12) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 27 | 0.05 | 7% |
| 0.2 to 0.4 | 11 | 0.31 | 36% |
| 0.4 to 0.6 | 6 | 0.46 | 33% |
| 0.6 to 0.8 | 2 | 0.70 | 100% |

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
| the latest 50 | 50 | 32 (64%) | 36% | 64% | 92% | 0.203 (base 0.230, 50) |
| the latest 100 | 68 | 42 (62%) | 40% | 60% | 87% | 0.208 (base 0.239, 68) |
| all | 68 | 42 (62%) | 40% | 60% | 87% | 0.208 (base 0.239, 68) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pair | 23 | 15 (65%) | 39% | 61% | 78% | 0.187 (base 0.238, 23) |
| paragraph | 5 | 3 (60%) | 40% | 60% | 100% | 0.188 (base 0.240, 5) |
| stretch | 10 | 5 (50%) | 70% | 30% | 80% | 0.250 (base 0.210, 10) |
| section | 30 | 19 (63%) | 30% | 70% | 93% | 0.213 (base 0.210, 30) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 1 | 0.15 | 0% |
| 0.2 to 0.4 | 2 | 0.28 | 50% |
| 0.4 to 0.6 | 37 | 0.54 | 51% |
| 0.6 to 0.8 | 30 | 0.65 | 70% |
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

## pangram 4.1, the API (Joel's key, run on his laptop; E218, E325)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |
| the latest 100 | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |
| all | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 11 | 8 (73%) | 18% | 82% | 91% | 0.217 (base 0.149, 11) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 10 | 0.55 | 80% |
| 0.6 to 0.8 | 5 | 0.62 | 80% |

## Misses since the ledger (65)

| cause | misses |
|---|---|
| not explained yet | 19 |
| balanced closer kept | 3 |
| parallel list kept | 2 |
| context: red in the whole guide, Human in the pair | 2 |
| six versions, same reading: the method is spent | 2 |
| the fix made its stretch worse | 2 |
| pessimism about cuts | 2 |
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
| ten short windows read AI in the whole half that read Human in their sections or pairs (E319): the guards questions, the sober induction's directions, two maxims | 1 |
| two windows of his forgiveness text read AI in the whole half; by itself it read Human (High) for him | 1 |
| my rewrites F-11 and F-16 read AI (High) themselves: the minds said as a run of short declaratives, one per sentence ('Your inner child still wants... The guards are bracing... Meanwhile your body remembers... Intuition speaks up...'), and the asides folded into 'because ... I also borrow ... since ..., since ...'; the original read Human by itself | 1 |
| cutting F-218 left the heading running straight into 'Indirect suggestions can bypass the subject's skeptical guard.', which read Human (Low); the section with the sentence read Human by itself | 1 |
| my F-251 ('Just don't get poetic ... as plain as a fire exit sign.') read AI (Low): a joke-shaped closer is still a closer | 1 |
| my F-253 read AI (High and three Low): the anchor options split into short sentences ('Pick one thing to anchor yourself with. It could be ... The two-hand practice from above is another good one.') are the same instructions in a tidier row; F-255 and F-265 were not flagged | 1 |
| my F-527 ('pin it back down ... which is how you keep the first one honest') read AI (Medium) and F-528's workshop leader example Human (Low): an explaining clause in place of the closer is still a closer, and the example sat in front of six questions | 1 |
| his own inner child guide's line (C-626, 'No warmth today? Then rest your hands there and notice what you find, no faking required.') read AI (High) here, after 'Make sure you're actually talking to your inner child, not just repeating a script.' (AI Low); his line is not offered as a card | 1 |
| pessimism about a run of questions | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [r1102b-B4](https://www.pangram.com/history/ecf802cd-e675-4bf6-9845-87870cddf8b4) | HG1102-40-S, 2 | Human | AI or mixed | the three echoes as three steps still read as a list, and the plainer climb read AI (Medium) beside them |
| [r1102b-D1](https://www.pangram.com/history/cebaccad-d951-4faf-8f36-282f80d44271) | HG1102-69-P10, 2 | Human | AI or mixed | the Meta Model's list of questions, unchanged, read AI (Low and Medium) in this stretch; in the section it read Human (Low and Medium) |
| [w1102-A](https://www.pangram.com/history/25bc4954-3ece-40f7-98c5-75fd5444f6e1) | HG1102-whole-A, 1 | Human | AI or mixed | ten short windows read AI in the whole half that read Human in their sections or pairs (E319): the guards questions, the sober induction's directions, two maxims |
| [w1102-B](https://www.pangram.com/history/aa3f74c7-cc59-40dd-b6e9-fcc0d3cc2b06) | HG1102-whole-B, 1 | Human | AI or mixed | two windows of his forgiveness text read AI in the whole half; by itself it read Human (High) for him |
| [w1102f-02](https://www.pangram.com/history/1c316dee-a9c1-42ba-95f4-c21a9cb17a1f) | HG1101-02, 2 | Human | AI or mixed | my rewrites F-11 and F-16 read AI (High) themselves: the minds said as a run of short declaratives, one per sentence ('Your inner child still wants... The guards are bracing... Meanwhile your body remembers... Intuition speaks up...'), and the asides folded into 'because ... I also borrow ... since ..., since ...'; the original read Human by itself |
| [w1102f-34](https://www.pangram.com/history/c044499e-e6f9-42ae-8b5a-f72a4685e909) | HG1101-34, 2 | Human | AI or mixed | cutting F-218 left the heading running straight into 'Indirect suggestions can bypass the subject's skeptical guard.', which read Human (Low); the section with the sentence read Human by itself |
| [w1102f-37](https://www.pangram.com/history/aa3c227e-ade5-4849-85ac-6582a9bc9615) | HG1101-37, 3 | Human | AI or mixed | my F-251 ('Just don't get poetic ... as plain as a fire exit sign.') read AI (Low): a joke-shaped closer is still a closer |
| [w1102f-38](https://www.pangram.com/history/49a602cf-c016-4f19-8772-1b61674314e4) | HG1101-38, 2 | Human | AI or mixed | my F-253 read AI (High and three Low): the anchor options split into short sentences ('Pick one thing to anchor yourself with. It could be ... The two-hand practice from above is another good one.') are the same instructions in a tidier row; F-255 and F-265 were not flagged |
| [w1102f-69](https://www.pangram.com/history/b16be294-97b8-4548-8682-271599de0ecf) | HG1101-69, 3 | Human | AI or mixed | my F-527 ('pin it back down ... which is how you keep the first one honest') read AI (Medium) and F-528's workshop leader example Human (Low): an explaining clause in place of the closer is still a closer, and the example sat in front of six questions |
| [w1102f-79](https://www.pangram.com/history/f44db6b6-054d-4f22-abf0-516e236708e6) | HG1101-79, 2 | Human | AI or mixed | his own inner child guide's line (C-626, 'No warmth today? Then rest your hands there and notice what you find, no faking required.') read AI (High) here, after 'Make sure you're actually talking to your inner child, not just repeating a script.' (AI Low); his line is not offered as a card |
| [f1102-527](https://www.pangram.com/history/2da7176a-9885-4040-828e-88015a3a0ed7) | HG-f1102-527, 1 | AI | Human | pessimism about a run of questions |
| [f1102b-119](https://www.pangram.com/history/9a2c0524-9c4f-437b-ab2a-a1cfed0e3b47) | HG-f1102-119, 2 | Human | AI or mixed | the fix made its stretch worse |
| [f1102b-762](https://www.pangram.com/history/26f67e2c-984e-4a54-a3ff-138d1ef4e6f7) | HG-f1102-762, 2 | Human | AI or mixed | the fix made its stretch worse |
| [HG-whole-1103](https://www.pangram.com/feed/4796254d-deaa-43f1-8bc9-25979960da03) | HG-whole, 18 | AI | Human | pessimism about cuts |
| [HG-rest-B-1103](https://www.pangram.com/feed/75baa67a-da78-4f74-b814-819444865b9c) | HG-rest-B, 16 | AI | Human | pessimism about cuts |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
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
| HG1101-02 | section | 2 of 2 | Mixed |
| HG1101-15 | section | 2 of 2 | Mixed |
| HG1101-17 | section | 2 of 2 | AI |
| HG1101-27 | section | 2 of 2 | Mixed |
| HG1101-34 | section | 2 of 2 | Mixed |
| HG1101-37 | section | 3 of 2 | Mixed |
| HG1101-38 | section | 2 of 2 | Mixed |
| HG1101-40 | section | 2 of 2 | Mixed |
| HG1101-44 | section | 2 of 2 | Mixed |
| HG1101-53 | section | 2 of 2 | AI |
| HG1101-59 | section | 2 of 2 | Mixed |
| HG1101-69 | section | 3 of 2 | Mixed |
| HG1101-79 | section | 2 of 2 | Mixed |
| HG1101-93 | section | 2 of 2 | Mixed |
| HG1101-17-P23 | pair | 1 of 6 | Mixed |
| HG1101-44-P5 | paragraph | 1 of 6 | AI |
| HG1101-44-P6 | paragraph | 1 of 6 | AI |
| HG1101-53-P1 | paragraph | 1 of 6 | AI |
| HG1101-53-P12 | pair | 1 of 6 | AI |
| HG1101-59-P1 | paragraph | 1 of 6 | AI |
| HG1102-40-S | pair | 2 of 6 | Mixed |
| HG1102-69-P10 | stretch | 2 of 2 | Mixed |
| HG1102-whole-A | stretch | 2 of 2 | Mixed |
| HG1102-whole-B | stretch | 2 of 2 | Mixed |
| HG-f1102-119 | stretch | 2 of 2 | Mixed |
| HG-f1102-762 | stretch | 2 of 2 | Mixed |

