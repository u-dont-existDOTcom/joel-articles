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

On the laptop, in `~/ai-work/claude-dangerous-lane/inbox/emu-hg-X/`: copy `run_emulate.py` from `emu-hg-g/`, put the run
folder's `BUNDLE.json` there (stage it in `/mnt/user-data/outputs/` and write it with device_commit_files; check its
SHA-256), then `nohup python3 run_emulate.py BUNDLE.json /abs/path/emu-hg-X RUN RUN ... > run-all.log 2>&1 &` (the script
reads the key itself; never print, copy or log it). Pack `*.out.txt *.out.json run-all.log` into a .tgz, stage it, unpack it
into the scratchpad, copy into `fix-20261018/emu-X/` and run `python3 tools/emu_runs.py back --align fix-20261018/emu-X`
from `humanize/`. 40 to 3,000 words a run (a window under 40 is refused); about 88,000 words left after emu-ag (2026-10-18). Never chain a run behind
another with `pgrep -f` on the other's command line: the waiting shell's own command line matches, so it waits forever
(emu-t lost eight minutes to that). Never edit Emulate's output with my own words except to put the meaning back, and
every such edit goes through the gate.

## Waiting on Joel

`OWNER-QUESTIONS.md` (three open: is the 28 September editor HTML the latest; what to do with the de-hypnosis checklist,
which reads AI in every version; and his own table-of-contents note, which reads AI-Low in the one version of HG02+03 that
otherwise reads Human).

## Where it stands

`STATUS.md` (newest on top) and the section table: `python3 tools/lane_status.py` (each section's newest whole check with
its stage, its paragraph checks, and **installed** for the sections in `fix-20261018/installed.json`).

## What 434g to 445g taught (2026-10-18)

- **My meaning fixes make a section read AI when they change much of it.** Of 33 fixed sections, the 3 whose fixes changed
  under 18% of the words stayed Human; of the 30 that changed more, 2 did (434g, 441g, 444g). The fixes put the published
  phrasing back, and the published phrasing is what read AI in 429g.
- **Plan B works for Pangram: send the fixed text back to Emulate** in the windows that read AI (`tools/refix_runs.py
  window_runs`). 443g: 17 of 21 such refix screens read 100% Human; 445g: 4 of 5 more.
- **But Emulate bends the meaning again** (the second reader found 0 to 71 problems per refix section; HG26, the "when to
  get help" section, softened "get urgent help now"). So each refix goes through a second reader, then a **triage**
  (`fix-20261018/rf-a/TRIAGE-BRIEF.md`): only what changes what a reader would do or believe is fixed, in as few words as
  possible and in the stretch's own voice; nuance and tone are let stand and listed. The aim is under about 10% of the words
  changed, so the section stays Human.
- **Every paragraph is then checked alone** (`tools/install_fixed.py`: `section_md` is the Markdown that will be installed,
  `para_texts` the fewest texts `paragraphs_alone.py` looks for). In 442g, 17 of 23 paragraph texts of Human sections read
  Human; the ones that didn't get their own refix run (emu-s).
- **Installed so far:** 23 keys, listed in `fix-20261018/installed.json` (`tools/install_fixed.py install`, links put back from
  each stretch's "links"). HG36's entry has an "open" note: its B10-B12 are as published and unchecked.
- **What 446g to 454g added:** pasted published wording reads AI even in a two-line fix (HG37, 454g), so a fix is always in
  the stretch's voice; a paragraph check is predicted by how much of it isn't Emulate's (`tools/para_chance.py`: under 5%,
  99% Human); several samples of a window go to Emulate at once and the second reader picks; a long script loses its
  steps in one window, so it goes in windows of 50 to 80 words; edits and their paragraph checks go in the same batch.

## The pipeline for a section (2026-10-18, current)

From `fix-20261018/` unless a command says `humanize/`:
1. **Screen**: Emulate's rewrite of the published text reads 100% Human (`make_bNNN.py`; whole AI windows as one run).
2. **Meaning**: my review (`rev-X/`), a second reader (`faithful.py verify` or `verify-chunks` for long sections), my
   answers (round 2, `dispositions.json`, `meaning-status.json`), a march read (`march_pairs.py`; split a big draft into
   parts of about 100 paragraphs and join the labels), then the edit check (`make_b434.py --batch N --write`).
3. **Refix** the edit's AI windows (`make_emu_X.py` with `refix_runs.window_runs`; a quotation of someone else is kept out),
   then screen (`refix_runs.assembled_fixed(fixed, [emu folders])`).
4. **Second reader of the refix** (`refix_runs.units_fixed` -> `rf-X/KEY.units.json`; `rf-a/make_verify.py rf-X`), then the
   **triage** (a Sonnet reader per few sections with `TRIAGE-BRIEF.md`, its `KEY.triage.json` checked by me), fixes applied
   (`faithful.py apply rf-X/KEY.units.json REVIEW OUT`), a march read of the fixed stretches, an edit check.
5. **Paragraph checks** (`make_b442.py` for fixed sections; `make_b445.py` shows the same for refix units), then **install**
   (`python3 tools/install_fixed.py install HUMANIZED-SO-FAR.md FIXED_OR_UNITS.json ...` from `humanize/`) and a line in
   `fix-20261018/installed.json`.

## Next step (2026-10-18, after batch 454g)

From `fix-20261018/` (each item's files are named; `STATUS.md` has the results):
1. **Batch 455g** (`make_b455.py`, to write): edits and paragraph checks of HG33 (`rf-k/HG33.fixed.json`), HG06
   (`rf-l/HG06.fixed.json`, the emu-ac sample of its forces paragraph), HG26 (`rf-l/HG26.fixed.json`, the emu-ac sample of the
   get-help paragraphs), HG31 (`rf-m/HG31.fixed.json`, the emu-ad sample of the reframing questions), HG36 (`rf-p/HG36.fixed.json`,
   B10-B12 put back) and HG37 (`rf-e/HG37.fixed.json`, its three pasted fixes reworded), once the march read `march-t` is in
   (`march_pairs.py read march-t march-t/march-labels.txt`; no break may be lost).
2. **Emulate on the laptop:** emu-ah and emu-ai (HG14's four AI paragraphs, HG37 B26, HG15 p10 and p11, two samples each) were
   running at 07:57 UTC in `inbox/emu-hg-ah`, `inbox/emu-hg-ai`: bring back, `emu_runs.py back --align`, second reader
   (`make_verify_samples.py` shows how), pick, triage, screen. HG15's p23-p24 sample is emu-ad's (`emu-ad/HG15-pw2.out.txt`):
   one fix, "learning that you can disappoint someone without disappearing" put back in its voice.
3. **HG17's script:** the second reader of `rf-r/` and `rf-s/` (the two samples of seven small windows, emu-af and emu-ag): pick
   the better sample per window, triage, then screen HG17 with the rf-j triage fixes.
4. **HG24:** `rf-o/HG24.units.json` (B36-B37 as published; B42-B48 from emu-aa) with the carried triage `rf-o/HG24.triage.json`
   and the new one `rf-o/HG24.triage.new.json` (Sonnet, running): merge, apply, march, screen.
5. **HG14:** its one triage fix is applied (`rf-k/HG14.fixed.json`); after emu-ah/ai, put the chosen paragraph samples in and
   screen with its paragraph checks.
6. HG18 and HG32: report to Joel (AI in every version; `OWNER-QUESTIONS.md`).
7. Keep `STATUS.md`, this note, the laptop copy and the scorecard page current after every batch.
