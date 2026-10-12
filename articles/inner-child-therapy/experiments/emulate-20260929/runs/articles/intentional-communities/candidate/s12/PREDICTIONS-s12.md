# Section 12 ("The Math of Absorption, and Who This Isn't For"): Pangram predictions and results

Predictions are written before each call (Human or AI, with the words that decide it). Results are from Pangram's web app (browser pane, tab "seed").

## The published section (baseline)

Batch 234g (written 01:12 UTC on 2026-10-12 by `date -u`, before the call; `v234.json`, parts in `pub-parts.json`): the published paragraphs, alone where they have 50 words or more, otherwise in runs, and the whole section. Stance ledger and preservation freeze: `STANCE-LEDGER-s12.md`.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 234g-H1P1P2 (88) | AI | "Modern life trains us to perform competence while hiding whatever might complicate the performance", "act surprised when nobody can sit through a conflict" | **AI (100%)**, 01:12:40 |
| 234g-P3P4 (85) | AI | "So the question isn't whether ... The practical question is", a three-part question, then "Some ... Some ... Some ... Most of us" | **AI (100%)**, 01:12:45 |
| 234g-P5P6P7 (75) | AI | "That does not make the community infinitely absorbent." alone as a paragraph; a definition paragraph | **AI (100%)**, 01:12:50 |
| 234g-P8P9 (64) | Human | "Good Lord." and the specific facts of his story | **Human (100%)**, 01:12:59 |
| 234g-P9 (57) | Human | the same | **Human (100%)**, 01:13:03 |
| 234g-P9P10 (99) | AI | P10's "the arithmetic is already visible", "I'm not speaking from a mountaintop" | **Mixed (42% AI: P10, "I could continue … mountaintop")**, 01:13:08 |
| 234g-P11P12 (79) | AI | "is therefore partly a resource question rather than a measure of compassion" | **AI (100%)**, 01:13:13 |
| 234g-P13P14 (67) | AI | "The difficult paradox is that", "The well does not become more understanding because the new member has a beautiful heart." | **AI (100%)**, 01:13:18 |
| 234g-P15 (63) | AI | a list of five kinds of people, "Pretending capacity is unlimited won't solve that.", "Even then, the power remains dangerous." | **AI (100%)**, 01:13:24 |
| 234g-P16L (94) | AI | a lead-in and a four-item list | **AI (100%)**, 01:13:29 |
| 234g-L4P17 (55) | AI | "That says nothing final about your worth. It describes timing." | **AI (100%)**, 01:13:33 |
| 234g-S12pub (679) | AI | most paragraphs above | **AI (100%, 687 words scanned)**, 01:13:39 |

Score for 234g, counted strictly: 11 of 12 (P9P10 came back Mixed, not AI); saying AI every time: 9 of 12. The published section reads 100% AI; only P9, his story, reads Human, alone and after P8. P10 is the AI part of P9P10.

## Candidate v1 (Emulate round a, with the meaning put back)

Emulate round a (laptop `emulate-runs/community-s12a`, two calls per unit, `emu/s12a-emu-all.json`) gave loose wording and many meaning shifts; v1 takes its looser phrasing and puts every preservation unit back (`fix-v1-parts.json`, `section-v1.md`). P8 and P9 stay as published. Gate round r1 (`review-r1/`): traces T1 to T5 all OK; cold reads S1 and S2 every paragraph OK; stance r1: "do some inner pl/ork" fixed to "do inner pl/ork", and "outside review" (published, kept) goes to Joel against his stated positions. Linter: REVIEW, no FAIL.

Batch 235g (written 01:37 UTC on 2026-10-12 by `date -u`, before the call; `v235.json`): each paragraph alone where it has 50 words, the short ones in runs, and the section.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 235g-H1P1aP2a (97) | AI | P2a's "Modern life trains us to look competent and hide whatever might complicate the act" still an aphorism; P1a's eight-item list | **AI (100%)**, 01:38:03 |
| 235g-P2aP3a (98) | AI | the same, then "isn't really the question. What matters in practice is" | **AI (100%)**, 01:38:06 |
| 235g-P3aP4a (93) | AI | "Some ... Some ... Some ... Most of us" | **AI (100%)**, 01:38:11 |
| 235g-P5a (51) | AI | "to listen, to be with someone through something, and to help people work through" (three) | **AI (100%)**, 01:38:21 |
| 235g-P5aP7a (89) | AI | the same, then a definition | **AI (100%)**, 01:38:26 |
| 235g-P7aP8P9 (102) | Human | P9's story and "Good Lord." carry it | **AI (100%)**, 01:38:30 |
| 235g-P9P10a (106) | Human | "I could go on and on", "the math is pretty clear by now", "not saying it from a mountaintop" | **Human (100%)**, 01:38:34 |
| 235g-P11aP12a (93) | AI | "partly a question of resources, not a measure of how compassionate it is" | **AI (100%)**, 01:38:39 |
| 235g-P13a (51) | AI | "It's a tough paradox." then a five-item list of chores | **AI (100%)**, 01:38:47 |
| 235g-P13aP14a (72) | AI | the same | **AI (100%)**, 01:38:51 |
| 235g-P15a (71) | AI | five kinds of people in a list | **AI (100%)**, 01:38:55 |
| 235g-P14aP15a (92) | AI | the same | **AI (100%)**, 01:39:00 |
| 235g-P16aL2aL3a (73) | Human | "Or if you want ...", "The same goes if you won't look at" | **AI (100%)**, 01:39:05 |
| 235g-L3aL4a (58) | Human | "way bigger than what you have to give", "It's about timing" | **AI (100%)**, 01:39:12 |
| 235g-L4aP17a (70) | AI | "A humane way of taking in members should be able to say" | **AI (100%)**, 01:39:17 |
| 235g-S12v1 (771) | AI | the AI paragraphs above | **AI (100%, 794 words scanned)**, 01:39:22 |

Score for 235g: 13 of 16; saying AI every time: 15 of 16. v1 reads 100% AI everywhere except P9 with P10a. Taking Emulate's looser words and putting the published structure back kept the published shapes: P7a pulls even P9 to AI (P7aP8P9). Next: check Emulate's own outputs, then fix meaning one change at a time on the ones that pass (the gate: "A draft that passed is the base").

## Emulate round a, as returned (no meaning fixes yet)

Batch 236g (written 01:40 UTC on 2026-10-12 by `date -u`, before the call; `v236.json`, texts in `emu-a-parts.json`): each of Emulate's sixteen outputs alone. They carry meaning shifts (`review-r1` notes below), so this only finds the shapes that read Human to build from.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 236g-E1A (79) | Human | "If I asked someone to sit down with me", "they'd probably politely decline", "And that's okay." | **Human (100%)**, 01:40:46 |
| 236g-E1B (103) | Human | "The strange thing is", "This does not surprise me", "put on a show" | **Human (100%)**, 01:40:51 |
| 236g-E2A (100) | Human | a question in quotes, "him or her", "Most of us are all of these" | **Human (100%)**, 01:40:55 |
| 236g-E2B (88) | AI | "Some people ... Some people ... Some people ..." | **Human (100%)**, 01:41:04 |
| 236g-E3A (86) | Human | "In other words, there's a lot of peer counseling going on.", "But it's not infinite." | **Human (100%)**, 01:41:09 |
| 236g-E3B (77) | Human | "a kind of see-saw relationship", "All of use have both." (typo) | **Human (100%)**, 01:41:14 |
| 236g-E4A (62) | Human | "I could go on and on", "quite apparent to most of the readers here" | **Human (100%)**, 01:41:18 |
| 236g-E4B (51) | Human | "ones self" twice, "One has to" | **Human (100%)**, 01:41:23 |
| 236g-E5A (75) | Human | "The problem is that", "crisis mode", "--" | **Human (100%)**, 01:41:30 |
| 236g-E5B (93) | Human | "it's time", "effected", "crisis/need" | **Human (100%)**, 01:41:34 |
| 236g-E6A (113) | Human | "This is one of the tough issues.", "someone has to ... someone has to" | **Human (100%)**, 01:41:39 |
| 236g-E6B (99) | Human | "Whether there are eight people in the community or eight hundred" | **Human (100%)**, 01:41:44 |
| 236g-E7A (98) | Human | "or people who are just…well, simply for basically any group" | **AI (100%)**, 01:41:48 |
| 236g-E7B (89) | Human | "I don't know." after the list, "and all of that" | **Human (100%)**, 01:42:07 |
| 236g-E8A (161) | Human | parentheticals, "etc.", "the group that founded this site" | **Human (100%)**, 01:42:12 |
| 236g-E8B (109) | Human | "you're probably not worthless", run-ons | **Human (100%)**, 01:42:16 |

Score for 236g: 14 of 16 (E2B Human where I said AI; E7A AI where I said Human); saying AI every time: 1 of 16. Every Emulate output reads Human but E7A. They are the base: v2 keeps their shapes and puts the meaning back one fix at a time.

## v2: Emulate's passing outputs, with the meaning put back

`fix-v2-parts.json`: each unit is the Emulate output that read Human (E1B, E2A, E3A, E5A, E6B, E7B, E8A), with the fixes the preservation units need (each fix noted in `DRAFTS-v2.md` once the results are in). P9 is published, P10a is v1's (Human with P9).

Batch 237g (written 01:45 UTC on 2026-10-12 by `date -u`, before the call; `v237.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 237g-P1mP2m (119) | Human | E1B's "The strange thing is", "This does not surprise me", "hide ourselves in our lives"; my completion "then they act surprised" | **AI (100%)**, 01:45:33 |
| 237g-P2m (73) | Human | the same | **Human (100%)**, 01:45:37 |
| 237g-H1P1mP2m (128) | Human | the same, with the heading | **AI (100%)**, 01:45:41 |
| 237g-P3m (54) | Human | E2A's quoted questions, "he or she", "him or her" | **Human (100%)**, 01:45:50 |
| 237g-P4m (50) | Human | E2A's semicolon run-on, "Most of us are all of these"; my "and need care more than responsibility" | **Human (100%)**, 01:45:55 |
| 237g-P3mP4m (104) | Human | the same | **Human (100%)**, 01:46:00 |
| 237g-P5mP6mP7mP8m (114) | Human | E3A's "In other words, there's a lot of peer counseling going on", "But it's not infinite."; risk: my "attention, steadiness and practical skill" | **Human (100%)**, 01:46:04 |
| 237g-P7m (53) | Human | "I'm going to use the phrase"; risk: the same list | **Human (100%)**, 01:46:11 |
| 237g-P7mP8mP9 (121) | Human | P9 | **Human (100%)**, 01:46:16 |
| 237g-P11m (69) | Human | "The problem is that", "crisis mode", "However,"; risk: my first sentence, the published one | **Human (100%)**, 01:46:21 |
| 237g-P11mP12m (99) | Human | "--" and the question | **Human (100%)**, 01:46:25 |
| 237g-P13m (74) | Human | E6B's "There is a difficult paradox to consider.", "The water well doesn't care" | **Human (100%)**, 01:46:30 |
| 237g-P13mP14m (95) | Human | "and some skill to contribute, and a willingness to learn" | **Human (100%)**, 01:46:34 |
| 237g-P15m (88) | AI | five changes to E7B, and "And even then, the power is dangerous." | **Human (100%)**, 01:46:42 |
| 237g-P15mP16mL1m (129) | AI | P15m | **Mixed (30% AI: P16m and L1m)**, 01:46:47 |
| 237g-U8m (154) | Human | E8A's parentheticals and "etc." | **AI (100%)**, 01:46:51 |
| 237g-S12v2 (888) | Human | most units are Emulate's shapes | **Mixed (52% AI: from P10a to the end, 479 words)**, 01:46:56 |

Score for 237g: 11 of 17 (P1mP2m and H1P1mP2m AI where I said Human; P15m Human where I said AI; P15mP16mL1m Mixed; U8m AI; the section Mixed). Saying AI every time: 2 of 17. Every unit passes now but P1 and the list. P2m passes alone, so P1m is the AI part of P1mP2m; E8A passed, so one of my four fixes to the list flipped it (P15mP16mL1m points at L1m).

Batch 238g (written 01:48 UTC on 2026-10-12 by `date -u`, before the call; `v238.json`): P1 variants with P2m (which passes alone), and the list (E8A) with one fix at a time.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 238g-P1n1P2m (122) | Human | E1B's own P1 ("ways of responding when people are trying to get away"): if this passes, my "what happens when somebody wants to leave" flipped P1m | **AI (100%)**, 01:48:40 |
| 238g-P1n2P2m (120) | AI | "what to do when somebody wants to leave" is still the plain published shape at the end of the list | **AI (100%)**, 01:48:44 |
| 238g-P1n4P2m (118) | Human | "here:", "Strangely enough", "smart adults" | **AI (100%)**, 01:48:49 |
| 238g-U8a (147) | Human | E8A with only L1's parenthetical replaced ("A founding group shouldn't pretend it can give you those.") | **Human (100%)**, 01:48:58 |
| 238g-U8b (154) | AI | L1 "running from some crisis right now", "(It's good that some groups can provide that, but ...)" | **Human (100%)**, 01:49:03 |
| 238g-U8c (164) | Human | E8A with only "it's about timing" added | **Human (100%)**, 01:49:07 |
| 238g-U8d (164) | Human | E8A with only P17 fixed ("There should be ways ... like saying") | **Human (100%)**, 01:49:12 |
| 238g-U8e (160) | AI | all three fixes | **Human (100%)**, 01:49:16 |

Score for 238g: 5 of 8 (P1n1P2m and P1n4P2m AI where I said Human; U8b and U8e Human where I said AI). Every list variant passes, all three fixes together too (U8e), so U8m's L1m or P17m wording was the trouble, not the fixes as such. Every P1 with P2m reads AI, E1B's own P1 included: the completed P2 sits badly after any P1, though P2m passes alone. Next: Emulate round b on P1 and P2 (round a cut both outputs off).

Emulate round b (laptop `emulate-runs/community-s12b`, `emu/s12b-emu-all.json`): four more versions of P1 and P2, all cut off again, with "or ... or ..." lists and an eight-fold "Talk to me about"; nothing usable whole. u1b2-emuA's "appoint a sub-committee, or just hit block" is borrowed below.

Batch 239g (written 01:52 UTC on 2026-10-12 by `date -u`, before the call; `v239.json`): P1 with the heading, P2 completions with E1B's own P2 start, the list's parts in runs, and the section with the list fixed (v3x).

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 239g-H1P1n1 (57) | Human | E1B's P1 with the heading | **AI (100%)**, 01:54:17 |
| 239g-H1P1m (55) | AI | the published "what happens when somebody wants to leave" | **AI (100%)**, 01:54:21 |
| 239g-P1n1P2a1 (115) | Human | E1B's P2 continued in its own words ("even when people try to deal with discomfort or conflict") | **AI (100%)**, 01:54:26 |
| 239g-P1n1P2a2 (113) | AI | "then our institutions act surprised when nobody can sit through a conflict" is the published shape | **AI (100%)**, 01:54:35 |
| 239g-P1n1P2a4 (117) | Human | "all anyone knows how to do is appoint a sub-committee or just hit block" | **AI (100%)**, 01:54:39 |
| 239g-P1mP2a2 (111) | AI | the same two published shapes | **AI (100%)**, 01:54:44 |
| 239g-P1mP2a4 (115) | Human | "just hit block" | **AI (100%)**, 01:54:49 |
| 239g-L4v1 (56) | Human | "far outstrips your ability to bring in a resource", the parenthetical | **Human (100%)**, 01:54:53 |
| 239g-P15mP16eL1v2 (129) | Human | P15m passes; L1v2 in the list that passed | **Human (100%)**, 01:55:03 |
| 239g-L4v1P17v1 (88) | Human | both from the list that passed | **Human (100%)**, 01:55:07 |
| 239g-S12v3x (880) | Mixed | P1 and P2 as in v2 still read AI together | **Mixed (45% AI: "body else. So when I say someone mi … oss lots of relationships", P10a's end into P11m, 96w; "bers is less. Even with only eight … or “in another role,” or", P13m's second sentence to P17v1, 327w)**, 01:55:12 |

Score for 239g: 7 of 11 (H1P1n1, P1n1P2a1, P1n1P2a4 and P1mP2a4 AI where I said Human); saying AI every time: 7 of 11. P1 is the AI part: E1B's P1 reads AI with only the heading, and no ending of P2 rescues it. Every list run passes. The section's AI windows cross paragraph ends: P10a's last sentence into P11m, and P13m's second sentence through the list, though each run inside them passes.

Batch 240g (written 01:59 UTC on 2026-10-12 by `date -u`, before the call; `v240.json`, new parts in `fix-v3-parts.json`): Emulate round b's one whole P1 (u1b2-emuB, "jealousy or God or death or ..."), as it came and with the meaning put back one change at a time (the leaving item; "Most" to "Many"; the published "Many perfectly intelligent adults"), and the runs under the section's two AI windows.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 240g-H1P1o1 (61) | Human | the "or ... or ..." run, "Most people, intelligent, well adjusted in their thirties or forties" | **Human (100%)**, 01:59:28 |
| 240g-H1P1o3 (58) | Human | the same with "what happens when somebody wants to leave" | **AI (100%)**, 01:59:32 |
| 240g-H1P1o5 (58) | Human | the same with "Many people" | **AI (100%)**, 01:59:37 |
| 240g-H1P1o2 (52) | AI | "Many perfectly intelligent adults would rather talk for six hours about solar panels" is the published sentence | **AI (100%)**, 01:59:46 |
| 240g-P1o3P2m (122) | Human | P2m passes alone, and the "or" run breaks the list shape every earlier P1 had | **AI (100%)**, 01:59:51 |
| 240g-P1o2P2m (116) | AI | the published sentence again | **AI (100%)**, 01:59:56 |
| 240g-P10aP11m (118) | AI | the first window: "I'm not saying it from a mountaintop" into "A group can only absorb as much need ..." and "The problem is that ... However, ..." | **AI (100%)**, 02:00:01 |
| 240g-P14mP15m (109) | AI | P15m's two lists after P14m's "and ... and" | **Human (100%)**, 02:00:05 |
| 240g-P13mP14mP15m (183) | AI | three lists in a row (P13m's five chores, P15m's five groups and three steps) | **AI (100%)**, 02:00:13 |
| 240g-W2 (343) | AI | the second window's whole stretch, lists all the way | **AI (100%)**, 02:00:20 |

Score for 240g: 6 of 10 (H1P1o3, H1P1o5 and P1o3P2m AI where I said Human; P14mP15m Human where I said AI); saying AI every time: 8 of 10. Emulate's own P1 passes with the heading, and the one change that flips it is the leaving item: "what happens when somebody wants to leave", the published words, reads AI in that sentence where "a time when somebody they loved wanted to leave them" passed. P13m, P14m and P15m pass in every pair but read AI as three; P10a with P11m reads AI, though each passes beside its other neighbor.

Batch 241g (written 02:03 UTC on 2026-10-12 by `date -u`, before the call; `v241.json`, new parts in `fix-v3-parts.json`): P1o1 (Emulate's P1, which passed) with one change each, other wordings for the leaving item that keep the article's meaning (leaving the community: its own list "Membership, land, resources, governance, children, leaving, etc." and "Good people leave for good reasons"), and for the people; then P11 with its first sentence, the published one, moved, merged, or left out (a test only: U19 stays in the section), and the three-paragraph stretch with one change each.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 241g-H1P1p1 (59) | Human | "what to do when somebody wants to leave" is Emulate's own wording from round b | **AI (100%)**, 02:04:02 |
| 241g-H1P1p2 (55) | Human | "or somebody wanting to leave" ends the "or" run on a short noun phrase | **Human (100%)**, 02:04:08 |
| 241g-H1P1p3 (59) | AI | "what we do when somebody wants to leave" is close to the published "what happens when" | **AI (100%)**, 02:04:11 |
| 241g-H1P1p4 (61) | Human | only "Most" to "Many" | **Human (100%)**, 02:04:18 |
| 241g-H1P1p5 (57) | Human | "intelligent and well adjusted", the age range gone | **Human (100%)**, 02:04:23 |
| 241g-P10aP11r1 (118) | Human | the published sentence comes last, after the example | **Human (100%)**, 02:04:28 |
| 241g-P10aP11r3 (118) | AI | "The problem is that a group can only absorb ..." keeps the thesis right after the mountaintop line | **AI (100%)**, 02:04:32 |
| 241g-P10aP11r4 (102) | Human | no thesis sentence at all (a test) | **Human (100%)**, 02:04:37 |
| 241g-P13n1P14mP15m (186) | AI | the three lists stay; one clause back to Emulate's "Whether there are eight people ... or eight hundred" | **Human (100%)**, 02:04:44 |
| 241g-P13mP14mP15n2 (184) | Human | P15's five groups now four items, "people who aren't very articulate or don't have the language of therapy" | **Human (100%)**, 02:04:49 |

Score for 241g: 8 of 10 (H1P1p1 AI where I said Human; P13n1P14mP15m Human where I said AI); saying AI every time: 3 of 10. Of the leaving wordings only "or somebody wanting to leave" passes; "what to do when" and "what we do when" read AI like the published "what happens when". Both fixes to the people pass alone ("Many"; the age range gone). P11 passes beside P10a with its first sentence moved to the end, and fails with it merged into "The problem is that". The three-paragraph stretch passes with either one change: Emulate's "Whether there are eight people ... or eight hundred", or P15's five groups in four items.

Emulate round c (laptop `emulate-runs/community-s12c`; P1 alone is 33 words, under Emulate's 40-word floor, so the heading went with it): four P1s that turn the meaning round ("Do not discuss: ...", "can't talk about their jealousy") or swell it; kept for the record, none needed yet.

Batch 242g (written 02:06 UTC on 2026-10-12 by `date -u`, before the call; `v242.json`): the passing fixes together. P1q2 is Emulate's P1 with three meaning fixes ("somebody wanting to leave", "Many", "intelligent and well adjusted"); P11r1 has the published first sentence last; P15n2 has the five groups in four items. Section v3 (`S12v3`) is v3x with those three.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 242g-H1P1q1 (55) | Human | the leaving fix with "Many"; each passed alone | **Human (100%)**, 02:06:33 |
| 242g-H1P1q2 (51) | Human | and the age range gone, which also passed alone | **Human (100%)**, 02:06:37 |
| 242g-P1q2P2m (115) | Human | P2m passes alone, and this P1 passes with the heading; every earlier pair had a P1 that failed with it | **AI (100%)**, 02:06:41 |
| 242g-P11r1 (69) | Human | P11m's sentences, the first one moved to the end | **Human (100%)**, 02:06:49 |
| 242g-P11r1P12m (99) | Human | P11mP12m passed; now the thesis sits next to "So it's partly a problem of resources" (two abstract lines in a row) | **Human (100%)**, 02:06:54 |
| 242g-P15n2 (89) | Human | P15m passed alone; one list item fewer | **Human (100%)**, 02:06:58 |
| 242g-P15n2P16eL1v2 (138) | Human | P15mP16eL1v2 passed | **Human (100%)**, 02:07:03 |
| 242g-W2b (344) | Human | the stretch that read AI as W2, with P15n2 | **AI (100%)**, 02:07:07 |
| 242g-S12v3 (891) | Human | every stretch under v3x's two AI windows passes now | **Mixed (11% AI, 921 words: "bers is less. Even with only eight … how beautiful a new membe", P13m's third and fourth sentences, 43w; "ce for it right now. (This doesn’t … or “in another role,” or", L4v1's parenthesis into P17v1, 64w)**, 02:07:15 |

Score for 242g: 6 of 9 (P1q2P2m and W2b AI, the section Mixed, where I said Human); saying AI every time: 2 of 9. The section went from 45% to 11% AI: the window over P10a and P11 is gone, and the one over P1 and P2 passes in the section though P1q2 with P2m reads AI as a pair (P1q2 is 43 words, so its own check is with the heading: 52 words, Human). Left: P13m's "Even with only eight people in the community, someone still has to ..." (my fix of Emulate's "Whether there are eight people in the community or eight hundred", which passed in the three-paragraph run), and the stretch from L4v1's parenthesis into P17v1's three options.

Batch 243g (written 02:09 UTC on 2026-10-12 by `date -u`, before the call; `v243.json`): P13's eight people said two other ways (Emulate's "Whether ... or" with the section's own "eighty"; "Even if there are only eight"), P17 with Emulate's "There are probably ways" and the three options kept, P1q2 with E1B's P2 shape, and the section with one or two changes from v3.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 243g-P13n5 (76) | Human | Emulate's "Whether there are eight people in the community or ..." | **Human (100%)**, 02:09:41 |
| 243g-P13n6 (76) | Human | "Even if there are only eight people" | **Human (100%)**, 02:09:45 |
| 243g-P13n5P14m (97) | Human | P13mP14m passed | **Human (100%)**, 02:09:49 |
| 243g-P13n6P14m (97) | Human | the same | **Human (100%)**, 02:09:56 |
| 243g-L4v1P17v2 (78) | Human | L4v1P17v1 passed; "There are probably ways" is Emulate's | **Human (100%)**, 02:10:01 |
| 243g-P1q2P2a4 (112) | AI | P1q2 with P2m read AI; P2a4 has the same published bones | **Human (100%)**, 02:10:06 |
| 243g-S12v4a (893) | Mixed | P13's window gone; the L4-to-P17 window stays | **Human (100%, 923 words scanned)**, 02:10:11 |
| 243g-S12v4b (893) | Human | both windows' changes | **Human (100%, 923 words)**, 02:10:15 |
| 243g-S12v4c (893) | Human | the same with "Even if there are only eight" | **Human (100%, 923 words)**, 02:10:23 |

Score for 243g: 7 of 9 (P1q2P2a4 and S12v4a Human where I said AI and Mixed); saying AI every time: 0 of 9. The section passes three ways: with P13's eight people said either new way, and with P17 as v1 or v2. P1q2 passes beside E1B's P2 shape, where it failed beside P2m: P2m's ending is the published one ("act surprised when nobody can sit through a conflict without appointing a subcommittee or blocking somebody").

Batch 244g (written 02:11 UTC on 2026-10-12 by `date -u`, before the call; `v244.json`): the meanings I'd rather keep, together. P13n6 ("Even if there are only eight people", closest to the published "Eight people still need ...") with P17v1 ("There should be ways", the published "should"); and P2c, which is P2m with Emulate's ending ("all anyone knows how to do is appoint a subcommittee or just hit block") in place of the published one, so P1 can pass beside a paragraph too.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 244g-P2c (79) | Human | P2m passed alone; only the ending changes, to Emulate's | **Human (100%)**, 02:11:44 |
| 244g-P1q2P2c (121) | Human | P1q2 passed beside P2a4, which has this ending | **AI (100%)**, 02:11:48 |
| 244g-S12v4d (893) | Human | each change passed in a section already (P13n6 in v4c, P17v1 in v4a) | **Mostly Human (5% AI, 923 words: "bers is less. Even if there are onl … how beautiful a new membe", P13n6's third and fourth sentences, 45w)**, 02:11:53 |
| 244g-S12v4e (899) | Human | the same with P2c | **Mostly Human (9% AI, 929 words: "k. So instead of asking \"Is this p … engage in self-examinati", P2c's end into P3m, 40w; and the same P13n6 window, 45w)**, 02:12:00 |

Score for 244g: 1 of 4 (P1q2P2c AI, both sections Mostly Human, where I said Human); saying AI every time: 1 of 4. P13n6 is borderline: its window passed in v4c and fails in v4d, where only P17's wording differs. P2c passes alone but not beside P1q2, and in the section its end pulls P3m's first lines to AI.

**Candidate v4 = S12v4a** (Human, 100%, 923 words, 243g): P1q2, P2m, P3m, P4m, the chart, P5m to P8m, P9 as published, P10a, P11r1, P12m, P13n5, P14m, P15n2, P16e, L1v2, L2e, L3e, L4v1, P17v1. Of the passing sections it keeps the most meaning: P17's "should" (v4b and v4c have "There are probably ways"). P13n5's "Whether there are eight people in the community or eighty" goes to the stance check against the published "Eight people still need ...". Every paragraph passes alone or in a run with a neighbor that passes (P1q2, 43 words, with the heading, 52 words), and the section passes.

## Gate round r2 on v4, and its fixes

Gate round r2 (`review-r2/`, `DISPOSITIONS-r2.md`): five traces, two cold reads, the stance check and the linter on v4. The linter fails v4 twice: P1q2's "jealousy or God or death or ..." is Joel's O14 ban (Emulate's "and ... and" trick: "use commas and keep the list's own 'or'"), and five paragraphs open with "You" (B13). The fixes below are one change each from v4, as the reviewers asked. P1 with commas is 36 to 41 words, so it is checked beside P2.

Batch 245g (written 02:34 UTC on 2026-10-12 by `date -u`, before the call; `v245.json`, new parts in `fix-v4-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 245g-P1t1P2m (108) | AI | a comma list (every earlier one read AI), and P2m's published ending, which failed beside P1q2 | **AI (100%)**, 02:35:16 |
| 245g-P1t2P2m (109) | AI | the same, with Emulate's "Many perfectly intelligent grownups would rather sit around" | **AI (100%)**, 02:35:20 |
| 245g-P1t3P2m (107) | AI | the same | **AI (100%)**, 02:35:24 |
| 245g-P1t5P2m (109) | AI | "I'm asking" | **AI (100%)**, 02:35:31 |
| 245g-P1t6P2m (114) | AI | P1 turned round ("would rather ... than talk about ..."), still a comma list | **AI (100%)**, 02:35:36 |
| 245g-H1P1t6 (50) | AI | the comma list | **Human (100%, 51 words)**, 02:35:40 |
| 245g-P2f (77) | Human | P2c with "our institutions" moved back to E1B's place; P2c passed alone | **Mixed (46% AI: its last sentence, "We have been encouraged to be narr … mittee or just hit block.", 36w)**, 02:35:45 |
| 245g-P1t2P2a4 (106) | Human | P2a4 passed beside P1q2 | **AI (100%)**, 02:35:50 |
| 245g-P1t2P2f (113) | AI | P2f carries P2m's meaning fixes, which failed beside P1q2 | **AI (100%)**, 02:35:57 |
| 245g-P3n1 (52) | Human | one phrase: "the practical questions to ask are" | **Human (100%)**, 02:36:01 |
| 245g-P3n2 (53) | Human | "some very practical questions to ask are" | **Human (100%)**, 02:36:06 |
| 245g-P5n3 (51) | Human | "being there for each other" added (a list of three, which the published has) | **Human (100%)**, 02:36:10 |
| 245g-P5n3P6mP7n1P8m (120) | Human | the run that passed, with two fixes | **Human (100%)**, 02:36:15 |
| 245g-P7n1 (54) | AI | the published four-item list back in ("attention, steadiness, skill and practical capacity") | **Human (100%)**, 02:36:24 |
| 245g-P10aP11s1 (119) | Human | one word, "practical" | **Human (100%)**, 02:36:29 |
| 245g-P11s1 (70) | Human | the same | **Human (100%)**, 02:36:34 |
| 245g-P11s1P12n1 (100) | Human | "the people they've promised to support" | **Human (100%)**, 02:36:39 |
| 245g-P11r1P12n1 (99) | Human | the same with P11r1 | **Human (100%)**, 02:36:43 |
| 245g-P13n5P14n1 (99) | Human | "So early on", "acute need" | **Human (100%)**, 02:36:50 |
| 245g-P13n5P14n2 (98) | Human | "So early on" | **Human (100%)**, 02:36:55 |
| 245g-P13n5P14n3 (98) | Human | "acute need" | **Human (100%)**, 02:37:03 |
| 245g-U8w (151) | Human | three list fixes: the lead-in reordered, L1's added sentence cut, "a bit" cut | **Human (100%)**, 02:37:04 |
| 245g-P15n2P16fL1w1 (131) | Human | the run that passed, with two of those fixes | **Human (100%)**, 02:37:08 |
| 245g-L4w1 (51) | Human | "a bit" cut | **Human (100%)**, 02:37:16 |
| 245g-L4w1P17v1 (76) | Human | the same | **Human (100%)**, 02:37:20 |
| 245g-S12v5 (885) | Mixed | P1t2 with P2m, and nine fixes at once shift every window | **Mixed (45% AI, 915 words: "body else. So when I say someone mi … members have free resour", P10a's end to P11s1's end, 97w; "bers is less. Whether there are eig … or “in another role,” or", P13n5's second sentence to P17v1, 323w)**, 02:37:25 |

Score for 245g: 22 of 26 (H1P1t6 Human where I said AI; P2f Mixed, P1t2P2a4 AI, P7n1 Human where I said otherwise); saying AI every time: 7 of 26. Every comma-list P1 reads AI beside P2m; P1t6, the list turned round ("would rather sit around ... than talk about ..."), passes with the heading at 51 words, which is its check. Every one-change fix passes alone and in its run. The section with all of them (v5) is back to the two windows v3x had, so the next batch adds them in groups.

Batch 246g (written 02:38 UTC on 2026-10-12 by `date -u`, before the call; `v246.json`): the section from v4 with the fixes in groups. v6a has the ones the linter and the stance check require (P1t6 for the O14 ban, P16f for B13, P3n1, L1w1, L4w1); v6b adds the trace fixes before P9 (P5n3, P7n1); v6c the ones in P11 and P12 (P11s1, P12n1); v6d the one in P14 (P14n1).

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 246g-S12v6a (881) | Human | v4 passed; these five pass alone and in their runs, and none sits in v5's first window | **Mostly Human (5% AI, 910 words: "bers is less. Whether there are eig … how beautiful a new membe", P13n5's third and fourth sentences, 45w)**, 02:39:03 |
| 246g-S12v6b (887) | Human | P5n3 and P7n1 are before both windows | **Mixed (11% AI, 916 words: the same P13 window, 45w; "ce for it right now. (This doesn’t … or “in another role,” or", L4w1's parenthesis into P17v1, 62w)**, 02:39:06 |
| 246g-S12v6c (882) | Mixed | P11s1 was in v5's first window | **Mixed (37% AI, 912 words: P10a's end to P11s1's end, 97w; the P13 window, 45w; "– I don’t know. It’s not going to b … or “in another role,” or", P15n2's second half to P17v1, 203w)**, 02:39:12 |
| 246g-S12v6d (883) | Mixed | P14n1 sits in v5's second window | **Mixed (11% AI, 912 words: the P13 window, 45w; the L4-to-P17 window, 62w)**, 02:39:19 |

Score for 246g: 0 of 4 (v6a Mostly Human, v6b Mixed, where I said Human; v6c and v6d Mixed as I said, but on other windows than I gave): saying AI every time: 0 of 4. P13n5's third and fourth sentences read AI whenever a window holds just them (45 words); in v4 the windows fell elsewhere. The L4-to-P17 stretch does the same when the text before it moves. P11s1's "practical roles" brings back v5's first window.

Batch 247g (written 02:41 UTC on 2026-10-12 by `date -u`, before the call; `v247.json`): v6a with P13's last two sentences closer to Emulate's E6B, which passed: "someone's heart" (v7a), also "fix the cars" (v7b), and E6B's own P13 with "eight hundred" (v7c); v7d is v7a with the trace fixes to P7 and P12.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 247g-S12v7a (879) | Human | one of my two fixes in that window undone | **Mixed (20% AI, 908 words: "body else. So when I say someone mi … oss lots of relationships", P10a's end into P11r1, 80w; "bers is less. Whether there are eig … care how beautiful someon", P13o2's last two sentences, 43w; the L4-to-P17 window, 62w)**, 02:41:22 |
| 247g-S12v7b (879) | Human | both undone | **Mostly Human (7% AI, 908 words: the L4-to-P17 window, "ce for it right now. (This doesn’t … or “in another role,” or", 62w)**, 02:41:27 |
| 247g-S12v7c (880) | Human | E6B's own sentences | **Mostly Human (7% AI, 909 words: the same L4-to-P17 window, 62w)**, 02:41:32 |
| 247g-S12v7d (880) | Mixed | two more changes before the window shift it again | **Mixed (33% AI, 910 words: P10a's end to P11r1's end, 96w; P13o2's last two sentences, 43w; P15n2's second sentence, 44w; ", legal aid, etc. (A founding group … or “in another role,” or", L1w1's end to P17v1, 125w)**, 02:41:39 |

Score for 247g: 0 of 4 (v7b and v7c Mostly Human, v7a Mixed, where I said Human; v7d Mixed as I said); saying AI every time: 0 of 4. A change late in the section moved a window early in it (v7a changed only P13, and P10a's end into P11r1 failed again), so the windows depend on the whole length, not on what comes before them. With E6B's "fix the cars" and "someone's heart" (v7b, v7c) the P13 window passes; the L4-to-P17 window is left. Next: test the windows' own stretches alone, to find wordings that pass wherever a window falls.

Batch 248g (written 02:43 UTC on 2026-10-12 by `date -u`, before the call; `v248.json`, parts in `fix-w-parts.json`): the three windows' stretches alone, as near as 50 words allow: P13 without its first sentence; L4's parenthesis with P17; P10a's last sentence with P11. If they read as the section's windows did, they are a cheap test for wordings.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 248g-W13n5 (69) | AI | the window that failed in v6a to v6d | **Human (100%)**, 02:43:17 |
| 248g-W13o1 (67) | Human | "fix the cars", "someone's heart": passed in v7b | **Human (100%)**, 02:43:21 |
| 248g-W13o2 (67) | AI | "someone's heart" only: failed in v7a | **Human (100%)**, 02:43:26 |
| 248g-W13o4 (68) | Human | E6B's own: passed in v7c | **Human (100%)**, 02:43:33 |
| 248g-W17a (58) | AI | L4w1's parenthesis and P17v1: failed in v7b and v7c | **Human (100%)**, 02:43:38 |
| 248g-W17b (60) | Human | with "a bit" (L4v1), as in v4, which passed | **Human (100%)**, 02:43:42 |
| 248g-W17c (58) | Human | "There are probably ways" (P17v2), as in v4b and v4c | **Human (100%)**, 02:43:47 |
| 248g-W17d (59) | AI | "build your resources back up" | **Human (100%)**, 02:43:52 |
| 248g-W17f (58) | Human | the parenthesis in three short sentences | **Human (100%)**, 02:43:59 |
| 248g-W11r1 (94) | AI | P10a's last sentence into P11r1, which failed in v7a | **Human (100%)**, 02:44:03 |
| 248g-W11s1 (95) | AI | the same with "practical roles", which failed in v5 and v6c | **Human (100%)**, 02:44:08 |

Score for 248g: 5 of 11 (W13n5, W13o2, W17a, W17d, W11r1 and W11s1 Human where I said AI); saying AI every time: 0 of 11. Every stretch passes alone, the ones that failed as section windows too. So a window's result in the section depends on more than its own words, and the stretches alone can't stand in for it: only the section can be the test. The section's windows move whenever its length changes, so the next batch tries v7b (one window short of passing) with the trace fixes in several combinations, all of which keep the meaning.

Batch 249g (written 02:45 UTC on 2026-10-12 by `date -u`, before the call; `v249.json`): v7b (P13o1) and v7c (E6B's P13) with the trace fixes, alone and together: P5n3 (being there for each other), P7n1 (skill and practical capacity), P11s1 (practical roles), P12n1 (promised support), P14n1 ("So", "acute").

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 249g-S12v8a (880) | Mixed | v7b's L4-to-P17 window failed at most lengths so far | **Mixed (27% AI, 910 words: P10a's end to P11's end, 96w; P13o1's last two sentences, 43w; "n replace those.) You want all of … or “in another role,” or", L1w1's end to P17v1, 115w)**, 02:45:38 |
| 249g-S12v8b (887) | Mixed | the same | **Mixed (27% AI, 917 words: the same three windows)**, 02:45:42 |
| 249g-S12v8c (888) | Mixed | P11s1 brought back the first window twice | **Mixed (44% AI, 918 words: P10a's end to P11s1's end, 97w; P13o1's second sentence to P17v1, 321w)**, 02:45:47 |
| 249g-S12v8d (881) | Mixed | as v8a | **Mostly Human (7% AI, 910 words: the L4-to-P17 window, 62w)**, 02:45:54 |
| 249g-S12v8e (879) | Mixed | as v8a | **Mixed (21% AI, 909 words: P10a's end into P11r1, 80w; L1w1's end to P17v1, 115w)**, 02:45:59 |
| 249g-S12v8f (880) | Mixed | as v8a | **Mostly Human (7% AI, 909 words: the L4-to-P17 window, 62w)**, 02:46:03 |
| 249g-S12v8g (888) | Mixed | as v8a | **Mixed (30% AI, 918 words: P10a's end to P11's end, 96w; P13o4's second sentence to P14n1, 67w; L1w1's end to P17v1, 125w)**, 02:46:08 |
| 249g-S12v8h (889) | Mixed | as v8c | **Mixed (45% AI, 919 words: P10a's end to P11s1's end, 97w; P13o4's second sentence to P17v1, 322w)**, 02:46:13 |

Score for 249g: 6 of 8 counted strictly (all eight fail as I said; v8d and v8f came back Mostly Human, not Mixed); saying AI every time: 0 of 8. Every variant with P12n1 ("the people they've promised to support") brings back the window over P10a's end and P11, and P11s1 does too; P7n1 and P14n1 change nothing (v8d, v8f: the same 7% window as v7b). The end of the section, L4's parenthesis into P17, keeps failing. In v4, which passed, the end had P16e, L1v2 and L4v1; the fixes there (P16f for B13, L1w1, L4w1) are needed, so the next batch tries other wordings of them on v7b with P7n1 and P14n1 (B9).

Batch 250g (written 02:47 UTC on 2026-10-12 by `date -u`, before the call; `v250.json`): B9 = v7b with P7n1 and P14n1 (both neutral in 249g), and other wordings at the end, each keeping the meaning the reviewers asked for: L1w2 "(A founding group shouldn't pretend it can give you those.)" (L1w1 is the published sentence almost word for word); L4w5 "so you can build up your resources first"; L4w3 the parenthesis in short sentences; P17v8 "There should be some way"; and P5n3 ("being there for each other") on its own.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 250g-S12v9 (882) | Mixed | v8d and v8f each failed on the end window | **Mostly Human (10% AI, 911 words: "nflict, care, etc. You’re not will … or “in another role,” or", L2e's end to P17v1, 94w)**, 02:48:14 |
| 250g-S12v9a (883) | Human | the published sentence out of the end | **Human (100%, "Human Written", 912 words)**, 02:48:19 |
| 250g-S12v9b (884) | Human | the same, with "first" | **Mostly Human (7% AI, 913 words: the L4-to-P17 window, 63w)**, 02:48:23 |
| 250g-S12v9c (883) | Mixed | "first" alone | **Mostly Human (7% AI, 912 words: the L4-to-P17 window, 63w)**, 02:48:30 |
| 250g-S12v9d (882) | Mixed | short sentences alone | **Mostly Human (10% AI, 911 words: L2e's end to P17v1, 94w)**, 02:48:34 |
| 250g-S12v9e (883) | Mixed | "some way" alone | **Mixed (21% AI, 912 words: P10a's end into P11r1, 80w; L1w1's end to P17v8, 116w)**, 02:48:39 |
| 250g-S12v9f (884) | Human | L1w2 with "some way" | **Mostly Human (7% AI, 913 words: the L4-to-P17 window, 63w)**, 02:48:44 |
| 250g-S12v9g (887) | Mixed | P5n3 changes the length, not the end | **Mostly Human (10% AI, 916 words: L2e's end to P17v1, 94w)**, 02:48:48 |

Score for 250g, counted strictly: 2 of 8 (five came back Mostly Human, which I'd called Mixed or Human); pass or no pass: 6 of 8 (v9b and v9f failed where I said they'd pass); saying AI every time: 1 of 8. **v9a passes: Human Written, 0% AI, 912 words.** It is v7b with P7n1, P14n1 and L1w2 ("A founding group shouldn't pretend it can give you those" in place of the published sentence).

Batch 251g (written 02:49 UTC on 2026-10-12 by `date -u`, before the call; `v251.json`): v9a with the one trace fix still out that hasn't failed yet, P5n3 ("being there for each other", the published "accompany").

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 251g-S12v10 (890) | Mixed | it moves the windows of a section that only just passed | **Human (100%, "Human Written", 917 words)**, 02:49:53 |

Score for 251g: 0 of 1; saying AI every time: 0 of 1. **v10 passes too, with P5n3: Human Written, 0% AI, 917 words. It is candidate v5.**

Batch 252g (written 02:50 UTC on 2026-10-12 by `date -u`, before the call; `v252.json`): v5's paragraphs that haven't been checked alone or in their runs yet.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 252g-P13o1 (74) | Human | E6B's P13 with "or eighty"; its last three sentences passed alone | **Human (100%)**, 02:50:45 |
| 252g-P13o1P14n1 (97) | Human | P13n5P14n1 passed | **Human (100%)**, 02:50:51 |
| 252g-U8x (152) | Human | the list with L1w2; every list run so far has passed | **Human (100%)**, 02:50:55 |
| 252g-P15n2P16fL1w2 (132) | Human | P15n2P16fL1w1 passed | **Human (100%)**, 02:51:03 |

Score for 252g: 4 of 4; saying AI every time: 0 of 4. Every paragraph of v5 passes alone or in a run with a neighbor that passes alone (P1t6 with the heading, 51 words), and the section passes (251g).

The linter fails v5 on B13 again: three paragraphs open with "So" (P3n1, P12m, and P14n1, whose "So" the trace asked for). The published has two ("So the question isn't", "So early members"), and "therefore" inside its P12.

Batch 253g (written 02:52 UTC on 2026-10-12 by `date -u`, before the call; `v253.json`): P14 keeps the link as "Early on, then," (P14n4), or loses it (P14n3, "acute" kept); or P3 drops its "So" (P3n3, which one cold reader said had nothing to follow from).

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 253g-P13o1P14n4 (97) | Human | one word moved | **Human (100%)**, 02:52:48 |
| 253g-P13o1P14n3 (96) | Human | P13n5P14n3 passed | **Human (100%)**, 02:52:53 |
| 253g-P3n3 (51) | Human | P3n1 passed | **Human (100%)**, 02:52:57 |
| 253g-S12v11a (888) | Mixed | any change moves the windows of a section that only just passes | **Mixed (15% AI, 917 words: P10a's end into P11r1, 80w; the L4-to-P17 window, 62w)**, 02:53:04 |
| 253g-S12v11b (887) | Mixed | the same | **Human (100%, "Human Written", 916 words)**, 02:53:10 |
| 253g-S12v11c (887) | Mixed | the same | **Human (100%, "Human Written", 916 words)**, 02:53:14 |

Score for 253g: 4 of 6 (v11b and v11c Human where I said Mixed); saying AI every time: 0 of 6. Two ways pass. **Candidate v6 = v11c**: P3 without its "So" (the link one cold reader couldn't follow from P2) and P14 with it (the link the trace asked for); P12's "So" stays, so two paragraphs open with "So", as in the published section.

## Gate round r3 on v6, and its fixes

Gate round r3 (`review-r3/`): two traces on the paragraphs changed since r2, two cold reads, the stance check and the linter (v6: REVIEW, no FAIL). The stance check and a trace both say L4's "your ability to bring in a resource for it" reads as a means test (can you get resources), where the published "Your current need greatly exceeds your available resource" is about what you have to give; and the second trace in a row says L2's "all of the benefits of village life" isn't the published "the feeling of village life". The other findings are in `DISPOSITIONS-r2.md`.

Batch 254g (written 03:07 UTC on 2026-10-12 by `date -u`, before the call; `v254.json`): L4 said three ways ("your free resource", "what you have to give", "the resource you have"), L2 with "the feeling", in the list's runs and in the section.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 254g-U8b1 (146) | Human | every list run so far has passed | **Human (100%)**, 03:08:21 |
| 254g-U8a1 (144) | Human | the same | **Human (100%)**, 03:08:25 |
| 254g-L4xbP17v1 (72) | Human | L4w1P17v1 passed | **Human (100%)**, 03:08:30 |
| 254g-L4xaP17v1 (70) | Human | the same | **Human (100%)**, 03:08:37 |
| 254g-L4xcP17v1 (71) | Human | the same | **Human (100%)**, 03:08:41 |
| 254g-S12v12a (881) | Mixed | the end window is the fragile one, and both changes sit in it | **Mostly Human (9% AI, 910 words: "nflict, care, etc. You’re not will … or “in another role,” or", L2f's end to P17v1, 90w)**, 03:08:46 |
| 254g-S12v12b (879) | Mixed | the same | **Human (100%, "Human Written", 908 words)**, 03:08:51 |
| 254g-S12v12c (883) | Mixed | one change in the end window | **Human (100%, "Human Written", 912 words)**, 03:08:55 |
| 254g-S12v12d (881) | Mixed | the same | **Human (100%, "Human Written", 910 words)**, 03:09:02 |
| 254g-S12v12e (880) | Mixed | the same | **Human (100%, "Human Written", 909 words)**, 03:09:07 |

Score for 254g: 5 of 10 (v12b to v12e Human where I said Mixed; v12a Mostly Human, not Mixed); pass or no pass: 6 of 10; saying AI every time: 0 of 10. **Candidate v7 = v12b**: L2f ("the feeling of village life") and L4xa ("a need that far outstrips your free resource right now", the section's own term from P7, for the published "your available resource"). v12e ("the resource you have") passes too, but "resource" alone can still be read as money.

## Round r4 on v7, and its fixes

Round r4 (`review-r4/`): a trace on the section's end and the stance check. Findings two reviewers now agree on: P13's "Whether there are eight people ... or eighty" makes the chores size-neutral, where the published point is that even eight people carry all of them (r3 trace, r4 stance); P14's "some skill" lost "practical" (r3 trace, r4 stance); L4's "finding support where you are so you can build up your resources" for the published "building support and capacity" (the r2, r3 and r4 traces); P17 lost "A humane membership process" (the r2 and r4 traces). Findings only one reviewer raised stay as they are, with the reason in `DISPOSITIONS-r2.md`.

Batch 255g (written 03:23 UTC on 2026-10-12 by `date -u`, before the call; `v255.json`): the four fixes, P13 two ways ("Even if there are only eight people", "With only eight people") and L4 two ways (Emulate's frame with "building up support and capacity"; the published "the first step may be building support and capacity").

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 255g-P13p1 (74) | Human | P13o1 passed; one clause | **Human (100%)**, 03:23:33 |
| 255g-P13p2 (71) | Human | the same | **Human (100%)**, 03:23:37 |
| 255g-P13p1P14p1 (98) | Human | P13o1P14n1 passed; one word added | **Human (100%)**, 03:23:43 |
| 255g-P13p2P14p1 (95) | Human | the same | **Human (100%)**, 03:23:51 |
| 255g-U8y1 (143) | Human | every list run has passed | **Mixed (49% AI: "up. You have a need that far outst … ole,” or “with more suppo", L4y1 and P17y1, 73w)**, 03:23:55 |
| 255g-U8y2 (136) | AI | L4y2 is the published sentence, and P17y1 the published opening | **Mixed (70% AI: ") You want the feeling of village … ole,” or “with more suppo", L2f to P17y1, 99w)**, 03:24:01 |
| 255g-L4y1P17y1 (69) | Human | the same pair passed with other wording | **Human (100%)**, 03:24:05 |
| 255g-L4y2P17y1 (62) | AI | two published sentences together | **Human (100%)**, 03:24:10 |
| 255g-S12v13a (879) | Mixed | four changes, two in the fragile end | **Mixed (24% AI, 908 words: P10a's end into P11r1, 80w; "water system. The water well doesn’ … contribute, and a willing", P13p1's end into P14p1, 36w; L1w2's end to P17y1, 106w)**, 03:24:18 |
| 255g-S12v13b (876) | Mixed | the same | **Mixed (24% AI, 905 words: the same three windows)**, 03:24:23 |
| 255g-S12v13c (872) | Mixed | the same, with the published L4 | **Mixed (25% AI, 901 words: the same first two; L1w2's end to P17y1, 110w)**, 03:24:27 |
| 255g-S12v13d (869) | Mixed | the same | **Mixed (38% AI, 898 words: P10a's end to P11r1's end, 96w; P13p2's last two sentences into P14p1, 64w; P15n2's second sentence to P17y1, 188w)**, 03:24:33 |

Score for 255g: 9 of 12 (U8y1 Mixed where I said Human; L4y2P17y1 Human and U8y2 Mixed, not AI); saying AI every time: 0 of 12. Four changes at once break the section in three places, and the list with P17y1 ("A humane membership process should have ways ...") fails as a run for the first time. Next: the section from v7 with one change at a time.

Batch 256g (written 03:25 UTC on 2026-10-12 by `date -u`, before the call; `v256.json`): v7 with one of the r4 fixes each: P13p1 "Even if there are only eight people", P13p2 "With only eight people", P14p2 "something practical to contribute", P14p1 "some practical skill", L4y1 "building up support and capacity where you are", P17z1 "There should be humane ways", P17y1 "A humane membership process should have ways", and L4y1 with P17z1.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 256g-S12s1 (879) | Mixed | the P13 window has failed with most wordings but E6B's | **Mixed (15% AI, 908 words: "body else. So when I say someone mi … ttention caring for those", P10a's end into P11r1, 60w; "nflict, care, etc. You’re not will … or “in another role,” or", L2f's end to P17v1, 88w)**, 03:26:13 |
| 256g-S12s2 (876) | Mixed | the same | **Human (100%, "Human Written", 905 words)**, 03:26:16 |
| 256g-S12s3 (879) | Human | one word in P14 | **Mostly Human (9% AI, 908 words: L2f's end to P17v1, 88w)**, 03:26:21 |
| 256g-S12s4 (880) | Mixed | P14p1 sat in a failing window in all four v13s | **Mostly Human (7% AI, 909 words: " resource right now. (This doesn’t … or “in another role,” or", L4xa's parenthesis into P17v1, 62w)**, 03:26:28 |
| 256g-S12s5 (875) | Mixed | the end window | **Mixed (20% AI, 904 words: P10a's end into P11r1, 80w; L1w2's end to P17v1, 103w)**, 03:26:33 |
| 256g-S12s6 (880) | Human | one word in P17 | **Mostly Human (7% AI, 909 words: L4xa's parenthesis into P17z1, 63w)**, 03:26:37 |
| 256g-S12s7 (882) | Mixed | P17y1 failed in the list runs | **Human (100%, "Human Written", 911 words)**, 03:26:42 |
| 256g-S12s8 (876) | Mixed | two changes at the end | **Mixed (18% AI, 905 words: P10a's end into P11r1, 80w; L2f's end to P17z1, 85w)**, 03:26:46 |

Score for 256g, pass or no pass: 4 of 8 (s2 passed where I said it wouldn't; s3, s6 failed where I said they'd pass; s7 passed); saying AI every time: 0 of 8. As single changes from v7, P13p2 ("With only eight people") and P17y1 ("A humane membership process should have ways") pass; P13p1, both P14s, L4y1 and P17z1 don't. Next: P13p2 and P17y1 together, with P14 and L4 in other wordings.

Batch 257g (written 03:27 UTC on 2026-10-12 by `date -u`, before the call; `v257.json`): c1 = v7 with P13p2 and P17y1; then P14 with "practical" three ways (P14p1 "some practical skill", P14p3 "some practical skills", P14p6 "some practical skill they can contribute") and L4 two ways (L4y4: "finding support where you are and building up your resources", the "so you can" the traces object to gone; L4y7: "building up support and resources where you are").

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 257g-S12c1 (879) | Human | each passed alone from v7 | **Human (100%, "Human Written", 908 words)**, 03:28:24 |
| 257g-S12c2 (880) | Mixed | P14p1 failed alone from v7 | **Mostly Human (7% AI, 909 words: L4xa's parenthesis into P17y1, 65w)**, 03:28:28 |
| 257g-S12c3 (880) | Mixed | the same, plural | **Human (100%, "Human Written", 909 words)**, 03:28:34 |
| 257g-S12c4 (877) | Mixed | the end window | **Mostly Human (10% AI, 906 words: L2f's end to P17y1, 89w)**, 03:28:39 |
| 257g-S12c5 (878) | Mixed | two changes | **Mostly Human (10% AI, 907 words: the same window, 89w)**, 03:28:45 |
| 257g-S12c6 (878) | Mixed | two changes | **Human (100%, "Human Written", 907 words)**, 03:28:49 |
| 257g-S12c7 (876) | Mixed | two changes | **Mixed (20% AI, 905 words: P10a's end into P11r1, 60w; P13p2's last sentence into P14p1, 36w; L2f's end to P17y1, 87w)**, 03:28:53 |
| 257g-S12c8 (879) | Mixed | two changes | **Mostly Human (7% AI, 908 words: L4y4's parenthesis into P17y1, 63w)**, 03:28:58 |

Score for 257g, pass or no pass: 6 of 8 (c3 and c6 passed where I said they wouldn't); saying AI every time: 0 of 8. **c6 passes with all four r4 fixes: candidate v8** (P13p2 "With only eight people in the community", P14p3 "some practical skills to contribute", L4y4 "finding support where you are and building up your resources", P17y1 "A humane membership process should have ways of ...").

Batch 258g (written 03:29 UTC on 2026-10-12 by `date -u`, before the call; `v258.json`): v8's new paragraphs in their runs.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 258g-P13p2P14p3 (95) | Human | P13p2P14p1 passed | **Human (100%)**, 03:30:03 |
| 258g-U8c6 (145) | Human | the list in the section that passed | **Mixed (42% AI: "now. (This doesn’t mean you’re bad … ole,” or “with more suppo", L4y4's parenthesis and P17y1, 63w)**, 03:30:07 |
| 258g-L4y4P17y1 (71) | Human | L4y1P17y1 passed | **Human (100%)**, 03:30:12 |

Score for 258g: 2 of 3 (U8c6 Mixed where I said Human); saying AI every time: 0 of 3. The list as a run fails with P17y1 for the third time (U8y1, U8y2, U8c6), though the section passes: the published opening "A humane membership process should ..." is the likely cause. Next: P17 with "humane" and the process put other ways.

Batch 259g (written 03:31 UTC on 2026-10-12 by `date -u`, before the call; `v259.json`): P17 with the "humane" standard and the membership process kept in four other wordings: P17z1 "There should be humane ways", P17z3 "Any humane membership process should have ways", P17z4 "If the membership process is humane, there should be ways", P17z6 "The membership process should be humane enough to have ways"; the list run with each; the list's first items in a run from P15n2, which passes alone; and v8 with each.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 259g-U8z1 (143) | Human | "humane" as one word added to P17v1, whose list run passed | **Mixed (41% AI: L4y4's parenthesis and P17z1, 61w)**, 03:31:33 |
| 259g-U8z3 (145) | AI | still the published opening, with "Any" | **Human (100%)**, 03:31:37 |
| 259g-U8z4 (148) | Human | a conditional, not the published shape | **Human (100%)**, 03:31:42 |
| 259g-U8z6 (148) | Human | the same | **Mixed (23% AI: "es.) (The membership process shoul … ole,” or “with more suppo", P17z6, 32w)**, 03:31:49 |
| 259g-P15n2toL3e (163) | Human | P15n2P16fL1w2 passed | **Human (100%)**, 03:31:54 |
| 259g-S12v8z1 (876) | Mixed | P17z1 failed as a change from v7 | **Mostly Human (7% AI, 905 words: L4y4's parenthesis into P17z1, 61w)**, 03:31:59 |
| 259g-S12v8z3 (878) | Mixed | as U8z3 | **Human (100%, "Human Written", 907 words)**, 03:32:03 |
| 259g-S12v8z4 (881) | Human | the list ending without the published opening | **Human (100%, "Human Written", 910 words)**, 03:32:08 |
| 259g-S12v8z6 (881) | Human | the same | **Mixed (14% AI, 910 words: P13p2's last sentence into P14p3, 36w; L2f's end to P17z6, 92w)**, 03:32:15 |

Score for 259g, pass or no pass: 5 of 9 (U8z3 and S12v8z3 passed where I said AI and Mixed; U8z1 and U8z6, S12v8z6 failed where I said Human); saying AI every time: 0 of 9. P17z3 ("Any humane membership process should have ways ...") and P17z4 ("If the membership process is humane, there should be ways ...") pass in the list run and in the section. **Candidate v9 = v8 with P17z3**: it keeps the published "humane membership process ... should"; P17z4 makes "humane" a condition.

Batch 260g (written 03:33 UTC on 2026-10-12 by `date -u`, before the call; `v260.json`): v9's last two paragraphs as a pair.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 260g-L4y4P17z3 (70) | Human | both passed inside the list run | **Human (100%)**, 03:33:14 |

Score for 260g: 1 of 1; saying AI every time: 0 of 1. v9 passes every check: each paragraph alone or in a run with a neighbor that passes alone (P1t6 with the heading; L2f and L3e from P15n2; the list's end as a pair and in the list run), and the section, Human Written, 0% AI (259g).

## Joel's message of 2026-10-12 05:33 UTC: v10

His decisions (OWNER-EDITS.json, s12-joel-20261012-0533): 17b, 18b; P3, P7 and P16 back to the guide's text (my versions broke their meaning), P16 with his own last sentence ("Even then, the power to veto membership applications based on capacity remains dangerous."); P22 out of parentheses ("2 parentheticals in a row"). Page numbers: the chart is P5, so his P7 is the published P6 and his P16 the published P15. The guide's P3 opens with "So", which makes three "So" openers with P13 and P15 (the linter's B13), so P13's "So" becomes "then" inside the sentence, with a named subject instead of "it" (P13q3 "Welcoming someone is ...", P13q4 "The ability to welcome somebody is ...").

Batch 261g (written 05:38 UTC on 2026-10-12 by `date -u`, before the call; `v261.json`, parts in `fix-v5-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 261g-P2mP3g (121) | AI | the guide's P3 ("So the question isn't ... The practical question is ...") read AI with P4 as published (234g) | **AI (100%)**, 05:39:23 |
| 261g-P3gP4m (98) | AI | the same | **Mixed (51% AI: P3g, 49w)**, 05:39:27 |
| 261g-P5n3P6gP7n1P8m (124) | Human | one short guide sentence among three passing paragraphs | **Human (100%)**, 05:39:31 |
| 261g-P16g (77) | AI | the guide's P15 read 100% AI (234g); two changes of his don't change its shape | **AI (100%)**, 05:39:38 |
| 261g-P12s (74) | Human | P12r1 passed; "or even more of it" added | **Human (100%)**, 05:39:43 |
| 261g-P12sP13q3 (106) | Human | "Welcoming someone is partly a question of resources, then" | **Human (100%)**, 05:39:47 |
| 261g-P12sP13q4 (109) | AI | "The ability to welcome somebody is partly ..." is the guide's subject | **Human (100%)**, 05:39:52 |
| 261g-P10aP12s (123) | Human | P10aP11r1 passed | **Human (100%)**, 05:39:57 |
| 261g-L4y4P22n (71) | Human | P22 as a plain paragraph; "Any" passed in parentheses | **Human (100%)**, 05:40:05 |
| 261g-U8n (145) | Human | the list run passed with P22 in parentheses | **Human (100%)**, 05:40:09 |
| 261g-P16gP16fL1w2 (120) | AI | the guide's P15 again | **Mixed (68% AI: P16g, 80w)**, 05:40:14 |
| 261g-S12v10a (874) | Mixed | P3 and P16 in the guide's words | **Mixed (30% AI, 897 words: "y. So the question isn’t whether a … them without being consum", P3g, 49w; "bers is less. With only eight peopl … ons based on capacity rem", P14's second sentence to P16g's end, 144w; the L4-to-P22 window, 63w)**, 05:40:19 |
| 261g-S12v10b (877) | Mixed | the same | **Mixed (23% AI, 900 words: P3g, 49w; P14's second sentence to P16g's end, 144w)**, 05:40:23 |

Score for 261g, counted strictly: 10 of 13 (P3gP4m and P16gP16fL1w2 Mixed, not AI; P12sP13q4 Human where I said AI); pass or no pass: 12 of 13; saying AI every time: 2 of 13. The guide's P3 and P16 read AI, as published; the guide's P7 sentence passes in its run, and so do 18b, P13 without "So" and P22 without parentheses. **v10 = v10b** (P13q4 "The ability to welcome somebody is partly a problem of resources, then, not compassion", the guide's subject): 23% AI, all of it in the windows over P3 and P16.

The new checks on v10 (`preservation-keys.json`, and the fixed trace brief's validation run TV2): P15 (page numbering; the published P14) had lost "available" ("more resource than acute need" for "more available resource than acute need"). P14p4 puts the guide's word back.

Batch 262g (written 06:41 UTC on 2026-10-12 by `date -u`, before the call; `v262.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 262g-P13p2P14p4 (96) | Human | one word added to a pair that passed | **Human (100%)**, 06:41:40 |
| 262g-S12v10c (878) | Mixed | P3 and P16 in the guide's words, as in v10 | **Mixed (30% AI, 901 words: P3g, 49w; P14's second sentence to P16g's end, 145w; the L4-to-P22 window, 63w)**, 06:41:44 |

Score for 262g, counted strictly: 2 of 2; pass or no pass: 2 of 2; saying AI every time: 0 of 2. **v10c is the version to install**: it has every decision of his 05:33 message and passes the key-word check, and it reads as v10a did (30% AI), on the guide's P3 and P16 and, once, on the list run. Those are his words as published; whether to re-humanize them goes to him (question 19).

Batch 263g (written 07:40 UTC on 2026-10-12 by `date -u`, before the call; `v263.json`, parts in `fix-v6-parts.json`). The sweep of the article for Joel's 05:33 kinds of break (`sweep-20261012/`) found two in my section 12 text: P22's "people who fall into these categories" narrows the published "every limit", and P13's "fix the cars" narrows "equipment repaired". Both get the general word back.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 263g-P22w | Human | the v10 shape, which passed, with "not turning every limit into a flat-out rejection" | not checked: under the dashboard's minimum length (the button stays off), so it is checked with L4 |
| 263g-L4y4P22w | Human | L4y4P22n passed (261g) | **AI (100%)**, 07:41:34 |
| 263g-P13p2w | Human | "fix whatever breaks" is plainer than "fix the cars" | **Human (100%)**, 07:41:38 |
| 263g-P13q4P13p2wP14p4 | Human | each passed with a neighbor | **Human (100%)**, 07:41:50 |
| 263g-S12v10d | Mixed | v10c read 30% AI on the guide's P3 and P16, which don't change | **Mixed (30% AI, 900 words: P3g, 49w; P14's second sentence to P16g's end, 145w; the L4-to-P22 window, 62w)**, 07:41:55 |

Score for 263g, counted strictly: 3 of 4 checked (L4y4P22w AI where I said Human); pass or no pass: 3 of 4; saying AI every time: 1 of 4. "fix whatever breaks" passes alone and in its run. "not turning every limit into a flat-out rejection" reads AI with L4, where P22n passed, so P22 needs another way to say "every limit".

Batch 265g (written 07:44 UTC on 2026-10-12 by `date -u`, before the call; `v265.json`). Two other ways to keep the published "every limit" in P22: P22x "not flat-out rejecting people every time it hits a limit"; P22y "people who fall into these categories, or anyone else it can't take right now".

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 265g-L4y4P22x | Human | P22n's shape, which passed with L4, and a plain "every time it hits a limit" | **Human (100%)**, 07:44:31 |
| 265g-L4y4P22y | AI | longer, and the added clause reads tacked on | **Human (100%)**, 07:44:36 |
| 265g-S12v10e | Mixed | the guide's P3 and P16 don't change | **Mixed (45% AI, 902 words: P3g, 49w; P10a's end into P12s, 60w; P13p2w's second sentence to P22x's end, 299w)**, 07:44:41 |
| 265g-S12v10f | Mixed | the same | **Mixed (30% AI, 910 words: P3g, 49w; P14's second sentence to P16g's end, 145w; the L4-to-P22 window, 72w)**, 07:44:50 |

Score for 265g, counted strictly: 3 of 4 (L4y4P22y Human where I said AI); pass or no pass: 3 of 4. Both new P22s pass with L4. In the section, P22x makes it worse (45%) and P22y leaves it where v10c was (30%, the same three windows). **v10f** (v10c with "fix whatever breaks" and P22y) is the version to install: it keeps every key word, and its windows are the guide's P3 and P16 and the list run, as before.

Joel's message of 2026-10-12 17:23 UTC: his P3 ("human, best") and P16 ("let's keep this one, best one"), with his own Pangram checks (P3 human; P16 fully human), and why the guide's versions read AI: "for P3 it's a list of 3 that's why it's AI, you couldn' tsee that? and capacity is an AI tell"; P16 "had another list of 3, plus a big list in the beginning", and "it was also the vagueness of that "not now."" His texts aren't checked again alone (his own checks count); only the new combinations are.

Batch 269g (written 17:27 UTC on 2026-10-12 by `date -u`, before the call; `v269.json`, his parts in `fix-v7-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 269g-P2mP3j | Human | both pass alone; his P3 has no list of three left | **AI (100%)**, 17:27:47 |
| 269g-P3jP4m | Human | the same | **Human (100%)**, 17:27:50 |
| 269g-P14p4P16j | Human | his P16 fully human; P15 passed beside P13 and P14 | **AI (100%)**, 17:27:55 |
| 269g-P16jP16fL1w2 | Human | his P16 into the list's lead-in | **Human (100%)**, 17:28:02 |
| 269g-S12v11 | Mixed | the list's end with P22 read AI in every section run since v10c (62 to 72 words) | **Mixed (31% AI, 934 words: P14's "With only eight people" to P16's end, 154w; L1's end to P22, 128w)**, 17:28:07 |

Score for 269g, counted strictly: 3 of 5 (P2mP3j and P14p4P16j AI where I said Human); pass or no pass: 3 of 5. His P3 clears the P3 window in the section; P2 with it reads AI as a pair, and the section doesn't flag them. What's left is mine: P15 ("more available resource than acute need, and some practical skills to contribute, and a willingness to learn": the list of three he named in P3 and P16, which I didn't see in my own P15), and the list run's end, where P22 has the published three alternatives with an "or" before each.

Batch 270g (written 17:30 UTC on 2026-10-12 by `date -u`, before the call; `v270.json`, parts in `fix-v8-parts.json`). His fix for a needed list of three, from P16 ("It would also need a way to revisit ..."): the third item in its own sentence. P15s1 does that ("They usually need to be willing to learn, too.", keeping "usually"); P22z does it for the three alternatives ("It could also say “with more support.”").

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 270g-P15s1P16j | Human | the list of three gone from P15 | **Human (100%)**, 17:30:18 |
| 270g-L4y4P22z | Human | P22's three alternatives as two and one | **Human (100%)**, 17:30:22 |
| 270g-S12v11a | Mixed | P15s1 only: the list run's window stays | **Human, "Mostly Human Written" (8% AI, 938 words: P14's "With only eight people" list, 40w; his P16's "Pretending capacity ... a “not now” decision", 36w)**, 17:30:27. Not a pass; the list run's window is gone |
| 270g-S12v11b | Mixed | P22z only: P14 to P16 stays | **Mixed (40% AI: P10a into P12s, 60w; P14 to P22z, 319w)**, 17:30:34 |
| 270g-S12v11c | Human | both | **Mixed (20% AI: P14 into P15s1, 60w; his P16's middle, 49w; L4 to P22z, 75w)**, 17:30:39 |

Score for 270g, counted strictly: 2 of 5; pass or no pass: 2 of 5. P15s1 is the better of the two: with it alone the section reads "Mostly Human" (8%), the list run's window gone, P22y kept. Left: P14's five-item list (mine), and 36 words in the middle of his P16, which he checked fully human alone.

Batch 271g (written 17:31 UTC on 2026-10-12 by `date -u`, before the call; `v271.json`). P14's list of five as pairs (his rule: lists in general read AI): P13p2x "grow the food and fix whatever breaks. Somebody has to balance the books and watch the kids, and the water system has to keep working."; P13p2t the same with the water system its own sentence. And one diagnostic only, not for the article without his OK: P16k, his two passing P16 fixes together ("Any real process would need concrete criteria, and review by someone who wasn't part of the decision. It would also need a way to revisit a “not now” decision on membership.").

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 271g-P13q4P13p2xP15s1 | Human | no list of three left in the run | **Human (100%)**, 17:32:17 |
| 271g-P13q4P13p2tP15s1 | Human | the same | **Human (100%)**, 17:32:21 |
| 271g-S12v11d | Human | P14's list gone; his P16's window may stay | **Mixed (11% AI: his P16's middle, 36w; L4 to P22, 72w)**, 17:32:26 |
| 271g-S12v11e | Human | the same | **Human (100%), "Human Written"** (946 words), 17:32:33 |
| 271g-S12v11f | Human | with P16k (diagnostic) | **Human (100%), "Human Written"** (950 words), 17:32:37 |

Score for 271g: 4 of 5 (S12v11d Mixed where I said Human). **Section 12 v11 = 271g's S12v11e: 100% Human with his P3 and P16 exactly as he chose them**, on try 3 of the section after his message (269g, 270g, 271g). My changes: P14's list of five as two pairs and a sentence (P13p2t), P15's third item in its own sentence (P15s1), both his list rule. The diagnostic with his two P16 fixes together (P16k) also reads 100% Human, so it isn't needed.

The new trace on v11's changed paragraphs (s12/review-r6/trace-r6.md, Sonnet): P15s1 OK. P14 (P13p2t) NEEDS FIX on two sentences older than this turn: "tolerate the disruption of new members" for the published "absorb disruption" ("absorb", the section's own term, which the key file's U23 hadn't listed), and "someone's heart" for "the new member's". By the 05:33 rule a lost key word goes back; both are fixed and the key file now lists them.

Batch 273g (written 17:42 UTC on 2026-10-12 by `date -u`, before the call; `v273.json`): P13p2u "the ability of that community to absorb disruption is less" and "the new member's heart"; P13p2v "absorb the disruption" and "a new member's heart".

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 273g-P13q4P13p2uP15s1 | Human | two words back in a run that passed | **Human (100%)**, 17:42:56 |
| 273g-P13q4P13p2vP15s1 | Human | the same | **Human (100%)**, 17:43:01 |
| 273g-S12v11g | Human (weak) | the section passed with P13p2t; windows move | **Human (100%), "Human Written"** (944 words), 17:43:06 |
| 273g-S12v11h | Human (weak) | the same | **Human (100%), "Human Written"** (945 words), 17:43:14 |

Score for 273g: 4 of 4. **Section 12 v11 = 273g's S12v11g**: his P3 and P16 as written; P14 with "absorb disruption" and "the new member's heart" (the published words), its list as two pairs and a sentence; P15's third item in its own sentence. 100% Human (944 words). Each paragraph of mine passes alone or in its run (P14 and P15 with P13, 273g; P15 with his P16, 270g; P22 with L4, 261g and 265g).

