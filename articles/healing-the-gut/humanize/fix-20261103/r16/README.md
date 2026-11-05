# r16: his batch-10 answers

Joel, 2026-11-05 23:00 UTC (`../../../experiments/t15-answers/`): batch-10's cards F10-1 to F10-3 approved, F10-4 and
F10-5 answered, and "awesome i'm glad you're understanding how to write for pangram finally, make sure that's in the repo
for all lanes".

`r16.md` is r15 with his two answers worded (`build_r16.py`, `CHANGES.json`):
- **F10-4, HRP:** "yes it was an old version of askrigor basically, we can tell them to re-check it with askrigor.com for
  an up-to-date verification (yes it will be public soon, don't need to mention it's not yet)". The report is now "this
  deep research report from an older version of AskRigor, my research tool, and re-check it with askrigor.com for an
  up-to-date verification". AskRigor is explained where it is first named (E369), and his re-check is joined to the
  same sentence (E368).
- **F10-5, the Gemini mode:** "i just tested it with free gemini and it worked ... i'd just tell people to use the highest
  thinking level they can for best answers as usual." The intro no longer names a mode, the Gem section drops "Pro", and
  his test and advice follow what the Gem is for: "I tested it on free Gemini and it works, but use the highest thinking
  level you can for the best answers."

F10-1 to F10-3 (the dose, the caution, Phase 2's opening) stay as r15 has them.

## Checks

Receipts pass for the three changed stretches (`checks/make_r16.py`): the intro (blocks 1-3), the HRP line with the
carnivore paragraph before it (16-17), and the Gem section with the note under it (35-36). Predictions are frozen:
r16-A #172 (Human, 0.75), r16-HRP #173 (Human, 0.65), r16-F #174 (Human, 0.70).

The web-app checks didn't run. At 23:15 UTC Pangram had signed Joel's account out in the desktop app's browser and
asked for its "Verify you are human" box, which a session never ticks. They run once he signs in again; the texts are
`checks/CHECK-r16-*.txt`.

## Batch 11

`b11/build_review.py` writes the two cards (F11-1 the report, F11-2 the Gemini mode). Its check refuses a card for a
stretch Pangram read without the card's own check ("you didn't check if your changes passed.. they didn't. don't waste
my time"), so the page goes out with the checks.

## How to write for Pangram, for every lane

His "make sure that's in the repo for all lanes": `AGENTS.md`'s workflow and a new `SKILL.md` section, "Writing for
Pangram: his fixes come first", carry E368 and E369 with the before-and-after checks, in pull request 308. This session's
permission check refuses a merge into main without review, so Joel merges it.
