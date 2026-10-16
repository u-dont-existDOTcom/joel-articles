# Predictions and Pangram results: batch 300g (2026-10-16, section 14's baseline)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). The published text of section 14, "Dissolution and Exit", as it stands in the article, after Joel's 18:22 UTC message ("continue into next section now"). Texts in `drafts.json`, records in `GATE.json`, both from `../make_baseline.py`; every prediction was written before the batch ran.

## Batch 300g

| text | mine | why | Pangram |
|---|---|---|---|
| S14-A | AI | the heading, P1 and P2 (97 words): P1 stages its point and lands it ("That is when the discussion needs to happen."); P2 is one packed question with nine duties in a row ("who keeps people housed and fed, gets medications and care ..., bridges food, housing, care, outside cash or benefits") | **AI** (AI Generated, low, 98 words, AI likelihood 0.87), 18:41:43, [check](https://www.pangram.com/history/f62dc40e-5529-41a6-a5aa-039c98d83714) |
| S14-B | AI | P3 and P4 (71 words): manual steps ("Design this like a living will. Preassign a bridge or successor for each critical function."), the weekday tell ("breakfast on Tuesday"), "continuity of basic life", and a list of three ("transition support, dignity, and a coherent story") | **AI** (AI Generated, low, 71 words, AI likelihood 1.00), 18:41:54, [check](https://www.pangram.com/history/d93610e8-5750-430c-9832-78c6db1e0563) |
| S14-C | AI | P5 (55 words): an aphorism up front ("institutions and relationships do not die at the same time") and a semicolon antithesis to close ("The communal economy had changed dramatically; the human bonds had not vanished.") | **AI** (AI Generated, low, 55 words, AI likelihood 0.34), 18:42:06, [check](https://www.pangram.com/history/3ff5e4e8-3778-4c22-9638-2292548d7d24) |
| S14-D | AI | P5, P6 and P7 (102 words): P5 as above and a closing aphorism ("some of what people learned to give one another may continue"); P6's father lines are personal but too short to carry the group | **AI** (AI Generated, medium, 103 words, AI likelihood 0.86), 18:42:15, [check](https://www.pangram.com/history/8ee8b636-b6a4-4bd1-aeb0-326411c7d41a) |
| S14v0 | AI | the whole published section (270 words): every paragraph above, and no break anywhere in it | **AI** (AI Generated, high, 272 words, AI likelihood 0.89), 18:42:27, [check](https://www.pangram.com/history/a2df8630-0e60-4f47-8487-b1f8c68ed1d7) |

Results of 300g (Pangram's History, 2026-10-16 UTC, 18:41:43 to 18:42:27): every group and the whole section read AI, as predicted (5 of 5). Emulate round a takes the section whole (`../emu-a/`).
