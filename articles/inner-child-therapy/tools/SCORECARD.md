# Pangram prediction scorecard: inner child guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-child-therapy/tools/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 3085 | 1395 (45%) | 57% | 43% | 96% | - |
| Pangram 4.1 GUI (dashboard) | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| pangram-4.1-substack | 66 | 41 (62%) | 53% | 47% | 48% | 0.203 (base 0.249, 66) |
| pangram-4.1-api | 19 | 16 (84%) | 79% | 21% | 16% | 0.169 (base 0.166, 19) |

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
| the latest 50 | 50 | 32 (64%) | 48% | 52% | 56% | 0.208 (base 0.250, 50) |
| the latest 100 | 66 | 41 (62%) | 53% | 47% | 48% | 0.203 (base 0.249, 66) |
| all | 66 | 41 (62%) | 53% | 47% | 48% | 0.203 (base 0.249, 66) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 12 | 10 (83%) | 100% | 0% | 17% | 0.079 (base 0.000, 12) |
| paragraph | 47 | 25 (53%) | 47% | 53% | 49% | 0.246 (base 0.249, 47) |
| section | 7 | 6 (86%) | 14% | 86% | 100% | 0.128 (base 0.122, 7) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 8 | 0.13 | 0% |
| 0.2 to 0.4 | 5 | 0.26 | 0% |
| 0.4 to 0.6 | 44 | 0.50 | 55% |
| 0.6 to 0.8 | 14 | 0.67 | 57% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## pangram-4.1-api

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 19 | 16 (84%) | 79% | 21% | 16% | 0.169 (base 0.166, 19) |
| the latest 100 | 19 | 16 (84%) | 79% | 21% | 16% | 0.169 (base 0.166, 19) |
| all | 19 | 16 (84%) | 79% | 21% | 16% | 0.169 (base 0.166, 19) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 7 | 6 (86%) | 86% | 14% | 29% | 0.187 (base 0.122, 7) |
| section | 9 | 7 (78%) | 67% | 33% | 11% | 0.161 (base 0.222, 9) |
| stretch | 3 | 3 (100%) | 100% | 0% | 0% | 0.148 (base 0.000, 3) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 9 | 0.31 | 11% |
| 0.4 to 0.6 | 10 | 0.45 | 30% |
| 0.6 to 0.8 | 1 | 0.60 | 100% |

## Misses since the ledger (29)

| cause | misses |
|---|---|
| too pessimistic about a cut | 12 |
| not explained yet | 3 |
| a tell I did not name | 2 |
| a window moved onto his line | 2 |
| a second cut of the same kind | 2 |
| a Low window came back | 2 |
| a tell I left in | 1 |
| an added move read AI | 1 |
| his questions are the tell | 1 |
| the list was not the only tell | 1 |
| the half varies | 1 |
| the section read differently from the paragraph alone | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [t93i_b08](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b08, 1 | Human | AI or mixed | a window moved onto his line |
| [t93i_b09](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b09, 1 | AI | Human | too pessimistic about a cut |
| [t95i_c01](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-c01, 1 | Human | AI or mixed | a second cut of the same kind |
| [t95i_c02](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-c02, 1 | Human | AI or mixed | a second cut of the same kind |
| [t95i_c03](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-c03, 1 | Human | AI or mixed | a tell I left in |
| [t95i_c04](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-c04, 1 | Human | AI or mixed | an added move read AI |
| [t95i_j843](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-j843, 1 | Human | AI or mixed | his questions are the tell |
| [t95i_j847](https://www.pangram.com/feed/f0a788bc-07a4-411d-bd1b-292c7370c630) | t95-item-j847, 1 | Human | AI or mixed | the list was not the only tell |
| [t97b_related_try](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t97-api/API-CHECKS.md#t97b_related_try) | related-section, 2 | AI | Human | too pessimistic about a cut |
| [t98i_related](https://www.pangram.com/feed/ecd65665-3f16-4254-bea2-ce60cf047546) | t98-related-mine, 1 | Human | AI or mixed | a window moved onto his line |
| [t98i_guide5](https://www.pangram.com/feed/ecd65665-3f16-4254-bea2-ce60cf047546) | t98-item-guide5, 1 | Human | AI or mixed | a Low window came back |
| [t98i_ended1](https://www.pangram.com/feed/ecd65665-3f16-4254-bea2-ce60cf047546) | t98-item-ended1, 1 | Human | AI or mixed | a Low window came back |
| [t98i_borrowed1](https://www.pangram.com/feed/ecd65665-3f16-4254-bea2-ce60cf047546) | t98-item-borrowed1, 1 | AI | Human | the half varies |
| [t99_bb_new1](https://www.pangram.com/history/80b68055-4d4e-4330-a8fd-fde76c3884eb) | bb-new1, 1 | Human | AI or mixed | a tell I did not name |
| [t99_ended_stretch](https://www.pangram.com/history/b9697aa6-8501-4b18-ac2b-2d699d38210e) | ended-section, 1 | AI | Human | the section read differently from the paragraph alone |

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
| bb-new1 | paragraph | 1 of 6 | Mixed |
| bb-stretch | stretch | 1 of 2 | Mixed |
| guide-P5 | paragraph | 1 of 6 | Mixed |
| guide-stretch | stretch | 1 of 2 | Mixed |
| ended-P1 | paragraph | 1 of 6 | Mixed |
| ifs-P7 | paragraph | 1 of 6 | Mixed |
| ifs-stretch | stretch | 1 of 2 | Mixed |

