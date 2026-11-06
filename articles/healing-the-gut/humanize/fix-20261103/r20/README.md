# r20: Phase 5's first two steps, try 2

r20 is r17 with two clarity fixes and a second try at Phase 5's first two steps, the three sentences his extension read
Human at Low confidence in the whole article (draft B, #183). Built by `build_r20.py`; the changes and their reasons are
in `CHANGES.json`.

- **The clarity fixes** come from the pre-publication compare read (`../r17/prepublish/FINDINGS.md`, F1.2 and F1.4):
  "once it's over" becomes "once the exposure or the stress is over", and "don't count on it" becomes "don't count on
  glutamine". Both read Human, High in their stretch (r19-D, #185).
- **Try 2** puts the reader's situation first in each step (the purge cleared out good bacteria too, so start re-seeding;
  the new bacteria feed on plant fiber, so bring plants back slowly), explains bacteriocins where it is first used and
  drops "titrate". His "Does anyone count their plants?" stays as he wrote it.

## What the checks showed

The cut of Phases 3 to 6, without headings (`checks/CHECK-r20-P36.txt` and its control `checks/CHECK-r17-P36.txt`):

| check | text | result |
|---|---|---|
| #187 | r17, unchanged (control) | AI Detected, 27.8% AI: [result](https://www.pangram.com/history/fd9ef004-3ba4-4386-bf49-fdb31df764ea) |
| #188 | r20 (try 2) | AI Detected, 28.3% AI: [result](https://www.pangram.com/history/072c7249-a3db-44f6-bd44-a2be6bca3a35) |

Both read Phase 5's steps AI (High and Medium), the control as much as the try, where the whole article reads them
Human (Low). So this cut can't judge the try (lesson gut-2026-11-06f), and try 2 goes to the whole article as draft C
(#189), beside try 3 as draft D (#190; `../r21/`). Every window, with its text, is in `checks/RESULTS-p36.json`.
