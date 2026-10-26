# Pangram prediction scorecard: inner child guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-child-therapy/tools/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 3085 | 1395 (45%) | 57% | 43% | 96% | - |
| Pangram 4.1 GUI (dashboard) | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| pangram-4.1-substack | 98 | 71 (72%) | 42% | 58% | 61% | 0.184 (base 0.243, 98) |
| pangram-4.1-api | 213 | 167 (78%) | 31% | 69% | 85% | 0.192 (base 0.214, 213) |

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
| the latest 50 | 50 | 44 (88%) | 28% | 72% | 80% | 0.147 (base 0.202, 50) |
| the latest 100 | 98 | 71 (72%) | 42% | 58% | 61% | 0.184 (base 0.243, 98) |
| all | 98 | 71 (72%) | 42% | 58% | 61% | 0.184 (base 0.243, 98) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| stretch | 16 | 14 (88%) | 100% | 0% | 12% | 0.080 (base 0.000, 16) |
| paragraph | 51 | 29 (57%) | 43% | 57% | 53% | 0.242 (base 0.245, 51) |
| section | 31 | 28 (90%) | 10% | 90% | 100% | 0.140 (base 0.087, 31) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 8 | 0.13 | 0% |
| 0.2 to 0.4 | 9 | 0.27 | 0% |
| 0.4 to 0.6 | 61 | 0.52 | 64% |
| 0.6 to 0.8 | 36 | 0.66 | 81% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## pangram-4.1-api

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 42 (84%) | 18% | 82% | 98% | 0.170 (base 0.148, 50) |
| the latest 100 | 100 | 85 (85%) | 18% | 82% | 97% | 0.175 (base 0.148, 100) |
| all | 213 | 167 (78%) | 31% | 69% | 85% | 0.192 (base 0.214, 213) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 113 | 88 (78%) | 32% | 68% | 85% | 0.186 (base 0.217, 113) |
| section | 80 | 62 (78%) | 29% | 71% | 89% | 0.202 (base 0.205, 80) |
| stretch | 20 | 17 (85%) | 35% | 65% | 70% | 0.182 (base 0.227, 20) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 13 | 0.32 | 8% |
| 0.4 to 0.6 | 139 | 0.55 | 67% |
| 0.6 to 0.8 | 127 | 0.64 | 83% |
| 0.8 to 1.0 | 4 | 0.80 | 75% |

## Misses since the ledger (74)

| cause | misses |
|---|---|
| not explained yet | 19 |
| too pessimistic about a cut | 12 |
| a tell I did not name | 11 |
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
| [t106_sec_hero](https://www.pangram.com/history/5105656f-4f96-45af-b7b5-5bab9fd6d771) | t106-sec-hero, 1 | Human | AI or mixed | **not explained yet** |
| [t106_sec_belong](https://www.pangram.com/history/4ee5effc-70d2-473c-9d01-3b00d7b42840) | t106-sec-belong, 1 | Human | AI or mixed | **not explained yet** |
| [t106_sec_timing](https://www.pangram.com/history/7c606adb-0eb5-4440-9de2-82634becc011) | t106-sec-timing, 1 | Human | AI or mixed | **not explained yet** |
| [t106_timing_before](https://www.pangram.com/history/c9ded038-bbf2-4b44-b8aa-5b49a31442f4) | t106-sec-timing, 2 | Human | AI or mixed | **not explained yet** |
| [t106_timing_d1](https://www.pangram.com/history/9ef9596e-81db-4646-a1a3-4b306e19c468) | t106-timing-p2, 1 | Human | AI or mixed | a tell I did not name |
| [t107i_ifs](https://www.pangram.com/feed/64c71597-3987-48a7-8431-c8bdc70fddcc) | t107i-ifs, 1 | Human | AI or mixed | **not explained yet** |
| [t109_guard_p3](https://www.pangram.com/history/4f6e4d83-13ca-47ed-9c2f-d92f72298047) | t109-guard-performance, 1 | Human | AI or mixed | **not explained yet** |
| [t109_start_p1](https://www.pangram.com/history/26d621a4-d7c4-49b8-9c82-f15bfe56535c) | t109-start-plain, 1 | Human | AI or mixed | **not explained yet** |
| [t109_guard_p1b](https://www.pangram.com/history/2b5501c8-bc19-42b2-8817-680658cf6311) | t109-guard-plain, 2 | Human | AI or mixed | **not explained yet** |
| [t109_guard_p3c](https://www.pangram.com/history/dbe0cc6a-0985-4089-964b-f4bbc40d406e) | t109-guard-performance, 3 | Human | AI or mixed | **not explained yet** |
| [t109_guard_p1d](https://www.pangram.com/history/bc6afa93-645e-40e9-b608-3bb4aa1bcfd3) | t109-guard-plain, 4 | Human | AI or mixed | **not explained yet** |
| [t111_c4_borrowlove](https://www.pangram.com/history/c18bb0c3-9232-470f-ab12-cf0850dbb3df) | t111-borrowlove, 1 | Human | AI or mixed | **not explained yet** |
| [t111_c8_belonging](https://www.pangram.com/history/1be9c136-ff8f-4a2e-8ee6-d009ca5d0dfa) | t111-belonging, 1 | Human | AI or mixed | **not explained yet** |
| [t114i_solomon](https://www.pangram.com/feed/909d378e-11d2-4722-b988-a508256c78b4) | t114i-solomon, 1 | Human | AI or mixed | **not explained yet** |
| [t115_lovewait_r2](https://www.pangram.com/history/b695880a-a675-4047-8b89-5f0b92d39fee) | ic-t115-lovewait, 2 | Human | AI or mixed | **not explained yet** |

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
| t109-guard-plain | paragraph | 4 of 6 | Mixed |
| t109-start-plain | paragraph | 1 of 6 | Mixed |
| t111-belonging | paragraph | 2 of 6 | AI |
| t112i-dontgive | section | 1 of 2 | pending |
| t112i-illwill | section | 1 of 2 | pending |
| t112i-lovenotyet | section | 1 of 2 | pending |
| t112i-borrowlove | section | 1 of 2 | pending |
| t112i-lovewait | section | 1 of 2 | pending |
| t112i-remind | section | 1 of 2 | pending |
| t112i-hook | section | 1 of 2 | pending |
| t112i-justlikeme | section | 1 of 2 | pending |
| t112i-photos | section | 1 of 2 | pending |
| t112i-close | section | 1 of 2 | pending |
| t112i-whatever | section | 1 of 2 | pending |
| t112i-guard | section | 1 of 2 | pending |
| t112i-belonging | section | 1 of 2 | pending |
| t112i-bad | section | 1 of 2 | pending |
| t112i-borrowed | section | 1 of 2 | pending |
| t112i-hardest | section | 1 of 2 | pending |
| t112i-forgive | section | 1 of 2 | pending |
| t112i-missing | section | 1 of 2 | pending |
| t112i-ifs | section | 1 of 2 | pending |
| t112s-A | stretch | 1 of unlimited (Substack) | pending |
| t112s-B | stretch | 1 of unlimited (Substack) | pending |
| t114i-solomon | section | 1 of 2 | Mixed |
| t114s-A | stretch | 1 of unlimited (Substack) | Mixed |
| t114s-B | stretch | 1 of unlimited (Substack) | Mixed |
| ic-t115-lovewait | section | 2 of 2 | Mixed |
| ic-t115-lovecoming | section | 1 of 2 | pending |

