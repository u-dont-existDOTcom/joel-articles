# Pangram prediction scorecard: bad trips guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/bad-trips/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.1 extension (free, live post; Joel's check of 2026-10-18, the same text as his 2026-11-03 paste by SHA-256) | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |
| Pangram web app (his account, Pangram Professional) | 3 | 3 (100%) | 100% | 0% | 0% | 0.092 (base 0.000, 3) |
| Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane | 193 | 178 (92%) | 88% | 12% | 14% | 0.128 (base 0.109, 193) |
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
| the latest 50 | 50 | 47 (94%) | 94% | 6% | 0% | 0.102 (base 0.056, 50) |
| the latest 100 | 100 | 96 (96%) | 96% | 4% | 0% | 0.100 (base 0.038, 100) |
| all | 193 | 178 (92%) | 88% | 12% | 14% | 0.128 (base 0.109, 193) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 37 | 34 (92%) | 95% | 5% | 14% | 0.099 (base 0.051, 37) |
| paragraph | 109 | 101 (93%) | 84% | 16% | 14% | 0.120 (base 0.132, 109) |
| pair | 47 | 43 (91%) | 89% | 11% | 15% | 0.171 (base 0.095, 47) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 11 | 0.14 | 0% |
| 0.2 to 0.4 | 107 | 0.29 | 4% |
| 0.4 to 0.6 | 65 | 0.45 | 17% |
| 0.6 to 0.8 | 11 | 0.68 | 82% |
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

## Misses since the ledger (17)

| cause | misses |
|---|---|
| in place | 3 |
| context | 3 |
| shape echo | 1 |
| parallel frames kept | 1 |
| a flaw of sense left in the ending | 1 |
| rewording without a sense fix | 1 |
| not explained yet | 1 |
| a quip kept | 1 |
| one sentence changed | 1 |
| the panel's one unanimous tell was the mirrored pair ('Many bad trips get worse because' / 'Others get worse because'); one sentence said as talk ('Other times it's the opposite:') broke it, and the four -ing list I expected to keep it AI did not | 1 |
| the integration list's items say who runs what and for whom in plain, specific terms (five free sessions, a monthly group, meditation-related difficulties); none of the list tells I expected (name-colon-description) mattered here | 1 |
| the opening's second sentence was the driver: 'Hours and services change, and not every option works in every country.' said as 'Their hours and services change, and some only work in one country.' turned every window Human, the first sentence left as it was | 1 |
| the clipped three-imperative rhythm was the driver: said as one flowing sentence it read Human, while changing only the last sentence (keeping two clipped ones) read 100% | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [bt-r06-forums-2](https://www.pangram.com/history/fd1df50a-5f61-44ee-ad14-ab61bda0542c) | bad-trips Active Seizure N-FORUMS (what forums and the rat study say), 2 | Human | AI or mixed | a flaw of sense left in the ending |
| [bt-r06-forums-3](https://www.pangram.com/history/d3ff8463-b3c1-40f3-8852-d81cedc403ed) | bad-trips Active Seizure N-FORUMS (what forums and the rat study say), 3 | Human | AI or mixed | rewording without a sense fix |
| [bt-r07-4](https://www.pangram.com/history/b8fbfcbc-c2d9-48b7-a1f8-0510320bb0a1) | bad-trips round 7 N-CANNA-2 (his forums and studies paragraph), 2 | Human | AI or mixed | **not explained yet** |
| [bt-room1-fix-1](https://www.pangram.com/history/8e79642a-8589-4524-a59d-e8b88cf6ff1b) | bad-trips PFA room, first part: the room's questions and the annoying room (B238, B239), 1 | Human | AI or mixed | a quip kept |
| [bt-room1-fix-3](https://www.pangram.com/history/b2a7067f-443e-4caa-91c2-34a748bb9cc6) | bad-trips PFA room, first part: the room's questions and the annoying room (B238, B239), 3 | Human | AI or mixed | one sentence changed |
| [bt-room-stretch-1](https://www.pangram.com/history/34d92f15-18c7-4849-9972-983239961bf9) | bad-trips PFA room stretch in place: my first part with his second (B238 to B241), 1 | Human | AI or mixed | in place |
| [bt-room-stretch-2](https://www.pangram.com/history/3d9ca55e-df3a-4ea4-8866-2d6071ba1b10) | bad-trips PFA room stretch in place: my first part with his second (B238 to B241), 2 | Human | AI or mixed | in place |
| [bt-room-stretch-4](https://www.pangram.com/history/6808a624-26bf-48d8-a5d9-96252b6c95e9) | bad-trips PFA room stretch in place: my first part with his second (B238 to B241), 4 | Human | AI or mixed | in place |
| [bt-dangers-heading](https://www.pangram.com/history/2745e050-1573-4da8-9c6a-ba510f0a80e6) | bad-trips PFA dangers paragraph with the section heading, 1 | AI | Human | context |
| [bt-test-acts](https://www.pangram.com/history/5a123a1a-623a-40ad-85ba-d4c6c869fe68) | bad-trips PFA dangers with the room's acts only, 1 | Human | AI or mixed | context |
| [bt-test-fixes](https://www.pangram.com/history/904c30a7-fe86-4630-8209-e1c049471074) | bad-trips PFA dangers with the fixes line only, 1 | AI | Human | context |
| [bt-anchor-v1](https://www.pangram.com/history/88fa84a3-9569-4e9b-84af-51c80a0efdd7) | bad-trips Get One Human Anchor P1 after the Human section, 2 | AI | Human | the panel's one unanimous tell was the mirrored pair ('Many bad trips get worse because' / 'Others get worse because'); one sentence said as talk ('Other times it's the opposite:') broke it, and the four -ing list I expected to keep it AI did not |
| [bt-contact-K5-after](https://www.pangram.com/history/07ee0dd7-de31-4f93-8630-16521ad77701) | bad-trips Who to Contact, and When after the Human section, K5-after, 1 | AI | Human | the integration list's items say who runs what and for whom in plain, specific terms (five free sessions, a monthly group, meditation-related difficulties); none of the list tells I expected (name-colon-description) mattered here |
| [bt-contact-kv2](https://www.pangram.com/history/3328665a-ddf4-4fbc-998c-58a8906ada02) | bad-trips Who to Contact, and When after the Human section, the opening's second sentence, 1 | AI | Human | the opening's second sentence was the driver: 'Hours and services change, and not every option works in every country.' said as 'Their hours and services change, and some only work in one country.' turned every window Human, the first sentence left as it was |
| [bt-nra-n3a](https://www.pangram.com/history/795e7185-2001-4eb5-ae47-9e7c0deb0dd9) | bad-trips No Rash Actions after the Human section, N3, 2 | AI | Human | the clipped three-imperative rhythm was the driver: said as one flowing sentence it read Human, while changing only the last sentence (keeping two clipped ones) read 100% |

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
| bad-trips PFA room stretch in place: my first part with his second (B238 to B241) | section | 6 of 2 | AI |
| bad-trips PFA room stretch as the guide has it after round 8 (his four paragraphs) | section | 1 of 2 | AI |
| bad-trips PFA room stretch, first paragraph alone (try 5's) | paragraph | 1 of 6 | AI |
| bad-trips PFA room stretch without the stock tips (a test: what the guide says elsewhere cut) | pair | 1 of 6 | AI |
| bad-trips PFA first five minutes, the section as the guide has it after round 9 | section | 5 of 2 | AI |
| bad-trips PFA section fix 1, first half (intro, dangers, room) | pair | 1 of 6 | AI |
| bad-trips PFA section fix 1, second half (the scripts and what comes next) | pair | 1 of 6 | AI |
| bad-trips PFA first half, the room said once | pair | 2 of 6 | AI |
| bad-trips PFA first half, the room said once, without the intro | pair | 2 of 6 | AI |
| bad-trips PFA dangers with the room's first sentence only | pair | 1 of 6 | AI |
| bad-trips PFA dangers with the room's acts only | pair | 1 of 6 | AI |
| bad-trips PFA first half, room paragraph cut, its own points after the fixes line | pair | 1 of 6 | AI |
| bad-trips PFA first half with the reminder | section | 2 of 2 | Mixed |
| bad-trips PFA first half with the practice part | section | 2 of 2 | Mixed |
| bad-trips PFA first half with the next-steps paragraph | section | 1 of 2 | AI |
| bad-trips PFA section, second half reworked after the cuts | section | 1 of 2 | AI |
| bad-trips PFA section, the second half said once | section | 2 of 2 | Mixed |
| bad-trips PFA practice lines beside the Human section | pair | 1 of 6 | Mixed |
| bad-trips Stillness or Movement paragraph 1 after the Human section | pair | 6 of 6 | Mixed |
| bad-trips Stillness or Movement paragraph 2 after the Human section | pair | 5 of 6 | AI |
| bad-trips Stillness or Movement paragraph 3 after the Human section | pair | 6 of 6 | Mixed |
| bad-trips Stillness or Movement paragraph 4 after the Human section | pair | 6 of 6 | Mixed |
| bad-trips Get One Human Anchor, the section as the guide has it | section | 1 of 2 | AI |
| bad-trips Get One Human Anchor after the committee cut | section | 2 of 2 | AI |
| bad-trips Get One Human Anchor P2 after the Human section | paragraph | 2 of 6 | AI |
| bad-trips Get One Human Anchor script 1 after the Human section | paragraph | 1 of 6 | AI |
| bad-trips Get One Human Anchor script 2 after the Human section | paragraph | 2 of 6 | Mixed |
| bad-trips Get One Human Anchor P1 after the Human section, first sentence changed | paragraph | 1 of 6 | Mixed |
| bad-trips Get One Human Anchor P2 after the Human section and P1, first sentence changed | paragraph | 1 of 6 | AI |
| bad-trips Get One Human Anchor P2 after the Human section and P1, second sentence changed | paragraph | 1 of 6 | AI |
| bad-trips Get One Human Anchor P2 after the Human section and P1, third sentence changed | paragraph | 1 of 6 | AI |
| bad-trips Get One Human Anchor script 2 after the Human section and P1, last sentence changed | paragraph | 1 of 6 | AI |
| bad-trips Get One Human Anchor script 1 after the Human section and P1, last sentence split | paragraph | 1 of 6 | AI |
| bad-trips Get One Human Anchor P2 after the Human section and P1, said again whole | paragraph | 2 of 6 | Mixed |
| bad-trips Get One Human Anchor P2 after the Human section and P1, backup first | paragraph | 1 of 6 | AI |
| bad-trips Get One Human Anchor script 1 after the Human section and P1, said again whole | paragraph | 3 of 6 | Mixed |
| bad-trips Get One Human Anchor script 2 after the Human section and P1, said again whole | paragraph | 3 of 6 | AI |
| bad-trips Get One Human Anchor P2 after the Human section and P1, W1 with its reasons chained | paragraph | 1 of 6 | Mixed |
| bad-trips Get One Human Anchor P2 after the Human section and P1, W1 with an aside | paragraph | 2 of 6 | Mixed |
| bad-trips Get One Human Anchor P2 after the Human section and P1, X3 with the reasons as events | paragraph | 1 of 6 | Mixed |
| bad-trips Get One Human Anchor P2 after the Human section and P1, X3 with its first sentence as a pick | paragraph | 1 of 6 | Mixed |
| bad-trips Get One Human Anchor P2 after the Human section and P1, X3 with what works better | paragraph | 1 of 6 | Mixed |
| bad-trips Get One Human Anchor P2 after the Human section and P1, X3's first two sentences joined | paragraph | 1 of 6 | Mixed |
| bad-trips Get One Human Anchor after the Human section, the card's section | section | 1 of 2 | AI |
| bad-trips Who to Contact, and When as the guide has it | section | 2 of 2 | AI |
| bad-trips Who to Contact, and When after the Human section | section | 2 of 2 | Mixed |
| bad-trips Alone at 3 a.m. as the guide has it | section | 1 of 2 | AI |
| bad-trips Alone at 3 a.m. after the Human section | section | 1 of 2 | Mixed |
| bad-trips Alone at 3 a.m. after the Human section, the lamp sentence changed | paragraph | 1 of 6 | Mixed |
| bad-trips Alone at 3 a.m. after the Human section, the triage line changed | paragraph | 1 of 6 | Mixed |
| bad-trips Alone at 3 a.m. after the Human section, the sleep line joined | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping, its opening, as the guide has it | section | 1 of 2 | AI |
| bad-trips For the Person Helping, its Do and Don't lists, as the guide has them | section | 1 of 2 | AI |
| bad-trips When the Content Turns Toward Harm, as the guide has it | section | 1 of 2 | AI |
| bad-trips Who to Contact, and When after the Human section, K1-intro | paragraph | 2 of 6 | Mixed |
| bad-trips Who to Contact, and When after the Human section, K2-during | paragraph | 1 of 6 | Mixed |
| bad-trips Who to Contact, and When after the Human section, K3-global | paragraph | 2 of 6 | Mixed |
| bad-trips Who to Contact, and When after the Human section, K4-us | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, Pa-B280 | paragraph | 3 of 6 | AI |
| bad-trips For the Person Helping after the Human section, Pb-B82 | paragraph | 2 of 6 | AI |
| bad-trips For the Person Helping after the Human section, Pc-B83 | paragraph | 2 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, Pd-B84 | paragraph | 2 of 6 | AI |
| bad-trips For the Person Helping after the Human section, Pd-B84, the two don'ts joined | paragraph | 1 of 6 | Mixed |
| bad-trips Who to Contact, and When after the Human section and its opening, the first list | paragraph | 2 of 6 | Mixed |
| bad-trips Who to Contact, and When after the Human section and its opening, the directories | paragraph | 2 of 6 | Mixed |
| bad-trips Who to Contact, and When after the Human section and its opening, the first list's Fireside line | paragraph | 1 of 6 | Mixed |
| bad-trips Who to Contact, and When after the Human section and its opening, the directories' second sentence | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, the opening without the grief paragraph | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, L1-do | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, L2-dont | paragraph | 1 of 6 | AI |
| bad-trips For the Person Helping after the Human section, HA-god | paragraph | 2 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, HB-lines | paragraph | 2 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, HC-safety | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, HD-call | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, HA-god's second sentence | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping after the Human section, HB-lines' other-lines label | paragraph | 1 of 6 | Mixed |
| bad-trips No Rash Actions as the guide has it | section | 1 of 2 | AI |
| bad-trips No Rash Actions after the Human section | section | 1 of 2 | Mixed |
| bad-trips No Rash Actions after the Human section, N1 | paragraph | 1 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N2 | paragraph | 2 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N4 | paragraph | 1 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N5 | paragraph | 1 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N2's list | paragraph | 1 of 6 | AI |
| bad-trips No Rash Actions after the Human section, N3's last sentence | paragraph | 1 of 6 | AI |
| bad-trips No Rash Actions after the Human section, N2, the term kept | paragraph | 1 of 6 | Mixed |

