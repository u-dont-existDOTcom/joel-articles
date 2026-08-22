# Humanization preservation gate design — independent conception snapshot

Status: working design note
Date: 2026-08-22

## Trigger

Repeated Romance humanization passes have produced candidates that later audits correctly reject because a claim, qualification, attribution, protected function, or owner-required idea was deleted, generalized, moved incorrectly, or reassigned. The current protocols catch many of these failures, but too often **after prose generation or after detector work**.

The latest concrete example is the recovered `Talk about making love before you do it` candidate: one repair correctly removed a false attribution to Joel's father but simultaneously dropped Joel's distinct later readiness/co-parenting question and the associated early-sex/red-flag function. The existing post-draft fidelity audit caught it, but only after the candidate had already been generated and dispatched for detector measurement.

## Problem

The workflow currently treats preservation largely as an audit obligation. It needs to become a **precondition for generation and promotion**.

A model can satisfy a high-level instruction such as `preserve every proposition` while still losing a small but consequential unit during synthesis, especially when it is simultaneously optimizing architecture, rhythm, detector behavior, and concision. Post-hoc cold audits reduce the damage but do not prevent wasted detector calls or repeated semantic regressions.

## Independent conception before existing-work scan

Introduce a **Preservation Proof Gate** for P2S/P3/P4 humanization and detector repair.

Before prose generation:

1. Freeze the authoritative source boundary and exact hash.
2. Decompose only the changed scope into atomic preservation obligations: claims, certainty, attribution/provenance, actor/action/object, chronology/causality, exact memories/quotations, unique examples, owner judgments, rhetorical/protected functions, links/media/native objects, and necessary recurrence.
3. Give every obligation a stable ID and an allowed disposition before drafting: `must remain here`, `may move to <destination>`, `owner-superseded`, `owner-deleted`, or `duplicate-function consolidation with named surviving realization`. There is no generic `omit` disposition for assistant convenience.
4. Freeze a **change whitelist** describing what the current operation is actually authorized to alter. Any semantic unit not on the whitelist is presumed invariant.

After prose generation, before detector submission:

5. Require a candidate-to-source traceability pass in which every preservation obligation maps to an exact candidate span or an already-authorized disposition.
6. Require a reverse-delta pass: every substantive candidate addition, deletion, attribution change, certainty change, actor/causal change, or movement must map to the change whitelist or owner authority.
7. Fail closed on any unexplained delta. Repair fidelity before Pangram.

After any detector-driven edit:

8. Re-run the same traceability and reverse-delta checks before another paid call. Do not rely on the fact that the prior candidate passed.
9. Treat detector-green text with an unexplained delta as a failed candidate, not a near-pass.

### Candidate insight

The key shift is from **generate → audit → catch loss** to **specify invariants → generate only inside an authorized delta → prove preservation → test detector**.

This should reduce both semantic errors and wasted Pangram calls because the detector never sees a candidate that has not already supplied evidence that all protected units survived.

### Constraints

- The mechanism must not force every sentence into a giant bureaucracy. It should operate on the changed section/boundary and load-bearing article dependencies, not mechanically atomize unchanged prose.
- It must preserve real editorial freedom: wording, order, paragraph structure, and consolidation can change when authorized.
- It must distinguish genuine duplicate-function consolidation from silent deletion.
- It must not make the model preserve bad assistant prose merely because it existed in an earlier candidate. Authority remains owner/registered source first.
- It must preserve source wording, retrospective interpretation, and later synthesis as distinct provenance objects.
- It must not turn detector results into semantic authority.
- It should be machine-checkable where feasible, while acknowledging that semantic mapping still needs judgment.

## Bounded existing-work scan

The scan searched the underlying problem rather than the proposed name.

### Requirements engineering and configuration control — largely solved and reusable

NASA requirements-management guidance requires baselined requirements, bidirectional traceability, source/owner identity, impact analysis before changes, consistency checking, and review/approval of changes. NASA's software-engineering handbook explicitly uses traceability to detect both missing implementation and extra/orphan implementation. ISO/IEC/IEEE 29148 is the corresponding general requirements-engineering standard family.

Reusable remainder:

- source baseline and stable requirement IDs;
- bidirectional requirement ↔ implementation traceability;
- change-impact analysis before approval;
- explicit treatment of orphan/extra elements;
- independent review where practical.

Editorial adaptation: `requirement` becomes a protected semantic/function unit; `implementation` becomes the candidate realization; `orphan implementation` becomes a substantive candidate delta with no source/change authority.

### Translation validation — strongly analogous and reusable

Pnueli, Siegel, Singerman, Shtrichman and later compiler-validation work established **translation validation**: instead of proving a translator/optimizer correct in general, validate every individual source→target transformation after it runs. This maps closely to LLM rewriting because the transformer is nondeterministic and cannot be trusted merely because its instructions are good.

Reusable remainder:

- each rewrite is independently validated against its exact source;
- correctness belongs to the produced transformation, not to confidence in the transformer;
- more aggressive transformations demand stronger validation.

Editorial adaptation: every D2/D3/D4 rewrite produces a candidate plus a preservation certificate/ledger; the humanization prompt itself is never evidence that preservation succeeded.

### Mutation testing — reusable for validating the validator

Mutation testing evaluates test adequacy by injecting artificial faults and checking whether the test suite detects them. The mature literature treats mutation as a way to expose weak tests rather than as a production transformation.

Reusable remainder:

- create synthetic semantic mutants: delete a claim, flip attribution, weaken certainty, swap actor/object, erase a unique example, merge two distinct provenance planes;
- the preservation gate should reject these mutants;
- if a mutant survives, the gate/test needs improvement.

This is a validator-regression technique, not article editing.

### Metamorphic testing — partially reusable

Metamorphic testing checks necessary relations among transformed inputs/outputs when a simple oracle is unavailable. It is useful for invariants such as: a style-only rewrite must preserve the claim set; adding a formatting-only change must not change semantic traceability; moving an intact section should preserve its unit identities while changing location.

Useful as a testing technique for future tooling, but not necessary as the primary editorial workflow.

### Text style-transfer evaluation — directly relevant but insufficient alone

Text style-transfer research explicitly separates **style transfer**, **content preservation**, and **naturalness/fluency**. Recent meta-evaluation work continues to find content-preservation measurement difficult and shows that widely used automatic metrics can be misleading. Human evaluation remains important, and metric ensembles can help.

Reusable remainder:

- never collapse detector/style success, content preservation, and writing quality into one score;
- do not trust embedding or LLM similarity alone as the preservation proof;
- keep exact structured traceability and human semantic review blocking.

### Existing project/universal work — partially solved

Current `EDIT-CONTRACT-AND-LEDGERS.md`, `HUMANIZATION-AND-COHERENCE.md`, `HUMANIZATION-ARCHITECTURE-GATE.md`, and the universal `editorial-authority-and-lossless-editing` / `whole-argument-reconstruction` patterns already establish authority, reversible deletion, source/meaning/context/destination ledgers, whole-argument recovery, and post-edit audits.

The novel remainder exposed by Romance is narrower: **those requirements are not yet a mandatory pre-generation and pre-detector proof obligation with bidirectional delta accounting.** The workflow can still generate first and discover loss later.

## Build/adapt/reuse decision

**Decision: COMPOSE + ADAPT.**

Do not invent a new semantic-similarity metric. Do not replace the current architecture or edit ledgers.

Compose:

1. NASA/29148-style bidirectional traceability and controlled baselines;
2. translation-validation's per-transformation proof obligation;
3. existing Joel article authority/meaning/context/destination ledgers;
4. mutation-testing-style causal regressions for the preservation validator;
5. the existing separation of fidelity, Pangram status, and idiolect retention.

Add only the editorial-specific remainder:

- stable preservation-unit IDs for the changed scope;
- an explicit authorized-change whitelist;
- source→candidate and candidate→authority traceability;
- a blocking zero-unexplained-delta condition before detector calls;
- mutation/regression fixtures that deliberately remove or alter protected units.

## Strongest baseline comparison

Current baseline: `generate/reconstruct → architecture/fidelity cold audit → detector → re-audit after detector edits`.

Proposed baseline: `freeze authority → preservation ledger + change whitelist → generate/reconstruct → bidirectional translation validation → architecture/fidelity cold audit → detector → repeat translation validation after every detector-driven edit`.

Expected advantages:

- semantic losses are rejected before paid detector work;
- accidental additions are caught as well as deletions;
- false attribution and provenance collapse become first-class delta failures;
- every deletion/consolidation has a named source and disposition;
- a green detector cannot hide an unexplained semantic change;
- review becomes easier because the candidate carries an explicit proof of what changed and what did not.

Tradeoff: more setup on substantial rewrites. Mitigation: scope the ledger only to the changed natural section plus known dependencies; do not atomize the entire unchanged article for a local repair.

## Implementation target

Promote a blocking `HUMANIZATION-PRESERVATION-GATE.md` and route P2S/P3/P4 and detector work through it. Update the edit contract, humanization protocol, task modes, architecture gate, and root skill so the preservation proof occurs **before** detector submission, not merely during closeout.

Future tooling should make the ledger machine-readable and add semantic mutation regressions. The first protocol revision can be prose/schema-driven; automation should follow only where it can detect real failure modes rather than create false confidence.
