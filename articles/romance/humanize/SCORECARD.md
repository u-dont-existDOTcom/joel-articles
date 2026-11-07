# Pangram prediction scorecard: romance article

Built by `tools/humanization/pangram_ledger.py build` from `articles/romance/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram 4.1, the web app (Joel's account, GUI credits) | 14 | 7 (50%) | 50% | 50% | 100% | 0.228 (base 0.250, 14) |

## pangram 4.1, the web app (Joel's account, GUI credits)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 14 | 7 (50%) | 50% | 50% | 100% | 0.228 (base 0.250, 14) |
| the latest 100 | 14 | 7 (50%) | 50% | 50% | 100% | 0.228 (base 0.250, 14) |
| all | 14 | 7 (50%) | 50% | 50% | 100% | 0.228 (base 0.250, 14) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pair | 12 | 5 (42%) | 58% | 42% | 100% | 0.245 (base 0.243, 12) |
| paragraph | 2 | 2 (100%) | 0% | 100% | 100% | 0.125 (base 0.000, 2) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 13 | 0.55 | 46% |
| 0.6 to 0.8 | 4 | 0.62 | 100% |

## Misses since the ledger (7)

| cause | misses |
|---|---|
| mirrored pair and a list kept | 1 |
| the check had no human context and the perks rewrite kept a list | 1 |
| a polished argument in my second paragraph | 1 |
| a generic reason clause kept | 1 |
| a dashed three-part aside kept | 1 |
| a contrast frame swapped for another | 1 |
| a three-item list in an if-clause | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [r01-s2](https://www.pangram.com/history/c2ef4f06-da74-439e-b714-d971e5a776f6) | romance-s2, 1 | Human | AI or mixed | mirrored pair and a list kept |
| [r02-s2](https://www.pangram.com/history/375a2b8a-ce7e-4cd3-b8af-0b18633fec65) | romance-s2, 2 | Human | AI or mixed | the check had no human context and the perks rewrite kept a list |
| [r02-s6](https://www.pangram.com/history/02957992-e302-47f5-b83b-62f94a8b85de) | romance-s6, 1 | Human | AI or mixed | a polished argument in my second paragraph |
| [r02-s7](https://www.pangram.com/history/b214bd97-7c58-43f3-a521-4182f7b09433) | romance-s7, 1 | Human | AI or mixed | a generic reason clause kept |
| [r02-s8](https://www.pangram.com/history/c764c228-211b-4a27-bacd-f4165453876d) | romance-s8, 1 | Human | AI or mixed | a dashed three-part aside kept |
| [r02-s10](https://www.pangram.com/history/a6a557ab-5ea6-42b9-b3c1-6fe8d337f4db) | romance-s10, 1 | Human | AI or mixed | a contrast frame swapped for another |
| [r02-s11](https://www.pangram.com/history/84f5d138-9e2b-413c-8f68-00c170c3e702) | romance-s11, 1 | Human | AI or mixed | a three-item list in an if-clause |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| romance-s2 | pair | 2 of 6 | AI |
| romance-s6 | pair | 1 of 6 | Mixed |
| romance-s7 | pair | 1 of 6 | Mixed |
| romance-s8 | pair | 1 of 6 | Mixed |
| romance-s10 | pair | 1 of 6 | Mixed |
| romance-s11 | pair | 1 of 6 | Mixed |

