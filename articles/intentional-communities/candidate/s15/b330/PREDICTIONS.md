# Predictions and Pangram results: batch 330g (2026-10-17, section 15 v8)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). Section 15 v8 (`../make_v8.py`) is v6 with the fixes of trace round r7: H1-P4 with the published "often" back (g, "things often go through"; m, "a lot often goes through"), "either" back in H2-P1 and "may" back in H3-P2. Marches s16/review-r5 and r6 (two readings, a break in each); lint REVIEW. Run together with 328g. Predictions written before the run.

## Batch 330g

| text | mine | why | Pangram |
|---|---|---|---|
| S15v8-H1-P4g | AI | the published "things often go through ... alongside the formal systems" back; 327g read variant a, with the same "go through", AI | **AI** (AI Generated, low, 53 words, AI likelihood 0.94), 05:12:39, [check](https://www.pangram.com/history/450082a7-13ba-4d19-8e9b-e00aedad18a2) |
| S15v8g-H1 | Human | the subsection read Human with every H1-P4 so far | **Mixed** (AI Detected; windows: Human, High, 126; AI-Generated, High, 67; Human, Medium, 51, 244 words, AI likelihood 0.49), 05:12:50, [check](https://www.pangram.com/history/a810aa6f-b7f7-4093-8224-6f1b3233ae37) |
| S15v8-H2-P1+P2 | Human | "No, not that either!" keeps the break; P2 read Human in 326g | **Human** (Human Written, medium, 143 words, AI likelihood 0.17), 05:13:03, [check](https://www.pangram.com/history/99f95c47-9676-4ef3-84ad-29ee21aac860) |
| S15v8-H2 | Human | read Human in 326g and 327g | **Human** (Human Written, high, 388 words, AI likelihood 0.12), 05:13:15, [check](https://www.pangram.com/history/ca1fe39b-2f4c-4a7d-8183-a0bd4315d87f) |
| S15v8-H3-P2 | Human | variant l read Human 0.04 in 327g; "may" is one word | **Human** (Human Written, medium, 121 words, AI likelihood 0.03), 05:13:26, [check](https://www.pangram.com/history/f5e7c2ed-30a6-4589-a4a2-839de0565ece) |
| S15v8-H3 | Human | read Human in 327g | **Human** (Human Written, high, 761 words, AI likelihood 0.16), 05:13:39, [check](https://www.pangram.com/history/c5a378d6-d4c8-4288-8672-cab811d2821f) |
| S15v8g | Human | the whole section has read Human in every version since v3 | **Human** (Human Written, high, 1421 words, AI likelihood 0.11), 05:15:06, [check](https://www.pangram.com/history/cd49bab2-1c3a-4c8a-9a3d-32af484e938d) |
| S15v8-H1-P4m | Human | "a lot often goes through" keeps more of Emulate's "so much" | **AI** (AI Generated, low, 54 words, AI likelihood 0.91), 05:15:38, [check](https://www.pangram.com/history/1d5121dc-9bfc-4470-909e-f09e8ef02046) |
| S15v8m-H1 | Human | as g | **Mixed** (AI Detected; windows: Human, High, 126; AI-Generated, High, 68; Human, Medium, 51, 245 words, AI likelihood 0.44), 05:15:48, [check](https://www.pangram.com/history/e7e4b776-73ab-4f15-ba7e-fc126be80400) |
| S15v8m | Human | as g | **Human** (Human Written, high, 1422 words, AI likelihood 0.11), 05:15:59, [check](https://www.pangram.com/history/b76cf06e-847b-46a3-b95b-c0495861f7d0) |

Results of 330g (Pangram's History, 2026-10-17 05:12:39 to 05:15:59 UTC; run with 328g): 7 of 10 predictions right. H1-P4 reads AI alone in both shapes with the published "often" back (g, "things often go through", 0.94; m, "a lot often goes through", 0.91), and the H1 subsection reads Mixed with either (0.49, 0.44: the end of H1-P3 and all of H1-P4 AI, 67 and 68 words). Everything else reads Human: H2-P1 with "either" back, with H2-P2 (0.17) and in H2 (0.12); H3-P2 with "may" back, alone (0.03) and in H3 (0.16); the whole section with g and with m (0.11, high, both). The misses: m alone and both H1 subsections, called Human. Round d's c ("so much is taken care of by") was the only H1-P4 shape that read Human alone (0.54), and it changed the meaning; the fixed meaning goes back to Emulate (round e, `../emu-e/`). H3-P2 changes again in v9 (round r8's trace: "any" and "long-term" back), so it goes to Pangram again.
