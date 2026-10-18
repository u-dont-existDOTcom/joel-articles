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

1. Is the Substack editor HTML of 2026-09-28 still the latest, or did he edit the post after that? (The merge uses it.)
2. The de-hypnosis checklist (HG32) reads AI in every version tried: published (429g), Emulate whole (432g), Emulate in
   six pieces (435g). It is a list of short questions. Options for him: keep it as published (the guide would then not
   be 100% Human there), let it become prose, or cut it down. Nothing is changed until he answers.

## Where it stands

`STATUS.md` (newest on top, with each section's newest check link; `python3 tools/lane_status.py` rebuilds the table).

## Next step (2026-10-18 04:00 UTC)

1. **Round-2 meaning fixes.** When the second reader's files are in (`fix-20261018/verify-b/*.verify.txt`, for HG14,
   HG20, HG35, HG02+03, HG27, HG33), put each real problem into the reviews (`rev-d/make_HG14_review.py`,
   `rev-d/HG20.review.json`, `rev-d/HG35.review.json`, `rev-e/make_reviews.py`; mark them `"round": 2, "from":
   "verify-b"`), then re-apply: `python3 ../tools/faithful.py apply rev-X/KEY.units.json rev-X/KEY.review.json
   rev-X/KEY.fixed.json` (from `fix-20261018/`).
2. **Put back six breaks** that my fixes took out (march-c): HG14 B6 (Emulate's "Please note," and "(to the best of my
   knowledge)"), B38 (its closing "Etc."), B42 ("Feel free to use this parts language when..."), B51 (a question, or
   Emulate's "practice the following sequence to “embody” it"), B60 (Emulate's own sentence "I think it can be a
   perfect fit." on its own); HG35 B2 (Emulate's whole sentence "There are definitely advantages to both working with
   someone and doing it yourself...", then the published points). Mark them `"march_note": "march-c"`.
3. **One march read (march-d)** of every stretch changed since its last read: verify-a's round-2 fixes (HG13, HG15,
   HG18, HG19, HG21, HG23, HG34, HG40), rev-e (HG02+03, HG27, HG33), verify-b's round 2 and the six breaks:
   `python3 ../tools/march_pairs.py draft rev-*/KEY.fixed.json ... --out march-d`, a Sonnet march reader on
   `march-d/march-prompt.txt` (short output: `T<n>: S B S`), then `python3 ../tools/march_pairs.py read march-d
   march-d/march-labels.txt`. An edit is held when it has fewer paragraphs with a break than Emulate's version had.
4. **Batch 434g, the test of the meaning fixes.** One `edit` record per meaning-fixed section (its "was" is the screen
   that read Human, with the link; march_was and march from the march reads; cold, grounding, stance and missing from
   the reviews and verify), predictions first, push, run. Sections that stay Human: paragraph checks, section records,
   install into `HUMANIZED-SO-FAR.md`, links put back from the reviews' "links" anchors.
5. **Third samples (emu-h).** On the laptop, `~/ai-work/claude-dangerous-lane/inbox/emu-hg-h/run-all.log` lists 12 runs
   when done. Pack the outputs into a tgz in the inbox, stage it, copy `*.out.txt` and `*.out.json` into
   `fix-20261018/emu-h/`, run `python3 tools/emu_runs.py back fix-20261018/emu-h` (from `humanize/`), and screen them
   (437g) with the newer folder last in each key's list of folders.
6. Keep `STATUS.md`, this note and the laptop copy current after every batch.
