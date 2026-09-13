# Romance Part 1 — nonlinear localization / rollback lesson — 2026-08-21

Status: **task evidence + reusable editorial/detector lesson candidate.** Canonical Romance `main` remains unchanged.

## Incident

During the Part 1 repair, the complete `Can Casual Sex or a Situationship Actually Be Honest?` natural section reached Pangram 4.0 **100% Human** on its third section-scoped measurement:

- section id: `part1-casual-sex-situationship`
- text SHA-256: `268165f899b11e7e56bffa18d80006d0b322c432a3a409195fe69e407f85061c`
- word count: 796
- Human `1.0`, AI `0.0`, assisted `0.0`.

A later aggregate Part 1 candidate changed a downstream STI/attachment realization inside that section from the registered wording:

`The STI part is easy: say what you know, or say you don’t know. Feelings aren’t. ...`

to a cleaner assistant realization:

`You can test for STIs and tell each other what you know. Attachment is less cooperative. ...`

The later Part 1 aggregate reached Human `0.992400050163269`, but its two residual AI windows were localized **earlier** in the Casual opening around `Your body doesn’t know...`, oxytocin/vasopressin, the first casual-sex disclosure, and `That may be candid...` rather than around the changed STI paragraph itself.

Restoring the registered STI wording recreated the exact previously 100%-Human Casual section, yet the next aggregate moved to Human `0.9838229417800903`; its one AI window expanded across the end of `Affection and the simmer` and the same Casual opening.

Therefore the detector's highlighted location did not identify a single causal sentence. The section is locally Human, but its interaction with the preceding section changes the aggregate classification.

## Reusable lesson

### Detector localization is not causal localization

A red Pangram window says where the classifier expresses uncertainty/AI evidence on that submitted boundary. It does **not** prove that the sentence responsible for the regression is inside that displayed window.

When a later edit causes a previously green section or aggregate region to regress:

1. compare exact text identities before rewriting the highlighted span;
2. identify edits made since the last known-passing local realization;
3. restore the smallest higher-authority / known-passing realization first when editorially valid;
4. only then test whether the residual is truly local or an interaction with adjacent context.

This is especially important because Pangram behavior is contextual and nonlinear. A downstream realization can change segmentation/classification upstream, and two individually Human sections can create an AI-shaped transition when placed together.

### Rollback is a first-class repair operation

Do not assume the next repair must generate new prose. If an assistant `cleanup` replaced owner/registered wording after the natural section had already passed, restore that known-good wording before spending another local-section call.

Rollback is preferable when it:

- increases owner-authority fidelity;
- recreates a previously measured passing natural section;
- removes an unnecessary assistant intervention;
- preserves all article functions and claims.

### Test transition interactions at a meaningful boundary

When the remaining aggregate window crosses a heading boundary, do not keep testing 50–100 word fragments from either side. Use a contiguous ~200+ word boundary containing the end of the first natural section and the start of the next, while charging the repair to the section actually being changed. This follows Joel's short-boundary correction and tests the discourse transition Pangram is actually seeing.

## Current Part 1 evidence sequence

- registered Part 1: Human `0.9205247164`, 10,236 words.
- aggregate repair r2: Human `0.9847978949546814`.
- aggregate repair r3: Human `0.980210542678833`.
- aggregate repair r4: Human `0.992400050163269`, two residual Casual-opening windows.
- aggregate repair r5 after restoring the known-passing Casual STI realization: Human `0.9838229417800903`, one 156-word AI window crossing `Affection and the simmer` → `Casual Sex`.

Current exact r5 Part 1:

- SHA-256 `e6b9e546bb2f07af8e18fc65fb6883d27bf0106d93f5f02d6674a88e034d572d`
- 9,910 words.

The next diagnostic is a 274-word transition boundary charged as the sixth/final `part1-affection-simmer` section call. It shortens Affection to the two thoughts it actually needs and then includes the unchanged Casual opening as context. Do not submit a seventh Affection call.

## Relationship to existing lessons

This strengthens, rather than replaces:

- natural sections over tiny detector windows;
- architecture/container repair before lexical paraphrase;
- exact owner-authority rollback after detector passes;
- ~200+ word contextual diagnostics for short Romance passages;
- cache/reservation recovery before any repeat;
- human/editorial quality and fidelity over detector optimization.
