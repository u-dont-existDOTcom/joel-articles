# The live post's whole-article check (2026-11-04, 22:17 UTC)

Joel ran his Pangram extension on the published post (r12, live since 21:35 UTC) and sent the result page at 22:35 UTC (`../../../../experiments/t12-answers/`).

**Result: [Mostly Human Written, 93.0% human](https://www.pangram.com/feed/e3a65841-a626-4b34-aad7-62b9dfa48ada)** (7.0% AI, Pangram 4.1, 3,642 words, "AI-generated content appears in scattered patches").

- Windows: Human High 11, Human Medium 11, Human Low 7, AI Low 14, AI Medium 2, AI High 2. `CONFIDENCE.md` lists every window below High with its place and whose words.
- The page was read in the desktop app's browser pane with `tools/humanization/pangram_feed_read.js` (compact mode): `META.json`, `WINDOWS.txt`. `build_result.py` makes `RESULT.json` from them.
- The checked text is `CHECKED-TEXT.txt`: `../checks/texts/r12-article.txt` without its 11 headings and the paid-subscriber line, with the post's one line break inside the Parasites item. Its SHA-256 is the page's own (e93ad829...), so every window is cut from the text the extension read.
- Ledger #142 called Human at 0.5: a **miss**, explained as context.

**Where the AI windows are**
- The fuels stretch: P20's three glutamine-mechanism sentences (AI Low), with Human Low on P19's last two sentences and P20's first.
- Phase 2's opening, Ruscio and Pimentel (AI High on "Mark Pimentel ... Low Fermentation Eating (Pimentel)").
- Phase 3's Elemental Diet sentence and Phase 4's two tests (AI Low).
- Phase 5's first four paragraphs, his own version (AI High on Bulsiewicz's 30+ plants; his "Does anyone count their plants?" reads AI Medium).

**What changed since r10, which read 100% Human**
- Every AI window except the fuels stretch's is on words that haven't changed since r10, whose check read them Human (High, or Medium where Pangram cut at "Dr." and "L.").
- Every quote mark and apostrophe in the post is straight now: 116 of them. r10's checked text had them curled, because a paste into Substack curls them. The r11 and r12 updates put the text in through the editor's schema, which kept them straight. The gate expected Substack to show them curled (`docs/HUMANIZATION-GATE.md`, E337 (gut)).
- Batch 8's 22 approved changes, some of them in Phases 3 and 4, right beside the windows.

**Next: telling the two apart** (`../substack/`)
- A temporary draft has the live post's words with all 116 marks curled, nothing else changed. Its text, straightened, is this check's text exactly.
- The prediction is frozen as #143: AI at 0.40.
- If it reads like r10, the marks did it, and the fix is to curl the live post's marks (his OK first, no email). If it reads like this check, the windows get fixed paragraph by paragraph, like the fuels stretch.
