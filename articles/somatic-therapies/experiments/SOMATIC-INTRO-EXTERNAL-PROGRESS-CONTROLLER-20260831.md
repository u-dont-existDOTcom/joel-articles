# Somatic Introduction — external progress controller

Updated: 2026-08-31
Status: **CURRENT OWNER-CORRECTION / active process architecture for the manual Introduction lane**

## Why this exists

Joel corrected a remaining flaw in the Somatic manual-humanization architecture.

A hard outside verifier can reliably reject a bad candidate, but rejection alone does not buy a better next raw generation. The next writer can simply ignore or fail to internalize the same instruction again. More instructions, a stronger reminder, or a richer rejection message do not solve that. They only improve the information available to a probabilistic generator; they do not force that generator to use it.

Therefore the process must stop treating the writer's internal compliance as the durable learning mechanism.

## Governing distinction

There are three separate problems:

1. **Generation:** produce a new realization.
2. **Adjudication:** decide whether that realization violates known lessons or regresses.
3. **Learning/progress retention:** make sure useful gains survive even when a later generator ignores feedback.

An outside verifier solves (2) much better than same-context self-review. It does not by itself solve (3).

No prompt-level mechanism can guarantee that an LLM will obey a semantic instruction on its next raw generation. The hard control available outside the model is over **selection, promotion, and state**, not over the model's latent generation process.

## Externalized monotonic frontier

For this lane, the durable unit of progress is not `the latest draft`. It is an **externally maintained frontier** consisting of:

- the best currently admissible candidate identity, if one exists;
- all semantic/provenance constraints that remain satisfied;
- all lesson dimensions currently cleared;
- unresolved defect(s), ranked by importance;
- the strongest known generative failure pattern;
- the next bounded search objective;
- the evidence used to accept or reject each raw sample.

A raw writer output is disposable and may be arbitrarily bad. It does **not** become the next state merely because it is newer.

## Verifier output must be comparative, not merely binary

The outside verifier must not return only `REJECT` or `you forgot X`.

It must compare the raw sample to the current frontier and return at least:

```text
HARD_CONSTRAINTS: PASS / FAIL
REGRESSIONS: [cleared dimensions that became worse]
IMPROVEMENTS: [dimensions that materially improved]
UNRESOLVED_DEFECTS: [ranked]
STRONGEST_BLOCKING_DEFECT: one concrete diagnosis
FRONTIER_COMPARISON: DOMINATES / NONDOMINATED / REGRESSES / INCOMPARABLE
NEXT_SEARCH_TARGET: one bounded change in generative problem, method, context, or representation
PROMOTION: ALLOW / BLOCK
```

A critique is useful only insofar as it changes external search state or promotion state. The generator may still ignore it.

## Promotion rule

A new raw sample may replace the current frontier only if:

1. semantic/function/provenance constraints remain satisfied;
2. it does not regress a dimension already cleared unless the owner explicitly accepts that tradeoff;
3. it materially improves at least one unresolved target or produces a genuinely different nondominated route worth retaining;
4. it clears the active hard admission gate before owner presentation.

Otherwise it is rejected as a sample and **cannot overwrite the frontier**.

This creates monotonicity in accepted state even though raw generations can regress.

## What happens after rejection

Do **not** merely send the rejection back to the same writer and hope it listens.

The controller changes the next search operation. Depending on the evidence, this may mean:

- use a fresh writing context rather than the saturated writer context;
- alter the representation of the unresolved thought without changing semantic authority;
- change which defect is targeted first;
- remove a rejected candidate from the next writer's context to avoid anchoring;
- preserve only the verified lesson/defect vector, not rejected sentence architecture;
- use a different available model/context when correlated generative priors are the blocker;
- generate another disposable sample and re-adjudicate externally.

The controller, not the writer, decides whether the search operation changed enough to justify another raw sample.

## Owner-facing guarantee and non-guarantee

This architecture **cannot guarantee that the next raw LLM generation is better**. No current prompt can hard-force semantic obedience inside the generator.

It can enforce a stronger and actually useful guarantee:

> **A regressive raw generation does not become the next owner-facing pass. The externally recorded frontier cannot silently forget cleared lessons. The next owner-facing pass must be a verified frontier advance, or there is no new pass yet.**

If repeated raw samples fail to advance the frontier, stop and change method or request genuinely new owner cognition rather than exposing the owner to repeated known regressions.

## Relationship to the existing Somatic contract

This file supersedes any interpretation of `A11 — instruction accretion is not a forcing function` that treats `quarantine + hard reject + tell the writer the defect` as a complete learning architecture.

Candidate quarantine and independent verification remain useful for adjudication. The missing third component is this externally maintained monotonic progress frontier.

Codex may mechanically store frontier state, launch bounded fresh contexts, and enforce promotion bookkeeping. Codex does not decide prose or editorial truth. The reasoning/writing Chat and independent verifier supply the semantic judgments; the external controller prevents those judgments from being forgotten by a later writer.
