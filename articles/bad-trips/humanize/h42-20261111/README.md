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

## How it ran (2026-11-11, turn 34)

Pangram reachable once he signed in to the desktop app's browser pane ("i logged in on your browser", 21:04 UTC; I
ticked nothing). `write_predictions.py` put the 50 predictions in the ledger (#383 to #432) before the first click; the
page helpers ran the batch from 21:06 to 21:15 UTC. The run stopped at h42-47, "Bring in mental-health support when:",
37 words: the web app's Check for AI button stays off under 50 words, so its prediction is voided (it gets checked with a
neighbour after the humanize edits) and h42-48 to h42-50 ran after it. 49 results, read from the History by
`__readI` (`pass/RESULTS-h42a-idx-1.json`, `-idx-2.json`, merged as `pass/RESULTS-h42a-idx.json`), turned into the
ledger's form with each window's words by `pass/ingest.py` (all 49 windows' first characters matched), recorded with
`pangram_ledger.py results`, and laid out by `pass/results_md.py` as `RESULTS.md`.

**What it found:** 16 read Human Written (8 Human High in every window), one Mostly Human (Dealing With Shadow Thoughts,
8%), 32 with AI windows (15 of them 100%). His own sections read Human where they're his; the AI is the medical part and most of the
remedies, the tripsitting middle (Grounding Menu 1, Get One Human Anchor, For the Person Helping, No Rash Actions, Euphoric), the shadow
part's middle (Sorrow, Hand on Heart, Demons, Abuse Memories, Spiritual ≠) and After the Storm. Nine predictions missed,
all the same way: a lone tell called AI in a section of his that read Human (explained in the ledger as "his voice
outweighed a lone tell").
