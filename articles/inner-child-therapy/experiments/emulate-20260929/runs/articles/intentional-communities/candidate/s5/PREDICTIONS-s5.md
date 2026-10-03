# Section 5: predictions before each Pangram call, and results

As published: 97% AI (baseline-05, 1,388 words): AI from the heading to P10's first sentence, Human for P10's next two sentences (Joel's ayahuasca at 26 and the monasteries, 39 words), AI from "That helped produce a God complex" to the end.

v1 was Emulate (two calls per unit, every paragraph) with small fixes; the gate ran three times before any Pangram call (v1: four traces, cold read, grounding, stance; v2: four traces, cold read, stance; v3: two traces, cold read, stance on what v2's gate sent back). Paragraphs under 50 words go with a neighbor that passes alone. Credits at the start: 59 at the last count (2026-10-02), with another session drawing on the same account.

## v3, round 1: the paragraphs the v2 gate passed and v3 didn't change (texts in `r3/` and `r4/`, byte-identical; records in `r3/pangram-s5.jsonl` for P2 and `r4/pangram-s5.jsonl` for the rest)

| text | mine | why | Pangram |
|---|---|---|---|
| P2 | Human (weak) | Emulate's casual shape ("-- which is false!", "They've"), though the FDA sentence is formal | Human (72) |
| P4P5 | Human (weak) | P4 is one long "or … or … or" sentence; P5 is mostly Emulate B, its last sentence mine | Human (108) |
| P5 | Human (weak) | the same, alone | Human (58) |
| P6 | AI | a formal survey summary, close to the published order | 100% AI (56) |
| P7 | AI | the published dishes triad is back for its meaning | 100% AI (69) |
| H2bP18P19 | AI | "No special shamans." as an opener, then a "who… who… who…" list, much of it rebuilt by me | 100% AI (124) |
| P19 | AI | the same list | Human (82) |
| P21P22 | AI | P22 is a four-part requirement list | not checked (P22 changed in v4) |
| P22 | AI | the same | not checked (P22 changed in v4) |
| P31P32 | AI | P32 is close to the published sentence shapes | 100% AI (77) |
| P32 | AI | the same | Human (59) |
| P33 | AI | three short, balanced sentences | 100% AI (54) |

Round 1 results (02:10 to 02:25 UTC, every one try 1, Pangram 4.0, all "short text"): **P2, P4P5, P5, P19 and P32 100% Human; P6, P7, H2bP18P19, P31P32 and P33 100% AI**, each AI one as a single span over the whole text. Mine: 8 of 10 (I called P19 and P32 AI, and both passed). So P4 passes with P5, which passes alone; P18 fails with the heading and P19, which passes alone; P31 fails with P32, which passes alone.

P21P22 and P22 weren't checked: the v3 stance check sent P22 back ("a clear idea" for "Decide … before anybody takes anything"), and v4 fixed it.

Credits: 59 before P2, 23 by the time P2's result was read (36 gone for a 68-word check; P2 itself costs 1), and P4P5 took the balance from 23 to 15 (8 for 108 words). Another session is checking on the same account at the same time. 6 left after P33.

The reader: the dashboard now keeps showing the result that was open before a submit, and lists each new check as a card above it with its whole text. `pg_read.js`'s tail test matched the card list, so it read the previous panel for P7 onward (none of those reads was recorded); the worker read each result from its own card with a panel-only check (`/home/claude/work/pgcard2.py`), and every record's text matches its file.

## v6 (texts in `r6/`)

v5 rebuilt the five that read AI on Emulate's round 2 (`emu/outputs2.json`, inputs from v4's text); the v5 gate (two traces, cold read, stance: no conflict) sent back small fixes, in v6. P31 is round 2's own sentence, unchanged since v5.

| text | mine | why | Pangram |
|---|---|---|---|
| P31P32 | Human | Emulate's P31 ("It's possible that the call is real, but it's a terrible idea to form a village while you're in that state") before a P32 that passes alone | 100% AI (83) |

v6 result (02:46 UTC, try 2 for P31): **P31P32 100% AI** (83 words), one span over both paragraphs. Mine: 0 of 1. The v6 stance check also sent that P31 back (a rule about timing, where the published says omnipotence is a bad premise). Credits 6 before, 2 after (4 gone for an 83-word check: the other session again).

## v7 (texts in `r7/`)

The v6 gate's fixes (P18, P29, P30, P33) and a new P31; the v7 trace and stance check found nothing to change.

| text | mine | why | Pangram |
|---|---|---|---|
| P31P32 | AI | "omnipotence is a terrible thing to build a village on" is still a one-line maxim, and two maxims for it read AI in front of the same P32 | not checked: out of credits |

v7 (03:12 UTC): the submit went in with "2 left" showing, but no result came: the page said "You have used all your AI detection credits for this month. Your monthly credits will refill in 15 days." Nothing was recorded. No more checks are possible on this account until Joel adds credits or they refill.

Where section 5 stands on Pangram: P2, P5, P19 and P32 pass alone, and P4 with P5. P6, P7, P18, P31 and P33 read AI and were rebuilt (v5 to v7; the v7 gate found nothing to change), unchecked. The other 23 paragraphs and the section are unchecked.

## Through the API (2026-10-03, after Joel's 04:03 answers and his new API key)

Joel's key works (probe: HTTP 404 on a dummy task, no charge). Two calibration checks of texts the dashboard had already scored, through `tools/humanization/pangram_api.py` (model pangram-4, version 4.0): **P2 (r3) 100% Human, 72 words** and **P33 v4 (r4) 100% AI, 54 words**, the same as the dashboard. So the API and the dashboard agree on these two, and records from both are comparable.

### v9, API batch 1 (texts in `checks-v9-api1.json`): paragraphs v8 and v9 didn't change, P10 with Joel's "25"

| text | mine | why | Pangram |
|---|---|---|---|
| P1 | AI | four dated facts, one to a sentence, close to the published shape | 100% AI (73) |
| P6 | AI | rebuilt on round 2; a formal survey sentence in the middle | Human (53) |
| H2aP9 | Human | Emulate A's "super helpful" and its loose second sentence | Human (89) |
| P10 | Human | Joel's middle (Human in the baseline), now with "25"; the last sentence is mine | Human (73) |
| P11 | Human | Emulate A's question opener, "4 hours" | Human (70) |
| P12 | AI | a balanced held/watched sentence, close to the published | 100% AI (51) |
| P13 | Human | Emulate A's "since the lighting is the same", the mother joke | 100% AI (70) |
| P13P14 | Human | P14 is short and plain | 100% AI (114) |
| H2bP18P19 | AI | "No special shamans." and the respect sentence again, much as v4 | 100% AI (121) |
| H2cP29P30 | Human | round 2's voice; three "And you run into…" | Human (108) |
| P30 | Human | the same, alone | Human (67) |
| P31P32 | AI | a one-line maxim for omnipotence, twice AI before with this P32 | 100% AI (75) |

Batch 1 results (04:13 to 04:14 UTC, API, Pangram 4.0): **P6, H2aP9, P10, P11, H2cP29P30 and P30 100% Human; P1, P12, P13, P13P14, H2bP18P19 and P31P32 100% AI.** Tries: P6 try 2 (v4's read AI), P18 try 2, P31 try 3; the rest try 1. Mine: 9 of 12 (I called P6 AI, P13 and P13P14 Human). So P9 and P29 pass with neighbors that pass alone (P9 is the h2's first paragraph; P29 is under 50 words, with P30).

### v10, API batch 2 (texts in `checks-v10-api2.json`)

v9 split or trimmed the lists of three (E125); v10 fixed what the v9 gate found in P8, P17, P28 and P33 (not in this batch).

| text | mine | why | Pangram |
|---|---|---|---|
| P2P3 | Human | P2 passes alone; P3's five axes are now two to a sentence | Human (124) |
| P7 | Human | round 2's voice, and the list down to two | 100% AI (70) |
| P20 | AI | close to the published sentence | 100% AI (55) |
| P21P22 | AI | P22 is still a run of requirements, if no longer one list | 57% AI (96) |
| P22 | AI | the same | 100% AI (56) |
| W-P22toP25 | AI | P22 and P24 close to the published | 100% AI (170) |

Batch 2 results (04:30 UTC, API): **P2P3 100% Human; P7, P20, P22 and the P22–P25 window 100% AI; P21P22 57% AI ("Mixed").** Tries: P3 try 1, P7 try 3, P20 try 1, P22 try 1. Mine: 5 of 6 (I called P7 Human). So P3 passes with P2, which passes alone.

The Emulate key returned HTTP 403 at 04:30 on the round-3 calls (a balance check too); it worked at 02:30. Asked Joel.

### v11, API batch 3 (texts in `checks-v11-api3.json`): the paragraphs not checked yet

| text | mine | why | Pangram |
|---|---|---|---|
| P8 | AI | close to the published, with the four harms split | 100% AI (76) |
| W-P15toP17 | Human | fragments, the rave, "Yeah" | Human (173) |
| P16P17 | Human | | Human (133) |
| P17 | Human | Emulate's "Yeah" and "dive into this"; the duties split into short sentences | 100% AI (85) |
| W-P23toP25 | AI | P23 and P24 close to the published | 100% AI (114) |
| W-P25toP28 | AI | P27 and P28 lists split, but instruction-heavy | 100% AI (187) |
| P27P28 | AI | | 100% AI (108) |
| P28 | AI | | Human (68) |
| P33 | Human | Joel's step in his own framing; a conditional sentence | Human (69) |

Batch 3 results (04:42 UTC, API, Pangram 4.0): **the P15–P17 window, P16P17, P28 and P33 100% Human; P8, P17, the P23–P25 and P25–P28 windows and P27P28 100% AI.** Tries: P33 try 2 (round 1's v4 read AI; v11 has Joel's step); the rest try 1. Mine: 7 of 9 (I called P17 Human and P28 AI). So P28 and P33 pass alone; P17 passes with P16 and inside the P15–P17 window but not alone, so it can't anchor P16 or P15; P27 fails with P28, which passes alone.

Where section 5 stands after batch 3: passing alone or with a neighbor that passes alone: P2, P3, P4, P5, P6, P9, P10, P11, P19, P28, P29, P30, P32, P33. Reading AI: P1, P7, P8, P12, P13, P17 (alone), P18, P20, P22, P31, and the runs around P23–P27. Short paragraphs waiting for an anchor: P14, P15, P16, P21, P23–P27. The Emulate key still returns 403, so the next round is the gate's other route: fresh writers, three variants each (`writers/`).

## v12 to v15: fresh writers (Emulate's key still returns 403; balance check at 05:18 too)

Eight Opus writers, one brief each (`writers/W1.txt` to `W8.txt`), three variants each (`writers/outputs-raw.md`, exact). v12 is the first pick for each paragraph, v13 the alternates; both went through the whole gate before any Pangram call: four traces, two cold reads, two stance checks, two grounding reviews (`TRACE-v12-*`, `TRACE-v13-*`, `SENSE-v12/13`, `STANCE-v12/13`, `GROUNDING-v12/13`), and the linter (`lint12/`, `lint14/`). Their fixes are v14 (v12's) and v15 (v13's); the fixed paragraphs go back through the gate before their checks. Batch 4a checks only what the gate passed unchanged.

### v14, API batch 4a (texts in `r14/`, names in `checks-v14.json`): gate-clean paragraphs and the pairs that anchor short ones

| text | mine | why | Pangram |
|---|---|---|---|
| P1 | AI (weak) | five dated facts still carry it, though grouped by year under a spoken conditional ("If you went by…") || 100% AI (69) |
| P12 | AI (weak) | the held/watched pair, then a formal "which require screening…" || Human (45) |
| P13 | Human (weak) | the lighting aside in parentheses, the mother joke || 100% AI (43) |
| P11P12 | Human (weak) | P11 passes alone and leads || Human (115) |
| P12P13 | Human (weak) | P13's aside || 100% AI (88) |
| P20 | Human | the open question asked aloud, "I don't know yet." || 100% AI (55) |
| P21 | Human (weak) | short; "Still," and the psychopath shaman || Human (35) |
| P20P21 | Human | || 100% AI (90) |
| P23 | AI (weak) | "not smuggled into one sentence here" is the published phrase || Human (40) |
| P24 | AI (weak) | "by pharmacological decree", the published quip || 100% AI (37) |
| P25 | Human (weak) | "6 months", the geometric visions || 100% AI (33) |
| P23P24 | AI | || 100% AI (77) |
| P24P25 | Human (weak) | || 100% AI (70) |
| P27 | Human (weak) | "By supports I mean…", a fragment || Human (42) |
| P27P28 | Human | P28 passes alone || 100% AI (110) |
| P30P31 | Human (weak) | P30 passes alone and leads; P31 last (with P32 it led, and failed three times) || Human (82) |

Batch 4a results (05:51 to 05:53 UTC, API, Pangram 4.0): **P12, P11P12, P21, P23, P27 and P30P31 100% Human; P1, P13, P12P13, P20, P20P21, P24, P25, P23P24, P24P25 and P27P28 100% AI.** Every one is a new text, try 1 for these writers' versions (P1 try 2 counting v11, P20 try 2, P13 try 2, P12 try 2). Mine: 7 of 16, my worst batch: I called P20 (the open question asked aloud) and P25 (the geometric visions) Human, and both read AI; I called P12 and P23 AI, and both passed. So P12, P21, P23 and P27 pass alone, and P31 passes with P30, which passes alone (try 4 for P31; three P31s had read AI ahead of P32). P27P28 reads AI though both pass alone: the section check will show whether that pair's seam matters. P1, P13, P20, P24 and P25 go to their gated alternates (v16).


### v16, API batch 4b: what the round-2 gate passed, and the alternates for batch 4a's five AI paragraphs

v16 is v14 with v15's P1, P13, P20, P24 and P25 (the gated alternates), and round 2's fixes to P8 and P22 (those two wait for round 3, so they aren't in this batch). Texts in `r16/`, names in `checks-v16.json`.

| text | mine | why | Pangram |
|---|---|---|---|
| P2 | Human | passed with "either" (72 words); one word changed || Human (68) |
| P2P3 | Human | passed before with "either" || Human (124) |
| P7 | AI (weak) | "Any community … will eventually learn" is back near the published shape; the 12 and 6 in digits, the parenthesis || 100% AI (65) |
| P13 | Human (weak) | the fragment "And which parts look like your mother.", "right down to the lighting" || 100% AI (45) |
| P12P13 | Human (weak) | P12 passes alone || 100% AI (90) |
| P14 | AI (weak) | "And community creates a rhythm." then a formal timing sentence || 100% AI (34) |
| P13P14 | AI (weak) | || 100% AI (79) |
| P14P15 | AI (weak) | P15's fragments may carry it || 100% AI (74) |
| P15 | Human (weak) | three fragments, never checked alone || Human (40) |
| P16 | Human | the rave, "inconvenient habits and all… 💃🕺" || Human (48) |
| P17 | Human (weak) | a question to the reader ("Is your community humble enough…?") || Human (54) |
| P16P17 | Human | || Human (102) |
| H2bP18P19 | AI (weak) | "No special shamans" opens again, though as a clause || 100% AI (121) |
| P18 | AI (weak) | || 100% AI (40) |
| P20 | Human (weak) | the parenthesis, "I don't know yet how to prevent that." || 100% AI (51) |
| P24 | Human (weak) | a question ("Months of honest relationship, though?") || 100% AI (39) |
| P23P24 | Human (weak) | P23 passes alone || 100% AI (79) |
| P25 | AI | close to the published two sentences || 100% AI (32) |
| P26 | AI (weak) | "Integration is just regular life." opens like a principle || 100% AI (53) |
| P25P26 | AI | || 100% AI (85) |
| P33 | Human | passed with "communities like it"; three words changed || Human (70) |
| P1 | AI (weak) | five dated facts again, though "way behind" and the "And since 2023" ending are loose || 100% AI-assisted ("Mixed", 69) |

Batch 4b results (06:11 to 06:13 UTC, API): **P2, P2P3, P15, P16, P17, P16P17 and P33 100% Human; P7, P13, P12P13, P14, P13P14, P14P15, H2bP18P19, P18, P20, P24, P23P24, P25, P26 and P25P26 100% AI; P1 100% AI-assisted** (Pangram's "Mixed": fraction_ai_assisted 1.0). Tries: P2 try 2 (one word changed), P33 try 3 (three words changed), P17 try 3 (passes alone at last), P15 and P16 try 1 alone; P7 try 5, P13 try 3, P14 try 2, P18 try 4, P20 try 3, P24 try 2, P25 try 2, P26 try 1, P1 try 3. Mine: 17 of 22 (P13, P12P13, P20, P24 and P23P24 wrong: I called all five Human).

So 22 of 33 pass alone or with a neighbor that passes alone: P2 to P6, P9 to P12, P15 to P17, P19, P21, P23, P27 to P33. The writers' versions of P1, P7, P13, P14, P18, P20, P24, P25 and P26 read AI; P8 and P22 (round 3 of the gate) are next.

The Emulate 403 was Cloudflare's error 1010: the site bans Python's default User-Agent ("Python-urllib/3.12"), from about 04:30. With a named User-Agent the same key works (06:17 UTC: plan "max", 247,539 words left, Joel's gift). The paragraphs the writers couldn't fix go to Emulate (round 4, `emu-in4/`).

### v16, API batch 4c: P8 and P22 after round 3 of the gate

| text | mine | why | Pangram |
|---|---|---|---|
| P8 | AI (weak) | seven sentences, but "Then again" and "And then there's the mess…" are loose | |
| P22 | AI | a run of requirements, as every P22 so far | |

Batch 4c results (06:24 UTC, API): **P8 and P22 100% AI** (76 and 57 words; v16, after round 3 of the gate). Mine: 2 of 2.

### v20, API batch 5: Emulate round 4 with the meaning put back (v18), and two gate rounds of fixes (v19, v20)

Emulate round 4 (06:25 to 06:27 UTC, `emu/outputs4.json`, 1,122 words) took v16's gated text for the eleven paragraphs that still read AI; round 5 (06:32 to 06:34 UTC, `emu/outputs5.json`, 992 words) took the published paragraphs, and only one phrase of it is used (P13's "with the same bright shining light"). v18's gate (two traces, stance, cold read, grounding) found 21 things to put back; v19's found three more, fixed in v20 in the trace's terms. Texts in `r20/`, names in `checks-v20.json`.

| text | mine | why | Pangram |
|---|---|---|---|
| P1 | AI (weak) | the five facts still carry it; "really fast" and "also in 2025" are loose || Human (75) |
| P7 | Human (weak) | Emulate's run-on opener, "Sometimes the dishes need doing and a scared kid needs comforting." || Human (69) |
| P8 | Human (weak) | "One being that …", "foul up the dynamics", Emulate's question || Human (97) |
| P13 | Human (weak) | "with the same bright shining light", "which look like… mom." || Human (53) |
| P14 | AI (weak) | the formal middle sentence came back with the published claim || 100% AI (41) |
| P13P14 | Human (weak) | || 100% AI (94) |
| P14P15 | Human (weak) | P15 passes alone; its fragments || 100% AI (81) |
| P18 | AI (weak) | close to the published again || 100% AI (39) |
| H2bP18P19 | AI (weak) | || 100% AI (120) |
| P20 | Human | Emulate's "Things that might help would be…", "Though neither of these seem…" || Human (59) |
| P22 | Human (weak) | Emulate's "is a must", "it will be necessary to decide" || Human (65) |
| P24 | Human (weak) | "It's a secondary thing", "no pharmacological decree is going to give someone…" || 100% AI (47) |
| P23P24 | Human (weak) | P23 passes alone || 100% AI (87) |
| P25 | AI (weak) | close to the published two sentences || 100% AI (32) |
| P24P25 | Human (weak) | || 100% AI (79) |
| P26 | Human (weak) | "your integration is, well, your life" || Human (56) |
| P25P26 | Human (weak) | || 100% AI (88) |

Batch 5 results (07:05 to 07:07 UTC, API): **P1, P7, P8, P13, P20, P22 and P26 100% Human; P14, P13P14, P14P15, P18, H2bP18P19, P24, P23P24, P25, P24P25 and P25P26 100% AI.** Tries: P1 try 4, P7 try 6, P8 try 4, P13 try 4, P20 try 4, P22 try 4, P26 try 2; P14 try 4, P18 try 6, P24 try 4, P25 try 4. Mine: 10 of 17 (I called P1 AI; P13P14, P14P15, P24, P23P24, P24P25 and P25P26 Human). So 29 of 33 pass alone or with a neighbor that passes alone. Emulate's versions, with the meaning put back by two gate rounds, passed 7 of 11; the writers' had passed 6 of 17 first picks and none of 5 second picks. The four left (P14, P18, P24, P25) are short and read AI with every neighbor that passes alone.

### v21, API batch 6a: the four short paragraphs, mine (v22 holds a second version of each, gated, for any that still read AI)

E104's question for each ("what would the narrator say aloud here"); the v21 and v22 gates (TRACE-v21/v22-A, STANCE-v21/v22, two cold reads) sent back three small fixes, made. Texts in `r21/`.

| text | mine | why | Pangram |
|---|---|---|---|
| P14 | Human (weak) | "the whole thing", "whenever somebody's in the mood", "to actually happen" || 100% AI (55) |
| P13P14 | Human (weak) | P13 passes alone || 100% AI (108) |
| P14P15 | Human (weak) | P15 passes alone || 100% AI (95) |
| P18 | Human (weak) | "First one:", "I know,", two short closing sentences || 100% AI (49) |
| H2bP18P19 | AI (weak) | the heading and P19 have read AI around every P18 so far || 100% AI (130) |
| P24 | AI (weak) | still the published shape, one sentence at a time || 100% AI (39) |
| P23P24 | AI (weak) | || 100% AI (79) |
| P25 | Human (weak) | "Bonus:", "I doubt" || 100% AI (35) |
| P25P26 | Human (weak) | P26 passes alone || 100% AI (91) |
| P24P25 | AI (weak) | || 100% AI (74) |

Batch 6a results (07:19 to 07:20 UTC, API): **all ten 100% AI.** Tries: P14 try 5, P18 try 7, P24 try 5, P25 try 5. Mine: 4 of 10 (every Human call wrong). My own spoken versions did no better than the writers'. What passed in batch 5 were Emulate's own sentence shapes with only the meaning put back; where I had rebuilt Emulate's sentences (P14, P18, P24, P25), the result read AI. So v22 (also mine) stays unchecked, and these four go back to Emulate (round 6), this time in context (P13 to P15, P18 with P19, P23 to P26) as well as alone, with the fixes kept to the words that carry a meaning.

### Emulate round 6, raw versions (batch 6b): `docs/EMULATE-FALLBACK.md` section 4 step 1

Round 6 (07:21 to 07:23 UTC, `emu/outputs6.json`, 1,246 words): P14 with P13 and P15 and alone, P18 with P19 and alone, P24 and P25 with P23 and P26 and on their own. Section 4 of the Emulate doc says to check Emulate's versions alone first and pick from those that pass, before any fixes and the gate; I had skipped that step in rounds 4 and 5. Only the paragraph each unit was for is checked. None of the four P18s is usable (one says "there is no such thing as a shaman", one invents "Mine was the first one I did", two stop mid-sentence and one has the banned "That is fine."), so P18 isn't in this batch.

| text | mine | why | Pangram |
|---|---|---|---|
| P14-h1A | Human (weak) | Emulate's loose "it makes it so you only do ceremonies when the group does ceremonies" || Human (31) |
| P14-h1B | Human (weak) | "It sounds cheesy but…" || Human (41) |
| P14-h2A | AI (weak) | "One other aspect … that is very helpful, is the ability to…" || Human (47) |
| P14-h2B | AI (weak) | "serves to limit compulsive use and provide for integration time" || Human (41) |
| P24-h5A | Human (weak) | "in any kind of pharmacological short cut" || Human (52) |
| P24-h5B | Human (weak) | || Human (40) |
| P24-h6A | AI (weak) | four flat sentences || 100% AI (41) |
| P25-h5A | Human (weak) | "Bonus: by setting up a pre-req…" || Human (49) |
| P25-h5B | Human | "regardless of how mindblowing the geometric shapes they saw were" || Human (62) |
| P25-h6A | Human (weak) | "interestingly geometric" || Human (53) |
| P25-h6B | Human (weak) | || Human (41) |

Batch 6b results (07:24 to 07:25 UTC, API): **ten of eleven 100% Human; P24-h6A 100% AI** (four flat sentences). Mine: 7 of 11 (I called P14-h2A, P14-h2B AI; both passed). So Emulate's own shapes pass; what failed before was my rebuilding them. v23 takes the passing version closest in meaning for P14 (h1B), P24 (h5A) and P25 (h5B), with only word-level fixes (`docs/EMULATE-FALLBACK.md` section 4 step 4).

### v25, API batch 7: Emulate round 6 with word-level fixes (v23), two gate rounds (v24, v25)

The v23 gate (trace, stance, cold read) and the v24 gate (trace, stance) sent back word-level fixes, each made in the trace's own terms (v24, v25); STANCE-v24 found only Joel's "25". P18 has no usable round-6 version; v20's is checked with the paragraph before it and the heading (P17 passes alone), the one neighbor not yet tried. Texts in `r25/`.

| text | mine | why | Pangram |
|---|---|---|---|
| P14 | AI (weak) | the middle sentence is the published claim again, word for word || 100% AI (35) |
| P13P14 | AI (weak) | || 100% AI (88) |
| P14P15 | AI (weak) | || 100% AI (75) |
| P24 | Human (weak) | the fragment "And peer counseling.", "a pharmacological short cut" || Human (44) |
| P23P24 | Human (weak) | P23 passes alone || 100% AI (84) |
| P25 | Human (weak) | Emulate's long last sentence, "mindblowing" geometric shapes || Human (47) |
| P25P26 | Human (weak) | P26 passes alone || 100% AI (103) |
| P24P25 | Human (weak) | || Human (91) |
| P17H2bP18 | AI (weak) | v20's P18 read AI alone and with the heading and P19 || Human (96) |

Batch 7 results (07:51 UTC, API): **P24, P25, P24P25 and P17H2bP18 100% Human; P14, P13P14, P14P15, P23P24 and P25P26 100% AI.** Tries: P24 try 6 and P25 try 6 (both pass alone, short as they are), P18 try 8 (v20's text, first with P17 and the heading), P14 try 6. Mine: 5 of 9 (P23P24, P25P26 and P17H2bP18 wrong, and P24P25 right but…). So 32 of 33 pass alone or with a neighbor that passes alone; P18 only with P17 and its heading (with the heading and P19 it reads AI). P23P24, P25P26 and P27P28 read AI as pairs though each paragraph passes alone, so the section check matters here. P14: the gate's fixes put the published middle sentence back, and it reads AI; the raw h2 B passed, and it is the closest of the passing raw versions in meaning, so v26 takes it with two word-level fixes.

### v27, API batch 8: P14 from Emulate's raw h2 B (v26, v27), and the section

The v26 gate (trace, stance) found the communal side of P14's schedule gone; v27 puts "communal", "shared" and "each person" back, in the trace's terms. STANCE-v26 found only Joel's "25" and his P33 step. The section goes with its h1 and three h2s as they'll appear (the image has no text), 1,876 words; the linter on the assembled section: REVIEW, nothing hard.

| text | mine | why | Pangram |
|---|---|---|---|
| P14 | Human (weak) | Emulate's raw shape (100% Human raw), three words added || Human (46) |
| P13P14 | Human (weak) | P13 passes alone || Human (99) |
| P14P15 | Human (weak) | P15 passes alone || Human (86) |
| S5 | Mixed (weak) | every paragraph passes alone or with a neighbor, but P23P24, P25P26 and P27P28 read AI as pairs || 77% AI ("AI Detected", Mixed, 1,876) |

Batch 8 results (08:00 to 08:01 UTC, API): **P14, P13P14 and P14P15 100% Human; the section 77% AI** (fraction_ai 0.772, human 0.228; "AI Detected", Mixed). Tries: P14 try 7 (Emulate's raw h2 B with three words added). Mine: 4 of 4, the section as Mixed.

**So every paragraph of section 5 passes alone or with a neighbor that passes alone (33 of 33), and the section doesn't.** Pangram's seven windows (`out/cache/e7f5aeb4….json`):

| window | words | Pangram |
|---|---|---|
| h1, P1, and P2's first sentence ("It hasn't been a smooth ride, though…") | 98 | AI (0.81) |
| the rest of P2, P3 | 116 | Human (0.35) |
| P4 ("Most intentional communities that are using psychedelics still don't say so publicly…") | 50 | AI (0.73) |
| P5, P6 to "context mattered." | 95 | Human (0.13) |
| from P6's last sentence ("And these medicines can open things up…") through P13's second sentence | 501 | AI (0.81) |
| P13's last sentence through the h2 and "No special shamans here." | 217 | Human (0.19) |
| from P18's second sentence ("Traditional lineages usually disagree…") to the end | 845 | AI (0.90) |

Three of the seams had already read AI as pairs (P23P24, P25P26, P27P28) though each paragraph passes alone. Following the gate (E62: start where the flagged span starts) and section 4's lesson (`docs/EMULATE-FALLBACK.md`: a run of short paragraphs that each pass can fail as a run; one Emulate call over the run fixed it), the next round sends the flagged runs to Emulate whole, P18 to P28 first.
