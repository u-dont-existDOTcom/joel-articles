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

Batch 7 results (07:51 UTC, API): **P24, P25, P24P25 and P17H2bP18 100% Human; P14, P13P14, P14P15, P23P24 and P25P26 100% AI.** Tries: P24 try 6 and P25 try 6 (both pass alone, short as they are), P18 try 8 (v20's text, first with P17 and the heading), P14 try 6. Mine: 6 of 9 (P23P24, P25P26 and P17H2bP18 wrong). So 32 of 33 pass alone or with a neighbor that passes alone; P18 only with P17 and its heading (with the heading and P19 it reads AI). P23P24, P25P26 and P27P28 read AI as pairs though each paragraph passes alone, so the section check matters here. P14: the gate's fixes put the published middle sentence back, and it reads AI; the raw h2 B passed, and it is the closest of the passing raw versions in meaning, so v26 takes it with two word-level fixes.

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

Over the turn (2026-10-03 04:03 onward, API batches 1 to 8, 118 checks besides the two calibration texts): mine 78 of 118.

## Joel's message of 20:51 UTC (2026-10-03)

Joel: P10 gets the proposed sentence; "P19 is a hard fail … OR is not ALSO" (I wrote "They may also be" in v1, and TRACE-v2-C marked it SAME-MEANING); P23's last sentence is his ("My reasons are given in those articles, respectively, since they need more space."); P28's "private" gets his parenthetical and "insured" goes; and on P18: "the reason that it fails should tell you how to fix it, right? What is the stumbling block exactly". v28 has his edits, the P19 fix ("Or they may be someone who…") and, from my own logic pass over all 33 paragraphs, P22's "medical and psychiatric" (published) for Emulate's "or".

### P18 diagnosis, API batch 9 (texts in `diag18/`): which sentence trips it

Every P18 so far makes the same four moves in the same order: the principle ("No special shamans"), the concession ("Traditional lineages usually disagree with me"), the other side's belief in neutral terms ("many ayahuasca and Bwiti communities believe the medicine should stay under trained lineage authority"), and a courtesy close ("I respect what these traditions have preserved, and I've learned from them"). In the section check the AI window began exactly at the concession. These checks take sentences out one at a time, with the heading and the fixed P19 (which is checked alone too, since it changed).

| text | mine | why | Pangram |
|---|---|---|---|
| diag-P19 | Human (weak) | passed with "also"; one word's logic changed | Human (78) |
| diag-H2bP18P19 | AI | as before, now with "or" in P19 | 100% AI (120) |
| diag-H2bP18noS3P19 | AI (weak) | without the courtesy close | Human (108) |
| diag-H2bP18noS2P19 | Human (weak) | without the concession and the neutral report of their belief | 100% AI (97) |
| diag-H2bS1P19 | Human (weak) | the principle alone, then P19 | Human (85) |

Batch 9 results (20:58 UTC, API, Pangram 4.0): **diag-P19, diag-H2bP18noS3P19 and diag-H2bS1P19 100% Human; diag-H2bP18P19 and diag-H2bP18noS2P19 100% AI.** Mine: 3 of 5 (I had it backwards: I blamed the concession). So the courtesy close trips it, alone: take it out and the heading, P18 and P19 read Human (108 words); keep it and take out the concession instead, and they still read AI. The section window starting at the concession was the chunk boundary, not the cause.

Why that sentence reads AI: "I respect what those traditions have preserved and have learned from them" (published) is the respectful nod a model adds after disagreeing with someone. It names a respect and a debt and fills in neither: what they preserved, what was learned. So it could close any paragraph that disagrees with any tradition. Every P18 so far (mine, the writers', Emulate's) changed its words and kept it, empty, and all of them read AI. What I can't do alone is fill it: what Joel learned from those lineages, or what they kept that he respects, is his to say.

### The gate on v29 and v30, then API batch 10 (texts in `r30/`)

v29 moved P18's respect up into the concession. Its trace (TRACE-v29-A) found two problems with that: "them" widened whom Joel says he learned from (traditional lineages in general, where the published "those traditions" follows the ayahuasca and Bwiti sentence), and the paragraph then ended on lineage authority right before P19's "My issue is with…", which reads as his verdict on those lineages. The courtesy at the end does a job there: it separates the lineages from the objection. So v30 keeps it at the end, reworded and traced clean ("I've learned from those traditions, though, and I respect what they've preserved."). Rewording it is the only move left that doesn't need Joel; I expect it to fail, since every wording so far has.

Joel's "check everything twice": two fresh logic audits of all 33 paragraphs against the published (LOGIC-v29-A forward, LOGIC-v29-B backward), with only the folder and a brief on connectives, negation, quantifiers, modals, and who does what. They agreed on P3 ("To be sure" for "therefore"), P4 ("or" for "and"), P17 ("say no, or pause" for "say no, pause, … and") and P10/P33 (Joel's own changes); A alone found P26 ("and … too … also": every effect in all five places) and "it can depend" in P3; B alone found P24's "once it's there" and P12's and P7's ambiguities (judged the same in effect, kept). The v29 trace added P22's "should be dealt with by seeking" (published "requires") and P28's "here" (published "around here"). All fixed word by word in v30 and traced again (TRACE-v30-A: none changes what a reader believes, apart from Joel's approved changes and P26, where it reads the published "and" as a list and so the "or" as a shift; the published says the weeks reveal "whether anything changed" in those places, so one is enough, which is what "or" says). STANCE-v30 flags the age (Joel's correction) and P10's new sentence (Joel's approval; the stance check reads it against P20 and P32, a point for Joel). The grounding review hit its output limit; nothing in v29 or v30 is a new paragraph, and every new sentence is Joel's or approved by him.

| text | mine | why | Pangram |
|---|---|---|---|
| P10 | Human (weak) | passed before; the new sentence is plain | Human (100) |
| H2bP18P19 | AI (weak) | the courtesy is still empty, only reworded | Mixed: 58% AI (120); the heading, P18 and P19's first two sentences AI (0.62, 67 words), the rest of P19 Human |
| P3 | Human (weak) | passed before; two words changed | Human (56) |
| P4P5 | Human (weak) | passed before; "or" to "and" | Human (104) |
| P17 | Human (weak) | passed before; a two-word question added | Human (54) |
| P22 | Human | passed before; two words | Human (60) |
| P23 | Human (weak) | Joel's sentence, plain | Human (41) |
| P22P23 | Human (weak) | | Human (101) |
| P24 | Human (weak) | passed before; three words | Human (44) |
| P26 | Human (weak) | passed before; connectives only | 100% AI (54; 0.80) |
| P28 | Human (weak) | Joel's parenthetical; "insured" gone | Human (81) |
| S5 | AI | the runs from P18 on are untouched | Mixed: 78% AI (1,910) |

Batch 10 results (22:04 UTC, API): **P10, P3, P4P5, P17, P22, P23, P22P23, P24 and P28 100% Human; P26 100% AI; H2bP18P19 Mixed (58% AI); the section Mixed (78% AI).** Mine: 10 of 12 (P26 wrong: I called it Human; H2bP18P19 I called AI, and it came back Mixed). So Joel's P23 sentence passes alone and with P22, his P28 passes, P10 passes with the new sentence, and every logic fix passed except P26's, where my "or … or … Or in" read AI (v20's "and … too … also" had passed): the fix changed the shape as well as the connective. The reworded courtesy took P18 with the heading and P19 from 100% AI to 58%, the AI window now the heading, P18 and P19's first two sentences (0.62): wording alone moves it, and not far enough.

Section windows (v30):

| window | words | Pangram |
|---|---|---|
| h1 to P2's "which is false!" | 143 | AI (0.77) |
| P2's last sentence and P3 | 71 | Human |
| P4 | 50 | AI (0.74) |
| P5 and P6 to the Global Ayahuasca Survey | 95 | Human |
| P6's last sentence to P10's first ("The deeper you go…") | 286 | AI (0.67) |
| P10's middle | 63 | Human |
| P10's new sentence to P13 | 203 | AI (0.80) |
| P14 to P17's second sentence | 147 | Human |
| P17's third sentence to P28 | 646 | AI (0.73) |
| h2c and P29 | 41 | Human |
| P30 to P33 | 213 | AI (0.84) |

Against v27 (four AI windows, 77%), P14 to P17 and h2c with P29 now read Human, and the long run from P17 to P28 is still AI.

### P26 again, API batch 11 (v31; TRACE-v31-A: both say "one or more of these places, not all", as the published does)

| text | mine | why | Pangram |
|---|---|---|---|
| P26 (v31) | Human (weak) | v20's three parts and sentence breaks back; "maybe … Maybe … Or in" carry the logic | 100% AI (56; 0.66) |
| P26-alt | Human (weak) | v20's shape with "or" in the pairs and "maybe" | 100% AI (55; 0.66) |

Batch 11 results (22:19 UTC): **both 100% AI** (0.66 each, down from v30's 0.80). Mine: 0 of 2. v20's "it'll show up … in your relationships and your daily behavior. In your sleep and your decisions, too. It's also in how well…" passed; every version that takes the "too" and the "It's also" out reads AI. The published frame is a test ("the following weeks reveal whether anything changed — in …"), and in a test the "and" lists the places to look, so v32 says the test and keeps v20's "and … too": "the weeks after will tell you whether it had any effect on you, in your relationships and your daily behavior. In your sleep and your decisions, too. And in how well…".

### P26, API batch 12 (v33; TRACE-v32-A: the "too" and "And in" sentences sat outside "whether", so they still added places where it shows; TRACE-v33-A: most readers take the five as places to look)

| text | mine | why | Pangram |
|---|---|---|---|
| P26 (v33) | AI (weak) | my own rebuild of v20's three parts ("the weeks after will show it. Look at … At …, too. And at …"); my rebuilds have mostly read AI | 100% AI (55) |

Batch 12 (22:38 UTC): **100% AI.** Mine: 1 of 1. So P26 goes back to Emulate (round 7, `emulate-runs/community-s5g`, 22:40): the traced v33 as input (i1), and the published paragraph (i2, refused: 32 words, Emulate takes 40 or more). Both i1 versions drop "without declaring a new spiritual emergency" and end on "etc"; each lists the five as places to look ("Look at your relationships, …"). Raw versions first (section 4 of the Emulate doc), API batch 13:

| text | mine | why | Pangram |
|---|---|---|---|
| emu7raw-P26-i1A | Human (weak) | Emulate's raw versions mostly pass | Human (44) |
| emu7raw-P26-i1B | Human (weak) | | Human (48) |

Batch 13 (22:41 UTC): **both 100% Human.** Mine: 2 of 2. i1A is the closer: B asks "How has your life changed", which assumes a change. v34 takes A with the meaning put back word by word: "Another" for "The other" (one of several principles), the published "Ceremony opens something." and "Did anything change?" for its "Did the ceremony open you up to anything?" (which merged the opening with the change), and the published "without declaring a new spiritual emergency" for its "etc, etc." (which also opened the list of five).

### P26, API batch 14 (v36: Emulate round 7's i1 A with the meaning put back; TRACE-v34-A and TRACE-v35-A: the five read as places to look, one or more, as published; their word-level findings made in their own terms)

| text | mine | why | Pangram |
|---|---|---|---|
| P26 | Human (weak) | the raw version passed; six word-level fixes, the published quip among them | 100% AI (46) |
| P25P26 | Human (weak) | read AI with v20's P26 | 100% AI (93) |
| P26P27 | Human (weak) | | 100% AI (88) |

Batch 14 (23:00 UTC): **all three 100% AI.** Mine: 0 of 3. The raw version passed and the fixed one doesn't, so, as with P18, the next check finds which fix trips it before any rewrite: v36 with one group of fixes undone at a time (API batch 15). The groups: F1 "Another aspect … your everyday life" (raw: "The other aspect … your life"); F2 "Ceremony opens something. Did anything change?" (raw: "Did the ceremony open you up to anything?"); F3 "in the weeks after" (raw: "over the last few weeks"); F4 "how well you handle frustration without declaring a new spiritual emergency" (raw: "how you handle frustration, etc, etc.").

| text | mine | why | Pangram |
|---|---|---|---|
| abl-P26-noF1 | AI (weak) | | Human (46) |
| abl-P26-noF2 | Human (weak) | a published short sentence then a short question: a stock rhythm | Human (48) |
| abl-P26-noF3 | AI (weak) | | 100% AI (47) |
| abl-P26-noF4 | AI (weak) | v20 passed with the quip | Human (41) |

Batch 15 (23:00 UTC): **noF1, noF2 and noF4 100% Human; noF3 100% AI.** Mine: 2 of 4 (I called noF1 and noF4 AI). So no one fix trips it: the paragraph sits near the line, and any one of F1, F2 or F4 tips it over; F3 doesn't matter. F2 (the published opening kept apart from the change) and F4 (the published quip, and a closed list of five) carry meaning; F1 ("Another … everyday") is the cheapest to give back. v37 takes noF1 as checked: "The other aspect is integration: your life." Its cost: "the other" can imply two principles, and "your life" can read as your whole life (v20's "your life" was accepted by every gate before).

TRACE-v37-A: the five read as places to look, one or more, as published; its other marks are v37's known costs ("the other aspect" with no named pair, "ordinary" and "daily" gone, the "you" voice, "how you make decisions"). v37's P26 passes alone (noF1 in batch 15 is its exact text).

### P18 with the paragraph before it, API batch 16 (v37's P18 is v30's reworded courtesy; P18 is 39 words, so it passes with a neighbor that passes alone)

| text | mine | why | Pangram |
|---|---|---|---|
| P17H2bP18 | Human (weak) | v20's P18 passed with P17 and the heading; P17 now passes alone with "To pause?" | Human (96) |

Batch 16 (23:11 UTC): **Human.** Mine: 1 of 1. So at v37 every paragraph passes alone or with a neighbor that passes alone (P18 with P17 and its heading).

Over the turn (Joel's message of 20:51; API batches 9 to 16, 30 checks): mine 19 of 30.

## Joel's message of 01:18 UTC (2026-10-04)

On P18, what he learned from those lineages: "the need for sacred ritual practices even if i don't do them myself, i see a lot of people need the rituals and the look and vibe to match before they feel comfortable doing this kind of thing. i've learned that the spirit realms are quite a mixed bag, you can have a shaman who heals people very well and yet he also may take money to send evil spirits to kill someone. i've learned that people do very often decide they are ready to do ceremonies long before they are really trained and prepared. i've learned what to do, and what not to do, based on observing the various traditions. and i'm sure i could still learn a lot from them and they could still learn a lot from me." On P33: "sure cut it" (", not just escaping society"). And "continue": PR #135 may merge at the end of this turn.

v38: P18's empty courtesy becomes his specifics, in his words wherever they read in place (his straight apostrophes): "I've learned what to do, and what not to do, from watching those traditions, though." then the rituals, the spirit realms, the readiness, and his closing "I'm sure I could still learn a lot from them, and they could still learn a lot from me." P33 without the tail.

### The gate on v38 to v40, then API batch 17 (texts in `r40/`)

TRACE-v38-A and STANCE-v38 marked v38's P18 as having dropped the published respect ("I respect what those traditions have preserved"): his answer adds to it, so v39 puts it back. The cold read couldn't place the spirit realms or the "And that…" fragment, and read "them" in the last sentence as the untrained people; v39 and v40 frame each lesson as his ("I see…", "I've also seen that…"), give the rituals his word "sacred", and say "from those traditions". The stance check's other marks are his answer itself (new claims about rituals, spirit realms, readiness, and that the lineages could learn from him): his to keep. Two notes for him: "do ceremonies" (lead them or take part?), and the rituals line beside P27's "That all matters more than ceremony aesthetics" (not a contradiction: comfort and safety). v38 also gave P26 back "Another" for "The other": v37 had made three paragraphs open with "The" (B13).

| text | mine | why | Pangram |
|---|---|---|---|
| P18 | Human (weak) | most of it is his own words, and specific | Human (154) |
| H2bP18P19 | Human (weak) | the empty courtesy is gone | Human (235; 0.22) |
| P33 | Human (weak) | passed with the tail | Human (66) |
| P26 | AI (weak) | "Another aspect is" is a stock transition, and batch 15 left open which word tipped v36 | 100% AI (45) |
| S5 | AI | the runs from P19 on and P30 to P33 are untouched | Mixed: 68.5% AI (2,012) |

Batch 17 (01:48 UTC): **P18, H2bP18P19 and P33 100% Human; P26 100% AI; the section Mixed, 68.5% AI.** Mine: 4 of 5 (P26's "Another aspect" read AI, as I called it, so "The other aspect" stays and the B13 "The" count is fixed elsewhere). So Joel's specifics fixed P18: with the heading and P19, 100% AI (empty courtesy) → 58% (reworded) → Human (his lessons). In the section, P16's end to P18 now reads Human (238 words).

Section windows (v40):

| window | words | Pangram |
|---|---|---|
| h1 to P2's "which is false!" | 143 | AI (0.77) |
| P2's last sentence and P3 | 71 | Human |
| P4 | 50 | AI (0.74) |
| P5 and P6 to the Global Ayahuasca Survey | 95 | Human |
| P6's last sentence to P10's first | 286 | AI (0.67) |
| P10's middle | 63 | Human |
| P10's last sentence to P13 | 203 | AI (0.79) |
| P14 and P15 to "drive away from the ceremony" | 68 | Human |
| P15's last sentence and P16's first two | 46 | AI (0.60) |
| P16's last sentence to P18 | 238 | Human (0.18) |
| P19 and P20's first sentence | 110 | AI (0.89) |
| P20's rest to P22's fourth sentence | 112 | Human |
| P22's last sentence to P33 | 578 | AI (0.87) |

### The section pass: Emulate round 8 (`emulate-runs/community-s5h`, 01:52 UTC), the AI windows as runs of whole paragraphs

v41 is v40 with P26's "The other aspect" back. Every AI window at v40 goes to Emulate as one unit of whole paragraphs, two calls each (section 4's run lesson): u1 P1–P2, u2 P4, u3 P7–P9, u4 P11–P13, u5 P15–P16, u6 P19–P20, u7 P22–P28, u8 P29–P33 (`emu/units8.json`). Raw versions first (API batch 18), then the closest passer per unit with the meaning put back word by word: every logic fix of v29 to v40, Joel's sentences exactly (P23's last, P28's parenthetical, P33's step), the links.

API batch 18: the 16 raw versions as returned (`api18.json`, built on the laptop by `community-s5h/make_raw_batch.py`, 3,075 words). A slip: the batch script started the check in the same command, before these predictions were written; I wrote them before reading any result.

| text | mine | why | Pangram |
|---|---|---|---|
| emu8raw-u1A | Human (weak) | Emulate's raw versions passed 12 of 13 in rounds 6 and 7 | Human |
| emu8raw-u1B | Human (weak) | | Human |
| emu8raw-u2A | Human (weak) | | Human |
| emu8raw-u2B | Human (weak) | | Human |
| emu8raw-u3A | Human (weak) | | Human |
| emu8raw-u3B | Human (weak) | | Human |
| emu8raw-u4A | Human (weak) | | Human |
| emu8raw-u4B | Human (weak) | | Human |
| emu8raw-u5A | Human (weak) | | Human |
| emu8raw-u5B | Human (weak) | | Human |
| emu8raw-u6A | Human (weak) | | Human |
| emu8raw-u6B | Human (weak) | | Human |
| emu8raw-u7A | AI (weak) | 360 words, the longest unit, and long runs have read AI where their paragraphs pass | Human |
| emu8raw-u7B | AI (weak) | | Human |
| emu8raw-u8A | Human (weak) | section 4's 250-word run passed raw | Human |
| emu8raw-u8B | Human (weak) | | Human |

Batch 18 (01:56 UTC): **all 16 raw versions 100% Human**, the 411- and 460-word runs included. Mine: 14 of 16 (u7 A and B I called AI). Their meaning drifts a long way (u6 A invents "my intuition says X, and I'm smarter than you"; u8 A has the training ground "alleviating my concerns"; u7 A promises safety posts "soon"; u7 B links "here, here, and here").

Before rebuilding runs from them, a look at what the runs carry: v41's paragraphs score almost nothing alone (from the cache: P22 0.006, P23 0.001, P24 0.002, P25 0.002, P27 0.099, P28 0.000, P30 0.335, P33 0.113; the highest anywhere is P26 at 0.44), yet the window from P22's last sentence to P33 reads 0.87. So no single paragraph is near the line there; it is the run. API batch 18b checks where: the window as Pangram cut it, its two halves, and the window with the paragraph-opening links taken out ("In addition,", "Also,", "As a bonus,", "The other aspect is"), a diagnostic only.

| text | mine | why | Pangram |
|---|---|---|---|
| dW13-0 (the window as cut) | AI | it read 0.87 in the section | 100% AI (568; 0.89) |
| dW13-1 (P23 to P28) | AI (weak) | six short "principle" paragraphs in a row | 100% AI (301; 0.98) |
| dW13-2 (h2c, P29 to P33) | AI (weak) | P30's anaphora ("And you run into…" ×3) | 100% AI (248; 0.95) |
| dW13-3 (the window, links out) | AI (weak) | if the links are the run's tell, this flips | 100% AI (559; 0.90) |
| v41-S5 (the section with v41's P26) | Mixed, about 65% AI | v40's P26 ("Another aspect") read AI alone and sat inside this window; v41's passes alone | Mixed: 68.5% AI, the same windows |

A catch while building these: v40's last window held v40's P26, which read 100% AI alone, so every text above takes v41's P26 ("The other aspect", Human alone), and the batch adds the whole section at v41.

Batch 18b (01:59 UTC): **all four diagnostics 100% AI; v41's section the same as v40's (68.5%).** Mine: 4 of 5 (I gave the halves AI (weak), and P23 to P28 came back 0.98). So paragraphs that score almost nothing alone (P23 to P28: 0.001, 0.002, 0.002, 0.44 for v40's P26, 0.099, 0.000) read 0.98 as a 300-word run, and taking out the paragraph-opening links changes nothing (0.90). Passing alone tells little about a run; the run has to be checked as a run. Emulate's raw runs of the same content read 100% Human.

v42 rebuilds the last window from round 8's raw runs (u7 A for P22 to P28; u8 A for P29 to P31 and P33, u8 B for P32, whose A version reversed the paragraph), with the meaning put back word by word: P22's "are ever casual", the reason ("since the authority is spread around") and the musts; Joel's P23 sentence exactly, with the links; P24's "can deepen … can't be a pharmacological short cut" (A had "should", and a "not Y" tail); P26's opening apart from the change and the five places to look; P27's "drug interactions" (A had "screening people for appropriate interaction"), "They matter more than ceremony aesthetics" and the safety material as it is now (A promised posts "soon"); P28's written record ("you need to write down"), Joel's parenthetical exactly, "is information"; P30's "can come with" (A had "often"), the belief "My love can heal anyone", "sincerely want to change but keep choosing the opposite", "a crisis" (A had "such fucked up lives"); P31's "terrible"; P32's "can", "promise too much", the math done only once people depend on them, the sections' purpose; P33's "it can become useful", "sometimes", Joel's step, and the objection answered (A had the training ground "alleviating my concerns"). "The urge" became "That urge" (P31) and "The use of medicine" became "Using medicine" (P24), so no three paragraphs open with "The".

API batch 19, diagnostics before the gate (nothing is adopted on them; the gate runs before any of this goes in): the rebuilt runs and the section.

| text | mine | why | Pangram |
|---|---|---|---|
| v42-u7run (P22 to P28) | Human (weak) | the raw run read Human; about fifteen word-level fixes | |
| v42-u8run (h2c, P29 to P33) | AI (weak) | P32 and P33 needed close to a rebuild | |
| v42-S5 | Mixed, about 45% AI | the other AI windows are untouched | |

Batch 19 (02:06 UTC): **both rebuilt runs 100% Human (0.044 and 0.001); the section Mixed, 36.1% AI (from 68.5%).** Mine: 2 of 3 (I called the second run AI). The section's AI windows at v42: h1 to P2 (0.79), P4 (0.74), P6's last sentence to P10's first (0.67), P10's last sentence to P13 (0.79), P15's last sentence and P16's first two (0.58), and P25's second sentence alone (50 words, 0.82; inside the run it read Human). P19 and P20 now sit inside a 600-word Human window.

TRACE-v42-A and -B (P22 to P33): the findings made word by word in v43 (P22: "reviewing medications and combinations", "deciding before anybody takes anything", "professional help or emergency care"; P23: "medicines and protocols that I see as…" without "some"; P24: "the other pl/ork that comes first" for "that I list above", "honest relationship"; P25: "it weeds out the experience collectors"; P27: "being disciplined about the dose"; P29: "really common", one urge, "whatever just opened up for them"; P30: "and I've felt that too", "You come back believing love can heal anyone", "people who…" without "a lot of", "more than your enthusiasm can hold"; P31: "That call"; P32: "formed during", "too many people too fast"; P33: "can be", "the practices", "another experiment"). Kept, with reasons: Joel's own changes (P23's last sentence, P28's parenthetical and "insured" out, P33's step), "integration: your life" (every gate since v20), "need to write down" (published: "Legality needs a written answer"). The linter failed P22 for two lists of three; its first clause is now a sentence of its own.

v43 also rebuilds the other AI windows from round 8: P1 and P2 from u1 A ("Key here is that…", the dates, "enacted", "lazily", the links back); P4 from u2 A with its specifics back (neighbors imagining chaos, insurers who might drop them, officials who may not understand the distinctions; "and"); P7 to P9 from u3 B (A invented "Like aikkh said"; B's P7 needed its claims back: collecting ceremonies and origin stories without being able to apologise, and insight that doesn't do the dishes or comfort a scared kid; P8's "In my experience" and "as a community"; P9's "an insight needs somewhere to land" and the people who held you noticing what happens); P11 to P13 from u4 B ("already has a cosmology to explain everything you say", "may be someone you've known for years", "You need someone…", "Your peers can also…", "insight and … convincing nonsense"); P15 and P16 from u5 B (the group arranges the childcare; raves' intimacy before trust without "can be great"; no "really amazing"). P19 and P20 stay as they are.

API batch 20, diagnostics before the gate:

| text | mine | why | Pangram |
|---|---|---|---|
| v43-u1run (h1, P1, P2) | Human (weak) | the raw run read Human; links and dates back | Mixed: 57% AI (164) |
| v43-P4P5 | Human (weak) | | Human (109) |
| v43-P4 | AI (weak) | its specifics back in one sentence, a list of four | Human (53) |
| v43-u3run (P7, P8, h2a, P9) | AI (weak) | P7 is nearly my own rebuild | 100% AI (221) |
| v43-u4run (P11 to P13) | Human (weak) | | Human (154) |
| v43-u5run (P15, P16) | Human (weak) | | Human (108) |
| v43-u7run (P22 to P28) | Human (weak) | the trace's fixes were small | Mixed: 11% AI (409) |
| v43-u8run (h2c, P29 to P33) | Human (weak) | | Human (287) |
| v43-S5 | Mixed, about 20% AI | | **Human: 4.6% AI** (2,090) |

Batch 20 (02:26 UTC): **the section reads Human for the first time: 4.6% AI**, two small windows left: P11's last sentence with P12's first (53 words, 0.57), and P25's second sentence alone (50 words, 0.76). Everything else, 2,000 words, sits in three Human windows (0.21, 0.10, 0.003). Mine: 6 of 9 (u1's run alone came back Mixed and u3's AI, though both read Human inside the section; u7's run Mixed at 11%). So a run's result depends on what Pangram's windows hold: P7 to P9 read 100% AI as a run of their own and Human inside a 750-word window. The section, checked as a section, is the test that matches Joel's; the runs alone are a guide.

Next: the gate on v43 (four traces, two logic audits, the stance check, a cold read), then each changed paragraph alone, then the two small windows.

### The gate on v43, then v44 and API batch 21

TRACE-v43-A to -D, LOGIC-v43-A and -B, STANCE-v43 and the cold read, against the rebuilt paragraphs. Fixed word by word in v44, in their terms: P1 "in a few jurisdictions" out (it narrowed the claim; both audits), "authorized psychiatrists limited access" (A's "via" moved the access); P2 "possessing small quantities for personal use"; P4 the secrecy back as a claim about most communities, with "even where the law allows some use" on the risks, "still", "parents worried about children"; P7 "hate doing the work"; P8 "can lower … and create strong bonds", "too", "tell the good from the bad" (A: "separate"); P9 the people who held you "can also notice" (the cold read stumbled on "there to notice"); P11 the contrast with the commercial alternative and "often" back; P12 "someone who's known you", "This matters even more", screening and watching tied to iboga-type experiences; P13 the peers check and the friends tell (not "help you"), "genuine insight", "which parts look like … and which look like… mom" (the cold read couldn't place "mom"); P15 "sit quietly", "obvious" out; P16 "inconvenient habits" (B had "bad habits" put up with); P26 "Then there's integration" (the cold read and two reviewers couldn't place "The other aspect of this"); P30 "and then you meet" three kinds of people, "and", "grandiosity" without "a degree of" (both audits: the rebuild had the belief correcting itself and an either/or); P32 "recruit too fast", "can end up"; P33 "if people are training there…" (the stance check: "living in a community in order to train" narrowed why people live there). Kept, with reasons: Joel's own changes (P10's sentence and "25", P18's lessons, P23's sentence, P28's parenthetical and "insured" out, P33's step), P3's wider advice he approved, wording every gate since v20 accepted ("integration: your life", P22's "not … ever casual", the "you" voice in P26).

| text | mine | why | Pangram |
|---|---|---|---|
| v44-S5 | Human (weak) | about fifteen fixes moved sentences back toward v41's, which read AI in runs | Mixed: 10.2% AI (2,070) |
| v44-P4 | Human (weak) | | Human (50) |
| v44-P30 | AI (weak) | the published triad is back | Human (66) |

Batch 21 (03:00 UTC): **the section Mixed, 10.2% AI** (v43: 4.6%); P4 and P30 pass alone. Mine: 2 of 3 (I called P30 AI). Four small AI windows: P4's second sentence (39 words, 0.65), P6's last sentence with P7's first two (49, 0.64), P11's last two sentences with P12's first (82, 0.75), and P25's second sentence again (50, 0.84). The windows are small, 40 to 80 words, and every change upstream moves the cuts downstream (P4 grew by a sentence, and the windows after it moved), so a fix is judged by the section, not by where the window fell last time. The meaning fixes that read AI are the ones that brought back v41's or the published phrasing (P4's split, P11's "commercial alternative", P12's first sentence).

API batch 22 tries other wordings for each of the four, checked the way Pangram cut them (diagnostics; the chosen wording goes through the trace before it goes in):

| text | mine | why | Pangram |
|---|---|---|---|
| dA1: P4 with the risks first, "so most … are still not open about it" | Human (weak) | Emulate's opener kept, the logic right | Human (0.21) |
| dA2: v43's P4 (Emulate's order) | Human | passed alone at v43 | Human (0.003) |
| dB1: P6's last sentence and P7's first two, "can't stand doing the work" | Human (weak) | | 100% AI (0.65) |
| dB2: the same with v43's "don't want to do the work" | Human (weak) | it sat in a Human window at v43 | 100% AI (0.91) |
| dC1: P11 and P12 with Emulate's "It's very different from paying someone you don't know…" and "already has a cosmology ready…", and P12 "Having someone who's known you for years as your sober sitter can make the difference between being watched and being held" | Human (weak) | closer to Emulate's B | Human (0.04) |
| dD1: P25's second sentence, Emulate's B | AI (weak) | | Human (0.000) |
| dD2: P25's second sentence, v41's | Human (weak) | passed inside P25 alone at v24 | Human (0.001) |
| dD3: P25's second sentence, a plainer one ("Someone who won't put six months into…") | AI (weak) | mine | 100% AI (0.84) |

Batch 22 (03:03 UTC): mine 5 of 8 (dB1 and dB2 I called Human; dD1 AI). So P4 with the risks first passes and keeps the logic; P25's second sentence passes in v41's wording (vetted since v24) and in Emulate's B, not in Emulate's A, which stayed in v42 to v44; the P11–P12 window passes in Emulate's B wording with the meaning in it; and the P6–P7 window reads AI whichever word stands for "hate", so the trigger is elsewhere in those three sentences.

API batch 23:

| text | mine | why | Pangram |
|---|---|---|---|
| dB3: P6's last sentence, P7's first, and A's question ("You've got 12 ceremonies and 6 origin stories, but you can't say sorry to your housemate?") | Human (weak) | Emulate's A shape | 100% AI (0.67) |
| dB4: P6's last sentence and v41's first P7 sentence | AI (weak) | | AI (0.27) |
| dB5: P7's first two sentences without P6's | Human (weak) | if P6's last sentence is the trigger | 100% AI (0.70) |
| dC2: dC1 with "It's very different from what often happens instead, paying someone you don't know…" | Human (weak) | "often" back | Human (0.04) |

Batch 23 (03:05 UTC): mine 2 of 4. P7's own first two sentences read AI without P6's (0.70), so they're the trigger; v41's first sentence with P6's last reads 0.27 (labelled AI). Emulate round 9 on P7 alone (`community-s5i`) came back unusable (A: "your community based on those peak experiences is shit"; B: "you're stuffed", "you came from blah blah land"). At v43 the same P7 sat inside a Human window; the cuts moved when P4 grew a sentence. v45 puts P4 back to one sentence (dA1), takes the passing wordings for P11–P12 (dC2) and P25 (v41's), and leaves P7 as v44 has it, to see where the cuts fall.

| text | mine | why | Pangram |
|---|---|---|---|
| v45-S5 | Human (weak) | | **Human: 8.1% AI** (2,056) |
| v45-P11 | Human (weak) | | Human (58) |
| v45-P12 | Human (weak) | | Human (53) |
| v45-P25 | Human | v41's, passed alone at v24 with "As a bonus" | Human (54) |

Batch 24 (03:07 UTC): **the section Human, 8.1% AI**; P11, P12 and P25 pass alone. Mine: 4 of 4. Three small AI windows: P4 (51 words, 0.59), P11's last two sentences with P12's first (79, 0.80) and P13's last two (41, 0.63). P6 to P11's first sentence and everything from P14 to the end (1,231 words) read Human. Two of the three windows had passed as texts of their own (dA1 0.21, dC2 0.04): the same words score differently inside the section, so the checks that decide now carry their neighbors.

API batch 25, the three spots with their neighbors (P3 to P5; P10 to P14):

| text | mine | why | Pangram |
|---|---|---|---|
| ctx4-v45 (P3, v45's P4, P5) | AI (weak) | P4 read AI in the section | Mixed: 35% AI (P4 0.57) |
| ctx4-b (P4 in Emulate's order, the "even where" on the concerns) | Human (weak) | | Human (0.01) |
| ctx4-v43 (v43's P4) | Human (weak) | it sat in a Human window at v43 | Human (0.01) |
| ctx11-v45 (P10 to P14 at v45) | AI (weak) | | 100% AI (0.81) |
| ctx11-v43 (P10, v43's P11 to P13, P14) | AI (weak) | v43 had an AI window at P11/P12 too | Human (0.32) |
| ctx11-raw (P10, Emulate's raw P11 and P12, v43's P13, P14) | Human (weak) | raw | Human (0.09) |

Batch 25 (03:09 UTC): mine 5 of 6 (ctx11-v43 I called AI; it read 0.32). With their neighbors, P4 in Emulate's order with the "even where" on the concerns reads Human (0.01) and keeps the logic, so v46 takes it. P10 to P14 read 0.81 with v45's P11 to P13 and 0.32 with v43's: the gate's fixes there (the "commercial alternative", "This matters even more", "genuine", "which parts look like…") pushed them over. v46 takes v43's three paragraphs with only the fixes that change what a reader believes, in the fewest words: P12 "someone who's known you for years" (who knows whom) and "For those you need someone to…" (iboga-type experiences, not every ceremony); P13 the peers check and the friends tell, without "help you", and "… mom" as the punchline (the cold read couldn't place "mom"). Left as v43 had them, with reasons: P11's "It's very different from paying someone you don't know…" (the contrast is still with paid strangers; no claim that all paid care is strangers), P12's "This is especially true", P13's "insight" without "genuine" (the contrast with "convincing nonsense" carries it).

| text | mine | why | Pangram |
|---|---|---|---|
| ctx11-v46 (P10, v46's P11 to P13, P14) | Human (weak) | v43's wording with four small fixes | Human (0.16) |

Batch 26 (03:11 UTC): mine 1 of 1. P10 to P14 read Human (0.16, 307 words) with v43's P11 to P13 and the four fixes, so v46 = v45 with P4b and these three paragraphs. Lint on v46: REVIEW, no FAIL (the REVIEW lines are the ones kept with reasons before; P12 and P13 each add a B2 "the difference between" contrast, which is Joel's published wording in both).

API batch 27, the whole section at v46 (written 03:17 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| v46-S5 | Human (weak) | both v45 AI spots passed with their neighbors (ctx4-b 0.01, ctx11-v46 0.16); the rest is v45's, which read Human; the cuts will move again | **Human: 2.4% AI** (2,043) |

Batch 27 (03:16 UTC): mine 1 of 1. **The section reads Human, 2.4% AI**: P4 and P13 now sit in Human windows. One AI window is left, 54 words at 0.62: P11's last sentence ("Sometimes they're great, but sometimes the person with the feather has only known you for 4 hours and already has a cosmology to explain everything you say.") with P12's first ("In a community, your sober sitter may be someone who's known you for years, and you feel the difference between being watched and being held."). The same seam read AI inside the section at v43 (53 words, 0.57), v44 (82, 0.75) and v45 (79, 0.80), with three different P12 first sentences, and Human every time P10 to P14 went alone (0.32, 0.16). Both sentences carry a clause the meaning restoration brought back from the published text ("already has a cosmology … everything you say", "the difference between being watched and being held"); Emulate's raws had dropped both. Sections 2 to 4 went in at 100% Human, so this window gets an ablation before any rewrite (EMULATE-FALLBACK: find the sentence first), in the section, since the seam only trips there.

API batch 28, ablations in the whole section (written 03:24 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| abl-11: v46 without P11's last sentence | Human, no AI window (weak) | the cosmology clause is the one in all four AI seams | Human: 9.4% AI (2,016) |
| abl-12: v46 without P12's first sentence | Human with an AI window left (weak) | P12's first sentence changed from v43 to v46 and the seam stayed AI | Human: 4.3% AI (2,018) |

Batch 28 (03:22 UTC): mine 0 of 2 on the windows (both sections read Human, as called). Without P11's last sentence the seam got worse: one AI window from P10's emoji to the end of P13 (160 words, 0.71), so the cosmology sentence isn't the trigger; without P12's first sentence the seam reads Human, so that sentence (with "the difference between being watched and being held") is the likelier one. Both ablations also opened windows that v46 doesn't have: P17's last four sentences (42 words, 0.78 and 0.62) and P19's last sentence with P20's first (48 words, 0.69). Those sentences sit inside a 1,306-word Human window at v46. So the section's small windows are where the cuts happen to fall: taking one sentence out upstream moves every cut after it, and a spot that reads Human in one cut reads AI in another. Lesson for the ledger: in a long section, a 40 to 60 word AI window is a property of the cut as much as of the words; check a fix in the whole section, and judge the section by its verdict, not by chasing every small window.

The gate on v46 (TRACE-v46-A to -C, LOGIC-v46-A and -B, STANCE-v46; the cold read stopped at the 64k output limit and runs again on v47). Fixed word by word in v47: P4 "still" back (TRACE-A: dropped; the v43 gate had asked for it); P12 "This is especially important" (TRACE-B and both audits: "especially true" can read as the feeling being stronger on iboga; published "This matters especially"; "important" is Emulate A's word); P13 "may notice the difference" (TRACE-B, both audits, the stance check: "can tell" asserts an ability; published "may notice"). Everything else they raised is Joel's own content or kept with a reason (the list is in the reply and STATUS).

API batch 29 (written 03:59 UTC, before the call), a diagnostic while the small gate runs on v47's three fixes:

| text | mine | why | Pangram |
|---|---|---|---|
| v47-S5 | Human, with the P11/P12 seam window still there (weak) | P11 and P12's first sentence unchanged; "still" in P4 moves the cuts by one word | **Human: 2.4% AI** (2,044) |

Batch 29 (03:59 UTC): mine 1 of 1. v47 reads like v46: Human, 2.4% AI, the same seam window (P11's last sentence with P12's first, 54 words, 0.65); the three fixes sit in Human windows.

The small gate on v47 (TRACE-v47-A, LOGIC-v47-A on P4, P12 and P13; the cold read of the whole section, SENSE-v47.md). New findings, fixed word by word: P4 "not open about it" can read as secrecy toward everyone (published "avoid saying so publicly") → "not public about it"; "concerns from" insurers and officials gives them concerns the published doesn't give them → "possible trouble … from"; P12's one "someone" to screen and watch reads as the sitter doing the medical screening (published: no one named) and "watch you" right after "being watched" makes the cold reader stop → "For those you need to be properly screened beforehand and monitored continuously"; the cold read can't place P11's "It" until P12 → "Support from people you trust is very different from…" (v49 only; v48 keeps "It's"). Kept with reasons: P13's "the difference between new understanding and… mom" (the friends notice which is which; the published's part-by-part "which parts resemble" read AI at v44 and v45), P13's "can give you" (published "produce"), "A few friends", P12's "you feel the difference" (the published's "Being watched and being held feel different").

API batch 30 (written 04:24 UTC, before the call), diagnostics while the gate runs on v49's changes:

| text | mine | why | Pangram |
|---|---|---|---|
| v48-S5 (P4, P12's last sentence) | Human, the seam window still there (weak) | P12's first sentence unchanged | Human: 2.4% AI (2,042) |
| v49-S5 (v48 and P11's "Support from people you trust…") | Human, the seam window still there (weak) | the anchor brings back a published noun phrase next to the seam | **Human: 0% AI** (one window, 0.16) |

Batch 30 (04:20 UTC): mine 1 of 2 (v49 I called with the seam window; it read 0%). **v49 reads 100% Human: one window over the whole section at 0.16.** v48 keeps the seam window (54 words, 0.74). The one difference is P11's second sentence: with "Support from people you trust is very different from…" in place of "It's very different from…", the seam reads Human. So the cold reader's "It" with no referent and Pangram's seam were the same sentence's problem, seen from two sides.

The small gate on v49 (TRACE-v49-A, LOGIC-v49-A on P4, P11, P12; SENSE-v49 on the whole section). P11 and P12 now read OK to the cold reader. New findings: P11 "very different" (published "is different from": degree raised, LOGIC CHANGED; v44 had dropped "very" and v46's return to v43's P11 brought it back unnoticed); "Sometimes they're great" can now take three antecedents (LOGIC, TRACE); "often" still missing (LOGIC CHANGED, as at v43). P29's "for them" (LOGIC-v46-B, SENSE-v49: "them" first reads as the others). Kept with reasons: P4's participles under "possible trouble" (both audits AMBIGUOUS: "possible" governs the whole phrase; four "may" clauses are the published's list shape), P12's "you feel the difference".

API batch 31 (written 04:38 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| v50-S5: v49 with "very" out, "paying people you don't know" (plural, so "they" takes the nearest plural), P29 "whatever just opened up" | Human, 0% (weak) | three small word changes; the seam's fix (the anchor) stays | Human: 2.4% AI (2,044) |
| v51-S5: v50 with ", which is often the alternative" after P11's second sentence | Human with an AI window at the seam (weak) | "often" brought the window back at v44 and v45 | **Human: 0% AI** (one window, 0.15) |

Batch 31 (04:35 UTC): mine 0 of 2, both the wrong way round: v50 (no "often") has the seam window back (54 words, 0.58), and **v51, with ", which is often the alternative", reads 100% Human (one window, 0.15)**. So the published's hedge is back and the section passes with it. The seam is where P11's second sentence ends and its third begins; what reads AI there isn't one phrase, so a fix is judged in the whole section, as batch 28 showed.

Paragraphs already checked alone in their v51 text (the API cache, by hash): P3 (0.35), P6 (0.0), P10 (0.25), P14 (0.0, 46 words), P17 (0.04), P18 (0.03), P19 (0.30), P20 (0.0), P21 (0.03, 35 words), P25 (0.0), P30 (0.23), and the heading with P18 and P19 (0.22). Every other paragraph changed after its last alone check (Emulate round 8 and the gates since), so they all go now.

API batch 32, the paragraphs alone (written 04:37 UTC, before the call; the gate runs on v51's P11 and P29 at the same time, and anything it changes is checked again):

| text | mine | why | Pangram |
|---|---|---|---|
| v51-P1 | AI (weak) | h1 to P2 read 57% AI as a run at v43 | Human (0.12) |
| v51-P2 | Human (weak) | | Human (0.0) |
| v51-P4 (50 words) | Human (weak) | P4b passed with P3 and P5 | Human (0.01) |
| v51-P5 | Human | unchanged since v41 | Human (0.0) |
| v51-P7 | AI (weak) | its first two sentences read 0.70 alone (batch 23) | **100% AI (0.97)** |
| v51-P8 | Human (weak) | | Human (0.0) |
| v51-P9 | AI (weak) | P7 to P9 read 100% AI as a run at v43 | Human (0.0) |
| v51-P11 | Human (weak) | | Human (0.04) |
| v51-P12 | Human (weak) | | Human (0.04) |
| v51-P13 (47) | Human (weak) | | Human (0.0) |
| v51-P15 | Human | | Human (0.0) |
| v51-P16 (48) | Human | | Human (0.0) |
| v51-P22 | Human (weak) | | Human (0.03) |
| v51-P23 (45) | Human (weak) | | Human (0.0) |
| v51-P24 (49) | Human (weak) | | Human (0.04) |
| v51-P26 | Human (weak) | | **100% AI (0.62)** |
| v51-P27 (40) | Human (weak) | | Human (0.0) |
| v51-P28 | Human (weak) | | Human (0.0) |
| v51-P29 (40) | Human (weak) | | Human (0.01) |
| v51-P30P31 (P31 is 16 words; P30 passed alone) | Human | | Human (0.22) |
| v51-P32 | Human (weak) | | **100% AI (0.86)** |
| v51-P33 | Human (weak) | | Human (0.0) |

Batch 32 (04:38 to 04:40 UTC): mine 18 of 22 (P1 and P9 I called AI, and both passed; P26 and P32 I called Human, and both read AI). **19 of 22 pass alone; P7 (0.97), P26 (0.62) and P32 (0.86) read 100% AI alone**, though all three sit in Human windows inside the section. The other short ones pass alone (P13, P16, P23, P24, P27, P29), and P31 with P30. So the per-paragraph rule and the section disagree for these three: the versions that fixed the section's windows (Emulate round 8, v43) fail alone; the earlier versions passed alone (v20's P7, 0.0, batch 5; v37's P26, 0.0, batch 15) and sat in AI windows at v40. P32 never passed alone in the API record (v9's P31P32 and v51's both 100% AI).

Next: v20's P7 and v37's P26 body (with "Then there's integration", the v43 cold read's fix for "The other aspect") into the section; P32 to Emulate (round 10, `emulate-runs/community-s5j`), raw versions alone first. Then the gate on every paragraph that changes, then the section.

Emulate round 10 on P32 (`emulate-runs/community-s5j`, v51's P32 as input, two calls; balance 241,083 → 240,963): A invents "like many of the earliest intentional communities" and turns the paragraph into a pointer to later sections (unusable); B keeps the shape: "Many of the groups … make the mistake of expanding to fast and taking on more than they can handle. They don't get around to thinking about how much need they have the capacity to deal with until they already have a number of people depending on them. Read the sections below … to see if they're helpful to avoiding this problem." Its meaning drifts: "many" and "make" (published: a group "can"), "taking on more than they can handle" (published: "promise too much"), "don't get around to" (certain), and the sections' purpose. P32-Br1 is B with those put back word by word: "can make the mistake of recruiting too fast and promising too much", "may not get around to", the purpose ("partly there to protect the original generosity from that first rush").

API batch 33 (written 04:50 UTC, before the call), the three paragraphs that fail alone:

| text | mine | why | Pangram |
|---|---|---|---|
| P26-c1: v37's body (passed alone, batch 15) with "Then there's integration: your life." | Human (weak) | only the opener differs from a text that passed | 100% AI (0.80) |
| v41-P32 (the round-8 input, never checked alone) | AI (weak) | close to the published shape | Human (0.27) |
| emu10raw-P32-B | Human | raw versions mostly pass | Human (0.0) |
| P32-Br1 | Human (weak) | B's sentences with the meaning back; the last clause is the published one | Human (0.0) |

Batch 33 (04:45 UTC): mine 3 of 4 (I called v41's P32 AI; it passed at 0.27). P32 passes alone in two versions: v41's (the round-8 input: "A group that begins in collective spiritual euphoria can recruit too quickly and promise too much, and only do the math on how much need it can absorb once several people already depend on it. The sections on capacity and on membership, later on in this article, are partly there to protect the original generosity from that first rush.") and Br1 (0.0). v41's is the closer one in meaning ("do the math" for "discover arithmetic", "can" over all three verbs, no "make the mistake", no "heady"), so it goes into the section first. P26's opener decides it: "The other aspect is" passed (batch 15), "Another aspect is" (batch 17) and "Then there's" (here, 0.80) read AI on the same body. Three more openers, each anchored without "other" (the cold reader couldn't place "The other aspect"):

API batch 34 (written 04:52 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| P26-c2: "As for integration, that's your life." and v37's body | Human (weak) | a spoken opener | 100% AI (0.64) |
| P26-c3: "Integration is your life." and v37's body | AI (weak) | the published shape ("Integration is ordinary life.") | 100% AI (0.61) |
| P26-c4: "Afterwards comes integration: your life." and v37's body | AI (weak) | a stock transition, like the two that failed | 100% AI |

Batch 34 (04:46 UTC): mine 2 of 3. All three openers read AI on v37's body (0.61 to 0.64 and AI). Five openers on the same body now: only "The other aspect is integration" passed. So the body sits near the line and the opener tips it; one passing opener out of five is luck, not a fix. P26 goes to Emulate (round 10, `community-s5j`, input P26-c1: the gated body with the anchored opener), raw versions alone first.

Emulate round 10 on P26 (input P26-c1; balance 240,963 → 240,875). A: "3. Integration – How has the ceremony fit into your life? Did it open something for you? Look at the last few weeks…, check in with relationships and behavior. Are you sleeping better? Making better decisions? Are you more able to handle frustration without creating a "new spiritual emergency"?" (a list number, and "better" gives the change a direction the published doesn't). B: "Integration: How has it affected your life? Did the ceremony open something up in you? Look at your life after the ceremony for a few weeks and see how things have changed, if at all. Look at your relationships, your behavior, your sleeping habits, your decision-making, and how well you can deal with frustration." B keeps the five places and "whether anything changed" ("if at all"), drops the spiritual-emergency quip, and turns the published claims into questions. Br1 and Br3 are B with those put back word by word: the claim "The ceremony opens something up in you", the quip ("without declaring a new spiritual emergency"), and the opener as a claim ("Integration is your life.", the published "Integration is ordinary life.") or as v51's label ("Integration: your life.").

API batch 35 (written 04:58 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| emu10raw-P26-A | Human | raw | Human (0.0) |
| emu10raw-P26-B | Human | raw | Human (0.0) |
| P26-Br1 ("Integration is your life." …) | Human (weak) | B's body with three meaning fixes | Human (0.01) |
| P26-Br3 ("Integration: your life." …) | Human (weak) | the same with v51's label | Human (0.03) |

Batch 35 (04:48 UTC): mine 4 of 4. Both raws and both restorations pass alone. v52 takes Br1 ("Integration is your life.", the published claim minus "ordinary").

v52 = v51 with the three that failed alone: v20's P7 (passed alone, batch 5), P26-Br1, and v41's P32 (passed alone, batch 33). Lint: REVIEW, no FAIL (new REVIEW lines: P26's five places as an E125 triple, which is the published list of five; "Integration is your life." as B5, the published opener).

API batch 36 (written 05:02 UTC, before the call), a diagnostic while the gate runs on P7, P11, P26, P29 and P32:

| text | mine | why | Pangram |
|---|---|---|---|
| v52-S5 | Human with a window or two (weak) | P7 sat in v40's AI run (P6 to P10), and v41's P32 in its P30 to P33 run; most of their neighbors are newer | **Human: 0% AI** (one window, 0.15) |

Batch 36 (04:50 UTC): mine 0 of 1 on the windows (I expected one or two). **v52 reads 100% Human (one window over the whole section, 0.15), and every one of its paragraphs passes alone** (P7, P26 and P32 in batches 5, 35 and 33; the rest in batch 32 and the cache). The gate now runs on the five paragraphs it hasn't seen in these words: P7, P11, P26, P29, P32.

The gate on v52 (TRACE-v52-A, LOGIC-v52-A on P7, P11, P26, P29, P32; SENSE-v52 on the whole section: every sentence of the five reads OK to the cold reader). Fixed word by word in v53: P11 "different from paid support, which is often people you don't know looking after you for a night" (LOGIC CHANGED for the third gate running: the contrast had narrowed from purchased support to paying strangers, and "often" sat on the wrong thing); P26 "Integration is everyday life." (LOGIC: "X is your life" reads as the idiom, everything to you; published "ordinary life") and "in the weeks after the ceremony" (LOGIC: "a few weeks" sets a number); P29 "A lot of people feel the urge" (LOGIC: "really common" makes it the usual response; published "Many people") and no quotation marks around "their people" (TRACE; the v7 trace had taken them out before). Kept with reasons: P7's "Sometimes the dishes need doing…" (LOGIC AMBIGUOUS: the sentence before says insight doesn't do the practical work, which is the published's categorical claim), P7's dropped "revise agreements" and "a new sacred name" (Joel's ruling on lists of three), P26's "you" voice and imperative (every gate since v20; the published names no one who watches, and the essay's "you" is the person whose life it is), P32's "do the math on how much need it can absorb" (the next sentence names the capacity sections), P4's "parents worried about children" (the cold reader asks whose; the published is as open).

API batch 37 (written 05:08 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| v53-P11 | Human (weak) | the published structure is back in the second sentence | Human (0.06) |
| v53-P26 | Human (weak) | two small word changes to a text at 0.01 | Human (0.01) |
| v53-P29 (38 words) | Human (weak) | | Human (0.0) |
| v53-P29P30 (P30 passed alone) | Human | | Human (0.0) |
| v53-S5 | Human, with the seam window back (weak) | P11's second sentence carries the seam, and it changed | Human: 5.0% AI (2,057) |

Batch 37 (05:07 UTC): mine 4 of 5 (the section's windows came out elsewhere than the seam I called). The three fixed paragraphs pass alone (P11 0.06, P26 0.01, P29 0.0), and P29 with P30. The section reads Human at 5.0% with two windows, neither at the P11 seam: P19's last two sentences (68 words, 0.68: the facilitator "may be wise. Or they may be…", and "the more deeply someone is opening up…") and P25's last sentence with P26's first (41 words, 0.68: "Integration is everyday life." on the end of the experience-collectors sentence). Both are spots that read AI before whenever a cut isolated them (batch 28's ablations had P19's; v43 and v44 had P25's). v53's P11 is two words shorter than v52's, P26 one; every cut after P11 moved.

What the batches since 27 show about the windows: v46 → v47 → v48 kept the same cuts with one-word changes; removing "very" (v50) brought the seam back and adding four words (v51) cleared it; v52 (100% Human) and v53 differ by three words of length upstream of P19. So which sentences share a window depends on the running length, and a window that isolates one of these spots reads AI. v54 keeps v53's meaning fixes at v52's lengths, word for word: P11 62 (", which is often paying people you don't know to look after you for a night", the published "paying strangers"), P26 56 ("in the weeks that follow the ceremony", the published "the following weeks"), P29 40 ("after they've gone through", "whatever has just opened up").

API batch 38 (written 05:16 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| v54-P11 | Human (weak) | | Human (0.04) |
| v54-P26 | Human (weak) | | Human (0.02) |
| v54-P29 (40 words) | Human (weak) | | Human (0.0) |
| v54-S5 | Human, 0% (weak) | v52's cuts, if the lengths decide them | Human: 5.0% AI (2,062) |

Batch 38 (05:09 UTC): mine 3 of 4. The three pass alone; the section reads exactly as v53 (the same two windows, 68 words at 0.73 and 41 at 0.66). So lengths don't decide the cuts: the windows follow the text. P19's window is word for word the same text as in v52, where it sat in a Human window, so what changed its score is elsewhere (P11 or P26: Pangram reads a window with its context). P25/P26's window holds the new opener "Integration is everyday life."

API batch 39 (written 05:19 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| v55a-S5: v54 with "Integration is just your life." ("just" for the published "ordinary": nothing special; it also can't be read as "everything to you") | Human, P19's window left (weak) | the opener is the likelier trigger of the P25/P26 window | Human: 4.7% AI |
| v55b-S5: v55a with v52's P11 (a diagnostic only: v52's P11 narrows the published contrast) | Human, 0% (weak) | if P11's new sentence is what moved P19's score | Human: 4.7% AI (the same windows as v55a) |
| v55-P26 | Human (weak) | | Human (0.01) |

Batch 39 (05:11 UTC): mine 2 of 3. v55a and v55b read the same (4.7%: P19's 68 words at 0.73; P25's last sentence alone, 37 words at 0.55; "Integration is just your life." now sits in the Human window after it). So P11 isn't what moved P19's score: v55b has v52's P11. What v55b still has that v52 (0%) doesn't is P26's and P29's changes, both downstream of P19 and P25. Pangram scores a window with the text after it as well as before.

API batch 40 (written 05:22 UTC, before the call), one change each on v52 plus the new P11 (the P11 fix doesn't move the windows):

| text | mine | why | Pangram |
|---|---|---|---|
| v56a-S5: v52, the new P11, and P26 "in the weeks after the ceremony" only (the "a few weeks" fix; "Integration is your life." kept) | Human, 0% (weak) | | Human: 3.0% AI (P19's window, 0.69) |
| v56b-S5: v52, the new P11, and v53's P29 only ("A lot of people feel the urge…", no quotation marks) | Human, 0% (weak) | | **Human: 0% AI** (one window, 0.16) |

Batch 40 (05:12 UTC): mine 1 of 2. **v56b reads 100% Human: v52 with both the P11 fix and the P29 fixes.** v56a's one change, P26's "in the weeks after the ceremony", brings back P19's window (0.69) three paragraphs upstream; the P25 window doesn't come back. So the P11 and P29 fixes are in at 0%, and P26 is the paragraph whose wording moves P19's score.

API batch 41 (written 05:25 UTC, before the call), the two P26 findings on v56b, one word each:

| text | mine | why | Pangram |
|---|---|---|---|
| v57a-P26: "after the ceremony for some weeks" ("some" names no number, like the published "the following weeks") | Human | one word on a text at 0.01 | Human (0.01) |
| v57b-P26: v57a-P26 with "Integration is just your life." | Human | | Human (0.01) |
| v57a-S5: v56b with v57a's P26 | Human, 0% (weak) | | Human: 4.7% AI (P19 0.74; P25's last sentence 0.61) |
| v57b-S5: v56b with v57b's P26 | Human with a window (weak) | two changes in P26 | Human: 4.7% AI (P19 0.70; P25's last sentence 0.68) |

Batch 41 (05:14 UTC): mine 3 of 4. Both P26 variants pass alone (0.01), and both bring back the two windows in the section (4.7%). So every change tried in P26's third sentence ("in the weeks after the ceremony", "in the weeks that follow the ceremony", "for some weeks") puts P19's and P25's windows back, while P11's and P29's fixes don't. **v56 (v56b) is the candidate: 100% Human (0.16), every paragraph passing alone, P11's and P29's meaning fixes in.** P26 keeps v52's words, with two of the v52 gate's findings left for Joel: "for a few weeks" (the published "The following weeks" names no number; "a few" is a small one) and "Integration is your life." (LOGIC: can read as the idiom "X is your life"; the cold reader read it right). With "in the weeks after the ceremony" the section reads 3.0% AI, still a Human verdict (v56a); that's his call.

v56, paragraph by paragraph against the API record (by hash, 05:20 UTC): all 33 pass alone in their exact v56 words (the latest check of each: P1–P5, P8, P9, P12, P13, P15, P16, P22–P24, P27, P28, P33 in batch 32; P3, P10, P17 at v30; P6 at v9; P7 at v20; P11 at v54; P14 at v27; P18 at v40; P19 in batch 22's diagnostics; P20 at v20; P21 at v14; P25 at v45; P26 as Br1; P29 at v53; P30 at v44; P32 as v41's), except P31 (16 words), which passes with P30 (batch 32), and P30 passes alone. The section: 100% Human (batch 40, v56b, the same text by hash).

The gate on v56 (TRACE-v56-A, LOGIC-v56-A on P11 and P29; SENSE-v56 on the whole section). LOGIC: no CHANGED in either; two weak AMBIGUOUS (P11's "they", whose nearest antecedent is the paid strangers; P29's "part of the same urge", which matches the published when read as one urge). TRACE: P11 none; P29's urge named as forming a village, "some … experiences", "serious" for "deep" (all in v43's P29 since the round-8 rebuild; kept: the published also gives one urge with three expressions). The cold reader: two sentences to fix. P2's "It's still a crime to traffic them": "them" has nothing to point to (v44's link text lost "drugs"; TRACE-v46-A had noted it too). And P26's "Integration is your life.": "puzzling at first ('make integration your whole life'?)", the same idiom LOGIC-v52 flagged. Neither change has been tried alone: batches 37 to 41 changed P26's third sentence every time.

API batch 42 (written 05:31 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| v58-P2: "It's still a crime to traffic drugs." | Human | one word on a text at 0.0 | Human (0.001) |
| v58-P26: "Integration is everyday life." (published "ordinary life"), the rest v52's | Human | | Human (0.02) |
| v58-S5: v56 with both | Human with a window (weak) | P26 has moved P19's score before | Human: 4.7% AI (P19 0.69; P25's last sentence 0.58) |

Batch 42 (05:28 UTC): mine 3 of 3. Both fixes pass alone; the section reads Human at 4.7%, the same two windows as every P26 change since batch 37. So P26's words as v52 has them are the only ones tried (eight variants) that keep the section at 0%, and "Integration is your life." is the one the cold reader stumbles on.

API batch 43 (written 05:33 UTC, before the call): one check to know whether the P2 fix costs anything on its own.

| text | mine | why | Pangram |
|---|---|---|---|
| v59-S5: v56 with P2's "traffic drugs" only | Human, 0% (weak) | far upstream, one word | **Human: 0% AI** (one window, 0.16) |

Batch 43 (05:29 UTC): mine 1 of 1. **v59 (v56 with "traffic drugs") reads 100% Human.** So the trade-off is P26 alone: its v52 words keep the section at 0%, and the two findings in them stay ("Integration is your life.", which the cold reader and LOGIC-v52 read as the idiom at first; "for a few weeks", which LOGIC-v52 calls a number the published doesn't set). Fixing them brings two small AI windows back elsewhere (P19's last two sentences, P25's last), at 4.7 to 5.0% with a Human verdict.

The rules decide it: meaning first ("Detector results are evidence, not editorial authority", AGENTS.md), and the section rule is that it passes, which a Human verdict is. So the candidate is v60: v59 with P26 as v53 had it ("Integration is everyday life.", "in the weeks after the ceremony"), which passes alone (batch 37, 0.01). v59 (0%) is the alternative for Joel.

API batch 44 (written 05:36 UTC, before the call):

| text | mine | why | Pangram |
|---|---|---|---|
| v60-S5 | Human, about 5% AI (P19's and P25's windows) | v53's P26 brought them in batches 37 and 38 | **Human: 5.0% AI** (P19's last two sentences, 68 words, 0.74; P25's last sentence with "Integration is everyday life.", 41 words, 0.61) |

Batch 44 (05:31 UTC): mine 1 of 1. v60 reads Human at 5.0% with the two windows. Every paragraph passes alone (P26's words as in batch 37). Turn tally from 01:18: batches 17 to 44, 129 checks; mine 97 of 129 (batches 17 to 26: 64, mine 49; batches 27 to 44: 65, mine 48, counting each section call as wrong when its windows came out other than called).

The gate on v60 (TRACE-v60-A, LOGIC-v60-A on P2 and P26; SENSE-v60 on the whole section): the cold reader now reads P2 and P26 without a stop. No new CHANGED in the words this pass changed. Raised again and kept, with reasons: P2's "only" (LOGIC AMBIGUOUS, TRACE slight: "decriminalized, not legalized" is the contrast the published "actually" draws; kept since v43), "It's still a crime to traffic drugs" (LOGIC AMBIGUOUS: could be read beyond Portugal; it follows "the thing with Portugal is…"), and P26's "Look at your life … and see" (LOGIC CHANGED, TRACE: an instruction, with the participant as the one who checks; the published states it, "The following weeks reveal…"). That last one has been in every version since v20 and every gate has kept it; the published itself gives instructions two paragraphs earlier ("Screen for… Review… Keep… Decide…"), and P9 already gives the noticing to the people who held you. It goes to Joel as a kept item, not a silent one.

**Section 5 is a candidate at v60.** Every paragraph passes alone (P31 with P30); the section reads Human (5.0% AI: P19's last two sentences and P25's last with P26's first, 41 to 68 words each); every finding of the gates since v43 is fixed word by word or kept with a reason for Joel. v59 is the 100% Human alternative, with v52's P26 ("Integration is your life.", "for a few weeks").

## 2026-10-06: Joel's GUI check of v60, and his fully human section

Joel's message of 2026-10-06 16:55 UTC, with his Pangram GUI report of v60 (`section_5_pangram_gui.pdf`, run 2026-10-05 04:31 GMT, Pangram 4.0, 2,114 words): **9% AI** in three windows: the heading with P1 (90 words, Medium confidence), P19's last two sentences (68, High) and P25's last sentence with "Integration is everyday life." (41, High). The API had read the same section at 5.0% (batch 44), with the first 1,275 words as one Human window (0.18). The GUI's text has "image 9" (the article page's image link, 2 words) where the API's had nothing; otherwise the words match. He fixed the heading ("The Medicine Part - Yes, I'm Naming It": the published heading's "X, Without Y" is an x-not-y tell), took out "Key here is that" (it points at nothing at a section's start; TRACE-v46-A had flagged "here" as unanchored and I kept it without listing it), rewrote P18 (now two paragraphs), P19's last sentences, P22's first, P25's joke, P26 (with emojis against wry humor) and P33's end, and pasted the whole section as fully human in the GUI (`s5/joel-s5-20261006.txt`, his characters).

API batch 45 (written 17:00 UTC, before the call): is the API the GUI?

| text | mine | why | Pangram |
|---|---|---|---|
| v60-gui: v60 with "image 9" after the last heading, as the page Joel copied from shows it | AI window at the opening (weak) | if the GUI and API are the same model, the two extra words (and the context effects of batches 37 to 42) should explain the difference | Human: 5.0% AI; the opening is inside a 1,275-word Human window (0.17, High), as in batch 44 |
| joel-S5: Joel's section exactly as pasted | Human, 0% | his GUI check says fully human | **Human: 0% AI** (one window, 0.05) |

Batch 45 (17:00 UTC): mine 1 of 2. With the web app's exact words (window word counts now match it to the word: 1,275 = 90 + 1,185, then 68, 280, 41, 450), the API still reads the opening as part of one Human window (0.17, High), where the web app split off the first 90 words as AI (Medium). So the API and the web app aren't interchangeable at a section's start, at least where the web app finds a Medium-confidence window; the final section check goes through the web app (Joel's suggestion, and HUMANIZATION-GATE's new ruling, PR #139). Joel's own section reads 100% Human in the API too (0.05), as in his web-app check. Section 5 is his text now, installed with the published links put back (`s5/section-joel-20261006.md`).
