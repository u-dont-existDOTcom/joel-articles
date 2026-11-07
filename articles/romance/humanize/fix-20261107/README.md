# Romance, fixing the live post's AI spans (from 2026-11-07)

- `live-check/`: his extension's result on the live post (`META.json`, `AI-WINDOWS.json`: the 41 AI windows, 21 spots, by
  code-point offset into the text it read; `LOW-WINDOWS.json`: its 54 Human Low windows, with the fix that has rechecked
  each where there is one).
- `r01/` to `r07/`: check texts (`checks/texts.py`), making-sense receipts (`make_receipts.py`), predictions
  (`predict_r0N.py`, from r03) and results (`RESULTS-*.json`), one key per check (`r01-s1` is spot S1's first try; a
  letter after the number, as in `r03-s2b`, tells apart two tries at one spot). Predictions and results are in
  `../pangram-ledger.jsonl`. `r03/checks/CHECK-r03-s2c.txt` was written but never checked: try 3 read first, and try 4
  went another way.
- `r03/panel-s2/`, `r04/panel-s7/`, `r04/panel-s10/`, `r04/panel-s11/`, `r05/panel-s17/`, `r05/panel-s21/`: the tell
  panels (two fresh readers each, `tools/humanization/tell_panel.py`) run after a spot read AI twice (E346).
- `r06/`: four sections checked whole with the best tries in them, and the post's last part (`CHECK-r06-tail.txt`, the
  2,871 words his extension never read), as it stands. `r07/`: S21's pair check, the narrowing the section gate asks for.

The spots are numbered S1 to S21 in the order they appear in the post (`../../CURRENT-STATE.md` lists which are done).
