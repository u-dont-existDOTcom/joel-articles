# Predictions and Pangram results: batch 292g (2026-10-15, Joel's 31 a)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Section 13 v12 paragraphs whose records came back clean in gate round r9 (`s13/review-r9/`), with the headings of the first, third and fifth subsections over their first paragraphs. Texts in `drafts.json`, records in `GATE.json` (built by `make_batch.py`). Predictions written before the call; results from the History, each with its check link (E175).

## Batch 292g

| text | mine | why | Pangram |
|---|---|---|---|
| S13v12-1hP1P2 | Human | the section's heading, the "cheesy but true" paragraph, and round e's conflict paragraph ("Don't even think about ...", "But really, truly dealt with it.", "Until then, what's it worth?"); the risk is its long sentence of four steps | **Human** (medium; 170 words), 16:53:55, [check](https://www.pangram.com/history/7a40bc0b-daf7-4c75-9f07-fdaa3ed956c3) |
| S13v12-1P1P2 | Human | the same without the heading | **Human** (medium; 162 words), 16:54:03, [check](https://www.pangram.com/history/c54b25d8-1c62-479d-bdbd-d775a1de6dbb) |
| S13v12-1P2 | Human | round e's paragraph alone | **AI** (AI-Generated, medium; 115 words, the whole text), 16:54:12, [check](https://www.pangram.com/history/200f9c1d-79c6-4f49-8223-503258cec054) |
| S13v12-3P1 | Human | Emulate's paragraph from round b, with a question and a reaction in front | **Human** (low; 66 words), 16:54:26, [check](https://www.pangram.com/history/8c9e35a5-e5ca-4d73-a590-2d9bdd4c47d3) |
| S13v12-3hP1 | Human | the same with its heading | **AI** (AI-Generated, low; 71 words, the whole text), 16:54:35, [check](https://www.pangram.com/history/9ac75023-1174-491a-a638-722dcbada762) |
| S13v12-4P7 | Human | Emulate's roles paragraph from round b, with the van keys in the writer's voice | **Human** (low; 95 words), 16:54:45, [check](https://www.pangram.com/history/3b1a27d4-d0c6-4a49-b4db-b83b1981750d) |
| S13v12-5P1 | AI | its first sentence is the published one, and the second carries the published three grounds in one sentence; "Yes, really." and "that's cool!" may not be enough | **Human** (low; 73 words), 16:54:56, [check](https://www.pangram.com/history/3f7add0b-a64b-495a-84ca-d2b8346c472e) |
| S13v12-5hP1 | AI | the same with its heading | **Human** (low; 78 words), 16:55:06, [check](https://www.pangram.com/history/6ec7073d-47e8-42aa-9d4e-08b935c9c2bd) |

Results of 292g (Pangram's History, 2026-10-15 UTC): six of eight read Human: the section's heading with its first two paragraphs, the same two paragraphs without it, the land-title paragraph alone, the roles paragraph, and the first removal paragraph alone and with its heading. Two read AI: the conflict paragraph alone (H1-P2, medium confidence, its second AI reading alone; with the paragraph before it, it reads Human, but the rule is alone), and the land-title paragraph under its heading (low confidence; alone it reads Human, low). Score: 4 of 8 (right: S13v12-1hP1P2, S13v12-1P1P2, S13v12-3P1, S13v12-4P7). Every text checked is the one in `drafts.json` (same SHA-256).
