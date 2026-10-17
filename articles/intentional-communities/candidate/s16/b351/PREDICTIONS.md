# Predictions and Pangram results: batch 351g (2026-10-17, section 16 v15 shape q)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Section 16 v15 (`../make_v15.py`), shape q: H3-P2 opening on a question ("So what do you actually do this month?"), v13's H3-P3, v11's H3-P4. Every run of three that holds H3-P2 to H3-P4 (`../slide.py`), each of them alone or with a neighbor, and the whole section; texts screened before are left out (their results stand). Marches review-r23 and r30 (two readings, a break in each); lint REVIEW. Predictions written before the run.

## Batch 351g

| text | mine | why | Pangram |
|---|---|---|---|
| S16v15q-H2-P5-H3-P2 | Human | a run or pair around H3-P2 to H3-P4 | **Human** (Human Written, medium, 149 words, AI likelihood 0.13), 08:43:29, [check](https://www.pangram.com/history/0b6d4f99-f4bb-4804-85ee-c331aebfbdc4) |
| S16v15q-H2-P6-H3-P3 | Human | a run or pair around H3-P2 to H3-P4 | **Mixed** (AI Detected; windows: Human, Medium, 94; AI-Generated, Medium, 35, 129 words, AI likelihood 0.31), 08:43:40, [check](https://www.pangram.com/history/c0bc5526-2a20-48b4-8b2a-1eb8da148509) |
| S16v15q-H3-P2-P4 | Human | a run or pair around H3-P2 to H3-P4 | **Human** (Human Written, high, 154 words, AI likelihood 0.03), 08:43:50, [check](https://www.pangram.com/history/bdf9aef4-0c58-4d4a-bc8d-0b3ed0e73d0f) |
| S16v15q-H3-P3-P5 | Human | a run or pair around H3-P2 to H3-P4 | **Human** (Human Written, high, 152 words, AI likelihood 0.06), 08:44:01, [check](https://www.pangram.com/history/1101ecb2-62a1-4e8b-b047-0e9ad715f6e3) |
| S16v15q-H3-P2+P3 | Human | a run or pair around H3-P2 to H3-P4 | **Human** (Human Written, low, 89 words, AI likelihood 0.01), 08:44:12, [check](https://www.pangram.com/history/fda8e1da-b9e8-4a69-baab-8f207ad29a6b) |
| S16v15q-H3-P3+P4 | Human | a run or pair around H3-P2 to H3-P4 | **Human** (Human Written, medium, 112 words, AI likelihood 0.07), 08:44:22, [check](https://www.pangram.com/history/be0a5279-2f1b-4d2d-aa1d-082c7fc89aa5) |
| S16v15q | Mixed | the whole section | **Mixed** (AI Detected; windows: Human, High, 542; AI-Generated, High, 35; Human, High, 47; AI-Generated, High, 250, 874 words, AI likelihood 0.47), 08:44:33, [check](https://www.pangram.com/history/53673eef-b6e6-4e3c-879e-da1505286134) |

## Results of 351g

Six of seven predictions right. Shape q's H3-P2 works: every run of three over H3-P2 to H3-P4 and both pairs read Human (0.01 to 0.07), where v14's read 0.91 to 0.99 (350g). Two places still read AI in the whole section (0.47): H3-P3's colon sentence ("Call it that, not a commune! Before you start talking about a shared future, meet regularly: practice listening and switching roles, get through at least one disagreement together, and keep your commitments to each other.", 35 words; AI in the run from H2-P6 too, 0.31), and everything from H3-P4's last sentence to the section's end (250 words). The run H3-P4 to H3-P6 (round e's three paragraphs, the same text as 348g's S16v11aa-H3-P4-P6, 0.69) was not run again. Five of the seven paragraphs from H3-P2 to H3-P7 open on a question, which is what v16 changes (`../make_v16.py`).

