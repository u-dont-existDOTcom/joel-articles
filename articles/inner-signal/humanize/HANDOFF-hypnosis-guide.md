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
  were merged; pull request 219 (to 2026-10-22 22:05 UTC) was merged at 22:16 UTC, and 222 after it; pull requests 224, 228,
  232 and 236 were merged (228 by Joel at 2026-10-23 18:09 UTC, 232 and 236 on 2026-10-24); the work since is in the pull request the newest "Next step" names. Main moves often (the Inner
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

**Re-run before rewording (Joel, 2026-10-23 12:30 UTC: "you can take text emulate gives which doesn't pass, and re-run it,
and then it can pass"; E235).** When Emulate's text (with my meaning fixes) reads AI, run it through Emulate again, put
back only what a sample drops, and check; question 14's seam passed that way on its first check after six versions of mine
failed. On a published article's flagged paragraphs Emulate goes first (E237); for citation-dense text, splice only the red
sentence from a sample of the paragraph and keep his lines and links (Nibbāna's n2).

## Waiting on Joel

Nothing for the guide: no open questions (1 to 14 are answered).

Nibbāna (`articles/nibbana/humanize/OWNER-QUESTIONS.md`): no open questions; his paste with the clipboard helper (the
23:40 turn's file, `Nibbana-COPY-TO-SUBSTACK-20261024b.html`; N5, the meme, he decides as he pastes).

Pull requests 236 and 237 were merged on 2026-10-24 and 25; this lane has nothing waiting to merge. The community lane's
newest pull request is in its own handoff.

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

## Next step (2026-10-24, after Joel's message of 23:40 UTC: N7 in; Nibbāna's helper is with him)

His message, word for word: `fix-20261024/joel-20261024-2340-message.txt` (also in Nibbāna's `fix-20261024/` and the
community article's `candidate/joel-20261024/`): "n7a", and the community article's 65. Done (in pull request 237):
- **N7 A as batch n9** (`articles/nibbana/humanize/fix-20261024/n9/answers_2340.py`, called by `n1/install_n1.py` after n8;
  record `EDITS-n9.json`): "The later Buddhist text *Milindapañha* ...", the one word changed, the link and italics kept.
- **The helper rebuilt** (`fix-20261024/helper/make_helper.py`, which now checks the n8 paragraphs as later answers left
  them): `exports/COPY-TO-SUBSTACK.html` 5444c935..., verify and the interaction test pass; sent in chat as
  `Nibbana-COPY-TO-SUBSTACK-20261024b.html`, replacing the 19:52 turn's file. If he pasted the earlier one, he changes the
  one word in his post.
- Delegations: none.

Next: as in the step below (when he says he has pasted, read his post against the working copy; then the guide's clarity
check, all four parts, with the InnerSignal protocol loaded in the main thread first).

## Earlier next step (2026-10-24, after Joel's message of 19:52 UTC: Nibbāna's helper is with him; N7 on him)

His message, word for word: `fix-20261024/joel-20261024-1952-message.txt` (also in Nibbāna's `fix-20261024/` and the
community article's `candidate/joel-20261024/`): the eighth recheck's link ("altho i don't think it was worth doing that
recheck since now we are making lots of edits to it"), his N6 picks with a note on 5, his GPT edit of Nibbāna ("i had GPT
apply all the nibbana cuts for you to save your credits, and it also fixed some other ai tells it saw, i checked the output
and it's 100% human on pangram. so save the result", three attachments in Nibbāna's `fix-20261024/gpt/`), and the
community article's 64. Done (in pull request 236):
- **Recheck 8 read** (`articles/nibbana/humanize/fix-20261023/recheck8/`: WINDOWS.txt a5e11c2c..., META.json, RESULT.json,
  SCORE.md): Human Written, 0 of 110 windows AI; forecast 55 of 55 (Brier 0.003); NB-whole#30 a miss (I called AI at 0.24,
  explained as pessimism).
- **His GPT edit saved as batch n8** (`fix-20261024/n8/gpt_2024.py`, called by `n1/install_n1.py` after n7; record
  `EDITS-n8.json`): 40 paragraphs (his 13 N6 cuts, GPT's edits in 23, its ten style edits), put into his editor HTML word by
  word so links and italics stay; `gpt/diff_gpt.py` lines GPT's text up with ours, and `gpt/REVIEW.md` is my read of every
  change (each keeps his meaning). N6's answers item by item: `fix-20261024/N6-ANSWERS.json`.
- **Tag order fixed:** `fix-20261023/n6/emulate_n6.py`'s `_Inline` had written four of his `<a><em>` as `<em><a>`; it now
  keeps the order tags opened in (as `tools/humanization/html_text_edit.py`, the shared version, with a test), and the
  working copy was rebuilt: same text, same tags, his order.
- **The clipboard helper for his post** (`articles/nibbana/exports/`, built by `fix-20261024/helper/make_helper.py` with the
  canonical generator, against recheck 8's helper): `COPY-TO-SUBSTACK.html` df57b0be..., four parts and three manual video
  steps, verify and the interaction test pass, all 40 n8 paragraphs in their new form; `HELPER-RECEIPT-20261024.json`.
  Sent to him in chat. His steps are on the questions page: replace the text between his videos part by part (the videos
  stay), the gallery near the end comes in as single pictures with its caption as a line, and N5 he decides as he pastes.
- **N7** (new): "The later Buddhist philosopher Milindapañha" (a book); my pick A, "The later Buddhist text
  *Milindapañha*".
- **Lessons** E256 (a recheck waits for answers that would change the text) and E257 (a qualifier that carries a point
  stays; his N6 and 64 answers are examples in `tools/humanization/caveat_examples.json`); E258 and E259 are the community
  lane's (the After shows the change; "isn't proof of / doesn't prove").
- Delegations: none.

Next:
1. **When Joel says he has pasted**: read his post's text (the published page or his editor HTML) against the working
   copy's text, and put N7's word in if he answered. If he changed the post on Substack after 2026-10-22, merge his edits
   with `tools/humanization/substack_merge.py` before he pastes anything.
2. **The guide's clarity check, all four parts** (clarity, the reader's edit, caveats, repeats; `docs/CLARITY-READ.md`), as
   in the step below. Load the InnerSignal therapy protocol in the main thread first (`load_therapy_protocol`), since the
   guide touches inner-child work; it can't be loaded from a subagent.

## Earlier next step (2026-10-23, after Joel's message of 23:28 UTC: Nibbāna's eighth recheck waits on his Brave; N6 on him)

His message, word for word: `fix-20261023/joel-20261023-2328-message.txt` (also in Nibbāna's `fix-20261023/`): "recheck
nibbana" with recheck 7's link. Done:
- **Nibbāna's seventh recheck read** (`articles/nibbana/humanize/fix-20261023/recheck7/`: WINDOWS.txt 776ddb0c..., META.json,
  RESULT.json from DRAFT-TEXT.txt a56e5aaf..., SCORE.md): Human Written, 0.39% AI, 2 of 114 windows AI (67 Low, 68
  Medium): the first two sentences of his unchanged "Part of the problem is that the Buddha ..." paragraph, light green
  in recheck 6. All four of batch n6's splices and his kept "I used to attribute ..." and "So enlightenment ..." read
  Human. NB-whole#29 right (Mixed); forecast 64 of 65, the miss that light green window at 0.02.
- **Emulate round 5** (laptop `emu-hg-cd` to `emu-hg-cf`, `n7/BUNDLE5.json`; about 52,970 words left) and **batch n7**
  (`n7/emulate_n7.py`, called by `n1/install_n1.py` after n6; record `EDITS-n7.json`): the two red sentences from sample
  cf, with four fixes of mine in "mine"; a fresh Sonnet reader (`REVIEW.md`) found "pull either away and the other falls"
  lost and "I think" a new hedge, both fixed (`TRIAGE.json`; E255).
- **Nibbāna recheck 8** (`recheck8/`): built (payload f060657e..., DRAFT-TEXT 6a0f5ae0..., 15,875 words), CHANGED.json (1
  part), FORECAST.json (55 parts, 24% no red), NB-whole#30 (AI at 0.24), pasted into draft 221726541 at commit 02d2a8cc
  (caption deleted), rendered text = DRAFT-TEXT.txt with `tools/humanization/substack_rendered_check.js` (new: the walk
  every recheck used, now a file).
- Delegation: one Sonnet splice reader (triaged by me).

Next:
1. **When Joel sends Nibbāna's eighth recheck link**: as for recheck 7 (`pangram_feed_read.js` compact, WINDOWS.txt,
   META.json, RESULT.json from DRAFT-TEXT.txt 6a0f5ae0..., the ledger result for NB-whole-n8, `part_forecast.py score`).
   If the new sentences read red again, Emulate's other samples (cd, ce) are there; or ask him (his words, or keep the
   red). If it reads with no red: the clipboard helper for his post (item 4 of the step below), with N6's picks in first.
2. **N6** and 3. **the guide's clarity check, all four parts**: as in the step below.

## Earlier next step (2026-10-23, after Joel's message of 22:29 UTC: Nibbāna's seventh recheck waits on his Brave; N6 on him)

His message, word for word: `fix-20261023/joel-20261023-2229-message.txt` (also in Nibbāna's `fix-20261023/` and the
community article's `candidate/joel-20261023/`, with GPT's reply to my community review beside it): N5 ("i'll look at it
later when youu give me the clipboard helper"), "did we already look at whether there's too much safety language in this
article? ... same question for community and hypnosis articles", Nibbāna's sixth recheck link, and his community answers.
Done:
- **Nibbāna's sixth recheck read** (`articles/nibbana/humanize/fix-20261023/recheck6/`: WINDOWS.txt 3571d0fb..., META.json,
  RESULT.json, SCORE.md): Mostly Human Written, 1.1% AI, 6 of 121 windows AI, all Low, next to his N4 15 and 16 moves, and
  one unchanged sentence. NB-whole#28 right; forecast 87 of 92, the misses the moves' neighbours at 0.05 (E249 worked as
  designed: they had their own parts) and one light green window.
- **Emulate round 4** (laptop `emu-hg-ca` to `emu-hg-cc`, `n6/BUNDLE4.json`; about 54,150 words left) and **batch n6**
  (`n6/emulate_n6.py`, called by `n1/install_n1.py` after n5; record `EDITS-n6.json`; inline markup kept by position, so
  links and italics outside a spliced sentence stay where they were): the awareness sentence (ca), the MN 75 sentence (ca),
  the next question (cb), the lucid-dream sentences (cc, with the reader's two fixes); his "I used to attribute ..." and
  "So enlightenment isn’t a simple bliss switch." kept. Reviewed by a fresh Sonnet reader (`REVIEW.md`), triaged
  (`TRIAGE.json`).
- **Nibbāna recheck 7** (`recheck7/`): built, CHANGED.json (6 parts), FORECAST.json (65 parts, 4% no red), NB-whole#29 (AI
  at 0.04), pasted into draft 221726541 (caption deleted), rendered text = DRAFT-TEXT.txt (a56e5aaf...).
- **The caveat read, part 3 of `docs/CLARITY-READ.md`** (E252): `clarity_read.py make --kind caveats`, examples
  `tools/humanization/caveat_examples.json` (from the Inner Child lane's turn-102 pass on its branch
  `handoff/claude-dangerous-adult-20260924-1631`, `experiments/t102-safety/`), a test. Run on Nibbāna
  (`fix-20261023/caveats/`: six Sonnet readers, 25 lines, my picks in ITEMS.json, `CAVEATS.md` is question N6) and the
  community article (that lane's handoff).
- **The repeats read, part 4** (E253): `clarity_read.py make --kind repeats` (each reader reads the whole article and owns
  one part's points), a test; first run on the community article.
- **E254** (GPT's reply to my community review). The next lesson is E255.
- Delegation: twelve Sonnet caveat readers and one Sonnet splice reader (all checked by me against the whole article).

Next:
1. **When Joel sends Nibbāna's seventh recheck link**: as for recheck 6 (`pangram_feed_read.js` compact, WINDOWS.txt,
   META.json, RESULT.json from DRAFT-TEXT.txt a56e5aaf..., the ledger result for NB-whole-n7, `part_forecast.py score`).
   If his "I used to attribute ..." reads red again, it goes to him (his own rewrite, or keep the red).
2. **N6**: put in his picks from `fix-20261023/caveats/ITEMS.json` (each cut exactly the struck words; the page's
   "After" is the paragraph after the cut), as a batch module called by `install_n1.py`, then the next recheck.
3. **The guide's clarity check, all four parts** (reread list, reader's edit, caveats, repeats): about 29,500 words. It
   reviews his inner-child writing, so the InnerSignal server's instructions apply: load the therapy protocol in the main
   thread first (`load_therapy_protocol`) and follow it; loading it from a subagent was refused once, so don't route it
   through one. Then the parts (`clarity_read.py make HUMANIZED-SO-FAR.md DIR --kind ... --parts 8`), fresh readers,
   `collect`, every item checked against the whole guide, `page`, his questions.
4. **When Nibbāna reads Human:** the clipboard helper for his post (`project-sources/substack_transfer_helper.py.txt`
   from the working copy), with N5 for him to decide there.

## Earlier next step (2026-10-23, after Joel's message of 20:35 UTC: Nibbāna's sixth recheck waits on his Brave; N5 on him)

His message, word for word: `fix-20261023/joel-20261023-2035-message.txt` (also in Nibbāna's `fix-20261023/` and the
community article's `candidate/joel-20261023/`): Nibbāna's fifth recheck link ("nibbana check 5"), part B's recheck link
("guide part b recheck"), his N4 answers ("N4 1a 2 b 3a 4 a 5a 6a 7a 8a 9a 10a 11a 12a 13a 14a 15a 16a 17a 18a"), and a
review of GPT's suggestions for the community article (that lane's handoff). Done:
- **Part B's recheck read** (`fix-20261023/recheck-b2/`: WINDOWS-B.txt 1da99bef..., META-B.json with the card line in
  "embeds", RESULT-B.json, SCORE.md): Mostly Human Written, 1.3% AI, 1 of 36 windows AI, the audit he kept (2c).
  HG-rest-B#59 right. Forecast 51 of 51, Brier 0.004. **The whole guide reads Human outside that audit** (part A: recheck
  A4, 100% Human).
- **Nibbāna's fifth recheck read** (`articles/nibbana/humanize/fix-20261023/recheck5/`: WINDOWS.txt f01813a6...,
  META.json, RESULT.json, SCORE.md): Mostly Human Written, 0.7% AI, 4 of 127 windows: "That creates a practical
  problem." (Low), the DN 3 sentence (Medium), the stage-map question (Low), and the room's "They were disjoint, but not
  isolated: ..." to "There was no cosmic knower celebrating its achievement." (Low). NB-whole#27 right; forecast 71 of 74.
- **N4 in** (`articles/nibbana/humanize/fix-20261023/n5/joel_2035.py`, called by `n1/install_n1.py` after batch n4;
  record `EDITS-n5-joel.json`): 17 changes word for word, 2 left out. New headings take the level of the heading of the
  section they split (as proposal 18 says; peers in the table of contents), not one level below as the earlier next step
  said. Pictures beside two moves: the skydiving meme moved with the caution (17); the nuggets meme stayed (14, question
  N5). His answers added to `tools/humanization/readers_edit_examples.json` (the four B-to-A and his B).
- **E250** (a past answer covers only what its reason covers) and **E251** (a reader's move carries pictures the reader
  didn't see) in `docs/HUMANIZATION-GATE.md`; the next lesson is E252.
- **Emulate round 3** (laptop `emu-hg-bx` to `emu-hg-bz`, `n5/BUNDLE3.json`; about 55,200 words left): the DN 3 stretch
  with 12A's structure and the room paragraph. The first launch passed a relative output folder and failed before any call
  (nothing charged); `run_emulate.py` needs the absolute folder.
- **Nibbāna batch n5** (`n5/emulate_n5.py`, record `EDITS-n5.json`): bz's "That leads to a practical problem.", bz's DN 3
  sentence (its added "In several suttas, most notably" cut), bx's question ("to the answer" put back), bz's room
  sentence ("connected everywhere" put back); his "Nothing observed them from behind. There was no cosmic knower
  celebrating its achievement." kept. Reviewed by a fresh Sonnet reader (`REVIEW.md`), triaged (`TRIAGE.json`).
- **Nibbāna recheck 6** (`recheck6/`): built, CHANGED.json (13 parts), FORECAST.json (92 parts, 1% no red), NB-whole#28
  (AI at 0.01), pasted into draft 221726541 (caption deleted), rendered text = DRAFT-TEXT.txt (f5c918c2...); the nested
  MN 89 note and all 60 headings were in the editor.
- Pull request 230 was merged by Joel; this turn's work is pull request 231
  (https://github.com/u-dont-existDOTcom/joel-articles/pull/231), his to merge.
- Delegation: one Sonnet reader for the splices (checked by my triage).

Next:
1. **When Joel sends Nibbāna's sixth recheck link**: read it with `pangram_feed_read.js` in compact mode, save
   `recheck6/WINDOWS.txt` (check its SHA-256), META.json, rebuild RESULT.json from DRAFT-TEXT.txt (f5c918c2...) and the
   windows as in recheck5, record NB-whole-n6's result, score `recheck6/FORECAST.json`. If the room's sentences or the DN 3
   stretch read red again, ask him (his words, Emulate's best, or keep the red); other red: Emulate first (E237, E244).
2. **N5**: A leaves the meme where it is; B moves it after the monk's paragraph (in `n5/joel_2035.py`, item 14).
3. **The guide's clarity read**, both parts, with the reader's edit (E242, E248): the guide is about 29,500 words, so use
   about eight parts of each kind (`clarity_read.py make HUMANIZED-SO-FAR.md DIR --parts 8`, and `--kind edit
   --max-items 3` in a second folder). It reviews his inner-child writing, so per the InnerSignal server's instructions
   the therapy protocol is loaded first in the main thread (`load_therapy_protocol`); loading it from a subagent was
   refused once, so don't route it through one. Then a fresh Sonnet reader per part, `collect`, every item checked against
   the whole guide, `page`, and his questions.

## Earlier next step (2026-10-23, after Joel's message of 18:13 UTC: part B's recheck and Nibbāna's fifth recheck wait on his Brave; N4 on him)

His message, word for word: `fix-20261023/joel-20261023-1813-message.txt` (and in Nibbāna's `fix-20261023/`), with GPT's
reply of 11:41 UTC that he attached (`gpt-readability-20261023-attachment.txt` beside it): recheck A4's and Nibbāna's
fourth recheck's links; "how does "tellingly" or "it's pretty clear that" put "me " in the explanation? same for removing
sumup line that's not putting me in. local mirror shop also not me."; "the clarity check for articles should also include
the readability check from GPT that i started doing in the inner child article". Done:
- **Recheck A4 read** (`fix-20261023/recheck-a4/`: WINDOWS-A.txt 4332e646..., META-A.json, RESULT-A.json): Human Written,
  0% AI, 108 windows Human. HG-whole#58 was a miss (AI at 0.12), explained ("pessimism about Emulate's whole-stretch
  re-run"). Forecast `SCORE.md`: 52 of 52, Brier 0.008.
- **Nibbāna's fourth recheck read** (`articles/nibbana/humanize/fix-20261023/recheck4/`, WINDOWS.txt 6cf900d2...): Mostly
  Human Written, 1.1% AI, 5 of 132 windows. NB-whole#26 right. Forecast 104 of 107, Brier 0.034; misses: my Soh gloss,
  "It sounds abstract, ...", the preservation stretch, and the unification paragraph in the rest (E249).
- **E247** (his question): E241 now lists his clarity rewrites' moves by what the words do; `docs/CLARITY-READ.md` and the
  Nibbāna questions page say the same.
- **E248, the reader's edit:** part 2 of `docs/CLARITY-READ.md` (GPT's five questions, his Inner Child answers 91.1 to 91.4
  as examples), `tools/humanization/clarity_read.py make --kind edit` (brief, collect and page for proposals; examples in
  `tools/humanization/readers_edit_examples.json`; tests), the working order's step 5.4, the declared gate, `docs/INDEX.md`.
  Run on Nibbāna (`articles/nibbana/humanize/fix-20261023/readers-edit/`): question N4.
- **E249:** `tools/humanization/part_forecast.py make` adds each changed part's neighbours itself (0.05 each;
  `--no-neighbours`), with a test.
- **Emulate, rounds br to bw** (laptop `emu-hg-br` to `emu-hg-bw`; bundles `n4/BUNDLE.json` and `BUNDLE2.json`, the same
  in `fix-20261023/b477/`; about 55,800 words left): three samples a round of each red paragraph; round 2's unification
  paragraph tied to the senses (NB-unif2).
- **Nibbāna batch n4** (`articles/nibbana/humanize/fix-20261023/n4/emulate_n4.py`, called last by `n1/install_n1.py`;
  record `EDITS-n4.json`): the definition from bu, "As you can see ..." from bv, the preservation sentences from br and bt,
  each with logged fixes ("mine"), Soh's sentence back to his words; "That creates a practical problem." kept (his).
  Reviewed by a fresh Sonnet reader (`REVIEW.md`), triaged (`TRIAGE.json`: three meaning fixes).
- **Guide batch 477** (`fix-20261023/b477/EDITS-b477.json`, in EDITS41): recheck B's red line from br.
- **Nibbāna recheck 5** (`recheck5/`): built, CHANGED.json (6 parts) and FORECAST.json (74 parts, 5% no red),
  NB-whole#27 (AI at 0.05), pasted into draft 221726541 (caption deleted), rendered text = DRAFT-TEXT.txt (5df5b089...).
- **Guide part B recheck** (`fix-20261023/recheck-b2/`): built, CHANGED.json (10 parts, the kept audit at 0.9),
  FORECAST.json (51 parts), HG-rest-B#59 (AI at 0.01), pasted into draft 221412532; rendered text, the card's line left
  out, = TEXT-B.txt (b4a57231...).
- **Nibbāna's reader's edit** (`articles/nibbana/humanize/fix-20261023/readers-edit/`): six fresh Sonnet readers, a sixth
  each (the first three, a third each, spent all their output thinking and were stopped); 19 proposals, two of them
  artifacts of the reading text (fixed in the tool: line breaks kept, images and videos marked), one added from my
  check (the "That creates a practical problem." heading); `ITEMS.json` has my pick and reason for each,
  `READERS-EDIT.md` is the list (question N4: 18 proposals, 13 picked A).
- Pull request 228 was merged by Joel at 18:09 UTC; this turn's work is pull request 230
  (https://github.com/u-dont-existDOTcom/joel-articles/pull/230).
- Delegation: one Sonnet reader for the splices (checked by my triage), six Sonnet readers for Nibbāna's reader's edit
  (checked by me against the whole article).

Next:
1. **When Joel sends Nibbāna's fifth recheck link**: read it with `pangram_feed_read.js` in compact mode, save
   `recheck5/WINDOWS.txt` (check its SHA-256), META.json, rebuild RESULT.json from DRAFT-TEXT.txt (5df5b089...) and the
   windows as in recheck4, record NB-whole-n5's result, score `recheck5/FORECAST.json`. Red on "That creates a practical
   problem." again: ask him, with bv's "There's also a practical problem." as an option. Other red: Emulate first on the
   paragraph it covers (E237, E244).
2. **When he sends part B's**: the same in `recheck-b2/` (`substack_check_text.py result recheck-b2/PAYLOAD-B.html
   WINDOWS-B.txt META-B.json --out RESULT-B.json`, text b4a57231...), key HG-rest-B-b477, score its forecast. The audit
   questions read red by his 2c.
3. **N4** (Nibbāna's reader's edit): put in what he picks word for word (a new heading one level below its section's, an
   existing heading moved as he picks), add his answers to `tools/humanization/readers_edit_examples.json`, and read each
   move's stretch in the next recheck (a move keeps its paragraphs' checks; E241 (Inner Child): read new neighbours for a
   repeat first).
4. **The guide's clarity read**, both parts, with the reader's edit, once part B reads Human outside the audit (E242,
   E248).

## Earlier next step (2026-10-23, after Joel's message of 16:55 UTC: recheck A4 and Nibbāna's fourth recheck wait on his Brave)

His message, as recorded (the raw text was lost to a context compaction; its parts are word for word):
`fix-20261023/joel-20261023-1655-message.txt` (and in Nibbāna's `fix-20261023/`): recheck A3's link; Nibbāna's third
recheck's link with the one red span and his fix of it; his answers 1 to 30 to the clarity list; "learn some pangram
lessons."; "let's make sure this kind of check is standard for articles as we write them and as we finalize before
publishing in future, i thought it already was". Done:
- **Recheck A3 read** (`fix-20261023/recheck-a3/`: WINDOWS-A.txt, META-A.json, RESULT-A.json; text e21fc7a8...): Mostly
  Human Written, 1.1% AI, 7 windows, all in Come all the way back (83 to 88, 93). HG-whole#56 right. Forecast scored
  (`SCORE.md`: 31 of 33, Brier 0.071; the red spread from the changed check paragraph into the script's end and the Note).
- **Nibbāna's third recheck read** (`recheck3/`, text b99bb0b6...): Human Written, 0.34% AI, 2 windows on the photon
  paragraph. NB-whole#25 right. Forecast 68 of 70, Brier 0.028.
- **Nibbāna batch n3** (`articles/nibbana/humanize/fix-20261023/n3/joel_1655.py`, called last by `n1/install_n1.py`; its
  record `EDITS-n3.json`, 36 edits): his photon fix and his words for 14 items, the 14 plain versions he passed (two
  changed: 2's saṃsāra gloss cut, 23's "realize" back), the four snags (mine), saṃsāra defined at its first mention and
  the rebirth paragraph made a reference. All 269 links kept; three italics dropped where his words changed (listed).
- **Nibbāna recheck 4** (`recheck4/`): built, CHANGED.json (36 parts) and FORECAST.json (107 parts) before the paste,
  NB-whole#26 (AI at 0.06), pasted into draft 221726541 (caption deleted), rendered text = DRAFT-TEXT.txt (7c8dc8b0...).
- **Guide batch 475** (`fix-20261023/b475/`): Emulate on the whole red stretch, script to Note (samples bo, bp, bq on the
  laptop, `emu-hg-bo` to `bq`, 1,272 words; 57,897 left); bp and bq changed person (a hypnotist's voice), so the splices
  are bo's (script's end, the line after the count, the Note) and bp's count up, with meaning fixes from master.html;
  the second reader (Sonnet, `REVIEW.md`), the triage (`TRIAGE.json`: two fixes, six let stand with reasons); four
  EDITS41 edits. No API check (Low and Medium red, E226; HG18-B311 keeps its two tries).
- **Guide batch 476** (`fix-20261023/b476/`): Emulate's misspellings and British spellings back to the published spelling,
  one edit per paragraph (25), E246. `apply_edits41.py`'s `superseded()` now accepts a chain whose text is in the working
  copy at any step (batch 475 changed text that 472 and 474 had produced).
- **Recheck A4** (`fix-20261023/recheck-a4/`): built, forecast (52 parts, 8% no red), first pasted without batch 476, then
  HG-whole#57 voided (never sent), rebuilt with 476, HG-whole#58 (AI at 0.12), pasted again into draft 221411215; its
  rendered text's first 99,999 characters = TEXT-A.txt (b3b63a02...).
- **The clarity read made standard** (E242): `docs/CLARITY-READ.md`, `tools/humanization/clarity_read.py` (make, collect,
  page; `tests/test_clarity_read.py`, no packages needed), `tools/humanization/clarity_examples.json` (his fixes as the
  briefs' examples), the working order's section 5 (`docs/FIXING-AN-ARTICLE.md`), a declared gate in the gate, and
  `docs/INDEX.md`.
- **The feed reader fixed** (E245): `tools/humanization/pangram_feed_read.js` finds the props from the main elements when
  the text-segment spans are gone, and has a compact mode (`window.__feedMode = 'compact'`).
- Lessons E241 to E246 (`docs/HUMANIZATION-GATE.md`), the Emulate page's noise step (`docs/EMULATE-FALLBACK.md`).
- Pull request 224 was merged by Joel at 15:33 UTC; this turn's work is on the same branch, in pull request 228
  (https://github.com/u-dont-existDOTcom/joel-articles/pull/228), with main merged in (the gate's lessons of both lanes kept).
- Delegation: one Sonnet subagent (the second reader of batch 475), checked by my triage.

Next:
1. **When Joel sends recheck A's link**: read it in the app's browser with `pangram_feed_read.js` in compact mode
   (`window.__feedMode = 'compact'`; save `window.__compact` as `recheck-a4/WINDOWS-A.txt` and check its SHA-256 against
   the page's), write META-A.json, rebuild with `substack_check_text.py result recheck-a4/PAYLOAD-A.html WINDOWS-A.txt
   META-A.json --out RESULT-A.json` (text b3b63a02...), record HG-whole-41r7b-a, and score `recheck-a4/FORECAST.json`.
   Any red in the return section again: Emulate on the paragraph it covers, with its neighbours (E244); ask him after
   the third try on the same stretch.
2. **When he sends Nibbāna's**: the same in `recheck4/` (DRAFT-TEXT.txt 7c8dc8b0... is the text; inline rebuild as in
   recheck3), key NB-whole-n4, then its forecast's score. Red on his own words goes to him; red on a plain version he
   passed goes to Emulate (splice only the red sentence, keep his lines and links), then to him.
3. Part B's Low line ("You don't have to fix this. I'm here now.", window 17 of recheck B) stays next for B, Emulate
   first; part B also has batch 476's spellings, so its next recheck reads them.
4. The clarity read for the guide itself (E242: "after a large batch of changes"), once part A reads Human: `clarity_read.py
   make` on the working copy, three fresh readers, then his list.

## Earlier next step (2026-10-23, after Joel's message of 14:14 UTC: recheck A and Nibbāna's third recheck wait on his Brave; N3 on him)

His message, word for word: `fix-20261023/joel-20261023-1414-message.txt` (and in Nibbāna's `fix-20261023/`): pull request
224's conflict again; recheck A's link; "i was thinking you should predict which part comes back as AI?"; Nibbāna's second
recheck with "one tiny ai segment" and his own fix of it; "is there any other stuff in the nibbana guide that's hard to
understand but still passing pangram?" Done:
- The conflict (the gate's lessons, the Inner Child lane's E228 to E231 against this lane's) resolved by keeping both with a
  numbering note; the universal scorecard rebuilt from the merged ledgers (94de6f15).
- Recheck A read (`fix-20261023/recheck/RESULT-A.json`, its text e27356d7..., the page's): Mostly Human Written, 1.4% AI,
  7 of 108 windows: the shortcut paragraph from the driving caution's second sentence (83 to 86, Low and Medium), the
  return's check (93, Low), Nothing happens' lines and It feels fake's question (102 and 103, Low and Medium, humanized).
  HG-whole#52 right. That folder stays as the record; the next part A is `fix-20261023/recheck-a3/`.
- Nibbāna's second recheck read (`recheck2/RESULT.json`): "Human Written", 0.27% AI, 2 windows on one paragraph, which he
  rewrote; his fix is in through `n1/install_n1.py` (`joel_1414`, 13 edits). The ledger read a "Human Written" headline as
  100% Human and refused Mixed; `verdict_of` now goes by the fraction or the windows (E239). NB-whole#24 right.
- **Batch 474** (`fix-20261023/b474/`): Emulate on all three stretches (`bl/`, `bm/`, `bn/`), only the red sentences spliced
  (`CANDIDATES.json`), each Human through the API (`API-CHECKS.md`; lineages HG17-drive-seam, HG18-B311 try 4, HG24-trouble),
  the reader (`REVIEW.md`) and its triage (`TRIAGE.json`: three fixes), installed as six EDITS41 edits (`make_b474.py`).
- **Part forecasts** (E238, `tools/humanization/part_forecast.py`, `tests/test_part_forecast.py`): `make` before the paste
  (CHANGED.json with my chances, the last check's Low and Medium windows at the measured rates), `score` after. Both new
  rechecks have one (`recheck-a3/FORECAST.json`: 13% no red; `recheck3/FORECAST.json`: 28%), with the whole-article
  predictions HG-whole#56 and NB-whole#25 at those chances.
- **The clarity read** (`articles/nibbana/humanize/fix-20261023/clarity/`): three Sonnet readers, a third each
  (`BRIEF-*.txt`, `READER-*.md`), checked by me against the whole article (`ITEMS.json`): 29 passages, 12 hardest, on
  `CLARITY.md`; question N3.
- Both rechecks pasted and verified (`recheck-a3/RECHECK-POST-A.json`, `recheck3/RECHECK-POST.json`). Lessons E238 to E240.
- Delegation: four Sonnet subagents (three clarity readers, one second reader), each one Read and one Write, all checked by me
  (the clarity flags against the whole article, the reader's findings by triage).

Next:
1. **When Joel sends recheck A's link**: read it as before (compact windows line, its SHA-256 against the page's), rebuild
   with `substack_check_text.py result recheck-a3/PAYLOAD-A.html WINDOWS-A.txt META-A.json --out RESULT-A.json` (text
   e21fc7a8...), record HG-whole-41r6-a, and score the forecast: `part_forecast.py score recheck-a3/FORECAST.json
   recheck-a3/RESULT-A.json --out recheck-a3/SCORE.md`. Any red: Emulate again on the whole stretch it covers (E235, E240).
2. **When he sends Nibbāna's**: the same in `recheck3/` (text b99bb0b6...), key NB-whole-n3, then its forecast's score.
3. **N3**: on A or C, rewrite the passages in his way (E236), each through the API, the reader, then a recheck with a part
   forecast; on B, take his words in word for word.
4. Part B's Low line (window 17) stays next for B, Emulate first.

## Earlier next step (2026-10-23, after Joel's message of 12:30 UTC: recheck A and Nibbāna's second recheck wait on his Brave)

His message, word for word: `fix-20261023/joel-20261023-1230-message.txt` (the same file in Nibbāna's `fix-20261023/`).
He asked: pull request 224 has conflicts; his two results; "it seems like you have quit using emulate, just curious? why?"
with the re-run trick; his rewrite of De-hypnosis's forces paragraph; "for the other parts you can either learn from me or
learn from emulate right?"; "n1 a."; N2 as his four rewrites. Done:
- Pull request 224's conflict (the gate's lessons of both lanes, numbered at the same time) resolved by keeping both with a
  numbering note (49b53bbf); it can merge.
- Recheck B read ([his result](https://www.pangram.com/feed/1db9825e-5fed-4528-aca5-9d4272b54f83); `fix-20261023/recheck/RESULT-B.json`,
  with `META-B.json`'s card line "Quick Triage Web-App Version HERE"): Mostly Human Written, 1.4% AI, 36 windows, two AI:
  the audit's questions (High; they stay, his answer 2c) and "You don't have to fix this. I'm here now." (Low, window 17,
  inside the inner child script; the published line is "You do not have to solve this. I am here now."). HG-rest-B#48 a
  miss, explained. Nibbāna's first recheck read too (12 AI windows; NB-whole#21 right).
- His forces paragraph in, word for word (EDITS41 HG16-joel-1230, `fix-20261023/make_joel_1230.py`; two typos fixed).
- **Batch 473** (`fix-20261023/b473/`, its `API-CHECKS.md` with each check's Pangram page): question 14's seam through his
  re-run trick (`fix-20261023/emu-seam/`, emu-hg-bi, bj, bk). Re-run bj's first paragraph, with "qualified" and "right away"
  put back, read Human, High, alone (HG17-B306#49); with re-run bk's return paragraph, Human, High, as one window (the pair's
  last try, HG18-B308#50). The reader (`REVIEW.md`) and its triage (`TRIAGE.json`) fixed two things: "You'll want to say,
  while you're awake, ..." (checked: Human, High and Medium, HG17-B306#51; the lineage has one try left) and "If you have
  met a younger state" (the published words; unchecked, the pair's lineage is used up). Installed as EDITS41 HG17-b473 and
  HG18-b473 (`make_b473.py`).
- **Nibbāna**: N1 a (try 1's science sentence), N2 (his four rewrites, his words, links put back, typos fixed) and batch n2
  (`articles/nibbana/humanize/fix-20261023/n2/`: the rebirth sentence from Emulate sample bj, Human, High, alone, NB-P228#22;
  the reader's rewrite of it read Human but split the chain into a Low window, NB-P228#23, so it stayed out; window 18
  reworded, OK by the reader) are in the working copy through `fix-20261023/n1/install_n1.py` (11 edits).
- **Both rechecks pasted and verified**: part A in draft 221411215 (`fix-20261023/recheck/RECHECK-POST-A.json`: its rendered
  first 99,999 characters hash to `TEXT-A.txt`, e27356d7...; prediction HG-whole#52, AI at 0.35); Nibbāna in draft
  221726541 (`articles/nibbana/humanize/fix-20261023/recheck2/RECHECK-POST.json`: rendered text = `DRAFT-TEXT.txt`, 0ed4d332...,
  after the gallery caption was deleted again; prediction NB-whole#24, AI at 0.15). The first Nibbāna recheck's files stay
  in `recheck/` as its record.
- Delegation (UDA's `patterns/delegate-easy-work-to-cheaper-models.md`): the two second readers were Sonnet subagents, one
  per article (one Read of `REVIEW-PROMPT.txt`, one Write of `REVIEW.md`), checked by my triage (`TRIAGE.json` in b473/
  and n2/), which checked the reader's own rewrites through the API before taking them (one in, one out).
- Lessons E234 to E237 in `docs/HUMANIZATION-GATE.md`. API checks this round ran on the laptop from
  `/home/joel/ai-work/claude-dangerous-lane/pangram-api/r20261023b/` with the repository's current `pangram_api.py`
  (fa9b21bd..., `--public` for each result's Pangram page): files go in through the connected `inbox/api-20261023b/`
  (device_commit_files only writes there), are copied over with their SHA-256 checked, and the logs come back the same way;
  one text per lineage per round (the ledger refuses a second prediction while a try has no result).

Next:
1. **When Joel sends recheck A's link**: read the windows from the page (`tools/humanization/pangram_feed_read.js`, its
   compact line), write `fix-20261023/recheck/WINDOWS-A.txt` and `META-A.json` (with any card line in "embeds"), rebuild
   with `substack_check_text.py result PAYLOAD-A.html WINDOWS-A.txt META-A.json --out RESULT-A.json` (its text must hash
   to e27356d7...), record HG-whole-41r5-a (`verdict_of`; "Mostly Human Written" is Mixed), and check windows 44 to 48, 77
   to 79, 85 and 86 of 22 October in place. Any red: Emulate re-run first (E235), then his words.
2. **When he sends Nibbāna's**: the same in `articles/nibbana/humanize/fix-20261023/recheck2/` (text 0ed4d332...;
   rebuild from the working copy with single spaces, as `make_recheck_nb.py` does), key NB-whole-n2.
3. **Part B's Low line** (window 17): an Emulate sample of its paragraph with only the script's middle spliced in, the
   reader, then recheck B (the API can't reproduce a Low window, E226).

## Earlier next step (2026-10-23 03:05 UTC: the guide's recheck B and Nibbāna's recheck wait on his Brave; questions 14, N1 and N2 on him)

The guide is as in the step below (nothing new from Joel since 01:10 UTC): items 1 to 4 there still hold. Done since then,
on his Nibbāna article (`articles/nibbana/humanize/`, its own ledger `pangram-ledger.jsonl`, lane "nibbana article" in
`tools/humanization/pangram_lanes.json`):
- Batch n1 (`fix-20261023/n1/`, its `API-CHECKS.md`): the nine High and Medium stretches of his check of 2026-10-20, three
  API rounds (ledger NB-P64#1 to NB-P266#19). Four fixes read Human, passed the reader (`REVIEW.md`) and are in the working
  copy `HUMANIZED-SO-FAR.html` (`install_n1.py`, `EDITS-n1.json`): unification, the percentages (try 2), the last test,
  rebirth. The science sentence read Human on try 1 but the reader flagged two additions, and the reader's own fix read AI
  (question N1). The near-death reports, SN 22.22 with the proton, the Diamond Sutra and the driving caution read AI in
  three tries each (question N2; E232).
- The whole-article recheck (`fix-20261023/recheck/`): `make_recheck_nb.py` (the transfer helper's four segments joined;
  the three notes travel as links and the editor rebuilt them), pasted into a new draft, 221726541 ("TEMP recheck
  (Nibbana article) - do not publish"), its rendered text equal to `DRAFT-TEXT.txt` after one gallery caption was deleted
  in the draft (`RECHECK-POST.json`; E233); prediction NB-whole#21.
- Lessons E230 to E233; both lanes' API pages now label every line of a window; `pangram_links_check.py` accepts an API
  check's heading on its `API-CHECKS.md` page as its link (`tests/test_pangram_links_check.py`).

Nibbāna's next steps:
1. **When Joel sends the Nibbāna recheck's link**: read the windows from the page (`tools/humanization/pangram_feed_read.js`,
   its compact line), and rebuild with `substack_check_text.py` on the working copy: the draft's checked text should hash
   to `DRAFT-TEXT.txt` (dfd00232...; the payload alone lacks the notes, so rebuild from the working copy and make the
   spaces single, as `make_recheck_nb.py` does). Record the ledger result for key NB-whole-n1 (`verdict_of`), check that the
   four fixes read Human in place, and list the Low windows still red for batch n2 (each fix through the API, "no worse"
   alone (E226), then the reader, then the next recheck).
2. **N1**: A, try 1's sentence goes in (`make_n1.py` E['n1-science'], add it to `install_n1.py`'s GO with its check
   n1_science, try 1); B, his word for "wild" checked through the API first (lineage NB-P237 has four tries left); C, his
   words; D, it stays.
3. **N2**: A, his words go in as he writes them (an edit each, its source his message), checked in the next recheck; B,
   tries 4 to 6 (three left for each lineage); C, they stay red.
4. API checks for Nibbāna run on the laptop from `/home/joel/ai-work/claude-dangerous-lane/pangram-api/nb-n1/`
   (`python3 pangram_api.py check TEXTS-N.json out --expect 4.1 --windows > roundN.log`; the texts as JSON written there
   and their SHA-256 checked; the log back as gzip and base64, SHA-256 checked), then `n1/record_round.py N` and
   `n1/api_page.py`.

## Earlier next step (2026-10-23, after Joel's message of 01:10 UTC: recheck B waits on his Brave, question 14 on him)

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
