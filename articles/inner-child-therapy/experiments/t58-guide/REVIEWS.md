# Turn 58: The Inner Guide Comes Later, group 4 (stopped at Joel's request)

Joel, 20:56 UTC (`experiments/t58-answers/JOEL-20261015-2056.md`): "4 hours for 2 paragraphs is a pretty bad result again ... updating everything on gh as you go". The lean process, E177: my own drafts, linted, my own march reading, a Pangram screen, then one review round on Sonnet. Joel, 21:41 UTC: "stop work at next boundary and save to gh so i can conttinue on other acct".

Group 4 (`tools/targets/t56-ig04.json`; the review target `tools/targets/t58-g4.json`): the Guide needs no certainty and picks the next sensible step that fits what you care about; problems blocked from outside (PGQ-014); one stuck problem shouldn't stop the rest, choosing today's focus, the overwhelm step (PGQ-017). The guide's "Don't make the person define ordinary words or listen to a long recap" is how a helper talks, so it stays out (E156).

## Rounds (all mine; every result in tools/PREDICTIONS.md, turn 58)

| round | drafts | Pangram alone |
|---|---|---|
| 1 | p5-m1, p6-m1, p7-m1 (thesis openers, paired questions, quotable last lines) | AI 0.94, 0.92, 0.97 |
| 2 | p5-m2, p6-m2, p7-m2 (start inside a moment) | AI 0.80, 0.999, 0.998 |
| 3 | p5-a to p7-c (nine: your little one; an opinion; plainest) | AI 0.64 to 0.999 |
| 4 | p5-d, p6-d, **p6-e**, p7-d, p7-e (the example carries the instruction) | **p6-e Human 0.002**; others AI 0.81 to 0.999 |
| 5 | p5-f to p5-h, p7-f to p7-i (p6-e's style) | AI 0.53 to 0.999 |
| 6 | p5-h3, **p56-a** (P5 folded into p6-e), **p7-f2**, **p7-f3**, p7-h2 | **p56-a Human 0.018; p7-f2 Human 0.32; p7-f3 Human 0.29**; p5-h3 AI 0.58; p7-h2 AI 0.93 |

Picked: **P5 = p56-a** (https://www.pangram.com/history/624b7d08-e989-449c-b6b9-b2ba11c9eb11) and **P6 = p7-f3** (https://www.pangram.com/history/20694104-b672-445a-964a-e06b47dbf64b), together in `GROUP4-DRAFT.txt`.

What read AI: the guide's instruction kept as its own sentence ("the next step that makes sense and fits what you care about", "keep in mind what you're waiting for", "say it in one sentence, pick one next step"), generic life-advice examples (a job, the rent), paired rhetorical questions, a quotable last line. What read Human: one plain case ("Say you're waiting on the landlord's signature…"), the article's own figure ("whatever the old parent in your head says"), idioms ("forging ahead as if you had it", "the cat's off her food").

## Reviews (Sonnet, E177)

- Stance check (`STANCE-1.md`): 0 conflicts; P1 to P4 unchanged.
- Repeats (`REPEATS-1.md`): repeat 5, P6's first two sentences restate P5's point ("One stuck thing doesn't mean everything has to wait, either." … "The signature can sit."); a weak echo of When the Spiritual Relationship Hurts' "act where it's yours to act". Nothing else touches P5 or P6.
- Grounding: not run (Joel declined it at 21:4x).

## Next

1. Cut P6's opening sentence and "The signature can sit." (the repeat), lint, and screen P6 alone again.
2. The grounding of both (`reviewer.py grounding experiments/t58-guide/GROUP4-DRAFT.txt <target t58-g4.json> OUT --article <draft article with both after P4>`), if Joel wants it.
3. Install both after P4 with notes, check the h1 so far in Pangram, push, open a pull request.
