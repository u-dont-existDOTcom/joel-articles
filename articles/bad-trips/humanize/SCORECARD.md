# Pangram prediction scorecard: bad trips guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/bad-trips/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.1 extension (free, live post; Joel's check of 2026-10-18, the same text as his 2026-11-03 paste by SHA-256) | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |
| Pangram web app (his account, Pangram Professional) | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |
| Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane | 41 | 34 (83%) | 71% | 29% | 46% | 0.167 (base 0.207, 41) |
| pangram 4.1, the web app: Joel's account, run by the lane in the desktop app's browser pane (E356) | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |

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
| the latest 50 | 41 | 34 (83%) | 71% | 29% | 46% | 0.167 (base 0.207, 41) |
| the latest 100 | 41 | 34 (83%) | 71% | 29% | 46% | 0.167 (base 0.207, 41) |
| all | 41 | 34 (83%) | 71% | 29% | 46% | 0.167 (base 0.207, 41) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 4 | 2 (50%) | 75% | 25% | 75% | 0.185 (base 0.188, 4) |
| paragraph | 29 | 26 (90%) | 62% | 38% | 48% | 0.160 (base 0.235, 29) |
| pair | 8 | 6 (75%) | 100% | 0% | 25% | 0.182 (base 0.000, 8) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 11 | 0.33 | 0% |
| 0.4 to 0.6 | 21 | 0.48 | 19% |
| 0.6 to 0.8 | 10 | 0.68 | 80% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## pangram 4.1, the web app: Joel's account, run by the lane in the desktop app's browser pane (E356)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |
| the latest 100 | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |
| all | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.4 to 0.6 | 6 | 0.49 | 33% |
| 0.6 to 0.8 | 3 | 0.67 | 100% |

## Misses since the ledger (9)

| cause | misses |
|---|---|
| not explained yet | 5 |
| shape echo | 1 |
| parallel frames kept | 1 |
| a flaw of sense left in the ending | 1 |
| rewording without a sense fix | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [bt-pfa-P3P4-D3](https://www.pangram.com/history/0993c7c4-386c-4a5b-821b-f15f3beb738d) | bad-trips PFA P4 his way (h04), 1 | Human | AI or mixed | shape echo |
| [bt-pfa-P3P4-D4](https://www.pangram.com/history/f1b3e3bb-30f2-4399-8398-82bd3998b413) | bad-trips PFA P4 his way (h04), 2 | Human | AI or mixed | parallel frames kept |
| [bt-r06-forums-2](https://www.pangram.com/history/fd1df50a-5f61-44ee-ad14-ab61bda0542c) | bad-trips Active Seizure N-FORUMS (what forums and the rat study say), 2 | Human | AI or mixed | a flaw of sense left in the ending |
| [bt-r06-forums-3](https://www.pangram.com/history/d3ff8463-b3c1-40f3-8852-d81cedc403ed) | bad-trips Active Seizure N-FORUMS (what forums and the rat study say), 3 | Human | AI or mixed | rewording without a sense fix |
| [bt-r07-4](https://www.pangram.com/history/b8fbfcbc-c2d9-48b7-a1f8-0510320bb0a1) | bad-trips round 7 N-CANNA-2 (his forums and studies paragraph), 2 | Human | AI or mixed | **not explained yet** |
| [bt-room1-fix-1](https://www.pangram.com/history/8e79642a-8589-4524-a59d-e8b88cf6ff1b) | bad-trips PFA room, first part: the room's questions and the annoying room (B238, B239), 1 | Human | AI or mixed | **not explained yet** |
| [bt-room1-fix-3](https://www.pangram.com/history/b2a7067f-443e-4caa-91c2-34a748bb9cc6) | bad-trips PFA room, first part: the room's questions and the annoying room (B238, B239), 3 | Human | AI or mixed | **not explained yet** |
| [bt-room-stretch-1](https://www.pangram.com/history/34d92f15-18c7-4849-9972-983239961bf9) | bad-trips PFA room stretch in place: my first part with his second (B238 to B241), 1 | Human | AI or mixed | **not explained yet** |
| [bt-room-stretch-2](https://www.pangram.com/history/3d9ca55e-df3a-4ea4-8866-2d6071ba1b10) | bad-trips PFA room stretch in place: my first part with his second (B238 to B241), 2 | Human | AI or mixed | **not explained yet** |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| bad-trips whole guide, published v5.5 | article | 1 of 2 | Mixed |
| bad-trips Psychological First Aid (h03) | section | 1 of 2 | AI |
| bad-trips PFA dangers paragraph (h03 P3) | paragraph | 2 of 6 | AI |
| bad-trips round 6 SEIZ-WARN B (cannabis at an aura) | paragraph | 4 of 6 | AI |
| bad-trips PFA P4 his way (h04) | pair | 4 of 6 | AI |
| bad-trips Active Seizure N-FORUMS (what forums and the rat study say) | paragraph | 4 of 6 | Mixed |
| bad-trips PFA P5 and P6 (look at the room; the annoying room) | pair | 1 of 6 | AI |
| bad-trips PFA P7 and P8 (dim the lights; music or quiet) | pair | 1 of 6 | AI |
| bad-trips PFA room his way: look at the room (B1) | paragraph | 5 of 6 | AI |
| bad-trips PFA room his way: music and water (B2, B3) | paragraph | 5 of 6 | AI |
| bad-trips PFA room, first part: the room's questions and the annoying room (B238, B239) | paragraph | 3 of 6 | AI |
| bad-trips PFA room stretch in place: my first part with his second (B238 to B241) | section | 2 of 2 | AI |
| bad-trips PFA room stretch as the guide has it after round 8 (his four paragraphs) | section | 1 of 2 | AI |

