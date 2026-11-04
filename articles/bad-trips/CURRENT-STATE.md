# Bad Trips guide: current state

Updated: 2026-11-04 (turn 8, his round-4 answers and message of 14:58 UTC). Registered 2026-11-03 at Joel's message of 15:45 UTC ("start working on humanizing my
badtrips guide at badtrips.u-dont-exist.com"; `experiments/t01-answers/JOEL-MESSAGE-20261103-1545.md`).

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
  https://claude.ai/artifact/12uJZXZ5xptJoYQjoXQJKq).

## Current checkpoint

- **In progress:** Turn 8: round 5's page (one card, the CBD paragraph in his words) is with him.
- **Next step (updated on every push, so another account can pick up here):** The humanize pass, section by section, starting now (it doesn't wait on round 5). No whole-guide check first: by pull request 293's E354 (Joel, 2026-11-04 14:41 UTC: "no the whole article doesn't decide, we need to first fix any windows we can see before we check the article"), every window already seen reading AI or Human at Low is fixed before the article is checked, and about three quarters of the guide (118 of the published post's AI or Low windows, about 9,250 words, matched by six-word runs) is still text that the baseline read so. Order: the sections with the most AI High words first; in each, the gate's writers, the tell panel (`tools/humanization/tell_panel.py`), `compare_read.py` and fidelity against `humanize/h01/FIDELITY-KEYS-R04.json`, one paragraph at a time where a section reads AI (E343), each sentence following the one before (E351), a ledger prediction before every Pangram check (`pangram_ledger.py predict`). Sections of 5 or 6 paragraphs go to Pangram's web app; many at once to a temporary Substack draft, whose secret link opens in his Brave from his laptop's shell (`brave-browser-stable '<link>'`, E353: the browser Claude in Chrome drives is not one he can see), and he sends the feed link. The Active Seizure section's other paragraphs read AI High (B109, B110, B112) and wait for his CBD paragraph, so the section is checked once. His round-5 answer goes in with an `apply_r05.py` like round 4's (the page's export as `review/r05/ANSWERS-R05-*.json`; his own version as he wrote it, with W-CBD2's three links on the words that name the same sources: the FDA label https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/210365s024s029s030lbl.pdf, the 12-week trial https://pubmed.ncbi.nlm.nih.gov/35802375/, the 2025 study https://pubmed.ncbi.nlm.nih.gov/40673944/).
- **Waiting on Joel:** round 5's card (the CBD paragraph in his words, or Keep).

## Remaining

His CBD paragraph (round 5); the whole-guide Pangram check; the 5 generic lines the check left for the humanizing; an overcompletion read (gate E328); the
humanizing of every section that reads AI or below High, by the gate's own writers (Emulate is no longer used on his writing, Joel 2026-11-03); the word-for-sense read
(gate E331); his post updated, with the title's version and date (gate E323).

## Blockers / unresolved

None.

## Evidence / artifacts

`experiments/t01-repeats/` (prompts, the three reports, NOTE.md), `review/r01/` (build script, cards, page, its cards
as Markdown, his answers, the apply script), `review/r02/` (round 2's page), `GUIDE-SO-FAR.md` (the guide after round
1) with its blocks and page form, `OWNER-EDITS.json`, `humanize/baseline-20261103/` (the checked text, the badge note,
the full analysis's windows), `humanize/pangram-ledger.jsonl`.

## Next safe action

`HANDOFF-bad-trips.md`, START HERE.
