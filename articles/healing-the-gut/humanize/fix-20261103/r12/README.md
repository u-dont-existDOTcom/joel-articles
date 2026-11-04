# r12: his batch-8 answers (2026-11-04)

Joel approved all 22 batch-8 cards at 21:01 UTC, with no revisions and no comments (`../../../experiments/t11-answers/`). `make_r12.py` puts each one in word for word, and checks every approved paragraph against `r12.md` and `r12.html`.

## The web-app checks (Pangram 4.1, his GUI credits; `checks/`, ledger #119 to #140)

**Every changed paragraph, in 14 cuts** (`checks/RESULTS-webapp.json`):
- 12 read Human Written: g01, g02, g03, g04, g06, g08, g09, g10, g11, g12, g14 fully, and g05 as Mostly Human.
  - g05 had two Human Low windows.
  - g09 had one Human Low window, which r11's same cut has too.
- [g07](https://www.pangram.com/history/d11abfe4-40c5-485d-8f91-c715510881b3) read Mostly Human (9% AI). Its AI Low window is on Phase 1's opener, which is untouched; that sentence sits at the end of the cut.
- [g13](https://www.pangram.com/history/80b7a95e-3c65-4943-8824-31d1ee228a7b) read AI Detected (38%). Its AI Low windows are on the stacks lead-in and the Ruscio/GI Revive sentences, both untouched.

**Controls: r11's versions of the same cuts** (`checks/RESULTS-controls-webapp.json`):
- [g13's](https://www.pangram.com/history/63b206c5-ade8-46a0-a2ed-6c96ca97901c) reads worse, AI Detected 70%, so the cut is the cause.
- [g07's](https://www.pangram.com/history/43f270c9-e592-47d9-b8dd-4eb4265589d9) and [g05's](https://www.pangram.com/history/cecb0923-ea97-4314-aaab-b85aa60fb433) read Human with no Low windows, so batch 8 moved a window in those cuts.
- [g09's](https://www.pangram.com/history/64df5ee7-0031-4032-9340-1d44925ee7c3) has the same Low window.

**The natural sections with the changes in** (`checks/RESULTS-natural-webapp.json` and the controls file):
- [The stacks section](https://www.pangram.com/history/3513e03a-c513-4ab7-992b-ff9ead34a379): Human Written, High 215 and High 348, with a 1-word Medium.
- [The recipe intro](https://www.pangram.com/history/b05c8d18-5300-47ae-ba41-9c2997599db6): High 191.
- [Phase 1](https://www.pangram.com/history/e2b76d46-7dda-4141-b156-6aef920b7306): High 244.
- [The fuels stretch](https://www.pangram.com/history/2103ebd9-b274-4d8c-b32a-53819d5c740d) (Mitochondrial to the cancer caution): AI Detected 26%.
  - The AI windows are only on sentences batch 8 didn't change: the glutamine mechanism ("It doesn't have to go through...", "Inside the mitochondria...", "The α-KG goes into the citric acid cycle...") and the caution's last two sentences.
  - F8-11's own paragraph reads Human there.
  - r11's same cut (`texts/r11c-fuels.txt`, prediction #141) was not run, because the Claude in Chrome extension disconnected.
  - This stretch read Human in the whole article (r10). As a cut of its own it is a window we can see now (E354). Next, it gets fixed or goes to him.

## What's next

**The second update of his post.** r12 is his approved wording, and the clearer version stays (AGENTS.md; E291). `../live/UPDATE-PLAN-2.json` and `../live/update2.js` were pushed at 01e2b53c. The steps, in his post's editor in the built-in browser:
1. Set `window.__planGut` to `{url: raw/01e2b53c.../live/UPDATE-PLAN-2.json, sha256: 1cf3274b20d607fa4e139d2e5cb8e517724645873da37fa1e31912d2ef38a658}` and `window.__srcGut` to `raw/01e2b53c.../r12/r12.html`.
2. Run `update2.js`. It checks the editor against r11's blocks and replaces only the top-level nodes that changed, with the natives carried as the same nodes.
3. Run `dispatch.js`.
4. Continue, then "Update now", with "Send via email" unchecked.
5. Read the post back against the plan.

Then he can run the free whole-article check: his extension on the live post.
