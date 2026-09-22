# Humanization Fresh-Critic Gate

Status: **BLOCKING** when a fresh model/context is used as pre-Pangram model-shape evidence in Joel-byline humanization.

Use with `HUMANIZATION-COLD-AUDIT-GATE.md`, `project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md`, the current post-generation tell library, and the preservation/architecture gates.

## 1. Role

A fresh critic is a **falsification surface**, not a voting surface.

Its task is to find a reason the candidate is still model-shaped before detector admission. Positive Human-facing features never offset an unresolved AI-shaped operation.

Freshness addresses context contamination. It does **not** establish critic competence, sensitivity, or completeness.

## 2. Packet

Give the critic:
- the literal target candidate **inside its natural reading boundary**;
- enough accepted prose immediately before/after to judge continuity, antecedents, register, and section placement;
- intended reader;
- heading promise/local purpose;
- current post-generation tell rubric.

Withhold:
- prior candidate history;
- prior defenses;
- detector scores/windows;
- preservation-unit ledgers and source-obligation checklists;
- same-context reasoning about why the candidate should work.

`candidate + rubric` alone is invalid when the possible defect concerns audience, transition, antecedent, or section function.

## 3. Adversarial order

Before cataloguing Human-facing features, require the critic to make the strongest case that the prose is model-shaped.

It must inspect:
- local realization;
- paragraph/section topology;
- reader model: **who is this talking to?**
- live reader pressure: **why does this matter now?**
- antecedents/referents;
- cumulative instruction-manual/listicle cadence;
- one-clean-teaching-job-per-beat / optimal semantic efficiency;
- abrupt complication;
- checklist/taxonomy flow;
- explanatory aftercare;
- source/requirements ledger made reader-visible.

## 4. Mixed aggregation

A finding does not become nonblocking merely because it is individually labelled `mixed`.

Before PASS, aggregate mixed findings at paragraph/section scale. If several features combine into a known model-shaped operation, the aggregate is blocking even when each feature could occur naturally by itself.

Human-facing features are recorded separately. They do not cancel AI-shape.

## 5. Candidate dispositions

Before PASS, disposition the three strongest credible AI-shape candidates, or all if fewer than three:

- `REPAIR`
- `PRESERVE-EXACT-REALIZATION-WITH-SPECIFIC-REASON`
- `NOT PRESENT`
- `UNRESOLVED`

`UNRESOLVED` blocks.

**Protected meaning/function is never by itself a reason to preserve current wording, cadence, paragraph topology, or another realization choice.** A preserve disposition must explain why the exact realization—not merely the cognition—is required by owner wording, quotation/provenance, safety, architecture, evidence, or genre.

## 6. Two-sided critic calibration

A non-detection can gate only when the critic configuration has current evidence of both specificity and sensitivity.

For each materially changed rubric/provider/model configuration, blind-test the same setup on:
1. at least one same-register owner-accepted/known-good control; and
2. at least one same-register owner-rejected/known-bad control representing a relevant failure class.

Do not reveal labels, provenance, or detector status to the critic.

Accepting the good control alone proves only that the critic can avoid overcalling AI. It does not show that the critic can detect the target failure class.

If the critic misses the known-bad control, its non-detection on the target is **non-gating evidence**.

Reuse a still-current calibration result. Do not rerun controls on every candidate.

Current regression fixtures and expected classifications are in `HUMANIZATION-AUDIT-ADMISSION-REGRESSION-20260922.md`.

## 7. Admission

`no definite AI tells` is not an admission result.

Fresh-critic PASS requires all of:
- no unresolved credible AI-shape candidate;
- no cumulative mixed pattern;
- reader-model check passes;
- why-now check passes;
- antecedent/referent check passes;
- at least one source-grounded Human-facing relation that is not merely a surface device;
- two-sided critic calibration passes for the current configuration.

A PASS here still does not prove human authorship. Continue separately through preservation, architecture/cold-read, final preservation, and Pangram in the normal order.

## 8. Failure handling

If the critic finds a blocking issue:
1. repair internally;
2. invalidate affected downstream gates;
3. use a new genuinely fresh context/request on the repaired target;
4. do not spend Pangram until this gate and the remaining non-detector gates pass.

If the same failure class recurs despite materially similar repairs, apply the strategy-efficacy rule and change architecture rather than adding another local prohibition.
