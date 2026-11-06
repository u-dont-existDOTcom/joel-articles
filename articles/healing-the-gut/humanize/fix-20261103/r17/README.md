# r17: the windows left below High, fixed (2026-11-06)

Joel's message of 2026-11-06 20:13 UTC: "yeah if it's "low" we should fix it, medium you could try to fix but if it's too
difficult we can put that as a later todo when we want to learn more, and some things are not worth fixing, pangram has
some bugs, like "Why?" often reads as medium, etc. but my question is why you said you would work on that and then you
just stopped" (gates gut-2026-11-06a and b).

- `r17.md` is r16 (every answer of batches 9 to 11 in) with four window fixes, made by `build_r17.py` (`CHANGES.json`):
  the resistant starch item (Human Low in #170), the beta-glucans item, Phase 4's organ checks and the pregnancy line
  (Human Medium). Under E373 these are the model's words he kept, so the fixes are mine.
- `checks/`: each stretch with its receipt (`make_r17.py`), predicted first, checked in his account's web app:
  - leaky gut list: [#175](https://www.pangram.com/history/8c06b157-bd34-48c0-ba02-9b5c3d7b4b7c) Human, the two short
    items Medium; with beta-glucans' reason, [#178](https://www.pangram.com/history/a87802e1-d404-4a91-b2d5-ec9caebeb2e4)
    Human Written, one window, High (try 2);
  - Phase 4: [#176](https://www.pangram.com/history/83c128b0-42d2-4883-8aa1-efa9f8494306) Human Written, one window,
    High;
  - the stacks from the kits on: [#177](https://www.pangram.com/history/8ff3fe60-b777-4eb0-b49a-01db1fbe7d6a) Human
    Written, High but a one-word split at "Dr.".
- `b12/`: batch 12's marking page, the four fixes on approve cards (https://claude.ai/artifact/1QDJftScnaAjnqGS5b8xyM,
  cards in `b12/REVIEW-CARDS.md`).
- `substack/`: the whole of r17 as a paste payload for a temporary draft, B (`make_payload.py`: r12's editor HTML with
  r17's words, links and marks kept, every quote mark curled), and `EXPECTED-TEXT-B.txt`, the text his extension reads
  from it (no headings), which the whole-article prediction #183 is frozen on.

The three old windows gate E354 still named before the whole-article check had already read Human, High in later
checks; my rewrites of them, `../r18/`, read worse and were taken back (gut-2026-11-06c).
