# The reviewer, tested (2026-09-28)

Joel, 00:56: "you can easily notice what looks ai from a prior turn, but not in this turn. that's why a sub agent should fix the problem, but i don't know how you are setting those subagents up. it seems like they must be either less intelligent ... or they don't have a good rubric". And 01:40: "i would also test on the human prose (not humanized) because if it's telling you that even the human prose looks AI then that is a problem".

**Short answer.** It was the setup, and the model matters too. With labeled examples from our own Pangram results, Opus got 43 of 53 held-out paragraphs right. It let no AI paragraph through, and it called all 19 of Joel's own passages Human. Sonnet stayed near chance with the same prompt. The prompts and builders are in `tools/reviewer/`. The raw verdicts are in `tools/calibration/REVIEWER-VALIDATION-20260928.json`.

## How the earlier reviewers were set up

- **The tell-list reviewer (2026-09-27).** It got the 33 definitions from `docs/HUMANIZATION-TELL-INVENTORY.md`, plus the inventory's general rules:
  - "Organization is not a tell."
  - "PRESENT means the operation is actually happening in this prose, not that a surface form associated with it appears."
  - "a list, first person, ... an organized structure is not a tell by itself."

  It was told not to give any verdict, and it saw no example of what Pangram had flagged. It marked nearly everything ABSENT, including paragraphs Pangram rates 100% AI (AUC 0.59, `tools/TELL-CALIBRATION-20260927.md`). The rules meant to stop over-flagging told it to look away from the march.
- **The judges (2026-09-28, early).** A bare "spot the AI" game, with no examples and no rubric (`JUDGE-BLIND-HUMAN-OR-AI-20260928.json`).
  - Opus got 18 of 28. It called 7 of the 14 human texts AI.
  - Sonnet got 18 of 28. It called both of Joel's own paragraphs AI.

## The new setup

`tools/reviewer/rubric.txt`, then our labeled paragraphs, then the passages to judge.

- **The rubric** says why earlier reviewers got it wrong:
  - every AI-labeled passage here was an AI trying hard to sound human, so casual voice tells you nothing;
  - Joel's own writing is often plainer and stiffer than the AI's.

  It gives Joel's descriptions of the march in his words ("marching order, predictable cadence with optimized structure"; "ensuring the thought is fully complete and summed up perfectly"; "notice things naturally in the midst of the organization"; sentences that "think about each other"). It gives a way to look: write each sentence's job, then read only the jobs. And it says the examples, not the rubric, are the teacher.
- **The examples** are our Pangram-labeled paragraphs (`tools/calibration/`), grouped by paragraph. Each group has a factual note on what changed between its versions and how Pangram responded, with no theory. For example: "In the first, the last two sentences are an AI's rewording of the author's two sentences. In the second they're the author's own words."
- **The output** is Pangram's likely verdict, a confidence, the sentences that decide it, and a reason.
- **Isolation.** Each prompt is a file. The subagent is told to read that file and nothing else, because the calibration file names say PASS and FAIL. Every run reported only the one Read.

## Held-out validation

The 54 paragraph-length texts were split into two folds of 27, with versions of the same paragraph kept in one fold. The pair that fails only when its two passing paragraphs are joined is used for training only. Each run learned from one fold and judged the other, so no reviewer judged a paragraph it had seen: 53 test passages, 25 AI and 28 Human.

| model | right | AI caught | Human called Human | right when it said Human | AUC |
|---|---|---|---|---|---|
| Opus | 43/53 (81%) | 25/25 | 18/28 | 18/18 | 0.87 |
| Fable | 33/53 (62%) | 21/25 | 12/28 | 12/16 | 0.78 |
| Sonnet | 32/53 (60%) | 14/25 | 18/28 | 18/29 | 0.59 |

On the 25 passages the old judges also saw:
- Opus went from 15 right (old judge prompt) to 19.
- Sonnet went from 18 to 16.
- Fable got 13.

**It points at the right sentences.**
- In the Guide paragraph, it named the two sentences I'd reworded from Joel's: "author's stiff sentences replaced with casual smoothed ones ('Then again', 'lean on')".
- In pl/ork, it named the "So…" ending.
- In three jobs r1b, it named the definitions.

**Opus's ten errors all go one way:** human-labeled paragraphs that it called AI. All ten are AI drafts that Pangram let through, mostly short ones (53–92 words). Its reasons, in its words:
- a march with casual filler: Three Functions P2, "problem, rename, 'often doing two at once,' then party example";
- setup, fix, lesson even in two sentences: the 2 a.m. Protector paragraph, and the friend-who-sits-with-you paragraph ("the outline still marches despite the irony in sentence two");
- ending on a cute image, a joke or reassurance: "a rock they found", the coffee line in Goodwill, "counts for a lot", "until you can hold the direction yourself";
- a joke per sentence: Borrow P7.

Two of the ten back it up. The Guide paragraph and Borrow P7 each passed alone, and Pangram called them 100% AI side by side.

## Joel's own prose (not humanized)

Twenty-nine passages, none of them among the reviewer's examples, judged in two runs shuffled differently. The texts are listed in `tools/reviewer/human_items.manifest.json`. The blog texts stay out of git, as the lab keeps its idiolect corpus.
- **19 of Joel's own passages:**
  - 15 paragraphs from his 2013–2016 blog posts (tafkajestdr.blogspot.com);
  - his raw note on inner-child trust;
  - the heart-loop paragraph;
  - his romance rewrite;
  - Catch the Hook P3.

  All 19 were called Human in both runs.
- **2 humanized somatic intros.** Joel, 02:08: "the somatic article was humanized, so i'm not surprised there are parts of it that still look AI". The shorter one was called AI both times, at 57 and 60. Its reason: "clean four-step march, one job each, ending on a 'comes to the rescue' handoff".
- **8 AI texts:** the three model imitations of the somatic intro (Pangram AI), my romance attempt (about 60% AI), and four paragraphs from failed Borrow drafts. All 8 were called AI in both runs.

The two runs agreed on every passage. The blog posts were easy for it (confidence 75–90). Article-register passages were harder (57–78), and that's the register I write in.

## On the loop's new drafts (Pangram checked afterwards)

Details are in `experiments/REVIEWER-WRITER-LOOP-20260928.md` and `tools/PREDICTIONS.md`.

| draft | reviewer beforehand | Pangram alone |
|---|---|---|
| r3B2 | HUMAN 65, HUMAN 70 | 100% Human (hit) |
| r4sf1 | AI 60, AI 60 | 100% Human (miss: too strict) |
| r5v2 | HUMAN 60 | 100% Human (hit) |
| r6b (its near twin r6a was reviewed) | AI 65 on r6a | 100% Human (miss: too strict) |

**How to read it.** Its Human has been right every time so far: 18 of 18 held out, 19 of 19 of Joel's own writing, and 2 of 2 on new drafts. Its AI at 60–65, on a paragraph whose march it already calls broken, has been a false alarm twice. That's the point to check Pangram rather than keep editing.

## Thinking level (Joel, 01:40)

It can't be set per subagent. The Agent tool has no such setting.
- This session runs at effort `max` (`CLAUDE_EFFORT=max`, `MAX_THINKING_TOKENS=31999`).
- The docs don't say whether subagents inherit it. Custom agent files take `model` and `tools` but no effort key (https://code.claude.com/docs/en/sub-agents.md, checked 2026-09-28).
- The Opus reviewers ran 4 to 20 minutes and used about 130–230k tokens each for one prompt of 7,000–9,000 words, so they were thinking at length.

## Limits

- The samples are small.
- It's one author and one article, mostly one AI writer, and Pangram 4.0.
- Most texts are short enough that Pangram marks them "confidence limited".
- Telling a reviewer the Pangram result moves its verdict: two sense-fix reviewers told "this came back 100% Human" both said HUMAN 95. Only tell it when asking for sense-only tickets.

Before trusting it on a new register or a new writer model, rerun the fold validation and the human-prose test after any change to the prompt, the examples or the model (`tools/reviewer/README.md`).
