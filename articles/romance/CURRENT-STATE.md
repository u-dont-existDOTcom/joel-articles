# Romance current state

Updated: 2026-11-07

## Goal

Joel, 2026-11-07 13:13 UTC: "start working on fixing the romance article, pangram 4.1 found some ai spans". The live post
reads Human in Pangram 4.1, with no AI window and no Low, its argument, memories and locks kept; then his post is updated,
with his OK and no email.

## Authority / baseline

- The live post as his extension read it on 2026-11-05: [Romance Advice I Wish My Parents Taught Me](https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents)
  ("Updated Aug 27, 2026"), [Mostly Human Written](https://www.pangram.com/feed/9e40aa8f-317c-4490-893d-9e99c839de88),
  4.2% AI, document confidence Medium: 741 words in AI windows over 21 spots (170 High, 169 Medium, 402 Low) and 911 words
  Human Low (`humanize/fix-20261107/live-check/`).
- `master.md` (2026-08-24) is not the live post: 125 of the live post's 355 lines differ (his update of 27 August among
  them). The live text was not copied into the repository whole; each paragraph being fixed is in its check text.
- `OWNER-LOCKS.json` still applies (protected functions). Its Two Pillars lock text differs from the live post's version
  of that paragraph ("without much outside support"), so the live post is his later word there; nothing is changed in it.

## Completed

- 2026-11-07: the live post's result recorded; the romance lane added to `tools/humanization/pangram_lanes.json` with its
  ledger `humanize/pangram-ledger.jsonl`.
- 2026-11-07: first tries at 13 of the 21 spots (`humanize/fix-20261107/r01/`, `r02/`), each paragraph checked in the web
  app with its making-sense receipt. Human in its own check: S1 the casual-sex turn (#1), S3 the support paragraph's
  summary cut (#3), S4 the provider question (#4), S5 Bee's shoes (#5), S9 the bed line (#10, its line Low), S12 the
  patient paragraphs (#13), S13 teacher and student (#14).
- 2026-11-07 (13:39 UTC pickup): tell panels on S2, S7, S10, S11, S17 and S21 (`humanize/fix-20261107/r03/panel-s2/`,
  `r04/panel-*`, `r05/panel-*`); second and later tries at S2, S6 to S11, and first tries at S14 to S21 (`r03/`, `r04/`,
  `r05/`). Human in their own checks, no Low: S6 bundling (#30), S8 idealization (#18), S11 her as Mom (#37), S14
  polarity inside the safety (#21), S15 proving I'm the man (#31), S16 the fantasy lines (#23), S18 the backup system
  (#25), S19 the confidants' side of the story (#32), S20 the agreement questions (#27).
- 2026-11-07 (14:27 UTC pickup): four sections checked whole with the best tries in them (`humanize/fix-20261107/r06/`):
  S10 alone time read Human (High) in its section (#44), so it is done. The post's last 2,871 words, which his extension
  never read, checked as they stand (#47): Mostly Human, 4.8% AI, with a new spot, S22, and 8 Human Low windows. The live
  post's 54 Human Low windows saved (`live-check/LOW-WINDOWS.json`): 19 already rechecked by a fix, 35 (673 words) open.
- 2026-11-07 (14:49 UTC pickup): S22's first try inside "After leaving" (#50, `humanize/fix-20261107/r08/`): one
  sentence fixed, the rest still AI. The marking page for S2 and S17 published
  ([the page](https://claude.ai/artifact/CMRNDtBm4bBRB3741geGoY), its cards in `review/teach-20261107/REVIEW-T1.md`).
  The first Low-window section, "Holding up a leaky dam" (#51, `r09/`): its short sentences joined read Human Medium, but
  the want list joined to its reason read AI Medium.
- 2026-11-07 (15:09 UTC pickup, `humanize/fix-20261107/r10/` to `r12/`): S22's paragraphs checked by themselves
  (#54 to #56), then its section a second time (#62): Human, no AI window left (41% AI in #50), two Human Low windows.
  "Holding up a leaky dam" (#57, #63): Human, one Low window left, on the want list. Three more sections with open
  Low windows read Human with no Low: "My flaws" (#61), "Peeking thru the window" (#67) and "Things get tricky fast"
  (#68). "The window of clarity" (#60, 15% AI) and "Situationships" (#59, 31% AI) narrowed to their paragraphs:
  paragraph 33 (#64) and the oxytocin paragraph (#66) read Human High by themselves, paragraph 34 Human Low (#65).
- 2026-11-07 (15:09 UTC pickup, `r13/`): after one fix each (his answer 28a), S22's section (#69) and "Holding up a
  leaky dam" (#70) read Human with no Low window, and "The window of clarity" read Human with no Low on its second try
  (#71). "Anti-PTSD Can Be Just As Dangerous As PTSD" read Human with no Low on its first (#73). Paragraph 34 of
  "Situationships" still reads Low on his three claims (#72); "Slow & steady" read 34% AI on its five-part list (#74);
  "Disconnect to connect" read Human with four Low windows by itself (#75).
- 2026-11-07 (15:57 UTC pickup, `r14/`, `r15/`): "Disconnect to connect" read Human with no Low on its second try,
  after its paragraphs read High by themselves (#77 to #80, #88). "Muses & Directors" (#81), "The Queen of Orgasms"
  (#82) and "Labels Are Descriptive, Not Prescriptive" (#84) read Human with no Low on their first try. The tell panel
  ran on "Situationships" paragraph 34 (`r14/panel-sit34/`); with its agreed tells fixed the paragraph still read Low
  (#85), and the section read 15% AI on its last try (#86). "Slow & steady" (#87) and "It always goes deeper" (#91,
  with S4 and S5 in) read Human with Low windows; "Jealousy on trial" read 16% AI (#83), then its two pairs read High
  by themselves (#89, #90); "Beware idealization in either direction" (#92, with S8 in) read 9.6% AI.
- 2026-11-07 (16:24 UTC pickup, `r16/`, every try linted first): "Slow & steady" (#96, after one more fix), "It
  always goes deeper" (#97, one High window, with S4 and S5 in) and "Fantasy" (#99, with S16 in) read Human with no
  Low. "Situationships" paragraph 34 read Human with no Low by itself (#95: his fun line left a little unbalanced,
  "without (most of) the responsibility", bad-trips-2026-11-07g). "Jealousy on trial" read 28% AI on its last try
  (#94), "Romance Shouldn't Be Adjudicated" 37% AI on its first (#98), and 147 with 148 37% AI (#93).
- 2026-11-07 (16:41 UTC pickup, `r17/`, every try linted first): "Situationships" read Human with no Low after its
  fix (#100, his answer 28a: paragraph 34 as #95 read, and 36's closing line said once, in its opener). "Some babies
  grow up faster" (#101, with S11 and S12 in), "Different levels in different domains can be complementary" (#102,
  with S13 in) and "Gaslighting in the dark" (#105) read one Human High window each, and "Why all of this sounds
  artificial" (#104) read Human with no Low. "What are you actually choosing together?" (#103, with S20 in) read Human
  with three Low windows, all in S20's questions, which had read High as a pair by themselves (#27).

### Before 2026-11-07 (the registered master, as recorded then)

#### Goal

Maintain the exact owner-authorized Romance working master as registered GitHub authority, preserving its argument, owner-final language, memories, native-object placement, source provenance, architecture, and detector evidence while keeping citation, publication, and whole-article owner-final status explicit and separate.

#### Authority / baseline

- Article id: `romance`
- Article status: **working**
- Canonical master on `main`: `articles/romance/master.md`
- Master SHA-256: `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`
- Master word count (Markdown whitespace): **20,364**
- Candidate id: `romance-r23r2-owner-final-20260824`
- Promotion PR: #46, merged to `main` as merge commit `1abe38d2d3cd85e35ce1fbeb46217cb5cf89ff59`
- Source candidate: exact r23 at `u-dont-existDOTcom/pangram-humanization-lab@f4f2d6404e7362441c9ac0969dfc79313bea6ba1`, branch `evidence/romance-r23-gui-20260824-a`
- Materialization: `work/romance-r22-reconciliation-20260823/materialized-r23r2-owner-final/`
- Preservation receipt: `work/romance-r22-reconciliation-20260823/R23R2-PRESERVATION-RECEIPT-20260824.md`

Joel's 2026-08-24 direct correction makes the exact r23r2 Two Pillars local realization owner-final, including its double space after `rare.` and capitalized `If`. Joel reports the exact local realization tested Human / low confidence and explicitly accepts that result as `good enough`. This is sufficient bounded detector acceptance for working-master promotion; it does not mark the whole article owner-final or published.

#### Completed

- Preserved the earlier registered master, exact r22 known-green rollback, exact r23 GUI candidate, rejected r23r1 proposal, and unused R23R1-R03 fallback as durable provenance.
- Reproduced exact r23 source identities before materialization:
  - master `322953b5d6f6ad49f7a3b41e5c6795b36404508f7768669cdcc72223f2f21a0d`, 20,364 words;
  - Part 1 `620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b`, 10,296 words;
  - Part 2 `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`, 9,917 words.
- Materialized r23r2 with one exact operation inside Two Pillars and no other r23 change.
- Locked the exact owner-final span at SHA-256 `cd8de93fda39fcdf13c4b1f6ba2f9250c11c40f8c8298f281055e37bafed6291`.
- Proved forward traceability, reverse traceability, and zero unexplained substantive deltas.
- Preserved heading order, all 11 native objects, all 22 Markdown links, protected anchors, section topology, architecture dependencies, and terminal stopping point.
- Deterministic rematerialization PASS.
- Machine preservation receipt PASS.
- Content repository validator PASS.
- Architecture-map validator PASS.
- `python -m unittest discover -s tests`: 99 tests PASS.
- Repository audit: 0 errors; 4 pre-existing governance warnings.
- `git diff --check` PASS.
- Hosted exact-byte/hash readback PASS.
- PR #46 merged successfully into `main` at `1abe38d2d3cd85e35ce1fbeb46217cb5cf89ff59`.

#### Current checkpoint

2026-11-07, the 16:41 UTC pickup. 17 of the 22 spots read Human with no Low window (S1, S3, S4, S5, S6, S8, S10, S11, S12,
S13, S14, S15, S16, S18, S19, S20, and S22 in its section, #69). S7 and S9 have a Low line, S21 reads AI only on its closing
sentence (#46), and S2 and S17 wait on the marking page for Joel's versions.

Eighteen sections with open Low windows in the live post now read Human with no Low window in their own check: "My
flaws" (#61), "Peeking thru the window" (#67), "Things get tricky fast" (#68), "Holding up a leaky dam" (#70), "The
window of clarity" (#71), "Anti-PTSD Can Be Just As Dangerous As PTSD" (#73), "Muses & Directors" (#81), "The Queen of
Orgasms" (#82), "Labels Are Descriptive, Not Prescriptive" (#84), "Disconnect to connect" (#88), "Slow & steady" (#96),
"It always goes deeper" (#97), "Fantasy" (#99), "Situationships" (#100, after its fix), "Some babies grow up faster"
(#101), "Different levels in different domains can be complementary" (#102), "Why all of this sounds artificial" (#104)
and "Gaslighting in the dark" (#105); so does "After leaving", with S22 in it (#69). "What are you actually choosing
together?" reads Human with three Low windows, on S20's questions (#103); it has one try left.

Still AI: "Jealousy on trial" (367 to 369, #94), "Romance Shouldn't Be Adjudicated" (285 to 287, #98) and "Beware
idealization" (148, #93). All three are his general claims about men, women, monogamy and idealization, said evenly.
Each reads High by itself and AI in its section, his live wording included, and my joins don't move them. That is the
pattern of S2's card on the marking page, so his answer there is the likeliest way to learn how he'd say these.

What these checks showed: a section checked by itself reads harsher than the whole post did, and his general claims
read AI there whatever the joins. His short sentences joined to what they belong with, a paragraph's point said first,
a claim left a little unbalanced ("without (most of) the responsibility"), and a repeat cut read High. A run of short
questions reads one window per question inside its section, even where the pair read High by itself.

## Remaining

1. S2 and S17: Joel's versions on the marking page; then carry what he did to the lines each card names, and to the
   stretches that share S2's pattern ("Jealousy on trial" 367 to 369, "Romance Shouldn't Be Adjudicated" 285 to 287,
   "Beware idealization" 148).
2. "What are you actually choosing together?": its second try, with S20's three Low questions fixed (the short opener
   joined to the first question with a colon, the either/or question left a little unbalanced, the rethink question
   joined to the split-up one).
3. The rest of the post's last part: "What I gained from loss" (443's short line, Low in #47); S7's and S9's Low lines;
   S21's section. "Two Pillars Don't Hold The Roof Up" keeps its one Low window (332), on the paragraph the owner lock
   keeps as the live post has it.
4. A whole-article check of the fixed version (a temporary draft for his extension, in two parts, since his extension
   reads only the first 100,000 characters), then his post updated with his OK, no email.

## Blockers / unresolved

- Publication remains blocked on the owner decisions recorded in `review/FINAL-CORRECTIONS-20260824.md`, including factual and citation corrections that require owner-approved prose.
- Copyright and license posture remain separate owner decisions.

#### Evidence / artifacts

- Canonical working master: `articles/romance/master.md`
- Owner locks / protected functions: `articles/romance/OWNER-LOCKS.json`
- Source/evidence index: `articles/romance/SOURCE-EVIDENCE.json`
- Architecture map: `articles/romance/ARCHITECTURE.md`
- Citation state: `articles/romance/CITATIONS.json`
- Detector evidence: `articles/romance/DETECTOR-EVIDENCE.json`
- Editorial state: `articles/romance/EDITORIAL-STATUS.json`
- r23r2 delta: `work/romance-r22-reconciliation-20260823/R23R2-OWNER-FINAL-DELTA.json`
- r23r2 machine-readable preservation receipt: `work/romance-r22-reconciliation-20260823/R23R2-PRESERVATION-RECEIPT.json`
- r23r2 preservation receipt: `work/romance-r22-reconciliation-20260823/R23R2-PRESERVATION-RECEIPT-20260824.md`
- r23r2 materialized master/halves/receipt: `work/romance-r22-reconciliation-20260823/materialized-r23r2-owner-final/`

#### Next safe action

Use exact r23r2 on `main` as the sole current Romance working authority. The next substantive publication-preparation work is a fresh whole-article editorial pass and citation review when requested. Do not equate the r23r2 merge with publication, licensing, completed citation review, whole-article owner-final acceptance, or a whole-article detector pass.

## Current checkpoint

2026-11-07, the 16:24 UTC pickup. 17 of the 22 spots read Human with no Low window (S1, S3, S4, S5, S6, S8, S10, S11, S12,
S13, S14, S15, S16, S18, S19, S20, and S22 in its section, #69). S7 and S9 have a Low line, S21 reads AI only on its closing
sentence (#46), and S2 and S17 wait on the marking page for Joel's versions.

Thirteen sections with open Low windows in the live post now read Human with no Low window in their own check: "My
flaws" (#61), "Peeking thru the window" (#67), "Things get tricky fast" (#68), "Holding up a leaky dam" (#70), "The
window of clarity" (#71), "Anti-PTSD Can Be Just As Dangerous As PTSD" (#73), "Muses & Directors" (#81), "The Queen of
Orgasms" (#82), "Labels Are Descriptive, Not Prescriptive" (#84), "Disconnect to connect" (#88), "Slow & steady" (#96),
"It always goes deeper" (#97) and "Fantasy" (#99); so does "After leaving", with S22 in it (#69). "Situationships"
paragraph 34 reads Human with no Low by itself (#95); its section has had its two tries (#59, #86).

Still AI: "Jealousy on trial" (367 to 369, #94), "Romance Shouldn't Be Adjudicated" (285 to 287, #98) and "Beware
idealization" (148, #93). All three are his general claims about men, women, monogamy and idealization, said evenly.
Each reads High by itself and AI in its section, his live wording included, and my joins don't move them. That is the
pattern of S2's card on the marking page, so his answer there is the likeliest way to learn how he'd say these.

What these checks showed: a section checked by itself reads harsher than the whole post did, and his general claims
read AI there whatever the joins. His short sentences joined to what they belong with, a paragraph's point said first,
and a claim left a little unbalanced ("without (most of) the responsibility") read High.

## Remaining

1. S2 and S17: Joel's versions on the marking page; then carry what he did to the lines each card names, and to the
   stretches that share S2's pattern ("Jealousy on trial" 367 to 369, "Romance Shouldn't Be Adjudicated" 285 to 287,
   "Beware idealization" 148).
2. "Situationships": one more check of the section after the fix (28a), with paragraph 34 as it read in #95.
3. The sections with a fixed spot and open Low windows ("Some babies grow up faster", "Different levels in different
   domains", "De-ontologizing Twin Flames"), each with the spot's best try in place; the 8 Low windows of the post's last
   part (#47); S7's and S9's Low lines; S21's section.
4. A whole-article check of the fixed version (a temporary draft for his extension, in two parts, since his extension
   reads only the first 100,000 characters), then his post updated with his OK, no email.

## Blockers / unresolved

- None blocking. Kim Anami's linked page could not be read from here (the fetch waited for an approval nobody
  answered), so her claims are kept as the live post words them.

## Evidence / artifacts

- `humanize/fix-20261107/live-check/META.json`, `AI-WINDOWS.json`, `LOW-WINDOWS.json`; `humanize/fix-20261107/r01/` to
  `r17/` (check texts, receipts, predictions, results, tell panels); `review/teach-20261107/` (the marking page for S2 and
  S17: `build_t1.py`, `REVIEW-T1.md`, `ARTIFACT.md`); `humanize/pangram-ledger.jsonl`; `humanize/SCORECARD.md`.

## Next safe action

Read Joel's answers on the marking page when he gives them; meanwhile Remaining 2 and 3.
