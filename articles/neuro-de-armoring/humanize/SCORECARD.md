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
| Pangram 4.1 (web app) | 21 | 11 (52%) | 48% | 52% | 90% | 0.212 (base 0.249, 21) |
| Pangram 4.1 (web app, his account, in the desktop app's browser pane) | 113 | 85 (75%) | 33% | 67% | 81% | 0.189 (base 0.220, 113) |
| Pangram 4.1 (web app, his account, Claude in Chrome in his browser) | 29 | 22 (76%) | 52% | 48% | 45% | 0.179 (base 0.250, 29) |

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
| the latest 50 | 21 | 11 (52%) | 48% | 52% | 90% | 0.212 (base 0.249, 21) |
| the latest 100 | 21 | 11 (52%) | 48% | 52% | 90% | 0.212 (base 0.249, 21) |
| all | 21 | 11 (52%) | 48% | 52% | 90% | 0.212 (base 0.249, 21) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 19 | 11 (58%) | 42% | 58% | 89% | 0.205 (base 0.244, 19) |
| pair | 2 | 0 (0%) | 100% | 0% | 100% | 0.276 (base 0.000, 2) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 18 | 0.52 | 44% |
| 0.6 to 0.8 | 3 | 0.60 | 100% |
| 0.8 to 1.0 | 3 | 0.83 | 100% |

## Pangram 4.1 (web app, his account, in the desktop app's browser pane)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 38 (76%) | 28% | 72% | 84% | 0.210 (base 0.202, 50) |
| the latest 100 | 100 | 76 (76%) | 30% | 70% | 84% | 0.186 (base 0.210, 100) |
| all | 113 | 85 (75%) | 33% | 67% | 81% | 0.189 (base 0.220, 113) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 85 | 66 (78%) | 35% | 65% | 78% | 0.181 (base 0.228, 85) |
| pair | 20 | 14 (70%) | 20% | 80% | 90% | 0.205 (base 0.160, 20) |
| section | 6 | 5 (83%) | 17% | 83% | 100% | 0.224 (base 0.139, 6) |
| stretch | 2 | 0 (0%) | 100% | 0% | 100% | 0.305 (base 0.000, 2) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 9 | 0.31 | 22% |
| 0.4 to 0.6 | 69 | 0.53 | 61% |
| 0.6 to 0.8 | 50 | 0.65 | 82% |
| 0.8 to 1.0 | 6 | 0.81 | 100% |

## Pangram 4.1 (web app, his account, Claude in Chrome in his browser)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 29 | 22 (76%) | 52% | 48% | 45% | 0.179 (base 0.250, 29) |
| the latest 100 | 29 | 22 (76%) | 52% | 48% | 45% | 0.179 (base 0.250, 29) |
| all | 29 | 22 (76%) | 52% | 48% | 45% | 0.179 (base 0.250, 29) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 22 | 18 (82%) | 45% | 55% | 55% | 0.155 (base 0.248, 22) |
| pair | 7 | 4 (57%) | 71% | 29% | 14% | 0.256 (base 0.204, 7) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 11 | 0.27 | 18% |
| 0.4 to 0.6 | 13 | 0.49 | 54% |
| 0.6 to 0.8 | 6 | 0.65 | 100% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## Misses since the ledger (58)

| cause | misses |
|---|---|
| not explained yet | 21 |
| shape | 17 |
| register | 4 |
| context | 2 |
| the panel's fixes worked better than I expected | 1 |
| my changes to try 5's Medium and Low sentences read AI | 1 |
| another family's writer changed the build | 1 |
| ambiguity | 1 |
| my additions made his rough paragraph tidy | 1 |
| the stop sign echoed the first sentence; a declining opening | 1 |
| a crisp stop sign in place of his slack ending | 1 |
| the paragraph split into windows; four changes at once | 1 |
| two small changes weakened his first sentence | 1 |
| his line alone still weakened his opening | 1 |
| a tell I underweighted: a repeat | 1 |
| the fix outweighed the tells I named | 1 |
| the attached sentence changes the whole pair's reading | 1 |
| an added clause split the near miss's window | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [sw22-23](https://www.pangram.com/history/3ad85ece-63b0-4c1a-bad6-df492b74835b) | neuro-de-armoring/PAIR-SW22-23, 1 | Human | AI or mixed | shape |
| [sw19b](https://www.pangram.com/history/cd2c9d6b-ada6-44c9-b29c-67292c104927) | neuro-de-armoring/P-SW19, 2 | Human | AI or mixed | shape |
| [sw22-23b](https://www.pangram.com/history/d91d27ac-0519-4188-a9ab-5ff119d64467) | neuro-de-armoring/PAIR-SW22-23, 2 | Human | AI or mixed | shape |
| [lma-73a](https://www.pangram.com/history/666f323c-0200-4f4f-a54e-be84150a350b) | neuro-de-armoring/W-LMA-73a, 1 | Human | AI or mixed | my additions made his rough paragraph tidy |
| [lma-t2](https://www.pangram.com/history/f3417de9-5888-4720-adc1-66303c140dab) | neuro-de-armoring/W-LMA-73a, 2 | Human | AI or mixed | the stop sign echoed the first sentence; a declining opening |
| [lma-t3](https://www.pangram.com/history/a4917d66-e42f-4533-8713-e72d039f379c) | neuro-de-armoring/W-LMA-73a, 3 | Human | AI or mixed | a crisp stop sign in place of his slack ending |
| [lma-t4](https://www.pangram.com/history/35b9a7c1-f6cb-4de9-8424-82b918c1b4c9) | neuro-de-armoring/W-LMA-73a, 4 | Human | AI or mixed | the paragraph split into windows; four changes at once |
| [lma-s1](https://www.pangram.com/history/d2357d72-aa6f-4a8c-9ff1-ab3e53ac084b) | neuro-de-armoring/W-LMA-his, 2 | Human | AI or mixed | two small changes weakened his first sentence |
| [lma-s2](https://www.pangram.com/history/e48fb85c-ea18-48c5-b61a-7066b4069dec) | neuro-de-armoring/W-LMA-his, 3 | Human | AI or mixed | his line alone still weakened his opening |
| [bl-lma](https://www.pangram.com/history/b88b1fce-db98-4e8b-9615-062fb097c8ac) | neuro-de-armoring/W-LMA-73A-blind (replay x1127a), 1 | Human | AI or mixed | a tell I underweighted: a repeat |
| [bl-cog](https://www.pangram.com/history/44991128-07f5-4096-9c95-c5f6a4ca5d85) | neuro-de-armoring/PAIR-COG-blind (replay x1127a), 1 | AI | Human | the fix outweighed the tells I named |
| [pair2223-s1](https://www.pangram.com/history/17aa8876-097f-43dd-a2f2-654c38d0bb89) | neuro-de-armoring/PAIR-SW22-23, 4 | Human | AI or mixed | the attached sentence changes the whole pair's reading |
| [pair2223-s2](https://www.pangram.com/history/beae5fbb-2ab5-4cda-a264-cf5017db761c) | neuro-de-armoring/PAIR-SW22-23, 5 | Human | AI or mixed | an added clause split the near miss's window |
| [sw19-s5](https://www.pangram.com/history/84d12e88-4359-49bd-a3e8-ed6306e429f3) | neuro-de-armoring/P-SW19, 6 | AI | Human | **not explained yet** |
| [sw21-s3](https://www.pangram.com/history/8a7cf54b-2112-41e5-94ab-b14087a373f1) | neuro-de-armoring/P-SW21, 4 | AI | Human | **not explained yet** |

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
| neuro-de-armoring/B048-his | paragraph | 1 of 6 | Mixed |
| neuro-de-armoring/B054-sc54 | paragraph | 3 of 6 | Mixed |
| neuro-de-armoring/W-LMA | paragraph | 5 of 6 | AI |
| neuro-de-armoring/W-AGM | paragraph | 3 of 6 | AI |
| neuro-de-armoring/W-LMA-blind (replay x1124b) | paragraph | 1 of 6 | AI |
| neuro-de-armoring/W-AGM-blind (replay x1124b) | paragraph | 1 of 6 | Mixed |
| neuro-de-armoring/W-ISO | paragraph | 3 of 6 | AI |
| neuro-de-armoring/PAIR-ISO-RULE | pair | 2 of 6 | AI |
| neuro-de-armoring/PAIR-COG-PROJ | pair | 4 of 6 | Mixed |
| neuro-de-armoring/W-AGMINTRO | paragraph | 3 of 6 | AI |
| neuro-de-armoring/W-HTPTOP | paragraph | 3 of 6 | AI |
| neuro-de-armoring/W-ISO-blind (x1126a) | paragraph | 1 of 6 | AI |
| neuro-de-armoring/W-AGMINTRO-blind (x1126a) | paragraph | 1 of 6 | AI |
| neuro-de-armoring/W-HTPTOP-blind (x1126a) | paragraph | 1 of 6 | Mixed |
| neuro-de-armoring/STRETCH-RULE-AGM | stretch | 2 of 2 | Mixed |
| neuro-de-armoring/W-LMA-73a | paragraph | 4 of 6 | Mixed |
| neuro-de-armoring/W-LMA-73A-blind (replay x1127a) | paragraph | 1 of 6 | Mixed |

