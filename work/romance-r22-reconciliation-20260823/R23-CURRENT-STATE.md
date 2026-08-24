# Romance r23 current state

Updated: 2026-08-24

## Status

The five-feature / six-operation r23 candidate is now **fully materialized, preservation-clean, and measured in its exact two composition-aware reader-visible halves through the authenticated local Playwright GUI**.

Registered `main:articles/romance/master.md` remains unchanged. PR #46's branch copy of `articles/romance/master.md` remains byte-identical to registered main; r23 stays isolated as a reconciliation candidate until the remaining Part-2 detector residual is resolved or explicitly accepted.

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

Current Pangram policy now routes full articles, half-article scans, and other aggregate/long production boundaries through GUI by default. The API is reserved for short/local sections unless Joel explicitly overrides a specific large API run. This is mechanically enforced in the Pangram repositories. Cross-transport duplicate and accounting protections remain mandatory.

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

Use **read-only authenticated Pangram History localization** on exact r23 Part 2 to locate the single residual AI segment. Do not buy another detector call merely to localize it.

After localization:
1. inspect the exact residual in its natural section/context;
2. determine whether it lies inside one of the three authorized Part-2 r23 edits or is a contextual interaction elsewhere;
3. preserve the owner-authorized functions and exact r22 rollback anchor;
4. make the smallest justified editorial repair only if a real local defect/realization problem exists;
5. re-run preservation/architecture proof after any semantic edit;
6. certify only the changed composition-aware Part-2 boundary through GUI under the current cost policy.

Do not alter registered main, merge r23 into article authority, or publish/export before this gate is complete or Joel explicitly accepts the residual.