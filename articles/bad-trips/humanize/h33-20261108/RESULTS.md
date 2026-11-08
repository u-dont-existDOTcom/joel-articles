# What carries his round-24 versions (2026-11-08, the session's own resume of 15:52 UTC)

Each test takes out of his Human version what I can't write myself, so a Human result says his frame carries it
(`build_tests.py`). Pangram's web app on his account; each prediction is in `../pangram-ledger.jsonl` first, each text
has its receipt (`make_receipts.py`, `fill_aft1.py`) and the needed read is in `NEEDED-READ.md`. The "base" in a test is
the first five minutes down to his reminder: the Human text every part is checked after (bad-trips-2026-11-08b), not a
merge.

| test | what it keeps | result | windows | link |
|---|---|---|---|---|
| SNOJ: his Give the Session without the Kenya story, the sitter joke and the redosing aside | the order of a session, the reasons, the "If ..., though" branches | Human Written, 0% AI | High 257, Medium 3 ("Stop adding stimulation.", bare once its aside went), High 82 | [22506017](https://www.pangram.com/history/22506017-45a9-43c3-bcd2-ccb3c5732ed7) |
| FNOJ: the base, then his anchor line ("not a guru" for his picture) and don'ts without the demon line and its aside | the role line, the scene items, the example, the concession, the soft end | Human Written, 0% AI | High 78, Medium 11 (a base sentence), High 105, Medium 60 (his first three don'ts), High 20 (his concession), Medium 29 (the last don't and the soft end) | [2a2e7aa4](https://www.pangram.com/history/2a2e7aa4-5375-460b-8412-4480c5b5c3a5) |
| AFT1: the base, then What Kind of Aftermath Is This?'s first two kinds in his frame, my words | the labels said as the reader's conditions, plain steps, the payoff as the reason | AI Detected, 56% | AI Medium 49 (the base's first sentence, pulled in), Human Medium 19, Human High 103, AI Medium 6 (the heading), AI High 86 (my first five sentences), AI Medium 11 (my last) | [808d56ff](https://www.pangram.com/history/808d56ff-7233-4aef-82ce-9b9092a6cd65) |
| AFT2p: the same two kinds alone, rewritten for the panel on AFT1 (`panel-AFT1/`) | one paragraph, a fix for each sentence two readers agreed on | AI Generated, 100% | AI High 112 (the whole text) | [bd962b1b](https://www.pangram.com/history/bd962b1b-99ca-487b-ac0f-1554e3b01a7d) |
| AFT3: the same two kinds alone, written from the contrastive read (`CONTRAST.md`) after the panel on AFT2 | three paragraphs; qualifiers inside the claims, an "although" mid-sentence, tails past the point, each kind opened on the reader's case | AI Generated, 100% | AI High 167 (the whole text) | [0ec38b6c](https://www.pangram.com/history/0ec38b6c-3395-42a6-b2ff-438096efe532) |

What it shows:
- His frame carries his own words with nothing personal in them: both read Human with his story, joke, opinion and
  pictures taken out. The demon line and its aside are what lift his don'ts from Medium to High: a break of his own
  in the middle of a run of don'ts. His concession ("While many interpretations are possible, ...") reads High even
  without it.
- With the story gone, the fresh reader found his "Sometimes people find that when they prepare ... The work is already
  done." unclear and unneeded: the story is what makes those two lines make sense, so it carries meaning, not only his
  voice.
- His frame with my words still reads AI (AFT1, the 14th such try counting h31's 13). The gap is in the sentences
  themselves, as h31 found.
- Fixing what the panel agreed on didn't move it (AFT2p), and neither did writing his sentence-level moves into my
  sentences (AFT3): a fresh reader put three of his Human paragraphs beside AFT2 (`CONTRAST.md`) and named nine
  differences, and AFT3 used them all, yet read AI High over every word. The panel on AFT3 (`panel-AFT3/`) still saw the
  same shape: a framing line, then one "If it's X" branch per kind, each ending in a referral. His session has "If ..."
  branches too and reads Human, so the shape alone isn't it, and what my sentences still lack is unnamed.
- So his frame carries his words but not mine, and copying his habits into my sentences doesn't either. Two of my
  drafts have now failed after the panel, so the gate's next step is a writer of another family
  (`tell_panel.py rewrite-prompt`, Codex), with the panel before its check.
