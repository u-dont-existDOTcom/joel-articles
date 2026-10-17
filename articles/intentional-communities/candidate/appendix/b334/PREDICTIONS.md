# Predictions and Pangram results: batch 334g (2026-10-17, the appendix v5 and v5x)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). The two entries that read AI in 331g, each in two shapes (`../make_v5.py`): Orlov with Rubin (o1 numbered inline, o2 split), the research paragraph alone (r1 numbered, r2 split); each whole appendix (v5: o1 and r1; v5x: o2 and r2). Built by `../apx_batch.py` (texts already screened in 331g left out). Marches review-r4 (two readings, a break in each); lint REVIEW. Predictions written before the run.

## Batch 334g

| text | mine | why | Pangram |
|---|---|---|---|
| APXv5-E18-19 | Human | Orlov's four things numbered inline (o1), the way Joel numbers his own four parts in section 4 | **Human** (Human Written, low, 76 words, AI likelihood 0.22), 05:49:28, [check](https://www.pangram.com/history/2aa98892-2708-426b-85e7-c30562bd1736) |
| APXv5-E25 | Human | the four things the report has, numbered (r1) | **AI** (AI Generated, low, 65 words, AI likelihood 0.79), 05:49:38, [check](https://www.pangram.com/history/59862e03-6d3d-4b25-a392-1676128ccc2c) |
| APXv5 | Human | o1 and r1; 331g's AI window was the research paragraph and the archive line before it | **Mixed** (AI Detected; windows: Human, High, 535; AI-Generated, High, 144, 679 words, AI likelihood 0.31), 05:49:49, [check](https://www.pangram.com/history/5738cee5-502a-4494-a897-2e8711b746fa) |
| APXv5x-E18-19 | Human | o2: "is uncomfortable reading", then the four things over two sentences, the second an exclamation | **Human** (Human Written, low, 76 words, AI likelihood 0.13), 05:50:00, [check](https://www.pangram.com/history/6ad94ff5-c9dc-46f0-ad4a-f2736351ff61) |
| APXv5x-E25 | Mixed | r2: "The evidence base is there, and the limits. So are the counterexamples, and ..." | **AI** (AI Generated, low, 69 words, AI likelihood 0.89), 05:50:12, [check](https://www.pangram.com/history/3c5909ec-8647-482a-996c-501f37f36d21) |
| APXv5x | Human | o2 and r2 | **Mixed** (AI Detected; windows: Human, High, 593; AI-Generated, High, 90, 683 words, AI likelihood 0.29), 05:50:23, [check](https://www.pangram.com/history/b5cc68db-50ea-42f9-9232-b8c9ff36d3f7) |

Results of 334g (Pangram's History, 2026-10-17 05:49:28 to 05:50:23 UTC; run with 335g): Orlov's entry reads Human with Rubin in both shapes (o1, numbered inline, 0.22; o2, split, 0.13). The research paragraph reads AI alone in both (r1 0.79, r2 0.89), as it did in 331g (0.84) and published (in G, 0.98), and each whole appendix reads Mixed (0.31, 0.29), its AI window the research paragraph with the entries just before it. v6 keeps o1 (the closer to the published) and tries the research paragraph with the author in front (`../make_v6.py`, batch 336g).
