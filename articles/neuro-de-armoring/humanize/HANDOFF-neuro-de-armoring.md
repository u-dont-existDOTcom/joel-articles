# Handoff: Neuro de-armoring humanization

Joel's protocol article "Bottom-up Healing for Trauma & Addiction: "Neurological De-Armoring" + Brainstem Relaxation v5.1
(Sept 10, 2026)" (https://ibogaqueen.substack.com/p/trauma-and-addiction-why-neurological, post 181671197), humanized so every paragraph and section reads Human in Pangram with every
compound, dose, unit, timing and warning exactly as it went in. It is #3 in his queue of 2026-09-28
(`articles/inner-child-therapy/experiments/emulate-20260929/ARTICLES.md`). Started 2026-11-02 at his message of 18:16 UTC:
"so are we done now can you update the hypnosis article? hypnosis.u-dont-exist.com then we can start on the next one we
had queued".

**Resume line (paste into any Claude account; the repository is public):**
> Continue my neuro de-armoring work: read https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/neuro-de-armoring/humanize/HANDOFF-neuro-de-armoring.md and carry on from its next step.

If that branch is gone (merged), the same file is on main:
https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/neuro-de-armoring/humanize/HANDOFF-neuro-de-armoring.md

From an account with Desktop Commander connected to the laptop: "Continue my neuro de-armoring work: on my laptop, read
~/claude-acceptance-transfer/handoffs/neuro-de-armoring.md and carry on from its next step."

## START HERE

- **2026-11-02, after Joel's message of 19:11 UTC: the lightest fix tried, and question 1 waits on him.** Part 1 C to E with the template taken off and every claim kept read [AI Detected, 90.6% AI](https://www.pangram.com/history/8a5c6453-c6f1-4ab3-b713-51e54e3550f2) (`fix-20261102/s04/`). Question 1 (`OWNER-QUESTIONS.md`, published as Neuro De-Armoring Questions, https://claude.ai/artifact/8cWv5mbXY8y53RL1nhvzky) asks how freely the science sections may be rewritten. When the post is updated, its title's "v5.1 (Sept 10, 2026)" changes too (gate E323).
- **2026-11-02: the lane is set up and the baseline is checked.** The article is registered (`articles/INDEX.json`,
  `articles/neuro-de-armoring/`: master.md is his post as it stands, IMPORT-RECEIPT-20261102.md). The baseline, through
  the API with public links (`fix-20261102/baseline/`, batch n1102, RESULTS.md): every one of the ten sections reads AI
  (58.6% to 100% AI), and the whole reads [AI Detected, 83.3% AI](https://www.pangram.com/history/72952f09-0e99-46d6-b89f-5fa574422584).
  His introduction reads Human (High). All eleven predictions were right.
- **The rule that comes first**: every compound, dose, unit, timing and warning exactly as it went in. `FIDELITY-KEYS.json`
  holds them (96 numbers with their units, 133 compounds and terms, 87 warning sentences; `tools/humanization/fidelity_keys.py`).
  Run `python3 tools/humanization/fidelity_keys.py check articles/neuro-de-armoring/humanize/FIDELITY-KEYS.json DRAFT.md`
  on every draft before it is checked in Pangram or shown to him; a FAIL is fixed, never waived. Emulate's rewrites of
  this article broke the rule in 14 of 40 captures (a lost "below 90 BPM", a dose range reworded, "Cycle off NAC" made
  optional; `QUALITY-neuro-de-armoring.md` on the branch `gpt/emulate-overnight-20260929`), so Emulate's text is not used.
- **The shared rules**: AGENTS.md, docs/HUMANIZATION-GATE.md (E321: what turned his own texts Human, in order), tells_lint.py,
  the owner-delivery gate, suggestion_review.py 1.5 cards (what Pangram read and the check of the suggestion, both linked),
  one try per lineage per round, predictions first.

## Whose words

All of the article is his published post. His queue's rule: "Paragraphs that already read Human in the Pangram baseline
stay exactly as they are." Everything else is rewritten in his register and reaches him as cards, each tested first. The
Scott passages, the introduction and the D-serine paragraph in Part 4 sound most like him.

## Next step (2026-11-02, after Joel's message of 19:11 UTC: question 1)

0. **His answer to question 1** decides the rewrite: a) freely in his voice, every claim, compound, dose, unit, timing and
   warning kept (fidelity_keys.py check), nothing invented (C03), one card per section; b) his own lines first, then the
   rest fitted around them; c) only Parts 2 to 5. Whatever he says, each section is checked in Pangram before it reaches
   him; ND1102-04 has used both its section tries, so its next check is the one more check after a fix that his answer
   28a gives a section (`pangram_ledger.py predict --after-fix`).
1. **Then the cards** (suggestion_review.py, one card per section, the fidelity check's PASS on each), the owner-delivery
   gate for every model-written card (three fresh reviewers, as in `articles/inner-signal/humanize/fix-20261102/w1102fix/gate/`).

## Earlier next step (2026-11-02: the baseline is in)

0. **The mailbox first** (`state/MAILBOX.json`, `lane_push.py --mailbox`), as in the other lanes.
1. **Section by section, the AI windows** (`fix-20261102/baseline/RESULTS.md`: 95 AI windows in the whole): start with the
   sections that read 100% AI (Part 1 C to E, Part 2's phosphatidylserine and uridine). For each window: keep his Human
   (High) stretches word for word; rewrite the rest in his register, E321's order first (a specific example of his own,
   such as Scott; cut the closer and the summing up; fold explanations in; join short sentences; plain words for the
   capitalized labels where they carry nothing), keep every list of doses a list, and run fidelity_keys.py check and
   tells_lint.py before anything goes to Pangram.
2. **Check each rewritten section by itself** through the API with `--public` (inbox/neuro-20261102 on the laptop: TEXTS.json,
   SHA256SUMS, `../pangram-r1102/pangram_api.py check TEXTS.json out --expect 4.1 --windows --public`), predictions first
   (`make_baseline.py` shows the form; lineages ND1102-NN), then read the results with
   `articles/inner-signal/humanize/fix-20261102/recheck/record_r1102.py --dir ... --ledger-file articles/neuro-de-armoring/humanize/pangram-ledger.jsonl`.
3. **Cards for him**: a cards page per round (`suggestion_review.py`), every card showing the fidelity check's PASS and both
   Pangram links; a questions page (`OWNER-QUESTIONS.md`, rendered with `render_questions.py` and the page title
   "Neuro De-Armoring Questions") when the first question comes.
4. **Then his post**: his approved changes through the post's editor, the same way as the hypnosis guide
   (`articles/inner-signal/humanize/fix-20261102/live/`; never the editor's paste), and the read-back from the public post.
