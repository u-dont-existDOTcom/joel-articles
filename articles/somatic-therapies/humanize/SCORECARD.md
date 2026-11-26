# Pangram prediction scorecard: somatic guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/somatic-therapies/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.1 (web app, his account, in the desktop app's browser pane) | 9 | 6 (67%) | 89% | 11% | 22% | 0.240 (base 0.099, 9) |

## Pangram 4.1 (web app, his account, in the desktop app's browser pane)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 9 | 6 (67%) | 89% | 11% | 22% | 0.240 (base 0.099, 9) |
| the latest 100 | 9 | 6 (67%) | 89% | 11% | 22% | 0.240 (base 0.099, 9) |
| all | 9 | 6 (67%) | 89% | 11% | 22% | 0.240 (base 0.099, 9) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 4 | 1 (25%) | 75% | 25% | 50% | 0.309 (base 0.188, 4) |
| paragraph | 5 | 5 (100%) | 100% | 0% | 0% | 0.186 (base 0.000, 5) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 8 | 0.44 | 12% |
| 0.6 to 0.8 | 1 | 0.65 | 0% |

## Misses since the ledger (3)

| cause | misses |
|---|---|
| shape | 2 |
| content | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [a1-sec-5](https://www.pangram.com/history/7f76bad0-ee08-4a1c-b586-8c119afa80ad) | somatic-therapies/ADD-A1, 1 | Human | AI or mixed | shape |
| [a3-sec-5](https://www.pangram.com/history/2ead9bf4-482d-487d-bb34-b40ceb60f1e3) | somatic-therapies/ADD-A3, 1 | AI | Human | content |
| [a3-sec-7](https://www.pangram.com/history/af6615cb-06d4-4f41-a73f-e4a9340d86fb) | somatic-therapies/ADD-A3, 2 | Human | AI or mixed | shape |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| somatic-therapies/ADD-A1 | section | 1 of 2 | AI |
| somatic-therapies/ADD-A2 | section | 1 of 2 | AI |
| somatic-therapies/ADD-A3 | section | 2 of 2 | Mixed |
| somatic-therapies/ADD-A1-P1 | paragraph | 1 of 6 | AI |
| somatic-therapies/ADD-A1-P2 | paragraph | 1 of 6 | AI |
| somatic-therapies/ADD-A1-P3 | paragraph | 1 of 6 | Mixed |
| somatic-therapies/ADD-A2-P1 | paragraph | 1 of 6 | Mixed |
| somatic-therapies/ADD-A2-P2 | paragraph | 1 of 6 | AI |

