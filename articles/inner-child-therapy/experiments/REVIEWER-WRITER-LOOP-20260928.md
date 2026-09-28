# The reviewer-writer loop on Also Look Outward P1 (2026-09-28)

**Result.** Draft r6b passes a cold sense read, sentence by sentence. It passes Pangram 4.0 alone (100% Human, 122 words, short text), and the section with it passes too (100% Human, 313 words, full confidence). The seven versions of this paragraph before it were all 100% AI alone:
- the version accepted on 2026-09-18;
- its fix;
- r1, r2, r5 and r7;
- the one installed now.

r6b is in the article as a candidate. Joel decides.

> Once you're in that happy place, look at the other person too, and don't go only by the one fight where they crossed your boundary, or, the other way around, by the one "no" or boundary of theirs that made you mad — granted, they're allowed to say no to you. Does it keep ending the same way, where you bring up something that hurt and end up reassuring them they're not a bad person, and the talk never comes back to what happened to you? (The psychologist Lindsay Gibson calls people like that emotionally immature, and one of her books is Disentangling from Emotionally Immature People.) Or can they hear you disagree and look at their own part?

The book is real: New Harbinger, 2023, https://www.newharbinger.com/9781648481512/disentangling-from-emotionally-immature-people/.

## The method (Joel, 00:56)

"a subagent would give the instructions for fixing each sentence and the writer would follow those like an engineering task rather than a 'see everything all at once' writing mode". Prompts and builders are in `tools/reviewer/` (`reviewer.py review | writer | sense`).

1. **Reviewer.** A fresh Opus subagent gets the validated reviewer prompt (`tools/REVIEWER-VALIDATION-20260928.md`), the meaning to keep, and the paragraphs before and after. It gives a verdict and one ticket per sentence:
   - KEEP; or
   - FIX, with the problem, an instruction, and what the reader should get from it (never the new words).
2. **Writer.** A fresh Opus subagent carries out the tickets literally. KEEP sentences stay character for character, nothing gets polished, and it reports what it did for each ticket.
3. **Next round.** A fresh reviewer that doesn't know the history. When two reviewers wrote different tickets, both sets were carried out and the next round's reviews picked between the results. I didn't pick.
4. **Sense.** Once a reviewer said HUMAN, a fresh cold reader checked each sentence for sense only. Its notes went back to a reviewer, who wrote tickets that fix the sense without bringing back the march.
5. **Pangram** came last. The prediction was written in `tools/PREDICTIONS.md` before each call.

The starting draft was r2. It had passed four cold reads for sense, and Pangram had rated it 100% AI.

## Rounds

Every draft, review, ticket set and sense read is in `reviewer-loop-20260928/<round>/`.

| round | draft | reviewer | cold sense read | Pangram alone |
|---|---|---|---|---|
| 0 | r0 (r2 from 2026-09-27) | AI 85 | OK (earlier) | 100% AI (earlier) |
| 1 | r1: questions merged, Gibson flat, a caveat at the end | AI 80, AI 85 | | |
| 2 | r2a: caveat becomes "the same jump … in politer words" | AI 80, AI 80 | | |
| 2 | r2b: the caveat folded into sentence 1, ends on Gibson | AI 75, AI 70 | | |
| 3 | r3A1, r3A2, r3B1 | AI 85, AI 70, AI 70 | | |
| 3 | r3B2: one long question with Gibson in parentheses inside it, ending "or can they…?" | HUMAN 65, HUMAN 70 | both sentences UNCLEAR | 100% Human (109 words) |
| 4 | r4sf1: r3B2 with sense tickets (the question split in three) | AI 60, AI 60 | sentence 1 UNCLEAR | 100% Human (118 words) |
| 4 | r4sf2 | AI 70 | sentence 1 UNCLEAR | |
| 5 | r5v1 | HUMAN 60 | sentences 1 and 4 UNCLEAR | |
| 5 | r5v2: "with you promising to be more careful how you bring things up?" | HUMAN 60 | sentences 1 and 3 UNCLEAR | 100% Human (105 words) |
| 6 | r6a: r4sf1 with "don't judge them only by" | AI 65 | sentence 1 UNCLEAR ("granted") | |
| 6 | r6b: r4sf1 with "don't go only by" | (not reviewed; see r6a) | all OK | **100% Human (122 words)**; the section **100% Human (313 words)** |

## What changed from the failures

This is read off the drafts, and Pangram confirms it.
1. **Gibson moved from the end to the middle.** She's now an aside, not the closing resource. The six earlier failures and r0–r2 all ended on her, and the reviewers pointed that out from round 2 on.
2. **It ends on an open question** ("Or can they hear you disagree and look at their own part?"), and Joel's P2 answers it ("You may not know for certain whether the other person is or could be capable of a healthier response…").
3. **The first sentence argues with itself.** "— granted, they're allowed to say no to you" is a reaction to its own example.
4. **Nothing sums up.** There's no closing caveat ("that doesn't settle whether this person is like that") and no callback bow ("the same jump … in politer words").

**What didn't need to change.** The reviewers kept calling one middle sentence stock: "where you bring up something that hurt and end up reassuring them they're not a bad person, and the talk never comes back to what happened to you". It's in r4sf1 and r6b, and both passed. The ending and where the resource sits mattered more than that line.

## Lessons

L1. **A validated reviewer plus a literal writer did what my own drafting didn't in seven tries.** The difference isn't more rules. The reviewer isn't the writer, and it learned Pangram's line from our labeled paragraphs.

L2. **The reviewer is strict.** It said AI 60–65 on two drafts Pangram passed. Its HUMAN has been right each time, so HUMAN is a stop signal. When it's at AI 65 or less and already calls the march broken, a Pangram check tells more than another edit.

L3. **What reads human and what makes sense pulled against each other.**
- The reviewer rewarded a tangle, r3B2, that a cold reader couldn't follow.
- The sense fixes that kept it passing were asked of a reviewer, with the reader's notes:
  - split the parenthetical out into its own sentence;
  - then change two words in sentence 1.
- The sense-first rule still holds for installing (E87). In this loop, sense was checked after each HUMAN and fixed by tickets.

L4. **Fresh reviewers disagree about tickets.** Carrying out two ticket sets and letting the next review choose worked better than choosing myself.

L5. **Telling a reviewer the Pangram result moves its verdict.** Two sense-only reviewers told "this came back 100% Human" both said HUMAN 95. Only tell it for sense-only tickets.

L6. **The meaning brief carried AI phrasing, and writers reused it.** "Taking care of their feelings while yours disappear" was in the brief, and the reviewers called it stock. Write briefs as bare points.

L7. **Cost.** 44 subagent runs in the loop: reviewers took 4–15 minutes each, writers 1–5. There were 5 Pangram checks, about 12 credits. The loop ran from 03:00, after a rate-limit pause, to the end of the turn.

## Open for Joel

- r6b is in the article as a candidate. His choices:
  - accept it;
  - drop P1, so the section opens with his P2;
  - write his own.
- A cold reader of the near twin r6a stumbled on "granted". The clause supports the point rather than conceding against it, so it reads more like "after all". The reader of r6b didn't flag it.
- The source's "you do not need repeated exposure to danger before protecting yourself" is still in no version.
