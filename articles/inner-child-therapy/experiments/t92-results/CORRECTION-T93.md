# A correction to ROUND2-RESULTS.json (turn 93, 2026-10-22)

ROUND2-RESULTS.json lists "Two Common Guarding Patterns P1 (mine)" under `fixed_since_round_1`. That's wrong. Window 207 of half A (AI, High, 95 words) covers P1 and P2's start, so P1 still read AI in round 2. ROUND2-AI-WINDOW-BEGINS.json, built in turn 92, had missed windows 207, 213 and 215, which is where the mistake came from. Those three are added there now.

So the turn-90 rework fixed six of my paragraphs, not seven:
- Chicken-and-Egg P15;
- When to Change the Strategy P3 and P4;
- If You Want to Kill Yourself P6 and P7;
- Borrowed Adulthood P1;
- The Inner Guide P5.

Two Common Guarding Patterns P1 to P4 all read AI after two tries. The result file stays as recorded. The windows, read again from the feed pages, are in `experiments/t93-tells/TELLS-ROUND2.md`.
