# The word-for-sense read of the whole guide (2026-11-09, turn 29)

Gate E331 ([SKILL.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/SKILL.md), "Word-for-sense read before publication"), run on the guide after his round-27 answers went in
([GUIDE-SO-FAR.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/GUIDE-SO-FAR.md), 342 blocks, 12,774 words, sha256 `c8f55833...` before the fixes below). It needs no Pangram, so it
ran while round 28 waits on him.

## How it was read

- `sense_read.py make` cut the guide into three parts (blocks 0-105, 106-247 and 248-341) and planted three errors in
  each, kept in [CANARIES.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/CANARIES.json) beside the parts, never in them (seed 2444). [STYLE.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/STYLE.md) is the guide's "what is not
  wrong here": his voice, his coinages, the guide's terms, the remedy names, people and places.
- Three fresh readers, one part each, got only their task line from [TASKS.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/TASKS.json) (the brief and their part), never the
  folder, and were not told that errors were planted. Their reads: [reads/READ-1.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/reads/READ-1.json) to [reads/READ-3.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/reads/READ-3.json).
- `sense_read.py score`: every block of every part on its read list, and **all nine planted errors found** (whether →
  weather, warmth → wealth, than → then; lose → loose, Peace → Piece, remove → remodel; quite → quiet, than → then, calm
  → clam). So the readers' other findings, and their silence elsewhere, can be trusted for errors of this kind
  ([SCORE.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/SCORE.json)).
- `sense_read.py nonwords`, the net under the read: 103 non-words with `--known STYLE.md` and his texts marked
  ([NONWORDS.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/NONWORDS.json)). All are terms, names, pieces of links or his coinages, except "ayahauasca", which reader 1 had
  found. Run first as [SKILL.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/SKILL.md) said, with his texts as known words, the net listed 6 and hid "ayahauasca", which is
  in his post: lesson bad-trips-2026-11-09c, and `--his` in the tool now marks such a word instead of hiding it.

## What each finding was, and what came of it

Five findings beyond the planted ones ([FINDINGS-RAW.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/FINDINGS-RAW.json)), and three things the readers put in their notes. Each was
read in place and traced to its source: his post of 3 November ([original.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/original.md)), his answers, or our rounds. In this
guide the post's text is the model's drafted text except what he wrote himself (gate E373).

| Block | Where | Finding | Whose | What came of it |
|---|---|---|---|---|
| B93 (8) | When to Bring In Outside Help | "Call medics while acting for:": "acting for" reads as acting on someone's behalf | the post's drafted heading | **Fixed:** "Call medics for:". The line under the list already says what "while acting" meant ("The remedies below can begin while help is being arranged."), and the next heading reads the same way ("Bring in mental-health support when:"). |
| B249 (164) | Stillness or Movement? | "Test them rather than ...": "them" points only at the heading | the post's drafted text | **Fixed:** "Test stillness and movement rather than turning them into rival religions." |
| B428 (333) | No "another ceremony will fix this" reflex | the list after "Don't take more" turns from things taken into things done, so "take more" governs "intense breathwork" and "fast" reads as an adjective | the post's drafted text | **Fixed:** "Don't take more psychedelics, cannabis or ketamine, do intense breathwork, fast, ..." |
| B182 (103) | Metta NMT Sniffer | "ayahauasca" | his own (his sniffer-stick paragraph, first person, in his post) | **To him:** round 29, card TYPO-AYA, the fix in place ("ayahuasca", as the paragraph spells it two sentences later), advice Approve. |
| B219 (138) | Some Remedies Require More Caution | "hyperintelligent", then "hyper intelligent" (reader 2's notes) | his own (his humic acid paragraph, first person, in his post) | **To him:** round 29, card TYPO-HYPER, "hyperintelligent" both times, advice Approve. |
| B141 (68) | the hierarchy's gut line | "is often mistaken as shadow work": "mistaken for" is the usual idiom | his own: his round-1 wording (card RP-4, 2026-11-03 18:59 UTC), on the keep-as-is list as K2 | **Kept:** "mistaken as" is a common form of the idiom, not a wrong word, and he chose this sentence "to sound more human". |
| B354 (268) | the MDMA section | "the commenters on the first thread" after "Here's a reddit poster" and "this thread" (reader 3's notes) | his own (his Reddit paragraph, in his post) | **Kept:** the paragraph links two Reddit threads, the poster's and the one "on this thread", so "the first thread" is the poster's; a reader can follow it. |
| B327 (237) | Two questions while glowing | a "2." with no "1." before it (reader 2's notes) | not in the guide | **Tool fixed:** the guide has both numbers; the part had dropped the first item's marker while the later items kept theirs. [tools/humanization/sense_read.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/tools/humanization/sense_read.py) now prints it ([tests/test_sense_read.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/tests/test_sense_read.py), test_list_markers). Reader 3's "numbering run-ons in 284" was the same thing, and its "stray markup in 267" ("**gone, **and") renders as his post has it, `<strong>gone, </strong>and`. |

The three fixes are [fix_slips.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h38-20261109/sense-read/fix_slips.py), beside this file. After them: the fidelity keys (R26) pass, the keep-as-is list
holds (23 kept, 12 meant cuts, none gone or back), his edits pass (64 of 64, 3 waiting for the humanize pass), and
the typography check finds nothing to swap. No Pangram check was run on them: the paragraphs they're in are the
drafted text the humanize pass will rewrite after the guide makes sense (his rule of 2026-11-08 17:22 UTC), and none
of the three changes what the text says.

Round 29's page: Bad Trips Guide, Round 29, https://claude.ai/artifact/HF6U6SMg9CVfLtzSeKrx84 (a view of
[review/r29/REVIEW-R29.html](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/review/r29/REVIEW-R29.html); its cards as text are [review/r29/REVIEW-R29.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/review/r29/REVIEW-R29.md)).
