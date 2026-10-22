# Pangram prediction scorecard: inner child guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-child-therapy/tools/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 3085 | 1395 (45%) | 57% | 43% | 96% | - |
| Pangram 4.1 GUI (dashboard) | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| pangram-4.1-substack | 38 | 23 (61%) | 55% | 45% | 26% | 0.208 (base 0.247, 38) |

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
| the latest 50 | 38 | 23 (61%) | 55% | 45% | 26% | 0.208 (base 0.247, 38) |
| the latest 100 | 38 | 23 (61%) | 55% | 45% | 26% | 0.208 (base 0.247, 38) |
| all | 38 | 23 (61%) | 55% | 45% | 26% | 0.208 (base 0.247, 38) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 8 | 6 (75%) | 100% | 0% | 25% | 0.106 (base 0.000, 8) |
| paragraph | 30 | 17 (57%) | 43% | 57% | 27% | 0.235 (base 0.246, 30) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 5 | 0.13 | 0% |
| 0.2 to 0.4 | 4 | 0.28 | 0% |
| 0.4 to 0.6 | 29 | 0.48 | 59% |
| 0.6 to 0.8 | 3 | 0.60 | 33% |

## Misses since the ledger (16)

| cause | misses |
|---|---|
| too pessimistic about a cut | 11 |
| not explained yet | 3 |
| a tell I did not name | 1 |
| a window moved onto his line | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [t79s_A](https://www.pangram.com/feed/8a00b6b8-ef47-4f75-b473-10e56ff8f5b3) | t79-substack-A, 1 | Human | AI or mixed | **not explained yet** |
| [t79s_B](https://www.pangram.com/feed/d8a345d5-7038-4344-a461-e33fae115884) | t79-substack-B, 1 | Human | AI or mixed | **not explained yet** |
| [t93i_a01](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a01, 1 | AI | Human | too pessimistic about a cut |
| [t93i_a02](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a02, 1 | AI | Human | too pessimistic about a cut |
| [t93i_a03](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a03, 1 | AI | Human | too pessimistic about a cut |
| [t93i_a05](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a05, 1 | Human | AI or mixed | a tell I did not name |
| [t93i_a08](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a08, 1 | AI | Human | too pessimistic about a cut |
| [t93i_a09](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a09, 1 | AI | Human | too pessimistic about a cut |
| [t93i_a10](https://www.pangram.com/feed/0f0ce34e-ecd5-480f-954b-c77cfa00f381) | t93-item-a10, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b01b](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b01b, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b02](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b02, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b04](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b04, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b05](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b05, 1 | AI | Human | too pessimistic about a cut |
| [t93i_b08](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b08, 1 | Human | AI or mixed | a window moved onto his line |
| [t93i_b09](https://www.pangram.com/feed/c81bb1ea-87e2-47ce-b67e-cdfffb4fe4a4) | t93-item-b09, 1 | AI | Human | too pessimistic about a cut |

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

