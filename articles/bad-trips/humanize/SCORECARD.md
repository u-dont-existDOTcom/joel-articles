# Pangram prediction scorecard: bad trips guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/bad-trips/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.1 extension (free, live post; Joel's check of 2026-10-18, the same text as his 2026-11-03 paste by SHA-256) | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |
| Pangram web app (his account, Pangram Professional) | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |
| Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane | 22 | 19 (86%) | 55% | 45% | 59% | 0.162 (base 0.248, 22) |

## Pangram 4.1 extension (free, live post; Joel's check of 2026-10-18, the same text as his 2026-11-03 paste by SHA-256)

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
| 0.0 to 0.2 | 1 | 0.02 | 0% |

## Pangram web app (his account, Pangram Professional)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |
| the latest 100 | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |
| all | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 1 | 1 (100%) | 100% | 0% | 0% | 0.062 (base 0.000, 1) |
| paragraph | 2 | 2 (100%) | 100% | 0% | 0% | 0.106 (base 0.000, 2) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 3 | 0.30 | 0% |

## Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 22 | 19 (86%) | 55% | 45% | 59% | 0.162 (base 0.248, 22) |
| the latest 100 | 22 | 19 (86%) | 55% | 45% | 59% | 0.162 (base 0.248, 22) |
| all | 22 | 19 (86%) | 55% | 45% | 59% | 0.162 (base 0.248, 22) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 1 | 1 (100%) | 0% | 100% | 100% | 0.040 (base 0.000, 1) |
| paragraph | 17 | 16 (94%) | 47% | 53% | 59% | 0.151 (base 0.249, 17) |
| pair | 4 | 2 (50%) | 100% | 0% | 50% | 0.239 (base 0.000, 4) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 2 | 0.35 | 0% |
| 0.4 to 0.6 | 13 | 0.48 | 23% |
| 0.6 to 0.8 | 7 | 0.68 | 100% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## Misses since the ledger (3)

| cause | misses |
|---|---|
| shape echo | 1 |
| parallel frames kept | 1 |
| not explained yet | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [bt-pfa-P3P4-D3](https://www.pangram.com/history/0993c7c4-386c-4a5b-821b-f15f3beb738d) | bad-trips PFA P4 his way (h04), 1 | Human | AI or mixed | shape echo |
| [bt-pfa-P3P4-D4](https://www.pangram.com/history/f1b3e3bb-30f2-4399-8398-82bd3998b413) | bad-trips PFA P4 his way (h04), 2 | Human | AI or mixed | parallel frames kept |
| [bt-r07-4](https://www.pangram.com/history/b8fbfcbc-c2d9-48b7-a1f8-0510320bb0a1) | bad-trips round 7 N-CANNA-2 (his forums and studies paragraph), 2 | Human | AI or mixed | **not explained yet** |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| bad-trips whole guide, published v5.5 | article | 1 of 2 | Mixed |
| bad-trips Psychological First Aid (h03) | section | 1 of 2 | AI |
| bad-trips PFA dangers paragraph (h03 P3) | paragraph | 2 of 6 | AI |
| bad-trips round 6 SEIZ-WARN B (cannabis at an aura) | paragraph | 4 of 6 | AI |
| bad-trips PFA P4 his way (h04) | pair | 4 of 6 | AI |

