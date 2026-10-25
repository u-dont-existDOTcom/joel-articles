# Turn 110: the review sheet's new sentences through the owner-delivery gate

Main took the owner-delivery gate during this turn (2026-10-25 17:44 UTC, [HUMANIZATION-OWNER-DELIVERY-GATE.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/docs/HUMANIZATION-OWNER-DELIVERY-GATE.md), issue #245): model-written Joel-byline prose goes to him as a proposed revision only after `owner_delivery_gate.py deliver` ([the tool](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/tools/humanization/owner_delivery_gate.py)) has admitted its exact bytes, with a fresh linter run, a verdict on every row of the tell inventory and three separately saved reviews (preservation and two cold reads). The sheet's first turn-110 version went out before the lane had merged it; the version that replaced it shows only admitted sentences ([build_review.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-review/build_review.py) refuses to build otherwise).

## What the gate covers here

The new words a model wrote, each as the literal sentence that would be new in the article:

| Name | The sentence | From |
|---|---|---|
| S1-nurturer | "I'd still keep the Nurturer voice." | P8, both reviews |
| S1-watch | the move-out sentence in two, with "call it all off" | GPT's readability fix and the cold read |
| S1-protective | "Blaming yourself can be doing a protective job, too." | GPT's S1 advice and the cold read |
| P2 | "I'd keep what you feel around them in mind, and look at their track record too." | GPT's wording, "I'd" kept |
| P5 | "My son did that for me, and I think that's very common for parents." | his answer of 2026-10-02 as an article sentence |
| P6 | "I'd leave out forgiving them and picturing their childhood here." | GPT's P6 |

Each folder has the draft, its context (the section as it would read), its source, the manifest ([S1-nurturer's ADMISSION.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/S1-nurturer/ADMISSION.json), for one: the writer's verdict on all 33 rows, a reason for each linter finding) and the three reviews. The reviewers were fresh Sonnet subagents with only [the brief](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/REVIEW-BRIEF.md) and the files (each role had its own copy, such as [the preservation reviewer's](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/BRIEF-preservation.md)).

## What it doesn't cover, and why

- **S3**, Before You Tell the Hardest Stuff: his own sentences only, word for word, in a new order. The gate is for generated prose, "not owner-authored prose".
- **The ten cuts** (C3 to C12): no new prose. Each paragraph is the article's text minus a line, already in the article.
- **S1's other sentences**: already in the article, word for word, only moved, and "It might say" is his own word from before turn 109. Whether the order was chosen for sense or to dodge the detector (T14) is judged in the three S1 sentences' ledgers: GPT's S1 advice chose it, before any check.
- **The three questions**: they add no text.

The whole S1 section can't go through the gate as one draft: the linter fails it on lines already in the article, unchanged (O9 on "Or saying no to someone, and not texting an hour later to take it back.", from the P3 he sent as his own on 2026-10-04, and R2, a mismatch it reads between "It might say", his word from before turn 109, and turn 109's "That part"), and a FAIL can't be waived for model prose. The gate is for the new model words, so each one goes through as its own sentence.

## Results

| Name | Preservation | Cold read 1 | Cold read 2 | The gate |
|---|---|---|---|---|
| S1-nurturer | PASS | PASS | PASS | admitted ([the sentence](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/S1-nurturer/FOR-JOEL.txt), [its proof](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/S1-nurturer/FOR-JOEL.proof.json)) |
| S1-watch | PASS | PASS | PASS | admitted ([the sentence](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/S1-watch/FOR-JOEL.txt), [its proof](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/S1-watch/FOR-JOEL.proof.json)) |
| S1-protective | PASS | PASS | PASS | admitted ([the sentence](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/S1-protective/FOR-JOEL.txt), [its proof](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/S1-protective/FOR-JOEL.proof.json)) |
| P2 | PASS | PASS | PASS | admitted ([the sentence](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/P2/FOR-JOEL.txt), [its proof](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/P2/FOR-JOEL.proof.json)) |
| P5 | PASS | PASS | PASS | admitted ([the sentence](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/P5/FOR-JOEL.txt), [its proof](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/P5/FOR-JOEL.proof.json)) |
| P6 | PASS | PASS | PASS | admitted ([the sentence](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/P6/FOR-JOEL.txt), [its proof](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/P6/FOR-JOEL.proof.json)) |

The reviewers' own notes outside the changes, for a later pass: in Don't Give the Inner Adult Away, the paragraph before P2 has "makes me more grounded, truthful, and free", a "me" in a paragraph that otherwise says "you" (preservation and cold read 1); and the preservation reviewer couldn't check from P6's section alone whether another section recommends forgiving a parent or picturing their childhood (How to Forgive Without Forgetting is the one that discusses it). Cold read 1 also reported that a hook had added the repository's [AGENTS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/AGENTS.md) to its context, so each reviewer had that file too, beside the brief and its files; it says nothing about these drafts. The first cold reader 2 ran out of output room before writing anything, and a second one, in a fresh context with its own context id, wrote the cold-read-2 reports.
