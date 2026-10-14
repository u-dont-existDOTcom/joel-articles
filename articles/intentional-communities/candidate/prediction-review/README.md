# Prediction review, 2026-10-10

Joel, 13:53 UTC: "show me the examples you got wrong and what AI tells you noticed and why you marked it human when it was AI and vice versa." This folder holds the data behind the page `../community-prediction-misses.html` and the lesson in `docs/HUMANIZATION-GATE.md` ("What the prediction review of 2026-10-10 taught", rules PR #154).

- `parse_preds.py` reads every `PREDICTIONS-s*.md` table in the lane into `all-calls.csv`: one row per Pangram call, with my call, my reason and the result (1,591 calls).
- `join_texts.py`, `join2.py` attach each call's exact text from the batch files.
- `build_page.py` builds the page from the joined rows (`python3 build_page.py ROWS.json`).
- `pairs.md`, `pairs-key.json`, `pairs-with-diffs.md`: 108 pairs of near-identical texts where one passed and one didn't, with the words that differ.
- `blind-test-*`: 185 held-out texts in two halves (A, B), the answer key, a tells checklist (`blind-test-CHECKLIST-v1.md`) and the calls made with and without it. My calls were right 65%, Sonnet's plain calls 58%, Sonnet with the checklist 55%; always AI, 52%.

Section 11's calls, made after this review, are scored at the end of `../s11/PREDICTIONS-s11.md`: 171 of 233 right (73%), where always AI would have been 44%.
