# Status: hypnosis guide humanization (newest on top)

## 2026-10-22, after Joel's message of 21:41 UTC (the pull request; answer 12, batch 471g; the screening read; bf's meaning work; the second screening post; Nibbāna's HTML)

**The pull request** ("the pr has conflicts"): main had taken the Inner Child lane's pull request 218, with a conflict in
`state/PANGRAM-SCORECARD.md` (regenerated with `pangram_ledger.py build`, merge afc6ea1b), then its 220 twenty minutes
later, with one in `docs/HUMANIZATION-GATE.md` (both new lesson sections kept, merge 9dff534e). Joel merged 219 at 22:16
UTC. `tools/humanization/lane_push.py` now runs CI's checks with bare Python before the push (a new test had needed
BeautifulSoup, which CI doesn't install; it skips without it now) and ends by saying whether the pull request can merge.

**The first screening post's result** ([his link](https://www.pangram.com/feed/e836ef9c-c964-4012-a5af-994ef88658eb), Mostly
Human Written, 8.6% AI, 12,253 words): windows read from the page's props, the text rebuilt from the payload (SHA-256
equal), each sample's windows cut by `screen/SPANS.json` (`screen/SCREEN-RESULT.json`). HG17: S2 (emu-bd) and S4 (emu-bf)
Human in every window, S1 and S3 Mixed; Appendix C: S5 (emu-bg) Mixed, its opening, statement, four tests and last
sentence red and its middle Human; S6 (emu-bh) red nearly throughout. Ledger: S4 right (Human at 0.55), S2 a miss
(explained), S1, S3, S5 and S6 right.

**Joel's answer 12, batch 471g** (`fix-20261022/b471/`): 12 a, A, "(what I call forced adulthood)"; 12 b, A, nothing;
12 c, the three roles kept with his clarification after the step. Round 1: the item review OK on both, the march with no
lost break, the stance check four findings: two drifts of the installed words (the "be able to fly" simile, the step's
lost jobs), fixed in round 2 ("like telling a baby bird to just fly"; "(Nurturer to warm, Protector to make it safe, and
Guide to point a direction)"; `r2/VERIFY-r2.md` OK), and two answered (his own term; "an inherited inner critic", kept as
said under answer 10). The gate (`batch/GATE.json`; lint FAIL in both versions on the same rules), the forecasts
(`batch/PREDICTIONS.md`), installed with `apply_edits41.py --add EDITS-471g.json`.

**HG17 from sample bf** (`fix-20261022/hg17-bf/`): its meaning check in three parts (`VERIFY-part1.md` to `part3.md`: kept
169, changed 52, lost 30, added claims 10). The fixes are drafted per part by an Opus reader against a triage brief
(`FIX-BRIEF.md`; `FIXDRAFT-partN.json`): only what a reader acts on, inside bf's own sentences, a reason for each item let
stand. 31 of the 32 drafted fixes went in (one cut of two harmless orientation questions left out), Joel's 11 b word for
word, the published headings (bf's run-in headings taken out of their paragraphs), the three links
(`make_hg17_bf_fixed.py`: `HG17.bf-fixed.json`, `SECTION.md`, `CANDIDATE.md`, `CHANGED-PARAS.json`). Reviews
(`make_hg17_bf_reviews.py`): the fix check (`FIX-CHECK.md`: 27 of 28 changed paragraphs OK, the 28th Joel's own 11 b
wording, answered; the audit of the 70 let stands found no disagreement); the cold read (`SENSE-HG17.md`: four unclear,
three fixed in round 2, the fourth the published design); the march (no break lost; the playlist line is now short enough
for the march to skip); the linter (`lint-compare.json`: two fixes reworded in round 2 and one in round 3, each for a rule
bf's paragraph didn't have). Round 2 (`r2/VERIFY-r2.md`: 5 of 5 OK; `r2/march/`). STANCE_STATUS

**The second screening post** (`fix-20261022/screen2/`, the same draft, its body cleared and pasted with the lane's helper;
words SHA-256 equal; the rendered paragraphs' textContent hashes to `TEXT-S2.txt`): Appendix B's stretch as installed
(B0), Appendix C as installed (C0), and two new openings with bg's middle and C0's end (C1, C2), to tell whether the
recheck's red window was Appendix B's lists or Appendix C's opening, and which opening reads Human. Predictions first
(ledger HG31-nlp-tail#28 to HG32-c2#31, all AI, 0.30 to 0.40). It waits on Joel's Brave.

**Nibbāna**: his editor HTML of 21:41 UTC (`articles/nibbana/humanize/source/substack-editor-20261022.html`) rebuilt the
way the check reads it is the checked text exactly; the rebuild tool learned three rules on the way (an embedded note's
straight quotes, trailing spaces, emoji joiners), with tests. Queued after this guide.

## 2026-10-22, after Joel's message of 18:37 UTC (the recheck read; answers 9 to 11, batch 470g; the screening post)

**The recheck's results** (his two links): [part A](https://www.pangram.com/feed/c8001eb5-84a6-41dc-a2c0-0f4733dc3fc7),
the whole guide to inside Appendix B, AI Detected, 13.8% AI; [part B](https://www.pangram.com/feed/558d14f6-625d-46aa-8495-adf9141cb3a4),
the appendices, Mostly Human Written, 4.9% AI. Red: the induction section (HG17) from its first paragraph to the shortcut,
most of its windows marked "humanized", with light or dark green only in Before you begin's steps 4 and 5, the sleep
paragraph, "Either way is ok" and Deepening, if useful; three short windows of the return (HG18); Appendix C's general
checklist as prose, one 518-word window, high. Dark green: every other section, the NLP appendix's Human version
included. In the ledger, HG-whole#21 (AI at 0.03) is right and HG-rest-B#20 (AI) is a miss, explained ("verdict
threshold misread": one red section in 10,444 words reads Mostly Human); batch 469g's forecasts are 15 of 15 right
(`fix-20261021/b469/batch/SCORE.md`). The windows were read from the page as one compact line each and the text rebuilt
from the payload (`tools/humanization/substack_check_text.py`, new: SHA-256 equal to the page's), instead of the 25,000
tokens of checked text a half used to cost.

**Why the induction section read AI**: its sample, ba, had been chosen by meaning alone; under gate E200 no sample went
through a Pangram screen, while HG18's, which reads Human, had been chosen by its screen. So six new samples
(`fix-20261018/make_emu_bc.py`, run on the laptop; each output's SHA-256 checked against the laptop's) go through a
screening post first: two of HG17 from the published text (emu-bc, emu-bd), two from the installed fixed section with
Joel's 11 b (emu-be, emu-bf), two of Appendix C from my prose (emu-bg, emu-bh). The post
([TEMP screen (hypnosis guide samples)](https://ibogaqueen.substack.com/p/8f4644c8-8bda-4321-8437-8a09148353cc?postPreview=paid&updated=2026-10-22T19%3A26%3A08.747Z&audience=only_paid&free_preview=false&freemail=),
draft 221684747; `fix-20261022/screen/`) was pasted with the new helper (words check: 12,184 words, SHA-256 equal), and
its rendered paragraphs hash to `TEXT-S.txt` (63,635 characters), so the check reads exactly that. Predictions first
(ledger HG17-emu-bc#22 to HG32-emu-bh#27: AI for S1 to S3, S5 and S6, Human at 0.55 for S4). It waits on Joel's Brave.

**Joel's answers 9 to 11, batch 470g** (`fix-20261022/b470/`): 30 edits in 23 paragraphs and 3 headings. 9: the guards
are childhood protector parts where the guide first uses the word, where it explains them (with his reason: "It's what
protects you when your consciously installed parental Protector isn't functioning, the same as when you were a child."),
and where anxiety or a negative state is put down to one, the synchronicity cue included. 10: the Inner Child article's
names (his table of 13:22 UTC, the core names, his nutshell): the h1 gives the inner adult three jobs; their first
naming is "your loving Nurturer, your safe Adult Protector (hereafter just the Protector) and your wise Guide"; Guide for
Leader/Guru throughout, Leader and Guru kept among the names a reader can choose; one name for the inherited parent,
"inherited parent script", explained once. 11 b: "If you are overwhelmed by chemicals, acutely confused, or not able to
keep yourself safe, ...". Four rounds of reviews: round 1, an Opus reader of each change against his answer, its meaning,
the names and its sense in place (`r1/REVIEW.md`: five CHANGED), a cold read of the h1 (`r1/SENSE-HG14.md`: the line to
say could be said to the script), the stance check (`r1/STANCE.md`: six conflicts in the changed paragraphs, all in the
installed versions' words, and fifteen places where the published text pulls against his positions, most of which the
batch fixes) and the march (no paragraph lost a break); round 2 fixed four of round 1's five with the reader's wording
(`r2/VERIFY-r2.md`: OK); round 3 put five of the stance check's conflicts right in the same paragraphs (reparenting
doesn't wait, "no value for its resume", the Protector and the Nurturer's limits, "as objectively and clearly as I can";
`r3/VERIFY-r3.md`: OK), with the sixth answered in `gate-answers.json`; round 4 reworded three of my phrases that brought
linter rules the installed paragraphs didn't have (`lint-compare.json`; `r4/`). Appendix B's "Put 3 good adults in" (the
review and the stance check both) is question 12 c with the invocation's "inner adult(s)" and Appendix K's "three-adult
arrangement"; the note's forced adulthood and learned patterns are 12 a and b. The gate: `batch/GATE.json`; the
forecasts: `batch/PREDICTIONS.md` (22 paragraphs, all Human, 0.70 to 0.90). Installed with
`fix-20261020/apply_edits41.py --add EDITS-470g.json`, each edit "pending" its reading in the next recheck.

**The Inner Child lane's note, part 1**: drafts A and B renamed without "Pangram" (reloaded to confirm); the new paste
helper `fix-20261022/screen/paste_payload_lane.js` (exact titles, an empty body only, the words check), the old one marked
superseded. The lessons are in `docs/HUMANIZATION-GATE.md`, "What Joel's answers of 2026-10-22 18:37 UTC taught".

**Pull request** [219](https://github.com/u-dont-existDOTcom/joel-articles/pull/219) carries this work (pull request 209,
the work before it, was merged on 2026-10-21 at 22:43 UTC).

**Queued after this guide: his Nibbāna article.** His result link came at 19:53 UTC
([the check](https://www.pangram.com/feed/1ffe8aed-a00a-4273-846c-635ae22b2917), made on 2026-10-20): Mostly Human Written,
4.5% AI, 22 of 166 windows AI, none "humanized"; the list and the next steps are in `articles/nibbana/humanize/QUEUE-20261022.md`.
The registered master (2026-09-28) is older than the post (the post opens "Hello Lovey Bunny!!" now), so the work starts
with his current editor HTML.

## 2026-10-21, the listening script installed (my check-in of 20:13 UTC; Joel's recheck results hadn't come in)

**The induction section (HG17), sample ba with every point back** (`fix-20261018/rf-zg/make_hg17_fixed.py`,
`HG17.fixed.json`, `FIXES.json`): the 30 points ba's second reader found lost are back inside ba's own sentences (the
script's pauses and steps, "What am I noticing now?", "Five.", "keep safety and exit instructions plain", the three
links), its 14 inventions are out (his father "uses" the mudra when he drives, "I always announce", "see link above",
"something like the below" with nothing below), and the changes that alter what a reader does or believes are put right.
The first pass put the points back in the published phrasings, and the linter found tells in eleven of those sentences
that ba didn't have (E186 "without ...ing", O9 "not Y" tails, O6, O14); they were reworded plainly before any reader saw
them (a lesson in `docs/HUMANIZATION-GATE.md`, "A lost point goes back in the sample's words").

**Three rounds of reviews** (`rf-zg/`): round 1, the cold read in the guide (`SENSE-HG17.md`: six UNCLEAR), the stance
check (`STANCE-HG17.md`: five conflicts, and one contradiction in the published text itself) and the march (`march/`);
the whole-section meaning check ran past its reader's 64,000-token output limit and wrote nothing, so it ran again in
three parts (`HG17.fixed.verify.part1-3.out.md`: kept 196, changed 28, lost 2, added-claims 9 over the three). Round 2
fixed the cold read's six and the stance check's five (what you leave alone had become optional, "communion with things",
drills before any other use, the adult self tied to an adult body, help for any leftover response) and gave two paragraphs
their break back; round 3 fixed the meaning parts' two lost points ("simple", "Give it time") and the changes a reader
would act on ("the Adult" capitalized twice, "say out loud", the room's sound, Appendix B's "richer language tools", and
the rest in `make_hg17_fixed.py`, REVIEWS). Each round's fixes were read again in place by a fresh reader
(`r2/VERIFY-r2.md`, `r3/VERIFY-r3.md`: every finding answered, every sentence's sense OK). What was let stand is in
`gate-answers.json`, each with its reason. The march: ba had 20 of 53 changed paragraphs with a break, the fixed text 24
of 55. The gate (`batch/GATE.json`, `make_gate_hg17.py`): an edit of an Emulate text, linter FAIL as ba's own (E23, B13;
no rule the sample didn't trip), cold read, meaning and stance clear; `hg17.js` written, not run (gate E200).

**Installed** with `tools/install_fixed.py` (the working copy now equals `rf-zg/CANDIDATE.md`; the 4.1 edits all in;
`fix-20261018/installed.json` HG17, "pending its 4.1 reading"). The published text's own contradiction (no exploratory
hypnosis when "intoxicated", against the Already open? practice for a state loveyhuasca opened and his own loveyhuasca
sessions) is question 11; until he answers, the section says what the published says, without the "otherwise" that made
every intoxicated reader one who can't keep safe.

**The recheck's part A, pasted again** (`fix-20261020/substack41r/make_recheck.py`; part B's payload unchanged, SHA-256
0072d5d0...): Joel hadn't opened the 19:32 links (nothing new in his History or the app's pane at 21:35 UTC), so part A
was rebuilt with the section in it and pasted into the same draft (`paste_payload.js`, `replace_title`), and one opening
reads both batch 469g and the listening script. In the ledger the unread part A prediction (HG-whole#19) is voided and
HG-whole#21 (key HG-whole-41r3-a, AI at 0.03, `make_preds_recheck3.py`) is written. New secret link for
[part A](https://ibogaqueen.substack.com/p/922161db-6015-4838-b495-3a4db7b12fea?postPreview=paid&updated=2026-10-21T21%3A38%3A01.929Z&audience=only_paid&free_preview=false&freemail=);
the old one shows the same draft (checked).

## 2026-10-21, after Joel's answers of 17:56 UTC (questions 1 to 8, his own edit, the inner-figure sweep, batch 469g; the recheck rebuilt)

**His message** (`fix-20261021/joel-20261021-1756-message.txt`): 1 yes, 2 c, 3 a, 4 d ("i am fine with all the
humanized replacements as long as we don't lose anything"; "ONE HONEST ACTION sounds super ai"), "5. no 5?", 6 b
(interactive, with context, merges considered), 7 b, 8 a (he fixed it himself:
[his check](https://www.pangram.com/history/18cfa70c-5f9e-4828-a9e7-68829d774e13), Human, 362 words,
`fix-20261021/JOEL-CHECK-18cfa70c.json`), and the conflation: "check the guide for that conflation bc i have seen it
before as well (and send this to the inner child guide chat to make sure also)".

**Installed:** his two edits of HG15 (`EDITS41.json` HG15-joel-p9 and -p11; the working copy's B187-B198 equal his
check's text); HG31 as `rf-z/HG31.v3.json` (3 a) and HG18 as `rf-zf/HG18.smp1.json` (4 d), with `tools/install_fixed.py`.
`apply_edits41.py` now handles an edit superseded by a later one (HG15-p11t under his edit) and an edit whose new text
contains its old text (b469-HG18-stopped-press would have gone in twice; `tests/test_apply_edits41.py`).

**The inner-figure sweep** (`fix-20261021/CONFLATION-SWEEP.md`, an Opus reader with the guide's map and his fix as the
example; prompt `CONFLATION-PROMPT.txt`): six findings; the batch's stance check found a seventh ("Protector parts" in
"You get anxious"). Four came in with plainer rewrites, three were in the published text. The sweep's reader had read the
working copy before HG31 and HG18 went in; I swept those two myself (one line, the synchronicity cue's "my Protector",
is question 9).

**Batch 469g** (`fix-20261021/b469/`, `make_b469.py`): Appendix C's general checklist as prose (2 c); HG18's lost
points (the body's contact, "hear the room, name where you are", pressing feet or hands after the eyes open when a
recording stops; and the cold read's two catches, "the five steps listed above" and a stray quotation mark); six
inner-figure fixes. Four rounds of reviews: round 1 (`r1/`: march, cold reads of HG32 and HG18, the meaning check, the
stance check, `CONFLATION-REVIEW.md` for the fixes in context), round 2 (`r2/`: Appendix C given questions and a
particular, the meaning check's catches; the stance check's four conflicts), `VERIFY-r3.md` and `VERIFY-r4.md` (each
put back a published meaning). `gate-answers.json` answers what was answered rather than fixed; `GATE.json`: every edit
clears the gate except Appendix C's prose, which has no break in its march read (the reader took every question in it
for the checklist's next step).

**No pangram.com check this turn (0 credits).** Main's rule of 2026-10-21 00:49 UTC (gate E200: many paragraphs go
through free Substack posts, and a paragraph goes to pangram.com alone only when a segment points at it) came in with the
merge of main (PR 207). So 469g's edits went into the working copy with "paragraph_result": pending, and their reading is
the recheck. Each changed paragraph's forecast is in `b469/batch/PREDICTIONS.md`.

**The recheck, rebuilt** (`fix-20261020/substack41r/make_recheck.py`; merge PASS; part A 28,019 words, part B 10,725):
pasted into the lane's own two temporary drafts, not new ones (`paste_payload.js` now replaces a draft's body only when
its title, given as `replace_title`, starts "TEMP Pangram"; both titles were renamed to that form), paid view, secret
links: [part A](https://ibogaqueen.substack.com/p/922161db-6015-4838-b495-3a4db7b12fea?postPreview=paid&updated=2026-10-21T19%3A23%3A15.548Z&audience=only_paid&free_preview=false&freemail=), [part B](https://ibogaqueen.substack.com/p/8051254d-8771-45cb-baa3-ff3fd295587a?postPreview=paid&updated=2026-10-21T19%3A25%3A03.905Z&audience=only_paid&free_preview=false&freemail=). The pages show the new text (checked on part A: the new lines in, the old out,
one copy). Predictions in the ledger before the check: HG-whole#19 (AI, 0.02) and HG-rest-B#20 (AI, 0.05), each with
what it decides; #17 and #18, the first build that was never read, were voided earlier.

**Lessons** (`docs/HUMANIZATION-GATE.md`, "What Joel's answers of 2026-10-21 17:56 UTC taught"): keep the inner figures
apart, with `tools/humanization/conflation_sweep_prompt.py` for every lane; "one honest action" (O44, W94); a saying as
people say it (J59); say what is lost (J60); a missing comma isn't a human tell; links on the pages too
(`tools/humanization/owner_refs_check.py`, `tests/test_owner_page_checks.py`); a review of repeats is a conversation.
The ledger's `cap_for` (question 7 b). Main's E200 to E204 and `docs/FIXING-AN-ARTICLE.md` arrived with the merge; the
budget doc's conflict was resolved keeping both.

**The Inner Child chat**: no channel from this session (ListAgents shows none), so the lesson is in the shared gate and
Joel has a note to paste there (questions page).

**Drafts**: E204 asks the worker to delete its drafts when done; I reused the two, and deleting them is Joel's (a
permanent deletion is outside what this worker does).

**The listening script (HG17), after the update to Joel at 19:32 UTC**: three Emulate samples of the whole induction
section from the published text (`fix-20261018/make_emu_az.py`, emu-az, emu-ba, emu-bb; 2,012 words each; the outputs
were read from the laptop and written here, each SHA-256 matching the laptop's file), aligned and composed
(`fix-20261018/rf-zg/`), and a second reader on each: ba keeps the most (156 points kept, 57 changed, 30 lost, 14
inventions; az 122, 76, 31, 9; bb 133, 68, 34, 21). The fixes on ba are next (the handoff's step 3).

## 2026-10-21, after Joel's messages of 23:32 and 23:54 UTC (both halves read in 4.1; the first fixes; the recheck waits on his Chrome)

**The whole guide in 4.1, both Mixed** (Substack's check, free; each result's every window is in
`fix-20261020/substack41/RESULT-41a.json` and `RESULT-41b.json`, mapped onto the guide's blocks by
`fix-20261020/result41/map_windows.py`). Part A ([feed](https://www.pangram.com/feed/fd91cf34-925f-48ca-8100-5fee8d5766c4))
read only the post's first 99,999 characters, 18,391 of 26,853 words, to Appendix B's first pattern: red in the two
scripts as published (2,301 words in one run), Appendix B as published from its start, the bridge into the scripts, and
two sentences each in "Why doing it myself worked better for me" (HG12) and "When “your voice” is everybody else’s voice"
(HG15, low). Part B ([feed](https://www.pangram.com/feed/6a48b3ce-6631-4c99-aec3-b127409dc2f8)), from "Appendices" to
the end (Joel ran it at 23:54): red in Appendices B and C as published (2,280 words in six windows), one instruction in
Appendix D (low) and two sentences of "Forgiveness without bypass" in Appendix F. Every other installed section read dark
green, with light green in a few sentences. Both predictions were right (AI, chance 0.01 each).

**The 4.1 risk read over-flagged** (`fix-20261020/result41/FORECAST-SCORE-41.md`): 166 sentences forecast red, 63 of them
read red (38%), and it named a sentence in 15 of the 23 red windows. The lesson is in `docs/HUMANIZATION-GATE.md`.

**Joel's 23:54 message: I run the Substack check myself** ("i imported my substack cookies so you just go to:
https://ibogaqueen.substack.com/publish/post then paste in the substack html then click the preview button ..."), quoted
in full in `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`, "Running the Substack check myself".

**Batch 467g** (`fix-20261020/b467/`): the seven red sentences' fixes, each paragraph alone and each section whole; the
gate's reviews held six first wordings before any call (three lost their paragraph's only break, four changed what the
line says). Passed and installed
through `fix-20261020/apply_edits41.py` (the list `EDITS41.json` keeps each edit with its checks): HG12's restating closer
cut ([check](https://www.pangram.com/history/add7ee33-578f-4e04-80a5-2b64858ebc0e)) and its story's closer said plainly
([check](https://www.pangram.com/history/3f7838aa-37a9-4eb5-b2b7-6733a7e2940b)), HG12 Human whole
([check](https://www.pangram.com/history/f2fa8fa3-2e64-4f8b-8e4c-9a102ceb5c32)); HG15's "inner parent" back to the guide's
"inherited parent" ([check](https://www.pangram.com/history/8e342f67-3726-4e97-86b5-87d941abbc5b)); Appendix D's
breathing steps as two sentences ([check](https://www.pangram.com/history/518ba839-31c3-4938-9b09-93f2a42874c9)),
Appendix D Human whole ([check](https://www.pangram.com/history/25912495-df6a-4a87-9f71-07b290424bbd)). Read AI: HG15's
"buy belonging" sentence ([check](https://www.pangram.com/history/6e97d63f-765f-4e8d-aecc-39ca783c05fa); the section
Mostly Human with only that sentence red, [check](https://www.pangram.com/history/9cfccd99-95ce-49b0-a65a-47216c218f42))
and the forgiveness couplets ([check](https://www.pangram.com/history/25833096-c587-4602-b24d-ba7affdfbcf3); Appendix F
Mostly Human, with two installed lines AI, low, that were light green in part B,
[check](https://www.pangram.com/history/74763536-ab88-4ec2-b347-0e186b0208ad)). Predictions: 6 of 10 right; each miss
is explained in the ledger.

**Batch 468g** (`fix-20261020/b468/`): the second tries for the two misses and the first 4.1 tries for Appendix F's two
lines that read AI (low) in its section check, each paragraph alone or with its neighbor. Round 1 of the gate's reviews
(`b468/r1/`) held the quoted promise (joining its three sentences took out the permission, its break) and found four
meaning changes; all were fixed before the call. Results:
- Appendix F's forgiveness list said about the people: Human, high
  ([check](https://www.pangram.com/history/637e6fb4-3a47-4fe6-899f-b5ff0923e7f3)). Installed.
- The self-forgiveness lines: Human, high
  ([check](https://www.pangram.com/history/fb5462fd-54ca-4993-a909-0072386f60bb)). Installed.
- HG15's "real gifts / buy belonging" closer in Joel's own concession frame: AI, high
  ([check](https://www.pangram.com/history/b252243a-a20d-4f01-8643-7551ffcb5d56)). Two tries of one mechanism, so it went
  to Joel as question 8; it stays as installed.
- The quoted promise with its two promises joined: AI, low
  ([check](https://www.pangram.com/history/2b0c9b19-25e2-4855-a867-42c9992b575b)). It read light green in the whole guide,
  so it stays as installed (the budget rule's light-green rule).

Predictions: 2 of 4 right; both misses are explained in the ledger (the merged closer got redder each try; the
concrete clauses worked better than I gave them). Lessons are in `docs/HUMANIZATION-GATE.md`. `fill_preds.py` had
counted an AI call that read Mixed as a miss; fixed, with a test.

**The recheck through Substack** (`fix-20261020/substack41r/`): `make_recheck.py` rebuilt both parts from the working
copy with its six 4.1 edits (merge PASS; canonical generator; clipboard test), and the predictions are in the ledger
(`HG-whole#17`, `HG-rest-B#18`, try 2 of 2 each). I made both drafts in the app's browser with Joel's steps, using
`paste_payload.js`, which checks the payload's SHA-256 before pasting it as a paste event. I set the "Paid subscriber
view" and opened the secret links. The Pangram label never appeared there: it comes from the Pangram Chrome extension,
which the app's browser doesn't have, and Joel's Chrome isn't connected. The two links went to Joel to open in his
Chrome (questions page, "For you to do").

## 2026-10-20, after Joel's message of 22:01 UTC (the whole guide's first 4.1 check, through Substack)

**His message.** He signed in to Pangram in the desktop app's browser, and: "for very large pangram checks (not just one
section, but like whole article especially) you can just ask me to make a temporary article on substack to check it
free" (Substack's check uses his Pangram account without his credits). He also sent his final community article with
the edits he and GPT made after 4.1 flagged them; the lessons are in `docs/HUMANIZATION-GATE.md`, "What Pangram 4.1
flagged in the community article", and in the brief `tools/humanization/reviewer/pangram41_risk.md`.

**Question 5 is settled** (option b, now free): the whole guide in one 4.1 check through a temporary Substack post, with
the four open sections as published (their defaults); then only what it flags, paragraph by paragraph on pangram.com
within the six tries; then the recheck through Substack. His Pangram History had no 4.1 checks of the guide (read free).

**The copy page** (`fix-20261020/substack41/`): `HUMANIZED-SO-FAR.md` merged into his editor HTML of 28 September with
`tools/humanization/substack_merge.py` (PASS: 8 native objects byte for byte, 26,819 words equal to the working copy's,
43 links), then the canonical generator (init, build, verify: one segment) and the clipboard test (both paths pass);
receipt `HELPER-RECEIPT-20261020.json`. The merge first failed on this guide's editor HTML, which has 125 blockquotes
(some of several paragraphs), an image inside a blockquote, and line-broken paragraphs the Markdown had joined, and the
working copy has list items of its own. The merge now puts an unchanged paragraph in the editor's own markup, keeps
blockquotes, and renders the master's list items; the community article's merge comes out byte for byte as before,
and `tests/test_substack_merge.py` covers the new cases. Sent to Joel with the request.

**The prediction** is in the ledger before the check (`pangram-ledger.jsonl`, `HG-whole#1`, key `HG-whole-41a`, text
`fix-20261020/substack41/WHOLE-GUIDE-41.txt`): not 100% Human, chance 0.01; red expected in Appendix C, NLP patterns 4 to 6,
the listening script and the return steps, maybe some tidy closers in installed sections. The sentence-by-sentence forecast is the
4.1 risk read (`fix-20261020/risk41/`: 18 parts of under 1,800 words, one Sonnet reader each, compiled by
`compile_risk.py` into `RISK-SUMMARY.md` and `RISK-ITEMS.json` before any result was read): 167 sentences expected red
and 123 light green in 154 sections, every quote found in the guide as quoted; red by pattern: aphorisms and balanced
closers 63, tidy follow-ups 48, parallel or signposting explanations 28, quips 14, stock words 12, generic scenarios 2.
That is far more than the community article's 25 rewritten runs, so I expect it to over-flag; the result scores it. The
first try with four parts of 6,800 words failed: each reader spent its whole output reasoning and wrote nothing.

## 2026-10-20, after Joel's message of 17:38 UTC (no checks run)

**Pangram 4.1.** Joel: "pangram 4.1 just came out so i updated some of your instructions for it. it is much more precise
than pangram 4, so you may find that some areas that were human on the hypnosis article are no longer human". His rules of
20 October are merged into this branch from main: `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md` (up to six tries per
paragraph lineage, each with a specific diagnosis; one section check plus one recheck after paragraph work; one
whole-article certification plus one recheck at the end; a prediction with its evidence before every call) and its 4.1
part (read each sentence's shading; dark green is the aim, light green a warning). Every result in this lane is Pangram
4.0. How to check the guide again in 4.1 is question 5 on the questions page (my pick: one whole-guide check once
questions 1 to 4 are settled, then only what it flags).

**Nothing could run anyway:** Pangram in the desktop app's built-in browser is signed out (the dashboard shows "Log in";
its History answers 401). Joel signs in; I don't.

**The ledger.** From now on every check in this lane goes through `tools/humanization/pangram_ledger.py` (this lane's
ledger is `pangram-ledger.jsonl`, created with its first prediction; its page is `SCORECARD.md`, built with the
universal page `state/PANGRAM-SCORECARD.md`). This lane's 4.0 record on it: 944 calls, 85% right against 78% for always
saying Human, Brier 0.120 against 0.174 for the base rate; the latest 100 calls 83% against 75%.

## 2026-10-18, after batch 466g (its checks ran from 09:53 to 11:08 UTC)

**Where it stands.** 30 keys are installed (33 of the guide's 40 h1 sections, every paragraph checked alone) and three
read Human as published (HG05, HG08, HG09): **36 of 40 done.** New: **HG24**, the troubleshooting list (460g), and
**HG36**, "Altered states", now whole (462g: its last three paragraphs are no longer as published). Open, each a question
for Joel: HG31 (question 3), HG17 and HG18 (their guided scripts, question 4: HG18 now has a version that reads Human
with its key safety statements, option d), HG32 (the checklist, question 2).

**What the batches showed (459g to 466g).**
- **HG24's opening: whole-stretch samples worked where small fixes didn't.** It read AI with or without its fixes in every
  version to 457g. Three new samples of B2-B8 in one window (emu-aq, emu-ar, emu-as, from my meaning-fixed text) all read
  100% Human whole and in every paragraph (459g,
  [HG24-oc](https://www.pangram.com/history/1879f7a6-4639-4205-8411-49a517876080)); the second reader found 7 to 10
  points in each; the one with the fewest took three small fixes (0.6% of the words: "necessarily", "from doing this" out,
  a repeat said once; `fix-20261018/rf-zb/HG24.triage.json`) and read Human whole and in every changed paragraph
  ([460g HG24-fix](https://www.pangram.com/history/2d821ba0-cb11-4fcb-98c2-75ecac9f3278)): installed.
- **HG36's end**: B10-B11 from three new samples (459g) and B9-B12 in one run from three more (461g) pass every paragraph
  alone, but the whole section keeps an AI window at the end, 64 to 213 words
  ([459g HG36-ea](https://www.pangram.com/history/53a8984a-f49b-41fd-bd18-f738863b6372),
  [461g HG36-sa](https://www.pangram.com/history/ec22c667-201c-4882-a22e-2a667fc5c73b),
  [461g HG36-sc](https://www.pangram.com/history/f03019e6-93cf-4059-837b-603d4f8c1a21)). Whole-section runs: two from my
  fixed text read AI ([HG36-wa](https://www.pangram.com/history/40df572c-c695-4ceb-9cd1-d1a91e890a5a),
  [HG36-wb](https://www.pangram.com/history/d7cad1de-47f5-49c2-acf4-0eb1cc56115f)), and one from the published text
  (emu-av) read 100% Human whole and in every paragraph
  ([461g HG36-wc](https://www.pangram.com/history/3f4f2894-6d3d-4bc8-8f26-c437e8ba059b)); its second reader's 29 findings were triaged into
  10 fixes (6.3% of the words: the substance claims of B1 and B3, the scope of the "don't use self-hypnosis to" list and
  "recover memories", sleep and everyday responsibilities in B7, "remember love", "may or may not" and the frightening
  image in B10, B11's question; `fix-20261018/rf-zd/HG36.triage.json`), and the fixed section read Human whole and in
  every changed paragraph ([462g HG36-fix](https://www.pangram.com/history/6e9604e0-5f3d-4b48-b781-078f0be25fb5)):
  installed, by rebuilding the article from the published text with every installed section.
- **The scripts.** HG18 in two medium windows (459g): one sample reads 100% Human whole and in every paragraph for the
  first time ([HG18-ma](https://www.pangram.com/history/2f1ed833-8320-435b-93b1-7ecde89b7546)) but loses four safety
  statements of the return (18 findings, `fix-20261018/rf-za/HG18.ma.verify.part1.out.txt`). HG17's listening script in
  three medium windows: every paragraph Human, the section AI elsewhere too (the two-hand and sleep inductions), 19 to 31
  points lost ([HG17-mb](https://www.pangram.com/history/7dcc7629-91be-45c9-ad44-215c2a7d55e1)). Both stay with question 4.
- **HG18 by the fast path (463g-466g).** One run of the whole section: from the published text two of three samples read
  100% Human whole and in every paragraph ([HG18-wb](https://www.pangram.com/history/848cb97f-c829-449c-b807-1379910eabc3),
  13 findings; HG18-wc, 19). wb with its eight triaged fixes read AI from B2 on
  ([464g HG18-fix](https://www.pangram.com/history/9cc8e268-caf5-4aef-966c-69d3b9fb1eb0)); diagnostics (465g) and four
  sets of the fixes (466g) found that "neither of them keeps me in this state" and "get up only when you feel steady"
  together read Human whole and in every paragraph
  ([466g HG18-smp1](https://www.pangram.com/history/f456f1ca-b66b-4830-8f96-45d8d8e64bac); `fix-20261018/rf-zf/HG18.smp1.json`),
  and each of the other fixes brought an AI window back at the end. Not installed: question 4 (option d).

**Predictions** (a call is right when I said Human and it read 100% Human, or said AI and it didn't). 459g 56 of 66,
460g 5 of 5, 461g 37 of 46, 462g 9 of 9, 463g 19 of 21, 464g 2 of 5, 465g 3 of 5 (diagnostics), 466g 9 of 10. Brier score:
0.163 over the 198 checks before 446g, 0.108 over the 746 since; paragraph checks (Emulate-share chances, 454g on) 0.087
over 438, and the chances are refitted (`tools/para_chance.py`). Whole-section screens since 454g, diagnostics left out:
21 of 51 Human; 454g-458g Brier 0.278 (my mean chance 0.64, 44% Human), 459g on 0.231 (my mean chance 0.49, 38% Human).

**Records.** `b461-results.json` to `b466-results.json` shorten the texts of their AI windows ("[...]"); each row's check link has the full text.

### Sections

| section | state | newest whole check | paragraph checks | earlier |
|---|---|---|---|---|
| HG01 | **installed** (fixed) | [434g HG01-fix](https://www.pangram.com/history/b5dc548b-e3f5-427f-8270-f1da2afb8d54) | 1 of 1 Human | 429g published AI 0.98; 431g screen H 0.00 |
| HG02+03 | **installed** (triaged) | [454g HG02+03-rfix](https://www.pangram.com/history/94dc9298-fb41-497c-a71a-8666a6c0df7f) | 8 of 8 Human | 429g published AI 1.00; 431g screen AI 0.05; 434g fixed AI 0.99; 435g screen H 0.06; 443g refix AI 0.03 |
| HG04 | **installed** (triaged) | [450g HG04-rfix](https://www.pangram.com/history/bf1c1412-591e-4c11-a5ba-3bfb565fb0bd) | 2 of 2 Human | 429g published AI 1.00; 431g screen AI 0.36; 433g screen AI 0.95; 436g screen AI 1.00; 437g screen H 0.00; 441g fixed H 0.04; 445g refix H 0.11 |
| HG05 | Human (published) | [429g HG05](https://www.pangram.com/history/5028ad7e-4df3-476d-b580-1d5eee5eb68d) | - | - |
| HG06 | **installed** (sample) | [455g HG06-smp](https://www.pangram.com/history/98448ce1-bbdc-4b1d-a0d4-f22df8e93ec2) | 3 of 3 Human | 429g published AI 0.89; 430g screen H 0.10; 434g fixed H 0.20; 445g refix H 0.00; 448g refix H 0.00; 451g refix H 0.00; 453g triaged H 0.22 |
| HG07 | **installed** (fixed) | [434g HG07-fix](https://www.pangram.com/history/ca3cf277-8622-4f71-8405-22406e199488) | 3 of 3 Human | 429g published AI 0.25; 430g screen H 0.00 |
| HG08 | Human (published) | [429g HG08](https://www.pangram.com/history/971cfbf5-1485-4266-903a-f49145a75aa3) | - | - |
| HG09 | Human (published) | [429g HG09](https://www.pangram.com/history/7a521519-0ecc-4adc-9c04-c9ee182b3fd8) | - | - |
| HG10 | **installed** (refix) | [443g HG10-refix](https://www.pangram.com/history/4c169e15-7347-45e9-8581-c6f830c6663a) | 4 of 4 Human | 429g published AI 1.00; 430g screen H 0.05; 434g fixed AI 0.15 |
| HG11 | **installed** (refix) | [443g HG11-refix](https://www.pangram.com/history/c5ab4670-be7b-444e-83ef-545b54412dc5) | 4 of 4 Human | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 0.98 |
| HG12 | **installed** (fixed) | [434g HG12-fix](https://www.pangram.com/history/781080d2-867c-4e50-9250-c8a6899036b8) | 7 of 7 Human | 429g published AI 0.63; 431g screen H 0.03 |
| HG13 | **installed** (triaged) | [449g HG13-rfix](https://www.pangram.com/history/12e8c230-f460-4cc4-b1a2-63ef3aafd796) | 11 of 11 Human | 429g published AI 1.00; 432g screen H 0.04; 434g fixed AI 0.73; 443g refix H 0.00 |
| HG14 | **installed** (sample) | [456g HG14-smp2](https://www.pangram.com/history/785f1bf2-39de-4977-aa07-ee5b4aa6d8dc) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.70; 443g refix H 0.03; 451g triaged AI 0.09; 454g refix H 0.02; 455g sample H 0.02 |
| HG15 | **installed** (sample) | [455g HG15-smp](https://www.pangram.com/history/1ced6e80-dfa7-4825-ba6e-e7e00c8a0b5e) | 5 of 5 Human | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.79; 443g refix H 0.00; 451g triaged H 0.11 |
| HG16 | **installed** (triaged) | [452g HG16-rfix](https://www.pangram.com/history/94cb4b13-f089-4a11-bf19-28672a8fbba4) | 16 of 16 Human | 429g published AI 1.00; 431g screen AI 0.55; 433g screen AI 0.97; 436g screen AI 0.30; 437g screen H 0.01; 444g fixed AI 0.69; 447g refix H 0.01 |
| HG17 | Mixed, AI 0.12 (sample) | [459g HG17-mb](https://www.pangram.com/history/7dcc7629-91be-45c9-ad44-215c2a7d55e1) | 17 of 17 Human | 429g published AI 1.00; 433g screen AI 0.48; 436g screen AI 0.36; 437g screen AI 0.23; 438g screen AI 0.05; 439g screen AI 0.11; 440g screen H 0.01; 444g fixed AI 0.78; 447g refix AI 0.27; 449g refix AI 0.18; 451g refix H 0.04; 456g sample AI 0.19; 457g diagnostic AI 0.21; 457g diagnostic AI 0.14; 459g sample AI 0.16 |
| HG18 | Mixed, AI 0.34 (sample) | [466g HG18-smp4](https://www.pangram.com/history/9aa89c54-2e90-4b1a-b128-2e2c033357fd) | 5 of 6 Human | 429g published AI 1.00; 431g screen H 0.07; 434g fixed AI 1.00; 443g refix AI 0.25; 445g refix AI 0.35; 448g refix AI 0.94; 451g triaged AI 1.00; 455g sample AI 0.89; 455g sample AI 0.38; 459g sample H 0.07; 459g sample AI 0.43; 463g published AI 0.93; 463g published H 0.03; 463g published H 0.06; 464g fixed AI 0.50; 465g diagnostic AI 0.37; 465g diagnostic AI 0.15; 465g diagnostic AI 0.33; 465g diagnostic AI 0.57; 465g diagnostic H 0.05; 466g sample H 0.08; 466g sample AI 0.16; 466g sample AI 0.21 |
| HG19 | **installed** (triaged) | [449g HG19-rfix](https://www.pangram.com/history/9bf6d74c-d3f0-428c-bf23-babac94186b1) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.99; 443g refix H 0.00 |
| HG20 | **installed** (triaged) | [452g HG20-rfix2](https://www.pangram.com/history/3531dc12-7906-464c-bb23-15b0ed812ebb) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.00; 434g fixed AI 0.88; 443g refix H 0.00; 449g triaged H 0.00 |
| HG21 | **installed** (triaged) | [450g HG21-rfix](https://www.pangram.com/history/dfe80d81-9e35-479b-bb70-d0474b847d2b) | 4 of 4 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.98; 443g refix H 0.00 |
| HG22 | **installed** (triaged) | [449g HG22-rfix](https://www.pangram.com/history/bdcc3330-4a5b-4ed7-b9d8-cadce5cf5f89) | 2 of 2 Human | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 1.00; 443g refix H 0.00 |
| HG23 | **installed** (triaged) | [450g HG23-rfix](https://www.pangram.com/history/668653c1-9c71-444e-ae0f-35e17f3efc6b) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.68; 443g refix AI 0.20; 445g refix H 0.01 |
| HG24 | **installed** (sample) | [460g HG24-fix](https://www.pangram.com/history/2d821ba0-cb11-4fcb-98c2-75ecac9f3278) | 4 of 4 Human | 429g published AI 0.98; 433g screen AI 0.18; 435g screen AI 0.43; 437g screen H 0.02; 441g fixed AI 0.74; 445g refix AI 0.11; 448g refix H 0.06; 455g sample AI 0.19; 456g sample AI 0.17; 457g diagnostic AI 0.11; 459g sample H 0.00; 459g sample H 0.00; 459g sample H 0.00 |
| HG25 | **installed** (triaged) | [449g HG25-rfix](https://www.pangram.com/history/691c0bdd-383a-48e3-80b5-562d8a5a9fb8) | 11 of 11 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.90; 443g refix H 0.00 |
| HG26 | **installed** (sample) | [455g HG26-smp](https://www.pangram.com/history/5fe51689-07f3-4efe-8290-cdc9e2ce09e7) | 2 of 2 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.69; 443g refix H 0.00; 449g triaged AI 0.23; 451g refix H 0.09; 453g triaged H 0.07 |
| HG27 | **installed** (triaged) | [450g HG27-rfix](https://www.pangram.com/history/11d866c6-0604-4a4b-bccd-0f49a397bc98) | 2 of 2 Human | 429g published AI 1.00; 430g screen H 0.03; 434g fixed AI 0.45; 435g screen H 0.00; 443g refix H 0.00 |
| HG28 | **installed** (triaged) | [450g HG28-rfix](https://www.pangram.com/history/2f048f61-2981-4376-9909-131d705ce07f) | 5 of 5 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.26; 443g refix H 0.12 |
| HG29+30 | **installed** (triaged) | [449g HG29+30-rfix](https://www.pangram.com/history/48b4dfd2-abd1-4157-b04d-16ba3bf10c20) | 17 of 17 Human | 429g published AI 1.00; 431g screen AI 0.29; 433g screen AI 0.56; 436g screen AI 0.26; 437g screen AI 0.30; 438g screen H 0.12; 439g screen H 0.03; 441g fixed AI 0.69; 445g refix H 0.00 |
| HG31 | Human (sample) | [458g HG31-smp3](https://www.pangram.com/history/946661a0-43e6-4c44-83c9-5d45ec4ecb18) | 2 of 2 Human | 429g published AI 1.00; 433g screen AI 0.32; 435g screen AI 0.16; 436g screen AI 0.18; 437g screen AI 0.18; 438g screen AI 0.18; 439g screen AI 0.12; 440g screen H 0.07; 444g fixed AI 0.81; 447g refix AI 0.26; 449g refix AI 0.28; 451g refix H 0.02; 455g sample AI 0.19; 456g sample AI 0.17; 457g diagnostic AI 0.08; 457g diagnostic H 0.04 |
| HG32 | AI 1.00 (screen) | [435g HG32-emuF](https://www.pangram.com/history/5a25465d-60b9-4bea-a03a-011b2ecdcb1a) | - | 429g published AI 1.00; 432g screen AI 0.99 |
| HG33 | **installed** (triaged) | [455g HG33-rfix2](https://www.pangram.com/history/52ded84a-c50d-440f-8e4d-68df4cb3835e) | 4 of 4 Human | 429g published AI 1.00; 432g screen AI 0.28; 434g fixed AI 0.99; 435g screen H 0.01; 443g refix H 0.08; 451g triaged AI 0.28; 454g refix H 0.02 |
| HG34 | **installed** (triaged) | [451g HG34-rfix](https://www.pangram.com/history/e8d1cf1d-b3d2-4357-9ace-f11319f30be9) | 6 of 6 Human | 429g published AI 1.00; 431g screen H 0.11; 434g fixed AI 0.69; 443g refix H 0.00 |
| HG35 | **installed** (triaged) | [453g HG35-rfix](https://www.pangram.com/history/0bbc85f4-a5d1-4383-b09d-447f3a7d7f30) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.50; 443g refix H 0.04; 451g refix H 0.06 |
| HG36 | **installed** (sample) | [462g HG36-fix](https://www.pangram.com/history/6e9604e0-5f3d-4b48-b781-078f0be25fb5) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.80; 443g refix AI 0.55; 445g refix H 0.03; 449g triaged H 0.01; 455g sample AI 0.80; 455g published AI 0.31; 456g sample AI 0.24; 456g sample AI 0.48; 457g sample AI 0.28; 457g sample AI 0.24; 459g sample AI 0.40; 459g sample AI 0.82; 459g sample AI 0.33; 461g published AI 0.28; 461g published AI 0.47; 461g published AI 0.56; 461g published AI 0.94; 461g published AI 0.38; 461g published H 0.00 |
| HG37 | **installed** (sample) | [455g HG37-smp](https://www.pangram.com/history/2bf4e800-b478-4f99-91e8-dc2e6ef3352a) | 3 of 3 Human | 429g published AI 1.00; 433g screen AI 0.64; 436g screen AI 0.66; 437g screen AI 0.53; 438g screen AI 0.12; 439g screen H 0.08; 444g fixed AI 0.99; 447g refix AI 0.18; 449g refix H 0.03; 454g triaged AI 0.18 |
| HG38+39 | **installed** (triaged) | [452g HG38+39-rfix](https://www.pangram.com/history/729996a1-aa2c-4cc5-80fd-d2493917a8a1) | 12 of 12 Human | 429g published AI 1.00; 433g screen AI 0.59; 436g screen AI 0.18; 437g screen AI 0.15; 438g screen AI 0.16; 439g screen H 0.03; 444g fixed AI 1.00; 447g refix H 0.00 |
| HG40 | **installed** (triaged) | [449g HG40-rfix](https://www.pangram.com/history/1626b3a6-281b-4eef-b363-076dd0b73919) | 9 of 9 Human | 429g published AI 1.00; 432g screen H 0.00; 434g fixed AI 0.93; 443g refix H 0.00 |

## 2026-10-18, after batch 458g (its checks ran from 08:32 to 09:31 UTC)

**Where it stands.** 29 keys are installed (32 of the guide's 40 h1 sections, every paragraph checked alone) and three
read Human as published (HG05, HG08, HG09): **35 of 40 done.** HG36's last three paragraphs are still as published and
read AI alone (455g); the section counts as installed with that caveat. Open: HG31 (a version that reads Human whole and
in every paragraph, 458g, waits on Joel: two meaning points it leaves out, question 3), HG17 and HG18 (their guided
scripts, question 4), HG24 (its troubleshooting opening), HG32 (the checklist, question 2).

**What the batches showed (455g to 458g).**
- 455g: HG33, HG06, HG26, HG37 and HG15 passed whole and in every paragraph: installed. 456g: HG14.
- **Several samples, then pick**: HG26's get-help paragraphs (one of three samples kept every safety item: one small fix),
  HG06's forces paragraph, HG15's p10 and p11, HG14's four paragraphs, HG37's p20: each the best of two or three samples,
  each Human in its paragraph check.
- **The diagnostics (457g) say which fixes read AI.** HG31 reads Human whole without its B25, B28 and B34 fixes and AI with
  B28's, reworded or not; with only B34's it reads Human (458g). HG24's opening reads AI with or without its fixes (its
  question list itself). HG17's script reads AI in small windows with or without fixes: the small windows don't flow, and
  Pangram reads the run of them as AI even though every paragraph alone reads Human.
- HG36: B10 from three new samples (two from my fixed text, one from the published): every paragraph passes in one of them
  (456g, 457g), but the whole section keeps a 52-56-word AI window at its end.
- HG18: two small-window samples: one reads AI only in its last two paragraphs (455g) but bends the return steps (15
  findings, among them "neither intention nor cue keeps the altered state running" lost).

**Predictions.** 453g 39 of 43, 454g 99 of 107, 455g 116 of 134, 456g 64 of 77, 457g 3 of 11 (diagnostics, chances near
0.5 on purpose), 458g 3 of 3. Brier score: 0.163 over the 198 checks before 446g, 0.104 over the 579 since; paragraph
checks 0.104 with the length chances (235 checks), 0.083 with the Emulate-share chances (302 checks, 454g on).
Whole-section screens of new samples are the weak spot: 11 of 25 Human since 454g against my 0.72 (Brier 0.278).

**Records.** In `b455-results.json`, `b456-results.json` and `b457-results.json` some AI windows' texts are shortened
("[...]"); each row's check link has the full text.

### Sections

| section | state | newest whole check | paragraph checks | earlier |
|---|---|---|---|---|
| HG01 | **installed** (fixed) | [434g HG01-fix](https://www.pangram.com/history/b5dc548b-e3f5-427f-8270-f1da2afb8d54) | 1 of 1 Human | 429g published AI 0.98; 431g screen H 0.00 |
| HG02+03 | **installed** (triaged) | [454g HG02+03-rfix](https://www.pangram.com/history/94dc9298-fb41-497c-a71a-8666a6c0df7f) | 8 of 8 Human | 429g published AI 1.00; 431g screen AI 0.05; 434g fixed AI 0.99; 435g screen H 0.06; 443g refix AI 0.03 |
| HG04 | **installed** (triaged) | [450g HG04-rfix](https://www.pangram.com/history/bf1c1412-591e-4c11-a5ba-3bfb565fb0bd) | 2 of 2 Human | 429g published AI 1.00; 431g screen AI 0.36; 433g screen AI 0.95; 436g screen AI 1.00; 437g screen H 0.00; 441g fixed H 0.04; 445g refix H 0.11 |
| HG05 | Human (published) | [429g HG05](https://www.pangram.com/history/5028ad7e-4df3-476d-b580-1d5eee5eb68d) | - | - |
| HG06 | **installed** (sample) | [455g HG06-smp](https://www.pangram.com/history/98448ce1-bbdc-4b1d-a0d4-f22df8e93ec2) | 3 of 3 Human | 429g published AI 0.89; 430g screen H 0.10; 434g fixed H 0.20; 445g refix H 0.00; 448g refix H 0.00; 451g refix H 0.00; 453g triaged H 0.22 |
| HG07 | **installed** (fixed) | [434g HG07-fix](https://www.pangram.com/history/ca3cf277-8622-4f71-8405-22406e199488) | 3 of 3 Human | 429g published AI 0.25; 430g screen H 0.00 |
| HG08 | Human (published) | [429g HG08](https://www.pangram.com/history/971cfbf5-1485-4266-903a-f49145a75aa3) | - | - |
| HG09 | Human (published) | [429g HG09](https://www.pangram.com/history/7a521519-0ecc-4adc-9c04-c9ee182b3fd8) | - | - |
| HG10 | **installed** (refix) | [443g HG10-refix](https://www.pangram.com/history/4c169e15-7347-45e9-8581-c6f830c6663a) | 4 of 4 Human | 429g published AI 1.00; 430g screen H 0.05; 434g fixed AI 0.15 |
| HG11 | **installed** (refix) | [443g HG11-refix](https://www.pangram.com/history/c5ab4670-be7b-444e-83ef-545b54412dc5) | 4 of 4 Human | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 0.98 |
| HG12 | **installed** (fixed) | [434g HG12-fix](https://www.pangram.com/history/781080d2-867c-4e50-9250-c8a6899036b8) | 7 of 7 Human | 429g published AI 0.63; 431g screen H 0.03 |
| HG13 | **installed** (triaged) | [449g HG13-rfix](https://www.pangram.com/history/12e8c230-f460-4cc4-b1a2-63ef3aafd796) | 11 of 11 Human | 429g published AI 1.00; 432g screen H 0.04; 434g fixed AI 0.73; 443g refix H 0.00 |
| HG14 | **installed** (sample) | [456g HG14-smp2](https://www.pangram.com/history/785f1bf2-39de-4977-aa07-ee5b4aa6d8dc) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.70; 443g refix H 0.03; 451g triaged AI 0.09; 454g refix H 0.02; 455g sample H 0.02 |
| HG15 | **installed** (sample) | [455g HG15-smp](https://www.pangram.com/history/1ced6e80-dfa7-4825-ba6e-e7e00c8a0b5e) | 5 of 5 Human | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.79; 443g refix H 0.00; 451g triaged H 0.11 |
| HG16 | **installed** (triaged) | [452g HG16-rfix](https://www.pangram.com/history/94cb4b13-f089-4a11-bf19-28672a8fbba4) | 16 of 16 Human | 429g published AI 1.00; 431g screen AI 0.55; 433g screen AI 0.97; 436g screen AI 0.30; 437g screen H 0.01; 444g fixed AI 0.69; 447g refix H 0.01 |
| HG17 | Mixed, AI 0.14 (diagnostic) | [457g HG17-dg2](https://www.pangram.com/history/ff617e1f-14ac-4a13-afc9-a749b7c820a1) | - | 429g published AI 1.00; 433g screen AI 0.48; 436g screen AI 0.36; 437g screen AI 0.23; 438g screen AI 0.05; 439g screen AI 0.11; 440g screen H 0.01; 444g fixed AI 0.78; 447g refix AI 0.27; 449g refix AI 0.18; 451g refix H 0.04; 456g sample AI 0.19; 457g diagnostic AI 0.21 |
| HG18 | Mixed, AI 0.38 (sample) | [455g HG18-swb](https://www.pangram.com/history/4ee2c491-32af-4784-941e-ae6a595bbb92) | 11 of 12 Human | 429g published AI 1.00; 431g screen H 0.07; 434g fixed AI 1.00; 443g refix AI 0.25; 445g refix AI 0.35; 448g refix AI 0.94; 451g triaged AI 1.00; 455g sample AI 0.89 |
| HG19 | **installed** (triaged) | [449g HG19-rfix](https://www.pangram.com/history/9bf6d74c-d3f0-428c-bf23-babac94186b1) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.99; 443g refix H 0.00 |
| HG20 | **installed** (triaged) | [452g HG20-rfix2](https://www.pangram.com/history/3531dc12-7906-464c-bb23-15b0ed812ebb) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.00; 434g fixed AI 0.88; 443g refix H 0.00; 449g triaged H 0.00 |
| HG21 | **installed** (triaged) | [450g HG21-rfix](https://www.pangram.com/history/dfe80d81-9e35-479b-bb70-d0474b847d2b) | 4 of 4 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.98; 443g refix H 0.00 |
| HG22 | **installed** (triaged) | [449g HG22-rfix](https://www.pangram.com/history/bdcc3330-4a5b-4ed7-b9d8-cadce5cf5f89) | 2 of 2 Human | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 1.00; 443g refix H 0.00 |
| HG23 | **installed** (triaged) | [450g HG23-rfix](https://www.pangram.com/history/668653c1-9c71-444e-ae0f-35e17f3efc6b) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.68; 443g refix AI 0.20; 445g refix H 0.01 |
| HG24 | Mixed, AI 0.11 (diagnostic) | [457g HG24-dg1](https://www.pangram.com/history/9f01ac01-6cf8-45c3-ad78-feeb20547e5a) | - | 429g published AI 0.98; 433g screen AI 0.18; 435g screen AI 0.43; 437g screen H 0.02; 441g fixed AI 0.74; 445g refix AI 0.11; 448g refix H 0.06; 455g sample AI 0.19; 456g sample AI 0.17 |
| HG25 | **installed** (triaged) | [449g HG25-rfix](https://www.pangram.com/history/691c0bdd-383a-48e3-80b5-562d8a5a9fb8) | 11 of 11 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.90; 443g refix H 0.00 |
| HG26 | **installed** (sample) | [455g HG26-smp](https://www.pangram.com/history/5fe51689-07f3-4efe-8290-cdc9e2ce09e7) | 2 of 2 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.69; 443g refix H 0.00; 449g triaged AI 0.23; 451g refix H 0.09; 453g triaged H 0.07 |
| HG27 | **installed** (triaged) | [450g HG27-rfix](https://www.pangram.com/history/11d866c6-0604-4a4b-bccd-0f49a397bc98) | 2 of 2 Human | 429g published AI 1.00; 430g screen H 0.03; 434g fixed AI 0.45; 435g screen H 0.00; 443g refix H 0.00 |
| HG28 | **installed** (triaged) | [450g HG28-rfix](https://www.pangram.com/history/2f048f61-2981-4376-9909-131d705ce07f) | 5 of 5 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.26; 443g refix H 0.12 |
| HG29+30 | **installed** (triaged) | [449g HG29+30-rfix](https://www.pangram.com/history/48b4dfd2-abd1-4157-b04d-16ba3bf10c20) | 17 of 17 Human | 429g published AI 1.00; 431g screen AI 0.29; 433g screen AI 0.56; 436g screen AI 0.26; 437g screen AI 0.30; 438g screen H 0.12; 439g screen H 0.03; 441g fixed AI 0.69; 445g refix H 0.00 |
| HG31 | Human (sample) | [458g HG31-smp3](https://www.pangram.com/history/946661a0-43e6-4c44-83c9-5d45ec4ecb18) | 2 of 2 Human | 429g published AI 1.00; 433g screen AI 0.32; 435g screen AI 0.16; 436g screen AI 0.18; 437g screen AI 0.18; 438g screen AI 0.18; 439g screen AI 0.12; 440g screen H 0.07; 444g fixed AI 0.81; 447g refix AI 0.26; 449g refix AI 0.28; 451g refix H 0.02; 455g sample AI 0.19; 456g sample AI 0.17; 457g diagnostic AI 0.08; 457g diagnostic H 0.04 |
| HG32 | AI 1.00 (screen) | [435g HG32-emuF](https://www.pangram.com/history/5a25465d-60b9-4bea-a03a-011b2ecdcb1a) | - | 429g published AI 1.00; 432g screen AI 0.99 |
| HG33 | **installed** (triaged) | [455g HG33-rfix2](https://www.pangram.com/history/52ded84a-c50d-440f-8e4d-68df4cb3835e) | 4 of 4 Human | 429g published AI 1.00; 432g screen AI 0.28; 434g fixed AI 0.99; 435g screen H 0.01; 443g refix H 0.08; 451g triaged AI 0.28; 454g refix H 0.02 |
| HG34 | **installed** (triaged) | [451g HG34-rfix](https://www.pangram.com/history/e8d1cf1d-b3d2-4357-9ace-f11319f30be9) | 6 of 6 Human | 429g published AI 1.00; 431g screen H 0.11; 434g fixed AI 0.69; 443g refix H 0.00 |
| HG35 | **installed** (triaged) | [453g HG35-rfix](https://www.pangram.com/history/0bbc85f4-a5d1-4383-b09d-447f3a7d7f30) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.50; 443g refix H 0.04; 451g refix H 0.06 |
| HG36 | **installed** (triaged) | [457g HG36-smd](https://www.pangram.com/history/637ebed7-d251-4ed1-8330-373e366df1be) | 2 of 4 Human | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.80; 443g refix AI 0.55; 445g refix H 0.03; 449g triaged H 0.01; 455g sample AI 0.80; 455g published AI 0.31; 456g sample AI 0.24; 456g sample AI 0.48; 457g sample AI 0.28 |
| HG37 | **installed** (sample) | [455g HG37-smp](https://www.pangram.com/history/2bf4e800-b478-4f99-91e8-dc2e6ef3352a) | 3 of 3 Human | 429g published AI 1.00; 433g screen AI 0.64; 436g screen AI 0.66; 437g screen AI 0.53; 438g screen AI 0.12; 439g screen H 0.08; 444g fixed AI 0.99; 447g refix AI 0.18; 449g refix H 0.03; 454g triaged AI 0.18 |
| HG38+39 | **installed** (triaged) | [452g HG38+39-rfix](https://www.pangram.com/history/729996a1-aa2c-4cc5-80fd-d2493917a8a1) | 12 of 12 Human | 429g published AI 1.00; 433g screen AI 0.59; 436g screen AI 0.18; 437g screen AI 0.15; 438g screen AI 0.16; 439g screen H 0.03; 444g fixed AI 1.00; 447g refix H 0.00 |
| HG40 | **installed** (triaged) | [449g HG40-rfix](https://www.pangram.com/history/1626b3a6-281b-4eef-b363-076dd0b73919) | 9 of 9 Human | 429g published AI 1.00; 432g screen H 0.00; 434g fixed AI 0.93; 443g refix H 0.00 |

## 2026-10-18, after batch 454g (its checks ran from 07:33 to 07:52 UTC)

**Where it stands.** 23 keys are installed in `HUMANIZED-SO-FAR.md` (26 of the guide's 40 h1 sections), every paragraph
checked alone, and three more sections read Human as published (HG05, HG08, HG09): 29 of 40 done. One caveat: HG36's last
three paragraphs (B10-B12) are in the article as published and were never checked (see Tools below); their repair is in
`fix-20261018/rf-p/`. Open: HG06, HG14, HG15, HG17, HG24, HG26, HG31, HG33, HG37 (in meaning or paragraph checks), HG18 and
HG32 (AI in every version; for Joel).

**What the batches showed (446g to 454g).**
- **The triage holds.** Triaged edits read Human whole in 20 of 24 checks (449g to 454g); the four that didn't (HG14, HG18,
  HG26, HG33 in 449g or 451g) had small AI windows, and three of them read Human after a new sample of those windows.
- **Pasted published wording reads AI, even in a small fix.** HG37's edit (454g) read AI in exactly two windows, both
  triage fixes that pasted the published sentences ("what response makes you safer, clearer, more loving, more grounded, and
  less hooked"; "Pride gives it an opponent, and panic gives it your nervous system"). They are reworded in the stretch's
  voice now. The triage brief already says so; the readers will be reminded.
- **A paragraph alone reads Human when Emulate wrote it.** Of 235 paragraph checks (442g to 453g), those under 5% not
  Emulate's words read Human 99% of the time (141 checks); 5-15%, 93%; 15-30%, 70%. That is now how a paragraph check is
  predicted (`tools/para_chance.py`).
- **Several samples at once.** Instead of one sample, one screen, one reading at a time, two or three samples of each window
  went to Emulate together (emu-ac, emu-ad, emu-ae, emu-af, emu-ag, emu-ah, emu-ai) and the second reader read all of them;
  the one that kept the meaning best is triaged. For HG26's get-help paragraphs, one of three samples kept every safety
  item (one fix: "concerning" physical symptoms).
- **Emulate can't keep a long script.** HG17's listening script (B17-B31) lost 11 to 26 steps in each of three samples as one
  window; it is now in seven small windows (emu-af, emu-ag).
- **HG24's "Refrain."** My meaning fix for "Don't pry." was the verb "Refrain."; two samples read it as a song's refrain
  ("(VOCAL) REFRain: Just shew me first your CAPACItY"). B36-B37 are as published now.
- 453g: HG16, HG35 and HG38+39 passed every paragraph and were installed; HG06's fourth paragraph (my fix) and HG26's two
  get-help paragraphs together read AI. 454g: HG02+03 read 100% Human whole for the first time (Joel's table-of-contents
  note too), every paragraph Human: installed. HG14 and HG33's new window samples read Human whole; five of HG14's 59
  paragraph checks read AI.

**Predictions.** 447g 6 of 9, 448g 8 of 9, 449g 9 of 12, 450g 91 of 92, 451g 49 of 52, 452g 25 of 30, 453g 39 of 43,
454g 99 of 107. Brier score (my chance of a 100% Human result against the result): 0.134 over the lane's 445 checks to
453g; 0.076, 0.112, 0.147 and 0.109 for 450g to 453g.

**Tools.** `tools/refix_runs.py`: `units_fixed` and `assembled_fixed` dropped every block after the first when a run's output
came back one segment per block for a stretch that was one unit (HG36 lost B10-B12 from its checked text that way; the
install left them as published; HG24's second reader never saw B43, B44, B47, B48). Both now take every segment, keep the
unit's own paragraphs where they line up one per block, and stop with an error otherwise (`tests/test_hypnosis_refix_merge.py`).
`tools/para_chance.py` (paragraph-check chances); `make_b446.collect()` reads only each section's newest version (an older
`rf-a` file had reused a newer check's result); `make_verify_samples.py` (the second reader for several samples);
`make_emu_ac.py`, `make_emu_af.py`, `make_emu_ah.py` (sample sets); `march_pairs.py` reads a hand-made map.

### Sections

| section | state | newest whole check | paragraph checks | earlier |
|---|---|---|---|---|
| HG01 | **installed** (fixed) | [434g HG01-fix](https://www.pangram.com/history/b5dc548b-e3f5-427f-8270-f1da2afb8d54) | 1 of 1 Human | 429g published AI 0.98; 431g screen H 0.00 |
| HG02+03 | **installed** (triaged) | [454g HG02+03-rfix](https://www.pangram.com/history/94dc9298-fb41-497c-a71a-8666a6c0df7f) | 8 of 8 Human | 429g published AI 1.00; 431g screen AI 0.05; 434g fixed AI 0.99; 435g screen H 0.06; 443g refix AI 0.03 |
| HG04 | **installed** (triaged) | [450g HG04-rfix](https://www.pangram.com/history/bf1c1412-591e-4c11-a5ba-3bfb565fb0bd) | 2 of 2 Human | 429g published AI 1.00; 431g screen AI 0.36; 433g screen AI 0.95; 436g screen AI 1.00; 437g screen H 0.00; 441g fixed H 0.04; 445g refix H 0.11 |
| HG05 | Human (published) | [429g HG05](https://www.pangram.com/history/5028ad7e-4df3-476d-b580-1d5eee5eb68d) | - | - |
| HG06 | Human (triaged) | [453g HG06-rfix](https://www.pangram.com/history/80bf4ff5-088b-4a3f-a447-f3b0c942b713) | 0 of 3 Human | 429g published AI 0.89; 430g screen H 0.10; 434g fixed H 0.20; 445g refix H 0.00; 448g refix H 0.00; 451g refix H 0.00 |
| HG07 | **installed** (fixed) | [434g HG07-fix](https://www.pangram.com/history/ca3cf277-8622-4f71-8405-22406e199488) | 3 of 3 Human | 429g published AI 0.25; 430g screen H 0.00 |
| HG08 | Human (published) | [429g HG08](https://www.pangram.com/history/971cfbf5-1485-4266-903a-f49145a75aa3) | - | - |
| HG09 | Human (published) | [429g HG09](https://www.pangram.com/history/7a521519-0ecc-4adc-9c04-c9ee182b3fd8) | - | - |
| HG10 | **installed** (refix) | [443g HG10-refix](https://www.pangram.com/history/4c169e15-7347-45e9-8581-c6f830c6663a) | 4 of 4 Human | 429g published AI 1.00; 430g screen H 0.05; 434g fixed AI 0.15 |
| HG11 | **installed** (refix) | [443g HG11-refix](https://www.pangram.com/history/c5ab4670-be7b-444e-83ef-545b54412dc5) | 4 of 4 Human | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 0.98 |
| HG12 | **installed** (fixed) | [434g HG12-fix](https://www.pangram.com/history/781080d2-867c-4e50-9250-c8a6899036b8) | 7 of 7 Human | 429g published AI 0.63; 431g screen H 0.03 |
| HG13 | **installed** (triaged) | [449g HG13-rfix](https://www.pangram.com/history/12e8c230-f460-4cc4-b1a2-63ef3aafd796) | 11 of 11 Human | 429g published AI 1.00; 432g screen H 0.04; 434g fixed AI 0.73; 443g refix H 0.00 |
| HG14 | Human (refix) | [454g HG14-refix2](https://www.pangram.com/history/06d1ce83-4310-473f-8153-6e4cff193db5) | 54 of 59 Human | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.70; 443g refix H 0.03; 451g triaged AI 0.09 |
| HG15 | Human (triaged) | [451g HG15-rfix](https://www.pangram.com/history/105ec30f-5031-4998-85a2-7540fb64af91) | 15 of 20 Human | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.79; 443g refix H 0.00 |
| HG16 | **installed** (triaged) | [452g HG16-rfix](https://www.pangram.com/history/94cb4b13-f089-4a11-bf19-28672a8fbba4) | 16 of 16 Human | 429g published AI 1.00; 431g screen AI 0.55; 433g screen AI 0.97; 436g screen AI 0.30; 437g screen H 0.01; 444g fixed AI 0.69; 447g refix H 0.01 |
| HG17 | Human (refix) | [451g HG17-refix3](https://www.pangram.com/history/0dfd0e10-5b95-4c30-ab76-31cd9d8a66ed) | - | 429g published AI 1.00; 433g screen AI 0.48; 436g screen AI 0.36; 437g screen AI 0.23; 438g screen AI 0.05; 439g screen AI 0.11; 440g screen H 0.01; 444g fixed AI 0.78; 447g refix AI 0.27; 449g refix AI 0.18 |
| HG18 | AI 1.00 (triaged) | [451g HG18-rfix](https://www.pangram.com/history/a4847ac0-004c-4b1b-92f7-6a103c7e595a) | - | 429g published AI 1.00; 431g screen H 0.07; 434g fixed AI 1.00; 443g refix AI 0.25; 445g refix AI 0.35; 448g refix AI 0.94 |
| HG19 | **installed** (triaged) | [449g HG19-rfix](https://www.pangram.com/history/9bf6d74c-d3f0-428c-bf23-babac94186b1) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.99; 443g refix H 0.00 |
| HG20 | **installed** (triaged) | [452g HG20-rfix2](https://www.pangram.com/history/3531dc12-7906-464c-bb23-15b0ed812ebb) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.00; 434g fixed AI 0.88; 443g refix H 0.00; 449g triaged H 0.00 |
| HG21 | **installed** (triaged) | [450g HG21-rfix](https://www.pangram.com/history/dfe80d81-9e35-479b-bb70-d0474b847d2b) | 4 of 4 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.98; 443g refix H 0.00 |
| HG22 | **installed** (triaged) | [449g HG22-rfix](https://www.pangram.com/history/bdcc3330-4a5b-4ed7-b9d8-cadce5cf5f89) | 2 of 2 Human | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 1.00; 443g refix H 0.00 |
| HG23 | **installed** (triaged) | [450g HG23-rfix](https://www.pangram.com/history/668653c1-9c71-444e-ae0f-35e17f3efc6b) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.68; 443g refix AI 0.20; 445g refix H 0.01 |
| HG24 | Human (refix) | [448g HG24-refix2](https://www.pangram.com/history/266d8b09-d06e-4e40-a595-c87acb623fe3) | - | 429g published AI 0.98; 433g screen AI 0.18; 435g screen AI 0.43; 437g screen H 0.02; 441g fixed AI 0.74; 445g refix AI 0.11 |
| HG25 | **installed** (triaged) | [449g HG25-rfix](https://www.pangram.com/history/691c0bdd-383a-48e3-80b5-562d8a5a9fb8) | 11 of 11 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.90; 443g refix H 0.00 |
| HG26 | Human (triaged) | [453g HG26-rfix](https://www.pangram.com/history/2dba6402-6101-4e5d-b28e-ca03db166edd) | 7 of 8 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.69; 443g refix H 0.00; 449g triaged AI 0.23; 451g refix H 0.09 |
| HG27 | **installed** (triaged) | [450g HG27-rfix](https://www.pangram.com/history/11d866c6-0604-4a4b-bccd-0f49a397bc98) | 2 of 2 Human | 429g published AI 1.00; 430g screen H 0.03; 434g fixed AI 0.45; 435g screen H 0.00; 443g refix H 0.00 |
| HG28 | **installed** (triaged) | [450g HG28-rfix](https://www.pangram.com/history/2f048f61-2981-4376-9909-131d705ce07f) | 5 of 5 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.26; 443g refix H 0.12 |
| HG29+30 | **installed** (triaged) | [449g HG29+30-rfix](https://www.pangram.com/history/48b4dfd2-abd1-4157-b04d-16ba3bf10c20) | 17 of 17 Human | 429g published AI 1.00; 431g screen AI 0.29; 433g screen AI 0.56; 436g screen AI 0.26; 437g screen AI 0.30; 438g screen H 0.12; 439g screen H 0.03; 441g fixed AI 0.69; 445g refix H 0.00 |
| HG31 | Human (refix) | [451g HG31-refix3](https://www.pangram.com/history/12d15b76-fec4-498b-9de9-e279687197db) | - | 429g published AI 1.00; 433g screen AI 0.32; 435g screen AI 0.16; 436g screen AI 0.18; 437g screen AI 0.18; 438g screen AI 0.18; 439g screen AI 0.12; 440g screen H 0.07; 444g fixed AI 0.81; 447g refix AI 0.26; 449g refix AI 0.28 |
| HG32 | AI 1.00 (screen) | [435g HG32-emuF](https://www.pangram.com/history/5a25465d-60b9-4bea-a03a-011b2ecdcb1a) | - | 429g published AI 1.00; 432g screen AI 0.99 |
| HG33 | Human (refix) | [454g HG33-refix2](https://www.pangram.com/history/eb55c9b5-7ce3-4a53-a669-c40abeb5ae0e) | 13 of 13 Human | 429g published AI 1.00; 432g screen AI 0.28; 434g fixed AI 0.99; 435g screen H 0.01; 443g refix H 0.08; 451g triaged AI 0.28 |
| HG34 | **installed** (triaged) | [451g HG34-rfix](https://www.pangram.com/history/e8d1cf1d-b3d2-4357-9ace-f11319f30be9) | 6 of 6 Human | 429g published AI 1.00; 431g screen H 0.11; 434g fixed AI 0.69; 443g refix H 0.00 |
| HG35 | **installed** (triaged) | [453g HG35-rfix](https://www.pangram.com/history/0bbc85f4-a5d1-4383-b09d-447f3a7d7f30) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.50; 443g refix H 0.04; 451g refix H 0.06 |
| HG36 | **installed** (triaged) | [449g HG36-rfix](https://www.pangram.com/history/fa11a700-2004-412b-bc7e-8f9a27e83937) | 5 of 5 Human | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.80; 443g refix AI 0.55; 445g refix H 0.03 |
| HG37 | Mixed, AI 0.18 (triaged) | [454g HG37-rfix](https://www.pangram.com/history/17263cdd-3367-485c-947b-a2f46020d00f) | 22 of 23 Human | 429g published AI 1.00; 433g screen AI 0.64; 436g screen AI 0.66; 437g screen AI 0.53; 438g screen AI 0.12; 439g screen H 0.08; 444g fixed AI 0.99; 447g refix AI 0.18; 449g refix H 0.03 |
| HG38+39 | **installed** (triaged) | [452g HG38+39-rfix](https://www.pangram.com/history/729996a1-aa2c-4cc5-80fd-d2493917a8a1) | 12 of 12 Human | 429g published AI 1.00; 433g screen AI 0.59; 436g screen AI 0.18; 437g screen AI 0.15; 438g screen AI 0.16; 439g screen H 0.03; 444g fixed AI 1.00; 447g refix H 0.00 |
| HG40 | **installed** (triaged) | [449g HG40-rfix](https://www.pangram.com/history/1626b3a6-281b-4eef-b363-076dd0b73919) | 9 of 9 Human | 429g published AI 1.00; 432g screen H 0.00; 434g fixed AI 0.93; 443g refix H 0.00 |

## 2026-10-18, after batch 445g (its checks ran at 05:44 UTC)

**Where it stands.** Three sections are installed in `HUMANIZED-SO-FAR.md` with every paragraph checked alone: HG01 (the
guide's opening), HG07 and HG12 (442g). Three more read Human as published (HG05, HG08, HG09). Twenty-two others have a
version that reads 100% Human whole and are in meaning checks or paragraph checks; the rest are in refix runs.

**What the batches showed.**
- 441g: of the three fixed sections, HG04 stayed Human (17% of its words changed); HG24 and HG29+30 read AI.
- 442g, the first paragraph checks (23 texts of the five fixed sections that read Human): 17 Human. HG01, HG07, HG12 passed
  every paragraph; HG04's first two paragraphs and HG06's last four didn't.
- 443g, Plan B (Emulate rewrites my meaning-fixed text in the windows that read AI): **17 of 21 Human**.
- 444g: HG16, HG17, HG31, HG37 and HG38+39 with my fixes: all AI, as predicted. Their refix runs (emu-t) are running.
- 445g: refix screens of HG23, HG36, HG29+30 Human; HG04 and HG06 Human whole with their new paragraphs (HG06's new
  third paragraph reads AI alone); HG18 and HG24 still have AI windows.
- **The changed share decides.** Of 33 fixed sections, those whose fixes changed under 18% of the words stayed Human (3 of 3);
  those that changed more mostly didn't (2 of 30). That is why a refix's meaning problems now go through a triage
  (`fix-20261018/rf-a/TRIAGE-BRIEF.md`): only what changes what a reader would do or believe is fixed, in few words.
- **Emulate bends meaning again in a refix.** The second readers found 0 (HG10) to 71 (HG14) problems a section. HG26, the
  "when to get help" section, softened "get urgent help now"; every safety point there will be fixed.

**Predictions.** 441g 2 of 3 right, 442g 17 of 23, 443g 17 of 21, 444g 3 of 5 (I said "Mixed" where two read all AI),
445g 10 of 13.

**Tools.** `tools/install_fixed.py` (the Markdown to install, its paragraph-check texts, the install itself);
`tools/refix_runs.py` (`window_runs`, `assembled_fixed`, `units_fixed`, `hit_published`, `fixed_draft_blocks`);
`faithful.py verify-chunks` (a long section's second reader in parts); `paragraphs_alone.tries_for` (what the check looks
for, for batch builders); the block map reads the published copy, so an installed section never moves it;
`tools/lane_status.py` names each check's stage and the installed sections.

**Sections.**

| section | state | newest whole check | paragraph checks | earlier |
|---|---|---|---|---|
| HG01 | **installed** (fixed) | [434g HG01-fix](https://www.pangram.com/history/b5dc548b-e3f5-427f-8270-f1da2afb8d54) | 1 of 1 Human | 429g published AI 0.98; 431g screen H 0.00 |
| HG02+03 | Mixed, AI 0.03 (refix) | [443g HG02+03-refix](https://www.pangram.com/history/67524dc3-d41b-4330-89fc-7e579024cede) | - | 429g published AI 1.00; 431g screen AI 0.05; 434g fixed AI 0.99; 435g screen H 0.06 |
| HG04 | Human (refix) | [445g HG04-refix](https://www.pangram.com/history/0d852f81-ed67-4424-8e4d-491ea72d0e99) | - | 429g published AI 1.00; 431g screen AI 0.36; 433g screen AI 0.95; 436g screen AI 1.00; 437g screen H 0.00; 441g fixed H 0.04 |
| HG05 | Human (published) | [429g HG05](https://www.pangram.com/history/5028ad7e-4df3-476d-b580-1d5eee5eb68d) | - | - |
| HG06 | Human (refix) | [445g HG06-refix](https://www.pangram.com/history/9e338eee-a171-49d8-82ff-bae6f547ec49) | - | 429g published AI 0.89; 430g screen H 0.10; 434g fixed H 0.20 |
| HG07 | **installed** (fixed) | [434g HG07-fix](https://www.pangram.com/history/ca3cf277-8622-4f71-8405-22406e199488) | 3 of 3 Human | 429g published AI 0.25; 430g screen H 0.00 |
| HG08 | Human (published) | [429g HG08](https://www.pangram.com/history/971cfbf5-1485-4266-903a-f49145a75aa3) | - | - |
| HG09 | Human (published) | [429g HG09](https://www.pangram.com/history/7a521519-0ecc-4adc-9c04-c9ee182b3fd8) | - | - |
| HG10 | Human (refix) | [443g HG10-refix](https://www.pangram.com/history/4c169e15-7347-45e9-8581-c6f830c6663a) | - | 429g published AI 1.00; 430g screen H 0.05; 434g fixed AI 0.15 |
| HG11 | Human (refix) | [443g HG11-refix](https://www.pangram.com/history/c5ab4670-be7b-444e-83ef-545b54412dc5) | - | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 0.98 |
| HG12 | **installed** (fixed) | [434g HG12-fix](https://www.pangram.com/history/781080d2-867c-4e50-9250-c8a6899036b8) | 7 of 7 Human | 429g published AI 0.63; 431g screen H 0.03 |
| HG13 | Human (refix) | [443g HG13-refix](https://www.pangram.com/history/51d47dc8-838d-4ae5-8340-42f46de2731c) | - | 429g published AI 1.00; 432g screen H 0.04; 434g fixed AI 0.73 |
| HG14 | Human (refix) | [443g HG14-refix](https://www.pangram.com/history/60e741f3-8543-4c65-9c28-357e6bb6b204) | - | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.70 |
| HG15 | Human (refix) | [443g HG15-refix](https://www.pangram.com/history/df417394-281f-4c3b-a1c8-018bb4cc115b) | - | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.79 |
| HG16 | Mixed, AI 0.69 (fixed) | [444g HG16-fix](https://www.pangram.com/history/219af50c-bf82-41ab-9325-b7a4b8e82180) | - | 429g published AI 1.00; 431g screen AI 0.55; 433g screen AI 0.97; 436g screen AI 0.30; 437g screen H 0.01 |
| HG17 | Mixed, AI 0.78 (fixed) | [444g HG17-fix](https://www.pangram.com/history/7022d346-a8e2-42a4-aec7-a590e7f8ac35) | - | 429g published AI 1.00; 433g screen AI 0.48; 436g screen AI 0.36; 437g screen AI 0.23; 438g screen AI 0.05; 439g screen AI 0.11; 440g screen H 0.01 |
| HG18 | Mixed, AI 0.35 (refix) | [445g HG18-refix2](https://www.pangram.com/history/83f75339-363d-429a-b377-c6339d236f5d) | - | 429g published AI 1.00; 431g screen H 0.07; 434g fixed AI 1.00; 443g refix AI 0.25 |
| HG19 | Human (refix) | [443g HG19-refix](https://www.pangram.com/history/8b56e974-fdf2-4a32-9a91-664f56592d85) | - | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.99 |
| HG20 | Human (refix) | [443g HG20-refix](https://www.pangram.com/history/6e72bc49-4c63-45e3-9b1a-6fd38a074db3) | - | 429g published AI 1.00; 433g screen H 0.00; 434g fixed AI 0.88 |
| HG21 | Human (refix) | [443g HG21-refix](https://www.pangram.com/history/ecb5e201-3788-4d72-b017-05e4810477d5) | - | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.98 |
| HG22 | Human (refix) | [443g HG22-refix](https://www.pangram.com/history/2131d174-4dfb-4032-888c-ae335dee75d0) | - | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 1.00 |
| HG23 | Human (refix) | [445g HG23-refix2](https://www.pangram.com/history/98f81bd1-01ea-484f-ad25-750093862233) | - | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.68; 443g refix AI 0.20 |
| HG24 | Mixed, AI 0.11 (refix) | [445g HG24-refix](https://www.pangram.com/history/9ce7c56c-5dbc-4e10-9897-788b4f9b4ad8) | - | 429g published AI 0.98; 433g screen AI 0.18; 435g screen AI 0.43; 437g screen H 0.02; 441g fixed AI 0.74 |
| HG25 | Human (refix) | [443g HG25-refix](https://www.pangram.com/history/eed35961-98d1-4370-bd77-57f7f56a5b76) | - | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.90 |
| HG26 | Human (refix) | [443g HG26-refix](https://www.pangram.com/history/1cca1598-4345-4927-8a24-04e3d5fdcab2) | - | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.69 |
| HG27 | Human (refix) | [443g HG27-refix](https://www.pangram.com/history/942920c5-fb3b-4f62-aca9-db6d08951a34) | - | 429g published AI 1.00; 430g screen H 0.03; 434g fixed AI 0.45; 435g screen H 0.00 |
| HG28 | Human (refix) | [443g HG28-refix](https://www.pangram.com/history/5fbf9cc2-3e0c-41e0-a3ec-e03736c21b16) | - | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.26 |
| HG29+30 | Human (refix) | [445g HG29+30-refix](https://www.pangram.com/history/19b268b0-7b72-441d-a943-2d18c193a976) | - | 429g published AI 1.00; 431g screen AI 0.29; 433g screen AI 0.56; 436g screen AI 0.26; 437g screen AI 0.30; 438g screen H 0.12; 439g screen H 0.03; 441g fixed AI 0.69 |
| HG31 | Mixed, AI 0.81 (fixed) | [444g HG31-fix](https://www.pangram.com/history/7421d3fc-5d39-4fec-b60d-b8c258c9dd30) | - | 429g published AI 1.00; 433g screen AI 0.32; 435g screen AI 0.16; 436g screen AI 0.18; 437g screen AI 0.18; 438g screen AI 0.18; 439g screen AI 0.12; 440g screen H 0.07 |
| HG32 | AI 1.00 (screen) | [435g HG32-emuF](https://www.pangram.com/history/5a25465d-60b9-4bea-a03a-011b2ecdcb1a) | - | 429g published AI 1.00; 432g screen AI 0.99 |
| HG33 | Human (refix) | [443g HG33-refix](https://www.pangram.com/history/6a7651a6-31f8-4396-b96c-da16b8febbb9) | - | 429g published AI 1.00; 432g screen AI 0.28; 434g fixed AI 0.99; 435g screen H 0.01 |
| HG34 | Human (refix) | [443g HG34-refix](https://www.pangram.com/history/71ba9c12-8313-48dd-a719-defee4f45d41) | - | 429g published AI 1.00; 431g screen H 0.11; 434g fixed AI 0.69 |
| HG35 | Human (refix) | [443g HG35-refix](https://www.pangram.com/history/5e037240-6d96-4ee8-85be-3a91aafe47a9) | - | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.50 |
| HG36 | Human (refix) | [445g HG36-refix2](https://www.pangram.com/history/2d675dff-0550-4b3c-8b68-89c42ebb66f5) | - | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.80; 443g refix AI 0.55 |
| HG37 | AI 0.99 (fixed) | [444g HG37-fix](https://www.pangram.com/history/81c9c3f6-f069-440a-a383-2a34871a89d9) | - | 429g published AI 1.00; 433g screen AI 0.64; 436g screen AI 0.66; 437g screen AI 0.53; 438g screen AI 0.12; 439g screen H 0.08 |
| HG38+39 | AI 1.00 (fixed) | [444g HG38+39-fix](https://www.pangram.com/history/f913c9f0-6243-4965-89b6-801690910ca6) | - | 429g published AI 1.00; 433g screen AI 0.59; 436g screen AI 0.18; 437g screen AI 0.15; 438g screen AI 0.16; 439g screen H 0.03 |
| HG40 | Human (refix) | [443g HG40-refix](https://www.pangram.com/history/52af1c90-5e5c-4286-907d-2a8cc9a43646) | - | 429g published AI 1.00; 432g screen H 0.00; 434g fixed AI 0.93 |

## 2026-10-18, after batch 440g (its checks ran at 04:26 UTC)

**Where it stands.** Every section but the de-hypnosis checklist (HG32) now has a version that reads 100% Human: 3 as
published, 33 as Emulate rewrote them. None is installed yet. Meaning work: 25 sections are done (my review, a second
reader, my answers to its findings, round-two and round-three fixes; `fix-20261018/meaning-status.json`, answered
findings in `fix-20261018/dispositions.json`); 8 more are in review (HG04, HG16, HG24: second reader running; HG29+30,
HG37, HG38+39: second reader running; HG17 and HG31: first review in parts). March reads of every unread stretch are
running (march-d, march-e). Then batch 434g: the corrected versions in Pangram.

**What worked for the failing sections (436g to 440g).** Second samples of short pieces fixed none (436g, 0 of 7). Sending
each AI window whole, with its headings, as one run did: 437g 3 of 8, 438g 1 of 5, 439g 3 of 5, 440g 2 of 2. A window
that keeps reading AI gets smaller with each whole-window sample (the induction: 1,283 AI words, then 950, 589, 117,
304, 0).

**Tools changed.** The window mapper reads the reader's short forms; the run mapper knows rewritten headings and, with
`--align`, cuts a run whose headings Emulate dropped by word overlap (it once took "Iteration (revise the prompt...)" for
the heading "Core prompts", now ruled out); a later folder's segment replaces every earlier one it overlaps;
`faithful.py chunks` cuts a long review into parts and `merge` adds later rounds of fixes; the gate no longer holds an
edit of an Emulate text for a linter FAIL its screen also had (57 of 59 screens FAILed, 28 of the 30 that read Human).

**Sections.**

| section | state | newest check | before |
|---|---|---|---|
| HG01 | Human | [431g HG01-emuA](https://www.pangram.com/history/82a93d2f-944b-4cf4-8d12-3d234c672f2a) | 429g AI 0.98 |
| HG01+TOC | Human as published | [432g HG01+TOC-probe](https://www.pangram.com/history/9e73b7bd-6a1b-4196-8ea4-cd6f6645b4c3) | - |
| HG02+03 | Human | [435g HG02+03-emuF](https://www.pangram.com/history/d0b61522-6920-41bf-9696-9d9e691a61a4) | 429g AI 1.00; 431g AI 0.05 |
| HG04 | Human | [437g HG04-emuH](https://www.pangram.com/history/7c55545c-f99e-468f-950b-5afd045339ff) | 429g AI 1.00; 431g AI 0.36; 433g AI 0.95; 436g AI 1.00 |
| HG05 | Human as published | [429g HG05](https://www.pangram.com/history/5028ad7e-4df3-476d-b580-1d5eee5eb68d) | - |
| HG06 | Human | [430g HG06-emuA](https://www.pangram.com/history/027a8de9-0e95-486c-8116-537066acdf77) | 429g AI 0.89 |
| HG07 | Human | [430g HG07-emuA](https://www.pangram.com/history/58314327-d533-40a5-9e6e-54ace93e3864) | 429g AI 0.25 |
| HG08 | Human as published | [429g HG08](https://www.pangram.com/history/971cfbf5-1485-4266-903a-f49145a75aa3) | - |
| HG09 | Human as published | [429g HG09](https://www.pangram.com/history/7a521519-0ecc-4adc-9c04-c9ee182b3fd8) | - |
| HG10 | Human | [430g HG10-emuA](https://www.pangram.com/history/c2963511-eeda-40d8-91a5-cb8859e3be6d) | 429g AI 1.00 |
| HG11 | Human | [430g HG11-emuA](https://www.pangram.com/history/157ed130-e3fe-4599-9810-5d07db9d3d0a) | 429g AI 1.00 |
| HG12 | Human | [431g HG12-emuA](https://www.pangram.com/history/0a29db60-da17-4708-b755-811072c8d3c2) | 429g AI 0.63 |
| HG13 | Human | [432g HG13-emuB](https://www.pangram.com/history/d274cdbe-9dc2-4bf5-8709-1812a07d9df7) | 429g AI 1.00 |
| HG14 | Human | [433g HG14-emuC](https://www.pangram.com/history/8455a492-80e6-434f-a267-9489485a05e6) | 429g AI 1.00 |
| HG15 | Human | [431g HG15-emuA](https://www.pangram.com/history/83cea455-7d6f-4096-8c0d-075a002fa8a0) | 429g AI 1.00 |
| HG16 | Human | [437g HG16-emuH](https://www.pangram.com/history/eadab2ae-1ca7-4401-bf43-c9d905943ede) | 429g AI 1.00; 431g AI 0.55; 433g AI 0.97; 436g AI 0.30 |
| HG17 | Human | [440g HG17-emuK](https://www.pangram.com/history/fdb72264-85fb-4259-986e-ab29176e6f19) | 429g AI 1.00; 433g AI 0.48; 436g AI 0.36; 437g AI 0.23; 438g AI 0.05; 439g AI 0.11 |
| HG18 | Human | [431g HG18-emuA](https://www.pangram.com/history/f7bfaff5-7844-44b8-b4ae-5cad302c5141) | 429g AI 1.00 |
| HG19 | Human | [431g HG19-emuA](https://www.pangram.com/history/ab3dac21-a2a4-4f59-8a06-1453cb61cfdd) | 429g AI 1.00 |
| HG20 | Human | [433g HG20-emuC](https://www.pangram.com/history/41c0e263-0634-4582-affa-dd9ce4f1a398) | 429g AI 1.00 |
| HG21 | Human | [431g HG21-emuA](https://www.pangram.com/history/3dcb39d2-f19e-47f8-b88a-40db881f3a00) | 429g AI 1.00 |
| HG22 | Human | [430g HG22-emuA](https://www.pangram.com/history/966ede09-185e-4eed-a1bb-d8e5048c2979) | 429g AI 1.00 |
| HG23 | Human | [431g HG23-emuA](https://www.pangram.com/history/57f9ffc1-d21b-4098-afca-272ea42bd7b0) | 429g AI 1.00 |
| HG24 | Human | [437g HG24-emuH](https://www.pangram.com/history/e270cbd7-3272-446d-8042-771294c32b77) | 429g AI 0.98; 433g AI 0.18; 435g AI 0.43 |
| HG25 | Human | [431g HG25-emuA](https://www.pangram.com/history/c67eef25-4a2b-46ad-b693-7a8b5564708c) | 429g AI 1.00 |
| HG26 | Human | [431g HG26-emuA](https://www.pangram.com/history/7d2d5e40-6356-4aca-b56c-c799d7599c06) | 429g AI 1.00 |
| HG27 | Human | [435g HG27-emuF](https://www.pangram.com/history/d3b20b3a-4da8-4e6f-ad46-9228719a9453) | 429g AI 1.00; 430g H 0.03 |
| HG28 | Human | [431g HG28-emuA](https://www.pangram.com/history/0c6cef60-62d0-4dd4-a5ef-7cd324102183) | 429g AI 1.00 |
| HG29+30 | Human | [439g HG29+30-emuI2](https://www.pangram.com/history/c26e0b02-5d1b-46c9-b266-01cf35a95498) | 429g AI 1.00; 431g AI 0.29; 433g AI 0.56; 436g AI 0.26; 437g AI 0.30; 438g H 0.12 |
| HG31 | Human | [440g HG31-emuK](https://www.pangram.com/history/79d0de8c-c05a-47ae-bd75-3b6a41725a57) | 429g AI 1.00; 433g AI 0.32; 435g AI 0.16; 436g AI 0.18; 437g AI 0.18; 438g AI 0.18; 439g AI 0.12 |
| HG32 | AI (1.00) | [435g HG32-emuF](https://www.pangram.com/history/5a25465d-60b9-4bea-a03a-011b2ecdcb1a) | 429g AI 1.00; 432g AI 0.99 |
| HG33 | Human | [435g HG33-emuF](https://www.pangram.com/history/a117d978-81e6-471a-b69a-ef650de6bd61) | 429g AI 1.00; 432g AI 0.28 |
| HG34 | Human | [431g HG34-emuA](https://www.pangram.com/history/393c3a23-f072-46b9-bbbd-3b073cb56b87) | 429g AI 1.00 |
| HG35 | Human | [433g HG35-emuC](https://www.pangram.com/history/30bbefef-30dd-4839-8310-faed3b8c9a77) | 429g AI 1.00 |
| HG36 | Human | [431g HG36-emuA](https://www.pangram.com/history/e4da8a40-1ed7-448d-878f-135793d37bd5) | 429g AI 1.00 |
| HG37 | Human | [439g HG37-emuJ](https://www.pangram.com/history/c79fca14-43f7-4f65-9328-30172dbf33f7) | 429g AI 1.00; 433g AI 0.64; 436g AI 0.66; 437g AI 0.53; 438g AI 0.12 |
| HG38+39 | Human | [439g HG38+39-emuJ](https://www.pangram.com/history/33b4df99-cdfd-4b05-b795-e1c6162ea422) | 429g AI 1.00; 433g AI 0.59; 436g AI 0.18; 437g AI 0.15; 438g AI 0.16 |
| HG40 | Human | [432g HG40-emuB](https://www.pangram.com/history/9c0b1518-c6fb-4ba2-89fd-4d8037aa1bcb) | 429g AI 1.00 |

## 2026-10-18 04:00 UTC

**Where it stands.** 37 sections (a section under 50 words checked with the next). 3 read 100% Human as published. 25 more
read 100% Human as Emulate rewrote them (their screens), but those are not installed yet: Emulate bends the meaning (it
invented a "Sarah", quotations, studies' conclusions, turned the inner child into "her", reversed cautions), so each
went through my meaning review against the published text, then a second reader (verify), then a march read. Batch 434g
is the test of whether the meaning-fixed versions still read Human. 9 sections still read AI somewhere (table).

**Running now.**
- Second reader (verify-b) for HG14, HG20, HG35, HG02+03, HG27 and HG33.
- Emulate third samples (`fix-20261018/emu-h/`, 12 runs, 2,988 words) on the laptop: each AI window of 436g (and 435g
  for HG24) sent whole, with its headings, as one run.

**Learned today.**
- Emulate's text reads Human far more often than mine: 25 of 34 sections on the first or second screen.
- Second samples of short pieces (40 to 180 words) inside an AI window don't help: 436g, 0 of 7 Human (HG04 got worse:
  its one 108-word AI window became the whole text).
- My meaning fixes take breaks out: march-c found 6 stretches where the published words I put back read flat
  (HG14 B6, B38, B42, B51, B60; HG35 B2); the gate holds those until a break is back.
- The de-hypnosis checklist (HG32) reads AI in every version (published, Emulate whole, Emulate in six pieces): a list
  of short questions. It needs Joel's call (questions page).
