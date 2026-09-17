# Joel Articles — owner-facing turn contract

Status: **ACTIVE OWNER RULE**

Date: 2026-09-17

Applies to owner-facing work in `u-dont-existDOTcom/joel-articles`. Current direct Joel instructions still outrank this file.

## End-of-turn article link

At the end of every Joel Articles owner-facing turn, include a direct link to the current full humanized article-so-far artifact for the active article. During an active humanization lane, maintain one stable article-local rolling review path and update it as accepted/locked prose or the current owner-review candidate changes. Never label a superseded candidate as current authority.

For the current Inner Child Therapy lane the stable review path is:

`articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md`

Inner Child Therapy remains unregistered/non-authoritative unless `articles/INDEX.json` later says otherwise.

## Owner-decision presentation

When asking Joel whether a possibly missing function should be restored, added, or made explicit:

1. show the exact current prose that already carries some or all of that function;
2. state the exact residual function, if any, that would remain missing;
3. give the material pros and cons of changing versus leaving it alone;
4. give a recommendation;
5. never silently restore removed material.

For material editorial choices generally, state the relevant pros, cons, and recommendation in plain language instead of asking Joel to infer the tradeoff from abstract descriptions.

## Audit means output + method audit

Whenever Joel says `audit`, do not audit only the current prose/artifact. Audit the producing chain as well.

Recover the literal prior plan when one exists and classify any failure across these loci:

- **plan generation** — the plan itself encoded the wrong architecture, assumption, scope, sequencing, or constraint;
- **implementation/generation** — the plan was sound or partly sound but the produced artifact did not actually implement it;
- **admission/review** — a gate or cold audit admitted a defect it should have blocked;
- **source/authority** — stale, wrong, or superseded authority was used;
- **strategy** — repeated evidence shows the current method's causal premise is not producing the owner outcome.

For every applicable locus, state the causal mechanism and the concrete process change that should prevent the same failure next time. Do not substitute `make a new plan` for this diagnosis.

If the prior plan was not durably captured, say so rather than reconstructing it from memory. Missing plan traceability is itself a process defect and must be repaired before relying on plan-versus-implementation claims.

When the same underlying structural failure survives a targeted repair, stop materially similar local refinement. Compare at least one structurally different approach before another same-method attempt, and switch strategy when the evidence supports it. Do not keep accumulating prohibitions around a generator that is reproducing the same architecture.

For humanization specifically, keep the preservation ledger as a fidelity constraint rather than allowing its enumerated units to become the prose outline. A candidate can preserve every unit and still fail because the generation architecture is model-shaped.

## Anti-listicle and anti-repetition owner rule

Avoid checklist/listicle realization whenever and however reasonably possible. A genuine map, procedure, or enumeration may still require explicit structure, but do not turn prose into taxonomies, matched category lists, or comprehensive mini-checklists merely because the source functions can be enumerated.

Do not repeat information the article has already supplied unless Joel is deliberately using repetition for emphasis. Joel commonly signals intentional repetition explicitly with wording such as `I know I mentioned this before but...`; absent that signal, prefer forward movement over recap.

## Humanization prediction format

When the active workflow asks for multiple predicted realizations before generation, provide **actual prose predictions by default**, substantial enough for Joel to inspect the model's writing assumptions. Do not silently substitute prose descriptions for the predicted realizations.

Abstract prediction descriptions are appropriate only when an unresolved architecture/boundary decision makes literal prose prematurely misleading. If used, state that reason explicitly. Once the architecture is sufficiently resolved, return to literal prose probes.

Predicted realizations are diagnostic planning probes, not automatically the final candidate or article authority.
