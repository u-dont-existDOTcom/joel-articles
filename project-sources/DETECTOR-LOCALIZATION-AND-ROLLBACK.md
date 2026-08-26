# Detector Localization and Rollback — Joel-byline Protocol

Status: **ACTIVE editorial/detector protocol.** Promoted 2026-08-21 from the Romance Part 1 and Part 2 repair sequences.

Use this after semantic/architecture review and with `RHYTHM-AND-THOUGHT-SHAPE.md`. It governs how to interpret detector windows and how to choose the next repair operation. Exact Pangram outcomes remain boundary-specific evidence; the editorial rules below are reusable.

## 1. A detector window is not a causal attribution

A Pangram red/AI window tells you where the classifier expresses AI evidence on the submitted boundary. It does **not** prove that the sentence which caused the regression is inside the highlighted window.

Contextual/nonlinear behavior can make:

- a downstream edit change an upstream highlighted window;
- an edit in one paragraph change the classification of the paragraph before it;
- two individually Human natural sections create an AI-shaped transition when adjacent;
- a locally 100% Human section participate in a red aggregate boundary.

Therefore never say `this sentence caused the detector failure` merely because Pangram highlighted it. Use `the residual window is here` until controlled evidence localizes causality.

## 2. Compare exact draft identities before rewriting highlighted prose

When a previously better or green boundary regresses:

1. identify the exact last known-passing or better text SHA;
2. diff it against the current candidate;
3. list every substantive edit made since that state;
4. ask whether one of those edits changed a natural section or transition even if Pangram now highlights somewhere else;
5. only then choose a repair.

Do not start by paraphrasing the highlighted sentence.

## 3. Prior Human status is evidence, not immunity

A previously Human-scoring span deserves protection from reflexive detector-driven rewriting, but **prior green status does not prove the prose is editorially strong in every later architecture**.

A stronger reorganization can expose a latent model-shaped passage that the old placement or surrounding boundary masked. When a formerly green span turns red after an independently justified structural improvement, test two competing hypotheses:

1. **boundary/composition sensitivity** — the prose is sound and the detector changed because the surrounding input changed;
2. **latent prose weakness exposed by better architecture** — the old context hid a genuinely generic, overcompleted, overly polished, or model-shaped passage that becomes obvious in the new rhetorical position.

Do not choose between them from detector color alone. Compare exact identities and prior boundary evidence, then cold-read the exposed span in its new article function. Give decisive weight to independent editorial quality, owner judgment, provenance, heading fit, paragraph jobs, live-question continuity, and minimum-change controls.

If the new architecture is clearly better **and** the exposed passage now reads genuinely model-shaped, keep the stronger architecture and repair the local defect. Do not roll back a good structural improvement merely to recover an old detector score.

Romance supplied a direct case on 2026-08-26: merging two adjacent sections created a stronger single progression but exposed a previously Human-scoring tail as High-confidence AI. The initial diagnosis incorrectly blamed contextual detector sensitivity. Joel correctly identified that the old arrangement had hidden weak AI prose more effectively. Keeping the merge and minimally rewriting only the exposed tail restored the pass while preserving the stronger article structure.

This rule refines, rather than contradicts, the known-green guard: known-green prose should not be reopened **solely because it turns red**, but it may be revised when the architecture change independently improves the article and a separate editorial diagnosis confirms a real defect.

## 4. Rollback is a first-class repair operation

The next candidate need not contain new prose. Prefer rollback when a later assistant cleanup replaced owner/registered wording or an already measured passing realization without adding necessary thought.

Restore the smallest higher-authority / known-passing realization first when it:

- improves provenance or owner fidelity;
- recreates a natural section that previously passed;
- removes an unnecessary assistant intervention;
- preserves meaning, links/media, and protected functions.

After rollback, test the appropriate wider boundary. A locally passing rollback can still interact differently in aggregate; that is evidence about context, not evidence that rollback was editorially wrong.

## 5. Natural section first; adjacent transition when needed

Old detector windows and arbitrary half-document splits are localization clues, not semantic units.

Default diagnostic order:

1. measure/reason about the **natural section** containing the residual;
2. if that section is sound or already Human, inspect the neighboring section;
3. if the aggregate residual crosses a heading or section boundary, test a contiguous **transition boundary** containing enough of both sections to preserve discourse context;
4. for Romance, normally use roughly 200+ reader-visible words when practicable rather than a tiny fragment.

Charge paid repair calls to the genuine section being changed. Do not invent a new section identity merely because the diagnostic boundary includes neighboring context.

## 6. Inspect the ending of the first section and opening of the second

A common cross-section AI shape is:

- section A finishes its real thought;
- the model adds a generalized synthesis, responsibility statement, balanced takeaway, or explanatory aftercare;
- section B opens with another explanation or category setup.

Each section may look acceptable alone, but together they produce a long explanatory run with no live change in pressure.

Before rewriting section B, ask whether section A simply needs to stop earlier. Likewise, a heading may already perform the categorization that the first paragraph repeats.

## 7. Delete duplicate miniature arguments before humanizing them

If a stubborn paragraph restates a point already established elsewhere in the article, do not keep rewriting the duplicate container.

Locate the strongest existing realization. Preserve any genuinely new local function, then delete or route the duplicate.

In Romance Part 1, a repeated `spiritual depth/meditation does not tell me how someone behaves in real relationship conflict` thought remained detector-hostile inside a later flaws section. The article had already made that point earlier through lived evidence. Removing the duplicate miniature argument and letting the personal idealization line be the stopping point produced a 100% Human local section and helped clear the complete Part 1 boundary.

The lesson is functional de-duplication, not `deletion is Human`.

## 8. Let the next lived example perform the conclusion

Before keeping a summary sentence, inspect what comes immediately after it.

If the next anecdote or lived consequence already demonstrates the complication, delete the abstract preview/recap unless it performs a separate necessary function.

In Romance Part 1, the abstract `the first night isn't necessarily the final ceiling` line was followed immediately by the Bee story showing exactly how sexual fit changed over time. The story was the conclusion; the abstract sentence was model aftercare.

## 9. Local Human results do not compose automatically

A complete natural section can measure 100% Human and still participate in a red article/half boundary because of adjacent context. Conversely, an aggregate can improve while one short local window remains noisy.

Keep these evidence levels separate:

- sentence/window localization;
- natural-section diagnostic;
- transition diagnostic;
- aggregate certification.

Section scores are not mathematically composable into an article score. After accepted local repairs, always certify the exact intended aggregate boundary when the task requires it.

## 10. Do not hill-climb partial aggregate percentages

Detector optimization is nonlinear. A locally correct editorial change can make the next aggregate percentage temporarily worse while moving the architecture toward a later complete pass.

Do not retain an inferior thought architecture merely because an intermediate aggregate measured 99.2% while a better architecture measured 98.1%.

Choose edits by:

1. semantic sanity;
2. owner fidelity/provenance;
3. article architecture and live thought;
4. natural-section evidence;
5. aggregate detector result.

Use the aggregate score to localize remaining work, not as a gradient that overrides the first four.

## 11. Recovery and paid-call safety

Result-file visibility is not paid-call authority. Before any recovery POST:

- inspect the durable call ledger;
- inspect exact text SHA reservations/cache;
- resume pending tasks rather than resubmitting;
- never create a new measurement key merely because a result wrapper is not yet visible.

The Pangram harness should block same-audit/same-section exact-text duplicates across measurement keys unless an intentional repeat is explicitly preregistered.

## Required repair check

When a detector residual appears, answer before drafting:

1. What natural section owns this thought?
2. Is the highlighted location actually where the last substantive edit occurred?
3. Is there a higher-authority or already-passing realization to restore?
4. Is the section repeating an argument already made elsewhere?
5. Does the prior section end with unnecessary synthesis/aftercare?
6. Does the next lived example already perform the conclusion?
7. Is the real unit a cross-section transition rather than either short window alone?
8. Did a stronger architecture expose prose that was previously masked rather than genuinely sound?
9. Am I choosing this edit because it is better prose, or merely because the last aggregate percentage was higher?

If these questions expose a larger causal/architectural issue, repair that before changing local vocabulary.
