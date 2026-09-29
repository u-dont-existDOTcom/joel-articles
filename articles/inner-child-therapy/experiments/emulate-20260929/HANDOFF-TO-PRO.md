# Partial checkpoint for Pro — data collection incomplete

The owner requested Pro for Part5. No Pro session/model has been verified or given this packet. Parts1–4 are incomplete because the browser could not verify its admin-enforced policy; no Pangram workaround was attempted. This is a prepared handoff, not completed Pro analysis.

Canonical repository: u-dont-existDOTcom/joel-articles, branch gpt/emulate-overnight-20260929, path articles/inner-child-therapy/experiments/emulate-20260929/. Read live Universal and Joel Articles authority instructions before acting. The owner-supplied directive controls. All data remains experimental; do not promote it to article authority.

Read MORNING-NOTE.md, CURRENT-STATE.md, RUNTIME-GATES.json, RESUME.md and LEDGER.md first. Exact source/output/result data is in runs/emulate.jsonl, runs/pangram.jsonl, runs/align/, runs/lint-source/ and the three check queues. Prepared Part4 texts are unsubmitted; never treat them as measured signal. Historical Claude results have rough timestamps and their existing provenance must be retained. The website optionB is DOM-only diagnostic and is excluded from paid checks.

Only four historical output versions are measured Human, from two distinct inputs; only two are multi-paragraph. Fifty-six new exact outputs are ungraded. No article has been humanized, so article QUALITY verdicts cannot be delivered. Do not infer semantic preservation or detector pass from provider fields. Completed analysis should wait for the missing measurements; any early analysis must explicitly say partial and ungraded. Do not invent MOVES/LESSONS evidence.

The packet excludes E_holdout entirely. Do not read it from GitHub or elsewhere. No transfer test or unlabeled original prose. A afters are reference-only; C2 rewrite is data-only. Pro writes analysis only, no browser.

## Part 5. Analysis (Pro)

Read everything in `runs/`, plus `inputs/MANIFEST.md`, `ARTICLES.md`, Joel's reference texts in set A, and `tools/JOEL-FIXES-CATALOGUE-20260928.md`. Write these in `analysis/`:

1. **`PAIRS.md`**, one entry per pair:
   - the input, the output, and the Pangram result before and after, with the flagged spans;
   - the alignment, with each unit marked kept, reworded, split, merged, moved, cut or added;
   - one line on what changed beyond the words.

   For set A, put Joel's version beside them.
2. **`MOVES.md`**, what Emulate does, measured and not assumed. Name each move in plain words, then give:
   - how often it happens, out of how many pairs;
   - 2–3 exact examples, with pair id and before and after;
   - whether it also happens to the controls (C1, C2);
   - whether Joel makes the same move in his fixes (set A).

   Cover at least:
   - sentence count and length, and the order of sentences and points;
   - topic sentences, and summary or closing lines;
   - lists and groups of three, questions, and contrasts ("not X but Y");
   - hedges, asides and parentheses;
   - concrete detail: added, cut, or invented;
   - first and second person, and register;
   - punctuation (dashes, semicolons, colons);
   - paragraph breaks and headings;
   - how much of the input's meaning is kept.

   Separate the moves it makes everywhere, which are its style, from the moves the splice data ties to the verdict changing, which are the signal.

   End with a short section, labelled as your opinion: what still reads machine-made to you in Emulate's outputs, with examples.
3. **`SPLICES.md`**, what the splice experiments show:
   - whether the flip comes from particular sentences, from how many are changed, or only from the whole piece;
   - which kinds of units flip it;
   - which original sentences bring AI back when they're put back.

   Use the flagged spans.
4. **`FRAGILITY.md`**, the edit test turned into advice: which edits Emulate's output survives.
5. **`SLOP-PREP.md`,** groundwork for a question Claude will take on. Some readers say Emulate's output still sounds like AI, even when Pangram passes it. Don't judge that here; lay out the material:
   - Run `tools/tells_lint.py` on every Emulate output, on every set A "before", on every Joel "after" in set A, and on Claude's own passing paragraphs (the `tools/calibration/PASS_*.txt` files without "joel" in the name).
   - Put the four groups side by side in one table, with each linter rule's hits per 100 words.
   - List the 10 Emulate outputs that passed Pangram but have the most linter hits, with the hits quoted.
6. **`LESSONS.md`**, rules Claude could follow when writing by hand. For each rule give:
   - the rule in one sentence;
   - the evidence (pair ids, splice results);
   - how confident you are;
   - what result would prove it wrong.

   Mark any rule a chat model can't follow as such, for example one that depends on word probabilities. Don't write a rule the data doesn't support. Say "no clear pattern" where there isn't one.
7. **Transfer test: not for Pro.** Claude will do it later with `inputs/learning/E_holdout/`, after reading this analysis. Don't read those files, and don't write paragraphs of your own.
8. **`QUALITY-<slug>.md`, one per article,** going section by section:
   - List what the original says (its points, facts, names, numbers, links), and whether the humanized version keeps each one.
   - List anything added. **Any new "I…" experience or fact about Joel's life means the section is rejected** (Joel's rule).
   - List any of Joel's bans that appear (below).
   - **For neuro de-armoring:** every compound, dose, unit, timing, warning and study claim must match the original exactly. Any change means the section is rejected.
   - List every coined word or catchy phrase of Joel's that the rewrite changed, such as "pl/ork", "Hearthwork", "wizdumb" or the emojis in headings. Joel wants them kept, and he decides.
   - Mark the paragraphs where Joel tells his own story, and say whether the rewrite still tells it truly.
   - Give each section a verdict: ready, needs a fix (say what), or failed Pangram.
9. **`MORNING-NOTE.md`** for Joel, at most 10 lines: what's done, what passed, what needs him, and the budget used.


## Joel's bans (check every output, and every text Pro writes)

- "doesn't get to decide" and its family ("doesn't get to", "gets to", "gets a vote"), said of a feeling or a thing;
- "Fine," "Good," or "Great," as a clause on its own;
- wry humor;
- too many made-up scenes (a caution, not a ban);
- lists that over-explain;
- invented facts about Joel's life or experience;
- in the inner child article, always "your little one", never "the kid";
- phrases Joel dislikes:
  - "that's doing some work"
  - "load-bearing"
  - "tells on itself"
  - "metabolize" or "digest" meaning deal with
  - "clean" as praise
  - "does its work"
  - "That's not X. It's Y."