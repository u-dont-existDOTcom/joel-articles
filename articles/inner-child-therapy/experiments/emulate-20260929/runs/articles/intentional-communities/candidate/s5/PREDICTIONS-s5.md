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
