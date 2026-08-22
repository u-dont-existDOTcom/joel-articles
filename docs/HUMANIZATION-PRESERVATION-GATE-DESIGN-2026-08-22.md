# Humanization preservation gate design — independent conception snapshot

Status: working design note, pre-existing-work scan snapshot
Date: 2026-08-22

## Trigger

Repeated Romance humanization passes have produced candidates that later audits correctly reject because a claim, qualification, attribution, protected function, or owner-required idea was deleted, generalized, moved incorrectly, or reassigned. The current protocols catch many of these failures, but too often **after prose generation or after detector work**.

The latest concrete example is the recovered `Talk about making love before you do it` candidate: one repair correctly removed a false attribution to Joel's father but simultaneously dropped Joel's distinct later readiness/co-parenting question and the associated early-sex/red-flag function. The existing post-draft fidelity audit caught it, but only after the candidate had already been generated and dispatched for detector measurement.

## Problem

The workflow currently treats preservation largely as an audit obligation. It needs to become a **precondition for generation and promotion**.

A model can satisfy a high-level instruction such as `preserve every proposition` while still losing a small but consequential unit during synthesis, especially when it is simultaneously optimizing architecture, rhythm, detector behavior, and concision. Post-hoc cold audits reduce the damage but do not prevent wasted detector calls or repeated semantic regressions.

## Candidate mechanism

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

## Candidate insight

The key shift is from **generate → audit → catch loss** to **specify invariants → generate only inside an authorized delta → prove preservation → test detector**.

This should reduce both semantic errors and wasted Pangram calls because the detector never sees a candidate that has not already supplied evidence that all protected units survived.

## Constraints

- The mechanism must not force every sentence into a giant bureaucracy. It should operate on the changed section/boundary and load-bearing article dependencies, not mechanically atomize unchanged prose.
- It must preserve real editorial freedom: wording, order, paragraph structure, and consolidation can change when authorized.
- It must distinguish genuine duplicate-function consolidation from silent deletion.
- It must not make the model preserve bad assistant prose merely because it existed in an earlier candidate. Authority remains owner/registered source first.
- It must preserve source wording, retrospective interpretation, and later synthesis as distinct provenance objects.
- It must not turn detector results into semantic authority.
- It should be machine-checkable where feasible, while acknowledging that semantic mapping still needs judgment.

## Pre-scan decision hypothesis

Likely implementation choice: **adapt/combine established traceability, change-impact analysis, regression-invariant, and configuration-control ideas rather than inventing a wholly novel editorial framework.**

This file intentionally records the independent conception before the existing-work scan so later prior art does not overwrite the original mechanism or problem framing.
