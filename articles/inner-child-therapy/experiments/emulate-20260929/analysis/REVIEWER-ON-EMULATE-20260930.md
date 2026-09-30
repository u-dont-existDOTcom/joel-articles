# The Inner Child reviewer on Emulate's output

**By Claude, 2026-09-30.** Joel asked whether Emulate's versions had been checked with his own system, which is stricter than Pangram. They hadn't: only the linter had been run over them, in aggregate (`CLAUDE-SLOP-COMPARISON.md`). So this runs the strict part, the reviewer from the reviewer-writer loop.

## Method

The reviewer's validated route, as in the Inner Child `tools/reviewer/README.md` at `35b88b5`: fresh Opus subagents, each reading one prompt file and nothing else. The prompt was the shared rubric, the labeled examples of both folds (`examples(extra=False)`, as in the human-prose test) and the verdict format. `reviewer-on-emulate-20260930/build.py` builds it.

- **Pairs:** ten of Claude's inner child drafts that Pangram calls 100% AI, and Emulate's versions of the same drafts, which Pangram calls 100% Human.
  - The drafts: A08, A10, A18, B07, B09, B10, B12, B15, B21 and B23.
  - The Emulate versions are the `gpt_*_api_r1` outputs. Only Emulate's tokenizer noise was cleaned (`do n't`, the ``` `` '' ``` quote marks).
- **Counterbalanced:** reviewer 1 saw the drafts of the first five and the Emulate versions of the last five; reviewer 2 saw the reverse. Neither saw both versions of a pair.
- **Controls:** four Make the Protector Visible texts with known Pangram results per reviewer, none of them among the labeled examples.
- **Blind:** no Pangram results, and nothing saying which texts were Emulate's. The build checks that no test text is already a labeled example.

## Results

| text | Pangram | reviewer |
|---|---|---|
| Claude's drafts (10) | AI, all ten | AI, all ten (58 to 92) |
| Emulate's versions (10) | Human, all ten | HUMAN, all ten (55 to 85) |
| Controls, Pangram AI (4) | AI | AI, all four |
| Controls, Claude paragraphs Pangram passed (4) | Human | AI for three (60, 78, 80); HUMAN for one (62) |

The keys, prompts and answers are in `reviewer-on-emulate-20260930/`.

**The linter** (`tools/tells_lint.py` at `35b88b5`) on the same ten pairs: every draft came out REVIEW. Of the Emulate versions, seven were REVIEW, two CLEAR and one FAIL (A18, coach phrases at 2.03 per 100 words against a limit of 2.0). So it doesn't separate them.

## What it means

- **Emulate's output passes the reviewer as well as Pangram.** The reviewer is stricter than Pangram only on Claude's own writing near the line.
- **What it read as human in Emulate's versions** was mostly roughness: comma splices, a missing article ("We have explained"), garbled phrases ("after spending the month"), clumsy repetition, "etc." lists, and endings that don't sum up. Our fixes remove some of that, so whether a fixed version still passes is untested. The gate runs the reviewer on it anyway.
- **The reviewer's HUMAN was right all eleven times here,** as every time before. Its AI on Claude's passing paragraphs was wrong three times in four.

## Limits

This was ten pairs from one article's genre, with two reviewers. The reviewer learned from the Inner Child article, so these results say nothing yet about the memoir-style community article or the hypnosis and neuro de-armoring guides.
