# Pangram prediction scorecard: healing the gut article

Built by `tools/humanization/pangram_ledger.py build` from `articles/healing-the-gut/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram API 4.1 | 97 | 71 (73%) | 55% | 45% | 47% | 0.173 (base 0.248, 97) |
| Pangram 4.1 (web app) | 10 | 5 (50%) | 70% | 30% | 80% | 0.224 (base 0.210, 10) |
| pangram 4.1, Pangram's check of the Substack draft (free, Joel's account) | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |
| pangram 4.1, the web app (Joel's account, GUI credits) | 60 | 50 (83%) | 17% | 83% | 97% | 0.155 (base 0.139, 60) |
| pangram 4.1, his Pangram extension on the live post (free, Joel's account) | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

## pangram API 4.1

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 34 (68%) | 64% | 36% | 52% | 0.181 (base 0.230, 50) |
| the latest 100 | 97 | 71 (73%) | 55% | 45% | 47% | 0.173 (base 0.248, 97) |
| all | 97 | 71 (73%) | 55% | 45% | 47% | 0.173 (base 0.248, 97) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 88 | 63 (72%) | 56% | 44% | 45% | 0.180 (base 0.247, 88) |
| section | 9 | 8 (89%) | 44% | 56% | 67% | 0.106 (base 0.247, 9) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 10 | 0.10 | 10% |
| 0.2 to 0.4 | 16 | 0.31 | 25% |
| 0.4 to 0.6 | 51 | 0.48 | 37% |
| 0.6 to 0.8 | 22 | 0.67 | 95% |
| 0.8 to 1.0 | 6 | 0.85 | 100% |

## Pangram 4.1 (web app)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 10 | 5 (50%) | 70% | 30% | 80% | 0.224 (base 0.210, 10) |
| the latest 100 | 10 | 5 (50%) | 70% | 30% | 80% | 0.224 (base 0.210, 10) |
| all | 10 | 5 (50%) | 70% | 30% | 80% | 0.224 (base 0.210, 10) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 4 | 3 (75%) | 25% | 75% | 100% | 0.203 (base 0.188, 4) |
| pair | 3 | 1 (33%) | 100% | 0% | 67% | 0.220 (base 0.000, 3) |
| section | 3 | 1 (33%) | 100% | 0% | 67% | 0.257 (base 0.000, 3) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 9 | 0.52 | 22% |
| 0.6 to 0.8 | 4 | 0.62 | 50% |

## pangram 4.1, Pangram's check of the Substack draft (free, Joel's account)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |
| the latest 100 | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |
| all | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 1 | 0.55 | 100% |

## pangram 4.1, the web app (Joel's account, GUI credits)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 41 (82%) | 18% | 82% | 96% | 0.162 (base 0.148, 50) |
| the latest 100 | 60 | 50 (83%) | 17% | 83% | 97% | 0.155 (base 0.139, 60) |
| all | 60 | 50 (83%) | 17% | 83% | 97% | 0.155 (base 0.139, 60) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 25 | 21 (84%) | 16% | 84% | 92% | 0.147 (base 0.134, 25) |
| pair | 9 | 7 (78%) | 22% | 78% | 100% | 0.174 (base 0.173, 9) |
| stretch | 22 | 18 (82%) | 18% | 82% | 100% | 0.161 (base 0.149, 22) |
| paragraph | 4 | 4 (100%) | 0% | 100% | 100% | 0.126 (base 0.000, 4) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 2 | 0.28 | 50% |
| 0.4 to 0.6 | 23 | 0.57 | 70% |
| 0.6 to 0.8 | 44 | 0.67 | 91% |
| 0.8 to 1.0 | 4 | 0.80 | 100% |

## pangram 4.1, his Pangram extension on the live post (free, Joel's account)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |
| the latest 100 | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |
| all | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 1 | 0.50 | 0% |

## Misses since the ledger (42)

| cause | misses |
|---|---|
| context | 7 |
| not explained yet | 4 |
| model-over-pessimism | 4 |
| explainer structure | 3 |
| one-sentence-stuck | 2 |
| one step a sentence not applied | 2 |
| tells | 2 |
| my rewrite of words that already read High | 2 |
| summary-voice-around-owner-lines | 1 |
| owner-voice-carries-neighbours | 1 |
| opener-and-attribution-asides | 1 |
| owner-lines-human-gemini-lines-ai | 1 |
| owner-line-human-kit-run-ai | 1 |
| plain-conditional-warning-human | 1 |
| panel-overflags | 1 |
| panel-overflags-labels-were-the-tell | 1 |
| reader-question-did-not-carry | 1 |
| balanced closer kept | 1 |
| links stated as a glossary | 1 |
| every sentence a so-chain | 1 |
| my new claims in an explainer's frame | 1 |
| context: red in the whole guide, Human in the pair | 1 |
| term explained after its first use, and a note splitting a sentence before its point (gates E368, E369) | 1 |
| the point after the names, and a note splitting his sentence (gate E368) | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [r08-kits-with-categories](https://www.pangram.com/history/38b2da46-e72e-429a-8568-076737a8976f) | b2-ST2-p3, 5 | Human | AI or mixed | explainer structure |
| [r08-p81](https://www.pangram.com/history/4a617063-c5be-4d4a-8cb2-afc19152d7a2) | b2-ST2-p5, 2 | Human | AI or mixed | explainer structure |
| [r09-stacks-section](https://www.pangram.com/history/3217da78-355a-4536-a491-004ef95ca3cd) | r07-stacks-section, 2 | Human | AI or mixed | context |
| [r09b-stacks-section-moved](https://www.pangram.com/history/05f663cd-bc40-4317-b7fb-1e280ed4a6bd) | r07-stacks-section, 3 | Human | AI or mixed | context |
| [r12-g07](https://www.pangram.com/history/d11abfe4-40c5-485d-8f91-c715510881b3) | r12-g07, 1 | Human | AI or mixed | context |
| [r12-g13](https://www.pangram.com/history/80b7a95e-3c65-4943-8824-31d1ee228a7b) | r12-g13, 1 | Human | AI or mixed | context |
| [r11c-g07](https://www.pangram.com/history/43f270c9-e592-47d9-b8dd-4eb4265589d9) | r11c-g07, 1 | AI | Human | context |
| [r12-fuels](https://www.pangram.com/history/2103ebd9-b274-4d8c-b32a-53819d5c740d) | r12-fuels, 1 | Human | AI or mixed | context |
| [gut-r12-live-article](https://www.pangram.com/feed/e3a65841-a626-4b34-aad7-62b9dfa48ada) | gut-article-whole, 2 | Human | AI or mixed | context |
| [r13-p21p22-r12](https://www.pangram.com/history/8563cfe5-5f52-43ad-903c-f5e1fdae01ca) | r13-fuels-p22, 1 | Human | AI or mixed | tells |
| [r13-p21p22-v3](https://www.pangram.com/history/84f98fca-d6d3-42b8-b14e-9b8e888e5601) | r13-fuels-p22, 2 | Human | AI or mixed | tells |
| [r15-C](https://www.pangram.com/history/02aaf3fa-f757-426f-a6c9-0ee74b8ad0fb) | r15-C, 1 | Human | AI or mixed | term explained after its first use, and a note splitting a sentence before its point (gates E368, E369) |
| [r15-H](https://www.pangram.com/history/de89477f-ceb5-4762-b6d7-87601979e4d7) | r15-H, 1 | Human | AI or mixed | the point after the names, and a note splitting his sentence (gate E368) |
| [r18-P](https://www.pangram.com/history/dcfc1cd4-912e-4a21-865a-2e297f278f35) | r18-P, 1 | Human | AI or mixed | my rewrite of words that already read High |
| [r18-S](https://www.pangram.com/history/579da364-48c8-490e-bd68-3cf167311fdd) | r18-S, 1 | Human | AI or mixed | my rewrite of words that already read High |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| GH-12 | paragraph | 1 of 6 | Mixed |
| GH-18-20 | paragraph | 1 of 6 | AI |
| GH-21-23 | paragraph | 1 of 6 | AI |
| GH-27-28 | paragraph | 1 of 6 | AI |
| GH-29-31 | paragraph | 1 of 6 | AI |
| GH-32-34 | paragraph | 1 of 6 | AI |
| GH-35 | paragraph | 1 of 6 | AI |
| GH-36-39 | paragraph | 1 of 6 | AI |
| GH-40 | paragraph | 1 of 6 | AI |
| GH-41 | paragraph | 1 of 6 | AI |
| GH-42 | paragraph | 1 of 6 | AI |
| GH-24-26 | paragraph | 1 of 6 | Mixed |
| b1-P1 | paragraph | 3 of 6 | AI |
| b2-LGF | paragraph | 5 of 6 | AI |
| b2-ST1 | paragraph | 2 of 6 | AI |
| b2-ST2 | paragraph | 2 of 6 | Mixed |
| b2-ST | section | 1 of 2 | AI |
| b2-ST2-p3 | pair | 5 of 6 | Mixed |
| b2-ST2-p5 | pair | 3 of 6 | AI |
| r03-fuel-butyrate | paragraph | 3 of 6 | AI |
| r03-fuel-glutamine | paragraph | 3 of 6 | Mixed |
| r03-fuel-tca | paragraph | 6 of 6 | AI |
| r05-fuel-acids | section | 3 of 2 | Mixed |
| r07-stacks-section | section | 4 of 2 | Mixed |
| gut-article-whole | article | 3 of unlimited (Substack) | pending |
| r12-g07 | section | 1 of 2 | Mixed |
| r12-g13 | section | 1 of 2 | Mixed |
| r11c-g13 | section | 1 of 2 | Mixed |
| r18-P | stretch | 1 of 2 | Mixed |
| r18-S | stretch | 1 of 2 | AI |
| r17-phase1 | section | 1 of 2 | pending |
| r17-stacks | section | 1 of 2 | pending |
| gut-article-r17 | article | 1 of unlimited (Substack) | pending |

