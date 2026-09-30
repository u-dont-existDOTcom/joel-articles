# GPT's run checked, what I learned, and what's next

**By Claude, 2026-09-30.** GPT's run ended at `c042984` on `gpt/emulate-overnight-20260929`. My files are on `claude/emulate-lessons-20260930`.

## What GPT did

**Done:**
- all 56 sentence checks;
- all 52 article baselines;
- Emulate website versions of every flagged stretch: 336 versions for 167 stretches, mostly two per stretch. Fifteen second options were lost when its browser reset.

**Not done:**
- Only 10 versions were checked alone (all 100% Human).
- No section was rebuilt with its rewrites and checked.
- No article was assembled.

**The baselines:** Pangram reads all three articles as mostly AI.

| article | checks | words | share of words Pangram calls AI |
|---|---|---|---|
| Community | 17 | 12,827 | about 94% |
| Hypnosis guide | 32 | 19,643 | about 95% (2 checks Human: "The Most Extreme Example" and "Reversing Accidental Affirmations") |
| Neuro de-armoring | 3 | 5,826 | about 88% |

**Problems in Emulate's versions:**
- GPT found fidelity problems (see its `QUALITY-*.md` files):
  - neuro de-armoring: a version that drops the below-90-BPM threshold and the stop instruction, and one that turns Scott's data into first person;
  - hypnosis guide: a version that drops the final safety paragraph;
  - community article: invented memories and a shifted chronology.
- I also found 37 versions that don't end on a full sentence. Some are headings, but several stop mid-sentence ("…you can deepen it by", "To that end,"). A few picked up page text: "Continue reading A New Age Might Come Suddenly", "Double click to interact with video".
- Versions of inputs under 300 words came out about 22% longer than the input.

**One wrong conclusion.** GPT's quality notes say community section 1 still scored 58% AI after the rewrite, "equal to the baseline". In those two checks only the section's opening was rewritten. The other four flagged stretches were still the original text, so the checks say nothing about Emulate. They did show one useful thing: with the opening rewritten, the flag moved onto the next paragraph (the Bruderhof one), which the baseline had called Human.

**Budgets:**
- Pangram: 1,324 credits left. I used 8 today.
- Emulate: 256,783 words. The balance jumped from 17,314 to 257,314 during the run, and GPT couldn't say why.

## What the sentence checks taught me

The full rules, with evidence and what would prove each wrong, are in `CLAUDE-LESSONS.md`. The three that matter most:
- **Most of my sentences pass in human company.** Put back one at a time into versions of Emulate's that passed, 32 of 36 stayed 100% Human. Pangram catches AI-shaped sentences together.
- **Lists of vivid examples in one breath are the loudest.** Three of the four put-backs that came back AI were that kind of sentence. Joel's own fix of one of them (A18) kept two examples in two sentences.
- **Emulate's mistakes can be fixed.** All 13 small corrections stayed 100% Human, including two whole clauses in my wording.

## The transfer test

The five guide paragraphs that open "Love Doesn't Have to Wait for Trust" (E1 to E5), which is also the next section of the inner child article. I wrote them by hand from the lessons, one paragraph at a time. `transfer-20260930/transfer-test-in-context.html` shows each try beside the guide's original.

| paragraph | try | Pangram |
|---|---|---|
| E1 | 1 | 100% AI (80 words) |
| E1 | 2 | **100% Human** alone (64 words), and **100% Human** after the end of "Not Every Hero Wears A Cape" and the heading (275 words) |
| E2 | 1, 2, 3 | 100% AI each time (77, 72 and 81 words) |
| E3 to E5 | | not drafted: I stopped at E2, per Joel's rule to get one paragraph passing before drafting the next |

First tries: 0 of 2 passed. **The lessons tell me which of my sentences are loudest. They don't yet tell me how to write a paragraph Pangram reads as human.** The E1 that passed had an "I think", a question and an everyday example at the end. The same moves didn't save E2, which stayed close to the guide's order and wording ("verdict", "old promises").

The brief's rule to add nothing beyond the guide was mine, and it blocks the move Joel's own fixes use most: adding his own thought where the guide is generic. **I find that rule unhelpful for this test, and I suggest we drop it next time,** with anything I add flagged for Joel's approval.

## What I suggest next

1. **Change the "never hand-fix" rule for article assembly.** I find this inherited rule unhelpful now and suggest we change it: allow small fixes that restore the source's facts, doses, warnings and links, or remove what Emulate invented, with a Pangram recheck of the paragraph and its section after each fix. All 13 such fixes in the sentence checks stayed Human. Without this, most sections can't be assembled: nearly every stretch has some version with a fidelity problem, and a third run isn't allowed.
2. **Then assemble the three articles, section by section:**
   - choose A or B for each stretch by Joel's choosing rule, and fix it;
   - leave the baseline-Human paragraphs untouched and restore links and emphasis from the source;
   - check the whole section, and swap the other version in wherever Pangram flags.

   The first-pass reading and fixing can go to cheaper Sonnet workers, one article at a time. I'd review every dose, warning and safety step in neuro de-armoring and the hypnosis guide myself.
3. **The inner child article:** E1's second try is a candidate first paragraph for the new section, for Joel to accept or edit. E2 onward goes back to his usual loop.
