# Pangram prediction scorecard: inner child guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-child-therapy/tools/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 3085 | 1395 (45%) | 57% | 43% | 96% | - |
| Pangram 4.1 GUI (dashboard) | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| pangram-4.1-substack | 52 | 31 (60%) | 58% | 42% | 40% | 0.209 (base 0.244, 52) |
| pangram-4.1-api | 10 | 9 (90%) | 80% | 20% | 10% | 0.127 (base 0.160, 10) |

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
| the latest 50 | 50 | 31 (62%) | 56% | 44% | 38% | 0.203 (base 0.246, 50) |
| the latest 100 | 52 | 31 (60%) | 58% | 42% | 40% | 0.209 (base 0.244, 52) |
| all | 52 | 31 (60%) | 58% | 42% | 40% | 0.209 (base 0.244, 52) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 10 | 8 (80%) | 100% | 0% | 20% | 0.088 (base 0.000, 10) |
| paragraph | 41 | 22 (54%) | 49% | 51% | 44% | 0.243 (base 0.250, 41) |
| section | 1 | 1 (100%) | 0% | 100% | 100% | 0.040 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 7 | 0.13 | 0% |
| 0.2 to 0.4 | 4 | 0.28 | 0% |
| 0.4 to 0.6 | 38 | 0.49 | 53% |
| 0.6 to 0.8 | 7 | 0.63 | 29% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## pangram-4.1-api

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 10 | 9 (90%) | 80% | 20% | 10% | 0.127 (base 0.160, 10) |
| the latest 100 | 10 | 9 (90%) | 80% | 20% | 10% | 0.127 (base 0.160, 10) |
| all | 10 | 9 (90%) | 80% | 20% | 10% | 0.127 (base 0.160, 10) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 2 | 2 (100%) | 100% | 0% | 0% | 0.122 (base 0.000, 2) |
| section | 8 | 7 (88%) | 75% | 25% | 12% | 0.128 (base 0.188, 8) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 7 | 0.30 | 0% |
| 0.4 to 0.6 | 3 | 0.48 | 67% |
| 0.6 to 0.8 | 1 | 0.60 | 100% |

## Misses since the ledger (23)

| cause | misses |
|---|---|
| too pessimistic about a cut | 12 |
| not explained yet | 3 |
| a second cut of the same kind | 2 |
| a tell I did not name | 1 |
| a window moved onto his line | 1 |
| a tell I left in | 1 |
| an added move read AI | 1 |
| his questions are the tell | 1 |
| the list was not the only tell | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [t93i_a09](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a09, 1 | AI | Human | too pessimistic about a cut |
| [t93i_a10](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a10, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b01b](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b01b, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b02](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b02, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b04](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b04, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b05](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b05, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b08](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b08, 1 | Human | AI or mixed | a window moved onto his line |
| [t93i_b09](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b09, 1 | AI | Human | too pessimistic about a cut |
| [t95i_c01](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-c01, 1 | Human | AI or mixed | a second cut of the same kind |
| [t95i_c02](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-c02, 1 | Human | AI or mixed | a second cut of the same kind |
| [t95i_c03](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-c03, 1 | Human | AI or mixed | a tell I left in |
| [t95i_c04](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-c04, 1 | Human | AI or mixed | an added move read AI |
| [t95i_j843](https://www.pangram.com/feed/aa99b16e-9e04-4e14-aa6d-86b041ed4c9e) | t95-item-j843, 1 | Human | AI or mixed | his questions are the tell |
| [t95i_j847](https://www.pangram.com/feed/f0a788bc-07a4-411d-bd1b-292c7370c630) | t95-item-j847, 1 | Human | AI or mixed | the list was not the only tell |
| [t97b_related_try](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t97-api/API-CHECKS.md#t97b_related_try) | related-section, 2 | AI | Human | too pessimistic about a cut |

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

