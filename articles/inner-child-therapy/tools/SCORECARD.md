# Pangram prediction scorecard: inner child guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-child-therapy/tools/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 3085 | 1395 (45%) | 57% | 43% | 96% | - |
| Pangram 4.1 GUI (dashboard) | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| pangram-4.1-substack | 85 | 59 (69%) | 45% | 55% | 58% | 0.187 (base 0.247, 85) |
| pangram-4.1-api | 158 | 120 (76%) | 36% | 64% | 80% | 0.199 (base 0.231, 158) |

106 of the older calls are scored here differently from the lane's own marks (98 marked right there, 8 marked wrong): this page uses one rule for every lane, where only a 100% Human result is a pass and a "Mixed" or "Human with an AI window" call counts as not Human.

## Pangram 4.0 (before the ledger)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 43 (86%) | 14% | 86% | 100% | - |
| the latest 100 | 100 | 63 (63%) | 37% | 63% | 100% | - |
| all | 3085 | 1395 (45%) | 57% | 43% | 96% | - |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 2241 | 961 (43%) | 59% | 41% | 96% | - |
| section | 538 | 294 (55%) | 47% | 53% | 95% | - |
| unrecorded | 306 | 140 (46%) | 56% | 44% | 97% | - |

## Pangram 4.1 GUI (dashboard)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| the latest 100 | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| all | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.6 to 0.8 | 28 | 0.70 | 96% |

## pangram-4.1-substack

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 37 (74%) | 38% | 62% | 80% | 0.174 (base 0.236, 50) |
| the latest 100 | 85 | 59 (69%) | 45% | 55% | 58% | 0.187 (base 0.247, 85) |
| all | 85 | 59 (69%) | 45% | 55% | 58% | 0.187 (base 0.247, 85) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 14 | 12 (86%) | 100% | 0% | 14% | 0.076 (base 0.000, 14) |
| paragraph | 51 | 29 (57%) | 43% | 57% | 53% | 0.242 (base 0.245, 51) |
| section | 20 | 18 (90%) | 10% | 90% | 100% | 0.122 (base 0.090, 20) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 8 | 0.13 | 0% |
| 0.2 to 0.4 | 7 | 0.26 | 0% |
| 0.4 to 0.6 | 52 | 0.51 | 60% |
| 0.6 to 0.8 | 28 | 0.67 | 75% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## pangram-4.1-api

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 41 (82%) | 26% | 74% | 92% | 0.184 (base 0.192, 50) |
| the latest 100 | 100 | 75 (75%) | 33% | 67% | 90% | 0.204 (base 0.221, 100) |
| all | 158 | 120 (76%) | 36% | 64% | 80% | 0.199 (base 0.231, 158) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 75 | 57 (76%) | 37% | 63% | 79% | 0.192 (base 0.234, 75) |
| section | 63 | 46 (73%) | 35% | 65% | 86% | 0.212 (base 0.227, 63) |
| stretch | 20 | 17 (85%) | 35% | 65% | 70% | 0.182 (base 0.227, 20) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 12 | 0.32 | 8% |
| 0.4 to 0.6 | 113 | 0.55 | 64% |
| 0.6 to 0.8 | 88 | 0.63 | 80% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## Misses since the ledger (65)

| cause | misses |
|---|---|
| too pessimistic about a cut | 12 |
| a tell I did not name | 11 |
| not explained yet | 10 |
| a Low window came back | 8 |
| an added move read AI | 3 |
| the section read differently from the paragraph alone | 3 |
| too pessimistic about a rewrite | 3 |
| a window moved onto his line | 2 |
| a second cut of the same kind | 2 |
| a repeat made adjacent by a move | 2 |
| his paragraph reads AI alone under 4.1 | 2 |
| a tell I left in | 1 |
| his questions are the tell | 1 |
| the list was not the only tell | 1 |
| the half varies | 1 |
| Low windows with no AI window | 1 |
| a Human result above 0.0000 | 1 |
| a cut took out what read human | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [t103f_ig_belonging_s06](https://www.pangram.com/history/585143e9-1f50-470c-8256-9ea294f9b6b3) | sec-ig-belonging, 2 | Human | AI or mixed | a tell I did not name |
| [t104_ig_belonging_his](https://www.pangram.com/history/1c31ecda-53ab-4a7d-b95c-5eab66ff5565) | sec-ig-belonging-joel, 1 | Human | AI or mixed | a Human result above 0.0000 |
| [t104_97_8_d4](https://www.pangram.com/history/3abf93cf-b9fb-4d01-844f-ccabb1cd786e) | cut-97.8, 4 | Human | AI or mixed | a tell I did not name |
| [t104_98_7_d5](https://www.pangram.com/history/64778cfd-d4f4-482f-94ee-0735b6110c68) | cut-98.7, 4 | AI | Human | too pessimistic about a rewrite |
| [t104_change_h3_d5](https://www.pangram.com/history/1e3f795f-5715-4bfb-a98d-9bd0396aa0ae) | sec-change-strategy-d5, 1 | Human | AI or mixed | the section read differently from the paragraph alone |
| [t104_change_h3_cut](https://www.pangram.com/history/523ede49-eea8-48e9-a9bb-69f5ff7785e8) | sec-change-strategy-cut, 1 | Human | AI or mixed | a Low window came back |
| [t105_98_7_d8](https://www.pangram.com/history/33d1a7d3-ca17-4331-b566-85743cc55238) | cut-98.7, 6 | Human | AI or mixed | a cut took out what read human |
| [t106_h3_journey](https://www.pangram.com/history/23800590-b449-4804-9dac-4b17d8926d18) | t106-h3-journey, 1 | Human | AI or mixed | **not explained yet** |
| [t106_sec_journey](https://www.pangram.com/history/b6e45715-fbfe-4847-9993-7253918dc5d9) | t106-sec-journey, 1 | Human | AI or mixed | **not explained yet** |
| [t106_sec_hero](https://www.pangram.com/history/5105656f-4f96-45af-b7b5-5bab9fd6d771) | t106-sec-hero, 1 | Human | AI or mixed | **not explained yet** |
| [t106_sec_belong](https://www.pangram.com/history/4ee5effc-70d2-473c-9d01-3b00d7b42840) | t106-sec-belong, 1 | Human | AI or mixed | **not explained yet** |
| [t106_sec_timing](https://www.pangram.com/history/7c606adb-0eb5-4440-9de2-82634becc011) | t106-sec-timing, 1 | Human | AI or mixed | **not explained yet** |
| [t106_timing_before](https://www.pangram.com/history/c9ded038-bbf2-4b44-b8aa-5b49a31442f4) | t106-sec-timing, 2 | Human | AI or mixed | **not explained yet** |
| [t106_timing_d1](https://www.pangram.com/history/9ef9596e-81db-4646-a1a3-4b306e19c468) | t106-timing-p2, 1 | Human | AI or mixed | a tell I did not name |
| [t107i_ifs](https://www.pangram.com/feed/64c71597-3987-48a7-8431-c8bdc70fddcc) | t107i-ifs, 1 | Human | AI or mixed | **not explained yet** |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| inner-child/t77a_j05 | paragraph | 1 of 6 | AI |
| t78-substack-part1 | stretch | 1 of unlimited (Substack) | pending |
| t78-substack-part2 | stretch | 1 of unlimited (Substack) | pending |
| t78-substack-part3 | stretch | 1 of unlimited (Substack) | pending |
| t78-substack-part4 | stretch | 1 of unlimited (Substack) | pending |
| t78-substack-part3-v2 | stretch | 1 of unlimited (Substack) | pending |
| t78-substack-part4-v2 | stretch | 1 of unlimited (Substack) | pending |
| t79-substack-A | stretch | 1 of unlimited (Substack) | Mixed |
| t79-substack-B | stretch | 1 of unlimited (Substack) | Mixed |
| t88-substack-A | stretch | 1 of unlimited (Substack) | Mixed |
| t88-substack-B | stretch | 1 of unlimited (Substack) | Mixed |
| t90-substack-A | stretch | 1 of unlimited (Substack) | Mixed |
| t90-substack-B | stretch | 1 of unlimited (Substack) | Mixed |
| t93-substack-A | stretch | 1 of unlimited (Substack) | Mixed |
| t93-substack-B | stretch | 1 of unlimited (Substack) | Mixed |
| t93-item-a04 | paragraph | 1 of 6 | Mixed |
| t93-item-a05 | paragraph | 1 of 6 | AI |
| t93-item-a06 | paragraph | 1 of 6 | Mixed |
| t93-item-a12 | paragraph | 1 of 6 | Mixed |
| t93-item-a13 | paragraph | 1 of 6 | Mixed |
| t93-item-a14 | paragraph | 1 of 6 | Mixed |
| t93-item-a15 | paragraph | 1 of 6 | AI |
| t93-item-a16 | paragraph | 1 of 6 | AI |
| t93-item-a17 | paragraph | 1 of 6 | Mixed |
| t93-item-a18 | paragraph | 1 of 6 | AI |
| t93-item-a19 | paragraph | 1 of 6 | AI |
| t93-item-b08 | paragraph | 1 of 6 | Mixed |
| t93-item-b10 | paragraph | 1 of 6 | Mixed |
| t95-item-c01 | paragraph | 1 of 6 | Mixed |
| t95-item-c02 | paragraph | 1 of 6 | AI |
| t95-item-c03 | paragraph | 1 of 6 | AI |
| t95-item-c04 | paragraph | 1 of 6 | Mixed |
| t95-item-j843 | paragraph | 1 of 6 | Mixed |
| t95-item-j847 | paragraph | 1 of 6 | Mixed |
| t95-item-j848 | paragraph | 1 of 6 | AI |
| t95-substack-A | stretch | 1 of unlimited (Substack) | Mixed |
| t95-substack-B | stretch | 1 of unlimited (Substack) | Mixed |
| parent-P4 | paragraph | 1 of 6 | AI |
| happy-h1 | section | 2 of 2 | Mixed |
| shallow-section | section | 2 of 2 | Mixed |
| parent-section | section | 1 of 2 | Mixed |
| happy-P4 | paragraph | 1 of 6 | AI |
| t98-related-mine | section | 1 of 2 | Mixed |
| t98-item-guide5 | paragraph | 1 of 6 | Mixed |
| t98-item-ended1 | paragraph | 1 of 6 | Mixed |
| t98-substack-A | stretch | 1 of unlimited (Substack) | Mixed |
| t98-substack-B | stretch | 1 of unlimited (Substack) | Mixed |
| guide-stretch | stretch | 2 of 2 | Mixed |
| borrow-p5 | paragraph | 2 of 6 | AI |
| borrow-main | stretch | 1 of 2 | Mixed |
| untangle-slow | paragraph | 3 of 6 | AI |
| cut-97.8 | paragraph | 4 of 6 | AI |
| cut-97.12 | paragraph | 3 of 6 | Mixed |
| cut-98.7 | paragraph | 6 of 6 | AI |
| sec-monologue-h2 | section | 2 of 2 | Mixed |
| sec-firstsocial-h2 | section | 2 of 2 | Mixed |
| sec-ig-belonging | section | 2 of 2 | Mixed |
| sec-ig-belonging-joel | section | 1 of 2 | Mixed |
| sec-change-strategy-d5 | section | 1 of 2 | Mixed |
| sec-change-strategy-cut | section | 1 of 2 | Mixed |
| stretch-change-strategy-987 | stretch | 1 of 2 | Mixed |
| t106-h3-journey | paragraph | 2 of 6 | Mixed |
| t106-sec-hero | section | 1 of 2 | Mixed |
| t106-sec-belong | section | 1 of 2 | Mixed |
| t106-sec-timing | section | 2 of 2 | Mixed |
| t107i-ifs | section | 1 of 2 | Mixed |
| t107s-A | stretch | 1 of unlimited (Substack) | Mixed |
| t107s-B | stretch | 1 of unlimited (Substack) | Mixed |

