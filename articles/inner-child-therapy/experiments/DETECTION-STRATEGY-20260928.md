# A strategy for detecting the march before Pangram does (proposal, 2026-09-28)

Joel, 00:44: "we need to develop a strategy to detect AI tells otherwise we can't generate human prose. pangram doesn't tell you how to fix it. it only tells you if you are good at detecting ai tells or not … i'm reluctant to continue this if we don't have a straetgy to move forward."


**Outcome (2026-09-28, later the same day).** Joel redirected this at 00:56: a fresh subagent with a good rubric should review, and a writer should carry out its per-sentence instructions. Both parts are done:
- The reviewer, trained on our labeled paragraphs, was validated on held-out paragraphs and on Joel's untouched prose (`tools/REVIEWER-VALIDATION-20260928.md`).
- The reviewer-writer loop passed Also Look Outward P1 with sense intact (`experiments/REVIEWER-WRITER-LOOP-20260928.md`).

The job-sequence labeling below wasn't needed for that. It stays a possible check on the reviewer.

## Where things stand

- **Saved:** 75 texts with Pangram 4.0 results in `tools/calibration/` (36 Human, 39 AI), each tied to a draft record (what it was for, the audit, the result, usually the flagged span). The older lab cache (`pangram-humanization-lab/cache/pangram-4/`) has 12 more, with window-level scores.
- **Not done:** until 2026-09-27 the set was used mainly to tune the linter's thresholds. Why each text failed is scattered across the drafts files and was never pulled together.
- **My detection is the weak point:**
  - My predictions are 0 of 4.
  - Blind model judges score 18 of 28 (Sonnet and Opus alike).
  - The tell list, as applied by a blind agent, missed the march in paragraphs Pangram rates 100% AI.
  - On my own drafts, I explain the march away. Also Look Outward r7, a thesis, then an example, then the lesson, an authority and a quip, was recorded as "no words match" on the march rows.

## What the data already shows (minimal pairs: one change, a different result)

1. **Joel's wording against my smoothing of it.** The Chicken-and-Egg Guide paragraph was 44% AI with my polish, and 100% Human with his words as written.
2. **A summarizing last sentence.** Three Adult Functions P1 r3b was 100% AI, and Human with that sentence cut.
3. **One paragraph that makes a section march.** Borrow One Competency was 100% Human, and 47% AI with the enjoying paragraph added.
4. **One sentence per job against one scene carrying the jobs.** The three jobs were 100% AI (r1b), then 100% Human (r2).
5. **Joel's minimal fixes (Borrow P3, P5; Three Adult Functions P1).** He replaced clever lines and bare prohibitions with the view a person would actually hold, and each flipped to Human (E60, E61).

## The strategy

1. **Test Joel's hypothesis on the data: the march is a job sequence.**
   - A fresh agent that doesn't know the results labels the job of every sentence in all 75 texts. The labels: thesis, example, lesson, authority, advice, caveat, closer or quip, reaction, digression, story beat, and so on.
   - Then measure whether template sequences (thesis → example → lesson → authority → closer, every sentence doing a job) predict Pangram's verdict on texts held out from the tuning.
   - If they reach about 80%, the job-sequence read becomes the check before any Pangram call. A fresh agent always runs it, never me on my own draft.
2. **Build a catalog of what flips a result.** Every minimal pair and every one of Joel's fixes gets its before, its after, the change, and both results. That's the "how to fix it" Pangram doesn't give. A new failure is repaired from the nearest entry, not by rewording.
3. **Change how drafts start.** My drafts march because I build them from a list of points. Two ways to start, both to be measured:
   - (a) Joel's rough words, which I place and trim without smoothing. That passes every time in the data so far.
   - (b) A draft that starts from a reaction to the point (what's wrong, odd or funny about it) and is allowed to be uneven, then goes through the fresh job-sequence read.
4. **Stop rule.** If the job-sequence read can't predict Pangram on held-out texts, the march isn't learnable this way, and (a) becomes the workflow.

## Would Joel fixing Also Look Outward help?

It helps the article; his fixes pass. It helps me only if the fix becomes a catalog entry (step 2), and if the fresh read learns to see what he saw (step 1). Until now I've pulled lessons from two of his fixes (E60, E61), not all of them.
