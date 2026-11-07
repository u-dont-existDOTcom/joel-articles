# Romance, fixing the live post's AI spans (from 2026-11-07)

- `live-check/`: his extension's result on the live post (`META.json`, `AI-WINDOWS.json`: the 41 AI windows, 21 spots, by
  code-point offset into the text it read; `LOW-WINDOWS.json`: its 54 Human Low windows, with the fix that has rechecked
  each where there is one).
- `r01/` to `r19/`: check texts (`checks/texts.py`), making-sense receipts (`make_receipts.py`), predictions
  (`predict_rNN.py`, from r03) and results (`RESULTS-*.json`), one key per check (`r01-s1` is spot S1's first try; a
  letter after the number, as in `r03-s2b`, tells apart two tries at one spot). Predictions and results are in
  `../pangram-ledger.jsonl`. `r03/checks/CHECK-r03-s2c.txt` was written but never checked: try 3 read first, and try 4
  went another way.
- `r03/panel-s2/`, `r04/panel-s7/`, `r04/panel-s10/`, `r04/panel-s11/`, `r05/panel-s17/`, `r05/panel-s21/`: the tell
  panels (two fresh readers each, `tools/humanization/tell_panel.py`) run after a spot read AI twice (E346); `r14/panel-sit34/` too.
- `r06/`: four sections checked whole with the best tries in them, and the post's last part (`CHECK-r06-tail.txt`, the
  2,871 words his extension never read), as it stands. `r07/`: S21's pair check, the narrowing the section gate asks for.
  `r08/`: S22's first try inside "After leaving". `r09/`: the first Low-window section, "Holding up a leaky dam".
- `r10/`: the narrowing the section gate asks for (E343), the dam's two changed paragraphs and S22's three, each by
  itself. `r11/`: the dam section's second try, S22's middle paragraph (never sent: 47 words, and the web app takes 50
  at least), and the first tries at "Situationships", "The window of clarity" and "My flaws". `r12/`: S22's section
  a second time, the dam after a fix (his answer 28a), the narrowing of "Situationships" and "The window of clarity",
  and the first tries at "Peeking thru the window" and "Things get tricky fast".
- `r13/`: S22's section and the dam after one more fix each (28a), "The window of clarity" a second time, paragraph 34
  of "Situationships" as the live post has it, and the first tries at "Anti-PTSD Can Be Just As Dangerous As PTSD",
  "Slow & steady may win the race" and "Disconnect to connect". Its `make_receipts.py` takes the rows of the sentences
  it shares with r11 and r12 from their receipt makers.
- `r14/`: the tell panel on "Situationships" paragraph 34 (`r14/panel-sit34/`) and its next try, the narrowing of
  "Slow & steady" and "Disconnect to connect", and the first tries at "Muses & Directors", "The Queen of Orgasms",
  "Jealousy on trial" and "Labels Are Descriptive, Not Prescriptive". `r15/`: the second tries at "Situationships",
  "Slow & steady" and "Disconnect to connect", the narrowing of "Jealousy on trial", and the first tries at "It always
  goes deeper" and "Beware idealization in either direction" with S4, S5 and S8 in. Results files abridge long Human
  High windows, marked "(through)"; their full words are the check texts.
- `r16/`: every try linted first (`tools/humanization/tells_lint.py`, gate bad-trips-2026-11-07h). Paragraph 34 of
  "Situationships" with its fun line left a little unbalanced, "Beware idealization" 147 with 148, the second tries at
  "Jealousy on trial" and "It always goes deeper", "Slow & steady" after a fix, and the first tries at "Romance
  Shouldn't Be Adjudicated" and "Fantasy" with S15 and S16 in.
- `r17/`: every try linted first. "Situationships" after its fix (his answer 28a), the first whole checks of "Some babies
  grow up faster", "Different levels in different domains can be complementary" and "What are you actually choosing
  together?" with S11, S12, S13 and S20 in, and the first tries at "Why all of this sounds artificial" and
  "Gaslighting in the dark" from the post's last part.
- `r18/`: the second try at "What are you actually choosing together?", and the first whole checks of "The conversation
  about flaws" (S7 in), "From flow to nitty gritty" (S9 in), "Which marriage vows are honest?" (S21 in) and "What I
  gained from loss".
- `r19/`: "From flow to nitty gritty" narrowed to 201 (its list re-shaped, then cut to two items), the section's last
  try, and one check after the fix.
- The marking page for S2 and S17 is in `../../review/teach-20261107/`.

The spots are numbered S1 to S21 in the order they appear in the post, and S22 is the one the post's last part turned up (#47) (`../../CURRENT-STATE.md` lists which are done).
