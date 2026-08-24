# Romance r22 → r23 reconciliation

Purpose: reconcile the detector-green r22 working candidate into registered Romance authority without merging the historical detector task branch, while preserving editorial features from older versions only when they are genuinely missing from the current function map.

Registered canonical master remains `main:articles/romance/master.md`, SHA-256 `af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`, until deliberate owner reconciliation changes the registered article family. The PR branch's `articles/romance/master.md` is intentionally byte-identical to registered main; candidate prose lives only under this work directory until promotion.

## Known-green rollback baseline — exact r22

Source:
`task/romance-detector-repair-20260820:work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/candidate-master.md`

- Git blob `9f6bf7ed77093569a98fe606fda96ac277839f99`
- SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`
- 20,282 Markdown words
- Part 1 SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`: Pangram 4.0 Human `1.0`, zero AI windows
- retained Part 2 SHA-256 `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`: Pangram 4.0 Human `1.0`

Those are two exact half measurements, not a measured whole-document score.

## Current continuation candidate — r23

Joel's 2026-08-24 owner review plus function-first re-audit narrowed the reconciliation to **five editorial features / six exact replacement operations**. The exact whitelist is:

`R23-FIVE-OWNER-EDITS-MANIFEST.json`

Current operations:
1. prospective libido-divergence planning in Talk;
2. owner Affection simmer/taking-for-granted/anti-homework realization;
3. owner Affection changed-sex-life/new-normal/feeling-wanted realization;
4. clearer student-testimonial attribution + owner jade-egg training relation;
5. owner-final Two Pillars sentence: `But sometimes a friend who actually knows us both sees the pattern before either of us does.`;
6. `I can hear a whole future in those two words—...` in Choosing Together.

The four exact changed natural boundaries are materialized under:

`r23-boundary-candidates/`

Read first:
- `OWNER-REVIEW-PROPOSED-FEATURE-RECOVERIES-20260824.md`
- `FUNCTION-COVERAGE-REAUDIT-SURVIVING-PROPOSALS-20260824.md`
- `R23-FIVE-OWNER-EDITS-MANIFEST.json`
- `r23-boundary-candidates/boundary-manifest.json`
- `R23-BOUNDARY-COLD-READ-20260824.md`

Boundary cold-read status: **PASS** with zero unexplained substantive deltas. Exact r23 detector status: **UNMEASURED**.

The complete r23 master and exact r23 Part 1 / Part 2 half-boundaries remain to be deterministically assembled from exact r22 plus the frozen six operations. `materialize_r23_five_owner_edits.py` is the frozen assembly tool for a runtime that has repository checkout access.

## Function-first reconciliation rule

Joel corrected the earlier comparison method because it was too close to blind copying. A wording difference does not prove a function disappeared.

Before any historical feature is proposed for reinsertion:

1. decompose the older span into distinct functions;
2. inspect the complete current natural section, and relevant linked sections, for each function by meaning rather than phrase match;
3. classify each function as absent / partial / equivalent / stronger or more concrete;
4. recover only the genuinely missing remainder;
5. cold-read the literal integration in the full current section;
6. check durable detector history before proposing verbatim historical wording inside a known-green boundary.

Canonical rule: `main:docs/HUMANIZATION-KNOWN-GREEN-CALIBRATION.md`.

The Two Pillars incident is the model example: the old three-sentence block carried three functions, while r22 already realized two more concretely. Only the outside-friend-pattern-seeing function was missing, so only one sentence survived.

## Closed proposals

Closed as already functionally covered in r22:
- slow/brakes purpose clause;
- Muses analytical/prose-function addition;
- Psychedelics sober stress-test list.

Rejected by Joel / owner review:
- generic three-sentence Two Pillars restoration;
- Attraction/exclusivity history→vow bridge;
- already-in-it stay-in-conversation diagnostic.

Do not resurrect these merely because older files contain them.

## Historical evidence, not current routing

The prior conservative materialization, `PRODUCTION-AI-SHAPE-AUDIT.md`, and `HOLISTIC-REPAIR-PROPOSALS.md` remain as failure/reconciliation evidence. They are **not** candidate authority. Joel tested the six-proposal holistic bundle in Pangram 4.0 and it returned 59.5% AI / 40.5% Human over 2,347 words, including several high-confidence AI runs.

Do not delete that history, but do not use it as the current candidate.

## Next technical gate

1. deterministically assemble exact full r23 from exact r22 + the frozen six operations;
2. verify full-candidate SHA, exact replacement counts, headings, links, native objects, protected anchors, and zero unexplained deltas;
3. generate exact r23 Part 1 / Part 2 boundaries using the same split contract as r22;
4. recover Pangram cache/reservation/call-ledger state before any paid action;
5. certify the changed full half-boundaries through the current trusted self-hosted route if current balance/call policy permits;
6. keep exact r22 as rollback if a changed boundary fails;
7. only after editorial/detector reconciliation deliberately update registered `articles/romance/` authority.

Do not spend four section-level Pangram calls and treat them as final certification; Romance has demonstrated composition sensitivity. Do not merge PR #29 wholesale. Do not publish/export.
