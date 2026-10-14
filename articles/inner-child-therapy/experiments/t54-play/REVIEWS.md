# Turn 54: Let the Child Be Bad at Things

Targets `tools/targets/t51-g1.json` to `t51-g3.json` (turn 50's dedup and stance ledger: `experiments/t51-play/`); fresh Opus writers, two at a time; later pairs from `t54-g2b.json`, `t54-g3b.json`, `t54-g3c.json`, `t54-g1b.json` (the scratch target for the second fix of P2 isn't kept), each brief with a line on why the last pair failed.

| draft | linter | march (two Sonnet readers) | then |
|---|---|---|---|
| g1-w1 | REVIEW | S S B S, S S B S | grounding OK; Pangram AI 0.90 (try 1) |
| g1-w2 | REVIEW | S S S B S twice | |
| g1-f1 (fix round) | REVIEW | S S S B S, S S S S S | |
| g1-f2 (fix round) | REVIEW | S S B S B twice | grounding OK; P2's grounding: its "part of you will want to know right away whether you're any good at it" says P2's demand first, so cut (g1-f3) |
| g1-f3 | REVIEW | S S S B twice | Pangram AI 0.97 (try 2); in as the faithful version, FAILS PANGRAM ALONE, question 25 |
| g2-w1, g2-w2 | FAIL (coach register) | | |
| g2-w3 | REVIEW | S S S S S twice | |
| g2-w4 | REVIEW | S S B S S twice | grounding: two flags (a deadline the guide doesn't set; "you… your worth" for the guide's "we… our worth"), fixed as proposed (g2-w4b) |
| g2-w4b | REVIEW | S S B S S twice | Pangram AI 0.66 (try 1): the guide's own sentences |
| g2-f1 (fix round) | REVIEW | S S B S S, S S S S S | |
| g2-f2 (fix round) | REVIEW | S S B S S twice | its "later, but… while that's landing" cut before review (g2-f3) |
| g2-f3 | — | S S B S S twice | grounding: one DUPLICATE flag, answered in P1; Pangram Human (91), try 2; in |
| g3-w1 | FAIL | | |
| g3-w2, g3-w3, g3-w4 | REVIEW | no break | |
| g3-w5 | FAIL | | |
| g3-w6 | REVIEW | S S S B twice | grounding: "which is pl/ork" hung on the discovery made quitting read as a miss; "Either way, that's pl/ork" as its own sentence (g3-w6b) |
| g3-w6b | REVIEW | S S S S B twice | Pangram Human (81), try 1; in |

Stance checks (`STANCE.md`, `STANCE-2.md`): 0 conflicts each; the one note (the h2 follows Key's credit) is the guide's own order (r4 lines 591 and 593). Cold reads of the h2: 3 of 3 OK (`COLD-READ.md`, `COLD-READ-2.md`). Repeats: round 2 found none inside the h2.

The h2 with g1-f3, g2-f3 and g3-w6b: AI 0.89, one window, all of it (https://www.pangram.com/history/7040d0e1-011f-4561-a0f4-173114babe0d). P1 fails alone, so that's where it starts.
