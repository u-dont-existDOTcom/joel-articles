# r50: his whole-article check of the r49 drafts (2026-11-27 19:27 UTC), and its two Medium windows

His message: "go" and the result pages of his Pangram extension on the two drafts pasted at r49:
[draft A](https://www.pangram.com/feed/1a5fcb3a-949b-4ad7-8117-b48f4d21db49) and
[draft B](https://www.pangram.com/feed/e8d99033-318d-4a92-9910-719ddccd48a5).

## The results

Read back from the feed's API in the built-in browser, every window with its confidence:
[RESULTS-whole-r49.json](RESULTS-whole-r49.json). Each check's text is the draft's rendered text exactly (A's SHA-256 is the
one [DRAFTS.json](../whole/DRAFTS.json)'s r49 entry recorded; B has the 57,048 characters it counted).

- **Draft B: Human Written, High, six windows, every one Human High.** Its r39 Medium window is gone.
- **Draft A: Human Written, High, ten windows: eight Human High and two Human Medium,** the same two one-sentence
  windows as at r39, their text unchanged since: the last line of live 20 ("Affection and the simmer") and the first line
  of live 33 ("Situationships").

## Why those two sentences, and what they were hiding

The feed gives every window its AI likelihood, and windows that share one are one segment: B's six windows are one
segment; A's windows 4 to 9 are one. Each Medium sentence is a segment of its own, with a likelihood (1.9e-12, 5.5e-15)
seven to thirteen orders above the text beside it (1.4e-25, 1.3e-19, 1.8e-21): Pangram split off the sentence that read
most like AI where it is, and a 16-word window can't reach High.

At r39 I called them "single sentences of his live text that Pangram cut off at the edge of a window" and left them.
Checked by itself now, live 20 reads
**[AI Detected, 41%](https://www.pangram.com/history/36aa6a6d-b5c1-4bba-8a68-129dcee268f9)**: its last line AI-Generated
(likelihood 1.00), the line before it AI-Generated Low. Its section read Human High in one window at r38, which hid it.
Live 33 reads [Human High](https://www.pangram.com/history/defcad22-a228-43a1-9e7a-e58878a8146c) by itself; only the
whole article split its first line off. Lesson [romance-2026-11-27b](../../../../../docs/lessons/2026-11-27-1927-romance.md).

## The two changes (in as [MINE-R50.json](MINE-R50.json), [mine_r50.py](mine_r50.py))

Every check: [CHECKS-R50.json](CHECKS-R50.json).

- **Live 20.** "A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate
  touch becomes a bid for sex, affection itself can start feeling like pressure." became "A hug, cuddle, kiss, or back rub
  should sometimes be allowed to end right there, or she'll start treating every touch like a sales pitch." The last line
  was a closing line that sounds wise and says the line before again (ways 6 and 16 of
  [his fixes](../../../../../tools/humanization/his_fixes_brief.md)); joined to the line it explains (way 8) and said as
  what it looks like. The paragraph: [Human High](https://www.pangram.com/history/52ff7f0c-e151-4e8d-a553-fc4282ee3be5);
  its section: [Human High, one window](https://www.pangram.com/history/27c3b372-bc6e-4443-b057-e593fd1b9821). Two other
  wordings read Human High too ("every hug", "or else every touch starts to feel like a sales pitch for sex"); "every
  touch" went in because the hug stands for all four.
- **Live 33.** "And then there's the situationship, which is hard to define because that's basically the point. Usually
  it's a happenstance relationship based on sex." became one sentence: "..., which is hard to define because that's
  basically the point, but usually it's a happenstance relationship based on sex." (way 8), his words kept. The
  paragraph: [Human High](https://www.pangram.com/history/722d3172-fb10-4237-97be-d89a690f5d31); its section:
  [Human High, one window](https://www.pangram.com/history/7ff558af-740d-40f9-8dcc-5475da271f17).

Neither is a version of his from a page, a kept line or a card (`whole/KEEP-AS-IS.json`, the HIS layers), and neither
changes what the paragraph says, so they went in without a card (AGENTS.md: a tested change goes in, named in the report).

**The word-for-sense read** of both sections with the changes ([sense/](sense/)): one fresh reader, every block read, 3 of
3 planted errors found. Its one other finding, "the existential void another superficial fix creates" (a relative clause
without "that"), is fine in place and unchanged text; nothing in the two changed sentences.

**The card game** ([BUILT-ON.json](../../../../BUILT-ON.json)): the cards that name the two sections
(`sex-affection-simmer`, `clarity-undefined-thing`, `solo-uneven-love`) say nothing the changes alter; no card changes.

## Next

Draft A pasted again with the two changes, for his extension; B is unchanged. See the round's entry in
[DRAFTS.json](../whole/DRAFTS.json).
