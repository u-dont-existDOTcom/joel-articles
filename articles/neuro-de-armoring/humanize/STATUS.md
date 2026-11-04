# Status: neuro de-armoring humanization (newest on top)

## 2026-11-04, after Joel's message of 16:12 UTC ("you don't need me to do that"): the lane's own web-app checks; 088 in; six stretches to him; E356

His message, word for word: `fix-20261104/joel-20261104-1612-message.txt` ("you don't need me to do that, what are you
talking about? you're not following the joel-articles and pangram humanization lab rules? why not? every other lane is
doing gui checks"). **The mailbox first** ("2026-11-04 16:12"); main merged (af929000: suggestion_review.py 1.6).
HUMANIZED-SO-FAR.md is now fb288da6 (block 88 in).

- **The error, and its cause**: last turn's checks page asked him to run six checks the lane runs itself (his standing "you
  don't need my ok each time to run the GUI pangram checks"; the gate's "The web app needs Joel's sign-in"; the budget
  doc's web-app sections). The lane had run every check through the API since 2 November, its turn notes carried "never
  use Joel's browser, clipboard, cookies or profile", which nothing in the repository says (the only copy is the session's
  own summary), and the web-app rules weren't read before asking. Lesson **E356** in docs/HUMANIZATION-GATE.md (numbered
  after the gut lane's E353 to E355 in pull request 293), and last turn's AGENTS.md paragraph, which said paragraph checks
  "go to him", now says the lane runs them and how.
- **The route**: the desktop app's browser pane was signed out of Pangram (the dashboard showed "Log in" and a "Verify you
  are human" box, not ticked). Claude in Chrome was refused once by the session's safety check (acting in his browser
  without his asking), so the lane asked him which route: "Use Claude in Chrome". The dashboard in his Brave (Pangram
  Professional), `tools/humanization/pangram_page_helpers.js` `__run` (each SHA-256 checked before the click) and a
  `__readFull` read from his history by SHA-256; the tab closed after.
- **Batch x1104k** (the four second tries and the two unsent first tries; predictions of last turn): b088 read Human
  Written, 0.0% AI (Medium, High, Medium, Low; a miss in my favour), b090 AI Detected, 27.2% AI (High, Medium, AI Low on its
  last sentence), the other four AI Generated, 100% AI (`checks/x1104k/RESULTS.md`; `checks/record_gui.py` records each
  window's confidence in the ledger, ND1104-B085#80 to B091#85).
- **Batch x1104l**: one-sentence fixes of b088's Low window and b090's AI window both moved the untouched windows (b088 AI
  Detected 13.8%; b090 100% AI with its first sentence AI), and the trial in his X-84 build read 100% AI (ND1104-B088#86,
  B090#87, B091#88). E350: those stretches go to him.
- **The tell panel on the second tries** (`panel/b085-n2`, `b086-n2`, `b089-n2`, `b091-n2`) and **Codex's rewrites**
  (`rewrite-b085`, `b086`, `b089`, `b091`: `tell_panel.py rewrite-prompt` with the points to keep and the fidelity check's
  words, his own paragraphs as voice; E256 (Inner Child)), batch x1104m: b086 AI Detected, 39.4% AI (Human Medium, Low,
  Low, then AI Low on its last two sentences), the other three 100% AI (ND1104-B085#89 to B091#92). Codex's drafts were
  checked without a panel read of their own; my changes to them: straight quote marks, and for 089 "actually" out (O25) and
  its short last sentence joined (B7). The panel on b090 (`panel/b090-n1`) for its help card.
- **Block 88 in the article** (`next2/apply_b088.py`): the second try, the fidelity check passing, my comparative read
  beside his post recorded (`next2/read/`), no finding.
- **Six stretches to edit** on Neuro De-Armoring Cards, 4 November (3) (https://claude.ai/artifact/TBrnTti2G9V4fBvC357cTy,
  version 4; `cards/build_page_x1104d.py`, REVIEW-X1104D.md): Y-85, Y-86, Y-89, Y-91 (his post's paragraphs, after three
  versions read AI), Y-88 (block 88's Low window) and Y-90 (his post's paragraph, my version's one AI sentence), each ask in
  his words with the human tells named and its panel linked (`pangram_links_check.py` passes).
- **Pages**: Neuro De-Armoring Checks republished with the results ("Nothing to do here"); the questions page (version 10)
  with the 16:12 section; question 8 still open.
- **Delegations**: a Sonnet and a Haiku subagent, the panel's readers for the four second tries, then one each for b090:
  done, summarized by `tell_panel.py summarize`. Codex on the laptop (its configured model, read-only, ephemeral): the
  panel's third reader for the same five, and the four rewrites from `rewrite-prompt`, checked by the fidelity check and
  then Pangram: done (one Mixed, three AI).

## 2026-11-04, after Joel's messages of 14:42 UTC ("done continue") and 14:59 UTC (the web app's credits): six drafts, four checked and 100% AI; the API out of credits; the panel and second tries; his checks in the web app

His messages, word for word: `fix-20261104/joel-20261104-1442-message.txt` ("done continue"; pull request 290 merged at
14:41:55) and `fix-20261104/joel-20261104-1459-message.txt` ("i'm not topping up the api unless you think it's really
important because we have tons of gui credits still"). **The mailbox first** (`state/mailbox/claude-community-joel-1018.json`,
"2026-11-04 14:42"); main merged twice this turn (1b2ef3dc, then eb7496ab, a fast-forward: pull request 294 and Inner Child
turn 123, no shared rule or tool changed). Nothing in the article changed: HUMANIZED-SO-FAR.md is still c73f5b5d.

- **Six first tries, his moves** (`fix-20261104/next1/blocks/`, blocks 85, 86, 88 to 91: the uridine stop signs and
  psychedelic caution, then the 5-HTP "Who this is for", tool, Scott's doses and trial), each passing the fidelity check by
  itself and together. Batch x1104j through the API (`fix-20261104/checks/x1104j/RESULTS.md`): the four that ran read 100%
  AI, all four predicted (ND1104-B085#74, B086#75, B088#76, B089#77); the API answered HTTP 402 "Insufficient credits" at
  the fifth, so B090#78 and B091#79 are void (never sent). `record_r1102.py` needs a log of JSON lines only, so the run's
  log was split (`API-X1104j.log` as it came, `API-X1104j-results.log` the results).
- **The tell panel on the four** (E346: his post's baseline read AI in both sections, so the first tries were each
  lineage's second AI read): `fix-20261104/panel/b085-n1/`, `b086-n1/`, `b088-n1/` and `b089-n1/` (PANEL.md each). Every
  sentence of all four was agreed by two or three readers: the label openers and "In practice"; the even symptom and use
  lists; "take that as a safety signal", "this isn't a casual experiment"; "discusses its role in"; the balanced "mixed ...
  but real enough"; and the build, claim, caveat, mechanism, list, instruction. Codex called "chasing the old visual
  threshold can overshoot", "a spaced-out kind of brain fog" and "low-serotonin-looking pattern" human.
- **Second tries of the four** (`fix-20261104/next2/blocks/`; `next2/check_next2.py` writes `CHECK-NEXT2.json`): every
  agreed sentence changed; the fidelity check passes each by itself and all six together. The linter's FAILs are the
  protocol's own lists (E125: the eight stop signs, the post's "wired, numb, or weirdly irritable", the four exclusions,
  W042's list, the four first signs), recorded and not cut; the rest are REVIEW items. **A meaning slip found**: my first try
  of the tool paragraph said the review covers 5-HTP's "use ... in serotonin-toxicity cases"; the review (Maffei 2020,
  PMC7796270, read this turn) treats serotonin syndrome as a risk of 5-HTP (sections 8.2.1 and 9), so the second try says
  "the serotonin-toxicity risk". The first try never went into the article.
- **Question 7, answered by his 14:59 message**: he checks each paragraph in Pangram's web app with his account's credits;
  the API isn't topped up (my view, which he asked for: it isn't really important, since the web app gives the same reading
  per paragraph; the cost is a round with him per set). `fix-20261104/checks/predict_batch.py` now takes `--detector`, so
  the ledger says who checks. Batch x1104k: the four second tries and the two unsent first tries, predicted before his
  checks (ND1104-B085#80 to ND1104-B091#85, all AI, 25% to 35%; `checks/x1104k/PREDICTIONS.md`), on a page of copy buttons,
  **Neuro De-Armoring Checks** (https://claude.ai/artifact/YW7suTvNrjNPvu1wApM93E, `checks/x1104k/build_check_page.py`,
  CHECK-PAGE.html): each button copies the paragraph alone (E326), tested in Chromium by reading the clipboard back, all six
  exact, with no sideways scroll at 400 px.
- **Questions page** (`OWNER-QUESTIONS.md`, republished to https://claude.ai/artifact/8cWv5mbXY8y53RL1nhvzky, version 9):
  question 7 answered; question 8 (may a warning's words change if its meaning stays) open.
- **Delegations**: one Sonnet subagent and one Haiku subagent, each the tell panel's reader for all four drafts (four
  prompts each, from `tell_panel.py prompt`), checked by `tell_panel.py summarize` (agreement across readers): done. Codex on
  the laptop (`codex exec --ephemeral -s read-only`, its configured model) as the third reader of the same four: done, all
  four exit 0.

## 2026-11-04, after Joel's message of 14:28 UTC ("pr 290 has conflicts")

**The mailbox first** (`state/mailbox/claude-community-joel-1018.json`, "2026-11-04 14:28"). 292 (Inner Child turn 122)
had merged at 14:27 with its own records in state/MAILBOX.json, and this branch still carried two records of its own
there (12:06 and 13:53, written before its switch to its own file), so the shared file conflicted again on GitHub, where
main's merge driver doesn't run. Main merged (1d12842c); the branch's two records moved to its own file and the shared
file set to main's content. `lane_mailbox.py settle` does that, and `lane_push.py` runs it before every push, so a lane's
pull request never changes the shared file (a test in `tests/test_lane_mailbox.py`; AGENTS.md). Nothing in the article
changed. Delegations: none.

## 2026-11-04, after Joel's answers of 13:53 UTC (his Scott paragraph, W-17, "290 has conflicts", "6a"): his version in; the conflict fixed; O64

His message, word for word: `fix-20261104/joel-20261104-1353-message.txt`; his answers: `fix-20261104/cards/ANSWERS-20261104-1352.json`.
**The mailbox first** ("2026-11-04 13:53"); since 12:06: 289 (gut r05) merged 12:16, 288 (Inner Child) 12:37, 291 (gut r06)
13:54, with its merge driver for state/MAILBOX.json (`tools/humanization/mailbox_merge.py`).

**290's conflicts** were state/MAILBOX.json, which every lane wrote each turn: main merged twice this turn (7d85d2dd,
c3392a5f), the mailbox merged with main's driver, the gate's numbering notes taken from main (the gut lane's E351; next
E353 after this lane's E352). So that another lane's merge no longer puts this lane's pull request in conflict,
`lane_mailbox.py` now records each lane in its own file, `state/mailbox/<branch>.json` (state/MAILBOX.json stays the
history, its checks still count; main's merge driver still merges it); `lane_push.py` stages the lane's file; tests in
`tests/test_lane_mailbox.py`; AGENTS.md says it. The driver can't help on GitHub, where no merge driver runs.

**His answers in** (`fix-20261104/cards/apply_cards_x1104c.py`, APPLIED-CARDS-C.json): Y-83b his version as he wrote it
(he checked it: [Human Written, 0.0% AI](https://www.pangram.com/history/6716a87f-8df3-4107-ab4c-5df53a83ef6d), every
window High; not checked again), W-17 approved; 6a: the five lines stay. 3c68e8e2 to c73f5b5d. Fidelity PASS (no key
changed), the comparison gate PASS (his words; W-17's sentence read by me, `fix-20261104/cards/read-c/`).

**What his version does** (`fix-20261103/examples/WHAT-HIS-VERSIONS-DO.md`, "His fifth version"; lesson E352): the negation
and its contrast in one sentence, joined with ", but". `tells_lint.py` O64 fails the split form ("You can't tell X. It
does suggest Y."), not an instruction or a next sentence with his "though"; tells registry W118. On the article as it
stands it flags nothing; on his post it flags the sentence he fixed.

Questions page: 6 answered, none open (version 8). Predictions: none this turn (his check stands). Delegations: none.

## 2026-11-04, after Joel's answers of 12:06 UTC (all 12 cards approved; "5a"): the cards in; 82's Low window fixed; 83's to him

His message, word for word: `fix-20261104/joel-20261104-1206-message.txt`; his answers: `fix-20261104/cards/ANSWERS-20261104-1205.json`.
**The mailbox first** ("2026-11-04 12:06"): pull request 287 merged by Joel at 11:36 UTC; the branch fast-forwarded to
main 999d6b91; new since: 289 (Healing the Gut r05, open; its E347 to E349, and an AGENTS.md change in its code review rules).

**The 12 cards in** (`fix-20261104/cards/apply_cards_x1104.py`, APPLIED-CARDS.json): each after-text as the card showed it;
the fidelity check's difference before and after each card recorded in FIDELITY-KEYS.json's new "owner_changes" with the
card's id (7 cards changed keys: Y-82's "cautious extrapolation", W-15's MAOIs and relapse line, W-125's clinician
exception, W-68's PS numbers, W-111's "must", W-112's "dangerous", W-154's L-serine comparison and keto sentence);
`fidelity_keys.py` reads them as his (a test in `tests/test_fidelity_keys.py`). My comparative read of the changed
paragraphs (E284, E294; `fix-20261104/cards/read/READ-RECORD.json`): three findings at severity 1, fates recorded.
e5ead544 to 46c8485f. Fidelity PASS, the comparison gate PASS.

**5a, two more tries each** (`fix-20261104/q5/`; checks x1104h and x1104i; lineages ND1104-B082b and ND1104-B083b):
- block 82: Codex's whole rewrite (`fix-20261104/rewrite-b082/`), [AI Detected, 62.4% AI](https://www.pangram.com/history/20dbe991-0598-4827-b42d-a55a4ef92a81);
  my second, only the Low sentence changed, [Human Written, 0.0% AI](https://www.pangram.com/history/426bed99-5f7e-4c53-866c-6917c4c0c8cd)
  (High, Medium, High). In (`fix-20261104/q5/apply_q5.py`): 46c8485f to 3c68e8e2.
- block 83: my rewrite of its last three sentences, [AI Detected, 84.6% AI](https://www.pangram.com/history/e8b5de85-2203-4504-b915-cd94e9fbf63e);
  only its "It does suggest" sentence changed, [AI Generated, 99.99% AI](https://www.pangram.com/history/7a054118-a4e0-411a-b9fa-3efb1ebf7850), the
  untouched sentences with it. The card's version (Codex's) stays; its Low window is card Y-83b, for his help.
- Lesson E350: a Low window in a paragraph that reads Human is fixed in that window's sentence only, and a one-sentence
  change that moves untouched sentences goes to him. His rule on Low and Medium windows is in AGENTS.md beside E278.

**The rest of the warnings**: W-17 (5-HTP and uridine "can change brain sensitivity quickly", said "in practice") is a
card; question 6 asks about the five "your call" lines (W001, W034 to W036, W053), my advice keep. The other "keep, or
soften" lines stay as they are, since each softening would narrow a real caution: lithium in the 5-HTP list (W014; a
review lists it), the same-day-psychedelics clauses (W016, W049, W063, W083: the firm names are already there), the 5-HTP
side effects (W043: nausea and stomach upset are its common ones), iboga's "most medications" (W002: a reader can't check
which drugs share CYP2D6 or prolong QT).

[Neuro De-Armoring Cards, 4 November (2)](https://claude.ai/artifact/TBrnTti2G9V4fBvC357cTy) (version 3 of that page;
`fix-20261104/cards/build_page_x1104c.py`, REVIEW-X1104C.md; browser test 62 of 62). Questions page: 5 answered, 6 open
(version 7). Predictions: 4 (x1104h 2, x1104i 2), all right. Delegations (model, piece, check, outcome): Codex on the laptop, the rewrite of
block 82 (check: Pangram; not used, 62.4% AI). The rest was mine.

## 2026-11-04, after Joel's answers of 10:39 UTC ("3a 4a"): 3a in; both uridine paragraphs Human; ten warnings cards

His message, word for word: `fix-20261104/joel-20261104-1039-message.txt`. **The mailbox first** (`state/MAILBOX.json`,
"2026-11-04 10:39"); then main merged (4da46a1b): the gut lane's pull request 286 (E342, E345, `hidden_links.py`, a new
`lane_push.py`); `state/MAILBOX.json` conflicted and both lanes' records were kept (24 checks, none lost).

**3a** (`fix-20261104/q3/apply_q3.py`, APPLIED-Q3.json): the two drug names back in brackets in his "Who this is for";
the "owner_open" entries gone from FIDELITY-KEYS.json. 72e9e316 to e5ead544. Fidelity PASS, the comparison gate PASS. That
version by itself: [Human Written, 0.0% AI](https://www.pangram.com/history/0faeb569-0041-45d3-9986-b77b3f490b83) (High).

**The tell panel, then the two paragraphs** (E253 (Inner Child): the turn before had asked his help without it). Codex on
the laptop, a Sonnet agent and a Haiku agent, each given PROMPT.txt only (`fix-20261104/panel/`, each folder's PANEL.md):
- the evidence paragraph (block 82): the panel agreed on four sentences of try 3. Try 5, with those fixed,
  [Human Written, 0.0% AI](https://www.pangram.com/history/036d5dff-88a6-4533-8023-989adbd74a3b) (windows High, Medium, Low, Medium). Try 6, aimed at
  the Medium and Low windows, [AI Detected, 30.3% AI](https://www.pangram.com/history/e36c7366-cdce-4f67-a1bf-cd61514e9fd5); try 5 stays
  (`fix-20261104/r3/blocks/082.md`; blocks-try5 and blocks-try6).
- Scott's paragraph (block 83): try 5, with the panel's tells on try 4 fixed, [AI Generated, 99.9% AI](https://www.pangram.com/history/e17c623b-66d3-4f9b-8e23-d8f2444df0d5).
  Try 6 came from Codex (`tell_panel.py rewrite-prompt`, `fix-20261104/rewrite-b083/`; my one change put back his post's
  "in the right person"): [Human Written, 0.0% AI](https://www.pangram.com/history/bdc81685-fdd0-420e-b74f-1a196b1ec606) (windows High, Medium, Low).
- Both lineages have used their six tries: question 5 asks him about more tries for the Medium and Low windows.
- The misses explained in the ledger (try 5 of 82, try 6 of 82, try 6 of 83). Lesson E346: a paragraph that has read AI
  twice goes to the tell panel before its next try; `pangram_ledger.py predict` refuses it without `--panel` (tests in
  `tests/test_pangram_ledger.py`; `docs/FIXING-AN-ARTICLE.md` section 6 item 4; `predict_batch.py` passes it).

**4a and the warnings cards** ([Neuro De-Armoring Cards, 4 November](https://claude.ai/artifact/TBrnTti2G9V4fBvC357cTy),
version 2; `fix-20261104/cards/build_page_x1104.py`, REVIEW-X1104.md; browser test 78 of 78): Y-82 and Y-83 (the two
paragraphs, to approve), then ten warnings cards from `fix-20261104/warnings/WARNINGS-CHECK.md` and the bad-trips lane's
agmatine check: his precautions with the agmatine cuts (W-15; by itself [Human Written, 0.0% AI](https://www.pangram.com/history/2c74da86-1945-434c-a365-6d849c787b62),
one window, High), the agmatine stop list's flatness said as experience (W-16, his 4a), the cap without "unless
clinician-supervised" (W-125), uridine's effects as experience (W-18, 4a), the choline headache as experience (W-85, 4a),
PS about 400 mg in two places (W-68), the PS "minority also report" sentence cut (W-73), potassium "aim for" (W-111, with
the 2019 figures), "dangerous" as supervised (W-112), D-serine's kidney warning from rats and the keto sentence cut
(W-154). Not yet carded: the 5-HTP and iboga softenings and the generic label lines (W001, W034 to W036, W053). Every
study link on the cards re-checked through PubMed this turn (Hellhammer 2004 and 2014, Kumssa 2021, the POTCAST analysis,
Meftah 2021); the Tufts page for the 2019 potassium figures opened.

Questions page: 3 and 4 answered, question 5 open (version 6). Predictions: 5 (x1104e 2, x1104f 2, x1104g 1); 3 missed,
each explained. Delegations (model, piece, check, outcome): Codex on the laptop, the panel's third reader four times and
the rewrite of Scott's paragraph (check: the panel read it, then Pangram; used, Human Written); a Sonnet and a Haiku agent,
the panel's other two readers on four texts each (check: their replies summarized by `tell_panel.py`; used). The fixes,
the cards and the warnings wording were mine.

## 2026-11-04, after Joel's message of 10:01 UTC: his "Who this is for" in; one paragraph at a time; the warnings checked

His message, word for word: `fix-20261104/joel-20261104-1001-message.txt` (go through the warnings Gemini put in; "i don't
want to do everything myself the point is to teach you"; one paragraph at a time; his version of the uridine "Who this is
for"). **The mailbox first** (`state/MAILBOX.json`, "2026-11-04 10:01"): pull request 281 merged at 2026-11-03 20:57 UTC;
main's new rules read and the branch fast-forwarded to main 9a211d85 (E337 to E341 from the gut and Inner Child lanes); the
bad-trips lane's agmatine check adopted.

**The typographic swap** (E337 (gut); `fix-20261104/swap/swap_x1104.py`, SWAPPED.json): 258 marks in 92 paragraphs;
three paragraphs keep their curly marks, the three this article's measurement found worse straightened. The fidelity
check now matches a dash whatever its spaces ("numb—living", "numb – living"). HUMANIZED-SO-FAR.md 6db92b7a to 6cf2ad04.

**His paragraph in** (`fix-20261104/b081/apply_b081.py`, APPLIED-B081.json): as he wrote it, the swap only. It leaves out
pramipexole and ropinirole, held open in FIDELITY-KEYS.json ("owner_open", new in `fidelity_keys.py`, with a test) as
question 3; his "isn't for" recorded for "not for". 6cf2ad04 to 72e9e316. Fidelity PASS (2 open with him), the comparison
gate PASS. By itself, with its heading: [Human Written, 0.0% AI](https://www.pangram.com/history/9225442f-06b8-4a7a-ab8e-d8a03f720290)
(High); with the two names in brackets, [Human Written, 0.0% AI](https://www.pangram.com/history/0faeb569-0041-45d3-9986-b77b3f490b83) (High).

**The next two paragraphs his way, one at a time** (`fix-20261104/r3/`, blocks-try1 to blocks-try3 and blocks; checks in
`fix-20261104/checks/x1104a` to `x1104d`, each with RESULTS.md): the evidence paragraph 62.2%, 30.9%, 0.0% (AI Assisted) and
2.6% AI; Scott's signal 100% AI in all four. Both on [Neuro De-Armoring Cards, 4 November](https://claude.ai/artifact/TBrnTti2G9V4fBvC357cTy)
(`fix-20261104/cards/`, browser test 62 of 62), the way he asks to be asked.

**The warnings** (`fix-20261104/warnings/WARNINGS-CHECK.md`, E344): the bad-trips lane's agmatine check mapped onto every
agmatine line here, and the other 48 warnings checked against PubMed. Question 4 asks what only his experience decides;
the cuts and softer wordings go to him as cards after it.

**One paragraph at a time, enforced** (E343): `pangram_ledger.py predict` refuses a section or stretch retry after an AI or
Mixed result until `--narrowed` names its paragraph checks (tests in `tests/test_pangram_ledger.py`); `docs/FIXING-AN-ARTICLE.md`
section 6 item 4.

Predictions: 10 (x1104a 4, x1104b to x1104d 2 each), all right. Delegations (model, piece, check, outcome): a Sonnet
helper, the research for the 48 non-agmatine warnings; check: six of its 29 sources re-opened through PubMed, each says what
the check says, one link (the trial's main paper) couldn't be opened and was replaced by the trial's own analysis; used, as
WARNINGS-CHECK.md's second part. The rewrites and the reading of his version were mine.

## 2026-11-03, after Joel's answers of 17:48 UTC: his three versions in; round 2 his way; question 2

His answers file for Neuro De-Armoring Cards, 3 November, sent with no other text, word for word in
`fix-20261103/examples/ANSWERS-20261103-1748.json`: all three cards "revise" with his versions, X-26 and X-84 with the
comment "passes", X-15 with none. **The mailbox first** (`state/MAILBOX.json`, "2026-11-03 17:48"): pull request 279 merged
by him at 17:48 UTC; 280 (Bad Trips) and 278 (Inner Child) are other lanes'; LESSON-INDEX entry 87 is now standing for him
(every final answer ends with one "GH handoff:" line).

**His versions in** (`fix-20261103/examples/apply_answers_x1103.py`, APPLIED-X1103.json, read/READ-RECORD.json): as he
wrote them, two typos fixed ("inhibiton", "guafacine"). HUMANIZED-SO-FAR.md a4b4e05a to 6db92b7a. This lane's comparison
gate is set up (`COMPARE-GATE.json`, like the hypnosis lane's): PASS, 0 unread. The fidelity check reads his wording as the
post's once recorded with his card (`FIDELITY-KEYS.json` "owner_wording", 12 entries; `fidelity_keys.py`, with tests);
"Don't" is read as "Do not" in any draft. PASS. Nothing of his was lost, so no question about it.

**X-15 by itself** (`fix-20261103/x15/`, batch x1103, predicted AI at 0.40): [Human Written, 0.3% AI](https://www.pangram.com/history/0bc718b1-278a-40ce-a7dd-6af7d45268d5),
its first sentence Human (High), the two short label sentences Human (Low). X-26 and X-84 not checked again (he said they
pass).

**What his versions do** (`fix-20261103/examples/WHAT-HIS-VERSIONS-DO.md`; gate E335; tells_lint.py O61, registry W113:
a dose as a label and its spec).

**Round 2 his way** (`fix-20261103/r2his/`, RESULTS-ROUND2.md): one stretch of each kind, from his post, fidelity PASS on
every draft. The science (V3) went from 100% AI to 40.9% and then 19.8% AI; the warnings (V1) and uridine (V2) stayed 100%
AI in both tries; three warnings by themselves in his label register, 100% AI; the 5-HTP warning with its warning phrases
re-said (an experiment), 100% AI. Gate E336: only his wording reads Human in the warnings and doses. Question 2 on
`OWNER-QUESTIONS.md` asks how he wants those done (recommended: he rewrites them a section at a time on a cards page, and I
do the science his way meanwhile).

Predictions: 11 (x1103 1, r1103c 3, r1103d 3, r1103e 3, r1103f 1), all AI, all right. Delegations (model, piece, check,
outcome): none; the rewrites and the reading of his versions were judgment throughout.

## 2026-11-03, after Joel's message of 15:22 UTC: question 1 answered; round 1 rewritten and checked; Emulate retired; three examples for him

His message (`fix-20261103/joel-20261103-1522-message.txt`): "no need to recheck i'm sure it's fine, move onto the next
article you said you were already working on it right". His answers to two questions in the app, word for word in
`fix-20261103/joel-20261103-1522-answers.txt`: question 1, "Freely, in your voice (Recommended)"; then, after round 1 read
AI and Emulate showed 0 words left, "yout old me emulate doens't even pass pangram 4.1 very well anymore so that's
pointless and emulate has done so much damage to my guides that took too long to fix as you saw with hypnosis guide.
give me a couple examples i will see how to rewrite it to train you". **The mailbox first** (`state/MAILBOX.json`,
"2026-11-03 15:22"): pull request 277 merged by him at 15:22 UTC; nothing else new.

**Round 1** (`fix-20261103/r1/`): every section rewritten freely in his voice (sections/S01 to S10.md; assemble_r1.py
makes CANDIDATE.md, fidelity_keys.py PASS on the whole, and cuts each section into stretches the API takes, his Human
(High) paragraphs left out of them); tells_lint.py on every section and its flags in my sentences fixed. Checked through
the API on the laptop with public links, predictions first: batch r1103a (`a/`, the first try of Psychology is the
Software: 40.4% and 100% AI) and batch r1103b (`b/`, 26 stretches: 19 at 100% AI, the best 12.7% AI, Psychology is the
Software's first half; RESULTS.md). Every prediction was AI, and right. Three predictions were voided, never sent: the
API counts a heading of eight words or more as a paragraph, so it refused one stretch, and the cut was made again.

**Round 2 stopped before it started** (`fix-20261103/r2/emulate_r2.py`, the 30 segments it would have sent): Emulate's
balance was 0 words, and his answer retires it (gate E333, `docs/EMULATE-FALLBACK.md`, AGENTS.md). Gate E334 says what
round 1 showed.

**His three examples** (`fix-20261103/examples/build_page_x1103.py`, REVIEW-X1103.*; published as Neuro De-Armoring Cards,
3 November, https://claude.ai/artifact/GKEbRH8VvXKzbEnZGCZUgz, capabilities db and downloads; browser test 60 of 60):
the underpinning paragraph (the science), the UMP trial (a dose with its instructions) and agmatine's interactions (a
list of warnings), each a stretch to edit, each linking its baseline result and my round-1 results.

Pull request 278, opened during the turn, is the Inner Child lane's (its real-life section), nothing for this lane. Predictions: 28 (2 in r1103a, 26 in r1103b), all AI, all right; 3 voided. Delegations (model, piece, check, outcome):
none; the rewrite was judgment throughout.

## 2026-11-03, after Joel's message of 14:52 UTC

His message was his answers to the hypnosis guide's question 34 and "make sure this closer reading is also part of the general joel-articles skill"; nothing changed in this lane. Question 1 still waits on him; this lane is next. The word-for-sense read is now in `SKILL.md` with its tool, `tools/humanization/sense_read.py`. Predictions: none. Delegations (model, piece, check, outcome): none.

## 2026-11-03, after Joel's message of 13:46 UTC

His message was the hypnosis guide's "33a" (the guide into his post, done), his Pattern 10 version and "oily" for "old"; nothing changed in this lane. The hypnosis guide is in his post, so this lane is next; question 1 still waits on him. Gates E331 and E332 apply here (the handoff's START HERE). Predictions: none. Delegations (model, piece, check, outcome): none.

## 2026-11-03, after Joel's message of 12:18 UTC

His message was the hypnosis guide's fourth free check and a card; nothing changed in this lane. Question 1 still waits on him; this lane is next once the hypnosis guide is in his post (its question 33).

## 2026-11-03, after Joel's message of 11:19 UTC

His message was the hypnosis guide's 31a, 32a and third free check; nothing changed in this lane. Question 1 still waits on him.

## 2026-11-03, after Joel's answers of 00:39 UTC

His answers were the hypnosis guide's third cards page. Their lessons apply here too: E328 (overcompletion is read for, and cut, before a flagged window is reworded; parallel structure is no reason to keep a second explanation), E329 (a window over a heading is tested as Pangram reads it before a card advises keeping it) and E330 (a made-up word is fine in an informal piece if it sounds right). Nothing in this lane changed; question 1 still waits on him.

## 2026-11-02, after Joel's message of 23:07 UTC

His message was the hypnosis guide's second free check; nothing changed in this lane. Question 1 still waits on him.

## 2026-11-02, after Joel's message of 21:59 UTC: his second Pangram account's lessons

Read in the hypnosis lane (`articles/inner-signal/humanize/fix-20261102/joel-pangram/history2/`): E326 and E327 and linter rules O59 and O60 apply to this lane's checks and drafts. Nothing in this lane changed; question 1 still waits on him.

## 2026-11-02, after Joel's message of 20:38 UTC: checks over six paragraphs go free (E325)

His message was about the hypnosis guide's whole check ("that should be done the free way to not waste my pangram
credits"). This lane's baseline of the whole article (5,821 words, batch n1102) was one of the five halves or whole
articles the lanes sent through the API on 2 November, against his rule (E218). `tools/humanization/pangram_api.py` and
`pangram_ledger.py` now refuse a text of more than six paragraphs or 1,200 words through the API (gate E325); the
handoff's START HERE says how this lane checks a bigger section or the whole article free. Question 1 still waits on him.

## 2026-11-02, after Joel's message of 19:11 UTC: the lightest fix tried on one section; question 1

His message was about the hypnosis guide (28a, 29a); this lane's next step went on. **Part 1, C to E**
(`fix-20261102/s04/rewrite_s04.py`, CANDIDATE.md, SECTION.txt): the template labels off ("The Problem:", "The Fix:", "The
Hardening:"), the self-answered question made a statement, the closer "The engine is flooded." folded in, short sentences
joined; his own sentences kept where mine failed the linter (the side effects, the hot and cold showers). fidelity_keys.py:
PASS. tells_lint with his text as owner: REVIEW. Checked through the API with a public link (batch n1102r, lineage
ND1102-04 try 2 of 2, called AI at 0.25, right): [AI Detected, 90.6% AI](https://www.pangram.com/history/8a5c6453-c6f1-4ab3-b713-51e54e3550f2)
from 100%; only the SSRIs paragraph reads Human (Low, Medium, Low). So the template is not the main tell: question 1 on
`OWNER-QUESTIONS.md` asks how freely the science sections may be rewritten (default a: freely in his voice, every claim,
number and warning kept, nothing invented, one card per section). Gate E323 for this post: its title's "v5.1 (Sept 10,
2026)" changes with the post.

Predictions: n1102r 1 of 1. Delegations (model, piece, check, outcome): none.

## 2026-11-02, after Joel's message of 18:16 UTC: the lane set up; the baseline checked

His message (`articles/inner-signal/humanize/fix-20261102/joel-20261102-1816-message.txt`): "... then we can start on the
next one we had queued". **The mailbox first**: recorded for the turn in `state/MAILBOX.json` ("2026-11-02 18:16"), nothing new.

**The article, registered** (`articles/INDEX.json`; IMPORT-RECEIPT-20261102.md): his post read through Substack's API from
the laptop (`source/POST-20261102.json`) matches the editor copy of 28 September word for word but for the video's
placeholder text, so master.md is that copy's Markdown. Owner locks: none yet; the protected function is the protocol's
fidelity (OWNER-LOCKS.json).

**The fidelity check** (`tools/humanization/fidelity_keys.py`, tests in `tests/test_fidelity_keys.py`; `FIDELITY-KEYS.json`):
every number with its unit, every compound and term, and every warning sentence with its own rarest words, from master.md.
It fails a draft with one dose changed ("150-300 mg" to "150-250 mg"), one compound left out of a list, or "Do not push
through numbness." taken out while other "do not" lines stay.

**The baseline** (`fix-20261102/baseline/make_baseline.py`, batch n1102, through the API on the laptop with public links;
RESULTS.md): ten sections and the whole, predictions first (all AI), all eleven right. The whole:
[AI Detected, 83.3% AI](https://www.pangram.com/history/72952f09-0e99-46d6-b89f-5fa574422584). By section: the introduction
and disclaimers 63.1% AI (his introduction Human (High)), Psychology is the Software 83.5%, Part 1 A and B 76.2%, Part 1 C to
E 100%, Part 2 phosphatidylserine 99.9%, uridine 100%, 5-HTP and ATP 82.1%, Part 3 87.2%, Part 4 58.6% (the D-serine
paragraph Human (High)), Part 5 and the Aftermath 75.9%.

**Next**: the AI windows, section by section (HANDOFF's Next step).

Predictions: n1102 11 of 11. Delegations (model, piece, check, outcome): none; the read and the predictions were the lead
session's.
