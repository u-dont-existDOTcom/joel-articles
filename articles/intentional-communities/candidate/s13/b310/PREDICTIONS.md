# Predictions and Pangram results: batch 310g (2026-10-16, screens of section 13 draft v30)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). v30 (`../make_v30.py`, `../v30-fixes.json`) is v29, which read 100% Human as a whole (309g), with the fixes of its meaning reviews (round r19, `../review-r19/DISPOSITIONS-r19.md`): a few words in ten paragraphs, each inside the sentence that was there, and H3-P1 back to v28's text. Screens (E175): lint and march passed (`../review-r19/MARCH-labels-5a.txt`, `-5b.txt`, `-6a.txt`, `-6b.txt`). Predictions written before the run.

## Batch 310g

| text | mine | why | Pangram |
|---|---|---|---|
| S13v30 | Human | v29 read Human (0.07); the fixes change a few words each, none of them back to a published sentence or a run of questions, and H3-P1's v28 text read Human inside the section in 309g's v29b | **Mixed** (AI Detected; windows: AI-Generated, High, 212; Human, High, 427; AI-Generated, High, 89; Human, High, 1596, 2324 words, AI likelihood 0.13), 22:53:06, [check](https://www.pangram.com/history/0af40fd9-46ba-4a93-8e73-2e2c8228fae4) |
| S13v30-H1 | Human | only H1-P4 changes: ", if you have any?" and "gets exhausted" | **Human** (Human Written, high, 362 words, AI likelihood 0.03), 22:53:09, [check](https://www.pangram.com/history/a2f13268-773e-4f3b-8b15-fbc22e2beea8) |
| S13v30-H2 | Human | "would be able to", "stay fully protected", the last sentence turned round before "Both of them!", "because" before the 1978 people | **Human** (Human Written, high, 366 words, AI likelihood 0.00), 22:53:19, [check](https://www.pangram.com/history/b314f808-4b1d-447d-9bf2-da7c143c4eb8) |
| S13v30-H3 | Human | v28's H3-P1 read Human in the subsection in 304g, and "Honestly, it's where I'd start for getting that order right!" is plain | **Human** (Human Written, high, 459 words, AI likelihood 0.00), 22:53:30, [check](https://www.pangram.com/history/8ec27e12-308f-4b52-beab-3c984b439f13) |
| S13v30-H5 | Human | read 0.00 in 308g; "There may be times", "during the separation", "it took them a long review", "they still need a final separation" are small and plain | **Human** (Human Written, high, 428 words, AI likelihood 0.00), 22:53:41, [check](https://www.pangram.com/history/4252aafe-449d-43bc-9674-74e432ed6b6b) |
| S13v30-J1 | Human | read Human in 307g to 309g | **Human** (Human Written, high, 538 words, AI likelihood 0.01), 22:53:52, [check](https://www.pangram.com/history/1c12207a-cd79-4c40-ae4f-a31927e82dde) |

Results of 310g (Pangram's History, 2026-10-16 UTC, 22:53:06 to 22:53:52): every changed subsection reads Human, high (0.00 to 0.03), and the whole section reads AI over 301 of its 2,324 words in two windows: 212 from the heading through H1-P3's first sentence, and 89 over H2-P4 whole (mapped with Pangram's word count). v29 had read 100% Human. Batch 311g puts each fix near the windows back alone to find which one moved them (`../b311/PREDICTIONS.md`). Predictions: 5 of 6.
