# Turn 57: The Inner Guide Comes Later, its P2 and P3 again (E175)

Joel, 2026-10-15 16:39 UTC (`experiments/t57-answers/JOEL-20261015-1639.md`): "why did that take you 4 hours 22 minutes to humanize 1 paragraph? ... it looks like you tried one time on p2 and p3 then gave up and you didn't even tell me like did you run out of ideas, do you not see any AI tells, do you see human tells, what exactly are you doing?" His answer, E175: screen in Pangram first, review only the survivors, keep going while there's an idea, and tell him the tells.

The guide's passage is one paragraph after P2; the article carries it as two (P3, forced adulthood; P4, the need and how you meet it). Targets: `tools/targets/t57-p2.json`, `t57-p3a.json` (rounds 2 and 3: `t57-p3a2.json`, `t57-p3a3.json`), `t57-p3b.json`.

## Rounds

| draft | linter | march (two Sonnet readers) | Pangram alone | then |
|---|---|---|---|---|
| p2-w1 (the babysitter) | REVIEW | B B S S twice | Human 0.011 | grounding OK; not picked (the Go Fish example is the guide's "attention without growth") |
| **p2-w2 (Go Fish)** | REVIEW | B B S S twice | **Human 0.042; again 0.034** | grounding OK, stance 0, cold reads OK; **in** |
| p2-w3 (the dentist) | REVIEW | S S S B twice | Human 0.32 | not reviewed |
| p3-w1, w2, w3 (dishes at a party; eating at the counter) | REVIEW | a break both times | AI 0.997, 0.63, 0.99 | |
| p3-w4, w5 (round 2) | REVIEW | no break | | blocked by the march |
| p3-w6, w7 (round 2: the step count and the hairdresser; the recovery room) | REVIEW | a break both times | AI 0.986, 0.46 | |
| p3-w8, w10 (round 3: the grocery bags; the road trip) | FAIL (coach density) | | | fixed to w8b, w10b |
| p3-w8b, w9 | REVIEW | no break | | w8c, w9b with one break each |
| p3-w10b | REVIEW | a break both times | AI 0.75 | |
| p3-w8c, w9b | REVIEW | a break both times | AI 0.93, 0.78 | |
| p3-m1, m3 (mine) | REVIEW | no break | | |
| **p3-m2 (mine: the fever and the kitchen)** | REVIEW | S S S S S B twice | **Human 0.041** | grounding: "You'll want to clamp down harder" read as advice; cold read the same; stance: "the sneakier one" ranks the two traps |
| p3-m2b | REVIEW | S S B S S B twice | Human 0.30 | stance: "someone safe" gone |
| **p3-m2c ("to someone you trust")** | REVIEW | S S B S S B, S B B S S B | **Human 0.41** | stance 0, cold read OK; **in** |
| p4-w1 | FAIL (two lists of three) | | | |
| p4-w2 ("hello??" before the corner) | REVIEW | B B S S B twice | Human 0.008 | grounding OK; stance 2: "works for you both" for the essay's "without erasing either person" |
| p4-w2b ("leaves room for both of you") | REVIEW | B B S S B twice | Human 0.051 | inside the h1, its last 59 words read AI |
| p4-w2c, w2d (the strategy half as two scenes) | REVIEW | a break both times | w2d AI 0.65 | grounding: one SHOULD question (what a better way looks like), answered in w2d; the h1 with w2d: Human, high |
| p4-w2e, w2f, **w2g** | REVIEW | a break both times | AI 0.76; Human 0.11; **Human 0.13** | w2g: grounding OK, stance 0, cold read OK; **in** |
| p4-w3 | REVIEW | B S S B twice | AI 0.94 | |

Groundings: `GROUNDING-*.md`. Stance checks: `STANCE-1.md` to `STANCE-6.md` (the last 0). Cold reads: `COLD-READ-1.md` to `COLD-READ-7.md` (all OK but the second, which flagged the clamp-down line). Repeats: `REPEATS-1.md` and `REPEATS-2.md`: nothing repeats inside the opening. Across sections, for the whole-article sweep: B9's two traps (The Chicken-and-Egg Problem), B14's chore on empty, B192's "instead of saying you're fine" (When to Change the Strategy; the one a reader would most notice), B156's bedtime, and B230's art and nature.

## The tells

- **What read AI:** the guide's sentences said the guide's way. Every one of P3's eight AI versions kept its therapy words: "perfect discipline", "never let a need show", "very little joy or closeness", "someone safe", "the next grown-up step", "tighten your grip". A scene in front didn't save them (the dishes at a party, 0.997), and neither did a goofy one (the grocery bags, 0.93). P4's strategy sentences ("Look at how you're going about getting the need met … is another matter. The Guide helps you find a way…") read AI inside the h1 even when P4 alone read Human.
- **What read Human:** the same meaning in plain words. "Nope, all good!" from somebody with a fever who's cleaning the whole kitchen anyway; "Not a lot of fun in that kitchen, and nobody gets very close to the person in it"; "Wanting them close is fine! The texts and the sulking aren't". One everyday example with an odd exact detail (Go Fish; "hello??" before they've reached the corner), a question ("Who wants to be the grown-up who finally wins?"), an opinion ("I think your little one just wants to know they're coming back."), the reader's own words in quotes.
- **What didn't tell:** the scenes themselves. Rounds 2 and 3 replaced the scenes and kept the words, and still read AI; my plain-word version kept the order and read Human.

## Pangram (dashboard, version 4.0; every result in tools/PREDICTIONS.md, turn 57)

- P2 alone: Human Written (0.042, low; 67): https://www.pangram.com/history/ddb0ab05-9be2-4b8a-82a4-30befa0fe514; as installed (0.034): https://www.pangram.com/history/3ea3355c-1d7c-4a35-8836-892ca64d504c
- P3 alone: Human Written (0.41, medium; 105): https://www.pangram.com/history/bc04eaee-d7f1-46c8-8329-b1c67073ddbb
- P4 alone: Human Written (0.13, medium; 105): https://www.pangram.com/history/c3fdea09-4c49-4767-909d-f4085a60b21b
- The h1 so far (heading, P1 to P4): Human Written (0.16, high; 375), one window: https://www.pangram.com/history/e6761e96-5537-486a-a320-124ff83c92cc
- Its earlier tries this turn: with p4-w2b, AI Detected (0.24): Human, high, 308 words, and AI, medium, 59 (P4's strategy half): https://www.pangram.com/history/438bb20e-acb9-4c32-b2e7-2ea902844bb1; with p4-w2d, Human Written (0.20, high): https://www.pangram.com/history/1aacb2ea-6167-4024-b7cf-b344b0e3148e

Question 28 is answered by these: P2 and P3 read Human, so the faithful versions are out. Next for this h1: group 4 (the Guide needs no certainty; problems blocked from outside, PGQ-014 and PGQ-017) and the healthy-mind paragraphs (PGQ-007).

## What the batches taught

- The web app doesn't scan an identical text again: it shows the earlier result, adds no history entry, and the batch's next click (the h1) was lost; I clicked it by hand. Don't resubmit a text that's already been checked; use its earlier result.
- A paragraph can read Human alone and AI inside its h1 (p4-w2b), or AI alone and Human inside it (p4-w2d). Both checks count.
