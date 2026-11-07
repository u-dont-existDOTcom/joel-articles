# Romance, fixing the live post's AI spans (from 2026-11-07)

- `live-check/`: his extension's result on the live post (`META.json`, `AI-WINDOWS.json`: the 41 AI windows, 21 spots, by
  code-point offset into the text it read).
- `r01/`, `r02/`: check texts (`checks/texts.py`), making-sense receipts (`make_receipts.py`), and results
  (`RESULTS-*.json`), one key per spot (`r01-s1` is spot S1's first try). Predictions and results are in
  `../pangram-ledger.jsonl`.

The spots are numbered S1 to S21 in the order they appear in the post (`../../CURRENT-STATE.md` lists which are done).
