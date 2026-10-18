# Handoff: Hypnosis guide humanization

Joel's hypnosis guide ("The Inner Signal", the self-hypnosis guide on his Substack), humanized section by section so every
paragraph and every section reads Human in Pangram's web app with the meaning kept, the same way as the community article.
It is the second article in his queue (`articles/inner-child-therapy/experiments/emulate-20260929/ARTICLES.md`, #2). Started
2026-10-18 after his message of 01:29 UTC: "let's move onto the next article in the queue to humanize from emulate's work.
continue working on that for the next 12 hours as i'll be away from computer. do whatever you can do, if you can't fix
something save it then give me the full report of what you need help with and why you couldn't figure it out."

**Resume line (paste into any Claude account; the repository is public):**
> Continue my hypnosis guide work: read https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/HANDOFF-hypnosis-guide.md and carry on from its next step.

If that branch is gone (merged), the same file is on main:
https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/humanize/HANDOFF-hypnosis-guide.md

From an account with Desktop Commander connected to the laptop: "Continue my hypnosis guide work: on my laptop, read
~/claude-acceptance-transfer/handoffs/hypnosis-guide.md and carry on from its next step."

## START HERE

- **Branch** `claude/community-joel-1018` (pull request 191, open, Joel's to merge; it also holds the community article's
  merge). Everything for this lane is in `articles/inner-signal/humanize/` (paths below are relative to it).
- **The text.** `source/substack-editor-20260928.html` is his Substack editor HTML of 2026-09-28 (the newest paste the
  repository has; it is newer than `../master.html`, r03 of 2026-09-11). `source/published-20260928.md` is the same as
  Markdown; `HUMANIZED-SO-FAR.md` is the working copy (a copy of it until a section is installed). Ask him for his latest
  editor HTML before the merge, in case he edited the post after 2026-09-28 (question 1 on the questions page).
- **Sections as Pangram reads them:** `tools/sections.py` (`sections(markdown, editor_html)`; the native objects, 8 of
  them, are found with the merge's own `island_groups`, and a blockquoted image marker now counts as an image).
- **The baseline** is batch 429g (`fix-20261018/b429/`, `make_b429.py`): every h1 section as it stands, 37 texts (a section
  under 50 words goes with the next). Predictions with chances were written first (`PREDICTIONS.md`), and the predictor's
  (`MODEL-PREDICTIONS.json`).
- **The rule from the queue:** a paragraph that reads Human in the baseline stays exactly as it is. Only flagged paragraphs
  are rewritten, from Emulate's output, with the meaning put back, through the gate (`tools/humanization/pangram_gate.py`:
  march, cold read, grounding, stance, lint), then checked alone (or with a neighbor under 50 words) and in the section.
- **Owner locks** (`../OWNER-LOCKS.json`) are r03's record of unchanged sections, "not an authorship claim"; they don't
  stop a candidate rewrite, but the protected functions (PF01 and on) are meaning that must survive.

## How to run a batch (Pangram's web app)

The desktop app's built-in browser, tab "seed", https://www.pangram.com/dashboard, the account Joel signed in to at
2026-10-18 01:54 UTC (1 credit per 100 words; its plan says 500 scans a month, so spend scans carefully). Never sign in,
never tick a CAPTCHA: if it's signed out, stop and tell him.
1. Build the batch with its gate records; write `PREDICTIONS.md` (`| text | mine | chance | why | Pangram |`, chance = my
   chance of a 100% Human result) before the run.
2. Commit and push the batch's `bNNN-items.json`; in the tab, fetch it from raw.githubusercontent.com at the commit's SHA,
   check the file's SHA-256 and each item's.
3. Paste `tools/humanization/pangram_page_helpers.js` into the tab if `window.__run` is missing (a reload clears it), then
   `window.__run('BNNNlog', items)`; it submits one text about every 10 seconds. Read results with
   `await window.__readC(items, pages)` and save them as `bNNN-results.json`.
4. `python3 tools/humanization/fill_preds.py bNNN-results.json PREDICTIONS.md` fills the Pangram column with each check's link.

## Emulate

On the laptop, from `~/ai-work/claude-dangerous-lane/joel-articles`: `python3 tools/humanization/emulate_humanize.py humanize
IN.txt OUTBASE` (the script reads the key itself; never print, copy or log it). 40 to 3,000 words a call; about 176,750 words
left on 2026-10-18. Never edit Emulate's output with my own words except to put the meaning back, and every such edit goes
through the gate.

## Waiting on Joel

`OWNER-QUESTIONS.md` (two open: is the 28 September editor HTML the latest; what to do with the de-hypnosis checklist,
which reads AI in every version).

## Where it stands

`STATUS.md` (newest on top, with each section's newest check link; `python3 tools/lane_status.py` rebuilds the table).

## The pipeline for a section (2026-10-18)

From `fix-20261018/`:
1. **Screen.** Emulate's version must read 100% Human first (`make_bNNN.py` with the section's Emulate folders, newest
   last; a folder's segments replace every earlier one they overlap). For an AI window that won't go: send the window's
   published blocks whole, with headings, as one Emulate run (`make_emu_X.py`; `python3 tools/emu_runs.py back --align
   fix-20261018/emu-X` from `humanize/`).
2. **Units.** `python3 ../tools/assemble.py KEY DIRS... --out rev-X/KEY.units.json` (from `humanize/`, paths with
   `fix-20261018/`); check its text equals the screen's draft.
3. **My review.** `rev-X/make_reviews.py` (smallest fixes, published words in Emulate's sentence, quotes in the
   stretch's own style) then `python3 ../tools/faithful.py apply rev-X/KEY.units.json rev-X/KEY.review.json
   rev-X/KEY.fixed.json`. A long section: `faithful.py chunks UNITS OUT_PREFIX 15` and a Sonnet reviewer per part,
   whose JSON I check before it goes in.
4. **Second reader.** `faithful.py verify rev-X/KEY.fixed.json verify-Y/KEY.verify-prompt.txt`, a Sonnet reader.
5. **Answer every finding.** Fix it (`rev-X/KEY.round2.json`, then `faithful.py merge` and `apply`) or answer it in
   `dispositions.json`; then mark the section in `meaning-status.json`.
6. **March.** `python3 ../tools/march_pairs.py draft rev-*/KEY.fixed.json ... --out march-Z --only-needed`, the prompt in
   march-c's form, a Sonnet reader, `march_pairs.py read march-Z march-Z/march-labels.txt`. Where a fix took out a
   break, put one back from Emulate's own words (march-c's six are in `rev-d/make_HG14_review.py` and
   `rev-d/HG35.review.json`).
7. **Pangram.** `python3 make_b434.py --dry` lists what's ready; `--write` builds the batch (one edit record per
   section). Then paragraph checks, section records, install into `HUMANIZED-SO-FAR.md`, links back from the reviews'
   "links".

## Next step (2026-10-18, after batch 440g)

1. Read march-d and march-e when they're in (`python3 ../tools/march_pairs.py read march-d march-d/march-labels.txt`,
   the same for march-e); for every stretch whose edit has fewer paragraphs with a break than Emulate's version, put a
   break back and read it again.
2. `python3 make_b434.py --write`, predictions first, push, run 434g in the seed tab.
3. The second readers of rev-f (verify-c) and rev-g (verify-d), and the part reviews of HG17 and HG31
   (`rev-g/HG17.review.partN.json`, `rev-g/HG31.review.partN.json`): check them, answer, march, then their own batch.
4. Keep `STATUS.md`, this note and the laptop copy current after every batch.
