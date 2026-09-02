# Somatic activation-steering checkpoint

Updated: 2026-09-02  
Status: `BOUNDED_SWEEP_COMPLETE_AWAITING_BLINDED_CHAT_EVALUATION`

The owner has selected the direct internal-attractor experiment: one fixed open/interceptable model, contrastive residual-stream activation extraction, causal activation addition, sign reversal, matched-norm random control, held-out generation, telemetry, and blinded Chat evaluation.

Frozen artifacts:

- `PROTOCOL.md`
- `experiment_config.json`
- `contrastive_pairs.json`

Hard holds remain: no Pangram, no model tournament or silent substitution, no registered-master edit, no article promotion, no unrelated Human donor prose, and no Codex editorial PASS/FAIL.

Completed outcome: one fixed-model sweep produced 63 exact candidates, raw per-token causal telemetry, a matched-norm random control, an unblinded condition map, and a verified blinded evaluator packet. Alpha-zero logits and the full 64-token sampled baseline were exactly identical; sign reversal moved projection in opposite directions. `run-20260902-a/VERIFICATION.json` is PASS.

Runtime feasibility note: an initial no-cache attempt was stopped during the first baseline before a candidate completed because full-prefix recomputation implied a many-hour run. Protocol amendment A1 switches only the execution path to paired-row KV-cached decoding; no partial candidate was inspected or retained, and the fixed model/data/grid/prompts/seeds remain unchanged.

Next action: current Chat evaluates `run-20260902-a/BLINDED-EVALUATION-PACKET.md` by opaque ID before consulting `CONDITION-MAP.json`. Codex must not make the final prose-human PASS/FAIL judgment.
