# Somatic Stage 1 — next direction: isolated-writer generation — 2026-09-07

Status: **ACTIVE METHOD DIRECTION / NON-AUTHORITATIVE PROSE**.

This note does not modify article authority, owner-accepted prose, locks, links/media/native objects, or the working merged article. It does not authorize a Pangram call.

## Decision

The current manual map sequence has produced useful diagnostic learning, but same-context map refinement has reached diminishing returns for generation.

Keep the current supervisor-side lessons and gates, but **stop treating further prompt/map refinement inside the same saturated chat as evidence that future Stage-1 obligations are sealed from generation**.

The next generative experiment should use a genuinely isolated writer context.

## Why

The map sequence successfully exposed several recurring failure modes:

- preservation-inventory staircase;
- sentence-by-sentence state-transition cadence;
- semantic stasis / paraphrase looping;
- cross-boundary repetition of already-known article material;
- supervisor-question leakage into prose;
- example/marker -> criterion/sufficient-condition escalation;
- activation -> deliberate-trauma-processing chronology drift;
- matched positive/negative completion;
- invented objections / defensive aftercare;
- abstraction -> immediate concrete-example overpackaging.

These are valuable supervisor-side gates.

However, the latest v2 audit invalidated the claimed writer isolation. The same chat/model had already read the Stage-1 preservation inventory and then produced several supposedly hidden relations (`small part`, `come back`, voluntary stopping). Within that saturated context there is no discriminating evidence that these relations emerged locally rather than through contextual leakage.

Continuing to refine the internal map risks teaching the same model a larger and larger avoidance checklist. That may improve self-audit while making generation more supervised and less natural.

## Next architecture

### 1. Supervisor context

The canonical article chat keeps full access to:

- GitHub authority/state/locks/evidence;
- article-wide reader state;
- preservation inventory;
- prior failed probes and audits;
- cadence/thought-shape lessons;
- role-strength, chronology, cross-boundary, aftercare, and stopping-point gates.

The supervisor prepares a minimal literal writer packet and later audits the returned prose.

### 2. Physically/informationally isolated writer context

A fresh writer context must not have seen:

- the Stage-1 preservation inventory;
- prior candidate prose;
- prior audits;
- detector history;
- synthesized reader questions;
- map diagnostics such as staircase, semantic stasis, aftercare, binary completion, or hidden obligations.

It receives only the minimum literal packet needed to write at the current article edge, for example:

- the literal immediate upstream reader-visible paragraph;
- the current heading/subheading;
- one bounded source/semantic custody relation required for the local movement;
- explicit bans on invented autobiography, symptoms, chronology, evidence, mechanisms, or factual specificity.

No hidden curriculum or target prose shape is supplied.

### 3. Generation

The isolated writer writes naturally from the literal packet.

Do not force one thought to reach a word target. If enough prose is needed to judge cadence, request a natural paragraph/section-sized movement while allowing the writer to stop when the thought stops.

If the first isolated movement is too short to evaluate, use a **new fresh isolated writer packet/context** for the next movement rather than extending the same writer with supervisor feedback that reveals hidden obligations.

### 4. Supervisor audit after generation

Only after prose returns, the canonical supervisor checks:

- article-wide and immediate cross-boundary subtraction;
- semantic contribution / redundancy;
- invented-objection / defensive-aftercare;
- role / entailment-strength preservation;
- chronology / agency invariants;
- conditional/binary-completion artifacts;
- abstraction -> example duplication;
- true stopping point;
- acoustic / cognitive cadence;
- forward/reverse preservation traceability.

A failed candidate is diagnostic evidence, not material to iteratively coach the same isolated writer unless the feedback can be given without exposing the hidden curriculum. Prefer a fresh isolated writer for substantially different retries.

## Strategic interpretation

The project is **not changing direction away from reader-state, preservation, and cadence analysis**. Those have become the supervisor's evaluation system.

The change is that they should no longer be the writer's internal generation environment.

The working model is now:

`rich canonical supervisor -> minimal isolated writer -> finished natural prose -> rich canonical supervisor audit`

rather than:

`rich canonical supervisor pretending part of itself cannot see what it already knows`.

## Immediate next experiment

Create one exact minimal writer packet for Stage 1 / Somatic Experiencing and run it in a genuinely fresh context that has not seen the Somatic preservation inventory or the preceding humanization experiment history.

Do not run Pangram unless Joel explicitly asks.