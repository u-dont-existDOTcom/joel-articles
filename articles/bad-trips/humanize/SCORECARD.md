# Pangram prediction scorecard: bad trips guide

Built by `tools/humanization/pangram_ledger.py build` from `articles/bad-trips/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| Pangram 4.1 extension (free, live post; Joel's check of 2026-10-18, the same text as his 2026-11-03 paste by SHA-256) | 1 | 1 (100%) | 100% | 0% | 0% | 0.000 (base 0.000, 1) |
| Pangram web app (his account, Pangram Professional) | 73 | 52 (71%) | 47% | 53% | 63% | 0.198 (base 0.249, 73) |
| Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane | 348 | 316 (91%) | 87% | 13% | 14% | 0.132 (base 0.113, 348) |
| pangram 4.1, the web app: Joel's account, run by the lane in the desktop app's browser pane (E356) | 8 | 6 (75%) | 50% | 50% | 75% | 0.170 (base 0.250, 8) |
| Pangram web app (his account) | 49 | 40 (82%) | 67% | 33% | 14% | 0.147 (base 0.220, 49) |
| Pangram web app (his account, Pangram Professional), in the desktop app's browser pane | 89 | 74 (83%) | 44% | 56% | 57% | 0.188 (base 0.246, 89) |
| Pangram web app (his account), in the desktop app's browser pane | 45 | 34 (76%) | 56% | 44% | 42% | 0.188 (base 0.247, 45) |
| Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py) | 82 | 58 (71%) | 35% | 65% | 72% | 0.212 (base 0.229, 82) |

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
| the latest 50 | 50 | 32 (64%) | 48% | 52% | 64% | 0.209 (base 0.250, 50) |
| the latest 100 | 73 | 52 (71%) | 47% | 53% | 63% | 0.198 (base 0.249, 73) |
| all | 73 | 52 (71%) | 47% | 53% | 63% | 0.198 (base 0.249, 73) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 17 | 12 (71%) | 24% | 76% | 82% | 0.206 (base 0.180, 17) |
| paragraph | 32 | 20 (62%) | 62% | 38% | 62% | 0.208 (base 0.234, 32) |
| stretch | 3 | 3 (100%) | 67% | 33% | 33% | 0.138 (base 0.222, 3) |
| pair | 21 | 17 (81%) | 38% | 62% | 52% | 0.186 (base 0.236, 21) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 14 | 0.32 | 7% |
| 0.4 to 0.6 | 44 | 0.52 | 57% |
| 0.6 to 0.8 | 24 | 0.65 | 83% |
| 0.8 to 1.0 | 1 | 0.85 | 100% |

## Pangram web app (his account, Pangram Professional), through the Claude desktop app's browser pane

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 42 (84%) | 84% | 16% | 24% | 0.188 (base 0.134, 50) |
| the latest 100 | 100 | 87 (87%) | 86% | 14% | 15% | 0.151 (base 0.120, 100) |
| all | 348 | 316 (91%) | 87% | 13% | 14% | 0.132 (base 0.113, 348) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 68 | 65 (96%) | 93% | 7% | 12% | 0.083 (base 0.068, 68) |
| paragraph | 233 | 208 (89%) | 85% | 15% | 14% | 0.138 (base 0.128, 233) |
| pair | 47 | 43 (91%) | 89% | 11% | 15% | 0.171 (base 0.095, 47) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 26 | 0.13 | 0% |
| 0.2 to 0.4 | 187 | 0.29 | 5% |
| 0.4 to 0.6 | 119 | 0.46 | 18% |
| 0.6 to 0.8 | 17 | 0.66 | 82% |
| 0.8 to 1.0 | 5 | 0.80 | 80% |

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

## Pangram web app (his account)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 49 | 40 (82%) | 67% | 33% | 14% | 0.147 (base 0.220, 49) |
| the latest 100 | 49 | 40 (82%) | 67% | 33% | 14% | 0.147 (base 0.220, 49) |
| all | 49 | 40 (82%) | 67% | 33% | 14% | 0.147 (base 0.220, 49) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| section | 49 | 40 (82%) | 67% | 33% | 14% | 0.147 (base 0.220, 49) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 11 | 0.12 | 9% |
| 0.2 to 0.4 | 30 | 0.27 | 23% |
| 0.4 to 0.6 | 3 | 0.55 | 100% |
| 0.6 to 0.8 | 5 | 0.65 | 100% |
| 0.8 to 1.0 | 2 | 0.82 | 100% |

## Pangram web app (his account, Pangram Professional), in the desktop app's browser pane

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 42 (84%) | 58% | 42% | 30% | 0.184 (base 0.244, 50) |
| the latest 100 | 89 | 74 (83%) | 44% | 56% | 57% | 0.188 (base 0.246, 89) |
| all | 89 | 74 (83%) | 44% | 56% | 57% | 0.188 (base 0.246, 89) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 38 | 31 (82%) | 34% | 66% | 68% | 0.192 (base 0.225, 38) |
| pair | 20 | 15 (75%) | 65% | 35% | 40% | 0.208 (base 0.227, 20) |
| heading | 15 | 14 (93%) | 13% | 87% | 93% | 0.195 (base 0.116, 15) |
| stretch | 15 | 13 (87%) | 73% | 27% | 13% | 0.154 (base 0.196, 15) |
| section | 1 | 1 (100%) | 0% | 100% | 100% | 0.040 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 31 | 0.30 | 23% |
| 0.4 to 0.6 | 51 | 0.54 | 71% |
| 0.6 to 0.8 | 25 | 0.62 | 92% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## Pangram web app (his account), in the desktop app's browser pane

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 45 | 34 (76%) | 56% | 44% | 42% | 0.188 (base 0.247, 45) |
| the latest 100 | 45 | 34 (76%) | 56% | 44% | 42% | 0.188 (base 0.247, 45) |
| all | 45 | 34 (76%) | 56% | 44% | 42% | 0.188 (base 0.247, 45) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 30 | 22 (73%) | 67% | 33% | 33% | 0.185 (base 0.222, 30) |
| pair | 6 | 4 (67%) | 50% | 50% | 17% | 0.205 (base 0.250, 6) |
| section | 1 | 1 (100%) | 100% | 0% | 0% | 0.122 (base 0.000, 1) |
| heading | 7 | 7 (100%) | 0% | 100% | 100% | 0.184 (base 0.000, 7) |
| stretch | 1 | 0 (0%) | 100% | 0% | 100% | 0.250 (base 0.000, 1) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 2 | 0.03 | 0% |
| 0.2 to 0.4 | 10 | 0.30 | 20% |
| 0.4 to 0.6 | 29 | 0.50 | 48% |
| 0.6 to 0.8 | 8 | 0.65 | 88% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 36 (72%) | 36% | 64% | 56% | 0.203 (base 0.230, 50) |
| the latest 100 | 82 | 58 (71%) | 35% | 65% | 72% | 0.212 (base 0.229, 82) |
| all | 82 | 58 (71%) | 35% | 65% | 72% | 0.212 (base 0.229, 82) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 82 | 58 (71%) | 35% | 65% | 72% | 0.212 (base 0.229, 82) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.0 to 0.2 | 7 | 0.13 | 14% |
| 0.2 to 0.4 | 12 | 0.26 | 50% |
| 0.4 to 0.6 | 47 | 0.55 | 68% |
| 0.6 to 0.8 | 31 | 0.63 | 71% |
| 0.8 to 1.0 | 5 | 0.87 | 100% |

## Misses since the ledger (114)

| cause | misses |
|---|---|
| not explained yet | 25 |
| context | 11 |
| his voice outweighed a lone tell | 10 |
| its AI window came from a bigger check, not from the paragraph by itself | 7 |
| in place | 5 |
| my plain instructing voice | 4 |
| his frame with my words | 3 |
| shape echo | 1 |
| parallel frames kept | 1 |
| a flaw of sense left in the ending | 1 |
| rewording without a sense fix | 1 |
| a quip kept | 1 |
| one sentence changed | 1 |
| the panel's one unanimous tell was the mirrored pair ('Many bad trips get worse because' / 'Others get worse because'); one sentence said as talk ('Other times it's the opposite:') broke it, and the four -ing list I expected to keep it AI did not | 1 |
| the integration list's items say who runs what and for whom in plain, specific terms (five free sessions, a monthly group, meditation-related difficulties); none of the list tells I expected (name-colon-description) mattered here | 1 |
| the opening's second sentence was the driver: 'Hours and services change, and not every option works in every country.' said as 'Their hours and services change, and some only work in one country.' turned every window Human, the first sentence left as it was | 1 |
| the clipped three-imperative rhythm was the driver: said as one flowing sentence it read Human, while changing only the last sentence (keeping two clipped ones) read 100% | 1 |
| a three-clause hedge stack | 1 |
| his five fixes carried the pair | 1 |
| his keep word in my frame | 1 |
| his list frame without his words | 1 |
| underweighted the structural fix | 1 |
| underweighted his version and the shape | 1 |
| underweighted the shape | 1 |
| the reader's added explanation read AI | 1 |
| called AI where it read Human, Low | 1 |
| the definitional pair after the action read AI | 1 |
| by itself, my explanatory register read AI throughout | 1 |
| his first person moved one window, not the paragraph | 1 |
| his words, opened on the scope, read Human | 1 |
| the longer heat line took the whole list to AI | 1 |
| his own heat line read AI in the list by itself | 1 |
| a run of category words beside a first-person story | 1 |
| his version's last two sentences beside a short lead-in line of mine | 1 |
| a short packed paragraph beside a list | 1 |
| a gloss said as a stock phrase | 1 |
| the split of a packed sentence | 1 |
| the reads' and the panel's marks fixed at once | 1 |
| the ending's missing payoff was the driver | 1 |
| existing lines, not the rename | 1 |
| his step 2 carried the pair | 1 |
| his step 2 carried its pair | 1 |
| the first person was not the driver | 1 |
| the reasons hung on each rule in one shape, and the drive line not pictured | 1 |
| a checklist built evenly, each act with its purpose, one purpose said twice | 1 |
| the reader's own moment first carried the remedy list | 1 |
| my tapping sentence put two asides in brackets in one sentence (the term, then 'instead' and the technique's name), where his line it replaced had one bracket after an act ('do some fidgeting (especially of the calf muscle, flexing the feet)') | 1 |
| the seizure lines don't follow the step: 'while you wait for an ambulance' right after 'before the ambulance comes', and 'do' breaks his 'I'd'; with them his own two sentences read AI Medium, where with his breathing line the step read Human High (6e5ea946) | 1 |
| step 8 grew to 247 words: DMSO in two sentences with a reason far from the act (a hospital infusion for a skin rub, the fit reader's mark), and his topical fragment made a sentence; the lines that read High in round 49 (a3c02dd9) went Low in the longer step | 1 |
| the Call Medics For list has read AI since the start: it is one of the medical sections not yet humanized (round 36's MEDICAL-HOW list); the one line that changed is the wording he approved | 1 |
| I priced the medical part's record (eight of eight of my tries AI on 2026-11-12, five of five on the kidney paragraph) and not what this try did differently: every sentence tied to the one before by what they share, each warning said as what happens or what to do, the caution in the first person, the ways of his round-57 kidney fix | 1 |
| I called the three paragraphs from the section's last reading in place (Human High 39, AI Low 9, AI High 49, AI Medium 8) and took the AI windows to be these; they were the paragraphs after them. B139 with his answer and B86's first two sentences read Human High 56, and only B86's list sentence fell short (Human Low 14) | 1 |
| I called it from the paragraph's run of eight signs, which stays, and from my record on this guide's body paragraphs; what changed was the verdict after the run: 'belongs in a different branch' became the two places in the guide a reader can go to, and the closing aphorism became the reason joined to that sentence | 1 |
| I called it from the section's reading in place (AI High 36, AI Low 40, AI Medium 12 over the first gut-tool paragraphs) and from its list of three ferments and its 'although ... which then requires' clause; by itself it reads Human High 56 in one window. Three of its four sentences are his practice in his plain words ('I prefer fermented beet juice made with apple vinegar and salt', 'Smelling the ferment helps a lot', 'Drinking a spoonful can also help') | 1 |
| the same: called from the section's reading in place. By themselves the two paragraphs read Human in every window, but none High (Low 9, Low 15, Low 30, Medium 18, Low 21), so both are still work to do. They are what he does with zeolite, in the first person, but in short flat sentences with nothing joining them ('Most sober people don't feel much from zeolite. Its effect becomes more obvious when ...') | 1 |
| I called AI because B151 read AI High as it stood an hour before (fc82fa68, with B153) and only seven of its words changed. It read Human High 151 in one window with the paragraph from his round-59 answer after it. Two things I underweighted: the AI window had held B153's seven-item list too, so it did not say B151 was the cause; and the three changes were the three places the readers could not follow (what 'These' are, what 'the come-up' is, what 'more mysterious' means) | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [a3-b114](https://www.pangram.com/history/25bc9042-d058-40dd-b052-f7c2c6ab660f) | bad-trips MDMA: Magnesium Alarm, the jaw alarm (B114) (h73), 2 | Human | AI or mixed | **not explained yet** |
| [a3-b117p](https://www.pangram.com/history/a74bc7a7-dcde-41f1-9a83-49b00d5ca2f8) | bad-trips MDMA: Magnesium Alarm, the softer peak (B117) (h73), 2 | Human | AI or mixed | **not explained yet** |
| [a3-b118](https://www.pangram.com/history/162c5eaf-11c9-4eca-bdb6-e90cee404bc5) | bad-trips MDMA: Magnesium Alarm, his second wife (B118) (h73), 2 | Human | AI or mixed | **not explained yet** |
| [a3-b120](https://www.pangram.com/history/230891b4-4860-4f70-aa2b-f80f19baecb2) | bad-trips MDMA: Magnesium Alarm, the kidneys (B120) (h73), 2 | Human | AI or mixed | **not explained yet** |
| [blind-b118](https://www.pangram.com/history/9cd7ae31-9cba-446c-8ad8-d55257ef87a5) | bad-trips B118, blind rewrite from his round-55 lessons (replay h74), 1 | AI | Human | **not explained yet** |
| [a2-b115](https://www.pangram.com/history/59518a51-ab5c-466e-b7ee-4b12b407d77d) | bad-trips MDMA: Magnesium Alarm, his amounts with why magnesium chloride (h74), 1 | Human | AI or mixed | **not explained yet** |
| [a2-b120](https://www.pangram.com/history/e2566e53-84ec-45c7-880d-87b8cbdcecda) | bad-trips MDMA: Magnesium Alarm, the kidneys from his post's text with his round-55 ways (h74), 1 | Human | AI or mixed | **not explained yet** |
| [asis-b111](https://www.pangram.com/history/e2e90101-4127-45cd-acf8-db5aa934890f) | bad-trips Seizure: What Else Helps, the magnesium and CBD paragraph (B111) as it stands, by itself (h75), 1 | AI | Human | **not explained yet** |
| [asis-b133](https://www.pangram.com/history/6d78093f-18c6-467b-9d77-015394d39638) | bad-trips How to Check for SS, the five patterns (B133) as they stand, by themselves (h75), 1 | AI | Human | **not explained yet** |
| [a2-b127-b128](https://www.pangram.com/history/75a2458d-38e7-4413-8d12-9ac6f8e7824c) | bad-trips Swallowed Too Much?, the charcoal and poison control paragraphs (B127, B128) as they stand, together (h75), 2 | AI | Human | I priced the medical part's record (eight of eight of my tries AI on 2026-11-12, five of five on the kidney paragraph) and not what this try did differently: every sentence tied to the one before by what they share, each warning said as what happens or what to do, the caution in the first person, the ways of his round-57 kidney fix |
| [asis-b139-open](https://www.pangram.com/history/d9dea7a8-acff-4c1a-b3cc-a7e9372a7452) | bad-trips My Acute Rescue Remedies, its first three paragraphs (B139, N-AN-Q1, B86) as they stand, together (h77), 1 | AI | Human | I called the three paragraphs from the section's last reading in place (Human High 39, AI Low 9, AI High 49, AI Medium 8) and took the AI windows to be these; they were the paragraphs after them. B139 with his answer and B86's first two sentences read Human High 56, and only B86's list sentence fell short (Human Low 14) |
| [a2-b141](https://www.pangram.com/history/6f789f5b-e8f0-451e-95a2-5de3b943f76d) | bad-trips My Acute Rescue Remedies, the gut-driven paragraph (B141) as it stands, by itself (h77), 2 | AI | Human | I called it from the paragraph's run of eight signs, which stays, and from my record on this guide's body paragraphs; what changed was the verdict after the run: 'belongs in a different branch' became the two places in the guide a reader can go to, and the closing aphorism became the reason joined to that sentence |
| [asis-b154](https://www.pangram.com/history/c293133e-f9b6-46a2-98eb-85e71e6a6ae0) | bad-trips ZeoCharge & Ferment, the ferments paragraph (B154) as it stands, by itself (h78), 1 | AI | Human | I called it from the section's reading in place (AI High 36, AI Low 40, AI Medium 12 over the first gut-tool paragraphs) and from its list of three ferments and its 'although ... which then requires' clause; by itself it reads Human High 56 in one window. Three of its four sentences are his practice in his plain words ('I prefer fermented beet juice made with apple vinegar and salt', 'Smelling the ferment helps a lot', 'Drinking a spoonful can also help') |
| [asis-b158-b155](https://www.pangram.com/history/25652097-7c2d-444d-ab06-9e9af3c993c1) | bad-trips ZeoCharge & Ferment, how he takes zeolite and how it has to be prepared (B158, B155) as they stand, together (h78), 1 | AI | Human | the same: called from the section's reading in place. By themselves the two paragraphs read Human in every window, but none High (Low 9, Low 15, Low 30, Medium 18, Low 21), so both are still work to do. They are what he does with zeolite, in the first person, but in short flat sentences with nothing joining them ('Most sober people don't feel much from zeolite. Its effect becomes more obvious when ...') |
| [a4-gutintro](https://www.pangram.com/history/a53a2ce3-838c-409f-801f-bfa6d403d9d9) | bad-trips Gut-Toxin & Die-Off Tools, its opening: B151 and the paragraph from his round-59 answer 2.2 (new block R59-GUT-COMMON), together (h78), 1 | AI | Human | I called AI because B151 read AI High as it stood an hour before (fc82fa68, with B153) and only seven of its words changed. It read Human High 151 in one window with the paragraph from his round-59 answer after it. Two things I underweighted: the AI window had held B153's seven-item list too, so it did not say B151 was the cause; and the three changes were the three places the readers could not follow (what 'These' are, what 'the come-up' is, what 'more mysterious' means) |

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
| bad-trips No Rash Actions after the Human section, N1 | paragraph | 2 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N2 | paragraph | 2 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N4 | paragraph | 2 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N5 | paragraph | 2 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N2's list | paragraph | 1 of 6 | AI |
| bad-trips No Rash Actions after the Human section, N3's last sentence | paragraph | 1 of 6 | AI |
| bad-trips No Rash Actions after the Human section, N2, the term kept | paragraph | 1 of 6 | Mixed |
| bad-trips When the Trip Feels Amazing as the guide has it | section | 1 of 2 | AI |
| bad-trips When the Trip Feels Amazing after the Human section | section | 2 of 2 | Mixed |
| bad-trips When the Trip Feels Amazing after the Human section, A1 | paragraph | 2 of 6 | Mixed |
| bad-trips When the Trip Feels Amazing after the Human section, A2 | paragraph | 1 of 6 | Mixed |
| bad-trips When the Trip Feels Amazing after the Human section, A3 | paragraph | 1 of 6 | Mixed |
| bad-trips When the Trip Feels Amazing after the Human section, A4 | paragraph | 2 of 6 | Mixed |
| bad-trips (Re)defining "Bad Trip" as the guide has it | section | 1 of 2 | AI |
| bad-trips (Re)defining "Bad Trip" after the Human section | section | 1 of 2 | Mixed |
| bad-trips (Re)defining "Bad Trip" after the Human section, R2 | paragraph | 3 of 6 | AI |
| bad-trips Spiritual is not Getting Your Ass Kicked as the guide has it | section | 1 of 2 | AI |
| bad-trips Spiritual is not Getting Your Ass Kicked after the Human section | section | 1 of 2 | Mixed |
| bad-trips Spiritual is not Getting Your Ass Kicked after the Human section, S2 | paragraph | 3 of 6 | AI |
| bad-trips The Other Bypass as the guide has it | section | 1 of 2 | Mixed |
| bad-trips The Other Bypass after the Human section, O5 | paragraph | 2 of 6 | Mixed |
| bad-trips The Other Bypass after the Human section, as the guide now has it | section | 1 of 2 | Mixed |
| bad-trips Why Bad Trips Tend to Happen as the guide has it | section | 1 of 2 | AI |
| bad-trips Why Bad Trips Tend to Happen after the Human section | section | 1 of 2 | Mixed |
| bad-trips Why Bad Trips Tend to Happen after the Human section, W2 | paragraph | 1 of 6 | Mixed |
| bad-trips Why Bad Trips Tend to Happen after the Human section, W3 | paragraph | 2 of 6 | Mixed |
| bad-trips Why Bad Trips Tend to Happen after the Human section, W4 | paragraph | 3 of 6 | Mixed |
| bad-trips Give the Session a Beginning and an End as the guide has it | section | 1 of 2 | AI |
| bad-trips Give the Session a Beginning and an End after the Human section | section | 1 of 2 | Mixed |
| bad-trips Give the Session a Beginning and an End after the Human section, G1 | paragraph | 2 of 6 | Mixed |
| bad-trips The Fear/Panic Loop as the guide has it | section | 1 of 2 | AI |
| bad-trips The Fear/Panic Loop after the Human section | section | 1 of 2 | Mixed |
| bad-trips The Fear/Panic Loop after the Human section, F1 | paragraph | 2 of 6 | AI |
| bad-trips The Fear/Panic Loop after the Human section, F2 | paragraph | 2 of 6 | Mixed |
| bad-trips Dealing With Sorrow as the guide has it | section | 1 of 2 | Mixed |
| bad-trips Dealing With Sorrow after the Human section | section | 1 of 2 | Mixed |
| bad-trips Dealing With Sorrow after the Human section, S2 | paragraph | 2 of 6 | Mixed |
| bad-trips Dealing With Sorrow after the Human section, S3 | paragraph | 2 of 6 | AI |
| bad-trips Hand on Heart as the guide has it | section | 1 of 2 | AI |
| bad-trips Hand on Heart after the Human section | section | 1 of 2 | Mixed |
| bad-trips Hand on Heart after the Human section, H1 | paragraph | 2 of 6 | Mixed |
| bad-trips Hand on Heart after the Human section, H2 | paragraph | 1 of 6 | Mixed |
| bad-trips Hand on Heart after the Human section, HT | paragraph | 2 of 6 | Mixed |
| bad-trips Demons, Jinn, Entities as the guide has it | section | 1 of 2 | AI |
| bad-trips Demons, Jinn, Entities after the Human section | section | 1 of 2 | Mixed |
| bad-trips Demons, Jinn, Entities after the Human section, DB | paragraph | 2 of 6 | Mixed |
| bad-trips Demons, Jinn, Entities after the Human section, DC | paragraph | 2 of 6 | Mixed |
| bad-trips Demons, Jinn, Entities after the Human section, DD | paragraph | 2 of 6 | Mixed |
| bad-trips Demons, Jinn, Entities after the Human section, DE | paragraph | 1 of 6 | AI |
| bad-trips Abuse Memories as the guide has it | section | 1 of 2 | AI |
| bad-trips Abuse Memories after the Human section | section | 1 of 2 | Mixed |
| bad-trips Abuse Memories after the Human section, A1 | paragraph | 2 of 6 | Mixed |
| bad-trips Abuse Memories after the Human section, A2 | paragraph | 2 of 6 | AI |
| bad-trips Abuse Memories after the Human section, A3 | paragraph | 2 of 6 | Mixed |
| bad-trips Dealing With Shadow Thoughts as the guide has it, the prose | section | 1 of 2 | Mixed |
| bad-trips Dealing With Shadow Thoughts after the Human section, the prose | section | 1 of 2 | Mixed |
| bad-trips Dealing With Shadow Thoughts after the Human section, T1 | paragraph | 1 of 6 | Mixed |
| bad-trips Dealing With Shadow Thoughts after the Human section, T4 | paragraph | 1 of 6 | Mixed |
| bad-trips Dealing With Shadow Thoughts after the Human section, T5 | paragraph | 2 of 6 | Mixed |
| bad-trips After the Storm as the guide has it | section | 1 of 2 | AI |
| bad-trips After the Storm after the Human section | section | 1 of 2 | Mixed |
| bad-trips After the Storm after the Human section, P1 | paragraph | 2 of 6 | AI |
| bad-trips After the Storm after the Human section, P2 | paragraph | 2 of 6 | Mixed |
| bad-trips After the Storm after the Human section, P3 | paragraph | 2 of 6 | Mixed |
| bad-trips After the Storm after the Human section, P4 | paragraph | 2 of 6 | Mixed |
| bad-trips After the Storm after the Human section, P5 | paragraph | 2 of 6 | Mixed |
| bad-trips After the Storm after the Human section, P6 | paragraph | 1 of 6 | Mixed |
| bad-trips No Rash Actions after the Human section, N2 with a grand purchase | paragraph | 1 of 6 | AI |
| bad-trips (Re)defining "Bad Trip" after the Human section, teaching try T | paragraph | 1 of 6 | Mixed |
| bad-trips After the Storm after the Human section, teaching try T | paragraph | 1 of 6 | AI |
| bad-trips Spiritual ≠, the bypassing and practice pair, his round-22 move | paragraph | 1 of 6 | Mixed |
| bad-trips The Fear/Panic Loop, his round-22 move | paragraph | 2 of 6 | AI |
| bad-trips Demons' hooks, his round-22 move | paragraph | 1 of 6 | Mixed |
| bad-trips For the Person Helping's opening, his round-22 move | paragraph | 2 of 6 | Mixed |
| bad-trips Hand on Heart's touch part, his round-22 move | paragraph | 2 of 6 | Mixed |
| bad-trips When the Trip Feels Amazing's bliss line, his round-22 move | paragraph | 1 of 6 | Mixed |
| bad-trips No Rash Actions, the experience-content paragraph, his round-22 move | paragraph | 1 of 6 | Mixed |
| bad-trips Dealing With Sorrow, the deepest utility, his round-22 move | paragraph | 1 of 6 | Mixed |
| bad-trips After the Storm, no another ceremony, his After the Storm moves | paragraph | 4 of 6 | AI |
| bad-trips Dealing With Shadow Thoughts, during a trip, his After the Storm moves | paragraph | 4 of 6 | AI |
| bad-trips No Rash Actions, the don't list, his After the Storm moves | paragraph | 1 of 6 | AI |
| bad-trips Abuse Memories, don't confront tonight, his After the Storm moves | paragraph | 2 of 6 | Mixed |
| bad-trips Alone at 3 a.m., the movement paragraph, his After the Storm moves | paragraph | 2 of 6 | Mixed |
| bad-trips Stillness or Movement?, the two cases, his After the Storm moves | paragraph | 1 of 6 | Mixed |
| bad-trips Minimum Viable Integration, his After the Storm moves | paragraph | 1 of 6 | Mixed |
| bad-trips No Rash Actions, the don't list, his version (round 23) | paragraph | 1 of 6 | Mixed |
| bad-trips After the Storm, the questions with the facts merged in (MVI cut as a repeat) | paragraph | 2 of 6 | Mixed |
| bad-trips For the Person Helping, its Don't list, his list fix (round 23) | paragraph | 4 of 6 | AI |
| bad-trips Why Bad Trips Tend to Happen, the distortions, his list fix (round 23) | paragraph | 1 of 6 | Mixed |
| bad-trips Give the Session a Beginning and an End, its list, his list fix (round 23) | paragraph | 1 of 6 | AI |
| bad-trips No Rash Actions, his round-23 list ablated: its absurd specifics made generic | paragraph | 1 of 6 | Mixed |
| bad-trips No Rash Actions, his round-23 list ablated: his structure undone | paragraph | 1 of 6 | Mixed |
| bad-trips B366a drug-neutral (his r24 paragraph) | paragraph | 1 of 6 | AI |
| bad-trips What Kind of Aftermath Is This?, his session frame carried | stretch | 2 of 2 | AI |
| bad-trips Aftermath first paragraph (h33) | paragraph | 1 of 6 | AI |
| bad-trips When to Bring In Outside Help / Call medics for: as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Risk of Harm: When Peer Support Isn't Enough as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Who to Contact, and When as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Acute Medical and Neurological Rescue as it stands (h42) | section | 1 of 2 | AI |
| bad-trips If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid First as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Active Seizure (1 of 2) as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Active Seizure (2 of 2) as it stands (h42) | section | 4 of 2 | Mixed |
| bad-trips MDMA: Jaw Tension Is the Magnesium Alarm as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Chest Pain and Injury as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Recent Oral Toxic Ingestion as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Suspected Serotonin Syndrome (SS) as it stands (h42) | section | 1 of 2 | AI |
| bad-trips My Acute Rescue Hierarchy of Remedies as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Some Remedies Require More Caution as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Gut-Toxin and Parasite-Die-Off Tools (1 of 2) as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Gut-Toxin and Parasite-Die-Off Tools (2 of 2) as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Mental Stabilizers That Don't Abort the Trip (2 of 6) as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Mental Stabilizers That Don't Abort the Trip (6 of 6) as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips When the Goal Is to Stop a Psychedelic Trip (1 of 2) as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips When the Goal Is to Stop a Psychedelic Trip (2 of 2) as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Grounding Menu: Choose One or Two Things (1 of 2) as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Get One Human Anchor as it stands (h42) | section | 1 of 2 | AI |
| bad-trips For the Person Helping: Calm Anchor, Not Guru (1 of 2) as it stands (h42) | section | 1 of 2 | AI |
| bad-trips For the Person Helping: Calm Anchor, Not Guru (2 of 2) as it stands (h42) | section | 1 of 2 | AI |
| bad-trips No Rash Actions: Visions Are Not Commands as it stands (h42) | section | 1 of 2 | AI |
| bad-trips When the Trip Feels Amazing: Euphoric Certainty as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Dealing With Sorrow: Missing Versus Sending Love as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Hand on Heart and Gratitude 🫶🏿 as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Demons, Jinn, Entities, and Shadow Forces as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Abuse Memories, Recovered Memories, and Certainty as it stands (h42) | section | 1 of 2 | AI |
| bad-trips Dealing With Shadow Thoughts as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Spiritual ≠ "Getting Your Ass Kicked" as it stands (h42) | section | 1 of 2 | AI |
| bad-trips After the Storm as it stands (h42) | section | 1 of 2 | Mixed |
| bad-trips Niacin's B3 forms and the bridge to tripsitting, fixed (h43) | paragraph | 2 of 6 | Mixed |
| bad-trips Risk of Harm, its first paragraph after round 33 (h43) | paragraph | 2 of 6 | AI |
| bad-trips Dealing With Shadow Thoughts, its during-a-trip lines with the paragraph before, fixed (h43) | paragraph | 1 of 6 | Mixed |
| bad-trips Risk of Harm's 911 and 988 paragraph after round 34 (h44) | paragraph | 1 of 6 | AI |
| bad-trips Recent Oral Toxic Ingestion, its first paragraph, his moves carried (h44) | paragraph | 1 of 6 | AI |
| bad-trips Recent Oral Toxic Ingestion, its charcoal paragraph, his moves carried (h44) | paragraph | 1 of 6 | AI |
| bad-trips Recent Oral Toxic Ingestion, its poison control paragraph, his moves carried (h44) | paragraph | 1 of 6 | AI |
| bad-trips Suspected Serotonin Syndrome's recognition part, his round-35 moves carried (h45) | pair | 2 of 6 | AI |
| bad-trips Acute Medical and Neurological Rescue, its first two paragraphs, his round-35 moves carried (h45) | pair | 2 of 6 | AI |
| bad-trips Chest Pain and Injury's branch paragraph, written against his fixes (h46) | pair | 1 of 6 | AI |
| bad-trips My Brain Feels Damaged's checks, written against his fixes (h46) | pair | 2 of 6 | AI |
| bad-trips My Brain Feels Damaged's evidence paragraph, rounds 37-38 lessons carried (h50) | paragraph | 2 of 6 | AI |
| bad-trips Active Seizure's rescue paragraph (B110) by itself, rounds 37-38 lessons carried (h50) | paragraph | 2 of 6 | Mixed |
| bad-trips Active Seizure's call list with his 22:34 UTC changes, by itself (h51) | paragraph | 4 of 6 | AI |
| bad-trips Suspected Serotonin Syndrome's cyproheptadine step (h55) | paragraph | 2 of 6 | AI |
| bad-trips MDMA's paragraph after his second wife's story (h55) | paragraph | 2 of 6 | AI |
| bad-trips My Brain Feels Damaged's numbered protocol (B144) as the guide has it (h57) | paragraph | 2 of 6 | AI |
| bad-trips Beach Morning Glory's last two paragraphs (B176, his story; B178, the MDMA line, under 50 words) (h57) | pair | 1 of 6 | AI |
| bad-trips (Re)defining "Bad Trip": his paragraph (B330c) and the line after it (B357, under 50 words) (h57) | pair | 2 of 6 | Mixed |
| bad-trips Recognizing serotonin toxicity: the heading, his lead-in and his list (B131 to B133) (h57) | heading | 2 of 6 | Mixed |
| bad-trips Bring in mental-health support when: its heading and list (B96, B97, 38 words), after the last item of his aftermath list (B426) before it (h57) | heading | 1 of 6 | Mixed |
| bad-trips Dealing With Shadow Thoughts' during-a-trip paragraph (B415, after his rewrite of the section) by itself (h58) | paragraph | 3 of 6 | AI |
| bad-trips Who to Contact, and When: B262, B263, B264 (76 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips Who to Contact, and When: B265, B266, B267, B268, B269, B270 (120 words), by itself as the guide has it (h59) | stretch | 1 of 2 | Mixed |
| bad-trips Alone at 3 a.m.: B272, B273, R31-ALONE (83 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips For the Person Helping: Calm Anchor, Not Guru: B82, B83 (76 words), by itself as the guide has it (h59) | pair | 1 of 6 | AI |
| bad-trips When What They Say Turns Toward Harm: B287, B288, B289 (68 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips When What They Say Turns Toward Harm: B291, B293 (94 words), by itself as the guide has it (h59) | pair | 1 of 6 | AI |
| bad-trips No Rash Actions: Visions Are Not Commands: B316, B317, B318 (137 words), by itself as the guide has it (h59) | stretch | 1 of 2 | Mixed |
| bad-trips No Rash Actions: Visions Are Not Commands: B319, B320, B321 (102 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips When the Trip Feels Amazing: Euphoric Certainty: B324, B326, B327 (80 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips Touch, Consent, and Compassion: B391, B392 (62 words), by itself as the guide has it (h59) | pair | 6 of 6 | AI |
| bad-trips Demons, Jinn, Entities, and Shadow Forces: B397, B398, B399 (64 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips Abuse Memories, Recovered Memories, and Certainty: B406, B407, B408, B409 (119 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips Spiritual ≠ "Getting Your Ass Kicked": B335, B336, B337 (61 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips After the Storm: B427, B428, B429, B430 (113 words), by itself as the guide has it (h59) | stretch | 1 of 2 | AI |
| bad-trips Suspected Serotonin Syndrome steps: B136, by itself as the guide has it (h62) | paragraph | 1 of 6 | AI |
| bad-trips Suspected Serotonin Syndrome steps: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | section | 1 of 2 | AI |
| bad-trips Suspected Serotonin Syndrome steps 3 and 4: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | paragraph | 2 of 6 | AI |
| bad-trips Suspected Serotonin Syndrome steps 5 and 6: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | paragraph | 3 of 6 | AI |
| bad-trips Suspected Serotonin Syndrome steps 7 and 8: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | paragraph | 2 of 6 | AI |
| bad-trips Grounding Menu Body, Smell and Breath (B297 to B302), the Smell line naming the stabilizers by its round-47 heading | stretch | 1 of 2 | Mixed |
| bad-trips Suspected Serotonin Syndrome step 1 by itself: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | paragraph | 2 of 6 | Mixed |
| bad-trips Suspected Serotonin Syndrome step 4 by itself: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | paragraph | 2 of 6 | AI |
| bad-trips Suspected Serotonin Syndrome step 5 by itself: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | paragraph | 1 of 6 | AI |
| bad-trips Suspected Serotonin Syndrome step 3 by itself: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | paragraph | 1 of 6 | Mixed |
| bad-trips Suspected Serotonin Syndrome step 7 by itself: B136, "Do this immediately when serotonin toxicity is reasonably suspected:" (h62 c1-ss-steps-1, as it stood) | paragraph | 1 of 6 | AI |
| bad-trips naloxone paragraph, blind rewrite from the lessons (replay h69) | paragraph | 1 of 6 | AI |
| bad-trips MDMA: Magnesium Alarm, the jaw alarm (B114) (h73) | paragraph | 2 of 6 | AI |
| bad-trips MDMA: Magnesium Alarm, his second wife (B118) (h73) | paragraph | 2 of 6 | AI |
| bad-trips MDMA: Magnesium Alarm, the kidneys (B120) (h73) | paragraph | 2 of 6 | AI |
| bad-trips MDMA: Magnesium Alarm, the softer peak (B117) (h73) | paragraph | 2 of 6 | AI |
| bad-trips B114, blind rewrite from his round-55 lessons (replay h74) | paragraph | 1 of 6 | AI |
| bad-trips MDMA: Magnesium Alarm, the kidneys from his post's text with his round-55 ways (h74) | paragraph | 1 of 6 | AI |
| bad-trips MDMA: Magnesium Alarm, the kidneys (B120) as it stands, by itself (h75) | paragraph | 2 of 6 | AI |
| bad-trips MDMA: Magnesium Alarm, the kidneys by a second writer from the tell panel (h75) | paragraph | 1 of 6 | AI |
| bad-trips Swallowed Too Much?, the activated charcoal paragraph (B127) as it stands, by itself (h75) | paragraph | 1 of 6 | AI |
| bad-trips B120, blind rewrite from his round-57 lessons (replay h76) | paragraph | 1 of 6 | AI |
| bad-trips Gut-Toxin & Die-Off Tools, its opening paragraph with the first of ZeoCharge & Ferment (B151, B153) as they stand, together (h78) | paragraph | 1 of 6 | AI |
| bad-trips ZeoCharge & Ferment, ozonating the zeolite and keeping it from metal (B156, B157) as they stand, together (h78) | paragraph | 2 of 6 | Mixed |

