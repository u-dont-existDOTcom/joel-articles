# Joel-byline revision-trajectory corpus — feasibility audit — 2026-09-09

Status: **DATA/STRATEGY FEASIBILITY AUDIT / RETRIEVAL PROTOTYPE JUSTIFIED / PARAMETER TRAINING NOT YET JUSTIFIED / NOT ARTICLE PROSE / NO PANGRAM AUTHORIZATION**

Parent design:
`JOEL-BYLINE-REVISION-TRAJECTORY-LEARNING-FALLBACK-20260909.md`

Production strategy:
`SOMATIC-HUMANIZATION-STRATEGY-V3-ROUTER-AND-OWNER-COGNITION-20260909.md`

## Decision first

There is already enough high-information GitHub material to build a **retrieval-only revision-trajectory prototype now**.

There is **not yet evidence that the corpus is large or independent enough to justify parameter training**. The raw repository contains many files, but file count would badly overstate sample count because numerous artifacts are successive candidates, audits, supplements, or detector records for the same natural boundary.

The correct unit of data is an **independent owner-correction trajectory clustered by natural article boundary and decision chain**, not a file, turn, sentence, or Pangram result.

## What was inspected

This audit sampled multiple distinct correction families rather than inferring feasibility from one trajectory.

### 1. Somatic Introduction — full owner-teaching trajectory

Files:
- `experiments/trajectories/SOMATIC-INTRO-OWNER-TEACHING-TRAJECTORY-20260902.md`
- `experiments/trajectories/SOMATIC-INTRO-OWNER-TEACHING-TRAJECTORY-20260902-FROZEN.md`

This is the strongest existing gold-style trajectory because it preserves the actual iterative episode: model candidate, owner criticism, next candidate, owner rewrite, substantive corrections, and final freeze.

High-value signals include:
- repeated model self-revision plateau (`it's not getting less model shaped`);
- owner deciding to rewrite rather than continue the same method;
- owner correction of substantive logic as well as prose shape;
- direct owner rewrite reported Human/high at its tested earlier boundary;
- explicit freeze preventing post-hoc reconstruction from overwriting the raw episode.

Primary failure stages represented:
`REALIZATION`, `SEMANTIC_FIDELITY`, `OVERCOMPLETION_STOPPING`, and strategy-switch evidence.

### 2. Somatic Stage 1 — triad / compact-program correction

File:
`SOMATIC-STAGE1-TRIAD-PROGRAM-SHAPE-OWNER-CORRECTION-AUDIT-20260907.md`

Independent boundary from the Introduction.

High-value signals:
- exact rejected Somatic Experiencing lead;
- owner-supplied readiness sentence kept separate from generator evidence;
- rejected `Borrowing an Adult Perspective` pseudo-program;
- rejected Yoga candidate;
- diagnosis that owner semantic obligations can still become AI-shaped when the model serializes them into nested enumerations/program slots;
- explicit instruction not to repair by merely changing list length.

Primary failure stages represented:
`REALIZATION`, `ROUTE_SELECTION`, `OVERCOMPLETION_STOPPING`, with tags `preservation-unit serialization`, `nested enumeration`, and `compact program shape`.

### 3. Somatic Yoga — contrast-completion detector correction

File:
`SOMATIC-STAGE1-YOGA-MEDIUM-AI-OWNER-CORRECTION-20260908.md`

Independent natural boundary with an owner-reported exact detector result: AI / medium confidence.

High-value signal:
- after earlier list/triad repair, the model still completed conceptual space through repeated positive/negative contrasts;
- owner pointed to `That can be...`, `It doesn't have to be...`, and `I'm talking about X, not Y...` as manifestations of the larger structure;
- the method was explicitly escalated rather than locally paraphrased again.

Primary failure stages represented:
`REALIZATION` and `OVERCOMPLETION_STOPPING`, with tag `contrast completion`.

### 4. Somatic massage/aquatic — owner-thought topology failure and repair

Files:
- `SOMATIC-MASSAGE-AQUATIC-BODYWORK-INTEGRATION-CANDIDATE-20260908.md`
- `SOMATIC-MASSAGE-AQUATIC-COLD-AUDIT-STRATEGY-20260909.md`
- `SOMATIC-AQUATIC-BODYWORK-TAIL-REDISTRIBUTION-CANDIDATE-20260909.md`

Independent source/section family.

High-value signals:
- initial candidate had rich owner material but model converted one connected Hale thought into modality/evidence/advice/safety cards;
- invented Joel first-person experience was separately identified as provenance failure;
- revised realization preserved owner order/asymmetry and did not force massage subsection completeness;
- full exact aquatic candidate was owner-reported Human / medium confidence.

Primary failure stages represented:
`ROUTE_SELECTION`, `REALIZATION`, `PROVENANCE`, `PLACEMENT`, `OVERCOMPLETION_STOPPING`.

This is currently the best positive/negative pair for the V3 hypothesis that externally supplied thought topology matters more than owner content alone.

### 5. Romance owner review — E18 unique-function recovery

File:
`work/romance-owner-manual-dedup-20260827/REVIEW-V3-OWNER-FEEDBACK-20260827.md`

Cross-article independent evidence.

High-value signal:
- an earlier dedup operation correctly saw duplicated self-practice material but incorrectly swallowed a unique owner claim: relying on friends for relationship help can itself **create/deepen community**;
- owner feedback distinguishes function-level preservation from topical similarity;
- this is a useful negative example for selectors/revisers that over-compress apparently redundant material.

Primary failure stages represented:
`SEMANTIC_FIDELITY`, `ROUTE_SELECTION`, `PLACEMENT`.

### 6. Romance R7 — minimum-dose realization repair after structural approval

File:
`work/romance-owner-manual-dedup-20260827/R7-HUMANIZATION-AND-SUBSTACK-MERGE-20260827.md`

Cross-article positive trajectory family.

High-value signal:
- structural operations were already owner-approved;
- only surviving assistant sentence realization inside those operations was humanized;
- untouched owner prose remained untouched;
- exact R7 candidate was owner-reported 100% Human / high confidence;
- zero unexplained substantive deltas.

Primary failure stages represented:
`REALIZATION`, with explicit minimum-edit-dose evidence.

### 7. Romance R23R2 — one-operation owner-final local realization correction

File:
`work/romance-r22-reconciliation-20260823/R23R2-OWNER-FINAL-DELTA.json`

High-value signal:
- only one local realization/order changed;
- semantic functions remained preserved;
- prior local realization owner-reported AI / low confidence;
- exact owner-final local realization owner-reported Human / low confidence and accepted `good enough`;
- preservation proof records zero unexplained substantive deltas.

This is valuable for a reviser/reranker because the transformation is **small and meaning-matched**, rather than a complete owner rewrite confounded by new cognition.

Primary failure stage represented:
`REALIZATION`, with boundary-sensitive detector evidence.

## Feasibility conclusion

The repository already contains **at least seven sampled correction families with materially different natural boundaries and failure types**. This is not a claim that there are exactly seven usable trajectories; it is the minimum established by this audit.

The recursive branch tree shows many additional candidate/audit/owner-correction/owner-acceptance artifacts in Somatic and Romance. However, they cannot be counted as independent examples until clustered. A single Stage-1 Yoga correction may have several candidate files, audits, lesson supplements, and handoffs. Treating those as separate training examples would create severe leakage and pseudo-sample inflation.

### Current disposition

- **Retrieval/case-based prototype:** justified now.
- **Selector/reranker training:** plausible later, but first normalize and count independent decision chains.
- **Supervised reviser training:** plausible later; the corpus has the right *kind* of data, but sample sufficiency is not yet established.
- **DPO/preference optimization:** premature.
- **Independent thought-originator training:** premature and should remain separate from production humanization.

## Why retrieval comes first

Retrieval can exploit the strongest existing signal without pretending the sample size is larger than it is.

A current worker could classify a live failure as, for example:

`owner material -> preservation units serialized into compact program`

and retrieve the Stage-1 triad correction as a **process analogue**. Or classify:

`model reorganized one irregular owner thought into editorial cards`

and retrieve the aquatic correction chain.

The retrieved object should expose:
- abstract failure relation;
- owner judgment/correction;
- what changed at the thought/operation level;
- what did **not** change;
- whether the lesson was later promoted or remained local.

It should **not** expose unrelated owner prose as a sentence donor for the new article span.

This gives us a useful experiment before training: does case-based retrieval reduce repeat failures on held-out live work?

## Corpus normalization required before any learned model

### 1. Cluster by natural boundary / owner decision chain

All revisions, audits, detector calls, supplements, and handoffs about the same underlying passage belong to one trajectory cluster.

Example:
`Stage-1 Yoga functional-interoception lane` is one evolving family, not one example per file.

### 2. Preserve chronology

Within a cluster:

`source state -> candidate -> owner feedback -> candidate -> owner correction -> accepted/rejected/frozen state`

Later owner corrections/retractions control interpretation. Do not flatten chronology into unordered preferred/rejected pairs.

### 3. Separate owner-origin changes from realization-only changes

Tag whether the accepted improvement came from:
- new owner cognition;
- owner wording only;
- restored source language;
- model realization;
- structural deletion/movement;
- evidence correction;
- mixed contribution.

A candidate improved by owner substitution is production success but not evidence for generator learning.

### 4. Exclude or quarantine bad labels

Mandatory exclusions/quarantines include:
- the retracted false aquatic Human/AI split;
- synthetic probes unless the task is explicitly generator research;
- superseded assistant interpretations contradicted by later owner correction;
- detector-only comparisons where semantic equivalence is not established;
- unrelated Human corpus prose as production training targets for a Somatic function.

### 5. Keep detector evidence secondary

Where available, record Pangram as exact-boundary metadata. Do not make it the corpus target label.

The primary supervision is:
- owner judgment/correction;
- semantic/preservation fidelity;
- failure stage;
- exact operation/delta;
- accepted/rejected status.

## Recommended first retrieval corpus

Start small and high-precision rather than ingesting the entire experiments directory.

Initial seed clusters:

1. Somatic Introduction frozen teaching trajectory.
2. Somatic Stage-1 triad/program correction.
3. Somatic Yoga contrast-completion correction.
4. Somatic massage/aquatic topology correction and successful redistributed realization.
5. Romance E18 unique-function dedup correction.
6. Romance R7 minimum-dose realization repair.
7. Romance R23R2 local owner-final realization correction.

Then add other clusters only after the schema and retrieval behavior prove useful.

These seven seed families intentionally cover distinct failure classes rather than maximizing volume.

## Retrieval key design

Do not primarily embed topic nouns (`yoga`, `romance`, `massage`). The useful neighborhood is structural/editorial.

Index fields should privilege:
- failure stage;
- failure tags;
- owner-thought topology available yes/no/partial;
- source type;
- operation type;
- amount of model architectural freedom;
- whether owner correction changed cognition versus surface realization;
- stopping-point failure;
- preservation/provenance issue;
- technical/reference versus narrative genre;
- minimum-dose versus full reconstruction.

Topic can remain a weak secondary key.

## Evaluation for retrieval-only baseline

Use held-out live corrections or existing clusters not used in the seed library.

Compare:

A. current V3 router without trajectory retrieval;
B. V3 router + top structurally analogous trajectory lesson(s).

Measure:
- whether the same owner-identified failure recurs;
- amount of owner rewriting needed;
- preservation failures;
- provenance/actor drift;
- unnecessary model scaffold;
- owner acceptance/preference;
- detector result only if Joel separately authorizes one.

Do not compare by whether the retrieved example's vocabulary appears in the candidate. Lexical copying is a failure, not a goal.

## Data-size judgment

No numerical training threshold is asserted.

What is established:
- there are multiple independent natural-boundary correction families across at least two articles;
- at least one trajectory is already preserved turn-by-turn and frozen;
- several others contain exact rejected/accepted spans and explicit owner judgments;
- the repository has enough material to test case-based retrieval;
- independence and normalization have **not** been established for the full corpus;
- therefore parameter training would currently risk overfitting a small number of highly revised boundaries and mistaking repeated files for independent examples.

## Next implementation step

Build a machine-readable **seven-cluster seed ledger** from the families above, using the schema in `JOEL-BYLINE-REVISION-TRAJECTORY-LEARNING-FALLBACK-20260909.md`.

The ledger should contain references/hashes and compact abstract lessons, not duplicate every full article passage. Keep exact text available by source path for audit/reconstruction.

Then use retrieval-only assistance prospectively on new Somatic humanization work before considering any fine-tuning.

No article authority changes, prose changes, publication/export, or Pangram calls are authorized by this audit.
