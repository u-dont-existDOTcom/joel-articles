# Round 8: the guide as installed in turn 114 (read in turn 115)

Your two links of 2026-10-26 12:24 UTC ([JOEL-20261026-1224.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-answers/JOEL-20261026-1224.md)). Each feed page was read in full, every window kept ([RESULT-A.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-results/RESULT-A.json), [RESULT-B.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-results/RESULT-B.json)), and the checked text matches each page's SHA-256 ([record_round8.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-results/record_round8.py)).

| half | result | AI | windows | AI windows | not High-confidence Human |
|---|---|---|---|---|---|
| [A](https://www.pangram.com/feed/909d378e-11d2-4722-b988-a508256c78b4) | Human Written, High | 0.37% | 93 | 1 (Low) | 47 |
| [B](https://www.pangram.com/feed/bd483bd6-edab-4f39-834c-3d959b0abb72) | Human Written, High | 0.21% | 87 | 3 (Low) | 46 |

**The predictions (ledger #347 to #359):** 12 of 13 right. The miss is the W-solomon item, read Human: its AI window is the paragraph after your Solomon's paradox paragraph ("Then take a small piece of whatever you'd tell them..."), mine.

**Round 6's AI windows** were on the photos paragraph and How This Relates to IFS, both of which you rewrote in turn 109. Both now sit inside High-confidence Human windows.

**Round 8's four AI windows** were all on words round 6 had read Human, but below High: Borrow Love's "Then take a small piece..." (Medium then) and three sentences of If You Want to Kill Yourself's first paragraph (Low then). None of those words changed between the rounds. Of the 79 windows round 8 read below High whose words were also in round 6, 64 were below High in round 6 too (49 Medium, 15 Low).

**Every window round 8 read below High** is in [WINDOWS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t115-results/WINDOWS.md), by section, with its paragraph, whose words, and round 6's reading of the same words: 4 AI (Low), 8 Human Low and 81 Human Medium, 23 of them seams of three words or fewer.

## Your question: were these saved, and were they treated the same as a pass?

Saved: every window, with its confidence, from rounds 1, 2, 6 and 8. Rounds 3 to 5 wrote down only their AI windows; the others are still on those rounds' feed pages.

Treated the same: yes. Every round's scoring and every fix pass counted a Human window as passing whatever its confidence. In turn 109 you asked me to save round 6's below-High windows, and I listed all 111, but no pass worked on them. Your point holds in this data: the four that turned AI were below High the round before.

From now on (lesson E276 (Inner Child) in [docs/HUMANIZATION-GATE.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/docs/HUMANIZATION-GATE.md)), every whole-guide read keeps every window and lists the ones below High with the round before's reading, an item's result gives its words below High beside its words in AI windows, and a pass works on them in this order: AI, Low, then Medium.
