# Pangram prediction scorecard: inner child guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-child-therapy/tools/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 3085 | 1395 (45%) | 57% | 43% | 96% | - |
| Pangram 4.1 GUI (dashboard) | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| pangram-4.1-substack | 66 | 41 (62%) | 53% | 47% | 48% | 0.203 (base 0.249, 66) |
| pangram-4.1-api | 48 | 37 (77%) | 46% | 54% | 56% | 0.193 (base 0.248, 48) |

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
| the latest 50 | 48 | 37 (77%) | 46% | 54% | 56% | 0.193 (base 0.248, 48) |
| the latest 100 | 48 | 37 (77%) | 46% | 54% | 56% | 0.193 (base 0.248, 48) |
| all | 48 | 37 (77%) | 46% | 54% | 56% | 0.193 (base 0.248, 48) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 23 | 17 (74%) | 43% | 57% | 65% | 0.204 (base 0.246, 23) |
| section | 14 | 11 (79%) | 50% | 50% | 43% | 0.180 (base 0.250, 14) |
| stretch | 11 | 9 (82%) | 45% | 55% | 55% | 0.184 (base 0.248, 11) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 9 | 0.31 | 11% |
| 0.4 to 0.6 | 35 | 0.52 | 60% |
| 0.6 to 0.8 | 15 | 0.61 | 93% |

## Misses since the ledger (37)

| cause | misses |
|---|---|
| too pessimistic about a cut | 12 |
| not explained yet | 3 |
| a tell I did not name | 3 |
| an added move read AI | 3 |
| a window moved onto his line | 2 |
| a second cut of the same kind | 2 |
| a Low window came back | 2 |
| the section read differently from the paragraph alone | 2 |
| too pessimistic about a rewrite | 2 |
| a tell I left in | 1 |
| his questions are the tell | 1 |
| the list was not the only tell | 1 |
| the half varies | 1 |
| Low windows with no AI window | 1 |
| a repeat made adjacent by a move | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [t97b_related_try](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t97-api/API-CHECKS.md#t97b_related_try) | related-section, 2 | AI | Human | too pessimistic about a cut |
| [t98i_related](https://www.pangram.com/feed/ecd65665-3f16-4254-bea2-ce60cf047546) | t98-related-mine, 1 | Human | AI or mixed | a window moved onto his line |
| [t98i_guide5](https://www.pangram.com/feed/ecd65665-3f16-4254-bea2-ce60cf047546) | t98-item-guide5, 1 | Human | AI or mixed | a Low window came back |
| [t98i_ended1](https://www.pangram.com/feed/ecd65665-3f16-4254-bea2-ce60cf047546) | t98-item-ended1, 1 | Human | AI or mixed | a Low window came back |
| [t98i_borrowed1](https://www.pangram.com/feed/ecd65665-3f16-4254-bea2-ce60cf047546) | t98-item-borrowed1, 1 | AI | Human | the half varies |
| [t99_bb_new1](https://www.pangram.com/history/80b68055-4d4e-4330-a8fd-fde76c3884eb) | bb-new1, 1 | Human | AI or mixed | a tell I did not name |
| [t99_ended_stretch](https://www.pangram.com/history/b9697aa6-8501-4b18-ac2b-2d699d38210e) | ended-section, 1 | AI | Human | the section read differently from the paragraph alone |
| [t100_guide5](https://www.pangram.com/history/5ee698a9-da9c-4ca9-80ee-9866cfab16ef) | guide-P5, 2 | AI | Human | too pessimistic about a rewrite |
| [t100_ended1](https://www.pangram.com/history/50f027e5-f84e-47d9-bbc0-43ee045bea9c) | ended-P1, 2 | AI | Human | too pessimistic about a rewrite |
| [t100_ifs_stretch](https://www.pangram.com/history/c4e53e05-a8e2-4090-861c-abbf245babc5) | ifs-stretch, 2 | AI | Human | the section read differently from the paragraph alone |
| [t101_borrow_main](https://www.pangram.com/history/80caed9d-cb5f-4978-8a36-75c5d12dcc7d) | borrow-main, 1 | Human | AI or mixed | Low windows with no AI window |
| [t101_borrow_h3](https://www.pangram.com/history/0646d274-08fa-4d24-ba75-c444710868ef) | borrow-h3, 1 | Human | AI or mixed | a repeat made adjacent by a move |
| [t102_borrow_p5](https://www.pangram.com/history/bf6562e2-577e-4fce-a12e-af98c12c7688) | borrow-p5, 2 | Human | AI or mixed | a tell I did not name |
| [t102_untangle_p](https://www.pangram.com/history/6aa17696-41e5-4a7c-88be-8bb14af1ee45) | untangle-slow, 1 | Human | AI or mixed | an added move read AI |
| [t102c_untangle_u02](https://www.pangram.com/history/b85736b8-dc31-4927-b434-626210690b5f) | untangle-slow, 3 | Human | AI or mixed | an added move read AI |

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

