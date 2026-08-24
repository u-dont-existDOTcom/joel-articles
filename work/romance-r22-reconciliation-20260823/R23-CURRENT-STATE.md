# Romance r23 current state

Updated: 2026-08-24

## Status

The five-feature / six-operation r23 candidate is **fully materialized, preservation-clean, and measured in its exact two composition-aware reader-visible halves through the authenticated local Playwright GUI**. Its single Part-2 residual is now localized from Joel's manual read of the already-paid Pangram report, and a smallest-justified r23r1 transition repair is frozen and preservation-clean but **not yet materialized or detector-certified**.

Registered `main:articles/romance/master.md` remains unchanged. PR #46's branch copy of `articles/romance/master.md` remains byte-identical to registered main; r23/r23r1 stay isolated as reconciliation candidates until the Part-2 detector gate is resolved or explicitly accepted.

## Known-green rollback baseline

Exact r22:
- master SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`; 20,282 words;
- exact tested Part 1 SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`; 10,239 words; Pangram 4.0 Human `1.0`, zero AI windows;
- exact retained Part 2 SHA-256 `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`; 9,892 words; Pangram 4.0 Human `1.0`.

These are two half measurements, not a measured whole-article score.

## r23 authorized delta

Exactly five editorial features / six frozen replacement operations:
- `R23-01` prospective libido-divergence planning;
- `R23-02A` Affection simmer / taking-for-granted / five-years-ago / anti-homework rewrite;
- `R23-02B` changed-sex-life curiosity / new-normal / feeling-wanted rewrite;
- `R23-03` student-report attribution + jade-egg preliminary-training relation;
- `R23-04` owner-final Two Pillars sentence: `But sometimes a friend who actually knows us both sees the pattern before either of us does.`;
- `R23-05` `I can hear a whole future in those two words—...`.

Exact old/new spans and hashes: `R23-FIVE-OWNER-EDITS-MANIFEST.json`.

Everything else is invariant relative to exact r22.

## Preservation / architecture proof

Four changed natural boundaries independently materialized from exact r22 + whitelist and cold-read PASS:
- Talk + Affection SHA-256 `a1c88e60e068101c268b8e0dc45558ec796fe6d8224de86c8b5ec64c5238e564`; 777 words;
- Spiritual practice SHA-256 `9722c938f9258316cef1efbe67768abee063f64923976711498bbaff57d106fb`; 290 words;
- Two Pillars SHA-256 `e89362da826bd77d747733512a935cf19c1ddf6d492175755931826968360113`; 734 words;
- Choosing Together through Attraction/exclusivity SHA-256 `a1bd65fc862a879170d6651f52f4d0da50150bf56de1f4f9e26437d30dd6cb8f`; 1,437 words.

Final full materialization reproduced all four fixtures exactly.

Preservation status:
- forward traceability PASS;
- reverse traceability PASS;
- unexplained substantive deltas **0**;
- headings unchanged;
- native objects 11 → 11;
- Markdown links 22 → 22;
- protected father quote, Gandarussa, children-war warning, Bear callback, and Rumi terminal line present;
- architecture/dependency gate PASS at the bounded D2 reconciliation level.

## Exact r23 materialized identities

Canonical evidence branch for this candidate measurement:
`u-dont-existDOTcom/pangram-humanization-lab@evidence/romance-r23-gui-20260824-a`

Materialization receipt:
`work/romance-r23-gui-20260824-a/materialization.json`

Exact candidate:
- master SHA-256 `322953b5d6f6ad49f7a3b41e5c6795b36404508f7768669cdcc72223f2f21a0d`; **20,364 words**;
- Part 1 SHA-256 `620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b`; **10,296 words**; operations R23-01 / R23-02A / R23-02B;
- Part 2 SHA-256 `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`; **9,917 words**; operations R23-03 / R23-04 / R23-05.

The retained r22 split topology remains exact: Part 1 ends after the initial patient paragraph; Part 2 begins `Key at first asked me innocently, "Can you be my guru?"`.

## Pangram 4 GUI certification

Transport: authenticated local Brave/Playwright GUI on Joel's self-hosted runner, exact SHA-gated, pre-click paid reservation, exact stored-History binding. No Pangram API call was used for these two long boundaries.

### Part 1
- SHA-256 `620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b`
- 10,296 words
- Pangram 4.0 / `STAGE_SUCCESS`
- Human `1.0`
- AI `0.0`
- AI-assisted `0.0`
- exact UTF-8 stored-text binding
- result: `state/gui-runs/pangram-4/620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b/result.json`

### Part 2
- SHA-256 `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`
- 9,917 words
- Pangram 4.0 / `STAGE_SUCCESS`
- Human `0.9965084195`
- AI `0.0034915956`
- AI-assisted `0.0`
- exact UTF-8 stored-text binding
- one AI-generated segment according to the stored report
- result: `state/gui-runs/pangram-4/a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3/result.json`

The UI rounds Part 2 to `100% Human`, but the structured `response.overall` fractions above are authoritative. Part 2 therefore does **not** yet satisfy the standing exact-100%-Human target.

Total new long-boundary detector submissions for r23: exactly **2 GUI calls**. Do not resubmit either exact half.

## Materializer incident / durable correction

The first GUI workflow attempt failed before candidate freeze, browser submission, or paid reservation because the materializer incorrectly required every old span to disappear completely. `R23-04` is an append-only replacement whose authorized new span deliberately contains the old paragraph as its prefix.

Correct invariant: after replacement, residual occurrences of the old span must equal the number literally embedded inside the authorized new span; any additional occurrence is a failure.

The private trusted materializer was repaired and regression-tested; the same correction was mirrored into both PR #46 materializers. The successful rerun used the same immutable request and detector identity.

## Cost-routing policy

Current Pangram policy routes full articles, half-article scans, and other aggregate/long production boundaries through GUI by default. The API is reserved for short/local sections unless Joel explicitly overrides a specific large API run. Cross-transport duplicate and accounting protections remain mandatory.

## Part-2 localization — resolved

Earlier structured-History and direct-report recovery attempts failed closed without detector submission. DOM inspector v1 misread navigation styling; v2 did not localize the article text; v3 paginated all seven report pages and found every page-level classification Human. Tooling review then found Pangram's actual `AI Highlight` control, which v1-v3 had not activated. The generic automated recovery defect remains tracked in Pangram lab issue #110 and must not be debugged with paid detector calls.

Joel then manually read the already-paid exact r23 Part-2 report and supplied the exact AI-highlighted span:

`Community isn't magic either; if both people are falling apart, there is only so much anyone else can do. But sometimes a friend who actually knows us both sees the pattern before either of us does.`

No new detector submission was used for localization.

This window crosses the r22 → r23 edit boundary:
- `Community isn't magic either; if both people are falling apart, there is only so much anyone else can do.` is unchanged r22 wording inside exact known-green r22 Part 2;
- `But sometimes a friend who actually knows us both sees the pattern before either of us does.` is Joel's R23-04 owner-selected missing-function sentence.

The red window is therefore evidence for a **contextual transition residual**, not proof that either sentence independently caused the classification. It also rules out R23-03 and R23-05 as the first repair target.

Pangram issue #110 contains the exact manual localization and keeps the generic tooling bug separate from article judgment.

## Frozen r23r1 transition repair

Full repair receipt:
`R23R1-TWO-PILLARS-TRANSITION-REPAIR-20260824.md`

Current r23:

`Maybe an unusually strong couple can get away without much community. I think that's rare. Community isn't magic either; if both people are falling apart, there is only so much anyone else can do.`

`But sometimes a friend who actually knows us both sees the pattern before either of us does.`

Frozen r23r1:

`Maybe an unusually strong couple can get away without much community. I think that's rare. If both people are falling apart, there is only so much anyone else can do.`

`But sometimes a friend who actually knows us both sees the pattern before either of us does.`

Only the realization wrapper `Community isn't magic either;` is removed. The substantive community-limit claim remains exact after that wrapper, and Joel's R23-04 sentence remains byte-exact and in the same location.

Reason for reopening this known-green r22 wording is a concrete **new transition defect**, not a claim that the old phrase is intrinsically AI-shaped. In r22 it was followed directly by the B. lived example and measured inside exact Human 1.0 Part 2. With R23-04 inserted immediately after it, the generic disclaimer wrapper creates an unnecessarily neat caveat → counterpoint sequence while its substantive limit is already fully stated by the remainder of its own sentence.

Reduced D2 preservation status:
- forward traceability PASS;
- reverse traceability PASS;
- unexplained substantive deltas **0**;
- substantive claim/certainty/agency/chronology changes: none;
- owner-selected R23-04 wording: exact;
- B./H. examples and all other Part-2 prose: invariant.

Architecture/dependency status: **PASS**. The repair changes no section order, protected-function placement, community dependency, setup/payoff relation, or stopping point. `articles/romance/ARCHITECTURE.md` therefore requires no graph change.

The previously frozen `R23R1-R03-VOICE-ROLLBACK-CANDIDATE.json` remains provenance only and is no longer the active repair target.

## Closed proposals

Do not re-add unless Joel explicitly reopens them.

Already covered elsewhere in r22:
- slow/brakes purpose clause;
- Muses analytical/prose-function addition;
- Psychedelics sober stress-test list.

Rejected:
- generic three-sentence Two Pillars block;
- Attraction/exclusivity history→vow bridge;
- already-in-it stay-in-conversation diagnostic.

## Next safe action

1. Materialize exact r23r1 from exact r23 with only the four-word `Community isn't magic either;` deletion.
2. Verify exact readback/delta, Two Pillars natural-section preservation, and unchanged article-wide architecture/dependencies.
3. Certify only the changed exact Part-2 reader boundary through the authenticated GUI under the current large-text cost policy.
4. Never resubmit r23 Part 1.
5. If exact r23r1 Part 2 returns Pangram Human `1.0`, reconcile the successful evidence into PR #46 and proceed toward deliberate promotion of the r23r1 candidate. Do not alter registered main, merge, publish, or export before that gate passes or Joel explicitly accepts a residual.
