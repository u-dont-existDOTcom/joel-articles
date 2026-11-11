# The humanize pass resumes: Pangram checks of the guide as it stands (2026-11-11)

His rule of 2026-11-08 17:22 UTC: humanize only after the guide makes sense, so a later sense fix doesn't force
re-humanizing. With round 33 in, the sense pass is done (CURRENT-STATE.md, turn 33), so each section of the guide as it
stands goes to Pangram's web app on his account, to find what reads AI or Low now, before the teaching round he said
he'd do once the guide makes sense (gate bad-trips-2026-11-07c).

## The batch, ready to run (h42a)

- `pass/build_units.py`: the guide after round 33 in 50 units, each a section or a run of one (at most about six
  paragraphs and at least 150 words: his rule for the web app, "a section check of about 5-6 paragraphs in the GUI is
  fine"), as the lane's earlier section checks typed them (`pass/UNITS.json`, `pass/units/*.txt`). 12,197 words, about
  122 of his credits.
- `pass/PREDICTIONS-h42a.json`: a call, a chance and the tells for each unit, quoted from its text, by fresh readers
  (`pass/PREDICT-BRIEF.txt`, `pass/PREDICT-BRIEF-gaps.txt`; 43 AI, 7 Human). Every quote is checked against its unit.
- `pass/write_predictions.py`: puts them in `../pangram-ledger.jsonl` (`--unchanged`, the text as it stands), only right
  before the checks run; it stops if a unit's text changed since `build_units.py`.
- `pass/ITEMS.py`: the batch in the page helpers' form.

To run: `python3 articles/bad-trips/humanize/h42-20261111/pass/write_predictions.py`; in Pangram's dashboard tab, paste
`tools/humanization/pangram_page_helpers.js`, then `__run('h42a', ITEMS)` with `ITEMS.py`'s output; when its log ends,
`__readC(ITEMS, 8)`, saved as `pass/RESULTS-h42a.json` and recorded with `pangram_ledger.py results`. Then a RESULTS.md
with each unit's link and every window's confidence (his: always the links; Medium windows shown too, since he fixes
those himself).

## Where it stopped (2026-11-11, turn 33)

The desktop app's browser pane was open on Pangram's dashboard but signed out, with the page asking to tick "Verify you
are human", which I never tick (AGENTS.md, gate E356). The lane's other route, a tab in his Chrome through Claude in
Chrome, was refused by the session's permission check when I asked to open one. So the batch waits on him: either he
signs in to Pangram in the browser pane and ticks the box, or he allows the Chrome route.
