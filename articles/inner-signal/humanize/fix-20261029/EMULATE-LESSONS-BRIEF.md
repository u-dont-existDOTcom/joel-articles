# The Emulate lessons study: the brief given to the study agent (2026-10-29 18:59 UTC)

Why: Joel, 2026-10-29 18:55 UTC: "i wonder if we really understood all the lessons from emulate's fixes or if we can
learn enough from what we got that we wouldn't need it anymore"; 19:22 UTC: "not sure why you are asking before even
checking if you can learn the lessons" (E293). Output: `fix-20261029/emulate-lessons/PAIRS.json` and `LESSONS.md`.
A fresh session that finds no LESSONS.md runs it again from this brief (a general-purpose agent, files only: no web, no
network, no Emulate calls, no laptop, no commits; writes only into `fix-20261029/emulate-lessons/`; reads but never writes
`articles/inner-child-therapy/`, which has a write lock).

## What's already known (read first)
- `docs/EMULATE-FALLBACK.md` section 1 ("What Emulate does", "What Pangram catches", "Writing from the lessons alone") and
  sections 5 and 6.
- `HANDOFF-hypnosis-guide.md`: the "## Emulate" section and the observations after it.
- The writers' current brief: the BRIEF string in `fix-20261029/b482/make_targets.py` (its "What reads AI to Pangram
  4.1" and "What reads human" lists), and `docs/HUMANIZATION-TELL-INVENTORY.md`.

## The data
This lane's Emulate batches: `fix-20261018/b4*/`, `fix-2026102*/b4*/` and `fix-2026102*/*/` (for example
`fix-20261026/b480/` with README.md, BUNDLE.json, the sample folders cj/ ck/ cl/, CANDIDATES.json and recheck/); layouts
differ by batch (README.md, *-items.json, *-results.json, drafts.json, PREDICTIONS.md, TEXTS.json). Each holds the input
stretch that read AI, Emulate's samples, and Pangram's readings of them. The ledger: `pangram-ledger.jsonl`. His published
version (AI-written): `source/published-20260928.md`.

## The method
1. Pairs: an input sentence (or 2 to 3 adjacent ones) that read AI, beside Emulate's replacement in a sample that read
   Human, aligned by meaning; 40 or more from as many batches as the data allows; and the failures (samples or parts of
   them that still read AI, with their input).
2. Label each change in shape (list split into sentences; list shortened; colon or dash removed; summing-up or closing
   line dropped; definition turned into an action or instruction; abstract nouns turned into people doing things; "not X
   but Y" or parallel pair broken; sentence lengths made uneven; a long sentence split; short sentences joined; a question
   added; first person or a personal aside added; hedge or doubt added; casual register added; a concrete particular
   added; order changed; subject changed; quip or metaphor removed; quip or metaphor added; "other: ...").
3. Tally over passes and failures; which changes the writers' brief has, lacks, or contradicts; two real examples
   (old -> new) of each missing one.
4. Emulate's meaning errors in the pairs (invented facts, dropped conditions, changed person or strength), kept apart.
5. Compare with our writers: batches 470/471 (`fix-20261022/b470`, `b471`) and 482 (`fix-20261029/b482/writers/`,
   CHOICES.json; batch 482's readings in place are `fix-20261029/b482/recheck/read/SPOTS.md`).

## Output
- `PAIRS.json`: [{"batch", "source_file", "input", "input_reading", "emulate", "emulate_reading", "labels", "meaning_error"}].
- `LESSONS.md`: the tallies, the missing lessons with examples, the meaning errors, the writer comparison, and at most 12
  bullet lines for the writers' brief (shape rules, never word lists), with how sure and what data is thin. Every quoted
  sentence exact, with the file it came from.
