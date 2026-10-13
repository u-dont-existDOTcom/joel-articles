# Turn 50: Joel's answers 17 to 19 (2026-10-13 00:47 UTC)

- **17, Untangling P3:** his version, as he wrote it ("beacuse" spelled right, the one change). His check: Human, medium. Ours: 100% Human (139), AI likelihood 0.008.
- **18, the Four Pairs questions:** his loosened last line ("that last line just needed a little loosening"). His check: Human, low. Ours: 100% Human (88), 0.204.
- **19, the credit to Key:** "A", the guide's line with "Murray Bowen's". With P6, since it's one sentence: 100% Human (100), 0.268.
- **Sections:** Four Pairs That Commonly Hook the Child 100% Human (563), 0.119; Sometimes There Isn't a Clear Child Yet 100% Human (1,609), 0.172. Untangling the Belonging Bargains: Mostly Human (919), with one AI window of 57 words (0.572) across the end of P2 ("In its controlling form, that caretaking can drift…") and the start of P3. Each passes alone.
- **What his fixes teach (E170):** his P3 added why a child of good parents takes the bargains too, the reason a grounding had parked in turn 49, and said the guide's abstraction in plain words; his questions fix loosened one line of a tight parallel list. A fix round now starts from the reviews' parked notes and the guide's abstractions (`docs/HUMANIZATION-GATE.md`, `tools/humanization/reviewer/tickets.txt`).
- **Tool:** `pangram_gate.py` builds a section from texts the page already holds (`concat`), so a check of an h2 or h1 no longer means pasting it in full; each text is built when its turn comes.

Predictions: 5 of 6 (the h2 missed).
