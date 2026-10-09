# The whole-article dedup pass, turn 35 (2026-10-08): inputs and reports

The write-up is `../../DEDUP-PASS-20261008.md`. These are the four readers' inputs and reports, kept so the findings can be checked.

- `article_blocks.md`: the article as it stood (comments removed), each block numbered [B#]. Every block number in the reports and the write-up is from this file. Two bracketed notes stand in for the embedded posts.
- `guide_items.md`: the waiting groups (depth, pleasantness, isolation and C2): each group's r4 guide passage, where it would go, and the drafts as they stood after turn 34.
- `prompt_A.md` and `out_A1.md`, `out_A2.md`: two separate readers, each looking for every point the article makes twice, and for contradictions.
- `prompt_B.md` and `out_B1.md`, `out_B2.md`: two separate readers, each checking every guide point and every draft sentence against the whole article (SAID, PARTLY, NEW).

Each reader was an opus subagent that hadn't seen the drafting. The prompts named scratch paths; here they're `./`. From now on the same prompts come from `tools/humanization/reviewer/reviewer.py dedup` and `reviewer.py repeats`, which number the blocks a little differently (they leave out the title and the working-review note, and number the embeds), so match by quote, not by number, across runs.
