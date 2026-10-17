# Predictions and Pangram results: batch 409g (2026-10-17, section 16 v26 kni, its changed paragraphs)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Section 16 v26 kni (`../make_v26.py kni`), the best faithful version so far (all of meaning round r42's fixes in; the whole section Mostly Human, 0.32, one 61-word window, 399g): H3-P6 and H3-P7, changed from v25, alone and with their neighbors, for `paragraphs_alone.py`. March review-r44; lint REVIEW. Predictions written before the run.

## Batch 409g

| text | mine | why | Pangram |
|---|---|---|---|
| S16v26kni-H3-P6 | Human | a paragraph of v26 kni (Mostly Human whole, 0.32), alone or with its neighbor | **Human** (Human Written, low, 55 words, AI likelihood 0.02), 12:20:02, [check](https://www.pangram.com/history/25e80c83-6bc2-4a29-998c-7261a238fea1) |
| S16v26kni-H3-P5+P6 | Human | a paragraph of v26 kni (Mostly Human whole, 0.32), alone or with its neighbor | **Human** (Human Written, low, 96 words, AI likelihood 0.15), 12:19:28, [check](https://www.pangram.com/history/530237b0-731d-4e0d-b057-5c69b56f801d) |
| S16v26kni-H3-P6+P7 | Human | a paragraph of v26 kni (Mostly Human whole, 0.32), alone or with its neighbor | **Human** (Human Written, low, 73 words, AI likelihood 0.12), 12:19:40, [check](https://www.pangram.com/history/23b759ac-0f52-443e-9025-d66415972448) |
| S16v26kni-H3-P7+P8 | Human | a paragraph of v26 kni (Mostly Human whole, 0.32), alone or with its neighbor | **Human** (Human Written, low, 72 words, AI likelihood 0.00), 12:19:52, [check](https://www.pangram.com/history/1b79d3b6-221b-4cb2-9ed5-c57a3683c000) |

## Results of 409g

Four of four right: H3-P6 alone (0.02) and every pair with H3-P6 or H3-P7 (0.00 to 0.15) read Human. With 388g and 389g, every paragraph of v26 kni reads Human alone or in its pair; the whole section reads Mostly Human (0.32, 399g), which is question 42.
