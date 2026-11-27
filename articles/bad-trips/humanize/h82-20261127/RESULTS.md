# Turn 74 (2026-11-27): his round-63 answers in; Beach Morning Glory reordered, one window left

His round-63 export of 20:03 UTC ([the answers](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r63/ANSWERS-R63-20261127-2003.json);
[what happened to each point](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r63/RESULTS-R63.md)). His check of his version was read from his
history in the built-in browser and matched to his text by SHA-256 ([HIS-CHECKS-R63.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r63/HIS-CHECKS-R63.json)).
Three fresh readers read the section as first drafted with both answers in ([needed](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h82-20261127/reads/need-draft-bmg-sec.txt),
[his fixes](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h82-20261127/reads/his-draft-bmg-sec.txt), [fit](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h82-20261127/reads/fit-draft-bmg-sec.txt)): the skin amounts, given before
the amounts by mouth, read as a second dose (the fit reader couldn't tell which one ends a trip), "For that" could point at
two things, and "I don't think anyone has the juice" left nothing to do. So B174 now follows B173, and its amounts point
back to the ones by mouth. Every text was checked through the API on his laptop with his key, plain, each with its
prediction in the ledger first: 11 checks, 11 calls right. Every dose and warning held (the R62 fidelity keys, the
owner-edits and keep-as-is checks), and each text of mine that went in passed the apply gate. The texts are built from Git
by [build_h82.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h82-20261127/build_h82.py); his words are copied from his answers file, never retyped.

## What went in ([apply_h82.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h82-20261127/apply_h82.py))

| Paragraph | What | Pangram |
|---|---|---|
| B171, which plant | "People still find it growing in some places, under names like railroad vine." (his comment on TEACH-B173) | [**Human High 69**, by itself](https://www.pangram.com/history/0e0bd36d-9b6b-4cec-9a9b-46461f9ecaed) |
| B173, how much by mouth (now second) | his version, whole: [his check, Human High 84](https://www.pangram.com/history/09e42ca2-b7ef-4439-92f3-402dd6f78314); with "(the dried juice)" | [**Human High 87**](https://www.pangram.com/history/bf3ae1f3-5f84-48bc-928c-17d1b1ed7de5) |
| | then "Eating a whole leaf" (after the section's second check) | [**Human High 88**](https://www.pangram.com/history/9bae6cd1-4ee3-4c96-8ed4-934174f557e9) |
| B174, handling and the skin (now third) | his "sensitive skin" back in the skin sentence | [Human High 122](https://www.pangram.com/history/385cddfb-eada-4eca-928d-67aa8a846661), with B171 |
| | "I'd use about the same amounts as by mouth, or maybe a few drops of fresh juice if you have any." | [**Human High 143**](https://www.pangram.com/history/3da1f8d2-0cc1-48a7-8f01-39360dc89579), with B171 |
| B176, the woman | its last line's point first: "I may have given her more than I would give now, though, since I was rushing to help her." | [**Human High 87**](https://www.pangram.com/history/79f9e21f-0a71-4659-bf65-d02eb700242b), with B178 |

**The section:** its second check (2 of 2), with his answers in: [Human, High 69, **Medium 36**, High 174, **Medium 18**, High 32](https://www.pangram.com/history/3a2d2b12-c8bb-4f15-97a9-32137b5d88d3)
(turn 72's first had a Low window and four Medium). The Medium windows were B173's first two sentences and B176's rushing
line. After the two fixes above, one more check (`--after-fix`): [Human, High 69, **Medium 37**, High 225](https://www.pangram.com/history/08dff6fa-724e-4546-93df-949200cd5079). B176's line is
fixed; B173's first two sentences still read Medium beside B171, though the paragraph reads High by itself. That window is
the next work; the section's five blocks stay on [the list of what is left](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h82-20261127/LEFT.md) (119 of 222) until
it reads High in every window.

## The blind test of his fix ([replay](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h82-20261127/replay/RESULTS.md))

His one word, "smooth" for "improve", took my try 3 of B173 (High, Medium 16, High) to Human High 84 in one window. Two
fresh writers that hadn't seen it rewrote that try from the lesson alone: 1 of 2 read Human High, and not the one that
found his word.

## What I fixed in the tools

- `sense_receipt.py` maps each claim of his answers to the sentence that carries it (`his_answer`) and names every word of
  his that sentence lacks; it would have caught "sensitive skin" (lesson bad-trips-2026-11-27k; tests:
  `tests/test_sense_receipt.py`, HisAnswer).
- `his_fixes_brief.md` has his thirtieth way (lesson bad-trips-2026-11-27j), worded as the blind test found it works.
