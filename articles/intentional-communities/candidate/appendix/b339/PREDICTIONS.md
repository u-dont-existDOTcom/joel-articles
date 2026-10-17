# Predictions and Pangram results: batch 339g (2026-10-17, the appendix v7 and v7x)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Two more shapes of the research paragraph, both from r4 with its list broken up (`../make_v7.py`): r5 alone and in v7, r6 alone and in v7x (both with Orlov o1), and the two runs trace T3's Doucleff fix and the Christian question changed (Liedloff with Doucleff, Doucleff with the heading and Christian). Built by `../apx_batch.py`; marches review-r9 and r10 (two readings, a break in each); lint REVIEW. Predictions written before the run.

## Batch 339g

| text | mine | why | Pangram |
|---|---|---|---|
| APXv7-E12-13 | Human | Christian as a question and its answer; Doucleff's three topics as a plain list | **Human** (Human Written, low, 56 words, AI likelihood 0.11), 06:26:08, [check](https://www.pangram.com/history/0498e23d-e67f-407e-a08d-73e13903d24f) |
| APXv7-E11-12 | Human | Liedloff's question and answer; Doucleff shorter | **AI** (AI Generated, low, 68 words, AI likelihood 0.52), 06:25:15, [check](https://www.pangram.com/history/cd908484-00f3-4886-be94-9dfc1c56ad72) |
| APXv7-E25 | AI | r5 keeps the list in one sentence ("the evidence base and its limits, the counterexamples, what I still couldn't verify, etc."); every one-sentence list so far read AI | **Human** (Human Written, low, 74 words, AI likelihood 0.16), 06:25:26, [check](https://www.pangram.com/history/3f783974-5947-46a9-91a1-f1a26c91f0bd) |
| APXv7 | Human | o1 and r5; v6x (r4) read 100% Human whole (336g, 0.15) | **Human** (Human Written, high, 681 words, AI likelihood 0.20), 06:25:36, [check](https://www.pangram.com/history/744f3011-fcc1-4048-8db9-caede43c17f9) |
| APXv7x-E25 | Human | r6 spreads the list over two short sentences ("The evidence base is in there, and where it runs out. So are the counterexamples, ...") | **Human** (Human Written, low, 79 words, AI likelihood 0.18), 06:25:48, [check](https://www.pangram.com/history/0b1db925-ad03-4ee6-aadd-26212aab3c27) |
| APXv7x | Human | o1 and r6 | **Human** (Human Written, high, 686 words, AI likelihood 0.21), 06:25:58, [check](https://www.pangram.com/history/c0260e63-0b84-43c2-a1aa-37bf5f109637) |

Results of 339g (Pangram's History, 2026-10-17 06:25:15 to 06:26:08 UTC): 4 of 6 predictions right. The research paragraph reads Human alone for the first time, in both new shapes (r5 0.16, r6 0.18), after seven shapes that read AI; with either, the whole appendix reads 100% Human, high (v7 0.20, v7x 0.21). Christian's entry as a question reads Human in its run with Doucleff (0.11). But trace T3's fix of Doucleff's entry (the three topics as a plain list) makes the pair with Liedloff read AI (0.52; with the old wording, 331g, 0.06), and the pair is the one run that can check both entries (`paragraphs_alone.py`: a same-heading pair that reaches 50 words). Next: two more Doucleff shapes that keep the three topics (`../make_v8.py`, batch 341g), and the traces of r5, r6 and Christian's entry (review-r12 and r12x).
