# Somatic activation-steering bounded sweep — mechanical report

Status: **COMPLETE / AWAITING BLINDED CHAT EDITORIAL EVALUATION**  
Experiment: `SOMATIC-ACTIVATION-STEERING-20260902-A`  
Pangram: **not run**  
Article authority: **unchanged**

## Fixed runtime

- `Qwen/Qwen2.5-0.5B-Instruct`
- Hugging Face revision `7ae557604adf67be50417f59c2c2f167def9a775`
- `Qwen2ForCausalLM`, 24 blocks, hidden size 896, 494,032,768 parameters
- model weights SHA-256 `fdf756fa7fcbe7404d5c60e26bff1a0c8b8aa1f72ced49e7dd0210fe288fb7fe`
- CPU float32; PyTorch `2.7.1+cpu`; Transformers `4.48.3`; Python `3.12.3`
- repository HEAD before experiment changes: `dc0c5fee19b175a63393ea55ec31bed45086a2bf`

No second model or model family was used.

## Exact design executed

- six training contrastive pairs and two calibration-only pairs;
- response-token mean pooling at every one of the 24 post-block residual streams;
- direction per layer: mean of training-pair `positive - negative` activations;
- primary sweep layers: 6, 12, 18 (zero-based);
- alphas: `-1, -0.5, 0, 0.25, 0.5, 1, 2`, with one deduplicated zero baseline per prompt;
- held-out fragments: `afterward`, `words come late`, `the story is already understood`;
- random Gaussian matched-L2-norm control at layer 12, alpha `-1` and `+1`;
- 63 exact blinded candidates total.

Protocol amendment A1 changed only no-cache full-prefix recomputation to paired-row KV-cached decoding after the first baseline proved operationally too slow. The first attempt was interrupted before a candidate completed; no partial candidate was inspected or retained. Model, data, prompt, seed, length, grid, intervention, and blinding stayed fixed.

## Deterministic gates

- tuple-preserving hook unit test: PASS;
- alpha-zero tensor identity unit test: PASS;
- sign-reversal unit test: PASS;
- actual-model alpha-zero logits: bit-identical, max absolute delta `0.0`;
- actual-model alpha-zero full 64-token generation: token IDs and exact text identical to unsteered H01 baseline;
- actual-model sign reversal at layer 12: projection delta `-3.2126834393` versus `+3.2126824856`;
- exact 63-condition grid: PASS;
- 63 candidate text hashes: PASS;
- 63 unique opaque IDs: PASS;
- blinded packet/raw-result identity: PASS.

## Causal telemetry summary

The direction generalized to the two calibration pairs at every swept layer. Mean positive-minus-negative calibration projection gaps were:

- layer 6: `+1.576171`;
- layer 12: `+2.694783`;
- layer 18: `+3.919623`.

Injection produced the predeclared signed projection response. Projection-displacement slopes versus alpha equaled the raw vector norm to numerical tolerance:

- layer 6: `2.344839`;
- layer 12: `3.212683`;
- layer 18: `5.692874`.

Mean same-prefix KL divergence rose with absolute alpha at every layer. For example, at layer 12 it increased from approximately `0.01463` at alpha `+0.25` to `0.24758` at `+1` and `0.86836` at `+2`. The corresponding mean top-token-change fractions were `0.03938`, `0.27083`, and `0.45584`.

At the same layer-12 L2 norm and alpha magnitude 1, the learned direction's mean KL across both signs/prompts was `0.22749`, versus `0.09283` for the random matched-norm control. Mean top-token-change fraction was `0.25` for the learned direction versus `0.12178` for the random control. The random control was not null—it also perturbed logits and texts—so editorial directionality cannot be inferred from generic change alone.

Mechanical conclusion: the learned contrastive vector is real in the pinned model, generalizes in projection to calibration pairs, and causes signed, strength-dependent internal and token-distribution changes beyond the alpha-zero baseline. Whether any positive-alpha text actually moves away from the Somatic mini-essay/semantic-orbit/closure attractor is deliberately unresolved pending blinded Chat reading. Codex makes no prose-human PASS/FAIL claim.

## Durable artifacts

- `run-20260902-a/RUN-MANIFEST.json` — hash manifest for all outputs
- `run-20260902-a/RUNTIME-MANIFEST.json` — pinned runtime and weight identity
- `run-20260902-a/DIRECTION-METADATA.json` and `vectors.npz` — vector derivation/calibration
- `run-20260902-a/RAW-RESULTS.jsonl` — exact candidates, conditions, and per-token telemetry
- `run-20260902-a/ANALYSIS.json` — non-editorial aggregates
- `run-20260902-a/CONDITION-MAP.json` — sealed condition mapping; withhold during cold evaluation
- `run-20260902-a/BLINDED-EVALUATION-PACKET.md` / `.json` — evaluator inputs
- `run-20260902-a/BLINDED-OUTCOME-TABLE.csv` — blinded mechanical outcome table
- `run-20260902-a/SMOKE-RESULTS.json` and `VERIFICATION.json` — deterministic gates

Blinded packet SHA-256: `6405dc1a43c63f0d3c7df1d9d34e6426c6769d7179a780d59b65377cac770313`.

## Repository validation

- experiment output verifier: PASS (63/63 hashes and exact grid);
- fail-closed control-state validator: PASS;
- Somatic task preflight: PASS;
- repository unit suite: PASS (149 tests);
- content-repository structure gate: PASS;
- repository audit: zero errors; four pre-existing repository-policy warnings (default-branch rules disabled, secret scanning and push protection unverified, and no declared public-repository license).

The concurrent owner-teaching-trajectory lane was preserved unchanged at `READY_FOR_OWNER_DISCOVERY_EPISODE_001`; no discovery candidate was generated or interpreted in this run.

## Stop boundary

Stop after durability/validation. Do not reveal `CONDITION-MAP.json` to the evaluator before frozen verdicts. Do not run Pangram, edit/promote the article, change models, or launch a follow-up sweep without a later current Chat/owner instruction.
