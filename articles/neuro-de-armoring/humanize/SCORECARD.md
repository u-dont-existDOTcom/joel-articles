# Pangram prediction scorecard: neuro de-armoring article

Built by `tools/humanization/pangram_ledger.py build` from `articles/neuro-de-armoring/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram 4.1, the API (Joel's key, run on his laptop; E218) | 12 | 12 (100%) | 100% | 0% | 0% | 0.019 (base 0.000, 12) |
| pangram 4.1, the API (Joel's key, run on his laptop; E218, E325: at most six paragraphs and 1,200 words) | 39 | 39 (100%) | 100% | 0% | 0% | 0.079 (base 0.000, 39) |
| pangram 4.1, the API (Joel's key, run on his laptop; E218, E325: one paragraph per text, 2026-11-04) | 23 | 20 (87%) | 74% | 26% | 22% | 0.192 (base 0.193, 23) |
| pangram 4.1, the web app (Joel's account and its credits, run by the lane in his Brave through Claude in Chrome; one paragraph per check) | 23 | 19 (83%) | 87% | 13% | 4% | 0.134 (base 0.113, 23) |
| pangram 4.1, the web app (Joel's account and its credits, run by the lane in his Brave through Claude in Chrome; one paragraph per check, or a pair where a paragraph is under the 50-word minimum) | 2 | 2 (100%) | 0% | 100% | 100% | 0.092 (base 0.000, 2) |
| pangram 4.1, the web app: Joel's account, run by the lane in the desktop app's browser pane (E356) | 9 | 8 (89%) | 67% | 33% | 22% | 0.161 (base 0.222, 9) |
| web app, his account | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |
| web app, his account, run by the lane in the desktop app's browser pane (E356) | 38 | 34 (89%) | 87% | 13% | 8% | 0.183 (base 0.114, 38) |
| pangram-4.1-substack | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |
| Pangram 4.1 (web app) | 12 | 6 (50%) | 50% | 50% | 100% | 0.204 (base 0.250, 12) |

## pangram 4.1, the API (Joel's key, run on his laptop; E218)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 12 | 12 (100%) | 100% | 0% | 0% | 0.019 (base 0.000, 12) |
| the latest 100 | 12 | 12 (100%) | 100% | 0% | 0% | 0.019 (base 0.000, 12) |
| all | 12 | 12 (100%) | 100% | 0% | 0% | 0.019 (base 0.000, 12) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 11 | 11 (100%) | 100% | 0% | 0% | 0.021 (base 0.000, 11) |
| article | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 9 | 0.09 | 0% |
| 0.2 to 0.4 | 3 | 0.22 | 0% |

## pangram 4.1, the API (Joel's key, run on his laptop; E218, E325: at most six paragraphs and 1,200 words)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 39 | 39 (100%) | 100% | 0% | 0% | 0.079 (base 0.000, 39) |
| the latest 100 | 39 | 39 (100%) | 100% | 0% | 0% | 0.079 (base 0.000, 39) |
| all | 39 | 39 (100%) | 100% | 0% | 0% | 0.079 (base 0.000, 39) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 34 | 34 (100%) | 100% | 0% | 0% | 0.073 (base 0.000, 34) |
| paragraph | 5 | 5 (100%) | 100% | 0% | 0% | 0.117 (base 0.000, 5) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 3 | 0.15 | 0% |
| 0.2 to 0.4 | 34 | 0.27 | 0% |
| 0.4 to 0.6 | 2 | 0.43 | 0% |

## pangram 4.1, the API (Joel's key, run on his laptop; E218, E325: one paragraph per text, 2026-11-04)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 23 | 20 (87%) | 74% | 26% | 22% | 0.192 (base 0.193, 23) |
| the latest 100 | 23 | 20 (87%) | 74% | 26% | 22% | 0.192 (base 0.193, 23) |
| all | 23 | 20 (87%) | 74% | 26% | 22% | 0.192 (base 0.193, 23) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 23 | 20 (87%) | 74% | 26% | 22% | 0.192 (base 0.193, 23) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 9 | 0.32 | 22% |
| 0.4 to 0.6 | 14 | 0.48 | 29% |
| 0.6 to 0.8 | 3 | 0.60 | 67% |

## pangram 4.1, the web app (Joel's account and its credits, run by the lane in his Brave through Claude in Chrome; one paragraph per check)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 23 | 19 (83%) | 87% | 13% | 4% | 0.134 (base 0.113, 23) |
| the latest 100 | 23 | 19 (83%) | 87% | 13% | 4% | 0.134 (base 0.113, 23) |
| all | 23 | 19 (83%) | 87% | 13% | 4% | 0.134 (base 0.113, 23) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 23 | 19 (83%) | 87% | 13% | 4% | 0.134 (base 0.113, 23) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 19 | 0.29 | 5% |
| 0.4 to 0.6 | 4 | 0.49 | 50% |
| 0.6 to 0.8 | 1 | 0.60 | 0% |

## pangram 4.1, the web app (Joel's account and its credits, run by the lane in his Brave through Claude in Chrome; one paragraph per check, or a pair where a paragraph is under the 50-word minimum)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 2 | 2 (100%) | 0% | 100% | 100% | 0.092 (base 0.000, 2) |
| the latest 100 | 2 | 2 (100%) | 0% | 100% | 100% | 0.092 (base 0.000, 2) |
| all | 2 | 2 (100%) | 0% | 100% | 100% | 0.092 (base 0.000, 2) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 1 | 1 (100%) | 0% | 100% | 100% | 0.062 (base 0.000, 1) |
| pair | 1 | 1 (100%) | 0% | 100% | 100% | 0.122 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.6 to 0.8 | 2 | 0.70 | 100% |

## pangram 4.1, the web app: Joel's account, run by the lane in the desktop app's browser pane (E356)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 9 | 8 (89%) | 67% | 33% | 22% | 0.161 (base 0.222, 9) |
| the latest 100 | 9 | 8 (89%) | 67% | 33% | 22% | 0.161 (base 0.222, 9) |
| all | 9 | 8 (89%) | 67% | 33% | 22% | 0.161 (base 0.222, 9) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 9 | 8 (89%) | 67% | 33% | 22% | 0.161 (base 0.222, 9) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 3 | 0.35 | 33% |
| 0.4 to 0.6 | 4 | 0.41 | 0% |
| 0.6 to 0.8 | 1 | 0.75 | 100% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## web app, his account

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |
| the latest 100 | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |
| all | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 1 | 0.50 | 0% |

## web app, his account, run by the lane in the desktop app's browser pane (E356)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 38 | 34 (89%) | 87% | 13% | 8% | 0.183 (base 0.114, 38) |
| the latest 100 | 38 | 34 (89%) | 87% | 13% | 8% | 0.183 (base 0.114, 38) |
| all | 38 | 34 (89%) | 87% | 13% | 8% | 0.183 (base 0.114, 38) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 30 | 27 (90%) | 87% | 13% | 10% | 0.181 (base 0.116, 30) |
| pair | 7 | 7 (100%) | 100% | 0% | 0% | 0.161 (base 0.000, 7) |
| stretch | 1 | 0 (0%) | 0% | 100% | 0% | 0.423 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 3 | 0.35 | 33% |
| 0.4 to 0.6 | 33 | 0.42 | 6% |
| 0.8 to 1.0 | 2 | 0.80 | 100% |

## pangram-4.1-substack

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |
| the latest 100 | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |
| all | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| article | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 1 | 0.01 | 0% |

## Pangram 4.1 (web app)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 12 | 6 (50%) | 50% | 50% | 100% | 0.204 (base 0.250, 12) |
| the latest 100 | 12 | 6 (50%) | 50% | 50% | 100% | 0.204 (base 0.250, 12) |
| all | 12 | 6 (50%) | 50% | 50% | 100% | 0.204 (base 0.250, 12) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 10 | 6 (60%) | 40% | 60% | 100% | 0.190 (base 0.240, 10) |
| pair | 2 | 0 (0%) | 100% | 0% | 100% | 0.276 (base 0.000, 2) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 10 | 0.55 | 40% |
| 0.6 to 0.8 | 3 | 0.60 | 100% |
| 0.8 to 1.0 | 2 | 0.82 | 100% |

## Misses since the ledger (19)

| cause | misses |
|---|---|
| not explained yet | 16 |
| the panel's fixes worked better than I expected | 1 |
| my changes to try 5's Medium and Low sentences read AI | 1 |
| another family's writer changed the build | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [b088](https://www.pangram.com/history/4079bcd3-65eb-43f8-97bb-ec8436fc5f19) | ND1104-B088, 3 | Human | AI or mixed | **not explained yet** |
| [b088m](https://www.pangram.com/history/f645d894-6c91-41b3-841d-26ec0d79b093) | ND1104-B088m, 1 | AI | Human | **not explained yet** |
| [b093](https://www.pangram.com/history/2be95f74-b2cf-45ec-a669-1807880af623) | ND1104-B093, 4 | AI | Human | **not explained yet** |
| [b095](https://www.pangram.com/history/53b000ed-a200-44af-8eb7-051b992576a1) | ND1104-B095, 1 | AI | Human | **not explained yet** |
| [778a81972c80](https://www.pangram.com/history/6e5452c4-3a59-480a-ae28-b9370928c6f5) | neuro-de-armoring/section-c-dynorphin, 1 | Human | AI or mixed | **not explained yet** |
| [p1-P032](https://www.pangram.com/history/eeb2d730-ca9e-41ea-815e-6163350f8aee) | neuro-de-armoring/P032, 1 | AI | Human | **not explained yet** |
| [p1-STRETCH-030-033](https://www.pangram.com/history/b1594a9f-6c90-4dcd-b117-68c50f21df5e) | neuro-de-armoring/STRETCH-030-033, 1 | AI | Human | **not explained yet** |
| [r4-B042e](https://www.pangram.com/history/e06f6f0d-f215-4c45-8c5a-9b76a2f96120) | neuro-de-armoring/B042, 3 | AI | Human | **not explained yet** |
| [sci-B038s](https://www.pangram.com/history/4c0e1a5b-51fe-4d93-854e-451a187daff3) | neuro-de-armoring/B038, 4 | Human | AI or mixed | **not explained yet** |
| [B039h](https://www.pangram.com/history/60a9335d-05f1-4227-a6e4-9956415a2a71) | neuro-de-armoring/B039, 1 | Human | AI or mixed | **not explained yet** |
| [PAIR-040-041](https://www.pangram.com/history/4312584e-a4de-471b-aaba-5459ffaa4cd9) | neuro-de-armoring/PAIR-040-041, 1 | Human | AI or mixed | **not explained yet** |
| [B037h](https://www.pangram.com/history/4026db4c-d192-4673-8adc-c56d711b8087) | neuro-de-armoring/B037, 2 | Human | AI or mixed | **not explained yet** |
| [B038h2](https://www.pangram.com/history/fa44a654-ae02-432f-b2aa-6dd033ca41f6) | neuro-de-armoring/B038, 5 | Human | AI or mixed | **not explained yet** |
| [B039n](https://www.pangram.com/history/7768cb2f-aa9a-4ab2-b99e-7e14ac8379f9) | neuro-de-armoring/B039, 2 | Human | AI or mixed | **not explained yet** |
| [PAIR-040-041n](https://www.pangram.com/history/ca20c43c-e69b-4360-a7e9-fb4941bbb23f) | neuro-de-armoring/PAIR-040-041, 2 | Human | AI or mixed | **not explained yet** |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| ND1102-01 | section | 1 of 2 | Mixed |
| ND1102-02 | section | 1 of 2 | Mixed |
| ND1102-03 | section | 1 of 2 | Mixed |
| ND1102-04 | section | 2 of 2 | Mixed |
| ND1102-05 | section | 1 of 2 | AI |
| ND1102-06 | section | 1 of 2 | AI |
| ND1102-07 | section | 1 of 2 | Mixed |
| ND1102-08 | section | 1 of 2 | Mixed |
| ND1102-09 | section | 1 of 2 | Mixed |
| ND1102-10 | section | 1 of 2 | Mixed |
| ND1102-whole | article | 1 of 2 | Mixed |
| ND1103-S02a | stretch | 2 of 2 | Mixed |
| ND1103-S02b | stretch | 2 of 2 | AI |
| ND1103-S01a | stretch | 1 of 2 | Mixed |
| ND1103-S01b | stretch | 1 of 2 | AI |
| ND1103-S03c | stretch | 1 of 2 | AI |
| ND1103-S04a | stretch | 1 of 2 | Mixed |
| ND1103-S04b | stretch | 1 of 2 | Mixed |
| ND1103-S04c | stretch | 1 of 2 | AI |
| ND1103-S05a | stretch | 1 of 2 | AI |
| ND1103-S05b | stretch | 1 of 2 | AI |
| ND1103-S07a | stretch | 1 of 2 | AI |
| ND1103-S07b | stretch | 1 of 2 | AI |
| ND1103-S08a | stretch | 1 of 2 | AI |
| ND1103-S08b | stretch | 1 of 2 | AI |
| ND1103-S08c | stretch | 1 of 2 | AI |
| ND1103-S08d | stretch | 1 of 2 | Mixed |
| ND1103-S09a | stretch | 1 of 2 | AI |
| ND1103-S09b | stretch | 1 of 2 | Mixed |
| ND1103-S09c | stretch | 1 of 2 | Mixed |
| ND1103-S10a | stretch | 1 of 2 | AI |
| ND1103-S10b | stretch | 1 of 2 | Mixed |
| ND1103-S10c | stretch | 1 of 2 | AI |
| ND1103-S03a | stretch | 1 of 2 | AI |
| ND1103-S03b | stretch | 1 of 2 | Mixed |
| ND1103-S06a | stretch | 1 of 2 | AI |
| ND1103-S06b | stretch | 1 of 2 | AI |
| ND1103-X15 | paragraph | 1 of 6 | Mixed |
| ND1103-R2V1 | stretch | 2 of 2 | AI |
| ND1103-R2V2 | stretch | 2 of 2 | AI |
| ND1103-R2V3 | stretch | 2 of 2 | Mixed |
| ND1103-P016 | paragraph | 1 of 6 | AI |
| ND1103-P017 | paragraph | 2 of 6 | AI |
| ND1103-P085 | paragraph | 1 of 6 | AI |
| ND1104-B082 | paragraph | 6 of 6 | Mixed |
| ND1104-B083b | paragraph | 2 of 6 | AI |
| ND1104-B085 | paragraph | 3 of 6 | AI |
| ND1104-B086 | paragraph | 3 of 6 | Mixed |
| ND1104-B088 | paragraph | 3 of 6 | Mixed |
| ND1104-B089 | paragraph | 3 of 6 | AI |
| ND1104-B090 | paragraph | 2 of 6 | AI |
| ND1104-B091 | paragraph | 3 of 6 | AI |
| ND1104-whole | article | 1 of unlimited (Substack) | pending |
| ND1104-B092 | paragraph | 5 of 6 | AI |
| ND1105-B098-100 | paragraph | 3 of 6 | Mixed |
| ND1105-B095-096 | paragraph | 3 of 6 | AI |
| neuro-de-armoring/section-c-dynorphin | paragraph | 1 of 6 | AI |
| ND1106-whole | article | 1 of unlimited (Substack) | Mixed |
| neuro-de-armoring/P025 | paragraph | 4 of 6 | AI |
| neuro-de-armoring/P026 | paragraph | 5 of 6 | Mixed |
| neuro-de-armoring/P027 | paragraph | 1 of 6 | AI |
| neuro-de-armoring/PAIR-027-028 | pair | 5 of 6 | AI |
| neuro-de-armoring/P020 | paragraph | 3 of 6 | AI |
| neuro-de-armoring/PAIR-020-021 | pair | 2 of 6 | AI |
| neuro-de-armoring/B038 | paragraph | 5 of 6 | AI |
| neuro-de-armoring/B043 | paragraph | 3 of 6 | AI |
| neuro-de-armoring/B044 | paragraph | 3 of 6 | AI |
| neuro-de-armoring/B037 | paragraph | 2 of 6 | AI |
| neuro-de-armoring/B039 | paragraph | 2 of 6 | Mixed |
| neuro-de-armoring/PAIR-040-041 | pair | 2 of 6 | AI |

