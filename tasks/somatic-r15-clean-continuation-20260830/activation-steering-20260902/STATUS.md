# Somatic activation-steering checkpoint

Updated: 2026-09-02  
Status: `FIRST_SWEEP_COMPLETE_BLIND_VERDICTS_FROZEN_POST_UNBLIND_ANALYSIS_COMPLETE`

The owner selected the direct internal-attractor experiment: one fixed open/interceptable model, contrastive residual-stream activation extraction, causal activation addition, sign reversal, matched-norm random control, held-out generation, telemetry, and blinded Chat evaluation.

Frozen design artifacts:

- `PROTOCOL.md`
- `experiment_config.json`
- `contrastive_pairs.json`

Completed run artifacts include:

- `run-20260902-a/BLINDED-EVALUATION-PACKET.md`
- `run-20260902-a/COLD-EDITORIAL-OPAQUE-VERDICTS-20260902.md`
- `run-20260902-a/CONDITION-MAP.json`
- `run-20260902-a/ANALYSIS.json`
- `POST-UNBLIND-ANALYSIS-20260902.md`

Hard holds remain: no registered-master edit, no article promotion, no unrelated Human donor prose, and no inference that this Qwen 0.5B result transfers to ChatGPT or another runtime. Pangram remains unjustified for sweep A because no candidate cleared the editorial gate.

## Frozen editorial outcome

All 63 opaque candidates were evaluated before the condition map was consulted:

- PASS: `0 / 63`
- UNCERTAIN: `0 / 63`
- FAIL: `63 / 63`

No candidate is Pangram-eligible or article-eligible from this run.

## Mechanical result

The intervention is causally operative rather than null:

- alpha-zero logits and full sampled baseline were exactly identical;
- sign reversal moved residual projection in opposite directions;
- intervention strength produced dose-dependent internal/output displacement;
- the learned direction produced meaningful behavior change relative to a matched-norm random control.

## Post-unblind interpretation

The learned direction is real but entangled.

Across all three held-out prompts and all three swept layers:

- all nine contrastive `alpha = -1.0` conditions failed toward abstract/grandiose/textbook/pseudo-clinical/decorative realization;
- all nine contrastive `alpha = +2.0` conditions failed toward excessive compression, semantic crudity, irrelevance, generic advice, tautology, or degeneration;
- moderate positive steering sometimes reduced ornament and explanatory completion, but did not supply distinctive live human thought movement.

The strongest conclusion is therefore not `steering failed`, nor `more positive alpha is better`. Sweep A found a causal component of the unwanted abstract/explanatory attractor, but subtracting that component is insufficient to generate human prose. The desired writing region is not a one-dimensional endpoint on this vector.

See `POST-UNBLIND-ANALYSIS-20260902.md` for the exact condition-aware interpretation and next-experiment constraints.

## Runtime feasibility note

An initial no-cache attempt was stopped during the first baseline before a candidate completed because full-prefix recomputation implied a many-hour run. Protocol amendment A1 switched only the execution path to paired-row KV-cached decoding; no partial candidate was inspected or retained, and the fixed model/data/grid/prompts/seeds remained unchanged.

## Next action

Do not automatically run a wider alpha sweep, another model tournament, or a Pangram batch.

Two distinct follow-up paths are now separated:

1. **Representation-engineering follow-up, only if later authorized:** disentangle the contrastive vector with more tightly matched/factorial pairs, then preregister a narrow moderate-positive test.
2. **Owner-teaching trajectory experiment:** the current Romance/Somatic comparison makes this the more immediately relevant hypothesis to test. Use the natural discovery/replay design in `../OWNER-TEACHING-TRAJECTORY-ESCAPE-EXPERIMENT-20260902.md` to determine whether Joel's ordered corrections induce a reproducible transient in-context writing state rather than a lucky sample or a bag of explicit rules.

The manual Joel↔Chat route remains the current owner-directed Somatic writing route on `main`; the trajectory experiment is meant to measure that phenomenon without replacing natural teaching with experiment bookkeeping.
