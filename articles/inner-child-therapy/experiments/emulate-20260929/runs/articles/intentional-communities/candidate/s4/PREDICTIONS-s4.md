# Section 4: predictions before each Pangram call, and results

As published: 87% AI (baseline-04, 1,105 words): AI from the heading to "fewer robes", Human for P8 to P11's "The adult reparents.", AI for P11's last sentence and P12, Human for P13 and P14, AI from P15 to the end.

## v3 (texts in `r3/`)

v1 was Emulate (two calls per unit) with small fixes; v2 and v3 fixed what the gate found (traces, cold reads, grounding, the whole-article stance check) before any Pangram call. Paragraphs under 50 words go with a neighbor; P8 to P10, P13 and P14 are the published text (Human in the baseline) and serve only as neighbors.

| text | mine | why | Pangram |
|---|---|---|---|
| section-v3 | AI somewhere (10 to 30%) | 25 rewritten paragraphs from mixed sources; my guess is P4 or P29 to P31 | 20% AI (1413) |
| P1 | Human | Emulate's long sentence, one fix | Human (68) |
| P2 | Human | Emulate, light fixes | Human (68) |
| P3 | Human | Emulate, four small fixes | Human (111) |
| H2P4P5 | AI | P4 is a principle in three short sentences, and P5's middle is mine | 100% AI (130) |
| P5 | AI | about half mine | 100% AI (90) |
| P5P6 | AI | follows P5 | 100% AI (127) |
| P6P7 | Human | Emulate's, the quip back in its words | Human (64) |
| P11P12 | AI | P11's last sentence and P12 are mine | Human (75) |
| P12P13 | Human | P13 is Joel's | Human (78) |
| P15P16 | Human | Emulate | Human (89) |
| P16 | Human | Emulate's formal register, a coin toss | Human (64) |
| P16P17 | Human | | Human (91) |
| P17P18P19 | Human | Emulate, with its "minute-ized and agenda-ized" | Human (84) |
| H3cP20P21 | Human | | Human (80) |
| P21 | Human | | Human (59) |
| H3dP22P23P24 | Human | | Human (94) |
| P24 | Human | | Human (62) |
| P25 | Human | Emulate B, its register | Human (95) |
| P26 | Human | Emulate A and B | Human (80) |
| P27 | Human | Emulate's questions | Human (71) |
| P28 | Human | | Human (60) |
| P29 | AI | three parallel "No amount of" sentences | 100% AI (51) |
| P29P30P31 | AI | P29, and P30 is mine | 100% AI (112) |

v3 results: **the section 20% AI** (1,413 words), in two spans: from P11's "The adult reparents." to the end of P12 (46 words), and from P13's last sentence (published, Joel's: "A living community should relate to its own teachings…") to the end of P20 (229 words). Every check inside those spans passed alone or in its pair. **P5, H2P4P5, P5P6, P29 and P29P30P31 100% AI**; every other paragraph check 100% Human. Mine: 23 of 24 labels right (I called P11P12 AI; it passed). For the section I had the size right and the place wrong: I guessed P4 or P29 to P31, and the spans were P11 to P12 and P13 to P20, where every paragraph passes on its own and the second span starts at an unchanged published sentence.
The worker counted 18 more credits gone than its checks used (372 at the start, 313 at the end): someone else was using the account at the same time.

## v4 (texts in `r4/`)

New Emulate calls for P5 alone, P29+P30, P11 to P13 and P15 to P17 (`emu/outputs2.json`). P5 rebuilt on e13-emuB with the four examples back, one to a sentence, as Joel did with a list (2026-10-01); P29 rewritten (every Emulate version was a three-part run, and v3's "No amount of" run read 100% AI); P11's tail, P12, P15 to P17 changed. Windows instead of section checks first: W1 is P11 to P13, W2 is P13 to P20 (the second span). W2-v4j has a proposal for P13's last sentence, which is Joel's published text: the span starts there.

| text | mine | why | Pangram |
|---|---|---|---|
| W1-P11P12P13 | Human | P12 no longer has the "may not even notice" landing | Human (134) |
| W2-v3 | AI | the section's span, if a window reproduces it | 100% AI (264) |
| W2-v4 | AI | the span starts at P13's last sentence, which v4 doesn't change | 100% AI (257) |
| W2-v4j | Human | the start of the span changed | 100% AI (257) |
| P3H2P4 | Human | P3 passed alone | Human (151) |
| P5 | Human | concrete, one example to a sentence | 100% AI (91) |
| H2P4P5 | Human | | 100% AI (131) |
| P5P6 | Human | | 47% AI (128) |
| P11P12 | Human | | Human (84) |
| P15P16 | Human | | Human (86) |
| P16 | Human | | Human (57) |
| P16P17 | Human | | Human (80) |
| P29 | Human | the parallel run broken | 100% AI (56) |
| P29P30P31 | Human | | 100% AI (117) |

v4 results: **W1 (P11 to P13) 100% Human**, so the first span is gone. **W2 100% AI in all three versions**, v3, v4 and with my P13 proposal, so P13's last sentence isn't what starts it, and the proposal is dropped. **P5 100% AI again**, and P5P6 47% AI (the four examples, one to a sentence); **P29 100% AI again**. P3H2P4, P11P12, P15P16, P16 and P16P17 100% Human. Mine: 8 of 14 right. The window cost: 3 credits each, against 14 for a section check. The worker counted 16 credits gone that its checks didn't use: someone else is checking on the same account.

## v5 (texts in `r5/`)

A third Emulate round on whole runs of paragraphs (`emu/outputs3.json`): P14 to P19 as one unit, P5+P6, and P28 to P31. Each paragraph in W2 passes alone, so the window's problem is the run; e17-emuA's run is in, with fixes for meaning (one founder, not "a few professionals"; power "just from that"; your children and the medicine work, not "see your kids" and "medication"; "believed in a dispute" from e17-emuB; the people involved, back in P18). P5 is e19-emuB: it says how the four parts tangle without the four "X can become Y" examples, which read AI every way I kept them (three tries). P29 is e20-emuA with its three-part run broken; P29y is a shorter one, checked after P28. P30 is e20-emuB's ("the inside of the container").

| text | mine | why | Pangram |
|---|---|---|---|
| W2-v5 | Human | Emulate's run, in one voice  | Human (297) |
| P5 | Human | Emulate's, almost as it came  | Human (69) |
| H2P4P5 | Human |  | 39% AI (109) |
| P5P6 | Human |  | Human (106) |
| P15P16 | Human |  | Human (133) |
| P16 | Human |  | Human (92) |
| P16P17 | Human |  | Human (108) |
| P17P18P19 | Human |  | Human (73) |
| P29 | AI | still two "make up for" sentences in a row  | Human (72) |
| P28P29y | Human |  | Human (105) |
| P29P30P31 | AI | follows P29  | Human (127) |

v5 results: **W2 100% Human**: Emulate's run of P15 to P19 broke the window that every earlier version failed. **P5, P5P6 and P29 100% Human**, and so are P15P16, P16, P16P17, P17P18P19, P28P29y and P29P30P31. **H2P4P5 39% AI**, on the heading and P4 only (P5 unflagged); P3H2P4 passed in v4, so P4 passes with a neighbor that passes alone. Mine: 8 of 11 (I called P29 and P29P30P31 AI, and both passed; I called H2P4P5 Human).

## v5, the section (texts in `r5/`), with a P4 alternative

The gate's trace, cold read and stance check on v5's ten changed paragraphs run at the same time; a meaning fix would mean checking again.

| text | mine | why | Pangram |
|---|---|---|---|
| section-v5 | Human | both v3 spans were fixed in their windows (W1 v4, W2 v5) | Human (1449) |
| H2P4bP5 | Human | P4b: "You keep authority over your own practice…", one sentence for the three clauses | not checked |

**v5 section: 100% Human (1,449 words), try 1** (04:38 UTC; I ran it myself, since the checking agents had hit the account's weekly limit). P4 stays: it passes with P3 before it (v4), and the section passes; H2P4bP5 wasn't checked, to keep the credits. The gate's fresh-agent checks on v5's ten changed paragraphs (trace, cold read, stance) couldn't run: every agent call failed on the weekly limit (resets 2026-10-06 14:00). So v5 is a candidate that still owes those three checks.

## v6: Joel's edits of 2026-10-02 21:16 (texts in `r6/`)

His P5, P7, P11 to P13, P26, P28 and P29, each checked by him (P11 to P13 together); P16's "believed in a dispute" confirmed. Two proposals of mine: "following what they've decided on so far" in P13 (a word seems to be missing), and "These four categories" in P5 (a cold reader couldn't tell which categories "These" meant, twice).

| text | mine | why | Pangram |
|---|---|---|---|
| section-v6 | Human | v5 passed, and his paragraphs pass; his note that a more human paragraph can expose the next one is the risk | 92% Human, 8% AI (1507) |
| P11P12P13what | Human | one word added to his passing trio | Human (153) |
| P5four | Human | one word added | Human (84) |

v6 results: **the section 92% Human, 8% AI**: one span, from P21's second sentence ("People need to be screened…") across the heading and the list to P24's first sentence. Those paragraphs passed in v3 and v5, and alone; Joel's note fits: once the paragraphs before them got more human, the AI in them showed. Both proposals pass: P11 to P13 with "what" 100% Human (153), P5 with "These four categories" 100% Human (84). Mine: 2 of 3. The v6 trace, cold read and whole-article stance check ran (`TRACE-v6-A.md`, `SENSE-v6.md`, `STANCE-v6.md`).

## v7 (texts in `r7/`)

P21 to P24 from one Emulate call over the run (e21, `emu/outputs4.json`), with small fixes; P16's last sentence rebuilt (the stance check and the trace both read Emulate's as a rule that a listener can never hold an admin role); P17's "refer to … for" garden path fixed (cold read). Windows first; the section only if both windows pass. Two more proposals on Joel's paragraphs: P5 with "plant medicine" (a cold reader couldn't tell doctors from medicine people), and P28 without "often" (for a child's serious report, section 8 says the process is decided beforehand).

| text | mine | why | Pangram |
|---|---|---|---|
| W3-P20toP25 | Human | the run from one Emulate call || Human (280) |
| W2-v7 | Human | two small fixes inside a window that passed || Human (303) |
| P21 | Human | || Human (77) |
| H3dP22P23P24 | Human | || Human (87) |
| P24 | Human | || Human (57) |
| P16 | Human | || Human (91) |
| P16P17 | Human | || Human (109) |
| P5fourplant | Human | one more word in a passing paragraph || Human (85) |
| P28still | Human | one word out || Human (79) |
| section-v7 | Human | || Human (1519) |

v7 results: **all ten 100% Human, the section too (1,519 words)**, try 1. Mine: 10 of 10. The v7 trace and stance check found two things to fix in my paragraphs: P23 read as a move or a forecast ("I'm personally moving towards… this will happen in three stages"), and P24 made the stage-one share optional, where section 15 says an outside earner "should contribute an agreed share". The stance check's other findings are on Joel's own paragraphs (his corrections of the published text), for him to see, not to fix.

## v8 (texts in `r8/`)

P23: "Personally, I'm aiming for communities with less and less money involved. I think the path there has three stages." P24: "Members might have outside jobs, and they bring an agreed share of that income in."

| text | mine | why | Pangram |
|---|---|---|---|
| W3-v8 | Human | two small fixes inside a window that passed | |
| H3dP22P23P24 | Human | | |
| P24 | Human | | |
| section-v8 | Human | | |
