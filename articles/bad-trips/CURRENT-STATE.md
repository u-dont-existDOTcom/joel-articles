# Bad Trips guide: current state

Updated: 2026-11-08 (turn 28, his messages of 17:22 and 17:24 UTC). Earlier: 2026-11-07 (turn 25, his round-23 export of 22:38 UTC). Registered 2026-11-03 at Joel's message of 15:45 UTC
("start working on humanizing my badtrips guide at badtrips.u-dont-exist.com";
`experiments/t01-answers/JOEL-MESSAGE-20261103-1545.md`).

## Goal

A guide with a quick version and a long version that says each thing once, with the call-for-help lines in one place
(his message: "this article has a big duplication issue ... too much safety language spread everywhere rather than in
one spot"), then every paragraph and section reading Human in Pangram, with the meaning kept and every remedy, compound,
dose, unit, timing and warning exactly as it went in, and his post updated with the changes he approves.

## Authority / baseline

- `master.md`: his post as of 2026-11-03 (`IMPORT-RECEIPT-20261103.md`): the Markdown of his pasted editor HTML
  (`source/owner-editor-20261103.html`), which matches the published post block for block. `original.md` is the same
  text; `original-blocks.json` numbers its blocks B0 to B438; `original-page.md` is the review pages' form of it.
- `OWNER-LOCKS.json`: no passages locked; protected functions: the remedies' fidelity (`humanize/FIDELITY-KEYS.json`)
  and call-for-help thresholds staying where the reader acts on them.
- The shared rules: `AGENTS.md`, `docs/FIXING-AN-ARTICLE.md`, `docs/HUMANIZATION-GATE.md`,
  `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`, `tools/humanization/`.

## Completed

- 2026-11-03 (turn 1): registered; fidelity keys extracted; the published post compared with his paste (402 of 402
  blocks the same); baseline free check on the live post (his extension's label: AI; full analysis pending, his task 1);
  two fresh readers' repeats reads and a third reader's safety-line map (`experiments/t01-repeats/`); the round-1
  marking page (`review/r01/`). 17:15 UTC: reader A's and B's reports and the first half of C's (B4 to B207) checked
  quote by quote against the article; 13 new cards (nine repeats, two safety lines, four questions where the guide says
  two things that don't fit together) added to round 1's page; then reader B's final report (17:30 UTC): three more
  (two repeats, the charcoal question), 35 cards; then reader C's final safety map (17:40 UTC): five more (three
  safety lines, a repeat, the question of moving the support lines) and two cards revised, 40 cards (version 6 of the
  page). Repeats and safety lines the readers found that stay, with what each copy carries:
  `experiments/t01-repeats/NOTE.md`.
- 2026-11-03 (turn 2, his message of 18:59 UTC): pull request 280's conflicts with main resolved (main's Emulate wording,
  gate E333; both lanes' mailbox records); the baseline's full analysis read (his link: AI Detected, 82% AI, 189
  windows, recorded with each window's confidence in `humanize/baseline-20261103/` and the ledger); his 40 answers
  recorded and applied (30 change cards, his RP-4 line, Q-1, Q-4, Q-5, Q-7; 14,504 to 13,808 words); his three new
  rules in the shared files (gate, `tells_lint.py` O46 and X1, the tells registry); round 2's page built.
- 2026-11-03 (turn 3, his messages of 22:04 and 22:05 UTC): main merged in again (the neuro lane's tells registry entry
  W113, O61, kept; this lane's two renumbered W114 and W115); his messages saved
  (`experiments/t01-answers/JOEL-MESSAGE-20261103-2204.md`); DMSO's blood-thinner line checked against PubMed and put on
  round 2's page as SF-8 (cut; the evidence is lab work: a mild platelet effect in donated blood, no clot in an injured
  mouse artery, no study of bleeding in people), 26 cards, version 2 of the page, no answers on it yet; the agmatine
  warnings (the neuro de-armoring protocol's, not this guide's) checked one by one:
  `experiments/t02-warnings/AGMATINE-WARNINGS-CHECK.md`. The whole-guide page's link check against his post lists two
  links gone, the appendix's Fireside and ICEERS root links: RP-14 (approved) cut that line as the support lines' third
  copy, and both services stay linked in Get One Human Anchor and Who to Contact.
- 2026-11-04 (turn 4, his round-2 answers of 10:26 UTC: all 26 cards approved, no comments): main merged in (the gut
  lane's W114 and W115 kept, this lane's tells renumbered W116 and W117; both lanes' index, lane and mailbox entries);
  his answers recorded (`review/r02/ANSWERS-R02-20261104-1026.json`) and applied by `review/r02/apply_r02.py`, every
  change of words checked against its card exactly (13,808 to 12,691 words; `review/r02/GUIDE-AFTER-R02.md`); round 1's
  output frozen as `review/r01/GUIDE-AFTER-R01.md` and round 2's page input as `review/r02/PAGE-R02.md`; the standard
  swap (gate E337 (gut)) run as the humanize pass's first step (`humanize/h01/swap.py`, 311 characters) to make
  `GUIDE-SO-FAR.md`; its fidelity keys taken (`humanize/h01/FIDELITY-KEYS-H01.json`: 134 warning sentences, 59 terms, 32
  numbers); `KEEP-AS-IS.json` started (gate E340: 8 kept, 5 meant cuts); every section link lands on a heading, no
  pointer broken (`section_refs.py`), all 14 pictures and 4 videos there (`post_embeds.py`, fixed to see the editor
  HTML's videos). Links that went with approved cuts: the Longer Triage's picture (LT-1), Poison Control's charcoal page
  (CL-12, with step 12's charcoal paragraph) and ICEERS's older address (CL-15; the service stays in Who to Contact).
- 2026-11-04 (turn 5, his message of 11:35 UTC: rewrite the web app to match the guide if it can be done, otherwise keep
  the checklist in the guide; the post waits until the work is finished): main merged (pull request 287); his message
  saved (`experiments/t04-answers/`); the app's widget saved from the live page on his laptop and rewritten to match
  the guide (`experiments/t05-webapp/`: `cut_widget.py`, `rewrite_app.py`, 44 exact replacements in the guide's words;
  version 8), tested in Chromium against the live version 7 (`test_app.py`: every check passes, the live app fails all
  ten situations the rewrite is for); the file sent to him and put on his laptop; last turn's web-app check corrected
  (it had missed the answers' collapsed field notes). The checklist leaves the guide once version 8 is live
  (OWNER-EDITS `checklist-to-app`).
- 2026-11-04 (turn 6, 13:19 UTC, no new message: the warnings check finished): main merged (pull request 288); the
  research helper's check of the guide's 149 warning lines (`experiments/t05-warnings/`) taken through E344: the
  sources behind every change re-opened by me (PubMed, the diclofenac, sulindac and RIMSO-50 labels, the AHA page),
  the rest by a second helper that hadn't done the first search (61 sources, 13 wording fixes: a wrong figure, two
  overstated findings, populations left out; no verdict changed); my own re-reading moved three lines to Keep
  (shungite, the mouth burn, the cluster headache "may") and found LSD on Scotton's table, the histamine review's
  silence on bacteria, the sheep studies of nebulized DMSO and the rat choline-uptake study. Result: 93 keep, 38 his
  experience, 5 his views, 5 generic (for the humanizing), and 9 cards on round 3's page (`review/r03/`, built from
  `GUIDE-SO-FAR.md` by `build_r03.py`, browser test 78 of 78; Bad Trips Guide, Round 3,
  https://claude.ai/artifact/3FcwLgzCtnfBeH2xHG6BXq): 2 cuts unless they're his experience (nebulized DMSO with tar,
  DMSO depleting choline), 5 lines changed to what their studies show (transdermal CBD, "Psychedelics" in serotonin
  syndrome, the ferment itch, DMSO sleep in rats, DMSO with corticosteroids and NSAIDs), a 2026 mouse study on beach
  morning glory, and the chest-pain line where the guide parts from the AHA.
- 2026-11-04 (turn 7, his round-3 answers of 14:25 UTC and his messages of 14:25 and 14:26 UTC: he's putting the app in
  himself, with GPT on his VPS, and asked whether to wait for the claims check): answered at once (go ahead, with
  version 9: version 8 plus the one round-3 line the app shares with the guide, the ferment itch; tested; sent and put on
  his laptop); main merged (pull request 291, its mailbox merge driver used and set in this clone); his messages saved
  (`experiments/t06-answers/`) and his answers (`review/r03/ANSWERS-R03-20261104-1425.json`) applied by
  `review/r03/apply_r03.py`: the 7 approved cards in, each checked against its card (W-SLEEP's link moved with its words),
  12,745 to 12,733 words; `GUIDE-SO-FAR.md` is now the guide after round 3 (no characters to swap); the two cuts on
  `KEEP-AS-IS.json` (C6, C7); fidelity keys taken again (`humanize/h01/FIDELITY-KEYS-R03.json`: 133 warning sentences, 57
  terms, 32 numbers); the whole-guide page re-rendered. W-GLORY rejected ("not sure why mice with no immune system says
  about an herb humans use traditionally already"). His W-CBD Revise came with a summary of the evidence on CBD and
  focal seizures; each point checked (PubMed: Patel et al. 2025, doi 10.1111/epi.18496; the FDA's Epidiolex label of May
  2026) and the paragraph redone as round 4's W-CBD2, with the four checklist pointers moved to the app (APP-1 to APP-4)
  on the same page (`review/r04/`, Bad Trips Guide, Round 4, https://claude.ai/artifact/HcLtoHF2XB2wSoxbvwmEVf; browser
  test 78 of 78). The live app still showed version 7 at 14:40 UTC.
- 2026-11-04 (turn 8, his round-4 answers of 14:58 UTC, all 5 approved, W-CBD2 with the comment "now fix it so it
  passes pangram", and his message "updated the web app"): main merged (pull request 294, no shared file changed); his
  message and answers saved (`experiments/t07-answers/`, `review/r04/ANSWERS-R04-20261104-1458.json`); the live page
  read from his laptop at 14:59 UTC shows version 9, its widget the same as `experiments/t05-webapp/APP-V9-20261104.html`
  (`experiments/t07-answers/APP-LIVE-20261104-1459.html`). Each round's input is frozen now, so every apply script
  reruns: `humanize/h01/swap.py` writes `humanize/h01/GUIDE-AFTER-SWAP.md` (no longer `GUIDE-SO-FAR.md`), which
  `review/r03/apply_r03.py` reads, and `review/r04/apply_r04.py` reads `review/r03/GUIDE-AFTER-R03-blocks.json`; both
  reproduce their outputs. `apply_r04.py` put the 5 cards in, each checked against its card, and took the Quick Bad Trip
  Checklist out (B3 to B64, 60 blocks; OWNER-EDITS `checklist-to-app` applied). Each of its sentences was compared with
  the long part and the app; the three it alone had went into the long part in his words: the stroke warning signs
  line and link (B104), the Chantress Seba line with his music page (B304, after the drum-rhythm item) and his love page
  link (on "Sending Love" in the sorrow heading, B376). 12,733 to 11,882 words; `review/r04/GUIDE-AFTER-R04.md` is
  `GUIDE-SO-FAR.md`. Checks: no section pointer flagged (`section_refs.py`); all 14 pictures and 4 videos there
  (`post_embeds.py`); the links gone are the checklist's own section links and one of its four Inner Child links (three
  stay). Fidelity keys taken again (`humanize/h01/FIDELITY-KEYS-R04.json`: 119 warning sentences, 58 terms, 30
  numbers); `ARCHITECTURE.md` redrawn without the checklist; the whole-guide page re-rendered. On his comment: Pangram's
  web app on the Active Seizure section and on four versions of the CBD paragraph, three of mine and one by GPT (Codex
  on his laptop): all AI (`humanize/h02-cbd/RESULTS.json`, every window with its confidence and link; not scored, as no
  prediction was logged first). A tell panel of three fresh readers on my second version (`humanize/h02-cbd/panel-C2/
  PANEL.md`): a balanced mini-review, every finding paired with its caveat, even sentence lengths, a tidy verdict. So
  the paragraph went to him for his own version (FIXING-AN-ARTICLE item 7, gates E256 and E333): round 5's page, one
  edit card, CBD-YOURS (`review/r05/`, browser test 62 of 62; Bad Trips Guide, Round 5,
  https://claude.ai/artifact/12uJZXZ5xptJoYQjoXQJKq). Then the humanize pass started, without a whole-guide check first
  (pull request 293's E354): `humanize/section_map.py` (`humanize/SECTION-MAP.md`) maps the guide onto the published
  post's check, 7,285 of its 11,722 words in AI High windows, 1,790 in Human High (the Healing Treadmill, most of Shadow
  Thoughts, half of the Other Bypass, the appendix). The first section, Psychological First Aid with Stillness or
  Movement? (`humanize/h03-pfa/`): my rewrite read AI in one window (High); narrowed to its dangers paragraph (E343), my
  first try read AI (High), and my second, with the tell panel's four agreed sentences fixed, AI (High, then Medium on
  the phone sentence; `humanize/h03-pfa/RESULTS.json`, links and predictions in the ledger). The readers' diagnosis on
  both tries: a checklist turned into prose in an even rhythm, with no first person and nothing at stake for the writer
  ("assembled rather than lived"; `panel-P3T1/PANEL.md`, `panel-P3T2/PANEL.md`), which only he can supply. So the
  paragraph is round 5's second card, PFA-YOURS (the page republished at the same address), and the how-to sections wait
  for his version (E333).
- 2026-11-04 (turn 9, his message of 22:37 UTC: the laptop resume line and his round-5 answers, exported 22:14 UTC, both
  cards Revise with his own versions and long comments): main merged (pull requests 295 to 302; the tells registry keeps
  both lanes' tells); his message and answers saved (`experiments/t08-answers/`, `review/r05/ANSWERS-R05-20261104-2214.json`)
  and applied by `review/r05/apply_r05.py`: his CBD paragraph as the three he broke it into (B111, N-CBD-2, N-CBD-3), his
  dangers paragraph (B236), three typos fixed ("take priority", "a rats", two trailing spaces), the FDA, trial and two
  DMSO links back on the words that name them, the 2025 study gone with his cut (11,882 to 11,941 words;
  `review/r05/GUIDE-AFTER-R05.md` is `GUIDE-SO-FAR.md`). `KEEP-AS-IS.json` K9 to K12 and cut C8; `OWNER-EDITS.json`
  r05-cbd-his-version and r05-pfa-his-version (16 passed); fidelity: only his cut's numbers left, keys taken again
  (`humanize/h01/FIDELITY-KEYS-R05.json`). His video link checked from his laptop ("Miraculous CBD Oil Stops Child's
  Epileptic Seizure Instantly", High At 9 News, 35 seconds). His new points checked against their sources (E348): the
  skin-gel trial's paper (O'Brien et al. 2022, full text), the Epidiolex label's doses, the 7-OH-CBD mouse study (Whalley
  et al., AES 2017): round 6's CBD-TRIAL. His note on what people report for seizures checked one by one (Epilepsy
  Action, Efron 1956, the Epilepsy Society's July 2026 sheet on Betts's work): round 6's SEIZ-WARN (`review/r06/`, 2
  cards, built by `build_r06.py`; REVIEW-R06.md has them as text). His lessons into the shared rules: E360 (one
  making-sense read before every Pangram try, `docs/MAKING-SENSE.md`, his question answered), E361 (the next obvious fix,
  not a new strategy), `tells_lint.py` O68 (a study opened bare, W122), the newcomer read's new questions and his pairs
  (`tools/humanization/hidden_links.py`, built on pull request 293's version), and the tell panel's "lived experience"
  notes sent through the making-sense read (`tell_panel.py`). The first five minutes' P4 drafted his way
  (`humanize/h04-pfa-his-way/P4-DRAFT.md`, D3 linter CLEAR), not yet checked.
- **Not done this turn, and why:** no Pangram check. A permission request (a WebFetch to PubMed) went unanswered early in the turn,
  with the note that he may be away and that no other call needing approval should be made until he writes
  again, so the browser routes to his Pangram account (the app's browser pane, Claude in Chrome) weren't tried, and
  round 6's page wasn't published as an artifact; the page went to him as a file, its cards as text on GitHub.
- 2026-11-05 (turn 10, his upload of 00:13 UTC: "Cannabis inhalation for rapid seizure relief: new research", from AskRigor,
  saved word for word in `experiments/t09-answers/`): the studies it rests on checked on PubMed from his laptop (Sivakumar et
  al. 2017, Hegde et al. 2012, Roebuck et al. 2022, Wallace et al. 2003); the Pangram checks of last turn run in his
  account through the desktop app's browser pane (Claude in Chrome wasn't connected), 13 checks with predictions first
  (`humanize/h05-checks-20261105/RESULTS.md`; 11 of 13 calls right). His CBD paragraphs with the video link: Human Written,
  0%, two windows Low (his words; for him on a later page if he wants). The trial sentences: Human on try 2. The warning
  stage: Human, High, on try 2. The cannabis paragraph from his research: AI in four tries (tell panel after the second);
  his P3 with my P4: AI in four tries, his P3 included. Round 6's page rebuilt as version 2 (3 cards: CBD-TRIAL,
  SEIZ-WARN with both paragraphs, MOVE-YOURS for his version; browser test 84 of 84) and published from this account
  (Bad Trips Guide, Round 6, https://claude.ai/artifact/61WV1ADoZb9fB8oKJkiL6H; db and downloads declared, as the page's
  answer store and export use them). The scorecards rebuilt.

- 2026-11-05 (turn 11, his round-6 answers exported 15:14 UTC, saved as `review/r06/ANSWERS-R06-20261105-1514.json`, and
  his message "make sure you merge lessons with main branch so everyone is sharing always"): his three versions and his
  placement in (`review/r06/apply_r06.py`: the warning stage with his humic line after the rescue medicine and before the
  CBD paragraph; his cannabis paragraphs; his topical CBD paragraph without 7-OH-CBD; his merged first-five-minutes
  paragraph; 11,941 to 12,287 words). His points checked against their sources (E348): the Congress transcript ("mais de
  30 testes"), ABRACE (a patients' association), the gel trial's authors (adults with focal epilepsy, not "generalized"),
  the Dravet and Lennox-Gastaut trials (convulsive and drop seizures), tuberous sclerosis (mostly focal), drug-caused
  seizures (generalized). His "fix the way you work" made into enforcement: `tools/humanization/sense_receipt.py` (a
  receipt per paragraph: each sentence's payoff for the reader's case; a checked point whose reason went is cut), which
  `pangram_ledger.py predict` and `suggestion_review.py` now require of my text, and a retry that rewrites more than 40%
  of the last try is refused without a reason (E361); `predict` now hashes the text as Pangram reads it. His merge rule:
  `lane_push.py --merge` (a branch that changes shared rules merges into main once its checks pass). Lessons E365 to E367
  (`docs/HUMANIZATION-GATE.md`; E362 is the other session's), `docs/MAKING-SENSE.md`'s questions 2, 3, 6 and 7 with his round-6 pairs, `AGENTS.md`.
  Pangram in his account (`humanize/h06-r07-20261105/RESULTS.md`, predictions first, 8 of 9 right): his warning stage,
  cannabis and topical CBD paragraphs Human, High; his forums paragraph AI in my two kept sentences. Round 7's page, 4
  cards, every new text Human, High, with its receipt and two fresh reads (Bad Trips Guide, Round 7,
  https://claude.ai/artifact/41gorxz7ZJ1MV8QL1E63vs; cards as text in `review/r07/REVIEW-R07.md`; browser test 78 of 78):
  ABRACE's two facts, the gel trial's authors and what it means for drug seizures, the paragraph after his move ("During
  the seizure, alongside any rescue medicine", the focal sentence cut), his forums paragraph (my sentences cut down to
  what the reader needs, after a tell panel).
- 2026-11-05 (turn 12, his round-7 answers exported 17:09 UTC, saved as `review/r07/ANSWERS-R07-20261105-1709.json`, all
  four approved, and his message: "you're right it's a non-profit that's important", a Gemini write-up on ABRACE's YouTube
  channel to take "the important points from (not trying to add clutter)", and "add all the rest of it to askrigor
  atlas"): round 7 in (`review/r07/apply_r07.py`; 12,287 to 12,298 words), and "by a non-profit patients' association
  called ABRACE" in his cannabis paragraph (Human, High). From the write-up nothing else went in: it is about children
  taking ABRACE's oils by mouth for months, its first-aid video says what Active Seizure already says, and the nasal
  spray is already in. The rest went to AskRigor (`experiments/t10-answers/ASKRIGOR-CHECK-20261105.md`): no CBD or
  seizure card existed; nine claims checked (clobazam holds; the trials' 30 to 50% leaves out placebo; diarrhoea
  understated; no trial supports any CBD:THC ratio); findings card ARF-0304 and the research map pending its review.
  The humanize pass: Psychological First Aid's room paragraphs (B238 to B241, "Then look at the room" to the playlist)
  read AI as they are, and in five tries each (four of mine, the last two after a tell panel, and one by Codex from the
  panel's notes), every one AI, 100% (`humanize/h07-20261105/RESULTS.md`, 13 of 13 predictions right). Round 8's page asks
  for his version (Bad Trips Guide, Round 8, https://claude.ai/artifact/FnvfZWzTyK2jktLGc88Vgr; the card as text in
  `review/r08/REVIEW-R08.md`; browser test 62 of 62).
- 2026-11-06 (turn 13, his round-8 answer exported 00:27 UTC, saved as `review/r08/ANSWERS-R08-20261106-0027.json`, and
  his comment, `experiments/t13-answers/JOEL-COMMENT-R08-20261106.md`): his version of the room stretch's second part in
  (`review/r08/apply_r08.py`; the fixes and the music, B240 and B241, the text of his check that read Human, 26e9138d).
  His five checks read from his history (`humanize/h08-20261106/HIS-CHECKS-READ-20261106.json`): the quips cut, the
  payoff at the start and the exact act each flipped a part to Human. Lessons E370 to E372 in the shared gate (his quips
  go where he asked for that; the reason first, plainly, and each act exact; a card for his version gives each paragraph's
  reading). His exercise, the first part (B238, B239): my fix reads Human, 0% alone (07e19481), with his line said plainly;
  in place before his second part the stretch reads AI, High, and so does his own stretch (54b7312f), so the stretch
  itself is next (`humanize/h08-20261106/RESULTS.md`). Round 9's page: one card, the first part (Bad Trips Guide, Round 9,
  https://claude.ai/artifact/KrdxXmj483tg4kEhAk8waB; `review/r09/REVIEW-R09.md`; browser test 56 of 56, the test now
  handles a page of one card to approve).
- 2026-11-06 (turn 14, his round-9 answer exported 16:38 UTC, saved as `review/r09/ANSWERS-R09-20261106-1638.json`:
  ROOM-FIRST approved, no comment): round 9 in (`review/r09/apply_r09.py`; B238 is my fix of the first part, B239 out;
  12,299 to 12,308 words; the fidelity keys record "stuck beside" for his "trapped beside", `humanize/h01/FIDELITY-KEYS-R09.json`).
  The room stretch in place (B238, B240, B241) is the text that read AI, High at 34d92f15; the tell panel on it agrees on
  its diagnose-then-fix build and on four of his sentences, none of mine (`humanize/h08-20261106/panel-STRETCH/PANEL.md`).
  Round 10's page: one card asking for his version of the stretch, each paragraph's reading on it (Bad Trips Guide, Round
  10, https://claude.ai/artifact/FUuDsfqAQgCwDgade5KwaY; `review/r10/REVIEW-R10.md`; browser test 62 of 62).
- 2026-11-06 (turn 15, his message of 17:30 UTC, saved as `experiments/t15-answers/JOEL-MESSAGE-20261106-1730.md`): round 10's card called the room stretch's sentences his and asked for his version; they were the guide's AI text he had humanized, and fixing it is my job. The rule, gate E373: in an article a model drafted, his words are only what he wrote himself before the humanizing; the model's text stays mine to fix after he humanizes it, his decisions in it kept (`OWNER-EDITS.json`'s r08-room-his and r09-room-first now check his decisions, not the wording). Enforced: `suggestion_review.py` refuses a stretch to edit without "whose" (his own, or he asked) and card text calling the model's text his; `pangram_ledger.py predict --his` takes only "his own: ...", with `--unchanged` for text as it stands; `sense_receipt.py make --his` needs `--whose`. Round 10 withdrawn (its page now says so). The stretch, fixed by me: eight versions, each with its receipt and fresh newcomer reads, two tell panels, the linter clear from try 7: all read AI, 100%; the whole section in place reads AI in one 453-word window, his dangers paragraph included (`humanize/h09-20261106/RESULTS.md`).
- 2026-11-06 (turn 16, his message of 19:43 UTC, saved as `experiments/t16-answers/JOEL-MESSAGE-20261106-1943.md`): "make the cuts regardless of pangram if it makes the guide read better". Gate E378: a cut the article's own goal calls for is made without a Pangram reason, a sentence he left standing isn't his decision to keep it, and a stuck check is not a reason to stop (`pangram_ledger.py`'s try-cap message now says so). The cuts (`experiments/t16-answers/apply_t16.py`): B240 keeps its first sentence; water, the hand on the shoulder and speaking slowly went from it, and the music paragraph B241 went, all said more fully in the Do list, Touch, Consent, and Compassion, Get One Human Anchor and the Grounding Menu; the sips moved to the Do list's "Water?" (12,308 to 12,260 words). Then the section's other AI lines, fixed his usual way: Pangram still reads the section AI, and both its halves (`humanize/h10-20261106/RESULTS.md`). Round 11's page: two cards, those lines said plainly and one paragraph moved (Bad Trips Guide, Round 11, https://claude.ai/artifact/XLrBKyfaQSjA4YRNh41Utw; `review/r11/REVIEW-R11.md`; browser test 78 of 78).

- 2026-11-06 (turn 17, his round-11 answers of 20:51 UTC, saved as `review/r11/ANSWERS-R11-20261106-2051.json`): both cards approved with no comment, PFA-PLAIN (the section's AI lines said plainly) and PFA-MOVE (the practice paragraph before the next-step one). In by `review/r11/apply_r11.py` (12,260 to 12,279 words; `OWNER-EDITS.json`'s r11-pfa-plain checks his wording and the order). The fidelity keys record what the approved card said in other words (`humanize/h01/FIDELITY-KEYS-R11.json`: "wary of" for "don't trust", "sort out the rest of your life tomorrow" for "solve your life tonight", "stopping the practice", "food and warmth" and "Protect their sleep" for the practical-move line). That showed a bug in `fidelity_keys.py`: a change recorded as "don't" never left its unit, so the room line's last key, "bathroom", still there, was matched to another paragraph and reported lost; fixed, with a test. Then the section: his dangers paragraph reads Human alone and with the heading, and every room paragraph after it (eleven wordings, its reason sentence alone, its acts alone) turned all of it AI; heading, intro, his paragraph and his fixes line read Human Written (3bd48be6, `humanize/h11-20261106/RESULTS.md`). Every point of the room paragraph is said in its own place elsewhere, so it is cut as a repeat (`experiments/t17-room-cut/apply_t17.py`, gate E378), with the bathroom and someone they're wary of moved to the Do list; the last paragraph (B246), a pointer plus sleep and meaning said in full later, turned the Human first half AI by itself and is cut too (`apply_t17b.py`; 12,279 to 12,169 words). Lesson bad-trips-2026-11-06a (`docs/lessons/2026-11-06-2051-bad-trips.md`). The reminder and the practice part each still turn the first half AI; try 3 of the section reworded them and read AI (58d85e07), and the section as the guide has it reads AI (dd66404c).

- 2026-11-06 (turn 18, his message of 22:25 UTC, saved as `experiments/t18-answers/JOEL-MESSAGE-20261106-2225.md`): "ok do i need to nudge you or you are still working". Turn 17 had ended on a report with a safe next step open: lesson bad-trips-2026-11-06b (`docs/lessons/2026-11-06-2225-bad-trips.md`), a report is no reason to end the turn. The next step done: the reminder's last two sentences and the intro line cut as repeats (`experiments/t18-answers/apply_t18.py`, `apply_t18b.py`; 12,169 to 12,125 words); the section to the reminder reads Human Written (a49943b6). The practice case rewrites lines he approved in round 11, so it is round 12's card (Bad Trips Guide, Round 12, https://claude.ai/artifact/1HFr66Lp93AeENmvGpMfh6; `review/r12/REVIEW-R12.md`); with it the section reads Mostly Human, every window Human (ecd2cd08, `humanize/h12-20261106/RESULTS.md`). Then Stillness or Movement?, checked after the Human section one paragraph at a time: every paragraph turns it AI, and my rewrites (two, the second after a tell panel) read worse than the guide's own words; one agreed sentence at a time helped once (paragraph 1, 58% to 34%), and his link moves (neuro-2026-11-06b) read worse too; every paragraph's lineage but the second has used its six tries (`humanize/h13-20261106/RESULTS.md`).

- 2026-11-06 (the session's own resume at 23:10 UTC, scheduled at the end of turn 18 so he needn't nudge): Get One Human Anchor and its repeats. Say-it-once cuts, no fidelity key in any (`experiments/t19-anchor/apply_t19.py`, `apply_t19b.py`, `apply_t19c.py`; 12,125 to 12,070 words): the committee line (it said again the section's first paragraph); the violence part's "recruit one additional calm adult or crisis professional" (Get One Human Anchor says it, violence among its cases); and Alone at 3 a.m.'s movement paragraph down to what only it says (pacing, towels, a cup, and sitting or lying under a blanket when moving makes it worse are Stillness or Movement?'s; that section and W077 unchanged, so no card). Pangram, each part after the Human section (`humanize/h14-20261106/RESULTS.md`): the first paragraph reads Human with one sentence changed (88fa84a3); the second goes from 100% to 40% said with an aside (308d1862); the two scripts read AI in every wording tried, six each, and keep the whole section and the Human section before it AI (c5fcdd50). Parts under 50 words can't be checked alone (Pangram's minimum). Then two more repeats cut (`apply_t19d.py`; to 12,025 words): Who to Contact, and When's "peer support does not replace ... crisis care" (the call-for-help part says it) and Alone at 3 a.m.'s list of services again. Who to Contact reads AI alone and 60% after the Human section; Alone at 3 a.m. 50% after it, and no better with any one sentence changed (`humanize/h15-20261106/RESULTS.md`). Round 13's two cards, Get One Human Anchor's paragraphs (Bad Trips Guide, Round 13, https://claude.ai/artifact/Eusd1vVS517ENfiTdbEQwf; `review/r13/REVIEW-R13.md`; browser test 78 passed). His answer, exported 00:01 UTC 2026-11-07 (`review/r13/ANSWERS-R13-20261107-0001.json`): both approved, no comment; in (`review/r13/apply_r13.py`; 12,048 words), the second paragraph's bold kept on the two people it names. For the Person Helping's three parts read AI, 100%, as the guide has them (`humanize/h16-20261107/RESULTS.md`).

- 2026-11-07 (the session's own resume at 00:11 UTC): Who to Contact, and When, part by part after the Human section (`humanize/h17-20261107/RESULTS.md`): the opening paragraph 63%, Human Written with its second sentence said plainly (3328665a); the lists 29%, 44%, 26% and Human; the whole section 60% to 47% with the change. Round 14's card, that one sentence (Bad Trips Guide, Round 14, https://claude.ai/artifact/3mZnazapnp3wfGJwjFrLHR; `review/r14/REVIEW-R14.md`; browser test 56 passed). For the Person Helping's opening, paragraph by paragraph after the Human section: three AI, 100%, one 60%; one-sentence changes read AI (`humanize/h16-20261107/RESULTS.md`).

- 2026-11-07 (the session's own resume at 00:27 UTC; his round-14 answer of 00:28): round 14 approved and in (`review/r14/apply_r14.py`). Who to Contact's lists after the changed opening: the first list 65%, 45% with the TripSit line said as talk (453eec39); the directories 49%, worse with either sentence changed. For the Person Helping's opening through the tell panel (`humanize/h17-20261107/panel-HELPER/PANEL.md`); its "real grief" paragraph is a repeat, but the fidelity keys hold its two warnings, so its cut is round 15's card, not an E378 cut (the guide keeps it).

- 2026-11-07 (the session's own resume at 00:40 UTC): round 15's three cards (Bad Trips Guide, Round 15, https://claude.ai/artifact/MSKNpp9YBQCXwUuo9KjLye; `review/r15/REVIEW-R15.md`; browser test 78 passed): the TripSit line (the first list 65% to 45%), the stay-present lead-in (60% to 45%), and the "real grief" paragraph cut as a repeat (his call: the fidelity keys hold its two warnings; the opening without it 79%). The Zendo summary split read AI (`humanize/h16-20261107/RESULTS.md`).

- 2026-11-07 (the session's own resume at 00:51 UTC): For the Person Helping's lists and harm part after the Human section, part by part (`humanize/h18-20261107/RESULTS.md`): the Do list 78%, the Don't list 100%, the "I am God" paragraph 47%, the script lines 52%, the redirect and safety paragraphs 78%, the emergency-services paragraphs 68%. The Don't list's items each repeat a nearby line, but each holds fidelity keys (W085, W087, and W105 for the planned-session copy), so which copy stays is a card. The "I am God" paragraph read worse with either of two sentences changed (70%, 63%), so its own words stay.

- 2026-11-07 (the session's own resume at 01:04 UTC): the harm part's script labels said differently read no better (69%, 52%; the lines stay, later list). No Rash Actions as the guide has it: AI, 100%; 64% after the Human section (`humanize/h19-20261107/RESULTS.md`).

- 2026-11-07 (the session's own resume at 01:14 UTC): No Rash Actions paragraph by paragraph after the Human section (`humanize/h19-20261107/RESULTS.md`): 38%, 100% (the lock and its list), 59%, 41%, 43%; the lock said as talk 73%; the list chained read AI. The lock's other mentions are tools or a menu item in his order, so none is cut.

- 2026-11-07 (the session's own resume at 01:26 UTC): round 16's two cards (Bad Trips Guide, Round 16, https://claude.ai/artifact/87kndi4Pbkqz5ufwtZpXC5; `review/r16/REVIEW-R16.md`; browser test 78 passed): No Rash Actions' three imperatives as one sentence (59% to Human Written) and the lock said as "Put yourself on a 24–72 hour action lock." (100% to 76%, the name kept for When the Trip Feels Amazing's reference). Both keep their bold when applied.

- 2026-11-07 (the session's own resume at 01:37 UTC): No Rash Actions' other three paragraphs as one flowing sentence each read worse (58%, 50%, 69% against 38%, 41%, 43%); they stay (later list).

- 2026-11-07 (the session's own resume at 01:48 UTC): When the Trip Feels Amazing: AI, 100%; 64% after the Human section; its paragraphs 62%, 51%, 69%, 59% (`humanize/h20-20261107/RESULTS.md`). Its danger list overlaps No Rash Actions' list; both hold fidelity keys, so which copy stays is a card.

- 2026-11-07 (the session's own resume at 01:57 UTC): When the Trip Feels Amazing's two clipped lines reworded read worse (70%, 80%); the section stays (later list).

- 2026-11-07 (01:57 resume, continued): (Re)defining "Bad Trip" and Spiritual ≠ "Getting Your Ass Kicked" checked (100% alone; their first paragraphs Human after the Human section, the not-broken paragraph and the bypassing/practice pair AI in every wording, panel included: later list). The Other Bypass: its last paragraph cut as said once (B342); with the young-parts pair said in one breath it reads Human: round 17's card (Bad Trips Guide, Round 17, https://claude.ai/artifact/CvMSkHaspNRPiaiwhZHeLj; `review/r17/REVIEW-R17.md`; browser test 56 passed). `humanize/h21-20261107/RESULTS.md`.

- 2026-11-07 (02:26, continued): Hang up the phone reads Human as the guide has it. Why Bad Trips Tend to Happen: its frame lines and causes read Human after the Human section; the not-every-lesson paragraph said in pairs reads Human in its own window (72% to 41%); the distortions list reads AI in every wording, panel included (later list). Give the Session a Beginning and an End: its list's preview cut as said once; the list reads AI (later list); its repeat of For the Person Helping's don't-force line is a card (fidelity key). Round 18's two cards (Bad Trips Guide, Round 18, https://claude.ai/artifact/33sDMncLXMKxe2z2aCXiQa; `review/r18/REVIEW-R18.md`; browser test 78 passed). `humanize/h22-20261107/RESULTS.md`.

- 2026-11-07 (02:42, continued): The Fear/Panic Loop, Dealing With Sorrow, Hand on Heart and Gratitude, and Demons, Jinn, Entities checked: three one-sentence gains (missing as contraction 47% to 21%, the hand on the heart 44% to 22%, train before the emergency 37% to 19%, each paragraph's own windows Human) and the demons safety rule as a say-it-once safety card: round 19 (Bad Trips Guide, Round 19, https://claude.ai/artifact/7J3EcDy1V89wTLg7KSXXip; `review/r19/REVIEW-R19.md`; browser test 78 passed). `humanize/h23-20261107/RESULTS.md`.

- 2026-11-07 (03:00, continued): Abuse Memories and Dealing With Shadow Thoughts checked: Shadow Thoughts' paragraphs read Human except 'During a trip, ...' (100%; later list); Abuse Memories' true-in-which-way line said as talk (38% to 18%) waits for round 20's cards; the Joker Poem is a quoted poem (unknown author), not checked. `humanize/h24-20261107/RESULTS.md`.

- 2026-11-07 (03:09, continued): After the Storm reads AI in every wording tried (later list); the Appendix reads Human. The first pass through the whole guide is done: every section read, as the guide has it and part by part after the Human base. Round 20 (Bad Trips Guide, Round 20, https://claude.ai/artifact/VjnhkppXLZLS8Kn6CavQe2; `review/r20/REVIEW-R20.md`; browser test 56 passed) holds ABUSE-TRUE. `humanize/h25-20261107/RESULTS.md`.

- 2026-11-07 (03:18, continued): the danger lists' card: When the Trip Feels Amazing's danger list cut as said in No Rash Actions, its grand purchase moved there (a fidelity key goes, so a card): round 21 (Bad Trips Guide, Round 21, https://claude.ai/artifact/39RMiW1JzaYTKSpwzwCLGS; `review/r21/REVIEW-R21.md`; browser test 56 passed). `humanize/h26-20261107/RESULTS.md`.

- 2026-11-07 (03:25, continued): the later list's one-try parts (touch, the loop breaker, Minimum Viable Integration, the kinds of aftermath) got one sentence changed each; none gained. The helper's don'ts against the opening and the harm part: each adds what the others lack, no card. Everything that doesn't need his answers is done for this pass.

- 2026-11-07 (turn 23, his message of 12:08 UTC with round 19's answers; saved as `experiments/t23-answers/joel-20261107-1208-message.txt`): every card of rounds 12 to 21 approved, 18 in all, none revised or rejected (rounds 19's export, the rest read from each page's saved decisions: `review/rNN/ANSWERS-RNN-20261107-*.json`). All in by `review/apply-20261107/apply_rounds.py` (11,976 to 11,908 words); `OWNER-EDITS.json` has an entry per card (55 pass); the fidelity keys record the approved losses (`humanize/h01/FIDELITY-KEYS-R21.json`: HELPER-GRIEF-CUT's W083 and W084, AMZ-DANGER-ONCE's W099 and its "3"; PASS). His two rules, now the repo's (`docs/lessons/2026-11-07-1208-bad-trips.md`): ask only where the meaning might change, there's a downside or the words are his own, every other tested change going straight in (bad-trips-2026-11-07a; `suggestion_review.py` refuses an approve card without "ask_because"); read his record first (bad-trips-2026-11-07b; `tools/humanization/approval_record.py --article bad-trips`); and when no wording reads human, the one or two paragraphs he could teach the most from, with my best tries (bad-trips-2026-11-07c). Round 22 is that: the not-broken paragraph and After the Storm's first paragraph, each tried once more first (56% and 100%; `humanize/h27-20261107/RESULTS.md`), as stretches for him to edit (Bad Trips Guide, Round 22, https://claude.ai/artifact/SgcKhA2rxHFRqGPN6yrrEk; `review/r22/REVIEW-R22.md`; browser test 62 passed).

- 2026-11-07 (the session's own check-in at 14:13 UTC): he answered round 22's first card on the page (13:51 to 14:02 UTC; `review/r22/ANSWERS-R22-20261107-db.json`) with two Pangram links to his own tries of the not-broken paragraph. They differ only in "It's not that you're damaged for good ..." (AI 99.99%) against "I might feel in the moment like you're damaged for good ... But more likely ..." (Human), so the denial was the tell (lesson bad-trips-2026-11-07d, `docs/lessons/2026-11-07-1402-bad-trips.md`). His version is in with two typos fixed, reading Human at High after the base (bad-trips-2026-11-07e). His move ("it might feel like X, but more likely Y") carried to the guide's other denials: six read Human and went in without cards (unhookable, the fruit of insight, the lesson line, No Rash Actions' urgency line and experience-content paragraph, Sorrow's deepest utility). Six stayed (touch, the bypassing pair, the fear loop, the hooks, the helper's opening, the bliss line): their tell is a list or a clipped pair, not the denial (`humanize/h28-20261107/RESULTS.md`). 12,046 words; owner edits 62 pass; fidelity PASS.

- 2026-11-07 (turn 24, his round-22 export of 15:38 UTC; `review/r22/ANSWERS-R22-20261107-1538.json`, his words in `experiments/t24-answers/`): both teaching cards answered with his own versions, both in with typos fixed (the not-broken paragraph Human High with its last sentence Medium; After the Storm's first paragraph Human, its first sentence Low beside the base's reminder). He cut "Don't rush to turn a hard experience into content" (`humanize/h01/FIDELITY-KEYS-R22.json`). Lessons bad-trips-2026-11-07f to i (`docs/lessons/2026-11-07-1538-bad-trips.md`): agency in the middle of instructions; a claim left a little unbalanced ("true (or false)"); "an" for "one" (the linter's O46 now flags "one" before any word and a noun, W123); and a fresh reader's sense read before any try (`suggestion_review.py` refuses a teaching stretch without its "sense"). His After the Storm moves carried by me read AI in 12 of 12 tries (`humanize/h29-20261107/RESULTS.md`), so round 23 asks him for the next two shapes: No Rash Actions' don't list and Minimum Viable Integration's steps (Bad Trips Guide, Round 23, https://claude.ai/artifact/1mNMZJRcdc1dfidAdpNmU9; browser test 62 passed). 12,087 words; owner edits 63 pass; fidelity PASS with R22.

- 2026-11-07 (turn 25, his round-23 export of 22:38 UTC, pasted as the whole message; `review/r23/ANSWERS-R23-20261107-2238.json`, his words in `experiments/t25-answers/`): No Rash Actions' don't list is his version, as he sent it (Human, High on his first try; in place after the Human base his paragraph reads Human, High, f14f541b). Minimum Viable Integration is cut as the repeat he saw ("i also feel like this has been said at least twice already"); what only its step 2 said (the facts to write down: what you took, how much, the setting, what set it off, what helped, what made it worse) went with it, and my merge of that into the questions paragraph read AI (QF, 82%), so it still needs a home that reads Human. His steps card covered only the list's first line: a bug in the card builder (`P()` took a list's first block), now refused in `review/r23/build_r23.py` and, for every lane, in `suggestion_review.py` (gate bad-trips-2026-11-07k). His list lesson, the fifth of his fixes in `SKILL.md` (bad-trips-2026-11-07j, tell J69; `docs/lessons/2026-11-07-2238-bad-trips.md`): take a long list apart into a short list of plain verbs and sentences built differently, each item something a reader can picture. My three tries carried right after his message still kept their lists whole and read AI (SH3 99%, AB3 68%, QF 82%; `humanize/h30-20261107/RESULTS.md`). 12,057 words; owner edits 65 pass; fidelity PASS with R23. Then (23:00 to 23:35 UTC, `humanize/h31-20261107/RESULTS.md`): his list fix carried by me to four lists, each taken apart (0 of 4 Human); two changes to his own paragraph measured what carried it (without its jokes it still reads Human; with them but in the old one-sentence form it reads AI, so his frame carries it, not the jokes); my Don't list with jokes of his kind (AI); his frame after tell panels on three paragraphs (0 of 3; the no-ceremony paragraph from AI High to Medium); Codex's rewrites from the panels' briefs with his voice lines (0 of 3). Nothing went into the guide. `SKILL.md` fix 5 and lesson j now carry the measurement. Round 24 asks him for two shapes his frame can't reach (gate bad-trips-2026-11-07c): the helper's don'ts that have to stay firm, and Give the Session's labelled bullets (Bad Trips Guide, Round 24, https://claude.ai/artifact/QiaRjeQFfPRzkBASwFudHX; `review/r24/REVIEW-R24.md`; browser test 62 passed; the list gate passes on both cards).

- 2026-11-08 (turn 26, from this account again: his round-24 export of 15:01 UTC, sent 15:07 UTC with the resume line; `review/r24/ANSWERS-R24-20261108-1501.json`, his words in `experiments/t26-answers/`): main brought in (romance and neuro de-armoring: the needed read before a model's paragraph is reworded, neuro-2026-11-08a; his new claims checked like the old, neuro-2026-11-08c). His four versions in as he sent them, "themself" fixed (`humanize/h32-20261108/apply_r24.py`): the first five minutes' reminder (one sentence for the reminder and its script, after his first check read them Medium), the helper's anchor line and don'ts under Don't, his (Re)defining "Bad Trip" (Human, every window, three Medium: c192b361) and his Give the Session (Human High, 0469ebb9; its picture and triage-app line kept). The dash swap's newer rule carried to the 19 blocks that still had spaced en dashes (`swap_dashes.py`). Why Bad Trips Tend to Happen said once under his (Re)defining (`merge_why.py`): heading and "That frame can be useful" cut, causes trimmed to the ones said nowhere else, picture, lesson line and thinking traps moved; the lesson line's cut holds warning W102, so it is round 25's one card (Bad Trips Guide, Round 25, https://claude.ai/artifact/3dKpHXmFwMSLYxDE2i9yiL). His rule that the guide doesn't assume a drug: a fresh reader's list (`humanize/h32-20261108/DRUG-READ.md`), 16 lines changed (`drug_fixes.py`), two of them in his new versions only after their checks read Human (f99fb1f0; the section 14a16456, the paragraph alone AI either way at 53 words, d7b3540f), receipts and the needed read in the folder. Fidelity `humanize/h01/FIDELITY-KEYS-R24.json` (W106, W107, W115 lose "peaking" and "intoxicated" under his rule): PASS; owner edits 63 pass; keep-as-is K18 to K20 (his joke, his guru line, his aside) and C11, C12 (his meant cuts). 12,057 to 12,368 words. Lessons bad-trips-2026-11-08a to c (`docs/lessons/2026-11-08-1507-bad-trips.md`). The helper's opening line's cut waits for that section's humanizing (its "Zendo-style" needs explaining where it is first used; `humanize/h32-20261108/NEEDED-READ.md`).

- 2026-11-08 (the session's own resume of 15:52 UTC): what carries his round-24 versions measured, each test after the Human base or alone as its link says (`humanize/h33-20261108/RESULTS.md`). His Give the Session without his Kenya story, sitter joke and redosing aside reads Human High (22506017), and his anchor line and don'ts without the demon line read Human, the don'ts Medium (2a2e7aa4): his frame carries his own words with nothing personal in them, and the demon line's break is what lifts the don'ts to High; without the story, a fresh reader found "The work is already done." unclear, so the story carries meaning too. My words in his frame read AI in all three tries on What Kind of Aftermath Is This?'s first two kinds (56% after the base, 808d56ff; alone, after the tell panel, bd962b1b; alone, written from a fresh reader's comparison of his sentences and mine, `CONTRAST.md`, 0ec38b6c), as 13 of 13 did in h31, Codex's three included. Nothing went into the guide.

- 2026-11-08 (the same resume, continued): the carry being spent, the stretches round 24 named were read for repeats instead, his first round-24 complaint (`humanize/h34-20261108/RESULTS.md`): two fresh readers quoted every other place that makes each item's point (`REPEATS-AFTERMATH.md`, `REPEATS-NAMED.md`), every quote checked, every candidate cut run through the fidelity keys, the keep-as-is ledger and the owner edits. One sentence repeated only his After the Storm lines and lost nothing, so it went ("Stabilize through sleep, food, routine, sober support, ordinary body, and ordinary world.", `dedup_cut.py`); most of the rest adds a remedy, threshold, script line or label no other line has, or holds a key or his Q-5 rule, so it stays. "Zendo-style" explained where the guide first names it, from the project's own pages, with two principles said plainly after a fresh reader's needed read (`zendo_fix.py`, `NEEDED-READ.md`). Round 26 has two cards (Bad Trips Guide, Round 26, https://claude.ai/artifact/HFHzRb4EuRmMu6J3EmZFn1; `review/r26/REVIEW-R26.md`; browser test 78 passed): the helper's opening line (it repeats his anchor line and don'ts but for "perform a rescue fantasy") and the aftermath list's trauma line (Abuse Memories says it all). Fidelity R24 PASS, owner edits 63 pass, keep-as-is 0 problems; 12,368 to 12,387 words.

- 2026-11-08 (the same resume, continued): the same repeats read for the rest of the long part (`humanize/h35-20261108/RESULTS.md`): Get One Human Anchor and Alone at 3 a.m., Hang up the phone, Dealing With Sorrow, Hand on Heart, Demons, Jinn and Dealing With Shadow Thoughts say nothing whole that another line says; the Grounding Menu, No Rash Actions, When the Trip Feels Amazing, Spiritual ≠ and The Other Bypass repeat only as menu options and local uses of a rule, each where the reader acts on it, so nothing there is cut. Then the Shadow Work opening, Psychological First Aid, Stillness or Movement? and the helper's opening and Do list: the Do list's "Offer choices instead of commands." said only what its own questions and his don'ts say, so it went (`humanize/h35-20261108/dedup_cut.py`); round 26's intro says so. Fidelity R24 PASS, keep-as-is 0 problems, owner edits 63 pass; 12,387 to 12,381 words.

- 2026-11-08 (the same resume: his round-26 export of 16:48 UTC, sent while it ran; `review/r26/ANSWERS-R26-20261108-1648.json`): both cards approved with no comment and in (`review/r26/apply_r26.py`): the helper's first sentence and the aftermath list's trauma line. The medical part and the Appendix read for repeats too (`humanize/h35-20261108/REPEATS-MEDICAL.md`): what they repeat are the call-for-help thresholds, kept both in the lists at the top and where the reader acts on them, routing lines and a remedy's cautions in its own profile, so nothing cut; the repeats pass is done for the whole guide. Fidelity R24 PASS, owner edits 64 pass (r26-said-once), keep-as-is 0 problems; 12,381 to 12,346 words.

- 2026-11-08 (turn 27, his round-25 export of 16:55 UTC; `review/r25/ANSWERS-R25-20261108-1655.json`): WHY-LESSON-CUT approved with no comment and in (`review/r25/apply_r25.py`): "Every hard experience can feel like a profound lesson. But sometimes the lesson is just to ..." cut, warning W102 an owner change (`humanize/h01/FIDELITY-KEYS-R25.json`: PASS); owner edits r18-why-lesson and h28-why-lesson-line superseded by r25-lesson-once, 63 pass; keep-as-is 0 problems; 12,346 to 12,306 words. Nothing waits on him now.

- 2026-11-08 (turn 27, continued): the overcompletion read (gate E328) of the whole guide (`humanize/h36-20261108/overcompletion/RESULTS.md`): five fresh readers, one part each, blind, given `BRIEF.md` (his definition and rulings, and this guide's two: a call-for-help threshold said again where the reader acts on it stays, a dose, timing or source is never what's cut); 39 candidates, each run through the fidelity keys, keep-as-is and owner edits (`check_candidates.py`) and read by hand. Nine went in (`cut_overcompletion.py`): restatements, a closer, two previews and a sentence repeating its heading, none losing a point, key, kept line or owner edit. The rest stay, each with its reason; No Rash Actions' "experience-content" lines failed their needed read as a cut (they explain the term, `NEEDED-READ.md`). No card. Fidelity R25 PASS, owner edits 63 pass, keep-as-is 0 problems; 12,306 to 12,173 words.

- 2026-11-08 (turn 28, his messages of 17:22 and 17:24 UTC, `experiments/t27-answers/joel-20261108-1722-1724-messages.txt`): his answer to turn 27's question ("give me your best tries and what would teach you the best and i'll do that") with a rule for every lane, humanizing after the article makes sense (bad-trips-2026-11-08d), and a second: the guide "lost my actual beliefs or like maybe they got put in one corner ... it's not all the generic trip safety advice you could find with any ai search" (bad-trips-2026-11-08e). Both in `docs/FIXING-AN-ARTICLE.md` (sections 6 and 4) and `docs/lessons/2026-11-08-1722-bad-trips.md`. Two fresh readers on his beliefs (`humanize/h37-20261108/beliefs/`): what of him dropped out between his post of 2026-11-03 and the guide (LOST.md), and where the guide is generic where a belief of his would change what the reader does (GENERIC.md).

- 2026-11-08 (turn 28, continued): the beliefs reads (`humanize/h37-20261108/RESULTS.md`): 18 lines of his post's framing gone (LOST.md) and 15 places where the guide is generic where his belief would change what the reader does (GENERIC.md; the sections used in trouble carry least of his method). Three of turn 27's overcompletion cuts were among the lost lines, so they're back as they were (`restore_my_cuts.py`; the shared rule now says a repeats or overcompletion read keeps his why). Round 27 (Bad Trips Guide, Round 27, https://claude.ai/artifact/69kipTsshviuZ3zPcaaDFp; `review/r27/REVIEW-R27.md`; browser test 84 passed): two sentences of his post back where they bear (BACK-HIERARCHY-WHY, BACK-GROUNDING-LOVE, receipts and needed read) and two teaching cards, each sense-read first (TEACH-LOOP, TEACH-AFTERMATH). Fidelity R25 PASS, owner edits 63 pass; 12,173 to 12,225 words.

## Current checkpoint

- **In progress:** Turn 28 (his messages of 2026-11-08 17:22 and 17:24 UTC): his two rules in; his beliefs read; round 27 out.
- **Next step (updated on every push, so another account can pick up here):** Round 27's answers when they come (Bad Trips Guide, Round 27, https://claude.ai/artifact/69kipTsshviuZ3zPcaaDFp): an approved put-back goes in as its card has it; his two teaching versions go in as he sends them, and what they carry (his method at the moment of use) goes to the generic places GENERIC.md names, each sense-read first and tested, the ones that read Human going straight in; a belief of his goes in his words only. Meanwhile, nothing that humanizes: the word-for-sense read (gate E331) of the whole guide, which comes before humanizing under his rule (bad-trips-2026-11-08d). Not carded yet (`humanize/h37-20261108/RESULTS.md`): his post's "the deeper question: is this sorrow, fear, shame, inner-child material, demons, jinn, ..." ("jinn" would come before the guide explains it). Still open: Minimum Viable Integration's facts to write down need a home; the questions paragraph's tell panel; "harm reduction" explained in the MDMA section if needed. Fidelity checks use `humanize/h01/FIDELITY-KEYS-R25.json`. No whole-guide check until no window already seen reads AI or Low (E354).
- **Waiting on Joel:** round 27's four cards (recorded once, not checked).

## Remaining

The Psychological First Aid section (it reads AI in place, both halves too); the rest of the guide one paragraph at a time; the whole-guide Pangram check; an overcompletion read
(gate E328); the word-for-sense read (gate E331); his post updated, with the title's version and date (gate E323).

## Blockers / unresolved

None.

## Evidence / artifacts

`experiments/t01-repeats/` (prompts, the three reports, NOTE.md), `review/r01/` (build script, cards, page, its cards
as Markdown, his answers, the apply script), `review/r02/` (round 2's page), `GUIDE-SO-FAR.md` (the guide after round
1) with its blocks and page form, `OWNER-EDITS.json`, `humanize/baseline-20261103/` (the checked text, the badge note,
the full analysis's windows), `humanize/pangram-ledger.jsonl`.

## Next safe action

`HANDOFF-bad-trips.md`, START HERE.
