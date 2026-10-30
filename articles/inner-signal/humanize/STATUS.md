# Status: hypnosis guide humanization (newest on top)

## 2026-10-30, after Joel's answers of 14:35 UTC (the cards page answered; "your "pevious" button brouught me to the bottom of the page")

His message, word for word: `fix-20261030/joel-20261030-1435-message.txt`; his answers file, word for word:
`fix-20261029/b483/review/ANSWERS-20261030-1435.json`; his card comments: `fix-20261030/joel-20261030-1435-comments.txt`.

**His answers are in** (`fix-20261029/b483/review/apply_answers_483.py`, APPLIED-483.json): 9 cards approved (T2, T3,
J1, J2, T10, T11, T13, T14, J4) and 19 in his own versions (T1, J5, T8, T16, N-65, R-96, R-237, R-238, N-239, N-243,
N-276, N-282, R-289, R-509, R-561, R-audit, R-630, R-755, N-757). Eight obvious typos fixed and listed ("telecaster" for
"teleprompter", "can make help smooth", "subsconscious", "awarenes", "sutble", three double spaces). Taken off his text:
the headings he typed above two versions (the guide has them), "this passes:" around R-630, and of R-755's three versions
the one he marked 100% High went in. Kept and asked: N-243's second paragraph ("Deciding to do it: ...", with how to stop),
which his version didn't include. His R-96 comment done: the next paragraph starts "First, access your witnessing
position". The four paragraphs with a typo fix or that change, read by me beside his file
(`fix-20261030/applied/read/`, E294); the comparison gate passes.

**The Previous button** (`fix-20261030/previous-button/`): it went to the last undecided card above and, with every card
above decided, wrapped round to the last one on the page. Now it goes to the card before (decided or not), and at the
first card it stays. Checked in a browser, old and new side by side; test added; suggestion_review.py 1.4.

**His lessons**: E294 (the read beside his text is done by the lead model, not Sonnet; the readers of batches 482 and 483
ran on Sonnet, as `compare_read.py`'s brief said, and missed "in waking life", "the verb" for "one central verb", the
words-as-signal mix-up, "make into" for "declare"; Emulate's "scared to death" for the "frightened" it was sent was
missed by every check since 2026-10-18), E295 (a card says "reads Human" only at High), E296 (his fixes: add clarity,
break a list or a long run with a line that sounds different, an example from life, say who does it; his tells: "one" for
"a", "proof", "secretly/silently", the passive: O46, O43, O47, O48 in `tells_lint.py`, W97 to W100 and J68 in the
registry), E297 (an exercise is given once). The read instructions in `compare_read.py`, `docs/CLARITY-READ.md` and
`docs/FIXING-AN-ARTICLE.md` say the lead model now.

**Next, in progress**: my own read of the whole guide beside the published version (errors like "in waking life", lost or
confused meaning, missing commas, invented content, repeated exercises), then his page.

## 2026-10-29, after Joel's message of 22:23 UTC (batch 483's recheck links; "ok give me the cards i'll fix everything and then you can learn")

His message, word for word: `fix-20261029/joel-20261029-2223-message.txt`. Pull request 262 was merged at 22:19 UTC.

**Batch 483's recheck, read** (`fix-20261029/b483/recheck/read/`: META, WINDOWS and RESULT as before, both SHA-256
matched; `confidence_483.sh` writes CONFIDENCE.md/json and SCORE-A/B.md; `spots_483.py` writes SPOTS.json/md; HG-whole#79
and HG-rest-B#80 right, Mixed). Part A [Mostly Human Written, 3.4% AI](https://www.pangram.com/feed/d7900092-2691-46bd-b76a-d2043526509c)
(try 13): 150 windows, 23 AI (10 Low, 6 Medium, 7 High), 127 Human (60 High, 52 Medium, 15 Low). Part B
[Mostly Human Written, 4.1% AI](https://www.pangram.com/feed/845b60a9-9b58-4824-bc34-29cb1e395efa) (try 11): 81 windows,
12 AI (3 Low, 4 Medium, 5 High, the audit one of them), 69 Human (32 High, 25 Medium, 12 Low). Part forecasts: A 59 of 82
parts right (Brier 0.205, 2 red windows outside the parts), B 39 of 46 (0.123).

**The writers with the shape rules from Emulate's fixes: 2 of 11** read Human in place (T2 High, his J5 Low); the other 9
read AI at High (T4, T5, T6, T9, T15, J3 and T17 as in batch 482; T7 and T12 worse, from Low and Medium). Batch 482's 11
Human versions all read Human again (T3, J1, T10, T11, J4 High; T1, J2, T8 Medium; T13, T14, T16 Low). Red on words
nobody changed: 26 windows, 13 of them red in batch 482's recheck too (the audit among them) and 13 new (part A: "It's all
just soup", Before you begin P3 and P4, Make the hypnosis more active, the two-hand and sleep inductions; part B: the
reframing questions' Nurturer line, "Here is some inner child love.", Appendix K's "not a validated form of treatment").
Against batch 482 (11 of 21), the lessons didn't carry the residue: what passed was an outcome list said as what you
notice in yourself (T2) and a list moved into brackets (J5); definitions (T7, T9), the script (T15, J3), the labelled steps
(T17), the borrowed-adulthood disclaimer (T4) and short instructions (T5, T6, T12) did not. Question 26 stays withdrawn (Joel is rewriting them himself; E293).

**His cards page** ([Hypnosis Guide Cards](https://claude.ai/artifact/SxZ3CYESSGw1KWJp46mRAG), published from this
account with db and downloads; `fix-20261029/b483/review/build_page_483.py` writes REVIEW-483.json, .html,
.artifact.html and .md): 28 cards on `HUMANIZED-SO-FAR.md` as it is. 13 to approve (9 ours, "Reads Human now"; 4 his
lines with a suggestion, "Your own words": J1, J2, J4, J5), each with how its words read before and how the new version
read in place (both rechecks for batch 482's), and the comparative read. 9 "For you to rewrite" (one per paragraph that
still reads AI: R-96, R-237, R-238, R-289, R-509, R-561, R-630, R-755, and the audit), each with the paragraph as both
tries read and how they read, plus any other words of the paragraph that read AI in the latest recheck. 6 "Reads AI,
not tried yet" (N-65, N-239, N-243, N-276, N-282, N-757): the rest of the red on unchanged words, by stretch. Its
decisions collection was empty at publishing. `tools/humanization/suggestion_review.py`'s card text now takes
`[name](https://...)` links and line breaks (test added), so a card names each Pangram check by its part.

## 2026-10-29 20:15 UTC: the Emulate lessons, and batch 483 pasted

**What Emulate's fixes teach** (`fix-20261029/emulate-lessons/`: LESSONS.md, PAIRS.json, build/; the brief is
`fix-20261029/EMULATE-LESSONS-BRIEF.md`). 98 pairs from 18 batch groups (68 passing, 22 failures, 8 reverse), every quote
checked against its file (by the study and again by me: 98 of 98 found). The brief already named what Emulate takes out;
it lacked how Emulate builds: it keeps or lowers the sentence count, chains steps, lets sentences run long, keeps lists
inside the sentence, asks a framed test directly. Batch 482 checked by my own count: same sentence count, 9 of 12 Human;
more sentences, 2 of 9. Emulate changed meaning in 52 of 70 passing pairs (dropped qualifiers first); under 4.1 its raw
output read Human in 2 of 6 screening samples; free-standing definitions, outcome lists and label-and-colon steps passed
only when it dropped them. The shape rules are in `docs/EMULATE-FALLBACK.md` section 1 (for every lane's writers) and
`fix-20261029/b483/LESSONS-FOR-BRIEF.md`; `tools/humanization/emulate-cases/README.md` indexes the cases (section 5).

**Batch 483** (`fix-20261029/b483/`): `make_targets.py` (TARGETS.json: the 9 stretches of ours whose batch 482 version
read AI, his J3, and his HG-S15 sentence as J5, each with its last try and how it read, the red beside it, and a note on the
four shapes nobody has solved); three writers (writers/BRIEF-W1..W3.md: the shape rules, what read AI last time); my picks
(CHOICES.json; no pick splits a sentence: T4, T7, T9, J3 and T15 join theirs); `make_b483.py` (CANDIDATE-MASTER.md:
batch 482's 11 Human versions word for word plus batch 483's 11, no link dropped); the comparative read (read/, one fresh
reader: 10 of 10 pass). The recheck (`b483/recheck/`): payloads (merge PASS; part B starts at the same section),
`make_changed.py` (each candidate 0.5 or 0.4 by its last try; red next to a rewrite 0.4, red that moved 0.55, the audit
0.95), FORECAST-A.json (82 parts, 9.7 expected red if independent) and FORECAST-B.json (46, 5.4); ledger HG-whole#79 (try
13, AI, 0.05) and HG-rest-B#80 (try 11, AI, 0.03); pushed at 0fc62a44, both drafts cleared and pasted from that commit
(editor words +34 and +25), saved bodies checked, and the secret links render exactly TEXT-A.txt's first 99,999
characters and TEXT-B.txt (RECHECK-POST-A.json, RECHECK-POST-B.json; cache keys recheck-a-29c and recheck-b-29c). The
links are on his questions page.

## 2026-10-29, after Joel's message of 19:22 UTC (batch 482's recheck links; "26 not sure why you are asking before even checking if you can learn the lessons")

His message, word for word: `fix-20261029/joel-20261029-1922-message.txt`. Pull request 261 was merged at 19:20 UTC.

**Batch 482's recheck, read** (`fix-20261029/b482/recheck/read/`: META, WINDOWS, RESULT rebuilt from the payloads with
`substack_check_text.py result`, both SHA-256 matched; CONFIDENCE.md; SCORE-A/B.md; HG-whole#77 and HG-rest-B#78 right,
Mixed). Part A [Mostly Human Written, 2.3% AI](https://www.pangram.com/feed/19fba559-fe64-46a3-92a1-ab87f728b4ba) (try
12): 158 windows, 20 AI (8 Low, 6 Medium, 6 High), 138 Human (62 High, 58 Medium, 18 Low). Part B
[Mostly Human Written, 3.9% AI](https://www.pangram.com/feed/82470746-1d28-4ddc-ac19-276ca31c19f2) (try 10): 87 windows,
13 AI (4 Low, 4 Medium, 5 High, the audit one of them), 74 Human (34 High, 28 Medium, 12 Low). Part forecasts: A 83 of 96
parts right (Brier 0.105), B 53 of 62 (0.110), no red outside the parts.

**The writers without Emulate** (`spots_482.py`, SPOTS.md): 11 of 21 candidates read Human in place (J1, J4, T3, T11,
T16 at High; J2, T1, T8, T10 Medium; T13, T14 Low) and 10 still AI (T2, T4, T5, T6, T9, T15, T17 and J3 at High, T12
Medium, T7 Low). T2, T5, T6, T12 and T17 went from AI Low to AI Medium or High; T7 went from AI High to AI Low. Red moved
onto 14 windows of words this batch didn't change, all next to rewrites: Why doing it myself P1 (after T2's paragraph,
the heading between them not in the checked text), the six metaphors section from the line before P1 to P3 (around T5
and T6), Make the hypnosis more active P1, the no-trance Choice line (T17's paragraph) and "The personal accounts and the
way I arrange this practice" (after it). The three-jobs line, his Quick start line and the Nimja line read Human; his
HG-S15 list and the audit read AI as before.

**26 withdrawn; lesson E293** (`docs/HUMANIZATION-GATE.md`; `docs/EMULATE-FALLBACK.md` sections 1 and 6): a question that
spends his money waits until the free work that could answer it is done (here: the study of the Emulate cases we have,
and the writers fed with its lessons on the failures). His questions page has no open questions.

Next: when the study (`fix-20261029/emulate-lessons/`) is in, check its pairs against their files, put the shape rules
that two or more cases back into the writers' brief, and run batch 483 on the 10 spots that still read AI (each from the
working copy's clear version, the writers shown what read AI in batch 482), read beside his published text, then the
recheck with batch 482's 11 Human versions in; then his marking page with every version that reads Human and clear.

## 2026-10-29, after Joel's messages of 18:18 UTC (the recheck's result links) and 18:55 UTC (Emulate: re-up or learn)

His messages, word for word: `fix-20261029/joel-20261029-1818-message.txt` and `fix-20261029/joel-20261029-1855-message.txt`
("emulate is 50k words for $15 per month. i'm not sure it is worth re-upping on it. well maybe it is. and i wonder if we
really understood all the lessons from emulate's fixes or if we can learn enough from what we got that we wouldn't need
it anymore").

**The recheck read** (`fix-20261029/recheck/read/`; HG-whole#75, try 11, and HG-rest-B#76, try 9, both right). Part A
[Mostly Human Written, 1.6% AI](https://www.pangram.com/feed/d1e283a5-efcf-4fc4-ad6f-d535e12951b2): 170 windows, 11 AI
(8 Low, 1 Medium, 2 High) and 159 Human (69 High, 70 Medium, 20 Low). Part B
[Mostly Human Written, 4.5% AI](https://www.pangram.com/feed/f9b45a7b-402c-412c-af68-a5f9ca44f6e6): 91 windows, 20 AI
(11 Low, 2 Medium, 7 High, the audit one of them) and 71 Human (33 High, 26 Medium, 12 Low). CONFIDENCE.md lists every
window below High with whose words it holds; SPOTS.md reads our 140 changes of 28 and 29 October in place (112 High, 12
Medium, 5 Low, 8 AI Low, 3 AI High: most AI readings are where a fix brought back his published sentence, the AI-written
one, as with the fractionation definition, the embedded invitation and the wellness trade show line).

**Batch 482, the next try** (`fix-20261029/b482/`; his rule for 25, E291: the clear version stays, and the new one has to
be clear and Human). `make_bundle.py` sorted every sentence of the windows below High (SORTED.json: to Emulate, his own
words to him, the audit left). Emulate's balance was 0 words at 18:28 UTC, so fresh writers made the versions, for the
AI windows first (the Low and Medium Human windows wait): `make_targets.py` writes TARGETS.json, 17 stretches of ours (T1
to T17) and 4 of his own lines that read AI (J1 to J4, suggestions only: they go in with his answer or not at all). Left
out: the Nimja link line; the three-jobs line (his inner child guide's sentence with its middle cut, to him with his full
sentence as my suggestion); his HG-S15 list and his Quick start line, whose windows start in our sentences before them.
Four writers (writers/BRIEF-W1..W4.md, each with the 4.1 tells and his rule) wrote two versions of each; I chose one
(CHOICES.json, each with its reason; one logged fix, T2's first sentence taken from v1). `make_b482.py` puts the picks in
CANDIDATE-MASTER.md (21 spots, no link dropped); the working copy doesn't change until he answers.

**The comparative read** (`read_candidates.py`, read/): two fresh readers, each paragraph beside his published version and
as it stands: 20 of 20 pass (clear, says what his says; 7 easier than before, 13 the same). `read_candidates.py` now also
gives the reader the published paragraph holding the very sentence a candidate changes (TARGETS.json's two closest
published paragraphs missed T3's "Self-hypnosis simply has one advantage ...", which is in the one before).

**The candidate recheck** (`fix-20261029/b482/recheck/`): `make_recheck.py` from CANDIDATE-MASTER.md (merge PASS; part B
starts at Your functioning in ordinary life is the feedback, as last time). `make_changed.py` gives each candidate its
chances by how its stretch read (all AI Low: red 0.2; any Medium or High: 0.35), and adds what read AI last time and is
unchanged (his HG-S15 list 0.55, the three-jobs line 0.65, his Quick start line and the Nimja line 0.3, the audit 0.95);
`part_forecast.py` (with --medium, rest 0.25) writes FORECAST-A.json (96 parts, 6.2 red expected if independent) and
FORECAST-B.json (62 parts, 6.5). Ledger: HG-whole#77 (try 12, AI, 0.05 chance of 100% Human) and HG-rest-B#78 (try 10, AI,
0.03: the audit). Pushed at e859ce30 (pull request 261), then both drafts cleared in the editor (ctrl+a, Delete) and
pasted with `paste_payload_lane.js` from that commit (SHA-256 checked; editor words +34 and +25, as every paste); the
drafts' saved bodies hold the new words; the secret links render exactly TEXT-A.txt's first 99,999 characters and
TEXT-B.txt (RECHECK-POST-A.json, RECHECK-POST-B.json, cache keys recheck-a-29b and recheck-b-29b).

**Emulate (his message of 18:55).** My advice: hold off re-upping until this recheck is read, since it is the direct
test of the writers without Emulate (none of the 21 versions came from it); if a third or more stay AI, one month ($15,
50k words; a round here is a few hundred words) for the spots the writers fail twice. His second question: the lessons
were not fully learned. `docs/EMULATE-FALLBACK.md` section 5 (save each case, pair each loud sentence with Emulate's
replacement by its change in shape) was never carried out: `tools/humanization/emulate-cases/` doesn't exist. A study of
the lane's own Emulate batches is running (`fix-20261029/emulate-lessons/`: PAIRS.json and LESSONS.md, the shape
changes the writers' brief lacks); its lessons go into the next round's brief.

## 2026-10-29, after Joel's message of 17:21 UTC (his answers to 24 and 25)

His message, word for word: `fix-20261029/joel-20261029-1721-message.txt` ("25 we never publish nonsense because it passes
pangram. we come back and we try again if clarity loses on pangram." and "approve all the cards and where there's no
"approve" option just take the advice given").

**His answers are in** `HUMANIZED-SO-FAR.md`: all 114 fix cards approved, and my advised wording on the four cards in his
own words, which have no Approve button (`fix-20261029/build_decisions.py`, DECISIONS-20261029.json: his decision in the
page's export form, named DECISIONS and not ANSWERS so that the comparison gate doesn't count my wording as his words).
`fix-20261028/comprehension/apply_answers_28.py` now takes the cards in his own words first and puts a fix on the same
paragraph on top (C-91 and C-92 share Appendix D's P2; before, the fix card overwrote his answer), carries an answer to a
second paragraph ("also": C-59's note said its answer went for Working with your guards, P6 too) and records each card's
fate (APPLIED-28.json; no link lost). The five paragraphs with my wording were read by a fresh reader beside his
published version (`fix-20261029/comprehension/read_advice.py`, verify/): 5 of 5 pass. `write_records.py` takes his
answers as the findings' fates: 137 fixed, 21 small snags kept, 6 his, 116 not, 1 done; three fixes change only
punctuation (C-1, C-25, C-54), which the gate's loose text doesn't see, so their findings stay on record as kept at my
severity 1. The comparison gate passes (0 unread, 0 open).

**His rule for 25**, lessons E291 (clarity is never traded for a Pangram reading: the clear version stays and the next try
has to be both) and E292 ("take the advice given" puts my words in, and they get the read): `AGENTS.md`,
`docs/FIXING-AN-ARTICLE.md` section 5, `docs/EMULATE-FALLBACK.md` (the bullet that waited on his ruling) and
`docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`.

**The recheck, built and forecast** (`fix-20261029/recheck/`): `make_recheck.py` from the guide itself (merge PASS; the
helper interaction tests pass): part A is the first 99,999 characters (18,197 words), and part B starts at Your
functioning in ordinary life is the feedback, a section earlier than last time, since the fixes made the main guide
longer (11,073 words). `make_changed.py` writes CHANGED-A.json (89 paragraphs the last check didn't read) and
CHANGED-B.json (65, and the audit as one part), each with my chances from one stated rule (new words, and runs of 8 or
more words brought back from his published version, the AI-written one); `tools/humanization/part_forecast.py` writes
FORECAST-A.json (182 parts) and FORECAST-B.json (133). Ledger: HG-whole#75 (AI, 0.15 chance of 100% Human) and
HG-rest-B#76 (AI, 0.03: the audit).

**The paste, after his "i signed in" (17:53 UTC).** At first Substack was signed out in the desktop app's browser (the
drafts API answered 403; pull request 259 went out with the recheck waiting on that). After he signed in: both drafts
cleared in the editor (ctrl+a, Delete), pasted with `fix-20261022/screen/paste_payload_lane.js` from commit 2fa3b7b5
(SHA-256 checked; editor words +34 and +25, as every paste of parts A and B), saved, and read through their secret links
with `tools/humanization/substack_rendered_check.js`: part A's first 99,999 characters hash to TEXT-A.txt's SHA-256, and
part B, with its web-app card line left out as before, to TEXT-B.txt's (RECHECK-POST-A.json, RECHECK-POST-B.json). The
two links are on his questions page; the results come back as feed links.

## 2026-10-28, after Joel's messages of 15:20 UTC ("the guide itself is now too incomprehensible") and 16:05 UTC ("repair the process durably")

His messages, word for word: `fix-20261028/joel-20261028-1520-message.txt` (with his answers file from the editor page,
`fix-20261028/ANSWERS-20261028-1519.json`: HG-S11 and HG-S12 approved, ED-A1, ED-A3, ED-A5 and HG-S15 revised, 83 not
marked) and `fix-20261028/joel-20261028-1605-message.txt`.

**His six answers are in** `HUMANIZED-SO-FAR.md` (`fix-20261028/comprehension/make_candidate.py --answers-only`,
CHANGES-ANSWERS.json): his four versions word for word (ED-A5's one sentence replaces its whole paragraph; HG-S15's "can
are" became "are", the one obvious typo), and the two approved cards' words.

**The comparative read** (`fix-20261028/comprehension/`, AUDIT.md): fresh readers went through the whole guide as it was
at 15:20 (commit 0a44911d) beside his published version, sentence by sentence (`make_chunks.py`, eleven parts; six of
them again in halves, `make_halves.py`, after their first readers hit the 64,000-token limit). 281 findings; my check of
each (CHECKED.json, against the whole guide and his decisions: his terms, his cuts of 25 October, his inner child guide's
lines): 41 real problems in 38 of 591 paragraphs (6 at severity 3), 118 small snags in 95 more, 6 in his own words, 116
not problems. 23 of the 41 came in on 18 October, 13 between 20 and 23 October, 4 on 25 October, 1 is his published
sentence whose lead-in was dropped; 29 of the 41 had been flagged by the 25 October strict check's readers and left as
"small", 11 named on 18 October and let stand. The diagnosis went to him at 15:57 UTC.

**The fixes** (`fix/`): fresh writers per part (`make_fix_briefs.py`, BRIEF-FIX-k), my review of every fix
(`review_fixes.py`, MY-REVIEW.json: kept, changed or dropped, with why), the candidate (`make_candidate.py`: CANDIDATE.md,
CHANGES.json), and fresh readers of every fixed paragraph beside his published one (`make_verify.py`, `collect_verify.py`,
verify/). The writers proposed 144 fixes; I dropped 7 and changed 24 (MY-REVIEW.json), so 137 are kept, in 114
paragraphs: every one of the 40 real problems (the 41st was settled by his own HG-S15 version) and 97 of the 118 snags.
Eleven fresh readers then read all 114 fixed paragraphs, and the one his two approved cards changed, beside his published
version (CLEAR, SAYS, BETTER): all passed, 3 of them (P589, P728, P752) after a second fix, when the first had left out a
point of his. My check had counted one more real problem at first: the sober induction's countdown seemed to start at 4,
but its "5." is a list number the readers' plain text dropped, and the writer's added "5." would have doubled it (E290).

**The fix page** ([Hypnosis Guide Fixes](https://claude.ai/artifact/BC6AzFGSwc6MSgoWR2upLd), published from this account; `build_page.py`: REVIEW-28.json,
.html, .artifact.html, .md; browser test 82 of 82): 118 cards, 114 fixes, one per paragraph (25 where a sentence doesn't
read, 12 where a point was lost or changed, 77 small snags), and 4 passages in his own words to keep or edit. It is
question 24; question 25 asks which wins when a clear fix reads AI or below High in the recheck (my default: clarity).
The comparison gate passes on the guide now and on the guide with every fix approved (`fix-20261028/comprehension/GATE-CANDIDATE.json`,
the same gate on CANDIDATE.md).

**The durable repair** (his 16:05 message; lessons E284 to E290):
- `tools/humanization/compare_read.py` (make, collect, record, gate; tests/test_compare_read.py): the comparative read for
  any article, and the gate: every paragraph his as published, his own words, or read beside his text at its present
  words; every finding a reader rated 2 or 3 with a fate and a reason; a garbled or unclear one never "kept" unless my
  check put it at 1, on record. The reader's text shows a list's numbers, bullets and quote marks as the page does
  (E290: a countdown's "5." was lost from the text, and I had counted it a real problem).
- `tools/humanization/lane_push.py` runs the gate for every COMPARE-GATE.json in the article's folder before committing,
  and stops; `--unread-ok "why"` puts the reason in the commit. This lane's is `COMPARE-GATE.json` (records:
  `fix-20261028/comprehension/READ-RECORD.json`, `verify/READ-RECORD.json`; `write_records.py`).
- `tools/humanization/clarity_read.py`: casual grammar is his voice in his own words only; `collect --prior` carries an
  earlier run's findings, and collect warns about a sibling run left out (tests in tests/test_clarity_read.py).
- `tools/triage_apply.py` refuses a triage that lets an unclear or garbled finding stand; the 18 October triage brief is
  marked superseded.
- Shared rules: AGENTS.md, `docs/FIXING-AN-ARTICLE.md` section 5, `docs/CLARITY-READ.md`, `docs/EMULATE-FALLBACK.md`
  section 4 (step 0a), `docs/HUMANIZATION-GATE.md` E284 to E290.

**On hold:** the 83 cards of the 27 October editor page he hadn't marked (questions 21 to 23); most offer Emulate's
re-runs, which get the comparative read before they come back (E288).

## 2026-10-27, after Joel's message of 15:37 UTC (batch 481's recheck links; questions 21 to 23 on one editor page)

His message, word for word: `fix-20261027/joel-20261027-1537-message.txt`.

**Batch 481's recheck, read** (`fix-20261026/b481/recheck/read/`: WINDOWS, META, RESULT, CONFIDENCE, SCORE, SPOTS):
[part A](https://www.pangram.com/feed/a67b13cb-7267-466e-9350-e70836380857) Human Written, 0 of 116 windows AI (58 High, 55 Medium, 3 Low); [part B](https://www.pangram.com/feed/9fd5c1d9-6766-439e-ba4b-8b8eb5108ee4) Mostly Human Written, 1.3%
AI, the audit (2c) the one AI window (20 High, 16 Medium, 1 Low). HG-whole#73 a miss (pessimism again, explained),
HG-rest-B#74 right; the part forecasts 53 of 53 (Brier 0.006) and 17 of 17 (0.008). Of batch 481's 24 fixes, 19 read High
in place, S14, S25, S28 and S31 Medium, S29 Low (`spots_in_place.py`; my chances of High scored 0.288 against a coin's
0.25, lesson E283). Of the ten older cards, nine read High and S5's no-warmth line Medium.

**The Hypnosis Guide Editor** (https://claude.ai/artifact/1ubA7VJSFNPhdtXFyrnEDG, published from this account; `fix-20261027/review/build_editor_27.py`,
EDITOR-27.json, .html, .md, browser test 84 of 84): question 21's 34 cards with their readings now and before
(`readings.py`, READINGS.json; S14 and S29 now advised "leave"), question 22 as 54 stretches to edit (every other window
under High: 35 short lines, 19 longer), question 23 as one stretch to edit (the audit, with Emulate's closest version for
ideas). The old page (other account) showed none of its highlights: its four card kinds had no colours.

**Tools**: `suggestion_review.py` 1.3: the "edit" card (Keep it as it is / Edit it), colours for every card kind, no
doubled advice label; the browser test checks edit cards and that every open highlight has a colour; a unit test.
Lessons E280 to E283; AGENTS.md's marking-page rule says where text to edit goes and that the page's cards are in Git as
Markdown.

## 2026-10-26, after Joel's message of 12:43 UTC (batch 480's recheck links; the questions page; the preview link; confidence)

**Batch 480's recheck, read** (`fix-20261026/b480/recheck/read/`): [part A](https://www.pangram.com/feed/0f1902cd-df2a-4837-9879-69979188e5f1)
Human Written, 0 of 153 windows AI (71 High, 68 Medium, 14 Low); [part B](https://www.pangram.com/feed/1a9e674f-113e-46ad-8a07-0fb6b71ad65e)
Mostly Human Written, 1.3% AI, the audit (2c) the one AI window (25 High, 20 Medium, 1 Low). HG-whole#71 a miss
(pessimism, explained), HG-rest-B#72 right; the part forecasts 27 of 27 (Brier 0.017) and 14 of 14 (0.010). Nine of the
ten cards read High in place; S3b's stop lines Medium, Low, Medium.

**The questions page** ("Hypnosis Guide Questions", https://claude.ai/artifact/8o79MFm9vSpyMGrAeArZYx): the guide's own
view of `OWNER-QUESTIONS.md` (`guide-questions.html`, `render_questions.py` with a page title); his "no open questions"
was the community page and InnerSignal's.

**Lesson E279** (a word of his that a sample drops goes back before the gate). **Two standing rules** (AGENTS.md, `docs/HUMANIZATION-GATE.md` E277 and E278, `docs/PANGRAM-PRODUCTION-BUDGET-20261020.md`,
`docs/FIXING-AN-ARTICLE.md` 14, memory): the secret preview link for every lane (`tools/humanization/substack_secret_link.js`),
and confidence for every window (`tools/humanization/window_confidence.py`, test).

**Batch 481** (`fix-20261026/b481/README.md`): Emulate's samples of the 22 groups with a Low window or a Medium one of 10
words or more (cm, cn, co), and of the audit; 24 splices, the strict Emulate check (clean), five linter FAILs fixed (one
spot dropped), the gate (24 drafts, 24 delivered after two rounds: five failed the first (S14, S31, S32, S34, S36, each on a word or mark of his) and were fixed and reviewed again with the two whose sections changed with them (S15, S30, S33)). The windows left and why are in CANDIDATES.json and his page.

**Question 21's page** (34 cards, REVIEW-481, browser test 74 of 74) republished to the same artifact; **questions 22 and 23**
open; **the recheck with batch 481 in** built, forecast (CHANCES.json with a chance of High per spot), predicted
(HG-whole#73, HG-rest-B#74), pasted and checked rendered, with each draft's secret preview link.

Predictions: HG-whole#71 a miss (explained), HG-rest-B#72 right; HG-whole#73 and HG-rest-B#74 open.
Delegations (model, piece, check, outcome): Sonnet ×36, the gate's reviewers (24 in the first round, eight groups by three roles; 12 in the second, four groups) in groups of two or three drafts, one at a
time (`b481/gate/BRIEF-<role>-<group>.md`), each review file checked by `owner_delivery_gate.py` against the drafts' hashes:
96 review files, 88 PASS and 8 FAIL (five drafts, all fixed and passed by fresh reviewers); group h's three reviewers also wrote five of their files again into folders that had moved, which are kept in `b481/gate/superseded/`, and two of them were stopped (lesson E279).

## 2026-10-26, after Joel's message of 00:54 UTC (batch 479's recheck links)

**Batch 479's recheck, read** (`fix-20261025/b479/recheck/`): [part A](https://www.pangram.com/feed/9b9bedd2-a7d1-4141-9d85-168fbe3e81e4)
Mostly Human Written, 0.9% AI, 7 of 153 windows AI; [part B](https://www.pangram.com/feed/84384f22-e09d-4a3b-bd39-a6617cd21cd1)
Mostly Human Written, 1.5% AI, 2 of 53 (one the audit he kept). HG-whole#66 and HG-rest-B#67 right; the part forecasts 21
of 23 (Brier 0.102) and 13 of 16 (0.170). S2 to S6 read Human in place; S1, his whole three-jobs sentence, read High red;
three unchanged stretches turned red (lesson E276).

**Batch 480** (`fix-20261026/b480/`): Emulate's versions of the four red stretches (S7 to S10), two meaning reads, the
linter's fixes, API checks 480g (#68 S7 Human, #69 S8 with the guard prompt Human, #70 S9 Mixed: Emulate's sentences
Human, the paragraph's unchanged tail red alone; explained). The recheck with every candidate in is predicted (HG-whole#71,
AI at 0.08; HG-rest-B#72, AI at 0.02), forecast, pasted into both drafts and checked rendered.

**The owner-delivery gate** (`fix-20261026/gate/GATE.md`): ten drafts (batch 479's six, batch 480's four), 10 of 10
delivered. S5's "Don't fake it." failed preservation (his line is a release) and became his own "no faking required".

**Question 21, the marking page**: ten cards on his working copy (`fix-20261026/review/`, 74 of 74 in the browser test),
published at https://claude.ai/artifact/TpZbfBZcwuj8PL7KFLhmjP. Waiting on his marks and the recheck's two links.

**Lesson** E276 (red moves onto text nobody changed); `docs/FIXING-AN-ARTICLE.md` 6.13; `part_forecast.py`'s Low default
0.02 to 0.05 (4 of 75 measured).

Predictions: HG-whole#66 and HG-rest-B#67 right (Mixed); 480g #68 and #69 right (Human), #70 a miss (Mixed; "context: Human
in the whole guide, red alone"); HG-whole#71 and HG-rest-B#72 open.
Delegations (model, piece, check, outcome): Sonnet, the meaning read of S7 and S8 (`b480/REVIEW-1.md`), checked against
his lines by me: S7 fixed ("keeps"), S8 kept; Sonnet, S9 and S10 (`b480/REVIEW-2.md`): kept; Sonnet, fifteen gate reviewers
in five groups of two or three drafts, one at a time (`gate/BRIEF-<role>-<group>.md`), each review file checked by
`owner_delivery_gate.py` against the drafts' hashes: 33 review files, 32 PASS and one FAIL (S5's first draft, fixed and
reviewed again by three fresh reviewers, all PASS).

## 2026-10-26, after Joel's message of 2026-10-25 23:50 UTC (the two recheck links)

**The recheck, read** (`fix-20261025/recheck/`: WINDOWS-A/B.txt checked against the pages' SHA-256, META, RESULT,
SCORE): [part A](https://www.pangram.com/feed/4c912830-87c4-4ee1-bff1-5acc606dc4f7) Mostly Human Written, 0.9% AI, 7 of 161
windows AI in three places; [part B](https://www.pangram.com/feed/6b07dbba-8dc6-42a0-b562-b46dbe778919) Mostly Human
Written, 2.2% AI, 8 of 61 windows AI in four places, one the audit he kept (2c). HG-whole#60 and HG-rest-B#61 right. The
part forecasts: A 244 of 248 parts right (Brier 0.016), B 156 of 162 (0.035), no red outside the forecast's parts. Pull
request 251 was merged before his message; this turn is pull request 253.

**Where the red came from** (`fix-20261025/b479/README.md`): four of the six stretches are in paragraphs his marking pages
changed: IC-A2 (his inner child guide's sentence with his rent joke cut out), EM-2 (my plainer words, gated, approved),
RR-4.1 and RR-4.6 (the stop lines before an induction), IC-B12 and IC-B14 (his inner child guide's words). The sixth is his
published test, put back by EM-16.

**Batch 479** (`fix-20261025/b479/`): Emulate first, three samples of each red paragraph; his own whole sentence for IC-A2;
splices of the red sentences only, after two meaning reads (one change to the caution's claim, one sample swapped, two of
cg's lines left as they were); the four High spots read Human, High, alone through the API (479g, 4 of 4 predictions
right). A recheck with every candidate in (`b479/recheck/`, from CANDIDATE-MASTER.md; the working copy is unchanged) is
predicted (HG-whole#66, AI at 0.20; HG-rest-B#67, AI at 0.02 for the audit), forecast part by part, pasted into the same two
drafts and checked rendered. Waiting on his Brave for the two results; then the candidates that read Human in place go on
his page, with the owner-delivery gate for Emulate's words.

**Lesson** E275 (an alignment card brings his whole sentence, not a trimmed one).

Predictions: HG-whole#60 and HG-rest-B#61 right (Mixed); 479g #62 to #65 right (Human); HG-whole#66 and HG-rest-B#67 open.
Delegations (model, piece, check, outcome): Sonnet, the meaning read of S1 and S2 (REVIEW-A1.md), checked against the
published lines by me: S2 fixed; Sonnet, S3a and S3b (REVIEW-A2.md): S3a's sample swapped, S3b fixed; Sonnet, S4 to S6
(REVIEW-B.md): kept; Sonnet, round 2 on S2, S3a, S3b (REVIEW-A3.md): S3a's trigger fixed, S3b's last two lines left as
they were, S2's two practices left out with the reason. Each reader had two or three items (E270).
InnerSignal protocol loaded in the main thread: 0.2.1, 6d30a6b4...1e120f (read whole before the inner child candidates).

## 2026-10-25, after Joel's message of 23:05 UTC ("251 has conflicts", "66a", and his answers to question 20)

**Pull request 251**: main had merged the Inner Child lane's turns 111 and 112 after my pushes, and both lanes' lesson
numbers met in `docs/HUMANIZATION-GATE.md`. Merged twice, both lanes' lessons kept; 251 can merge.

**His answers to 20 are in** (`fix-20261025/emulate-check/apply_answers_20.py`, `APPLIED-20.json`; his message and his
answers file `ANSWERS-20261025-2300.json` saved word for word): 17 approved; his own versions of EM-Q1 (Emulate's quote
marks off in 84 of 85 places, "coming back" keeping them; "Just because an idea should be a resource ..." cut; two
"protector"s made "guard") and EM-16 ("if it's a guard"); EM-11 rejected ("actually emulate's version is better, hypnosis
is for pain btw, surprised you didn't know that"): Emulate's sentence stays, its quote marks with it. 69 paragraphs
changed, the ISH link kept on "article about self hypnosis".

**The guard sweep** (his comment on EM-Q1; `guard_sweep.py`, `GUARD-SWEEP.json`): 19 places where "protector" meant a
guard say guard now (the heading is "Working with your guards"); the 20 uses of the adult Protector and the 3 bracketed
glosses right after "guards" stay. **The strict check again** (`emulate-check/after-20/`, with his question 20 sentences
in ALLOWED.txt): nothing new; what's left is what he left or what was triaged before.

**The whole guide's recheck** (`fix-20261025/recheck/`): `make_recheck.py` (part B now starts at Closing, a section
before part A's 99,999-character cut, since the main guide grew past it and its last 1,349 characters were in neither
part), `make_changed.py` (136 and 88 changed paragraphs), FORECAST-A/B.json (0.1% and 0.3% chance of no red; neighbours
at 0.02, since most changes are marks and single words), predictions HG-whole#60 and HG-rest-B#61, then pasted: part A
into a new draft (222109105; the old one was gone), part B into its draft (221412532); both rendered texts hash to
TEXT-A/B.txt (RECHECK-POST-A/B.json). Waiting on his Brave for the two results.

**Lessons** E272 (his line is checked for what it says), E273 (Emulate's quote marks are a card, his register decides),
E274 (his terms follow his newest guide); `docs/FIXING-AN-ARTICLE.md` 6.10 and 6.11.

Predictions: HG-whole#60 and HG-rest-B#61, AI at 0.01 each, open.
Delegations (model, piece, check, outcome): none; each piece needed this turn's context or was a check run here.
InnerSignal protocol loaded in the main thread: 0.2.1, 6d30a6b4...1e120f.

## 2026-10-25, after Joel's message of 19:42 UTC (his answers in; the strict Emulate check; the community check)

**His answers are in the guide** (`fix-20261025/review/apply_answers.py`, `APPLIED.json`; his message and answers file are
saved word for word): 139 he approved, his own versions of 4 (RR-2.1, RR-7.3, RR-8.3, CV-8.9), 35 he left to my advice
that I advised, and 118 left out; 138 paragraphs changed, 18 blocks added and 8 moved. His comments are passes over the
whole guide: "the kid" (and "my kid") is "your little one", no quote marks around inner child, and IC-T1's they/them on
the words the other cards added. Where two cards changed one paragraph both went in, change by change; the follow-on fixes
are named in `APPLIED.json` ("These cues", "the inner meeting", "etc).", and Appendix G pointing to IC-A17's lines).

**The strict Emulate check** (`fix-20261025/emulate-check/`, `tools/humanization/emulate_artifacts.py`, lesson E268):
the guide against his published post, his drafts, his inner child texts, his messages and today's approved sentences.
Fixed outright: 9 more spaces before punctuation (31 with his TY-6), 53 typos and slips (`fix_typos.py`), the
references' italics, "(1995) pp" and "randomized controlled trials" (`fix_citations.py`). Ten Sonnet readers read every
changed paragraph beside his (808 findings, `READS-ALL.json`; my fate for each that matters in `TRIAGE.md`). The rest is
**question 20, the Emulate check page** (REVIEW-EMULATE: 20 cards: 85 quote marks as one card, 16 changes of meaning, 3
sources; https://claude.ai/artifact/FUoU6T1mGt1WiQBP1UjaWW), its new sentences of mine through main's owner-delivery gate
(`emulate-check/gate/`, GATE.md from `run_gate.py`): 10 drafts delivered after three PASSes each; 6 withdrawn on round 1's
fails, their cards using his own words; the rest are his words or a word of his (EM-8 now his "enter": "when entering the
trance"). Browser test 74 of 74 on the final page. **The community article** got the same check (its STATUS).
Also: `repo_links.py fix` linked to the Inner Child lane's branch by default; it now links to the branch it runs on (test).

**The standard**: `AGENTS.md` now says editing suggestions go on the marking page, and that every Emulate-infused article
gets the strict check; `docs/EMULATE-FALLBACK.md` (step 5.0) and `docs/FIXING-AN-ARTICLE.md` (6.9) say how; lessons E268
and E269. E270: the owner-delivery gate's reviewers get two or three drafts each (its doc says so now).

Predictions: none (no Pangram check this turn: the guide is checked once, after his answers on the Emulate page).
Delegations (model, piece, check, outcome): 12 Sonnet readers of the guide's paragraph pairs (parts 1 to 9, and part 10
in two halves after its reader ran out of output; every quote searched in the guide, every "matters" finding checked by
me against his texts and records: 20 cards); 8 Sonnet readers of the community's pairs (60 findings checked: 6 cards);
the owner-delivery gate's reviewers (GATE.md): round 1, 3 Sonnet agents, one per role over 16 drafts; the preservation
reviewer and cold reader 2 wrote all 16 (6 drafts failed: withdrawn), and cold reader 1 read all 16 before writing any and
was stopped after 46 minutes with none written; round 2, 4 Sonnet cold readers over the 10 left, 2 or 3 each and one at a
time, with a fresh preservation reviewer and cold reader 2 for C-E3a (its context changed): all PASS, in about 9 minutes.
InnerSignal protocol loaded in the main thread: 0.2.1, 6d30a6b4...1e120f.

## 2026-10-25, after Joel's message of 14:40 UTC (the reader fixed, the inner child alignment, the review page)

**The review page** is question 19 (`OWNER-QUESTIONS.md`): his whole guide with 178 suggestions marked where they apply,
colour-coded by kind, each with Approve / Reject / Revise / Not approved yet and a comment box
(https://claude.ai/artifact/HAPtqUNY4cYvk48TA4eYHp; Git: `fix-20261025/review/REVIEW.json` and `REVIEW.html`, made by
`review/build_review.py` with `tools/humanization/suggestion_review.py`). It replaces questions 15 to 18. On it: the
reread run again on the fixed brief (`clarity2/`: 80 passages, 47 offered, 32 I'd leave; three of the first reread's),
the reader's edit (30 offered, 3 I'd leave), the caveats (32 and 36), the repeats (18 and 46), the inner child alignment
(`ic-align/`: 43 differences with his latest inner child guide, 42 offered and his they/them for one section), and 6
typos. His 15.1 wording is in, decided by him (RR-1.1). Tested in Chromium: 74 checks passed (`review/BROWSER-TEST.json`).
The reread's brief is fixed (E264), and a long list of suggestions now ends with this page (E265). Nothing in the guide
has changed yet.

Predictions: none (no Pangram check this turn). Delegations (model, piece, check, outcome): 10 Sonnet readers on the
fixed reread brief (all reported; each item checked by me against the whole guide and his referent rule: 47 offered, 32
left, 1 folded); 2 Opus readers comparing the guide with the inner child guide (both reported, one after running out of
output once; each quote checked word for word in both guides and each item against the InnerSignal protocol 0.2.1: 42
offered, 1 left, 1 widened). InnerSignal protocol loaded in the main thread: 0.2.1, 1da3ddf0...7a27.

## 2026-10-25, after Joel's message of 01:01 UTC ("finish the guide first": the four-part clarity check)

**The guide's clarity check, all four parts**, is questions 15 to 18 (`OWNER-QUESTIONS.md`), each with its page in
`fix-20261025/`: what a reader has to reread (`clarity/CLARITY.md`: 64 passages, 7 hard, 57 to reread, 15 small snags),
the reader's edit (`edit/READERS-EDIT.md`: 33, my pick A on 30), the caveats (`caveats/CAVEATS.md`: 68, cut 32 and keep
36) and the repeats (`repeats/REPEATS.md`: 64, cut 18 and keep 46). My check of every item is `fix-20261025/my_checks.py`,
done with the InnerSignal protocol loaded in the main thread (0.2.1, 1da3ddf0...). Found on the way: Pattern 4's
references to two examples the 3 a version had left out (E263). Nothing in the guide has changed yet.

Predictions: none (no Pangram check this turn). Delegations (model, piece, check, outcome): 37 Sonnet readers, one per
brief (6 reread, 11 reader's edit, 8 caveats, 10 repeats, then 2 for part 1's halves); my reading of all 295 items against
the whole guide, each found word for word; 36 reported, part 1's first reader ran out of output (E262).

## 2026-10-24, after Joel's message of 23:40 UTC (Nibbāna: N7 A in, the helper rebuilt)

**N7 A** ("n7a") as batch n9: "The later Buddhist text *Milindapañha* ...", one word, link and italics kept
(`articles/nibbana/humanize/fix-20261024/n9/`). **The helper rebuilt** with it (`exports/COPY-TO-SUBSTACK.html`
5444c935...; checks pass) and sent; no Nibbāna questions open.

Predictions: none this turn in this lane. Delegations: none.

## 2026-10-24, after Joel's message of 19:52 UTC (Nibbāna: recheck 8 read, his GPT edit saved, the clipboard helper; N7)

**Nibbāna's eighth recheck** ([his link](https://www.pangram.com/feed/355a29d0-0ea5-4070-a7d2-731806c645f0)): Human
Written, 0 of 110 windows AI. Forecast 55 of 55 (Brier 0.003); NB-whole#30 a miss (AI called at 0.24; pessimism). His
note: "altho i don't think it was worth doing that recheck since now we are making lots of edits to it" (E256).

**His GPT edit saved** as batch n8 (`articles/nibbana/humanize/fix-20261024/n8/`): 40 paragraphs, his 13 N6 cuts, GPT's
edits in 23 and its ten style edits, put into his editor HTML word by word; my read of each change
(`fix-20261024/gpt/REVIEW.md`) finds each keeps his meaning. N6 answered: 13 cut, 10 kept, four against my pick (5 kept;
13, 14 and 23 cut), now caveat examples (E257). The batch class's tag order is fixed (four `<a><em>` had come out
`<em><a>`) and the working copy rebuilt.

**The clipboard helper for his post** (`articles/nibbana/exports/COPY-TO-SUBSTACK.html`, df57b0be...): the canonical
generator against recheck 8's helper, four parts and three video steps, verify and the interaction test pass, the 40 n8
paragraphs in it; receipt `HELPER-RECEIPT-20261024.json`; sent in chat. N7 (the Milindapañha) asked; N5 he decides as he
pastes.

Predictions: NB-whole#30 scored (above). Delegations: none.

## 2026-10-23, after Joel's message of 23:28 UTC (Nibbāna's seventh recheck read; batch n7; the eighth recheck pasted)

**Nibbāna's seventh recheck** ([his link](https://www.pangram.com/feed/31fd6bda-482c-4991-a5ef-d586de30aecb)): Human
Written, 0.39% AI, 2 of 114 windows AI, the first two sentences of an unchanged paragraph of his that read light green
before; all four of batch n6's splices read Human. Emulate's round 5 went in for those two sentences only (batch n7,
reviewed and triaged: E255, Emulate's "I think" is a hedge), and the eighth recheck is pasted and verified. The rendered
check is a tool now (`tools/humanization/substack_rendered_check.js`).

Predictions: NB-whole#29 right (recheck 7, Mixed); the part forecast 64 of 65. NB-whole#30 (recheck 8, AI at 0.24) waits
on his result.
Delegations (model, piece, check, outcome): Sonnet, the meaning check of batch n7's splice (`n7/REVIEW.md`): CHANGED,
triaged into two fixes.

## 2026-10-23, after Joel's message of 22:29 UTC (Nibbāna's sixth recheck read; batch n6; the caveat and repeats reads added)

**Nibbāna's sixth recheck** ([his link](https://www.pangram.com/feed/6d05010a-d5c8-4554-bbb7-ff2736b3974e)): Mostly Human
Written, 1.1% AI, 6 windows, all Low, beside his N4 moves; batch n5's four sentences read Human. Emulate's round 4 went in
sentence by sentence (batch n6, reviewed and triaged), and the seventh recheck is pasted and verified. His question about
too much safety language made it a standard check (part 3 of the clarity read, with a tool and a test), and his wish to
deduplicate made a fourth part (repeats across the whole article). Nibbāna's caveat list is question N6; the guide's
clarity check, all four parts, is next for this guide. Lessons E252 to E254.

Predictions: NB-whole#28 right (recheck 6, Mixed); the part forecast 87 of 92. NB-whole#29 (recheck 7) waits on his result.
Delegations (model, piece, check, outcome): Sonnet ×6, Nibbāna's caveat readers (a sixth each), every line checked by me
against the whole article: 25 lines, 23 offered (11 cut, 12 keep), 2 kept; Sonnet, the meaning check of batch n6's four
splices (`n6/REVIEW.md`): 2 CHANGED, triaged (another sample for one, the reader's fixes for the other). The community
lane's readers are in its own status.

## 2026-10-23, after Joel's message of 20:35 UTC (part B and Nibbāna's fifth recheck read; his N4 answers in; batch n5; Nibbāna's sixth recheck pasted)

**Part B's recheck** ([his link](https://www.pangram.com/feed/d63c3c9f-b71f-4435-9b20-59027a31225b)): Mostly Human
Written, 1.3% AI, one window red, the audit he kept; the forecast called 51 of 51. The whole guide now reads Human outside
that audit, so its clarity read (both halves) is next. **Nibbāna's fifth recheck** ([his link](https://www.pangram.com/feed/54a79d39-a6ba-4e9e-80b4-7e1178527768)):
Mostly Human Written, 0.7% AI, 4 windows (his DN 3 stretch and the room's "They were disjoint ..."); batch n4's five
stretches read Human. His 18 answers to the reader's edit are in (17 changes, one left out), Emulate's round 3 spliced
sentence by sentence (batch n5, reviewed and triaged), and the sixth recheck is pasted and verified with a part forecast.
Lessons E250 (a past answer covers only what its reason covers) and E251 (pictures beside a reader's move).

## 2026-10-23, after Joel's message of 18:13 UTC (recheck A4 and Nibbāna's fourth recheck read; batches 477 and n4; the reader's edit added to the clarity read)

**Recheck A4** ([his link](https://www.pangram.com/feed/fd67dd6e-7193-4bdf-9ed8-3ed235d62d94)): Human Written, 0% AI, all
108 windows Human; the part forecast called 52 of 52 right, and my whole-part call (AI) was the miss. **Nibbāna's fourth
recheck** ([his link](https://www.pangram.com/feed/933f5abe-7627-4367-8dd2-8601a9125249)): Mostly Human Written, 1.1% AI,
5 of 132 windows: the unification definition (High, alone after his 14 moved the window's edge), Soh's sentence with my
gloss, "It sounds abstract, ...", and the preservation sentences. Emulate ran on each red paragraph (rounds br to bw), and
batch n4 spliced in only the red sentences, the reader's three meaning fixes in; Soh's sentence is back to his words and
the snag is fixed in the definition ("all of the senses"). For the guide, batch 477: Emulate's br for recheck B's red
inner child line. Nibbāna's fifth recheck and the guide's part B recheck are pasted and verified, with part forecasts.
His question ("how does "tellingly" ... put "me " in the explanation?") corrected E241 (E247); GPT's reader's edit is part 2
of docs/CLARITY-READ.md, with a tool (`clarity_read.py --kind edit`) and tests (E248), and it ran on Nibbāna (question N4);
part_forecast.py adds neighbours itself (E249).

## 2026-10-23, after Joel's message of 16:55 UTC (recheck A3 and Nibbāna's third recheck read; batches 475, 476 and n3; the clarity read made standard)

**Recheck A3** ([his link](https://www.pangram.com/feed/43889be6-155e-4584-b232-90c4ad70e629)): Mostly Human Written,
1.1% AI, 7 windows, all in Come all the way back; batch 474's other two stretches read Human. Batch 475 put Emulate's
versions of the whole return stretch in (script to Note, from samples bo and bp, the reader's two fixes in), and batch 476
put Emulate's misspellings and British spellings back to the published guide's spelling in 25 paragraphs. Recheck A4 is
pasted with a part forecast. **Nibbāna's third recheck** ([his link](https://www.pangram.com/feed/f2b77491-4933-42cf-a431-8b063208fa78)):
Human Written, 0.34% AI, 2 windows on the photon paragraph, which he rewrote; his rewrite and all his answers to the
clarity list are in (batch n3, 36 edits, with the snags and saṃsāra defined at its first mention), and its fourth recheck
is pasted. The whole-article clarity read is now standard for every article (docs/CLARITY-READ.md, its tool and tests).
Lessons E241 to E246.

## 2026-10-23, after Joel's message of 14:14 UTC (recheck A read; batch 474; part forecasts; Nibbāna's clarity read)

**Recheck A** ([his link](https://www.pangram.com/feed/3f9225c6-4ec8-452e-bdff-d44040b1acc0)): Mostly Human Written, 1.4%
AI, 7 of 108 windows, down from 10: his forces paragraph and the return paragraph Human; the shortcut paragraph red again in
place from the driving caution (Low and Medium), the return's check (Low), and Nothing happens' lines (new). Batch 474 put
Emulate's versions of all three in (each Human alone, the reader's three fixes in), and recheck A is pasted again with a
part forecast. Nibbāna's second recheck read "Human Written" with one red paragraph, which Joel rewrote; his fix is in, its
third recheck is pasted, and a cold read found 29 passages that pass but are hard to understand (question N3). Lessons E238
to E240.

## 2026-10-23, after Joel's message of 12:30 UTC (recheck B read; question 14 through his Emulate re-run trick; recheck A and Nibbāna's second recheck pasted)

**Recheck B** ([his link](https://www.pangram.com/feed/1db9825e-5fed-4528-aca5-9d4272b54f83)): Mostly Human Written, 1.4% AI,
2 of 36 windows: the audit's questions (they stay, answer 2c) and "You don't have to fix this. I'm here now." (Low), next
for B. **Question 14's seam passed through his re-run trick** on the first check after six versions of mine failed (batch
473: [the shortcut paragraph alone](https://www.pangram.com/history/8c07a601-45c9-4d33-9555-6b51302e81d3),
[the pair](https://www.pangram.com/history/ce2c2f4e-e14f-45a6-9ed8-27c25aaf1397), and
[with the reader's fix](https://www.pangram.com/history/1129f619-ef4e-4276-8889-f8b3496f19b7), all Human, 0% AI). His own
forces paragraph is in. Recheck A is pasted and its rendered text matches what I predicted from; it waits on his Brave.
On Nibbāna: N1 a and his four N2 rewrites are in, the rebirth sentence comes from Emulate
([Human, High](https://www.pangram.com/history/d09ef29a-c0be-4cd6-a42f-99383aa60007)), and its second recheck waits too.
Pull request 224's conflict is resolved. Lessons E234 to E237 (a Low window alone is a warning; the re-run trick; what his
N2 rewrites changed; Emulate first was the rule, and batch n1 skipped it).

## 2026-10-23, 03:05 UTC (the guide waits on Joel; his Nibbāna article's first 4.1 pass)

Nothing new on the guide: recheck B's link and question 14 are with Joel. The lane's queue moved on to his Nibbāna
article, with its own questions page ([OWNER-QUESTIONS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/OWNER-QUESTIONS.md)) and ledger: batch n1 put four
fixes in the working copy (each Human on its own through the API and OK by the reader), the science sentence went to him
as question N1 and four stretches as N2 (AI in three tries each), and the whole-article recheck is pasted into a new
temporary draft and verified, waiting on his Brave. Lessons E230 to E233; the API check pages of both articles now label
every line of a window (E230: I had read the driving caution's unlabelled line as Human).

## 2026-10-23, after Joel's message of 01:10 UTC (recheck A read; answer 13, his own Appendix C; batch 472g through the API; recheck B pasted)

**Recheck A's result** ([his link](https://www.pangram.com/feed/47610d4b-fb69-4966-896f-317b029fc1af)): Mostly Human
Written, 1.4% AI, 10 of 100 windows; the windows read from the page as one compact line, the text rebuilt from the payload
(`fix-20261022/recheck/RESULT-A.json`, SHA-256 fd2e3ed6..., equal to the page's). The induction section from bf read Human
in place (28 windows, 13 of them light green on short lines) but for its last paragraph. Red: De-hypnosis's run of
questions (part 7 of the result page, Low and one Medium); the seam from the induction's last paragraph into the return's
first (part 9, High); the return's "Get up only when you feel steady. Make sure you're truly oriented and alert. Don't
just assume it ..." (part 9, Low). In the ledger, HG-whole#33 (AI at 0.10) is right: I first typed its verdict as Human,
corrected to Mixed, and the same check of every result line found part B of 2026-10-21 (HG-rest-B#20) typed the same way,
now Mixed and right (its earlier "verdict threshold misread" explanation was the misread); `pangram_ledger.py result` now
refuses a verdict its headline contradicts (E225). Batches 470g and 471g: 17 of 17 forecasts right in part A, 7 to score
in part B (`fix-20261022/recheck/score_recheck.py`, `b470/batch/SCORE.md`, `b471/batch/SCORE.md`).

**Joel's answer 13** (`fix-20261023/joel-20261023-0110-message.txt`): his own five paragraphs for Appendix C's prose, the
opening he checked ("13 human high conf") and the signs, what to do, and the good and bad guide; installed as he typed them
with "accomodate" fixed (`fix-20261023/make_joel_0110.py`, edit HG32-joel-0110). His "learn some lessons" is E223 (what his
opening did that six versions of mine didn't, against sample S5), and his "it seems like you duplicated this in your
check" is E224 (samples that share text go in separate API checks).

**Batch 472g** (`fix-20261023/b472/`): the three red stretches, each checked through the API on a pair (E218; the laptop's
lane-folder `pangram_api.py` is the old 4.0-only one, so the repository's was fetched at 92f87f0d into the check's folder,
SHA-256 4a100ecd...). Fourteen checks ([the page](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/fix-20261023/b472/API-CHECKS.md)), each predicted first (ledger #34 to #47):
- The bases: the seam read AI, High, throughout, as in place; the two Low stretches read Human, so their pairs can show
  only that a fix is no worse (E226).
- s1: b (his bracketed list for the ten questions) read Human, its sentence's window High; c, which joined "It's all
  around you." on to clear the linter's B3, read worse (9.6% AI), so b goes in (E211, E228).
- s3: c (the commands joined, the count's caveat as a gloss in brackets, the installed "truly") read Human in one High
  window, and goes in.
- s2, the seam: AI, High, in six versions (b: the return paragraph reworded; c: the induction paragraph reworded; d: both;
  e: both in his register, the induction paragraph alone too; f: e without the tidy closers, alone too). Both paragraphs
  are the published text's, with no earlier draft of his, so it is question 14 (E227).
A reader checked s1b and s3b against the published guide in place (`REVIEW.md`: both OK); `lint-compare.json`;
`GATE.json`; installed by `install_b472.py` (edits b472-s1b and b472-s3c).

**Recheck B** (`fix-20261023/recheck/`, built by its `make_recheck.py`): the appendices with his Appendix C, predicted first
(HG-rest-B#48, Human at 0.55), pasted into draft B after its title was checked and its body cleared with real keystrokes
(the helper's paste: 10,852 editor words, 25 more than the payload's count, as part A had 34 more), and its rendered
paragraphs, the known button line left out, hash to `TEXT-B.txt` (76745975...): [TEMP recheck B (hypnosis guide appendices)](https://ibogaqueen.substack.com/p/8051254d-8771-45cb-baa3-ff3fd295587a?postPreview=paid&updated=2026-10-23T02%3A10%3A00.000Z&audience=only_paid&free_preview=false&freemail=).
It waits on Joel's Brave. Part A waits for question 14.

## 2026-10-22, after Joel's message of 21:41 UTC (the pull request; answer 12, batch 471g; both screenings read; the induction section from bf; recheck A; Nibbāna's HTML)

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
bf's paragraph didn't have). Round 2 (`r2/VERIFY-r2.md`: 5 of 5 OK; `r2/march/`). The stance check (`STANCE-HG17.md`: three conflicts, each fixed
in round 4, `r4/VERIFY-r4.md`: the already-open practice made a step toward deepening, the preview made optional, an
early stop without the return; and two contradictions inside the published text: "when intoxicated", which Joel's
11 b settles, and "You can simply open your eyes and finish" against "Use Come all the way back, even when you ended
early", where round 4 follows the return and the questions page asks him). The gate (`batch/GATE.json`). Installed by
`install_bf.py`; its first run joined the section's last paragraph to the next h1 ("# Come all the way back" read as
part of the paragraph), caught by comparing the pasted recheck post with its rebuild line by line, and fixed.

**The second screening post** (`fix-20261022/screen2/`, the same draft, its body cleared and pasted with the lane's helper;
words SHA-256 equal; the rendered paragraphs' textContent hashes to `TEXT-S2.txt`): Appendix B's stretch as installed
(B0), Appendix C as installed (C0), and two new openings with bg's middle and C0's end (C1, C2). Predictions first (ledger
HG31-nlp-tail#28 to HG32-c2#31, all AI, 0.30 to 0.40). [Joel's result](https://www.pangram.com/feed/5af06c6a-8f56-4bd7-9c86-5e9813f7a97e)
(23:01 UTC; AI Detected, 59.5% AI; checked text SHA-256 equal to `TEXT-S2.txt`; `RESULT-S2.json`, `SCREEN2-RESULT.json`
by `read_screen2.py`): B0 Human (a miss, explained: the red window began in it, but its color was Appendix C's); C0 AI
throughout, high, its first window marked "humanized"; C1 Human from the list of tricks to "A bad guide can't.", AI in its
opening and in the bad guide's last sentence; C2 AI nearly throughout. The opening's sixth try failed, so it is question
13 for Joel (his own words), with C1 as the default meanwhile. Its meaning check, read while the post waited
(`VERIFY-C.md`): nothing lost in C1 or C2.

**Recheck A** (`fix-20261022/recheck/`: `make_recheck.py`, part A the whole guide, the check reading its first 99,999
characters, into the appendices): predicted (HG-whole#33, AI at 0.10: the return's three short red stretches are
unchanged), pasted into draft A (the paste's words were 34 more than the payload's count, the same 34 at both pastes; the
rendered post's lines hash to the rebuild, with the page's two button lines read as the rebuild reads them;
`RECHECK-POST-A.json`). The first paste showed the induction section's install had glued its last paragraph to the next
h1; part A was rebuilt after the fix and round 4, the first prediction voided (HG-whole#32). It waits on Joel's Brave.
Part B waits on question 13.

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
