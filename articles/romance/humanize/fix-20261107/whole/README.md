# The fixed version of the romance post, for its whole-article check (2026-11-07)

The live post ("Romance Advice I Wish My Parents Taught Me", updated Aug 27, 2026) with every section's and spot's best
tested text in place: 40 changes, 66 live paragraphs (`CHANGE-MAP.md`). S2 and S17 (on the marking page), the three
stretches that share S2's pattern ("Beware idealization" 148, "Romance Shouldn't Be Adjudicated" 285 to 287, "Jealousy
on trial" 367 to 369) and "Two Pillars" 332 (owner lock) are as the live post has them.

- `LIVE-INDEX.txt`: the post page's paragraph list (p, li, h2 to h4, in order; the h1 headings aren't in it), each with
  its tag and the first 12 hex characters of the SHA-256 of its text, whitespace collapsed. A list item shows twice in
  that list (its li and the p inside it).
- `LIVE-CHANGED.json`: the live words of the 66 changed paragraphs, copied from the page and checked against those
  fingerprints.
- `assemble.py`: aligns each check text with its live run by the fingerprints; `PLAN.json` holds each check's run and
  operations. `build.py` writes `CHANGE-MAP.json`, `CHANGE-MAP.md`, `REPLACEMENTS.json` (live paragraph to its new
  paragraphs, for the draft) and the reads' inputs, `ORIGINAL-CHANGED.md` and `REWRITE-CHANGED.md`.
- `compare/`: the compare read of every changed paragraph beside the live one (`compare_read.py`, read by the lead
  session, gate E294): 7 findings, all severity 1, each kept with its reason (`compare/DISPOSITIONS.json`,
  `compare/READ-RECORD.json`).
- `sense/`: the word-for-sense read of the changed paragraphs (`sense_read.py`, one fresh reader, three planted errors):
  every planted error found, no other finding (`sense/SCORE.json`); the non-word net found only his words and terms
  (`sense/NONWORDS.txt`).
- `build_draft.js`: builds one part of the fixed post in a new draft's editor tab, from the post API and this folder's
  files at a commit, checks every paragraph against `LIVE-INDEX.txt`, and pastes it (never publishes). Pictures, videos,
  embeds and buttons are left out of the drafts: Pangram's check reads paragraphs and list items only. A changed
  paragraph's inline formatting (links, bold) isn't carried into the draft; the live update will merge the new words into
  the editor HTML (`tools/humanization/substack_merge.py`).
- `DRAFTS.json`: the two temporary drafts made with it (draft A to "Primal attraction", draft B from there), each one's
  checked text's SHA-256, and the rendered check of each secret link (both matched). The links themselves stay out of Git.
  The whole-article check waits until every window a smaller check read AI reads Human in a later smaller check (gate
  gut-2026-11-07a); then the drafts get the text pasted again.
- `EMBEDS.md`: the live post's pictures, videos and embeds, from the post itself.
- `compare-r20/` and `sense-r20/`: the same two reads for the changes `r20/` added (304 to 306, 312): no compare finding;
  both planted errors found and nothing else.
