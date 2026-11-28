# AI slop that passed Pangram: his edits of text that already read Human

Joel, 2026-11-28 15:19 UTC: "i also want you to keep track of whenever i edit a section because it doesn't get my
points across, try to develop some understanding of which sections might be ai slop even if they pass pangram high conf.
you surely already have many of my edits like this saved but probably you haven't been using them if they didn't
directly help with pangram, you prob just tagged them as "only author could do this" but should have tagged as "pangram
passed ai slop" or whatever else you can figure out more specifically about why i might have edited it."

The rule is R-slop-that-passed in [the rule tree](../../rules/README.md). Each time he edits a passage because it
doesn't get his point across, the passage goes in [entries.json](entries.json): the version he fixed, how it read in
Pangram (each check's link and windows), his version, his words, and what the version lacked, said specifically. That
last part is the editor's reading, marked as such, until he confirms it. An edit is put down to "what only he could
add" only for the fact or story itself; whatever else it fixed is a fault the editor could have seen.

## The record so far

**1. Romance, "Things get tricky fast" (his edit of 2026-11-28).** An earlier, nearly identical wording read Human,
High, in one window, three times: [2026-11-07](https://www.pangram.com/history/dd569cb2-3b4c-4f43-bebe-d9043481e166),
[2026-11-23](https://www.pangram.com/history/ec654e49-002c-49c2-9390-b49bbc0a0af6) and
[2026-11-24](https://www.pangram.com/history/8d300648-e283-4b37-842c-ff05f7caeaf5). The version he rewrote changed a
few sentences after that and wasn't checked itself. He rewrote all of it. What it lacked, in our reading:

- **his point**: ask people you trust about a new partner, early, because it gets harder to hear them the longer you
  wait. The section never said it;
- **what the reader does**: it described what couples do ("Couples withdraw from friends ...") where his speaks to
  "you";
- **plain words**: "the romantic dyad", "the only reality in the room";
- **no tidy closers**: "The relationship can close off at exactly the point when both people most need a view from
  outside it.";
- **no hedge that dilutes the point**: "Sometimes withdrawing isn't wrong.";
- **no short robotic lines**: "Friends hear less. Sharp questions start to feel rude.";
- **a pointer that says where**: "I'll come back to that." against his "I'll expand on ... in Don't Make Your Partner
  Your Whole World.";
- and his own story, which is his to add (the first wife, the OKCupid profile).

**2. The places where an edit of his was put down to "what only he could add"** (27 in the lessons, the replay results
and the old gate), re-tagged by a fresh reader: [RETAG-20261128.md](RETAG-20261128.md). 11 were faults the editor
could have seen without him, 13 were really his (a fact, a story, a decision, an opinion), and 3 weren't about an edit.
In 7 of the 13 his fact came with a wording fix that the tag hid. The faults that recur:

- empty abstract words where a thing should be named ("meaningful", "prepared correctly", "quality mattered
  enormously", "the power", "capacity");
- a passage that describes and never says the point or what to do, then ends on a closer;
- in cautions, a hedge the evidence doesn't back, the conditions before the consequence, "it's fine to" for an
  instruction, a risk with no reason given;
- emphasis added to sound human ("or you just stop caring"), taken for his voice.

**What the record can't show yet.** Of the 111 fixes of his collected on 2026-11-12
(`articles/bad-trips/humanize/h46-20261112/his-fixes/PAIRS.json`), only 6 had their version checked in Pangram as it
stood before his fix, and none of those had read Human High: the lanes checked text they meant to change, not text that
already passed. [find_passed.py](find_passed.py) does that count. A first try matched checks by the first 200
characters and took three checks of his own versions for the versions he fixed; the reader caught it, and it now
matches the whole text. So from now on, when he edits a passage, the lane looks up how that version read before
recording it.
