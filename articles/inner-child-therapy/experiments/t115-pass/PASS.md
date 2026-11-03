# Turn 115: the one pass on round 8's spots below Human, high

You, 2026-10-26 12:24 UTC: "try to get it all high conf human with one more pass, then whatever remains you can just give me as highlighted in a docx so i can see what to work on directly" ([your message](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-answers/JOEL-20261026-1224.md)).

**The method** is the one you set in turn 93 (your answer to question 83): I find the tells in my own paragraphs and take them out, adding nothing. A sentence that restates, sums up or reassures, or that another line already says, is cut; otherwise its point is said once, plainly, about the people. Your words, and the version of Untangling the Belonging Bargains you approved word for word, are left for you. The order: AI windows, then Low, then Medium below 0.985 calibrated confidence ([fixes.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-pass/fixes.py)).

**What it covers:** 12 changes, one in each of 12 paragraphs of mine (one of them opens with your words about your father, which stay), seven cuts and five plain rewordings, which take in all four AI windows of round 8 and seven of its eight Low ones. The eighth Low window is in your second paragraph of If You Want to Kill Yourself, your words. One more cut is a suggestion only, because you approved its paragraph as it is (C2): "Privacy isn't fakery."

| | where | the tell | the change |
|---|---|---|---|
| F02 | Borrow Love P4 | an image for the step, filler, a packaged example, a reassuring follow-up | said plainly; the follow-up cut |
| F04 | If You Want to Kill Yourself P1 (safety) | a question answered by a knock-down; a disclaimer and its reframe | one condition of the same instruction; one plain statement of what the steps are for |
| F01 | Borrow Love P2 | a short tidy instruction between the image and the comfort | cut |
| F03 | Love Doesn't Have to Wait for Trust P7 | a short balanced instruction; a tidy prediction | both cut (P5 and Mr. Rogers say the first) |
| F05 | Write It. Don't Send It Yet. | a balanced inversion closer | said plainly |
| F06 | How to Forgive Without Forgetting P3 | a short knock-down after a balanced sentence | one sentence about the people |
| F07 | You Are Worthy of Love. Always. | a follow-up explaining your guide's line; a short reassurance | both cut |
| F08 | Five Stages of Reparenting | an aphoristic closer | cut |
| F09 | If the Love Isn't Coming Yet P1 | "not X, it just Y" | cut to "That just means you start smaller." |
| F10 | Remember When You Already Did It | a question answered by a short answer, in parentheses | one condition |
| F11 | Notice the Part That Came Here P1 | a stock phrase and its restating follow-up | cut |
| F12 | Notice the Part That Came Here P2 | a reassuring permission | cut |

**Reviews and the gate:** three fresh reviewers (preservation and two cold reads) passed all 12. The five rewordings also went through the owner-delivery gate, and all five were admitted ([GATE-OUTCOMES.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-gate/GATE-OUTCOMES.json)). The safety paragraph keeps every instruction in its order, and every MUST its grounding set. Its wording of your guide's "That isn't my answer" is now carried by "keeps the question ... open", which all three reviewers accepted. Two descriptions were corrected after the reviews, as they noted. F03 also drops the hedged "might only be one sentence". F07 also drops "And you aren't alone.", which the next sentence says concretely.

**Nothing is installed yet.** Several of these paragraphs are ones you approved as they are, so the docx shows the pass as tracked changes for you to accept or reject.

**The checks:** each changed block went through the API, alone, predictions first (ledger #360 to #370, [API-CHECKS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-api/API-CHECKS.md)). Nine blocks read Human Written. In them, F01, F02, F05 and F11 read Human, high on every window over the changed paragraph. The others read at worst Medium there, and nothing read Low or AI: the crisis paragraph's new last sentence, F06's "Or the skills.", F07's paragraph, F08's boss example, F10's new parenthesis and F12's "What was it?". F03's first try still read "You don't have to accept every conclusion ..." Human, Low, so its second try cut that clause too (the Mr. Rogers scene shows it), reviewed again, and its paragraph then read Human, Medium. That second check put an AI, Low window on a sentence of that section the pass didn't touch, "Be careful not to take the accusation as proof your love really is conditional ...", which round 8 read Human, high in the whole guide. It's marked in the docx for the next whole-guide check. F09's block (If the Love Isn't Coming Yet) timed out without an answer, so it may or may not have reached Pangram, and it isn't sent again until the account's History shows which.

The next whole-guide check (round 9) reads the pass in context, with your own changes from the docx.
