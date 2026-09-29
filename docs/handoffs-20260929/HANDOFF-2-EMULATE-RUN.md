# Handoff 2: the Emulate run (GPT collects the data, Claude learns from it)

Written by Claude on 2026-09-29.

## What it's for

- Humanize Joel's community, hypnosis and neuro de-armoring articles with Emulate (https://www.tryemulate.ai). Hearthwork is optional.
- Collect before-and-after data so Claude can learn what Emulate does that beats Pangram. Joel says it isn't just paraphrasing.

## Where it lives

The folder is `articles/inner-child-therapy/experiments/emulate-20260929/` in `joel-articles`.
- **Instructions:** `GPT-OVERNIGHT-DIRECTIVE.md` is the full plan. `GPT-RESUME-CLOUD-BROWSER.md` is how to finish it.
- **Inputs:** `inputs/MANIFEST.md` lists the learning sets:
  - A: 27 of Claude's AI drafts that Joel fixed by hand, each with his fix as a reference;
  - B: 24 of Claude's drafts of one section;
  - C: two human controls;
  - `E_holdout/`: reserved for Claude's transfer test and never sent anywhere.

  Joel's articles are in `inputs/articles/` and listed in `ARTICLES.md`.
- **GPT's work so far:** on branch `gpt/emulate-overnight-20260929`. Read `MORNING-NOTE.md`, `LEDGER.md` and `RESUME.md` there.

## Where it stands (2026-09-29, 03:00)

- **Done:**
  - 56 exact Emulate versions via the API (sets A, B and C, plus probes D1 and D2);
  - 26 Pangram baselines;
  - the charge test;
  - 99 output checks and 105 splice and edit checks, prepared but not submitted.
- **Not done:**
  - Pangram checks of any new output;
  - the splice experiments;
  - every article;
  - Pro's analysis.

  GPT used a browser on Joel's desktop, where a security check blocked pangram.com. The fix is ChatGPT's cloud browser with Joel signed in there.
- **Budgets:** Emulate has 52,803 words left. Pangram had 2,127 credits at last read. Joel says Pangram's API is too costly, so checks go through the dashboard.
- **Facts learned:**
  - The API returns one version per call, 5–9 seconds each, and every call is charged.
  - A website run gives two options for one charge. The Copy button only appears after "Keep this one", and the other option then disappears. But option A's text read straight off the page matched its Copy text exactly, so both options can be read from the page before choosing.

## Rules that decide the output

- **Joel's choosing rule** (in the directive): the version must pass in its section, then keep the facts, then stay closer to what the original meant, then have fewer linter hits, then GPT's judgment with its reason written down. Run once more only if no version so far passes and keeps the facts, and never a third time.
- **Articles:** only paragraphs Pangram flags get rewritten. In the neuro de-armoring article, every dose, compound and timing must come out exactly as it went in. Emulate's output never replaces Joel's own writing.

## Claude's part, once the data is in

- **Slop comparison:** why readers still hear AI in Emulate's output. Compare Emulate's version with Joel's fix of the same draft, using `SLOP-PREP.md` and `tells_lint.py`.
- **Lessons and the transfer test:** read the splice results and Pro's `MOVES.md` and `LESSONS.md`, then write the `E_holdout` paragraphs by hand from the lessons and check them on Pangram.
