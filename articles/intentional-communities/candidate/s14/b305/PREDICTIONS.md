# Predictions and Pangram results: batch 305g (2026-10-16, section 14 draft v4 as drafts)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Section 14 v4 (`../make_v4.py`): v3 with ending W2, which read Human in every group as a screen (303g), the published "childcare and schooling" and "bridging ... food, housing and care" back in P2, and "bridge or successor" in P3. Every record is complete (`GATE.json`; `../review-r5/DISPOSITIONS-r5.md`). If every group and the section read Human, v4 is installed. Every prediction was written before the batch ran.

## Batch 305g

| text | mine | why | Pangram |
|---|---|---|---|
| S14v4-1P12 | Human | read Human (high) twice with other wordings of the two P2 lines; the published "bridging ... food, housing and care" is back in the run of "Who takes responsibility" questions | **Human** (Human Written, high, 163 words, AI likelihood 0.02), 19:43:47, [check](https://www.pangram.com/history/a153cd3c-f2d2-475c-b880-467f028e496f) |
| S14v4-P2 | Human | as above; the risk is the published list back inside the question run | **Mixed** (AI Detected; windows: Human, Medium, 89; AI-Generated, Medium, 33, 122 words, AI likelihood 0.46), 19:43:58, [check](https://www.pangram.com/history/dedaa1cc-aaec-4b8b-978a-9dd49dd848c0) |
| S14v4-P34 | Human | read Human (low) in 301g; only "bridge or successor" changed | **Human** (Human Written, low, 87 words, AI likelihood 0.07), 19:44:07, [check](https://www.pangram.com/history/63225774-9c97-4e0b-8b75-1333391499c4) |
| S14v4-P5 | Human | the same text read Human (low) in 303g | **Human** (Human Written, low, 58 words, AI likelihood 0.17), 19:44:21, [check](https://www.pangram.com/history/ba2a626b-afb8-4f85-94d9-1ed616bf5697) |
| S14v4-P67 | Human | the same text read Human (low) in 303g | **Human** (Human Written, low, 68 words, AI likelihood 0.19), 19:44:32, [check](https://www.pangram.com/history/16f9c36a-df3d-474d-9c73-c5f26eaf044d) |
| S14v4-P567 | Human | the same text read Human (medium) in 303g | **Human** (Human Written, medium, 126 words, AI likelihood 0.27), 19:44:44, [check](https://www.pangram.com/history/b8fc014c-0863-4acb-817a-e6b49995b895) |
| S14v4 | Human | every whole section read Human (high) in 301g and 303g | **Human** (Human Written, high, 376 words, AI likelihood 0.30), 19:44:56, [check](https://www.pangram.com/history/e3d9d78f-650b-4b71-b5fa-9bb004f5f8d7) |

Results of 305g (Pangram's History, 2026-10-16 UTC, 19:43:47 to 19:44:56): every group reads Human and so does the whole section (high, 0.30), except P2 alone: Human over its first 89 words, AI (medium) over its last 33, the six-item "Who takes responsibility for transportation, for the records, ..." question and "That's a lot of loose ends!". Those two sentences are v3's; v4's two fixes made P2 11 words shorter, and the shorter paragraph split into two windows, the second one those two sentences alone. Predictions: 6 of 7.

## Batch 305g-x (screens of a P2 variant, written before the run)

v4's P2 read AI over its last 33 words when alone (the six-item "for ..." question and "That's a lot of loose ends!"), though Human inside the heading group and the section. v3's P2, 11 words longer, read Human alone (303g, medium, 0.01) with the same last two sentences. v4x (`../v4x.md`) puts the childcare question back to v3's length with the published meaning ("Who keeps childcare going, and makes sure the kids' schooling carries on?"), to see whether the shorter paragraph split into a window that leaves those two sentences alone.

| text | mine | why | Pangram |
|---|---|---|---|
| S14v4x-P2 | Human | 125 words, close to v3's 133, which read as one Human window | **Human** (Human Written, medium, 128 words, AI likelihood 0.11), 19:47:33, [check](https://www.pangram.com/history/5f719826-acd2-433b-a098-c9de3bcda276) |
| S14v4x-1P12 | Human | as 305g's heading group | **Human** (Human Written, high, 169 words, AI likelihood 0.00), 19:47:46, [check](https://www.pangram.com/history/609c1f5b-2716-4d7d-b268-ac9232072546) |

Results of 305g-x (19:47:33 to 19:47:46): P2 alone reads Human (medium, 0.11) as one window at 125 words, and the heading group Human (high, 0.005). So a paragraph can read AI alone because a fix shortened it, not because of what the fix said: the window split left the list question by itself. Predictions: 2 of 2. v5 (`../make_v5.py`) takes this wording.
