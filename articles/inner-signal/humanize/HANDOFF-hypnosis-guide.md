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
from `humanize/`. 40 to 3,000 words a run (a window under 40 is refused); about 80,000 words left after emu-ay (2026-10-18).
Stage every file for the laptop under a name of its own (its SHA in the name): device_commit_files can write an older file
that was staged under the same name (2026-10-18: the handoff copy came back as an older version), so check the SHA there
before using it. Several sample sets run in one `sh -c "...; ..."` chain, one after the other. Never chain a run behind
another with `pgrep -f` on the other's command line: the waiting shell's own command line matches, so it waits forever
(emu-t lost eight minutes to that). Never edit Emulate's output with my own words except to put the meaning back, and
every such edit goes through the gate.

## Waiting on Joel

`OWNER-QUESTIONS.md` (four open: is the 28 September editor HTML the latest; the de-hypnosis checklist, which reads AI in
every version; HG31's two meaning points against a Human reading; and the two guided scripts, HG17 and HG18).

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
- **Installed so far:** 30 keys (36 of 40 sections done with HG05, HG08, HG09 as published; HG24 on 460g, HG36 whole on 462g), listed in `fix-20261018/installed.json` (`tools/install_fixed.py install`, links put back from
  each stretch's "links"). HG36's old entry (B10-B12 as published, unchecked) is kept under "was" in its new one.
- **What 446g to 454g added:** pasted published wording reads AI even in a two-line fix (HG37, 454g), so a fix is always in
  the stretch's voice; a paragraph check is predicted by how much of it isn't Emulate's (`tools/para_chance.py`: under 5%,
  99% Human); several samples of a window go to Emulate at once and the second reader picks; a long script loses its
  steps in one window, so it goes in windows of 50 to 80 words; edits and their paragraph checks go in the same batch.
- **What 459g to 461g added:** a stretch that keeps reading AI gets one new run over the whole stretch, not pieces between
  installed paragraphs: HG24's opening in one window read Human in 3 of 3 samples, HG36's whole section in one run in 1
  of 3, but HG36's B10-B11 or B9-B12 between installed paragraphs in 0 of 6 (each paragraph passed alone; the AI window
  sat where the runs meet). Predict accordingly: about 0.6 for a one-window sample of a stuck stretch, 0.15 for pieces
  between installed runs. Samples of my meaning-fixed text kept HG36's meaning best but read AI; the one of the published
  text read Human. Paragraph chances were refitted on all 637 paragraph checks (`tools/para_chance.py`: 0.95, 0.91,
  0.75, 0.75). `compose_v.compose` writes `rf-v/KEY.units.json`: a builder that renames it must put back the file that
  was there (459g's first dry run moved HG17's and HG24's; restored from Git).

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

**The fast path for a stretch that keeps reading AI (459g on; HG24 went from AI to installed in two batches this way):**
1. One new run over the whole stretch, never pieces between installed paragraphs (the AI window sits where runs meet),
   in two or three sample sets (`make_emu_aq.py`, `make_emu_at.py`: `make_emu_ac.window` for my fixed text, or the
   published blocks).
2. One batch: each sample's section screened whole with its paragraph checks (`make_b459.py`, `make_b461.py`, through
   `compose_v.compose`; two runs of a section in one folder need the window's `skip`), and a Sonnet second reader per
   sample at the same time (`make_verify_samples.prompts(folder, key, units, '.TAG')`).
3. The sample that passed with the fewest findings goes to its own folder (`rf-zb/`, `rf-zd/`: `KEY.units.json`, its
   verify files), its triage (`KEY.triage.json`, the brief's rules), `tools/triage_apply.py`.
4. One batch: the fixed text whole with every paragraph its fixes changed (`make_b460.py`), then install as in step 5.

## Next step (2026-10-18, after batch 462g)

From `fix-20261018/`; `STATUS.md` has the results and `OWNER-QUESTIONS.md` the decisions that are Joel's. Every section
that isn't a question for him is done: 36 of 40 (33 installed with every paragraph checked alone, three Human as
published). Nothing is left to run until he answers.
1. **HG31** reads Human whole and in every paragraph as `rf-z/HG31.v3.json` (458g), without two of its triage fixes (B25's
   examples, B28's "never hide a demand"). Install it only when Joel answers question 3 with (a); with (b), the fixes stay
   and its Pattern 4-6 window needs another way (457g: B28's fix reads AI in any wording tried so far; try the fast path's
   one new run over B25-B34 from the published text).
2. **HG17 and HG18** (question 4): wait for Joel. Facts: HG18's 459g sample `rf-za/HG18.ma.json` reads 100% Human whole and
   in every paragraph but loses four safety statements (`rf-za/HG18.ma.verify.part1.out.txt`); with (b) those would be put
   back as triage fixes in its voice and checked; with (c) his own words go in as written. HG17's script loses 11 to 31
   steps in every Emulate version that reads Human, and its two-hand and sleep inductions read AI in the 459g screens too.
3. **HG32** (question 2): wait for Joel.
4. **The merge** (question 1): when Joel says the 28 September editor HTML is the latest (or pastes a newer one), merge
   `HUMANIZED-SO-FAR.md` into it with the clipboard helper, as for the community article.
5. **To reinstall a section**: `tools/install_fixed.py install` replaces published blocks, so a section that is already in
   the article is reinstalled by rebuilding the article from `source/published-20260928.md` with every `fixed` file in
   `fix-20261018/installed.json` (462g: HG36; the rebuild with the old list reproduced the article exactly).
6. Keep `STATUS.md`, this note, the laptop copy and the scorecard page current after every batch.
