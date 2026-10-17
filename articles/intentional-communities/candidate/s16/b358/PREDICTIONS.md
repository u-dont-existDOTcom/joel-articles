# Predictions and Pangram results: batch 358g (2026-10-17, section 16 v16 shape eeee)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Section 16 v16 (`../make_v16.py eeee`): v15 q with only H3-P3 changed (354g's), a control for the colon sentence's window. The run that starts at H3-P2 and the whole section. March review-r20 and r31; lint REVIEW. Predictions written before the run.

## Batch 358g

| text | mine | why | Pangram |
|---|---|---|---|
| S16v16eeee-H3-P2-P4 | Human | v15 q's run read Human (0.03); only H3-P3's colon sentence changes | **Human** (Human Written, high, 163 words, AI likelihood 0.14), 09:10:48, [check](https://www.pangram.com/history/66913b7d-6fe7-401e-8228-ca53f064b0b5) |
| S16v16eeee | Mixed | a control: only H3-P3 changes from v15 q, so the window from H3-P4's end on should stay | **Mixed** (AI Detected; windows: Human, High, 459; AI-Generated, High, 43; Human, High, 40; AI-Generated, High, 341, 883 words, AI likelihood 0.50), 09:10:58, [check](https://www.pangram.com/history/cf67f073-9280-4147-bd92-b56e85addfed) |

## Results of 358g

Two of two right. The control: with only H3-P3 changed from v15 q, the run H3-P2 to H3-P4 read Human (0.14) and the whole section read AI over the same two windows as the other v16 shapes (341 and 43 words). So the 250-word window of v15 q became one window from H3-P3's second sentence whatever the tail was.
