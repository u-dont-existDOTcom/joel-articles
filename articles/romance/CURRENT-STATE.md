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

Exact r23r2 identities:

- master: SHA-256 `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`; **20,364** Markdown whitespace words;
- Part 1: SHA-256 `620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b`; **10,296** words; byte-identical to r23 Part 1;
- Part 2: SHA-256 `fbbcf64af313488b2ad8bb8969422f5bc85895eca908e41e9f796b2c0724e4eb`; **9,917** words;
- Two Pillars natural boundary: SHA-256 `1bd239b9b56926b2a2dabc5a2f106ca58f50bcccd993b950e924fc481c27736e`; **734** words;
- exact owner-final Two Pillars span: SHA-256 `cd8de93fda39fcdf13c4b1f6ba2f9250c11c40f8c8298f281055e37bafed6291`.

Detector evidence:

- current Part 1 retains exact Pangram 4.0 Human `1.0` evidence because its bytes did not change from r23;
- superseded r23 Part 2 measured Human `0.9965084195`, AI `0.0034915956`, AI-assisted `0.0` and localized one transition residual;
- Joel reports the r23r1 ordering tested AI / low confidence;
- Joel reports the exact r23r2 local realization tested Human / low confidence and accepts it as `good enough`;
- no new Pangram call was run for r23r2, and no full Part-2 or whole-article score is claimed.

Article-wide state:

- preservation: **PASS**, unexplained substantive deltas `0`;
- architecture/dependencies: **PASS**;
- citation review: `pending`;
- whole-article editorial review: `pending`;
- article status: `working`, not `owner_final` or `published`;
- publication exports: none registered.

#### Remaining

- Keep citation review and a future fresh whole-article editorial pass explicit; do not infer either from the bounded r23r2 correction.
- Do not run another Pangram Part-2 call solely to increase detector confidence; Joel accepted the exact local result.
- Do not normalize, re-punctuate, or reflow the exact owner-final Two Pillars lock.
- Do not publish/export without a separate explicit owner action and registered publication provenance.
- Copyright/license posture remains a separate owner decision.

No competing Romance master remains unresolved. Exact r23r2 on `main` is the current registered working authority.

#### Blockers / unresolved

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

2026-11-07, the 13:39 UTC pickup of Joel's 13:13 UTC ask. 15 of the 21 spots read Human in their own checks with no
Low window: S1, S3, S4, S5, S6, S8, S11, S12, S13, S14, S15, S16, S18, S19, S20. Human with a Low window: S7, the
shut-down questions (#39), and S9, the bed line (#10; its next try #40 read worse). Still AI: S2 the monastic paragraph
(five tries; the last, #38, 27% AI, with only the perks and West sentences AI Low), S10 alone time (four tries, none
Human: my rebuilds read worse than his own words), S17 Kim Anami and S21 the extra promise (three tries each; in these
two-paragraph checks his own sentences read AI too, Human in the live post).

What worked: changing only the sentence in the window and keeping his words around it (S8, S11, S15, S16, S18, S19,
S20). What didn't: rebuilding a sentence along a tell panel's list (S10, S21), the same finding as the neuro lane's
lesson neuro-2026-11-07e.

His extension read only the first 99,999 characters of the live post (`live-check/META.json`): the post is 116,586, so
its last part, from "It’s not always possible in that moment to change a defensive posture" on, has never been checked.

## Remaining

1. S17 and S21: check each inside its whole section, as the live post has it, with the best try in it (the short checks
   read his own sentences AI).
2. S10, and S2 if its last try fails: on the marking page for Joel with my tested tries, as the paragraphs he could teach
   most from (gate bad-trips-2026-11-07c).
3. The Low windows: S7's shut-down questions, S9's bed line, then the live post's 911 words of Human Low.
4. The unchecked last part of the post: its own check.
5. A whole-article check of the fixed version (a temporary draft for his extension, in two parts if it is over 100,000
   characters), then his post updated with his OK, no email.

## Blockers / unresolved

- None blocking. Kim Anami's linked page could not be read from here (the fetch waited for an approval nobody
  answered), so her claims are kept as the live post words them.

## Evidence / artifacts

- `humanize/fix-20261107/live-check/META.json`, `AI-WINDOWS.json`; `humanize/fix-20261107/r01/` to `r05/` (check texts,
  receipts, predictions, results, tell panels); `humanize/pangram-ledger.jsonl`; `humanize/SCORECARD.md`.

## Next safe action

Check S17 and S21 inside their sections; put S10 (and S2 if needed) on the marking page; then the Low windows.
