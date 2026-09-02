# Owner Correction — Recover the Attractor Experiments Before More Generation — 2026-09-02

Status: ACTIVE direct-owner correction. This supersedes any implication that an alternate-model tournament is an acceptable next strategy.

## Owner correction

Joel states that he had already rejected a model tournament because he had tried that approach before and it did not work. Do not resume or extend alternate-model comparison as the primary Somatic humanization strategy.

Joel asks instead to recover and explain the earlier research-derived experiments aimed at escaping or diagnosing the model/training-distribution attractor. He specifically says those experiments were never explained to him concretely enough to understand how they would work.

## Required distinction before any new experiment

Do not collapse these separate mechanisms:

1. **Process/context isolation (including n8n):** tests whether workflow/context leakage suppresses rare alternative samples. This can change information routing around a model but cannot directly change model weights, hidden activations, logits, decoding objective, or learned continuation probabilities.
2. **Structural out-of-distribution text transformation (ELOQUENT-style):** changes the generated text's register/form/discourse distribution to probe detector blind directions. This is primarily a detector-distribution experiment and is not, by itself, an intervention on the generator's internal learned attractor.
3. **Activation/representation steering:** requires an open/interceptable model runtime. It changes internal residual-stream/hidden-state activations during inference using a learned or contrastive steering direction, then measures whether generation causally shifts away from the unwanted continuation basin. This is the mechanism most directly aimed at changing the generator's internal trajectory without retraining weights.

## Current evidence boundary

Historical working-context recovery indicates that the n8n isolation comparison and activation-steering idea were designed but the semantic-attractor candidate-generation/steering experiment did not actually run. Activation steering remained blocked on access to an open/interceptable runtime exposing hidden activations or logits.

The prior ELOQUENT-derived structural-OOD design must be treated as historical research context until reconciled into GitHub; do not infer that its Pangram transfer pilot completed merely because a design exists elsewhere.

## Immediate next action

Chat must explain the recovered mechanisms and exact experimental designs to Joel before authorizing another candidate-generation lane.

Until Joel chooses the next experiment:

- no model tournament;
- no new Somatic candidate generation;
- no Pangram call;
- no registered-master edit;
- no prompt-architecture expansion;
- no n8n/Hermes experiment by inference.

GitHub remains canonical for durable article/task state; historical File Library/chat artifacts are recovery evidence only until reconciled.