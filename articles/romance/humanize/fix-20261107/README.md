# Romance, fixing the live post's AI spans (from 2026-11-07)

- `live-check/`: his extension's result on the live post (`META.json`, `AI-WINDOWS.json`: the 41 AI windows, 21 spots, by
  code-point offset into the text it read; `LOW-WINDOWS.json`: its 54 Human Low windows, with the fix that has rechecked
  each where there is one).
- `r01/` to `r12/`: check texts (`checks/texts.py`), making-sense receipts (`make_receipts.py`), predictions
  (`predict_rNN.py`, from r03) and results (`RESULTS-*.json`), one key per check (`r01-s1` is spot S1's first try; a
  letter after the number, as in `r03-s2b`, tells apart two tries at one spot). Predictions and results are in
  `../pangram-ledger.jsonl`. `r03/checks/CHECK-r03-s2c.txt` was written but never checked: try 3 read first, and try 4
  went another way.
- `r03/panel-s2/`, `r04/panel-s7/`, `r04/panel-s10/`, `r04/panel-s11/`, `r05/panel-s17/`, `r05/panel-s21/`: the tell
  panels (two fresh readers each, `tools/humanization/tell_panel.py`) run after a spot read AI twice (E346).
- `r06/`: four sections checked whole with the best tries in them, and the post's last part (`CHECK-r06-tail.txt`, the
  2,871 words his extension never read), as it stands. `r07/`: S21's pair check, the narrowing the section gate asks for.
  `r08/`: S22's first try inside "After leaving". `r09/`: the first Low-window section, "Holding up a leaky dam".
- `r10/`: the narrowing the section gate asks for (E343), the dam's two changed paragraphs and S22's three, each by
  itself. `r11/`: the dam section's second try, S22's middle paragraph (never sent: 47 words, and the web app takes 50
  at least), and the first tries at "Situationships", "The window of clarity" and "My flaws". `r12/`: S22's section
  a second time, the dam after a fix (his answer 28a), the narrowing of "Situationships" and "The window of clarity",
  and the first tries at "Peeking thru the window" and "Things get tricky fast".
- The marking page for S2 and S17 is in `../../review/teach-20261107/`.

The spots are numbered S1 to S21 in the order they appear in the post, and S22 is the one the post's last part turned up (#47) (`../../CURRENT-STATE.md` lists which are done).
