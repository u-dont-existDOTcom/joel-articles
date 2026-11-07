# Pangram prediction scorecard: healing the gut article

Built by `tools/humanization/pangram_ledger.py build` from `articles/healing-the-gut/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram API 4.1 | 97 | 71 (73%) | 55% | 45% | 47% | 0.173 (base 0.248, 97) |
| Pangram 4.1 (web app) | 10 | 5 (50%) | 70% | 30% | 80% | 0.224 (base 0.210, 10) |
| pangram 4.1, Pangram's check of the Substack draft (free, Joel's account) | 1 | 1 (100%) | 0% | 100% | 100% | 0.202 (base 0.000, 1) |
| pangram 4.1, the web app (Joel's account, GUI credits) | 80 | 62 (78%) | 25% | 75% | 90% | 0.168 (base 0.188, 80) |
| pangram 4.1, his Pangram extension on the live post (free, Joel's account) | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |
| pangram 4.1, his Pangram extension on a temporary Substack draft's secret link (free, Joel's account) | 3 | 2 (67%) | 33% | 67% | 100% | 0.209 (base 0.222, 3) |

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
| the latest 50 | 50 | 38 (76%) | 28% | 72% | 88% | 0.173 (base 0.202, 50) |
| the latest 100 | 80 | 62 (78%) | 25% | 75% | 90% | 0.168 (base 0.188, 80) |
| all | 80 | 62 (78%) | 25% | 75% | 90% | 0.168 (base 0.188, 80) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 30 | 26 (87%) | 13% | 87% | 93% | 0.138 (base 0.116, 30) |
| pair | 9 | 7 (78%) | 22% | 78% | 100% | 0.174 (base 0.173, 9) |
| stretch | 31 | 24 (77%) | 29% | 71% | 81% | 0.175 (base 0.206, 31) |
| paragraph | 10 | 5 (50%) | 50% | 50% | 100% | 0.233 (base 0.250, 10) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 5 | 0.31 | 40% |
| 0.4 to 0.6 | 34 | 0.55 | 56% |
| 0.6 to 0.8 | 52 | 0.67 | 85% |
| 0.8 to 1.0 | 6 | 0.80 | 100% |

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

## pangram 4.1, his Pangram extension on a temporary Substack draft's secret link (free, Joel's account)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 3 | 2 (67%) | 33% | 67% | 100% | 0.209 (base 0.222, 3) |
| the latest 100 | 3 | 2 (67%) | 33% | 67% | 100% | 0.209 (base 0.222, 3) |
| all | 3 | 2 (67%) | 33% | 67% | 100% | 0.209 (base 0.222, 3) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 3 | 2 (67%) | 33% | 67% | 100% | 0.209 (base 0.222, 3) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 2 | 0.55 | 50% |
| 0.6 to 0.8 | 1 | 0.65 | 100% |

## Misses since the ledger (51)

| cause | misses |
|---|---|
| context | 7 |
| model-over-pessimism | 6 |
| not explained yet | 4 |
| explainer structure | 3 |
| one-sentence-stuck | 2 |
| one step a sentence not applied | 2 |
| every sentence a so-chain | 2 |
| tells | 2 |
| my rewrite of words that already read High | 2 |
| parallel cases in one mould | 2 |
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
| my new claims in an explainer's frame | 1 |
| context: red in the whole guide, Human in the pair | 1 |
| term explained after its first use, and a note splitting a sentence before its point (gates E368, E369) | 1 |
| the point after the names, and a note splitting his sentence (gate E368) | 1 |
| the cut, and my fixes made it worse | 1 |
| the first case is the AI core | 1 |
| a step that can't stand alone | 1 |
| the post-panel wording, not the joining | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [r13-p21p22-r12](https://www.pangram.com/history/8563cfe5-5f52-43ad-903c-f5e1fdae01ca) | r13-fuels-p22, 1 | Human | AI or mixed | tells |
| [r13-p21p22-v3](https://www.pangram.com/history/84f98fca-d6d3-42b8-b14e-9b8e888e5601) | r13-fuels-p22, 2 | Human | AI or mixed | tells |
| [r15-C](https://www.pangram.com/history/02aaf3fa-f757-426f-a6c9-0ee74b8ad0fb) | r15-C, 1 | Human | AI or mixed | term explained after its first use, and a note splitting a sentence before its point (gates E368, E369) |
| [r15-H](https://www.pangram.com/history/de89477f-ceb5-4762-b6d7-87601979e4d7) | r15-H, 1 | Human | AI or mixed | the point after the names, and a note splitting his sentence (gate E368) |
| [r18-P](https://www.pangram.com/history/dcfc1cd4-912e-4a21-865a-2e297f278f35) | r18-P, 1 | Human | AI or mixed | my rewrite of words that already read High |
| [r18-S](https://www.pangram.com/history/579da364-48c8-490e-bd68-3cf167311fdd) | r18-S, 1 | Human | AI or mixed | my rewrite of words that already read High |
| [r19-P45](https://www.pangram.com/history/00f07f88-96d7-48c8-accf-24249c02731c) | r19-P45, 1 | Human | AI or mixed | the cut, and my fixes made it worse |
| [gut-r20-article](https://www.pangram.com/feed/154d7a1d-7062-492b-96c1-ed381d39eb0b) | gut-article-r20, 1 | Human | AI or mixed | every sentence a so-chain |
| [r23-P45](https://www.pangram.com/history/8dc695e5-8976-40c8-a4f4-f88bd96ef5e9) | r23-P45, 1 | AI | Human | model-over-pessimism |
| [r21-P45](https://www.pangram.com/history/fa4cd031-8b4f-41e0-b580-40ecdf57fbe0) | r21-P45, 1 | AI | Human | model-over-pessimism |
| [r24-org](https://www.pangram.com/history/535e5ae8-b748-4dcb-bb49-f341b131a689) | r24-org, 1 | Human | AI or mixed | parallel cases in one mould |
| [r25-org](https://www.pangram.com/history/d584fee7-bc2f-41db-9939-73e001fe2d4e) | r24-org, 2 | Human | AI or mixed | the first case is the AI core |
| [r27-org](https://www.pangram.com/history/09108ab5-f50f-42a9-bdd3-976572ef7857) | r24-org, 3 | Human | AI or mixed | a step that can't stand alone |
| [r28-p4](https://www.pangram.com/history/d18c0cd1-200b-476b-93ee-d5f54f6c20d6) | r24-org, 4 | Human | AI or mixed | the post-panel wording, not the joining |
| [r29-p4](https://www.pangram.com/history/13582f54-d1e2-4362-adac-f99aa4d96ca9) | r24-org, 5 | Human | AI or mixed | parallel cases in one mould |

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
| r19-P45 | stretch | 1 of 2 | Mixed |
| r17-P45 | stretch | 1 of 2 | Mixed |
| r17-P36 | stretch | 1 of 2 | Mixed |
| r20-P36 | stretch | 1 of 2 | Mixed |
| gut-article-r20 | article | 1 of unlimited (Substack) | Mixed |
| gut-article-r21 | article | 1 of unlimited (Substack) | pending |
| r23-P36 | stretch | 1 of 2 | Mixed |

