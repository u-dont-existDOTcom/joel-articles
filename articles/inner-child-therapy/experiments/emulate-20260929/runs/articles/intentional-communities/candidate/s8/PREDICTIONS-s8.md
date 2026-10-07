# Section 8 ("The Grown Children Get the Final Review"): predictions and Pangram results

Written before each call. Times come from the History page of Joel's Pangram account (GMT), or from the laptop's API logs.

The published section: 28 paragraphs under one h1, three h2s and an h3 (1,355 words in the markdown), two images with captions (Joel's: "Me as a child, wearing the pen holder my dad made, ready to write my Final Review 😹"; "African kids enjoying their childhood!"), and an embedded video (the page shows "Double click to interact with video", left out of every check as page furniture). Facts and figures to keep exactly: nursed until five, not vaccinated, the friend's "a treasure and a burden", Liedloff and the Ye'kuana, the kibbutz study, Tamera's Children's Place, ZEGG's Kinderhaus, the 1984 Island Pond raid and its 112 children, "roughly 85 percent or more", the research corpus search.

Baseline (written 01:50 UTC, before the calls): the published text by subsection in the web app, and the whole section on the API as a probe of whether the key has credits again (it returned HTTP 402 on 10-06 at 21:10):

| text | mine | why | Pangram |
|---|---|---|---|
| pub-S8a (opening to "That sentence…", 239 words), web app | Mixed | Joel's caption and his son's video joke beside the drafted paragraphs | Mixed (52% AI): P2's second sentence to P3's end (73 words) and P5's second sentence to P6 (44); P1, the caption, P4 (his video joke) and P5's first sentence read Human |
| pub-S8b (the mother and the village, 213), web app | AI | | AI (card) |
| pub-S8c (freedom inside protection, 501), web app | AI | the five-part protection list | AI (card) |
| pub-S8d (the door at adulthood, 318), web app | AI | | AI (card) |
| pub-S8e (child-rearing values, 68), web app | AI | | AI (card) |
| pub-S8 (the whole section, 1339), web app | AI (mostly) | | AI (97%, 1,374 words scanned): two AI windows, the heading to P3 (152) and P5's second sentence to the end (1,144) |
| pub-S8 on the API | refused (402) | out of credits on 10-06 | refused (HTTP 402, insufficient credits) |

Baseline (web app 01:52 UTC, all six checks at 1:52 AM on the History page; API probe 01:51:13 UTC, from api94.log's file time): mine 7 of 7. Only Joel's lines and their neighbors read Human: P1 (in the subsection run, not in the whole section), the caption, P4 ("I actually learned how to parent my son from his future review via his quantum jumping time machine…") and P5's first sentence. The API key is still out of credits.

Plan, from section 7's lessons: write a faithful plain version first (m1: each published sentence, same claims and connectives, lists kept or split, no additions), feed m1 to Emulate (faithful input), splice Emulate's sentences with word fixes, check paragraphs and then subsections and the section in the web app, run the gate, fix one thing at a time on a passing text. No "and … and … and" lists (Joel, 10-07: Emulate's trick, and not needed). Joel's lines stay as he wrote them: the caption, P4, the friend's quoted words.

Emulate (started 01:59:56 UTC on the laptop): community-s8a gets the published text, community-s8b gets m1 (mine-m1.json, corrected at 01:58 after my own read: kept "review" in P3, kept the list in P17 instead of "anything", kept "or" in P25 and P18's lists, no added "But" in P2, P25's last sentence read as "It's to not turn belonging into a trap", which is a question for Joel). Both sets use the same 14 units (emu-groups.json): P2+P3, P5+P6, P7+P8, P9+P10, P11+P12, P13+P14, P15–P17, P18+P19, P20, P21, P22+P23, P24, P25, P26–P28. Input hashes match the laptop copies (a 4c3a47f76011, b ecf219fa3c5e).

## Draft v1 (`drafts-v1.json`, file time 02:16:44 UTC)

Spliced from the four Emulate rounds (a published, b and c faithful pairs, d faithful single paragraphs; `emu/s8-emu-all.json`, `emu/s8cd-emu-all.json`), with word-level fixes back to the published meaning. Joel's lines untouched: P1 (published, read Human in the baseline), the caption, P4, the second caption. P15 ("The protection has several parts:") untouched. Links and their URLs kept; anchor words follow the new wording. P25's last sentence reads the published double negative as "It's to keep belonging from turning into a trap" (a question for Joel). Lint (`tells_lint.py`, with O11 to O13): FAIL on two lists of three in P21 and P25 (both the published lists), REVIEW on "kids" for "children" (Emulate's register throughout), E23 on P20 and P23, O9 on P10 and P26 (both the published "rather than"), O6 on P14's fear sentence (the published "Fear can destroy that gift").

The gate's agents (three traces, two logic audits, the cold read, the stance check; `review-d1/`) run at the same time as batch 95g.

Batch 95g (written 02:19 UTC by `date -u`, before the call; the web app, paragraphs alone, or with a neighbor when under 50 words):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 95g-P2P3 (88 words) | AI | P3 is mostly the published wording, and P2's second sentence is mine | AI (100%) |
| 95g-P5P6 (71) | Human | P5's first sentence read Human in the baseline; the rest is round c's sample with one word fixed | **Human (100%)** |
| 95g-P7 (57) | Human (weak) | round c's sentence structure, my "handle" and "a lot of the fathering" | **Human (100%)** |
| 95g-P8 (100) | AI | long, and much of it is my rewording of round d's sample | **Human (100%)** |
| 95g-P9P10 (110) | AI | P9 is close to the published sentences | AI (100%) |

Batch 95g (submitted about 02:20 UTC, read 02:41; times to fill from the History page): mine 4 of 5 (P8 read Human where I said AI).

## The gate on draft v1 (`review-d1/`, agents launched about 02:20 UTC; reports written 02:27 to 02:40 by file time)

Three traces (P2 to P10, P11 to P19, P20 to P28), two logic audits (forward and backward), the cold read and the stance check. **Stance: 4 conflicts**: P2 ("trying to create a village" implies he is founding one; the essay says he isn't; and the general rule, communities need agreement on children's health before parents can trust one another, had become a description of his own village), P23 ("if they were free to leave" implies children who stay aren't free), P14 ("act on any kind of problem" cuts against children settling ordinary disputes themselves). Every finding below is fixed in draft v2, mostly by going back toward the published words:
- P2: "create" → "design"; the general claim back ("a certain amount of agreement on children's health is necessary before parents can actually trust one another"); "a deciding factor" → "one of the values that would decide". The cold read: "belongs here" is addressed to an editor ("here where, and why tell me?"), so the opener says why vaccination comes up: "I bring up vaccination because…".
- P5: "she knew she belonged" (adds what she was aware of) → "she belonged"; "she was expected to live" (others' expectation, not the life she lived) → "because of the strict religious life she had no say in".
- P6: "That's more useful" (could be only the burden sentence) → "What she said is more useful".
- P7: "I'm in the camp that says" → "My view is that"; the shared-care community back as the setting (no "but"), "so it isn't all on them" out; "to 'liberate' the moms" → "in the name of liberating her", one child and one mother as published.
- P8: "an outsider's view" → "one outsider's interpretation"; "idealizing them" → "idealizing what she saw"; "She notes that they carry their babies with them wherever they go" (her report as fact, and "wherever they go" new) → "In her account, babies are carried along in ordinary adult life"; "no one exhausted parent" (read as "nobody exhausted") → "a single exhausted parent"; "recreate" → "imitate".
- P10: "That being said" (made P10 a step back from P9's caution) out; "a direct look" → "to be studied directly, not caricatured".
- P12: "construct their own world" → "still get a world of their own"; "a taste of that … one of the freest memories I have" back.
- P13: "without the adults noticing" (domination adults see would pass) → the published "quietly", which is the exact word here.
- P14: "says kids shouldn't have" → "treats any warm relationship … as suspect"; "notice and act on any kind of problem" → "notice when something changes, and … act when something's wrong"; "won't stop the bad things" (a flat claim, and "abuse" gone) → "That kind of fear can destroy the gift without actually preventing abuse".
- P16: "time alone with them" (narrower) → "private access to them"; "what legitimate safety needs" (misread) → "requires".
- P17: "Surprises are different, because there's a time when the surprise will be revealed" (a rule turned into an exemption) → "A surprise needs an end date."
- P18: "will be taken seriously" → "adults will listen seriously".
- P19: "loved by others in the community" → "someone people love"; "many communities" → "communities"; "know what you're going to do" → "Decide on the process for responding ahead of time"; "put the child in immediate safety" → "make sure everyone is safe right away"; "hide behind their status in the community" → "nothing gets hushed up because of anybody's status".
- P20: "raided Island Pond" (the town) → "seized 112 children in the Island Pond raid"; "friends from down the street" (could live inside) → "local friends"; the route "they can reach without going through the community's leadership"; "Trying to enclose children…can also fail" (could mean the attempt fails) → "A community that closes itself off completely can also fail".
- P21: "the records", "the cases" (presuppose cases exist) → "records", "cases"; "continued to be" → "remained".
- P23: "If all the children stay … if they were free to leave" → "If a community's children never leave, how can it know whether they'd freely come back?"; the list back in one sentence, so "without being treated as traitors" covers every item.
- P24: "aren't just going to give" → "aren't going to give"; "going to actually work" → "can actually work".
- P25: "some education" → "know enough … that they aren't helpless"; the topics back (jobs, rent, contracts, banking, scams, ID, getting around, how to ask for help); "can at least not punish …, or withhold" (could parse as allowed to withhold) → "can at least avoid punishing … or withholding"; "people" → "a young adult"; "keep belonging from turning into a trap" → "not turn belonging into a trap" (the community as the one who would turn it; Joel's question stands).
- P26: "leave and stay away" → "leave for good", and the two cases back in one sentence so "that" covers both.
- P28: "isn't enough to answer" → "doesn't answer".
Kept, with reasons: the cold read's "the Ye'kuana are never identified" and "Tamera's Children's Place is never described" (the published text doesn't either, and adding facts is not mine to do); "the research corpus" (a link to his research page); the headings read as body text (the cold-read prompt strips heading marks); P4's "actually" (his joke); P22's "Popular culture has blown Rumspringa out of proportion" for "the popular caricature … is exaggerated" (one trace marked the attribution; the logic audits didn't, and it's the same claim).

Emulate round e (started 02:43:43 UTC on the laptop, `community-s8e`): the faithful wording of v2, twelve units, for sentences to splice where v2 reads AI.

Batch 96g (written 02:44 UTC by `date -u`, before the call; draft v2):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 96g-P5P6 (68) | Human | the 95g pair with three word fixes | **Human (100%)** |
| 96g-P7 (51) | Human (weak) | the 95g paragraph with its end back in the published words | **Human (100%)** |
| 96g-P8 (94) | Human (weak) | the 95g paragraph with five fixes, three toward the published words | AI (100%) |
| 96g-P11P12 (76) | Human (weak) | round c's samples with fixes | **Human (100%)** |
| 96g-P13P14 (114) | AI | P13 is mostly mine | AI (100%) |

Batch 96g (submitted 02:45:21 UTC by the browser's clock, read 02:46): mine 4 of 5 (P8 read AI where I said Human). P8 passed at v1 and the gate's five fixes tipped it together; section 7's method: one fix at a time on the passing paragraph.

Batch 97g (written 02:46 UTC by `date -u`, before the call): P8 of v1 with the fixes one group at a time (a: "In her account, they carry their babies with them and bring them into daily adult life", the "wherever they go" fix reworded from v2's; b: "one outsider's interpretation … idealizing what she saw"; c: "a single exhausted parent isn't expected", "imitate"; d: all three), and P15 to P17 of v2.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 97g-P8a (97) | Human (weak) | one sentence changed, round d's verbs kept | Mixed (66% AI): "Still, it's a powerful picture. In her account…" to the end (64 words) |
| 97g-P8b (102) | Human (weak) | two phrases back to the published words | Mixed (41% AI): the opening to "…it's a powerful picture." (41 words) |
| 97g-P8c (100) | Human | two small word changes | AI Assisted (100%) |
| 97g-P8d (99) | AI | close to v2, which read AI | AI (100%) |
| 97g-P15P16P17 (81) | AI | rule-list style, mostly the published sentences | AI (100%) |

Batch 97g (submitted 02:47:06 UTC by the browser's clock, read 02:48): mine 2 of 5. Each group of P8 fixes tips the paragraph that passed at v1, each in its own window. So P8 keeps v1's words where a finding is minor and the v1 words say the same thing (kept findings, with reasons: "an outsider's view" and "one outsider's interpretation" both mark the account as one person's reading; "idealizing them" and "idealizing what she saw" are the same here, since what she saw was the Ye'kuana), and the two real fixes get new wordings, one at a time (batch 100g).

Emulate round e is in (`emu/s8e-emu-all.json`, sha 23fa646fe8b8).

Batch 98g (written 02:49 UTC by `date -u`, before the call; draft v2):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 98g-P18 (61) | AI | mostly my wording on the published structure | AI (100%) |
| 98g-P19 (74) | AI | the same | AI (100%) |
| 98g-P20 (97) | AI | close to the published sentences | Mixed (45% AI): "In 1984, Vermont authorities…" to the end (45 words); the first three sentences Human |
| 98g-P21 (104) | AI | close to the published sentences | AI (100%) |
| 98g-P22P23 (92) | AI | P23 is mine | AI (100%) |

Batch 98g (submitted 02:50:05 UTC by the browser's clock; an earlier submit at 02:49 failed in the pane with "Policy check temporarily unavailable" and sent nothing; read 02:51): mine 4 of 5 (P20 read Mixed, not AI).

The v3 candidates (`cands-v3.json`), from round e's samples with the gate's fixes kept: P2 and P3 (round e u1), P9 and P10 (u2), P13 and P14 (u4), P16 and P17 (u5), P18 and P19 (u6), P20's second half (u7), P21 (u8), P22 (u9). P23 is mine. P8's two real fixes, one at a time on v1 (e: "She writes that they carry their babies with them and bring them into daily adult life"; f: "no single exhausted parent"; g: "mimic"; h: all three). Emulate round f (started 02:52:23 UTC, `community-s8f`, sha baef3c18480c): the faithful wording of the v3 candidates, and of v2 where unchecked, for more sentences.

Batch 99g (written 02:52 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 99g-P24 (63) | AI | my wording on m1, two phrases from round a | **Human (100%)** |
| 99g-P25 (157) | AI | long, list-heavy, close to the published sentences | AI (100%) |
| 99g-P25P26 (194) | AI | the same | AI (100%) |
| 99g-P27P28 (67) | AI | close to the published sentences | AI (100%) |
| 99g-P2P3 (v3, 93) | Human (weak) | round e's sentences, word fixes | AI (100%) |

Batch 99g (submitted 02:53:36 UTC by the browser's clock, read 02:54): mine 3 of 5 (P24 read Human where I said AI; P2 with P3 read AI again where I said Human).

Batch 100g (written 02:54 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 100g-P8e (97) | Human (weak) | v1 with "She writes that" and without "wherever they go" | **Human (100%)** |
| 100g-P8f (100) | Human | v1 with "no single" | Mixed (42% AI): "Children are around people of several ages…" to the end (43 words) |
| 100g-P8g (100) | Human | v1 with "mimic" | **Human (100%)** |
| 100g-P8h (97) | Human (weak) | all three | Mixed (43% AI): the same last two sentences |
| 100g-P9P10 (v3, 109) | Human (weak) | round e's sentences | **Human (100%)** |

Batch 100g (submitted 02:54:46 UTC by the browser's clock, read 02:55): mine 3 of 5. P8: "She writes that … " passes, "mimic" passes, "no single" tips the last two sentences, alone or with the others. The "no one" fix needs another wording (batch 102g).

Batch 101g (written 02:55 UTC by `date -u`, before the call; v3 candidates):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 101g-P13P14 (113) | Human (weak) | round e u4's sentences | AI (100%) |
| 101g-P15P16P17 (94) | AI | rule-list style, though the sentences are round e's | AI (100%) |
| 101g-P18 (67) | AI | more mine than round e's | AI (100%) |
| 101g-P19 (67) | Human (weak) | round e u6's sentences | **Human (100%)** |
| 101g-P20 (98) | Human (weak) | the first half passed in 98g; the second half is round e u7's | Mixed (44% AI): "In 1984…" to the end again (46 words) |

Batch 101g (submitted 02:55:56 UTC by the browser's clock, read 02:57): mine 3 of 5.

Emulate round f is in (`emu/s8f-emu-all.json`, sha d7c5062f24a6). The v4 candidates (`cands-v4.json`) take whole sentences from rounds a to f that already say the published thing, with single words changed, which is what worked in section 7: P2 (round f u2 B), P3 (round e u1 A), P13 (round b u6 B), P14 (round e u4 B and round c u6 B), P15 to P17 (round f u5 B and round e u5 B), P18 (round e u6 A), P20's second half (round c u9 A), P25 (round d u11 B), P26 to P28 (rounds e and f u12). P8i and P8j: v1 with the two fixes that passed (e and g), and j also with "one exhausted parent isn't expected" for "no one exhausted parent is expected".

Batch 102g (written 02:59 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 102g-P2 (v4, alone, 61) | Human (weak) | round f's sentences with three word fixes | **Human (100%)** |
| 102g-P2P3 (v4, 103) | Human (weak) | P3 from round e | **Human (100%)** |
| 102g-P8i (97) | Human | two fixes that each passed alone | Mixed (43% AI): the last two sentences |
| 102g-P8j (96) | Human (weak) | the same, and the published "one exhausted parent isn't expected" | AI Assisted (100%) |
| 102g-P21 (v3, 110) | AI | close to the published sentences | AI (100%) |

Batch 102g (submitted 03:00:10 UTC by the browser's clock, read 03:01): mine 3 of 5. P2 and P3 pass (v4). P8's two passing fixes don't combine (as in section 7's batch 88g): P8e ("She writes that…", the meaning fix) stays, and "recreate" and "no one exhausted parent" get other wordings.

Batch 103g (written 03:01 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 103g-P13P14 (v4, 116) | Human (weak) | round b's and e's sentences, word fixes | Mixed (42% AI): P13 (48 words) AI, P14 Human |
| 103g-P15P16P17 (v4, 96) | AI | rule lists still | AI (100%) |
| 103g-P18 (v4, 58) | Human (weak) | round e's sentences | AI (100%) |
| 103g-P20 (v4, 99) | Human (weak) | round c's sentence for the raid | Mixed (46% AI): from "As the 1984 Island Pond raid showed…" to the end (47 words) |
| 103g-P22P23 (v3, 95) | AI | P23 is mine | AI (100%) |

Batch 103g (submitted 03:01:27 UTC by the browser's clock, read 03:02): mine 2 of 5. P14 (v4) reads Human inside its pair; P13, P15 to P18, P20's second half and P22 with P23 keep reading AI. Emulate rounds g1 and g2 (started 03:03:06 UTC, `community-s8g1`, `community-s8g2`, the same inputs, sha 280bcc628682): the gate-fixed wording of those paragraphs, for four samples each.

Batch 104g (written 03:03 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 104g-P25 (v4, 180) | AI | round d's structure, many of my word fixes, three lists | AI (100%) |
| 104g-P25P26 (v4, 220) | AI | the same | AI (100%) |
| 104g-P27P28 (v4, 76) | Human (weak) | round f and e sentences | AI (100%) |
| 104g-P8k (97) | Human (weak) | P8e with "copy" for "recreate" | Mixed (43% AI): the last two sentences |
| 104g-P8l (97) | Human (weak) | P8e with the published "imitate" | Mixed (43% AI): the last two sentences |

Batch 104g (submitted 03:03:52 UTC by the browser's clock, read 03:04): mine 2 of 5. With "She writes that…" in, every other word for "recreate" tips P8's last two sentences: "mimic" (102g), "copy" and "imitate" (104g), three tries. Unless P8m passes, P8 is P8e, and "recreate" and "no one exhausted parent" go to Joel as kept findings with the tries counted.

Emulate rounds g1 and g2 are in (`emu/s8g-emu-all.json`, sha 7c5698384c20). The v6 candidates (`cands-v6.json`): P13 (round g u1 B's "explicit because … misunderstood otherwise", the list as three plain clauses), P16 and P17 (round g u2: "A surprise isn't a secret, because at the end of a certain date it has to be told"), P18 (round g u1 A's "don't … don't … and don't brush it off … they may still need protection"), P20 (round g u4 B's raid sentence), P21 (round g u5 B), P23 (round g u6 A's three "Let them" sentences), P26 to P28 (round g u8 A and B). P25 split in two paragraphs (a and b) to see whether each half can pass; the split is a structure change and would go to Joel as a proposal.

Batch 105g (written 03:07 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 105g-P8m (95) | Human (weak) | P8e with the parent clause turned around | AI Assisted (100%) |
| 105g-P13P14 (v6 with v4, 109) | Human (weak) | P14 read Human in 103g | Mixed (41% AI): P13 (41 words) AI |
| 105g-P15P16P17 (v6, 101) | AI | the rule list again | AI (100%) |
| 105g-P17 (v6, alone, 64) | Human (weak) | round g's sentences | **Human (100%)** |
| 105g-P18 (v6, 61) | Human (weak) | round g's sentences | **Human (100%)** |

Batch 106g (written 03:07 UTC, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 106g-P20 (v6, 103) | Human (weak) | round g's raid sentence | **Human (100%)** |
| 106g-P21 (v6, 116) | Human (weak) | round g's sentences | AI (100%) |
| 106g-P22P23 (v3 with v6, 99) | AI | P22 read AI with P23 before | AI (100%) |
| 106g-P25a (61) | AI | a list | **Human (100%)** |
| 106g-P25b (106) | AI | lists | AI (100%) |

Batch 105g (submitted 03:08:13 UTC by the browser's clock, read 03:08): mine 3 of 5. Batch 106g (submitted 03:08:58, read 03:09): mine 3 of 5. P17, P18 and P20 pass; P8m doesn't, so P8 is P8e (kept: "recreate", three other words tried; "no one exhausted parent", three other wordings tried). P25's first half passes as its own paragraph.

Batch 107g (written 03:10 UTC by `date -u`, before the call; the v7 candidates are in `cands-v7.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 107g-S8e (H4 with P27, P28 v6, 86) | Human (weak) | round g's sentences | AI (100%) |
| 107g-P13aP14 (112) | Human (weak) | P13 without a three-item list | **Human (100%)** |
| 107g-P13bP14 (107) | AI | three "can't" clauses | **Human (100%)** |
| 107g-P15P16P17 (v7 P15, P16, v6 P17, 103) | AI | the opener and the rule again | **Human (100%)** |
| 107g-P14 (v4, alone, 68) | Human | read Human inside two pairs | **Human (100%)** |

Batch 108g (written 03:10 UTC, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 108g-P21 (v7, 118) | AI | the stages as a range instead of a list | AI (100%) |
| 108g-P22 (v7, alone, 67) | Human (weak) | round g's sentences | **Human (100%)** |
| 108g-P22P23 (v7 with v6, 107) | Human (weak) | the same | AI (100%) |
| 108g-P25b (v7, 102) | AI | lists | AI (100%) |
| 108g-P25bP26 (v7 with v6, 144) | AI | the same | AI (100%) |

Batch 107g (submitted 03:11:13 UTC by the browser's clock, read 03:11): mine 2 of 5. Batch 108g (submitted 03:11:58, read 03:12): mine 4 of 5. P13 (both v7 wordings), P14, P15 to P17 and P22 pass. But v7's P16 brought back "time alone with them", which the d1 audits had marked narrower than "private access" (it leaves out private messages and the like), so P16 goes back to "private access to them" and is checked again (109g).

P21 has read AI in five wordings, all with the five-stage list (conduct, assessment, intervention, review, what happened later). P25's second half has read AI in every wording with its three lists. Both are what Joel called "overcompleting" in section 6. Batch 109g checks one version of each without the lists (P21: "the whole sequence is on record, from what the child did to what happened later"; P25: "skills they can take with them, people outside, their own records, and somewhere to go next", and "help with the move"); these are cuts, so they go to Joel as proposals beside the full versions, not into the candidate.

Batch 109g (written 03:13 UTC by `date -u`, before the call; `cands-v8.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 109g-P15P16P17 (v8 P16, 103) | Human (weak) | one phrase changed in a passing triple | **Human (100%)** |
| 109g-P22P23 (v7 with v8, 109) | Human (weak) | P23 rebuilt from round g, "for it" covering every item | **Human (100%)** |
| 109g-P21 (v8, a proposal, 110) | Human (weak) | the stage list compressed | AI (100%) |
| 109g-P25 (v8, a proposal, 121) | Human (weak) | P25a with the lists cut | AI (100%) |
| 109g-P27P28 (v8, 76) | Human (weak) | round g's "however sincere" and "without being so rigid" | AI (100%) |

Batch 109g (submitted 03:14:09 UTC by the browser's clock, read 03:14): mine 2 of 5. P15 to P17 pass with "private access to them", and P22 with P23 passes. P21 reads AI even with the stage list compressed, so the list isn't the whole reason; P25 with its second half cut short still reads AI.

Batch 110g (written 03:15 UTC by `date -u`, before the call; `cands-v9.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 110g-P25bs (the short second half alone, a proposal, 60) | AI | it read AI inside P25 | AI (100%) |
| 110g-P21 (v9, 106) | AI | round f's "I failed to find one", the same structure | AI (100%) |
| 110g-P27P28 (v9, 80) | Human (weak) | round g's question form for P27 | AI (100%) |
| 110g-S8e (the published H4 with v9, 89) | Human (weak) | the same | AI (100%) |
| 110g-S8e-newH4 (92) | Human (weak) | the heading reworded with the same promise | AI (100%) |

Batch 110g (submitted 03:15:51 UTC by the browser's clock, read 03:16): mine 2 of 5. Every P27 with P28 so far keeps P28's balanced close ("enough shared principles … to offer coherence, plus enough room for parents to remain parents"), the polished "enough … enough" pair the linter's O7 is for; v10 breaks the balance into two sentences. P21 v10 says the result of the search instead of narrating it ("My research for this article turned up no well-documented case…"), the research-process gate's default, keeping the link and the five stages.

Batch 111g (written 03:16 UTC by `date -u`, before the call; `cands-v10.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 111g-P21 (v10, 92) | AI | the same claims in the same order | AI (100%) |
| 111g-P25b (v10, alone, 110) | AI | lists | AI (100%) |
| 111g-P25 (P25a with v10 P25b, 171) | AI | the same | AI (100%) |
| 111g-P27P28 (v10, 72) | Human (weak) | the polished pair broken up | AI (100%) |
| 111g-S8e (v10 under the published H4, 81) | Human (weak) | the same | AI (100%) |

Batch 111g (submitted 03:17:31 UTC by the browser's clock, read 03:18): mine 3 of 5. P21 (eight wordings now), P25's second half (six) and P27 with P28 (six) still read AI. Emulate round h (`community-s8h1`, `community-s8h2`, the v10 wording of those three units and of P26 with P27 and P28) for four more samples each.

Batch 112g (written 03:19 UTC by `date -u`, before the call; `cands-v11.json`, raw samples with the fewest fixes: P21 from round g u5 B, P25's second half from round d u11 B, P27 from round a u14 A, P28 from rounds c and g):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 112g-P21 (v11, 103) | AI | the same claims | Mixed (35% AI): only the last two sentences (39 words) |
| 112g-P25b (v11, alone, 110) | AI | lists | AI (100%) |
| 112g-P25 (P25a with v11, 171) | AI | the same | AI (100%) |
| 112g-P27P28 (v11, 79) | Human (weak) | round a's "two people and two childhoods, not twenty and twenty" | AI (100%) |
| 112g-S8e (v11 under the published H4, 88) | Human (weak) | the same | AI (100%) |

Batch 112g (submitted 03:19:48 UTC by the browser's clock, read 03:20): mine 2 of 5. P21's first three sentences (round g's) now read Human; only the last two don't. Emulate round h is in (`emu/s8h-emu-all.json`, sha 694cb3f3eeed).

Batch 113g (written 03:21 UTC by `date -u`, before the call; `cands-v12.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 113g-P21a (108) | Human (weak) | v11's passing start, round g u5 B's "In the hardest cases" | **Human (100%)** |
| 113g-P21b (111) | Human (weak) | v11's passing start, round h u1 B's "I think it's essential" | AI (100%) |
| 113g-P25b (v12, alone, 124) | AI | round h u2 A, lists | **Human (100%)** |
| 113g-P27P28 (v12, 78) | Human (weak) | round h's "And that's just two people. Now think of twenty adults" | AI (100%) |
| 113g-S8e (v12 under the published H4, 87) | Human (weak) | the same | AI (100%) |

Batch 113g (submitted 03:22:15 UTC by the browser's clock, read 03:23): mine 1 of 5. P21 passes (v12 a: v11's start with "Either way, I can't claim communities already know how to handle the hardest cases on their own. In those cases, the child, the family, and the potential victims all need access to competent help and review, outside the control of the home community."), and so does P25's second half (round h u2 A with fixes). P27 with P28 has read AI in eight wordings.

Batch 114g (written 03:23 UTC by `date -u`, before the call; `cands-v13.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 114g-P25 (P25a with P25b v12, one paragraph, 185) | Human (weak) | each half passed alone | AI (100%) |
| 114g-P25P26 (227) | Human (weak) | the same, with P26 | AI (100%) |
| 114g-P27P28 (v13, 94) | Human (weak) | round h u3 A's "still end up with very different opinions", round h u3 B's "it takes more than…" | AI (100%) |
| 114g-S8e (v13 under the published H4, 103) | Human (weak) | the same | AI (100%) |
| 114g-P27v12P28v13 (86) | Human (weak) | to tell which paragraph carries the AI reading | AI (100%) |

Batch 114g (submitted 03:23:47 UTC by the browser's clock, read 03:24): mine 0 of 5. P25's two halves pass alone and read 100% AI as one paragraph (the non-additivity section 7 found). So the candidate keeps P25 as two paragraphs, a structure change that goes to Joel as a proposal (merged, it reads AI). P27 with P28: ten wordings, all AI. To find which paragraph carries it, batch 115g puts each beside P24, which passes alone (diagnostic checks, not article text).

Batch 115g (written 03:24 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 115g-D1-P24P27 (v13 P27, 107) | Mixed | P27's list | **Human (100%)** |
| 115g-D2-P24P28 (v13 P28, 113) | Mixed | P28's close | Mixed (45% AI): P28, the whole of it (51 words) |
| 115g-D3-P24P26 (c6 P26, 105) | Human (weak) | round g's sentences | **Human (100%)** |
| 115g-P25bP26 (v12 with c6, 166) | Human (weak) | P25b passed alone | **Human (100%)** |

Batch 115g (submitted 03:24:58 UTC by the browser's clock, read 03:25): mine 3 of 4. P28 carries the AI reading (P27 v13 reads Human beside P24), and P26 passes beside P25's second half.

Batch 116g (written 03:25 UTC by `date -u`, before the call; `cands-v14.json`, three P28s with the balanced close broken up):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 116g-P27P28a (82) | Human (weak) | "So … to hang together. Parents still need room to be parents, though." | AI (100%) |
| 116g-P27P28c (91) | Human (weak) | round h u3 A's "well, at least everyone means well" | AI (100%) |
| 116g-P27P28d (80) | Human (weak) | the plainest | AI (100%) |
| 116g-S8e-c (100) | Human (weak) | c under the heading | AI (100%) |
| 116g-S8e-d (89) | Human (weak) | d under the heading | AI (100%) |

Batch 116g (submitted 03:26:19 UTC by the browser's clock, read 03:27): mine 0 of 5. Every P28 so far ends on the published "room for parents to remain parents" in some form ("parents still need room to be parents", "people can't be parents", "parents to parent"): the repeated word is the polished touch. v15 says what remaining parents means instead ("make their own calls about their own kids", "room to decide things for their own kids").

Batch 117g (written 03:27 UTC by `date -u`, before the call; `cands-v15.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 117g-P27P28e (86) | Human (weak) | no "parents … parents" | AI (100%) |
| 117g-P27P28f (83) | Human (weak) | the same | AI (100%) |
| 117g-D-P24P28e (diagnostic, 105) | Human (weak) | P28 beside a passing paragraph | AI (100%), P24 included |
| 117g-D-P24P28f (diagnostic, 102) | Human (weak) | the same | **Human (100%)** |

Batch 117g (submitted 03:27:37 UTC by the browser's clock, read 03:28): mine 1 of 4. P28f passes beside P24 and P27 v13 passes beside P24, but the two together read AI: the non-additivity again. Batch 118g tries P28f with the earlier P27s.

Batch 118g (written 03:28 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 118g-P27v12P28f (75) | Human (weak) | "And that's just two people. Now think of twenty adults" | AI (100%) |
| 118g-P27v11P28f (80) | Human (weak) | "not twenty and twenty" | AI (100%) |
| 118g-P27v10P28f (71) | Human (weak) | "Multiply that by twenty adults, each with their own childhood." | AI (100%) |
| 118g-P27c6P28f (80) | Human (weak) | round g's "split apart over disagreements on" | AI (100%) |
| 118g-P27c4P28f (78) | Human (weak) | round f's "different experiences of how they were brought up" | AI (100%) |

Batch 118g (submitted 03:28:36 UTC by the browser's clock, read 03:29): mine 0 of 5. P27 and P28 pass beside other paragraphs and read AI together in every pairing (twenty tries). The candidate so far is `cand-current.json` (P25 in two paragraphs; P27 v13 and P28f as placeholders). Batch 119g checks the first four subsections as they stand, and one proposal for P27 with P28: P28 without its first sentence ("Goodwill doesn't answer those questions once a kid is already living inside the disagreement."), which restates the subheading; that would be a cut, so it goes to Joel.

Batch 119g (written 03:29 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 119g-S8a (270) | Human (weak) | each paragraph passed alone or with its neighbor | **Human (100%)**, 276 words scanned |
| 119g-S8b (269) | Human (weak) | the same | AI (100%), 281 words scanned |
| 119g-S8c (641) | Mixed | the same, but a long run, and section 7's parts didn't add up | **Human (100%)**, 673 words scanned |
| 119g-S8d (406) | Human (weak) | the same | AI (92%): from P22's second sentence ("Pop culture makes Rumspringa…") to the end, 370 words |
| 119g-P27P28s2 (a proposal, 69) | Human (weak) | the restated heading cut | **Human (100%)** |

Batch 119g (submitted 03:30:34 UTC by the browser's clock, read 03:31): mine 2 of 5. S8a and S8c pass as subsections; S8b and S8d don't, though every paragraph in them passes alone or with its neighbor. P27 with P28 passes when P28 drops its first sentence (the proposal).

Batch 120g (written 03:31 UTC by `date -u`, before the call): diagnostics for S8b (without its heading, and with the heading reworded: "The Mother Comes First, and the Village Is Real. One Doesn't Replace the Other.") and S8d (built up from the top), and the proposal under its heading.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 120g-S8b-noH (257) | Human (weak) | the tricolon heading may be what tips it | Mixed (54% AI): P7 with P8 (148 words) AI, P9 and P10 Human |
| 120g-S8b-H1c (271) | Human (weak) | the same | Mixed (72% AI): P7's second sentence to P8's end (130 words) and P9's last sentence to P10's end (71) AI |
| 120g-D-S8d-1 (H3, P22, P23, 116) | Human (weak) | P22 with P23 passed | **Human (100%)** |
| 120g-D-S8d-2 (with P24, 179) | Human (weak) | P24 passed alone | **Human (100%)** |
| 120g-S8e-prop (H4, P27, P28's second sentence, 78) | Human (weak) | the pair passed | **Human (100%)** |

Batch 120g (submitted 03:32:11 UTC by the browser's clock, read 03:33): mine 3 of 5. In S8b the heading isn't the cause: without it, P7 with P8 reads AI (each passes alone). S8d passes from its heading through P24. The proposal for S8e passes under the published heading.

Batch 121g (written 03:33 UTC by `date -u`, before the call):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 121g-S8b-P8v1 (diagnostic, v1's P8, 272) | Mixed | does the "She writes" fix tip the pair? | AI (84%): the heading to P8's end (163 words) and P9's last sentence to P10's end (71) |
| 121g-S8b-P8g (v1's P8 with "mimic", 272) | Mixed | the same question | AI (84%): the same two windows |
| 121g-D-S8d-3 (to P25a, 240) | Human (weak) | P25a passed alone | Mixed (41% AI): P22's second sentence to P23's first (55 words), P24's last sentence to P25a's second (41) |
| 121g-D-S8d-4 (to P25b, 364) | Mixed | P25's halves read AI together | AI (91%): P22's second sentence to the end (328 words) |
| 121g-D-S8d-5 (P24 to P26, 290) | Mixed | the same | AI (100%) |

Batch 121g (submitted 03:33:49 UTC by the browser's clock, read 03:35): mine 2 of 5. S8b reads AI with v1's P8 too, so the gate's P8 fix isn't what tips it; P7 with P8, and P9's end with P10, read AI together though each passes alone. S8d tips once P25a joins (and the windows move up into P22 and P23, as in section 7's batch 64).

Sent Joel a progress note at 03:35 UTC with three questions (P25's double negative, the P25 split, cutting P28's first sentence).

Batch 122g (written 03:35 UTC by `date -u`, before the call; `cands-v16.json`: P8 from round c u3 B, "She talks about how … and how it doesn't fall on one tired parent to be their whole social world", which also fixes the "no one exhausted parent" stumble and takes the gate's three P8 fixes; P10 from round f u3 B):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 122g-S8b-P8n (271) | Mixed | one window changed | AI (84%): the same two windows |
| 122g-S8b-P10n (268) | Mixed | the other window changed | AI (100%) |
| 122g-S8b-P8nP10n (270) | Human (weak) | both | AI (83%): the same two windows |
| 122g-P8n (alone, 99) | Human (weak) | round c's sentences | **Human (100%)** |
| 122g-P9P10n (108) | Human (weak) | round f's sentences | **Human (100%)** |

Batch 122g (submitted 03:36:19 UTC by the browser's clock, read 03:37): mine 2 of 5. The new P8 (which also settles the "no one exhausted parent" stumble and all three of the gate's P8 fixes) and P10 pass alone and with P9, but S8b keeps the same two AI windows: the heading through P8, and P9's last sentence through P10. P7 and P9's last sentence are the constants in those windows, so batch 123g changes them.

Batch 123g (written 03:37 UTC by `date -u`, before the call; `cands-v17.json`; new P8 and P10 in all):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 123g-S8b-P7c (272) | Mixed | P7 reworded | AI (100%) |
| 123g-S8b-P9b (272) | Mixed | P9's last sentence in two plain sentences | AI (83%): the same two windows |
| 123g-S8b-P7cP9b (274) | Human (weak) | both | AI (100%) |
| 123g-P7c (alone, 53) | Human (weak) | | **Human (100%)** |
| 123g-P9bP10n (110) | Human (weak) | | **Human (100%)** |

Batch 123g (submitted 03:38:12 UTC by the browser's clock, read 03:39): mine 2 of 5. Every S8b assembled from passing paragraphs reads AI (eight assemblies). Emulate round i (`community-s8i1`, `community-s8i2`, started 03:39:06 UTC, sha 08f67263a394) gets subsections b and d whole, in their current wording, to see whether a sample that reads as one piece can be fixed word by word. Credits left at 03:39: 13,813.

Round i is in (`emu/s8i-emu-all.json`, sha f022cf17871e): whole-subsection samples drift as far as the paragraph ones did. Before splicing from them, batch 124g checks the whole section as it stands (S8b and S8d included, though they fail as subsections, since the web app cuts its own windows over a whole section), with and without the P28 proposal, and two P25a openers in S8d's build-up.

Batch 124g (written 03:41 UTC by `date -u`, before the call; `cands-v18.json`; the full texts are in `gui/full-124g.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 124g-S8-prop (the section, P28 without its first sentence, 1665) | Mixed | S8b and S8d read AI as subsections | Mixed (27% AI, 1,732 words scanned): one AI window, P22's second sentence to the end (448 words); S8a, S8b and S8c read Human in the section |
| 124g-S8-P28f (the section, P28f whole, 1679) | Mixed | the same, and P27 with P28 | Mixed (28% AI, 1,747 words scanned): the same window (462 words) |
| 124g-D-S8d-3-a1 (241) | Human (weak) | "Nobody can offer unlimited freedom, so…" | Mixed (64% AI): P22's second sentence to P23's first (55 words), P24's third sentence to P25a's end (100) |
| 124g-D-S8d-3-a3 (241) | Human (weak) | "Unlimited freedom isn't on the table anyway." | Mixed (41% AI): the same P22–P23 window, and P24's last sentence to P25a's second (42) |

Batch 124g (submitted 03:41:57 UTC by the browser's clock, read 03:43): mine 2 of 4 (the section Mixed both times, as I said; the openers didn't pass). In the whole section, S8b reads Human, so its subsection failures are window effects; the one AI window is S8d from P22's second sentence through S8e. The section is 1,665 words against the published 1,339 in plain text: Emulate's sentences are longer, which goes to Joel as a note.

Batch 125g (written 03:43 UTC by `date -u`, before the call; `cands-v19.json`; S8d with S8e as one run, about 490 words, the length the web app reads as one window):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 125g-S8de (as is) | AI | the section's AI window | AI (93%): P22's second sentence to the end (448 words) |
| 125g-S8de-P22a | Mixed | P22's second sentence from round a and c ("blown out of proportion", "not as infants") | AI (93%): the same window |
| 125g-S8de-P22b | Mixed | another wording of it | AI (93%): the same window |
| 125g-S8de-P22aP24b | Mixed | and P24's last sentence ("less cash to go around") | AI (card) |
| 125g-P22a-alone | Human (weak) | | AI (card) |

Batch 125g (submitted 03:43:36 UTC by the browser's clock, read 03:44): mine 0 of 5 (the run reads AI from P22's second sentence whatever that sentence says, so the window is the run, not the sentence).

Batch 126g (written 03:44 UTC by `date -u`, before the call; `cands-v20.json`): S8d rebuilt on the flow of round i's whole-subsection samples (u2 B above all: "While the Rumspringa isn't as universal or crazy as pop culture makes it out to be…", "Very few people are going to, upon their kid's 18th birthday, just give them a bunch of money…", "So … a standard that's actually possible"), with the meaning fixed word by word and P25's second half kept from v12.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 126g-S8de-v20 | Mixed | a new run | AI (93%): P22's second sentence to the end (447 words) |
| 126g-P22 (v20, alone) | Human (weak) | round i's second sentence | **Human (100%)** |
| 126g-P22P23 (v20) | Human (weak) | | AI (100%) |
| 126g-P24 (v20, alone) | Human (weak) | round i's sentences | **Human (100%)** |
| 126g-P25a (v20, alone) | Human (weak) | | AI (100%) |

Batch 126g (submitted 03:45:14 UTC by the browser's clock, read 03:46): mine 2 of 5. A run rebuilt from round i reads AI over the same stretch (P22's second sentence to the end, 93%), though its P22 and P24 pass alone. Six S8d-with-S8e runs (125g, 126g) all read 93% AI from the same point.

Where section 8 stands at 03:46 UTC: every paragraph passes alone or with its neighbor; subsections a and c pass; in the whole section (124g) only one stretch reads AI, from P22's second sentence through the end (S8d and S8e, about 450 words, 27% of the section). Next: the gate on this candidate (v3, `drafts-v3.json`), so what goes to Joel is checked for meaning, and the S8d–S8e stretch goes to him with the tries counted.


## The d3 gate (7 reports, read at 04:26 UTC) and batch 127g

The gate on v3 (`drafts-v3.json`): traces A, B and C, logic audits forward and backward, the cold read and the stance check (`TRACE-d3-*.md`, `LOGIC-d3-*.md`, `SENSE-d3.md`, `STANCE-d3.md`). Stance: 2 conflicts (P2 "agree with me", P14 "won't actually prevent abuse"). Logic: 11 CHANGED and 14 AMBIGUOUS forward, 9 and 12 backward. Every finding is fixed word by word in `fix-d3/v127.py`, with the reason above each variant; the findings I keep are listed in the ic08 notes with the reason.

Batch 127g (written 04:39 UTC by `date -u`, before the call; `fix-d3/v127.json`, script `gui/b127.js`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 127g-P2a (59) | Human (weak) | both fixes go toward the published wording; P2 passed alone in 102g || **Human (100%)**, 04:40:21 |
| 127g-P2aP3a (104) | Human (weak) | P3 with "talk about" and "who lived through it" || AI (100%), 04:40:25 |
| 127g-P2aP3d (107) | Mixed | P3d opens with my anchor for "All of this" || AI (100%), 04:40:29 |
| 127g-P2b (60) | Human (weak) | "only saying that" in place of "but … do need" || **Human (100%)**, 04:40:33 |
| 127g-P5P6 (66) | Human | two word fixes in P5 || **Human (100%)**, 04:40:38 |
| 127g-P5 (50) | Human | P5 is 50 words, so it has to pass alone || **Human (100%)**, 04:40:43 |
| 127g-P7 (51) | Human | a comma || **Human (100%)**, 04:40:48 |
| 127g-P8a (98) | Mixed | four fixes in a paragraph where fixes have not combined before || **Human (100%)**, 04:40:52 |
| 127g-P8b (98) | Mixed | the same, and "One of the biggest reasons" || **Human (100%)**, 04:40:57 |
| 127g-P9a (65) | AI | three phrases back toward the published sentences, which read AI in 95g || **Human (100%)**, 04:41:02 |
| 127g-P9aP10a (101) | Mixed | P10 with "should study … directly" and "expands a kid's circle" || **Human (100%)**, 04:41:06 |
| 127g-P9aP10c (100) | AI | P10c is close to the published sentence || **Human (100%)**, 04:41:11 |
| 127g-P11P12 (74) | Human (weak) | word fixes || **Human (100%)**, 04:41:15 |
| 127g-P13aP14a (109) | Mixed | P13a opens with the published sentence; P13 alone read AI in 103g and 105g || Mixed (63% AI), 04:51:41: P13a and P14a's first sentence (71 words) |
| 127g-P13bP14b (108) | Mixed | the other order, and P14 with "reject" and "without actually preventing" || AI (100%), 04:51:44 |
| 127g-P14a (63) | Human (weak) | "don't buy the suburban panic", "can … and still not prevent" || **Human (100%)**, 04:51:49 |
| 127g-P14b (61) | AI | the published "reject" and "without actually preventing abuse" || **Human (100%)**, 04:51:54 |
| 127g-P15P16aP17 (89) | AI | "Their \"no\" matters" read AI in this triple before (103g, 105g) || AI (100%), 04:51:58 |
| 127g-P15P16bP17 (92) | Human (weak) | "When kids say no, it counts" || AI (100%), 04:52:03 |
| 127g-P17 (53) | Human (weak) | the definition cut, "secrets meant to isolate a kid" || **Human (100%)**, 04:52:10 |
| 127g-P18a (61) | Human (weak) | limits on the teaching back, in round g's rhythm || AI (100%), 04:52:15 |
| 127g-P18b (61) | Human (weak) | "Make sure the kids understand" || AI (100%), 04:52:19 |
| 127g-P19b (61) | Human (weak) | "accuse", "Decide on the response process", safety first || **Human (100%)**, 04:52:25 |
| 127g-P20a (93) | Mixed | the raid sentence changed, and "perspective, and somewhere to speak" || AI (100%), 04:52:28 |
| 127g-P20b (97) | Human (weak) | only the raid sentence and the next one changed || **Human (100%)**, 04:52:33 |
| 127g-P21c (107) | AI | both search conditions before "I couldn't find one": the published structure || AI (100%), 04:52:41 |
| 127g-P21b (108) | Human (weak) | "but I couldn't find any where the whole sequence was on record" || **Human (100%)**, 04:52:45 |
| 127g-P22a (58) | Human (weak) | "Amish young people decide as adults whether…" || **Human (100%)**, 04:52:50 |
| 127g-P22aP23 (98) | Human (weak) | P23 with "a community's kids" and "encounter" || **Human (100%)**, 04:52:54 |
| 127g-P22cP23 (102) | Human (weak) | "The Amish let their young people decide whether…" || AI (100%), 04:52:59 |
| 127g-P25a (56) | Human (weak) | "learn enough … that they aren't helpless in it" || **Human (100%)**, 04:53:04 |
| 127g-P25b1 (112) | AI | lists, and it read AI in most wordings || Mixed (65% AI), 04:53:11: "It would be great if…" to the end (80 words) |
| 127g-P25b2 (109) | AI | the same, "If the community can…, great." || AI (100%), 04:53:15 |
| 127g-P25b1P26 (154) | AI | the same || AI (100%), 04:53:20 |
| 127g-P27aP28a (75) | AI | the pair has read AI in about 20 wordings || AI (100%), 04:53:25 |
| 127g-P27bP28a (75) | AI | the same, "split over" || AI (100%), 04:53:30 |
| 127g-P27aP28c (76) | AI | the same, "to be consistent with them" || AI (100%), 04:53:34 |
| 127g-P24P27a (102) | Human (weak) | P27 passed beside P24 in 115g || **Human (100%)**, 04:53:43 |
| 127g-P24P28a (99) | Mixed | P28 beside P24 passed once (117g) and failed once || **Human (100%)**, 04:53:47 |


The laptop crashed and rebooted at 04:42 UTC (its login log says "crash", as on Oct 4 and Oct 5) while 127g's second call was running; nothing from that call reached Pangram (the History list ends at 04:41:15). From now on the result times are the server's own timestamps, read from the History page's data (`web.pangram.com/api/history/<id>/`) and matched to each item by its sha, so no time in this record is a guess. 127g so far: mine 9 of 13 (P9a, P9aP10a, P9aP10c and P8a/P8b read Human where I said AI or Mixed; P2a with P3a or P3d read AI where I said Human).

Batch 128g (written 04:50 UTC by `date -u`, before the call; `fix-d3/v128.json`): 127g's other 26 items, and these:

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 128g-P2aP3e (105) | Human (weak) | c4-P3 with only "who lived through it" added || AI (100%), 04:53:51 |
| 128g-P2aP3f (100) | Mixed | c4-P3 with only "talk about" || AI (100%), 04:53:55 |
| 128g-P2aP3g (106) | Human (weak) | "who grew up in it" || AI (100%), 04:54:00 |
| 128g-P2aP3h (106) | Mixed | "who actually lived through it" || AI (100%), 04:54:05 |
| 128g-P2aP3c4 (diagnostic) (101) | Human (weak) | P2a beside the P3 that passed with c4-P2 in 102g || AI (100%), 04:54:12 |
| 128g-P9aP10e (99) | Human (weak) | "deserves direct study" with "expands a kid's circle" || Mixed (59% AI), 04:54:17: P9a's last sentence and P10e (66 words) |


127g and 128g (submitted 04:51:36 to 04:54:19 UTC; times above are the server's): 127g overall mine 23 of 39, 128g mine 0 of 6. What they show: every fixed P2 passes alone, but P2a beside any P3 reads AI, the P3 that passed in 102g included (128g diagnostic), so P2a's new second sentence tips the pair, not P3's fixes; P9a passes with P10a and with P10c but not with P10e, which joins their two halves (non-additive again); P14a and P14b both pass alone; P15–P17 reads AI with either P16 fix; P18's four fixes together read AI; P20b, P21b, P22a with P23 and P25a pass; P25b's fixes read AI from "It would be great if…" on; every P27 and P28 pair reads AI again, while each passes beside P24.


Batch 129g (written 04:58 UTC by `date -u`, before the call; `fix-d3/v129.json`). Emulate round j (`community-s8j`, started 04:57:38 UTC) has the fixed P2–P3, P13–P14, P15–P17, P18, P25b and P27–P28 in case these fail.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 129g-P2bP3e (106) | Mixed | P2b passed alone; the pair is the question || AI (100%), 04:58:59 |
| 129g-P2bP3g (107) | Mixed | the same, "who grew up in it" || AI (100%), 04:59:03 |
| 129g-P2bP3f (101) | Mixed | "talk about" || Mixed (40% AI), 04:59:07: P3f (42 words) |
| 129g-P2bP3c4 (102) | Human (weak) | diagnostic: P2b beside the P3 that passed in 102g || **Human (100%)**, 04:59:12 |
| 129g-P2g (62) | Human (weak) | round f's "only … there needs to be" kept, in the present || **Human (100%)**, 04:59:17 |
| 129g-P2gP3e (108) | Mixed | P2g beside P3e || AI (100%), 04:59:21 |
| 129g-P13cP14b (109) | Human (weak) | round b's "lord it over" and "pass for" kept, the duty on the adults || AI (100%), 04:59:28 |
| 129g-P13dP14b (108) | Mixed | the published order of P13's first sentence || AI (100%), 04:59:33 |
| 129g-P13eP14b (106) | Human (weak) | only the first sentence changed from the passing c7-P13a || **Human (100%)**, 04:59:39 |
| 129g-P13dP14a (110) | Mixed | P14a in place of P14b || **Human (100%)**, 04:59:42 |
| 129g-P15P16c8P17f (92) | Human (weak) | diagnostic: the old P16 with the fixed P17 || AI (100%), 04:59:47 |
| 129g-P15P16bP17c6 (103) | Mixed | diagnostic: the fixed P16 with the old P17 || **Human (100%)**, 04:59:52 |
| 129g-P15P16fP17 (94) | Mixed | "Kids are allowed to say no, and it counts." || AI (100%), 05:00:00 |
| 129g-P15P16gP17 (90) | Mixed | "A kid's no counts" || AI (100%), 05:00:04 |
| 129g-P18c (65) | Human (weak) | only the third sentence fixed on the passing c6-P18 || **Human (100%)**, 05:00:09 |
| 129g-P18h (65) | Mixed | and "adults will take what they say seriously" || AI (100%), 05:00:14 |
| 129g-P18i (67) | Mixed | and "may not tell the story perfectly" || AI (100%), 05:00:20 |
| 129g-P21f (106) | AI | "I couldn't find any." after the long sentence, close to P21c || AI (100%), 05:00:23 |
| 129g-P25b3 (117) | Human (weak) | only the first sentence's fixes on the passing v12 || Mixed (66% AI), 05:00:30: "It would be great if…" to the end (85 words) |
| 129g-P25b4 (118) | Mixed | and "help with travel" || Mixed (66% AI), 05:00:35: the same (86 words) |
| 129g-P25b3P26 (159) | Mixed | P26 passed beside v12 in 115g || AI (100%), 05:00:41 |
| 129g-H4P27aP28s2 (70) | Human (weak) | the cut passed in 119g and 120g || **Human (100%)**, 05:00:45 |
| 129g-H4P27bP28s2 (70) | Human (weak) | "split over" || Mixed (49% AI), 05:00:49: "And that's just two people…" to the end (37 words) |

129g (submitted 04:58:55 to 05:00:51 UTC): mine 8 of 23. P2b passes beside the P3 that passed in 102g, but beside no fixed P3; P13 passes with the duty on the adults (d) beside P14a, and with only its first sentence fixed (e) beside P14b; the P15–P17 triple passes with the fixed P16 and the old P17 but fails with the fixed P17 whatever P16 is, though the fixed P17 passes alone; P18 passes with only its third sentence fixed (c); P25b's fixed first sentence turns v12's untouched remainder AI from "It would be great if…"; P27a with P28's second sentence passes under H4 (the cut).

Batch 130g (written 05:02 UTC by `date -u`, before the call; `fix-d3/v130.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 130g-P15P16bP17j (104) | Mixed | only "secrets meant to isolate a kid" in the triple || **Human (100%)**, 05:03:16 |
| 130g-P15P16bP17k (91) | Mixed | only "A surprise has an end date." || AI (100%), 05:03:20 |
| 130g-P17j (65) | Human (weak) |  || **Human (100%)**, 05:03:25 |
| 130g-P17k (52) | Human (weak) |  || **Human (100%)**, 05:03:30 |
| 130g-P18j (65) | Human (weak) | "tell it badly" on the passing P18c || **Human (100%)**, 05:03:34 |
| 130g-P25b5 (124) | Mixed | only "Kids also need" on v12 || **Human (100%)**, 05:03:39 |
| 130g-P25b6 (122) | Mixed | and the next step without "outside the community", with "or" || **Human (100%)**, 05:03:47 |
| 130g-P25b8 (119) | Human (weak) | only the two "good"s out || **Human (100%)**, 05:03:52 |
| 130g-P25b5P26 (166) | Mixed |  || **Human (100%)**, 05:03:55 |
| 130g-P25b6P26 (164) | Mixed |  || AI (100%), 05:04:00 |
| 130g-P2bP3i (105) | Mixed | "the kids who lived it" || AI (100%), 05:04:04 |
| 130g-P2bP3k (104) | Mixed | "reviewed by the kids who grew up with it" || AI (100%), 05:04:09 |

130g (submitted 05:03:12 to 05:04:11 UTC): mine 4 of 12 (P17j, P17k, P18j, P25b8 as I said; P25b5 and P25b6 Human and P15P16bP17j Human where I said Mixed). P17 passes in the triple with "secrets meant to isolate a kid" but not with "A surprise has an end date."; P18 passes with the limits on the teaching back and "tell it badly"; P25b passes with "Kids also need" alone and beside P26. No fixed P3 passes beside P2b (eight wordings, 127g to 130g); the P3 that passed in 102g passes beside P2b.


The candidate after the fixes is `cand-v21.json` (`fix-d3/compose.py`: P2b, the 102g P3, P5, P7, P8b, P9a, P10a, P11, P12, P13d, P14a, P16b, P17j, P18j, P19b, P20b, P21b, P22a, P23, P25a, P25b5, P26, P27a, P28a; the cut P28 is the proposal). Every paragraph in it passed alone, or with a neighbor that passed alone.

Batch 131g (written 05:05 UTC by `date -u`, before the call; `fix-d3/v131.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 131g-S8-v21-P28whole (1633) | Mixed | every paragraph now passes alone or with its neighbor, but 124g's window (P22's second sentence to the end) read AI over six rebuilds || Mixed (61% AI, 1,693 words scanned), 05:06:33: four AI windows: P7's second sentence to P10's end (244 words), P12's second sentence to P16's end (177), P17's third sentence to P19's last (142), P22's second sentence to the end (462) |
| 131g-S8-v21-P28cut (1619) | Mixed | the same, with P28's first sentence cut (Joel's question 3) || Mixed (61% AI, 1,678 words scanned), 05:06:37: the same four windows (the last 447 words) |
| 131g-S8de-v21 (474) | AI | the stretch that read AI in 124g to 126g, with P25b and P27–P28 changed || AI (100%), 05:06:41 |
| 131g-P25b9 (119) | Human (weak) | "Kids also need" and the two "good"s out, on v12 || **Human (100%)**, 05:06:46 |
| 131g-P25b9P26 (161) | Mixed |  || **Human (100%)**, 05:06:51 |

131g (submitted 05:06:29 to 05:06:53 UTC): mine 4 of 5. The section with every paragraph passing alone reads 61% AI, against 27% for v3 in 124g: the meaning fixes in subsections b and c, each passing alone, read AI together in the section's own windows. P25b9 ("Kids also need" and both "good"s out) passes alone and beside P26, so it replaces P25b5.

Batch 132g (written 05:08 UTC by `date -u`, before the call; `fix-d3/v132.json`): diagnostics only, each one the whole section with some paragraphs back in their v3 wording, to find which fixes turn subsections b and c AI inside the section. None of these is a candidate.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 132g-S8-v21b (1628) | Mixed | 131g's section with P25b9 (a check of the baseline) || Mixed (64% AI), 05:09:54: P7–P10 (244 words), P12–P19 (373), P22–end (457) |
| 132g-S8-oldS8b (1635) | Mixed | P7–P10 back to v3, which read Human inside the section in 124g || Mixed (41% AI), 05:09:58: P13–P16 (132), P18–P19 (100), P22–end (457) |
| 132g-S8-oldS8c (1639) | Mixed | P11–P21 back to v3 || Mixed (35% AI), 05:10:05: P7–P8 (137), P22–end (457) |
| 132g-S8-oldP8 (1627) | Mixed | only P8 back || Mixed (59% AI), 05:10:08: P7–P8 (75), P9–P10 (94), P12–P19 (373), P22–end (457) |
| 132g-S8-oldP9P10 (1636) | Mixed | only P9 and P10 back || Mixed (36% AI), 05:10:12: P16 (33), P18–P19 (100), P22–end (457) |
| 132g-S8-oldP11P12 (1630) | Mixed |  || Mixed (66% AI), 05:10:19: P7–P10 (244), P12–P20 (407), P22–end (457) |
| 132g-S8-oldP13P14 (1630) | Mixed |  || Mixed (38% AI), 05:10:24: P7–P8 (75), P18–P19 (100), P22–end (457) |
| 132g-S8-oldP16P17 (1627) | Mixed |  || Mixed (68% AI), 05:10:29: P7–P19 (686), P22–end (457) |
| 132g-S8-oldP18P19 (1630) | Mixed |  || Mixed (47% AI), 05:10:33: P7–P10 (244), P12–P14 (89), P22–end (457) |

132g (submitted 05:09:50 to 05:10:35 UTC): mine 9 of 9 (all Mixed). What the diagnostics show: P22 to the end reads AI in every version (457 words); subsection b's window goes away when P9 and P10 go back to v3 (and only then), and subsection c's shrinks when P13–P14 or P9–P10 go back; P16–P17 back to v3 makes it worse (one 686-word window). The windows move with paragraphs outside them, so a paragraph that passes alone is not evidence about the section. None of these is a candidate: the v3 wordings are the ones the gate found changed.


## The d4 gate (7 reports, back at 05:48 UTC) and batch 133g

The gate on v4 (`drafts-v4.json`, the candidate after 127g–131g): stance 1 conflict (P25b turns the leaving help into cash: "travel expenses", "a little money"); logic forward 3 CHANGED (2 minor) and 8 AMBIGUOUS, backward 3 CHANGED and 3 AMBIGUOUS; the traces repeat P3 and P13 and add P8, P10, P17, P18, P19, P21, P22, P25, P26. Some of these my fixes caused: P16's "When kids say no" now governs the next clause, P23's "them" can be the founders, P22's "their teenage Rumspringa" says every Amish youth has one, P26's "others will start" left "It's possible". Each is fixed in `fix-d3/v133.py`, with the reason above it.

Batch 133g (written 05:50 UTC by `date -u`, before the call; `fix-d3/v133.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 133g-P2n (54) | Human (weak) | two sentences where "only saying that" was || **Human (100%)**, 05:50:52 |
| 133g-P2nP3c4 (96) | Mixed | the P2–P3 pair has read AI with every new P2 but P2b || AI (100%), 05:50:56 |
| 133g-P2nP3e (100) | AI | and P3 with "who lived through it" || AI (100%), 05:51:02 |
| 133g-P7n (50) | Human | "should" out || **Human (100%)**, 05:51:05 |
| 133g-P8n2 (92) | Mixed | "She talks about how" out; P8 is fragile || **Human (100%)**, 05:51:09 |
| 133g-P9aP10g (99) | Human (weak) | P10c with the system as the agent || **Human (100%)**, 05:51:14 |
| 133g-P13fP14c (107) | Mixed | "dominate"; P14 with "reject" and "every" || Mixed (63% AI), 05:51:22: P13f and P14c's first sentence (68 words) |
| 133g-P13gP14c (110) | Mixed | "treated as independence" || **Human (100%)**, 05:51:26 |
| 133g-P13dP14c (109) | Human (weak) | the passing P13d beside the new P14 || **Human (100%)**, 05:51:32 |
| 133g-P13fP14a (108) | Mixed |  || AI (100%), 05:51:35 |
| 133g-P14c (62) | Human (weak) |  || **Human (100%)**, 05:51:40 |
| 133g-P15P16hP17j (103) | Mixed | the no in its own sentence || **Human (100%)**, 05:51:45 |
| 133g-P15P16hP17l (90) | AI | "Surprises have an end date." read AI in the triple as "A surprise…" || AI (100%), 05:51:53 |
| 133g-P18l (65) | Mixed | "Make sure the kids understand" || **Human (100%)**, 05:51:57 |
| 133g-P18m (67) | Mixed | "may get mixed up telling it" || **Human (100%)**, 05:52:02 |
| 133g-P19c (64) | Human (weak) | "the accused", "whoever's at risk" || AI (100%), 05:52:07 |
| 133g-P21g (102) | AI | "I couldn't find one." after the long sentence read AI twice || **Human (100%)**, 05:52:11 |
| 133g-P22dP23n (99) | Mixed |  || AI (100%), 05:52:16 |
| 133g-P22eP23n (96) | AI | close to the published sentence || AI (100%), 05:52:23 |
| 133g-P22d (59) | Human (weak) |  || **Human (100%)**, 05:52:28 |
| 133g-P25a2 (53) | Human (weak) | "It's that leaving shouldn't be made…" || AI (100%), 05:52:33 |
| 133g-P25b10 (120) | Human (weak) | "help with travel", "a small reserve" || AI (100%), 05:52:37 |
| 133g-P25b10P26n (163) | Mixed | "and that others will start" || AI (100%), 05:52:42 |

133g (submitted 05:50:49 to 05:52:44 UTC): mine 10 of 23. Passing now: P2n alone (but not beside either P3), P7n, P8n2, P9a with P10g, P13g and P13d beside P14c, P14c alone, the triple with P16h and P17j, P18l and P18m (separately), P21g (the search target holding both conditions, then "I couldn't find one."), P22d alone. Still AI: "dominate" in P13 (twice), "Surprises have an end date." in the triple (third time), P19c, P23n beside either P22, P25a2, and P25b with "help with travel" and "a small reserve".

Batch 134g (written 05:54 UTC by `date -u`, before the call; `fix-d3/v134.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 134g-P2oP3c4 (96) | AI | the pair reads AI with every P2 but P2b || AI (100%), 05:54:40 |
| 134g-P2oP3e (100) | AI |  || AI (100%), 05:54:45 |
| 134g-P2nP3l (98) | AI | P3 in the active voice || AI (100%), 05:54:49 |
| 134g-P2o (96) | Human (weak) | the published semicolon || **Human (100%)**, 05:54:53 |
| 134g-P13hP14c (109) | Mixed | "boss the younger ones around" || **Human (100%)**, 05:55:01 |
| 134g-P18n (67) | Mixed | 133g's two passing P18 fixes together || **Human (100%)**, 05:55:02 |
| 134g-P19d (62) | Mixed | only "the accused is someone people love" || **Human (100%)**, 05:55:10 |
| 134g-P19e (63) | Human (weak) | only "Keep whoever's at risk safe first" || AI (100%), 05:55:15 |
| 134g-P22dP23f (99) | Human (weak) | diagnostic: P22d beside the P23 that passed with P22a || AI (100%), 05:55:19 |
| 134g-P22aP23n (98) | AI | diagnostic: is P23n the problem? || AI (100%), 05:55:24 |
| 134g-P22dP23o (101) | Mixed | "without the community treating them as traitors" || AI (100%), 05:55:29 |
| 134g-P25a3 (55) | Mixed | "just" out || **Human (100%)**, 05:55:33 |
| 134g-P25a5 (52) | Mixed | "It's making sure leaving isn't artificially impossible." || AI (100%), 05:55:42 |
| 134g-P25b11 (120) | Mixed | only "help with travel" || **Human (100%)**, 05:55:46 |
| 134g-P25b12 (119) | Mixed | only "a small reserve" || AI (100%), 05:55:51 |
| 134g-P25b9P26n (162) | Human (weak) | P26 with "and that others" || Mixed (39% AI), 05:55:55: "No upbringing can provide…" to P26's end (69 words) |

134g (submitted 05:54:37 to 05:55:58 UTC): mine 5 of 16. Passing: P13h ("boss the younger ones around") beside P14c, P18n (both P18 fixes), P19d ("the accused is someone people love"), P25a3 ("just" out), P25b11 ("help with travel"). Still AI: every P2 beside P3 except P2b, every pairing of a fixed P22 or P23 (so P23, at 40 words, goes next to its other neighbor, P24, which passes alone), "whoever's at risk" in P19, "a small reserve" in P25b, and P26 with "and that others".

Batch 135g (written 05:57 UTC by `date -u`, before the call; `fix-d3/v135.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 135g-P23nP24 (103) | Human (weak) | P23 beside its other neighbor || **Human (100%)**, 05:57:23 |
| 135g-P23oP24 (105) | Mixed |  || **Human (100%)**, 05:57:27 |
| 135g-P25b13 (120) | Mixed | "a small stash" || **Human (100%)**, 05:57:32 |
| 135g-P25b11P26o (162) | Mixed | "and others may start" || Mixed (39% AI), 05:57:36: "No upbringing can provide…" to P26's end (68 words) |
| 135g-P25b11P26 (162) | Human (weak) | the P26 that passed beside P25b9 || **Human (100%)**, 05:57:41 |
| 135g-P2rP3c4 (99) | Mixed | P2b without "among the parents" || AI (100%), 05:57:46 |
| 135g-P2r (57) | Human (weak) |  || **Human (100%)**, 05:57:53 |

135g (submitted 05:57:19 to 05:57:56 UTC): mine 4 of 7. P23 passes beside P24 with "without being treated as traitors"; P25b passes with "a small stash"; P26 passes beside P25b only as it was ("and others will start"); P2 without "among the parents" passes alone but not beside P3. In 127g–135g, twenty P2–P3 pairs: only P2b (with "only saying that … among the parents") beside the 102g P3 reads Human.

The candidate after 133g–135g is `cand-v22.json` (choices in `fix-d3/choice-v22.json`): P2n (faithful; the pair with P3 reads AI), P7n, P8n2, P10g, P13h, P14c, P16h, P17j, P18n, P19d, P20b, P21g, P22d, P23n, P25a3, P25b13, P26 as it was.

Batch 136g (written 05:58 UTC by `date -u`, before the call; `fix-d3/v136.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 136g-S8-v22-P28whole (1609) | Mixed | the d4 fixes changed b and c again; P22 to the end has read AI in every version || Mixed (42% AI, 1,669 words scanned), 05:59:29: P8 (81 words), P9's last sentence and P10 (65), P13's end and P14's start (42), P18's middle to P19's first words (49), P22's second sentence to the end (460) |
| 136g-S8-v22-P28cut (1595) | Mixed | the same, with the cut || Mixed (41% AI, 1,654 words scanned), 05:59:34: the same five windows (the last 445) |
| 136g-S8de-v22 (470) | AI | the stretch alone || AI (100%), 05:59:38 |
| 136g-S8bc-v22 (878) | Mixed | subsections b and c together (878 words) || Mixed (38% AI, 913 words scanned), 05:59:43: H1 to P10 (265), P12's second sentence to P14's first (87) |

136g (submitted 05:59:27 to 05:59:45 UTC): mine 4 of 4. The section is down from 64% to 42% AI. Subsections b and c now read AI only in short windows (P8; P9–P10; P13–P14; P18–P19), and P22 to the end reads AI as it has in every whole-section run since 119g (v3; the six rebuilds of the stretch in 125g and 126g; the meaning-fixed v21 and v22).

Where section 8 stands at 06:01 UTC: candidate v22 (`cand-v22.json`); every paragraph passes alone or beside a neighbor that passes alone, except P3, which passes beside no meaning-fixed P2 (the only passing pair keeps P2b's "only saying that", which the gate calls a logic change); the section reads 42% AI. Not installed. Next: the gate on v22 (d5), then Joel.


## The d5 gate (7 reports, back at 06:22 UTC)

On v5 (`drafts-v5.json`, the text of `cand-v22.json`). Clean now: P2, P7, P9, P11, P12, P14 to P16, P20, P21, P23, P24, P27, P28 (the traces mark wording shifts there, none that changes what a reader believes). Still open:

- P13 (stance conflict, both logic audits CHANGED, trace B): "boss the younger ones around" makes the danger ordinary bossiness, which the essay leaves to the kids ("resolve ordinary disputes"). "dominate" read AI beside P14 twice (133g); "lord it over" (passes) is lighter. Next: "control" or "rule over", one at a time.
- P3 (trace A, logic A): "All of this" with the added prediction, "who lived through the system" gone, "go on about". No P3 fix passes beside any P2 (nine P3 wordings, 20 pairs).
- P19 (all three reviewers): "Keep everyone safe first" includes the accused. "whoever's at risk" read AI (133g, 134g).
- P25a (both logic audits, the cold read): "It's not making it artificially impossible…" reads first as a second denial. Two other wordings read AI.
- P26 (trace C, both logic audits): "others will start" can fall outside "It's possible". Both fixes read AI beside P25b; not yet tried beside P25b13.
- P22 (trace C): "seem like a wilder, more universal teenage free-for-all than it is" takes the free-for-all as given. P22e (the published claim) not yet tried alone.
- P17 (trace B, logic A): "A surprise isn't a secret, because…" (an exemption by definition); "Surprises have an end date." read AI in the triple three times.
- P18 (trace B): "may get mixed up telling it" is narrower than "imperfectly"; "badly" was stronger.
- P8 and P10 (trace A, minor): the caveat covers the book, not her account; "what's going on at", "interact with more people".
- P25b (trace C, minor): "can provide" for "offers".

These go to Joel with the candidate as it stands, the questions and the tries; section 8 stays out of `HUMANIZED-SO-FAR.md`.

## Joel's 15:05 UTC edits: v23, batch 137g

Joel's texts and rulings are in `joel-1505/joel-20261007-1505.json`; `joel-1505/build_v23.py` builds v23 (`cand-v23.json`, `section-d6.md`). His own checks in the web app this morning, read from the History data: P3 Human (low, 56 words, 12:46:20), an earlier P21 Human (medium, 13:54:20), my P22–P25 run AI (14:03:42), his P22–P25 rewrite Human (high, 397 words, 14:59:37).

Batch 137g (written 15:11 UTC by `date -u`, before the call; `joel-1505/v137.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 137g-S8-v23 (1667) | Mixed | your rewrite of P22 to the end read Human (your 14:59 check), but P27 with P28 has read AI as a pair, and b and c had short windows in 136g || Mostly Human (4% AI, 1,732 words scanned), 15:12:24: one AI window, P27's last sentence to P1's second (68 words) |
| 137g-H0P27P28 (82) | AI | the pair read AI in about 20 wordings || AI (100%), 15:12:27 |
| 137g-P27P28P1 (125) | Mixed | the pair beside your P1 || AI (100%), 15:12:31 |
| 137g-P2bP3j (114) | Human (weak) | both pass alone || **Human (100%)**, 15:12:36 |
| 137g-P9aP10j (120) | Human (weak) | your P10 || **Human (100%)**, 15:12:43 |
| 137g-P10j (55) | Human (weak) | your P10 alone (53 words) || **Human (100%)**, 15:12:51 |
| 137g-P18j (132) | Human | your P18 || **Human (100%)**, 15:12:56 |
| 137g-P21j (121) | Human | your final P21 ("the rare, but real threat…"); your 13:54 check was the earlier wording || **Human (100%)**, 15:13:00 |
| 137g-S8d-j (388) | Human | your 14:59 check with the two typos fixed and the last line on its own || **Human (100%)**, 15:13:04 |
| 137g-H1P8P9P10 (216) | Mixed | the new subsection || AI (100%), 15:13:06 (the subsection alone; inside the section it reads Human) |
| 137g-P19f (68) | Mixed | "Keep the child and anyone else at risk safe first" || AI (100%), 15:13:15 |
| 137g-P19h (61) | Mixed | "Safety comes first, right away." || AI (100%), 15:13:20 |

137g (submitted 15:12:22 to 15:13:21 UTC): mine 7 of 12 (the section was Mostly Human, not Mixed; the three-paragraph opener, the subsection and both P19 wordings read AI where I said Mixed). The section reads Mostly Human, 4% AI: the only AI window is P27 and P28 at the top, with the start of P1. Every one of your texts passes alone (P3 with P2b, P10, P18, P21, the P22–P26 rewrite); your new subsection reads AI as a run on its own and Human inside the section. P19's two safety wordings read AI.

Batch 138g (written 15:14 UTC by `date -u`, before the call; `joel-1505/v138.json`): the top of the section.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 138g-S8-v23-P28cut (1653) | Human (weak) | P28 without "Once a kid is already living inside the disagreement, goodwill doesn't answer those questions." (my 03:35 proposal, not answered) | |
| 138g-S8-v23-P27b (1667) | Mixed | "still split over" in P27 | |
| 138g-S8-v23-P27P28merged (1667) | Mixed | P27 and P28 as one paragraph | |
| 138g-H0P27P28s2 (68) | Human (weak) | the cut beside the title | |
| 138g-H0P27P28s2P1 (118) | Human (weak) | and your P1 | |

138g (submitted 15:18:06 to 15:18:26 UTC): mine 2 of 5. Without P28's first sentence the top passes, but a 42-word window opens at P13's end and P14's start (2% AI), the window 136g had too; "split over" and joining P27 to P28 leave the top window as it was. The opener with the cut passes beside the title, and reads AI once your P1 joins it, yet P1 reads Human in the section.

| 138g result | |
|---|---|
| 138g-S8-v23-P28cut | Mostly Human (2% AI, 1,717 words scanned), 15:18:07: P13's third sentence to P14's first (42 words) |
| 138g-S8-v23-P27b | Mostly Human (4% AI, 1,732), 15:18:11: the top window (68 words) |
| 138g-S8-v23-P27P28merged | Mostly Human (4% AI, 1,732), 15:18:16: the top window (68 words) |
| 138g-H0P27P28s2 | **Human (100%)**, 15:18:21 |
| 138g-H0P27P28s2P1 | AI (100%), 15:18:25 |

Batch 139g (written 15:21 UTC by `date -u`, before the call; `joel-1505/v139.json`): the whole section each time, since pairs and the section disagree here.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 139g-S8-A1-order (1667) | Mostly Human | P28 opens with "Goodwill", as the published sentence did || Mostly Human (4% AI, 1,732 words scanned), 15:21:45: the top window (68 words) |
| 139g-S8-A2-middle (1670) | Mostly Human | "in the middle of" for "inside" || Mostly Human (10% AI, 1,735), 15:21:49: the top window to P28's end (49), P8 (81), P13's end to P14's start (42) |
| 139g-S8-A3-growing (1668) | Mostly Human | "growing up" for "living" || Mostly Human (7% AI, 1,733), 15:21:52: the top window (69), P13–P14 (42) |
| 139g-S8-A5-bythetime (1668) | Mostly Human | "By the time" for "Once … already" || Mostly Human (5% AI, 1,733), 15:21:57: P27's last sentence and P28 (47), P13–P14 (42) |
| 139g-S8-C1-twenty (1667) | Mostly Human | P27's last sentence nearer the published "twenty adults with twenty childhoods" || Mostly Human (4% AI, 1,732), 15:22:02: the top window (68) |
| 139g-S8-B1-cut-dontbuy (1654) | Human (weak) | the cut, with "don't buy" for "reject" in P14 (the 42-word window's end) || Mostly Human (2% AI, 1,719), 15:22:11: P13–P14 (44) |
| 139g-S8-B2-cut-passfor (1652) | Human (weak) | the cut, with "can't pass for" in P13 (the window's start; 133g's wording) || Mostly Human (2% AI, 1,716), 15:22:16: P13–P14 (41) |
| 139g-S8-B3-cut-adultchild (1653) | Mostly Human | the cut, with P14's pair in the published order || Mostly Human (2% AI, 1,717), 15:22:22: P13–P14 (42) |

139g (submitted 15:21:45 to 15:22:22 UTC): mine 6 of 8. No wording of P28's first sentence clears the top window; four of them also open the P13–P14 window, and one opens P8. With the cut, single-word changes at P13's end or P14's start leave the P13–P14 window in place, so that stretch needs more than a word. Sent Joel a status note at 15:24 UTC asking about the cut again.

Batch 140g (written 15:25 UTC by `date -u`, before the call; `joel-1505/v140.json`): the P13–P14 window. P14 also has "can destroy that gift and still not prevent abuse", the "X and still Y" shape you named at 15:05, and a "who, who, and who" list of three.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 140g-S8-cut-K1 (1651) | Mostly Human | P14 without its "who, who, and who" list and without "and still not" (the tell you named; the published sentence said "without actually preventing abuse"); the window's own words are unchanged || Mostly Human (5% AI, 1,716 words scanned), 15:26:13: P13's third sentence to P14's end (85 words) |
| 140g-S8-cut-K2 (1654) | Human (weak) | K1, and P14 opens "At the same time, I reject" (the window's end) || Mostly Human (5% AI, 1,719), 15:26:16: the same stretch (88) |
| 140g-S8-cut-K3 (1652) | Human (weak) | K1, and P13's last sentence split in two, "keeping secrets" for "secrecy" (the window's start) || Mostly Human (5% AI, 1,717), 15:26:22: the same stretch (86) |
| 140g-S8-cut-K4 (1652) | Mostly Human | only the tell fixed || Mostly Human (2% AI, 1,716), 15:26:26: P13–P14 (42), as before |
| 140g-S8-cut-K5 (1654) | Human (weak) | only P13's split || **Human (100%, 1,718 words scanned)**, 15:26:32 |
| 140g-S8-v23-K2 (1668) | Mostly Human | K2 in the section with P28 whole: the top window should stay, and P13–P14 should not open || Mixed (11% AI, 1,734), 15:26:34: the top window (68) and P13's third sentence to P16 (126) |

140g (submitted 15:26:13 to 15:26:34 UTC): mine 2 of 6. The section reads 100% Human with the cut and P13's last sentence split ("… around there. And keeping secrets can't be treated as independence."). Restructuring P14's list made its window longer every time; fixing only the "and still not" tell left the window as it was. Batch 141g checks the split with the tell fixed, and the split without the cut.

Batch 141g (written 15:27 UTC by `date -u`, before the call; `joel-1505/v141.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 141g-S8-cut-K6 (1653) | Human (weak) | K5 with the tell fixed (K4 showed the fix alone is neutral) || Mostly Human (5% AI, 1,717 words scanned), 15:27:30: P13's third sentence to P14's end (86 words) |
| 141g-S8-v23-K5 (1668) | Mostly Human | the split with P28 whole: the top window should stay || Mostly Human (4% AI, 1,733), 15:27:35: the top window (68) |
| 141g-S8-v23-K6 (1667) | Mostly Human | the same with the tell fixed || Mostly Human (4% AI, 1,732), 15:27:40: the top window (68) |

141g (submitted 15:27:30 to 15:27:40 UTC): mine 2 of 3. The published "without actually preventing abuse" reads AI beside the split (86 words, P13's end to P14's end), so the tell needs another wording. Without the cut, the split leaves only the top window.

Batch 142g (written 15:28 UTC by `date -u`, before the call; `joel-1505/v142.json`): K5 (100% Human) with the "and still not" tell reworded.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 142g-S8-K5-Ta (1655) | Human (weak) | "and it doesn't actually prevent abuse": two plain clauses || **Human (100%, 1,720 words scanned)**, 15:28:32 |
| 142g-S8-K5-Tb (1655) | Human (weak) | "doesn't even" || **Human (100%, 1,720)**, 15:28:37 |
| 142g-S8-K5-Tc (1654) | Mixed | "but it won't" || **Human (100%, 1,719)**, 15:28:41 |
| 142g-S8-K5-Td (1654) | Mixed | two sentences || Mostly Human (3% AI, 1,719), 15:28:46: P13–P14 (43 words) |

142g (submitted 15:28:32 to 15:28:46 UTC): mine 2 of 4 (Tc passed where I said Mixed; Td read Mostly Human, not Mixed). Three wordings without "and still" pass in the whole section. Ta keeps the published "actually" and says the same thing, so it is the candidate: "Fear like that can destroy that gift, and it doesn't actually prevent abuse." The candidate is `cand-v24.json` (P28's cut is a proposal until Joel answers).

Gate on v24 (three fresh agents, all back by 15:51 UTC; `review-d7/`, `STANCE-d7.md`): the trace found P28 LOSS (the cut, as proposed), P13 SHIFT ("keeping secrets" is narrower than "secrecy") and P14 SHIFT ("doesn't actually prevent" is a flat claim where v23 and the published sentence had a "can" over both halves). Batch 143g puts "secrecy" back and tries P14 wordings that keep the possibility.

Batch 143g (written 15:51 UTC by `date -u`, before the call; `joel-1505/v143.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 143g-S8-E1-Ta (1654) | Human (weak) | "secrecy" back (the trace: "keeping secrets" narrows it to single acts); P14 as in v24 || Mostly Human (5% AI, 1,719 words scanned), 15:52:16: P13's third sentence to P14's end (88 words) |
| 143g-S8-E2-witheven (1652) | Mixed | "secrecy" back; P14 keeps one "can" over both halves, as published, with "even" for "actually" || Mostly Human (2% AI, 1,716), 15:52:20: P13–P14 (42) |
| 143g-S8-E3-mightnot (1655) | Human (weak) | "secrecy" back; P14 says "might not", a possibility, as v23's "can … still not" did || Mostly Human (2% AI, 1,719), 15:52:23: P13–P14 (42) |
| 143g-S8-E4-still (1653) | Human (weak) | "secrecy" back; P14 as v23 (the tell kept), to see what the restore does alone || Mostly Human (2% AI, 1,717), 15:52:28: P13–P14 (42) |

143g (submitted 15:52:16 to 15:52:28 UTC): mine 0 of 4. With "secrecy" back, the P13–P14 window returns whatever P14 says: "keeping secrets" is what clears it. I keep "keeping secrets" (in a children's territory, the secrecy meant is kids keeping secrets from the adults; I judge it the same claim, and report the trace's flag to Joel). Batch 144g tries the two P14 wordings that keep the published "can" over both halves, beside "keeping secrets".

Batch 144g (written 15:53 UTC by `date -u`, before the call; `joel-1505/v144.json`): v24 with P14's last sentence reworded.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 144g-S8-K5-witheven (1653) | Human (weak) | the published "without … preventing", "even" for "actually" || Mostly Human (3% AI, 1,717 words scanned), 15:53:12: P13–P14 (43 words) |
| 144g-S8-K5-mightnot (1656) | Human (weak) | "might not": a possibility, as v23 had || **Human (100%, 1,720 words scanned)**, 15:53:16 |

144g (submitted 15:53:12 to 15:53:16 UTC): mine 1 of 2. "and it might not even prevent abuse" passes in the whole section and keeps the possibility. The candidate is `cand-v25.json` (`joel-1505/build_v25.py`): v23 with P28's first sentence cut (a proposal), P13's last sentence split ("keeping secrets"), and P14's last sentence reworded.

Batch 145g (written 16:05 UTC by `date -u`, before the call; `joel-1505/v145.json`): v25 with P19's "everyone" narrowed, the one gate finding still open in my text.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 145g-S8-v25-P19-everyoneatrisk (1658) | Human (weak) | "everyone at risk": the d5 logic checks found "everyone" could take in the accused; the published "Immediate safety comes first" meant the child and others at risk || **Human (100%, 1,722 words scanned)**, 16:05:58 |
| 145g-S8-v25-P19-anyoneatrisk (1658) | Human (weak) | "anyone at risk" || **Human (100%, 1,722)**, 16:06:03 |

145g (submitted 16:05:58 to 16:06:03 UTC): mine 2 of 2. "Keep everyone at risk safe first" is the reading both d5 logic checks gave the published "Immediate safety comes first", so it closes their AMBIGUOUS finding. The candidate is `cand-v26.json` (`joel-1505/build_v26.py`), the text 145g checked: 100% Human, 1,722 words scanned.


Joel's message of 20:21 UTC (`joel-2021/joel-20261007-2021.json`): the P28 cut approved ("p28 looks better now yes"), the H4 heading stays out, his new first paragraph for the last subsection (P23 with the published P26's point), his new P10, P18 "children", P22 "a commitment they make as adults", P25's last line shortened. v27 = v26 with those (`joel-2021/build_v27.py`).

Batch 146g (written 20:24 UTC by `date -u`, before the call; `joel-2021/v146.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 146g-S8-v27 (1746) | Mostly Human | his new P10 adds 70 words above the P13–P14 stretch, which has opened and closed with length changes far above it (138g, 143g); his paragraphs have passed alone || **Human (100%, 1,812 words scanned)**, 20:24:18 |
| 146g-S8-v27-P22make (1744) | Mostly Human | the same, with P22's fourth "as adults" dropped ("a commitment they make"): my approved suggestion doubled a phrase already in the sentence || **Human (100%, 1,810)**, 20:24:22 |


146g (submitted 20:24:18 to 20:24:22 UTC): mine 0 of 2. v27, with everything Joel approved at 20:21, reads 100% Human as a section, and so does the variant without P22's fourth "as adults". v27 goes in `HUMANIZED-SO-FAR.md`; the variant is a proposal.

