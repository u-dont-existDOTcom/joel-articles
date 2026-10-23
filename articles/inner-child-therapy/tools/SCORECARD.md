# Pangram prediction scorecard: inner child guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/inner-child-therapy/tools/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.0 (before the ledger) | 3085 | 1395 (45%) | 57% | 43% | 96% | - |
| Pangram 4.1 GUI (dashboard) | 28 | 27 (96%) | 4% | 96% | 100% | 0.104 (base 0.034, 28) |
| pangram-4.1-substack | 66 | 41 (62%) | 53% | 47% | 48% | 0.203 (base 0.249, 66) |
| pangram-4.1-api | 101 | 76 (75%) | 40% | 60% | 75% | 0.203 (base 0.239, 101) |

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
| the latest 50 | 50 | 36 (72%) | 36% | 64% | 92% | 0.216 (base 0.230, 50) |
| the latest 100 | 100 | 75 (75%) | 39% | 61% | 76% | 0.203 (base 0.238, 100) |
| all | 101 | 76 (75%) | 40% | 60% | 75% | 0.203 (base 0.239, 101) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 50 | 37 (74%) | 40% | 60% | 78% | 0.202 (base 0.240, 50) |
| section | 33 | 24 (73%) | 42% | 58% | 73% | 0.212 (base 0.244, 33) |
| stretch | 18 | 15 (83%) | 33% | 67% | 72% | 0.189 (base 0.222, 18) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 9 | 0.31 | 11% |
| 0.4 to 0.6 | 79 | 0.54 | 62% |
| 0.6 to 0.8 | 45 | 0.62 | 82% |

## Misses since the ledger (51)

| cause | misses |
|---|---|
| too pessimistic about a cut | 12 |
| a tell I did not name | 9 |
| a Low window came back | 7 |
| not explained yet | 3 |
| an added move read AI | 3 |
| a window moved onto his line | 2 |
| a second cut of the same kind | 2 |
| the section read differently from the paragraph alone | 2 |
| too pessimistic about a rewrite | 2 |
| a repeat made adjacent by a move | 2 |
| his paragraph reads AI alone under 4.1 | 2 |
| a tell I left in | 1 |
| his questions are the tell | 1 |
| the list was not the only tell | 1 |
| the half varies | 1 |
| Low windows with no AI window | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [t102c_untangle_u02](https://www.pangram.com/history/b85736b8-dc31-4927-b434-626210690b5f) | untangle-slow, 3 | Human | AI or mixed | an added move read AI |
| [t103_97_8](https://www.pangram.com/history/4b249916-5525-49aa-bbbb-072a3ff3ee8a) | cut-97.8, 1 | Human | AI or mixed | a tell I did not name |
| [t103_97_12](https://www.pangram.com/history/ae33a2e2-0c16-4c90-9317-7134c113e110) | cut-97.12, 1 | Human | AI or mixed | a tell I did not name |
| [t103_98_2](https://www.pangram.com/history/3f3313f9-dc3e-413d-968b-e2bea8ac5d4a) | cut-98.2, 1 | Human | AI or mixed | his paragraph reads AI alone under 4.1 |
| [t103_98_7](https://www.pangram.com/history/92c0822d-5e94-4ed7-b44a-b3c1c9e785d5) | cut-98.7, 1 | Human | AI or mixed | a tell I did not name |
| [t103b_98_2_old](https://www.pangram.com/history/8e13e541-1157-4912-b56d-e68dfbf338d6) | cut-98.2, 2 | Human | AI or mixed | his paragraph reads AI alone under 4.1 |
| [t103b_monologue_h2](https://www.pangram.com/history/a63d4654-6fa7-4c36-9a11-f2f308f6ac59) | sec-monologue-h2, 1 | Human | AI or mixed | a Low window came back |
| [t103b_kill_stretch](https://www.pangram.com/history/fd1dd840-4dd2-4a96-860a-fad85f0e9a86) | sec-kill-stretch, 1 | Human | AI or mixed | a Low window came back |
| [t103b_firstsocial_h2](https://www.pangram.com/history/590addf4-f9aa-4eaf-a209-b6ec0f4df87e) | sec-firstsocial-h2, 1 | Human | AI or mixed | a Low window came back |
| [t103b_speak_h2](https://www.pangram.com/history/eb92af2e-b417-48b4-a978-be19e4f68b67) | sec-speak-h2, 1 | Human | AI or mixed | a Low window came back |
| [t103c_97_8_s01](https://www.pangram.com/history/32cfcfdc-cd7a-4edd-86aa-c2b3a6653022) | cut-97.8, 3 | Human | AI or mixed | a tell I did not name |
| [t103c_98_7_s02](https://www.pangram.com/history/80ce41ab-d0f2-46b1-8155-577397f1d8b9) | cut-98.7, 3 | Human | AI or mixed | a tell I did not name |
| [t103c_firstsocial_old](https://www.pangram.com/history/2bda009a-216a-4750-aadc-e7ce1ea0dd47) | sec-firstsocial-h2, 2 | Human | AI or mixed | a Low window came back |
| [t103d_ig_belonging_s05](https://www.pangram.com/history/aee791f1-113e-48e7-9517-58eceb02067a) | sec-ig-belonging, 1 | Human | AI or mixed | a repeat made adjacent by a move |
| [t103f_ig_belonging_s06](https://www.pangram.com/history/585143e9-1f50-470c-8256-9ea294f9b6b3) | sec-ig-belonging, 2 | Human | AI or mixed | a tell I did not name |

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
| cut-97.8 | paragraph | 3 of 6 | AI |
| cut-97.12 | paragraph | 3 of 6 | Mixed |
| cut-98.2 | paragraph | 2 of 6 | Mixed |
| cut-98.7 | paragraph | 3 of 6 | AI |
| sec-monologue-h2 | section | 2 of 2 | Mixed |
| sec-firstsocial-h2 | section | 2 of 2 | Mixed |
| sec-ig-belonging | section | 2 of 2 | Mixed |

