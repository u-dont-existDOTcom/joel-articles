# Checks of 2026-11-05 (turn 11): his round-6 paragraphs, and round 7's four drafts

Pangram's web app on his account, through the Claude desktop app's browser pane, `tools/humanization/pangram_page_helpers.js`'s
`__run` and `__readC`: each text's SHA-256 checked before the click, each result read back from his history by SHA-256.
Predictions in `../pangram-ledger.jsonl` before every check. The first seven predictions were voided unsent: `predict` had
hashed each file with its final newline, so no hash was the text Pangram reads; `predict` now hashes the text without it
(with a test), and they were made again. Every window's confidence is given; less than High is work to do (E278), Low
first.

Each draft of mine has its making-sense receipt beside it (`R7-N.receipt.json`, gate E363) and its newcomer reads
(`newcomer-R7-N/`: the first read, of the paragraph as it was; `draft/`, of the draft as checked; `draft-N/`, of earlier
drafts, each gap answered or dropped with a note). The reads changed three drafts before Pangram saw them: "the syndromes
it's approved for" read as the gel being approved (now "oral CBD"); "adjuncts to what?" after his move (now "alongside
any rescue medicine"); and the topical CBD paragraph's conclusion, which two readers couldn't draw (now said).

| text | whose | try | result | windows | link |
|---|---|---|---|---|---|
| the warning stage, with his humic line (N-WARN) | his version (my five sentences, his last) | 1 | Human Written, 0% | Human, High | [result](https://www.pangram.com/history/d6589034-372d-4da4-a85b-1121a8e07f6c) |
| cannabis at an aura and the ABRACE spray (N-CANNA-1) | his | 1 | Human Written, 0% | Human, High | [result](https://www.pangram.com/history/ae1cbe48-eeb7-4e04-8b62-bbb970071cb1) |
| the forums and studies paragraph (N-CANNA-2) | his opener, my two sentences | 1 | AI Detected, 62% | Human Low (his opener); AI Medium ("But other people say ... cut them about in half."); AI Low ("So the THC may be what makes it go either way.") | [result](https://www.pangram.com/history/64d111ca-8c3a-4d94-adc5-beb4a8b32bf0) |
| topical CBD (N-CBD-2) | his | 1 | Human Written, 0% | Human, High | [result](https://www.pangram.com/history/b24a1f68-fe39-4ef8-bfef-a03bbce3dc1c) |
| R7-1, ABRACE: patients' association, more than 30 tests | his, two changes | 1 | Human Written, 0% | Human, High | [result](https://www.pangram.com/history/a5570612-ceb1-479d-815e-1cb646423ebc) |
| R7-2, the gel trial's authors, and the conclusion | his, one sentence and a clause mine | 1 | Human Written, 0% | Human, High | [result](https://www.pangram.com/history/954a53dc-72c4-457a-b5e2-3e87a8e4ade6) |
| R7-3, P3 after his move: "During the seizure, alongside any rescue medicine", no focal sentence | his, the opening mine | 1 | Human Written, 0% | Human, High | [result](https://www.pangram.com/history/ffbdf673-64f0-4253-8712-88b419ddb4f4) |
| R7-4, the forums paragraph: my sentences split, the rats introduced, "cannabis" for "it" | his opener, mine | 2 | AI Detected, 51% | Human Low (his opener); Human Low ("But other people say THC vapes and concentrates brought their seizures on."); AI High (the rats and "So the THC may be what makes cannabis go either way.") | [result](https://www.pangram.com/history/b8fbfcbc-c2d9-48b7-a1f8-0510320bb0a1) |
| R7-4, the forums paragraph: the panel's agreed tells cut (the gloss, the mirrored CBD result, the summing-up close), "a few people on the same forums", "And rats bred to have seizures" | his opener, mine | 3 | Human Written, 0% | Human, High | [result](https://www.pangram.com/history/59bba2ed-ed63-4db5-9884-5bcd465d4ec2) |

Tell panel on try 2 (Codex on his laptop, Sonnet, Haiku): `panel-R7-4/PANEL.md`. All three agreed on the gloss ("the brief
staring seizures called absence seizures"), the mirrored "more ... while ... about in half" and the summing-up close; two on
the "That matches" bridge and the "some swear / other people say" frame. A second panel on the fixed draft
(`panel-R7-4b/PANEL.md`) agreed on two smaller things ("some" twice, a trailing "too"), fixed before the check.

What it shows. Every text of this round read Human, High, on its first try except the forums paragraph, which took three:
the first fix (split, the rats introduced, "cannabis" for "it") moved one sentence to Human but the rats and the close to
AI High; the third, after the panel, cut what all three readers agreed on and read Human, High. The two newcomer reads per
draft caught three sense breaks before Pangram did ("it's approved for" read as the gel; "adjuncts to what?" after his
move; a conclusion two readers couldn't draw). Predictions: 8 of 9 right; the miss was the forums paragraph's try 2, which I called Human at 0.5 (the voided seven were made again before any check).
