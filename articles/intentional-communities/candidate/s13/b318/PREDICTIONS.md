# Predictions and Pangram results: batch 318g (2026-10-17, the last three paragraphs of section 13 draft v34)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). After batch 317g read the whole of v34 100% Human, its install script ran `tools/humanization/paragraphs_alone.py` (Joel's rule: every paragraph passes alone) and stopped: three paragraphs had no check of their exact text alone. H3-P5, the book line (31 words by spaces, so it goes with H3-P4, which v34 changed); H4-P6 and H5-P4, made plainer in v32 at the pause tally and never read alone since (batches 314g and 316g read other paragraphs). Screens as batch 317g's (round r21's marches for these paragraphs; lint REVIEW; keys PASS). Predictions written before the run.

## Batch 318g

| text | mine | why | Pangram |
|---|---|---|---|
| S13v34-H3-P4+P5 | Human | H3-P4 read Human alone in 317g (0.00), and the pair read Human in 314g (0.00) with H3-P4's earlier wording | **Human** (Human Written, high, 172 words, AI likelihood 0.00), 01:35:35, [check](https://www.pangram.com/history/b400ad04-6b3c-4401-b38f-b0d4946fb8ef) |
| S13v34-H4-P6 | Human | v31's read Human alone in 312g (0.00, low); "think someone's safe just because they're going along with everyone else" and "Six months with someone" are plainer, not more polished | **Human** (Human Written, low, 78 words, AI likelihood 0.03), 01:35:46, [check](https://www.pangram.com/history/4f539847-67cd-40c0-a568-5408c983df8f) |
| S13v34-H5-P4 | Human | v31's read Human alone in 312g (0.00, low); one word changed, "ombudsperson" for "ombud" | **Human** (Human Written, low, 74 words, AI likelihood 0.00), 01:35:57, [check](https://www.pangram.com/history/16d79008-8451-42a6-a85b-46fb8e1a3b17) |

Results of 318g (Pangram's History, 2026-10-17 01:35:35 to 01:35:57 UTC): 3 of 3 predictions right; all three read Human alone (0.00, 0.03, 0.00). Run from the page with the items passed in directly (hashes checked in the page against `b318-items.json` before the run), not fetched from GitHub. Why these three were missed: batches 314g and 316g took their paragraph list by hand, and the plainer words from the pause tally (made after the traces) never joined it; the install check caught it. Lesson: before building a batch, run `paragraphs_alone.py` on the draft and put every paragraph it reports as never checked into the batch.
