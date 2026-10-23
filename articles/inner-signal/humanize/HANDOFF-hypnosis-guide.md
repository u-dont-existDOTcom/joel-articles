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

- **2026-10-22: the Inner Child lane's note (`NOTE-FROM-INNER-CHILD-LANE-20261022.md`) is handled.** Part 1: the
  drafts are renamed without "Pangram" ("TEMP recheck A (hypnosis guide) - do not publish", "TEMP recheck B (hypnosis
  guide appendices) - do not publish"; the screening post is "TEMP screen (hypnosis guide samples) - do not publish"),
  and pastes go through `fix-20261022/screen/paste_payload_lane.js` (exact titles, an empty body only: clear it with
  ctrl+a and Delete in the editor first, then the words check); `fix-20261020/substack41r/paste_payload.js` is marked
  superseded. The Pangram result opens in Brave's side panel, so Joel copies its link ("Copy shareable link to result").
  Part 2: Joel answered for it (question 10, 18:37 UTC: "check the work in the innerchild article lane regarding the
  naming conventions as they've been updated"), batch 470g; two of its points and one from the review are question 12.
- **2026-10-20: Pangram 4.1 and Joel's budget rules.** This lane's results up to batch 466g are Pangram 4.0; from the
  whole-guide check of 2026-10-20 on they are 4.1, and the ledger keeps the two apart. His rules of 20
  October (merged into this branch from main) govern every call: `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md` (six tries
  per paragraph lineage, each with a specific diagnosis; one section check plus one recheck; one whole-article
  certification plus one recheck at the end; read 4.1's sentence shading). Every call goes through
  `tools/humanization/pangram_ledger.py` with this lane's ledger `pangram-ledger.jsonl` (`predict` before, `results`
  after, `explain` for each miss, `build --universal state/PANGRAM-SCORECARD.md` after the session; this lane's page is
  `SCORECARD.md`). Joel signed in to Pangram in the desktop app's browser again on 20 October (his message of 22:01
  UTC), the same account as the community checks; on 2026-10-22 at 22:44 UTC it was signed out there (History asked to
  sign up). Never sign in: whole-guide and screening checks go through his Brave anyway, and a single paragraph can go
  through the API on the laptop (`tools/humanization/pangram_api.py`, model "pangram-4", whose results say 4.0).
- **Whole-guide checks go through a temporary Substack post, free** (Joel, 2026-10-20 22:01 UTC: "for very large pangram
  checks (not just one section, but like whole article especially) you can just ask me to make a temporary article on
  substack to check it free"; `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`). Since his 23:54 message I make the drafts
  myself in the app's browser (his Substack cookies are there): `fix-20261020/substack41r/make_recheck.py` builds both
  parts (the check reads at most 99,999 characters), `paste_payload.js` pastes one after checking its SHA-256, then
  Preview, "Paid subscriber view", Share, the secret link. The Pangram label needs the Pangram Chrome extension, which
  the app's browser lacks, so Joel opens the secret links in his Chrome (or connects Claude in Chrome there). Never
  Publish. Paragraph and section checks stay on pangram.com.
- **What 4.1 flags** (the community article's lesson, `docs/HUMANIZATION-GATE.md`, "What Pangram 4.1 flagged in the
  community article"): wry quips, aphorisms and balanced closers, tidy restating or reassuring follow-ups, parallel or
  signposting explanations, generic "you"/"imagine" scenarios, stock words. A break is not a joke; cut a restating
  sentence rather than reword it; name the person and the moment.
- **Branch** `claude/community-joel-1018`. Pull request 191 (the community article's merge and this lane up to the first
  4.1 check) was merged on 2026-10-20 at 23:29 UTC; pull requests 206 and 209 (the 4.1 work to 2026-10-21 22:43 UTC)
  were merged; pull request 219 (to 2026-10-22 22:05 UTC) was merged at 22:16 UTC; the work since is pull request 222
  (https://github.com/u-dont-existDOTcom/joel-articles/pull/222), open and Joel's to merge. Main moves often (the Inner
  Child lane merges too): `lane_push.py` says after each push whether the pull request can merge. Everything for this lane is in `articles/inner-signal/humanize/` (paths below are relative to it).
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
   chance of a 100% Human result) before the run, and put each text in the ledger
   (`python3 tools/humanization/pangram_ledger.py predict articles/inner-signal/humanize/pangram-ledger.jsonl --lineage L
   --scope paragraph|section|article --text FILE --key KEY --call Human|AI --chance P --tells ... --human-tells ...`, from
   the repo root; it refuses what the budget rule forbids). `pangram_ledger.py check LEDGER bNNN-items.json` before the run.
2. Commit and push the batch's `bNNN-items.json`; in the tab, fetch it from raw.githubusercontent.com at the commit's SHA,
   check the file's SHA-256 and each item's.
3. Paste `tools/humanization/pangram_page_helpers.js` into the tab if `window.__run` is missing (a reload clears it), then
   `window.__run('BNNNlog', items)`; it submits one text about every 10 seconds. Read results with
   `await window.__readC(items, pages)` and save them as `bNNN-results.json`.
4. `python3 tools/humanization/fill_preds.py bNNN-results.json PREDICTIONS.md` fills the Pangram column with each check's link,
   and `python3 tools/humanization/pangram_ledger.py results articles/inner-signal/humanize/pangram-ledger.jsonl
   bNNN-results.json` scores them in the ledger; `explain` each miss's cause.

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

`OWNER-QUESTIONS.md`: recheck B's result link (draft B is pasted and verified, 2026-10-23 02:05 UTC); question 14 (the seam
between the shortcut part and the return, his own words). Questions 1 to 8 were answered at 2026-10-21 17:56 UTC, 9 to 11
at 2026-10-22 18:37 UTC, 12 at 21:41 UTC, 13 at 2026-10-23 01:10 UTC.

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

## Next step (2026-10-23, after Joel's message of 01:10 UTC: recheck B waits on his Brave, question 14 on him)

Done since the step below: recheck A read (`fix-20261022/recheck/RESULT-A.json`, Mostly Human Written, 1.4% AI; ledger
HG-whole#33 right once its verdict was corrected to Mixed, E225); 470g's and 471g's forecasts scored for part A, 17 of 17
(`fix-20261022/recheck/score_recheck.py`); his answer 13 installed, his own Appendix C prose (`fix-20261023/make_joel_0110.py`,
edit HG32-joel-0110); batch 472g through the API on the laptop (`fix-20261023/b472/`, its `API-CHECKS.md`; fourteen checks,
ledger #34 to #47): b472-s1b and b472-s3c in, the seam (HG17-B306 and HG18-B308) AI in six versions; recheck B rebuilt,
predicted (HG-rest-B#48) and pasted (`fix-20261023/recheck/RECHECK-POST-B.json`, its rendered text equal to TEXT-B.txt).
Lessons E223 to E229 in `docs/HUMANIZATION-GATE.md`.

1. **When Joel sends recheck B's result link**: read the windows from the page (the compact line, as in
   `fix-20261022/recheck/`), then `substack_check_text.py result fix-20261023/recheck/PAYLOAD-B.html WINDOWS-B.txt
   META-B.json --out RESULT-B.json` (no `--limit` needed: part B is 57,384 characters; the checked text should hash to
   76745975...), the ledger result for key HG-rest-41r4-b (use `verdict_of`'s rule: Human only for a 100% Human result),
   his Appendix C's windows read on their own, and the part B forecasts scored (`fix-20261022/recheck/score_recheck.py` reads RESULT-B.json from
   `fix-20261023/recheck/`). A red stretch gets a diagnosis;
   one of his own paragraphs that reads red goes back to him with the check's link and part number (E214), never into my
   words.
2. **Question 14** (`OWNER-QUESTIONS.md`): A, his words for the two seam paragraphs go in as he writes them (an edit of
   each paragraph in `fix-20261020/EDITS41.json`, source his message, as HG32-joel-0110); B, a seventh try: the shortcut's
   retiring steps folded into "Also, be sure that this is working for you ..." (lineage HG17-B306 has three API tries
   left, HG18-B308 one); C, they stay red. Until he answers, nothing changes there.
3. **Then recheck A**: `fix-20261023/recheck/make_recheck.py` again, a prediction for part A (key HG-whole-41r5-a; add its
   row to that folder's `make_preds_recheck.py`), pasted into draft A (221411215, "TEMP recheck A (hypnosis guide) - do
   not publish") with `fix-20261022/screen/paste_payload_lane.js` after clearing its body with real keystrokes, and the
   rendered lines compared with TEXT-A.txt before Joel is asked. It reads b472-s1b, b472-s3c and his answer to 14 in place.
4. **API checks** (E218: paragraphs and sections, five or six paragraphs at most) run on the laptop from
   `/home/joel/ai-work/claude-dangerous-lane/pangram-api/hg-b472/`, with the repository's `pangram_api.py` fetched there at
   a main commit (SHA-256 4a100ecd... at 92f87f0d); the lane folder's own copy is the old 4.0-only one. The texts go over
   as gzip and base64 with their SHA-256 checked on both sides; one open check per lineage (the ledger refuses a second).
5. **Queued after this guide: his Nibbāna article** (`articles/nibbana/humanize/QUEUE-20261022.md`), then **question 6 b**.

## Earlier next step (2026-10-22, after Joel's links of 21:41 and 23:01 UTC: recheck A waits on his Brave, question 13 on him)

Done since the step below: pull request 219's conflicts (main took the Inner Child lane's 218, then its 220; merges afc6ea1b
and 9dff534e), merged by Joel at 22:16 UTC; his answer 12 as batch 471g (`fix-20261022/b471/`: two review rounds, gated,
forecast, installed); both screening posts read (`fix-20261022/screen/SCREEN-RESULT.json`: HG17's bd and bf Human in every
window; `fix-20261022/screen2/SCREEN2-RESULT.json`: Appendix B's stretch Human, Appendix C as installed AI, the new opening
C1 Human from the tricks list to "A bad guide can't.", AI in its opening and the bad guide's last sentence); the induction
section from sample bf with its meaning fixes, four rounds of reviews, gated and installed (`fix-20261022/hg17-bf/`:
`make_hg17_bf_fixed.py`, `make_hg17_bf_reviews.py`, `make_hg17_bf_r2.py --round N`, `make_gate_hg17_bf.py`,
`install_bf.py`); recheck A pasted and verified (`fix-20261022/recheck/RECHECK-POST-A.json`); Nibbāna's editor HTML
registered, its rebuild equal to the check.

1. **When Joel sends recheck A's result link**: read the windows from the page (`tools/humanization/pangram_feed_read.js`,
   its compact line), `substack_check_text.py result fix-20261022/recheck/PAYLOAD-A.html WINDOWS-A.txt META-A.json --limit
   99999 --out RESULT-A.json` (the checked text should hash to TEXT-A.txt's fd2e3ed6...), the ledger result for key
   HG-whole-41r4-a (prediction HG-whole#33), the induction section's windows read on their own (its span in TEXT-A.txt
   starts at "Inductions serve to gather you up"), and 470g's and 471g's forecasts scored (`b470/batch/FORECAST.json`,
   `b471/batch/FORECAST.json`; their part A paragraphs). A red stretch in the induction section gets a diagnosis in its
   place, its light-green neighbours read with it.
2. **Question 13, Appendix C's opening** (`OWNER-QUESTIONS.md`): A, his own words for the opening's two paragraphs and the
   bad guide's last sentence, go in as he writes them (an edit of b469-HG32-prose in `fix-20261020/EDITS41.json`, with the
   reviews); B, the published list comes back; C, they stay. Until he answers, the default: C1
   (`screen2/CANDIDATES.json`) goes in, its meaning check (`screen2/VERIFY-C.md`, nothing lost) triaged as for bf ("for a
   minute" and the four tests outside the quote are the opening's, which his words replace; "tricks ... being used" and
   "remain an option" are bg's middle, which reads Human: fix only what a reader would act on), then the cold read, the
   stance check, the march, the gate.
3. **Recheck B** (the appendices) once Appendix C is settled: `make_recheck.py` again, `make_preds_recheck.py B` (its row
   is a placeholder until then), pasted into draft B (221412532, "TEMP recheck B (hypnosis guide appendices) - do not
   publish") the same way, the rendered lines compared with the rebuild before Joel is asked.
4. **Queued after this guide: his Nibbāna article** (`articles/nibbana/humanize/QUEUE-20261022.md`, with the red windows,
   their whole paragraphs and a first look at their shapes in `RED-WINDOWS-20261020.md`). The fixes go into his editor HTML
   of 21:41 UTC.
5. **Question 6 b**, after the 4.1 work: the repeats one at a time, as below.

## Earlier next step (2026-10-22, after Joel's answers of 18:37 UTC: the screening post waits on his Brave)

Done since the step below: the recheck's results (Joel, 18:37 UTC:
[part A](https://www.pangram.com/feed/c8001eb5-84a6-41dc-a2c0-0f4733dc3fc7), AI Detected, 13.8% AI;
[part B](https://www.pangram.com/feed/558d14f6-625d-46aa-8495-adf9141cb3a4), Mostly Human Written, 4.9% AI) are read:
ledger HG-whole#21 right, HG-rest-B#20 a miss with its cause; batch 469g's forecasts 15 of 15
(`fix-20261021/b469/batch/SCORE.md`); each reading in `fix-20261020/EDITS41.json` and `fix-20261018/installed.json`.
Red: the induction section (HG17) from its first paragraph to the shortcut, most windows marked "humanized"; three
short windows of the return (HG18); Appendix C's prose, one 518-word window. His answers 9, 10 and 11 are batch 470g
(`fix-20261022/b470/`: `make_b470.py` with its rounds, `make_b470_r2.py`, `make_gate_b470.py`, `make_preds_b470.py`),
installed with `fix-20261020/apply_edits41.py --add`. Six new Emulate samples of the two red sections came back from the
laptop (`fix-20261018/emu-bc` to `emu-bh`, each SHA-256 checked against the laptop's) and are in the screening post
(`fix-20261022/screen/`: `make_screen.py`, `SCREEN-POST.json`; ledger HG17-emu-bc#22 to HG32-emu-bh#27).

1. **When Joel sends the screening post's result link**: read only the windows from the page (its compact line), then
   `python3 tools/humanization/substack_check_text.py result fix-20261022/screen/PAYLOAD-S.html WINDOWS.txt META.json
   --out RESULT-S.json` (the rendered post's paragraphs hash to `TEXT-S.txt`'s SHA-256, d3938178..., so the rebuilt text
   is the checked text), cut the windows by sample with `screen/SPANS.json` (a window across a boundary belongs to both),
   and give each sample its result in the ledger (`result --key screen-S1` to `screen-S6`).
2. **Pick per section**: the HG17 sample (S1 to S4) that reads Human, or the one with the fewest red windows, and the
   Appendix C one (S5, S6) the same way. If none of a section's samples reads Human, say so to Joel with the windows and
   switch method rather than sampling again the same way (for HG17, new runs over each red stretch from the published
   text in windows of 50 to 80 words; for Appendix C, the question of the list back to him).
3. **Meaning work on the chosen sample** as in `fix-20261018/rf-zg/`: a second reader of every point of the published
   section against it; lost points back in the sample's own words (the gate doc's lesson); inventions out (the samples
   have some: S2 credits the two-hand induction to "the Gerson hypnosis course", S5 has "slow the fuck down"); Joel's
   11 b wording for the safety line; the section's three links; then the cold read, stance check, march, rounds, the
   gate and the install. Keep the changes few: ba's restorations were in plain words and still read AI.
4. **Then one whole-guide recheck** with everything (the two sections and batch 470g): `make_recheck.py` with a new date,
   pasted into drafts A and B with `paste_payload_lane.js` (their titles above; clearing the body with ctrl+a and Delete
   can write to Joel's clipboard: tell him), each part's ledger prediction first, and 470g's per-paragraph forecasts
   (`b470/batch/FORECAST.json`) scored after.
5. **Waiting on Joel**: the screening post's result link; question 12; for the Nibbāna article, its current editor
   HTML.
6. **Queued after this guide: his Nibbāna article** (18:37 UTC: "my nibbana article is now not fully passing pangram 4.1,
   you can add that to the queue to work on"; his result link at 19:53 UTC). Its reading and the 22 AI windows are in
   `articles/nibbana/humanize/QUEUE-20261022.md`: Mostly Human Written, 4.5% AI. The registered master (2026-09-28) is
   older than the post, so ask him for the current editor HTML before any fix.
7. **Question 6 b**, after the 4.1 work: the repeats one at a time, as below.

## Earlier next step (2026-10-21 21:41 UTC, after the listening script went in: the recheck waits on his Chrome)

Done since the step below: the induction section (HG17), the one section that was still as published, is installed as
Emulate's sample ba with every lost point put back (`fix-20261018/rf-zg/`: `make_hg17_fixed.py` with its three rounds,
REVIEWS tagged by round; `make_hg17_reviews.py` for round 1's prompts, `make_hg17_round2.py --round N` for each later
round, `make_gate_hg17.py` for the gate; `gate-answers.json` holds what was let stand). Part A of the recheck was rebuilt
with it and pasted into the same temporary draft (ledger: HG-whole#19 voided, HG-whole#21 written,
`fix-20261020/substack41r/make_preds_recheck3.py`). Every one of the 40 sections is now humanized; two (Appendix C's
prose and the induction section) wait for their first 4.1 reading.

1. **When Joel sends the recheck's results** (or loads them into the app's browser): as step 1 below, with part A's key
   now `HG-whole-41r3-a` (`result --key HG-whole-41r3-a`; part B is still `HG-rest-41r2-b`). In part A, map the windows
   over the induction section (`result41/map_windows.py`) and read its sentence shading: its forecast is light green or
   red in parts of the script (the count, the two-hand lines, the shortcut's steps).
2. **Then fix with a diagnosis**, a paragraph to pangram.com only when a segment points at it (E200). For the induction
   section, a red window's paragraphs get a fix in ba's register (a break where a person would react or pause, never a
   quip), or a new Emulate run over that stretch from the published text, then its meaning reviews as in `rf-zg/`. Record
   each section's reading in `fix-20261018/installed.json` (HG17's "whole") and each 4.1 edit's in `EDITS41.json`.
3. **Waiting on Joel**: questions 9, 10 and 11 (11: whether "intoxicated" in "Before you begin" rules out a session on
   loveyhuasca; option B would say "overwhelmed by chemicals", as "Capacity before content" does), the recheck's links,
   the note for the Inner Child chat, and deleting the two temporary drafts once the results are read (E204; permanent
   deletion isn't something this worker does).
4. **Question 6 b**, after the 4.1 work: the repeats one at a time, each with both passages, what's around them, how far
   apart they are, and keep / cut / merge with a pick (gate doc, 2026-10-21 17:56 section).

## Earlier next step (2026-10-21, after Joel's answers of 17:56 UTC and batch 469g: the recheck waits on his Chrome)

Done since the step below: his answers to questions 1 to 8 (`fix-20261021/joel-20261021-1756-message.txt`): his own
HG15 edit installed (`EDITS41.json`, HG15-joel-p9 and -p11, his check Human); HG31 (3 a) and HG18 (4 d) installed as
their Human versions; the inner-figure sweep (`fix-20261021/CONFLATION-SWEEP.md`) and batch 469g (`fix-20261021/b469/`:
Appendix C's general checklist as prose, HG18's lost points, seven inner-figure findings, six fixed), four rounds of
meaning reviews, then into the working copy through `apply_edits41.py` with "paragraph_result": pending. Under gate E200
(main's rule: many paragraphs go through free Substack posts) nothing went to pangram.com this turn. The recheck is
rebuilt (`fix-20261020/substack41r/make_recheck.py`) and pasted into the lane's own two temporary drafts
(`paste_payload.js` with `replace_title`), and its predictions are in the ledger (HG-whole#19, HG-rest-B#20, with
`--decides`). The secret links are on the questions page.

1. **When Joel sends the recheck's results** (or loads them into the app's browser): on each feed page, run
   `tools/humanization/pangram_feed_read.js`, save `fix-20261020/substack41r/RESULT-41r2-a.json` and `-b.json`, map
   them (`result41/map_windows.py`), score them in the ledger (`result --key HG-whole-41r2-a` and `HG-rest-41r2-b`),
   and score 469g's forecasts (`fix-20261021/b469/batch/PREDICTIONS.md`, `FORECAST.json`). Click every Human and Likely
   human row in All Segments when a result is Mixed (the budget rule's 4.1 segments rule) to find the suspect part.
2. **Then fix with a diagnosis**, a paragraph to pangram.com only when a segment points at it: Appendix C's prose had no
   break in its march read (`b469/r2/march-labels.txt`), so if it reads red, give the paragraphs breaks in Joel's raw
   register (a reaction, his doubt, a particular, never a quip) or run Emulate over it; the NLP appendix and the return
   steps were checked only in 4.0. Record each edit's reading in `EDITS41.json` (`paragraph_result`, `section_check`).
3. **The listening script** (HG17, the one section still as published): his 4 d, "i am fine with all the humanized
   replacements as long as we don't lose anything". Done: the fast path's three Emulate samples of the whole section
   from the published text (`fix-20261018/make_emu_az.py`; `emu-az`, `emu-ba`, `emu-bb`, copied from the laptop with
   their SHA-256 checked, 6,036 Emulate words, 73,647 left), aligned (`tools/emu_runs.py back --align`), composed into
   units (`rf-zg/HG17.az.json`, `.ba.json`, `.bb.json`, over `rf-j/HG17.fixed.json`), and a second reader on each against
   the published section (`rf-zg/HG17.X.verify.out.md`): az kept 122 points, changed 76, lost 31, invented 9; **ba kept
   156, changed 57, lost 30, invented 14** (the base); bb kept 133, changed 68, lost 34, invented 21. Next: in
   `rf-zg/HG17.ba.json`, put back all 30 lost points inside ba's own sentences (the listening script's pauses and steps,
   "What am I noticing now?", "Five.", the three links, "keep safety and exit instructions plain", the heading lines the
   alignment kept as text), take out the 14 inventions (his father "uses" the mudra while driving; "I always announce
   when I am doing it"; "see link above"; "something like the below" with nothing below), and fix the changed points
   that change what a reader does or believes (the triage brief, `fix-20261018/rf-a/TRIAGE-BRIEF.md`); then the gate's
   reviews, the install with "pending", and its reading in the next recheck through Substack.
4. **Waiting on Joel**: questions 9 (the synchronicity cue's "my Protector") and 10 (one name for the inherited parent),
   the recheck's links, the note for the Inner Child chat, and deleting the two temporary drafts when the results are in
   (E204 asks the worker to delete them; permanent deletion isn't something this worker does).
5. **Question 6 b**, after the 4.1 work: the repeats one at a time, each with both passages, what's around them, how far
   apart they are, and keep / cut / merge with a pick (gate doc, 2026-10-21 17:56 section).

## Earlier next step (2026-10-21, after batch 468g: the recheck waits on Joel's Chrome)

Done since the step below: both halves of the first 4.1 check read and mapped (`fix-20261020/substack41/RESULT-41a.json`,
`RESULT-41b.json`, `result41/`); the risk read scored; batches 467g and 468g, which installed six 4.1 edits through
`fix-20261020/apply_edits41.py` (`EDITS41.json`: after any rebuild or re-install, run it again); the recheck's drafts
made in the app's browser (`substack41r/`). The ledger: `python3 tools/humanization/pangram_ledger.py status
articles/inner-signal/humanize/pangram-ledger.jsonl`.

1. **When Joel sends the recheck's results** (or loads them into the app's browser): on each feed page, run
   `tools/humanization/pangram_feed_read.js` and save the JSON as `fix-20261020/substack41r/RESULT-41r-a.json` and
   `RESULT-41r-b.json`. Map them (`result41/map_windows.py RESULT.json OUT.json`), score them in the ledger (`result`
   with `--key HG-whole-41r-a` and `HG-rest-41r-b`, the feed link, the shading), and explain a miss. Then check each
   installed 4.1 edit's sentences in context, and record each section's feed link in `EDITS41.json` (`section_check`).
2. **What it may show.** If an installed section reads red in context where it read Human in its small checks, that's
   a context effect: read the light green around it first (`docs/HUMANIZATION-GATE.md`). It gets a fix only with a
   specific diagnosis, within the paragraph's six tries. The section recheck on pangram.com (one left for HG15 and
   HG35) is for a localized repair after that.
3. **Waiting on Joel**: questions 2 to 4 (the as-published sections), 6 (repeats), 7 (a third whole-guide check), 8
   (HG15's closing pair: HG15-p9 has used 2 of 6 tries, both of one mechanism; don't try it again without his words or a
   new mechanism). The quoted promise in Appendix F (HG35-p15, 1 of 6 tries) stays as installed unless the recheck reads
   it red.
4. **The final certification** comes after his answers to 2 to 4, as a third whole-guide check, which needs his yes
   (question 7).

## Next step (2026-10-20, after Joel's 22:01 message: the whole guide's first 4.1 check)

0. **The whole-guide 4.1 check** (question 5 settled: option b through Substack). The copy page
   `fix-20261020/substack41/COPY-TO-SUBSTACK-HYPNOSIS-CHECK.html` went to Joel at about 22:35 UTC with the request; the
   prediction is `HG-whole#1` in the ledger (key `HG-whole-41a`, text `WHOLE-GUIDE-41.txt`). When he says it ran:
   1. Look for it in his Pangram History (free; `pangram_page_helpers.js`'s History reads, or
      `https://web.pangram.com/api/history-list/` and `/api/history/<uuid>/` from the dashboard tab). If it's there, save
      the readout (every window, label and confidence) as `fix-20261020/substack41/RESULT-41a.json`; if not, his
      screenshot or link.
   2. Score it: `pangram_ledger.py results` (or `result` by key) and `explain` the miss if it is one; compare the red
      and light-green sentences with the risk read (`fix-20261020/risk41/RISK-SUMMARY.md`, `RISK-ITEMS.json`, written
      before the result was read) and record how many it caught.
   3. Fix only what reads red (and light green carrying one of 4.1's patterns), section by section from the sections'
      `installed` files: each paragraph within its six tries on pangram.com, each try with a diagnosis in the ledger,
      the gate (march, cold read, grounding, stance, lint) and the meaning kept; then the section check.
   4. The recheck through the same Substack draft (a new copy page from the fixed working copy).
   The four open sections (questions 1 to 4) stay as published until Joel answers.

## Next step (2026-10-18, after batch 466g)

From `fix-20261018/`; `STATUS.md` has the results and `OWNER-QUESTIONS.md` the decisions that are Joel's. Every section
that isn't a question for him is done: 36 of 40 (33 installed with every paragraph checked alone, three Human as
published). Nothing is left to run until he answers.
1. **HG31** reads Human whole and in every paragraph as `rf-z/HG31.v3.json` (458g), without two of its triage fixes (B25's
   examples, B28's "never hide a demand"). Install it only when Joel answers question 3 with (a); with (b), the fixes stay
   and its Pattern 4-6 window needs another way (457g: B28's fix reads AI in any wording tried so far; try the fast path's
   one new run over B25-B34 from the published text).
2. **HG17 and HG18** (question 4): wait for Joel. HG18: `rf-zf/HG18.smp1.json` (463g's HG18-wb, one run of the whole
   section from the published text, with two triaged safety fixes, C and F of `make_b465.py`) reads 100% Human whole and in
   every paragraph (466g); with (d) install it (`tools/install_fixed.py install HUMANIZED-SO-FAR.md
   fix-20261018/rf-zf/HG18.smp1.json`, then its line in `installed.json`). The other fixes (A, B, G) each brought an AI
   window back at the end (465g, 466g). HG17's script loses 11 to 31 steps in every Emulate version that reads Human, and
   its two-hand and sleep inductions read AI in the 459g screens too: the fast path (one run over the whole section, three
   samples) is the next thing to try if Joel wants (b).
3. **HG32** (question 2): wait for Joel.
4. **The merge** (question 1): when Joel says the 28 September editor HTML is the latest (or pastes a newer one), merge
   `HUMANIZED-SO-FAR.md` into it with the clipboard helper, as for the community article.
5. **To reinstall a section**: `tools/install_fixed.py install` replaces published blocks, so a section that is already in
   the article is reinstalled by rebuilding the article from `source/published-20260928.md` with every `fixed` file in
   `fix-20261018/installed.json` (462g: HG36; the rebuild with the old list reproduced the article exactly).
6. Keep `STATUS.md`, this note, the laptop copy and the scorecard page current after every batch.
