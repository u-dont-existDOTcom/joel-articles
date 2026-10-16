# Predictions and Pangram results: batch 297g (2026-10-15, after Joel's 32 b)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Every section 13 paragraph v21 changed, with records clean in gate round r14 (`s13/review-r14/`, with `DISPOSITIONS-r14.md`): H2-P3 alone, H3-P5 after H3-P4 (H3-P5 is under 50 words), H4-P5 alone, H5-P3 alone. Texts in `drafts.json`, records in `GATE.json` (built by `make_batch.py`). Predictions written before the call; results from the History, each with its check link (E175).

## Batch 297g

| text | mine | why | Pangram |
|---|---|---|---|
| S13v21-2P3 | Human | it read Human (291g) with "Yes, it keeps getting longer."; now that line is gone and "Both of them!" closes it, the published claim said again as a reaction | **Human** (low; 75 words; AI likelihood 0.04), 21:03:55, [check](https://www.pangram.com/history/9f00d15f-1dcb-44a4-a303-92c5a0fbf867) |
| S13v21-3P4P5 | AI | H3-P4 read Human, but H3-P5 is now nearly the published sentence ("For the full sequence ... the vision comes before the members, the members before you pool the major resources, and the land comes last"), with only the pointer to the reading list as mine | **Human** (medium; 137 words; AI likelihood 0.00), 21:04:06, [check](https://www.pangram.com/history/5bb8ef86-7a12-471e-bb82-e33858c8b78c) |
| S13v21-4P5 | Human | the questions that read Human (294g), with "Write down your answers to these questions:" and the hint ending "! 😜"; the risk is the new imperative opening | **Human** (medium; 108 words; AI likelihood 0.03), 21:04:17, [check](https://www.pangram.com/history/594647ac-b020-4429-b129-894af4796e52) |
| S13v21-5P3 | Human | it read Human (295g, 0.15) with "Just not the community itself!"; three words changed | **Human** (medium; 110 words; AI likelihood 0.19), 21:04:28, [check](https://www.pangram.com/history/88ec5488-e8db-431d-8041-ed2084e65b22) |

Results of 297g (Pangram's History, 2026-10-15 UTC): all four read Human: H2-P3 alone with "Both of them!", H3-P5 after H3-P4 with the published pairwise order and the pointer to the reading list, H4-P5 alone with "Write down your answers" and the hint's 😜, and H5-P3 alone with "Just not whoever's being reviewed!". Every paragraph of v21 now has a Human check on its own text. Score: 3 of 4 (wrong: S13v21-3P4P5). Every text checked is the one in `drafts.json` (same SHA-256).
