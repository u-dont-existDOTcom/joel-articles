# Somatic activation/representation-steering experiment — frozen protocol

Status: **FROZEN BEFORE MODEL EXECUTION**  
Experiment ID: `SOMATIC-ACTIVATION-STEERING-20260902-A`  
Authority: non-authoritative mechanism experiment; never article prose authority  
Owner authorization: current Chat instruction, 2026-09-02

Protocol amendment A1, recorded before any candidate completed: the initial full-prefix/no-cache implementation made one 64-token baseline take several minutes on the inspected two-core CPU, implying a many-hour sweep. The run was interrupted during Candidate 1; no partial candidate text was inspected, retained, or entered into analysis. Generation now uses the model's native KV cache with a paired identical-text batch. Batch row 0 remains unsteered and batch row 1 receives/accumulates the intervention; both rows receive the same sampled token, so every next-token comparison remains on the same literal prefix. This changes execution efficiency, not model, data, prompt, decoding seed/settings, intervention layer/strength, condition grid, or blinding.

## Boundaries

This experiment tests one causal question on one fixed open model: does adding a contrastively derived residual-stream direction change the model's internal trajectory and generated continuations away from the already-observed Somatic mini-essay / semantic-orbit / conceptual-closure side of the contrast?

It does not test prompts, n8n isolation, model families, Pangram, authorship, or article fitness. It does not edit `articles/somatic-therapies/master.html`, promote any candidate, or import unrelated Human donor prose. Chat remains the only prose-human/editorial evaluator. A generated difference is not a PASS.

## Runtime feasibility and fixed model

Pre-run inspection on the execution host found:

- no CUDA GPU;
- 23 GiB total RAM, approximately 9.6 GiB available at inspection;
- 15 GiB swap, approximately 8.4 GiB free;
- 33 GiB free disk;
- 2 physical / 4 logical Intel i5-7200U CPU cores;
- local `orcarouter/Qwen3.8-27B-Uncensored` artifacts only as GGUF and MLX.

The local 27B GGUF cannot expose per-layer PyTorch residual streams. The MLX artifact is not usable on this Linux/Intel host. Downloading or converting full 27B Transformers weights would exceed the safe disk/RAM envelope. Prompting the GGUF is explicitly rejected as fake steering.

The fixed runtime is therefore:

- model: `Qwen/Qwen2.5-0.5B-Instruct`;
- Hugging Face revision: `7ae557604adf67be50417f59c2c2f167def9a775`;
- architecture asserted at runtime: `Qwen2ForCausalLM`;
- model geometry asserted at runtime: 24 decoder blocks, hidden size 896;
- execution: CPU, float32, PyTorch/Transformers, `trust_remote_code=False`;
- decoding: fixed sampling configuration and per-candidate seed from `experiment_config.json`.

The model is the smallest technically adequate fixed instruction model that fits comfortably enough for a multi-condition residual-stream sweep on this host. It can test whether the proposed intervention is mechanically and causally operative in this model. It cannot prove transfer to the historical 27B Qwen runtime, Claude, ChatGPT, or the registered article workflow.

If any asserted identity or geometry differs, the run fails closed. There is no automatic model substitution.

## Public implementation scan and classification

Classification: **ADAPT**.

Reused scientific and implementation patterns:

1. Contrastive Activation Addition (CAA), Panickssery et al., `arXiv:2312.06681`, official code `nrimsky/CAA` at inspected commit `5dabbbd9a0bca5f25e174501e959de378806aa48`: teacher-force paired positive/negative realizations, capture block-output residual activations, compute the per-layer mean of pairwise differences, and add a scaled vector during generation.
2. Representation Engineering, Zou et al., `arXiv:2310.01405`, official code `andyzoujm/representation-engineering` at inspected commit `5455d8a375d5fb1cb191f9ebcd089b7c21e9a31e`: cluster-mean positive-minus-negative directions and tuple-preserving residual control.

Adaptations:

- native Qwen2 decoder-block forward hooks instead of replacing Llama-specific modules;
- response-token mean pooling instead of CAA's Llama-specific penultimate-token choice;
- injection only at the assistant-generation cue and generated-token positions;
- same-prefix unsteered counterfactual logits for per-step KL and top-token deltas;
- deterministic alpha-zero equivalence, sign reversal, random matched-norm control, candidate hashing, and blinded export.

Built locally because the reference packages do not supply it:

- Somatic provenance-safe contrastive data and held-out prompts;
- exact runtime/weight identity manifest;
- causal telemetry and non-editorial dose-response summaries;
- opaque candidate mapping and evaluator packet.

No reference package is vendored. The implementation is small enough to audit directly and retains the reference method's essential causal operation.

## Contrastive data

`contrastive_pairs.json` contains eight matched pairs. Every pair expresses the same Somatic thought/function on both sides:

- `positive`: direct/natural-human-side realization;
- `negative`: recurring model-shaped-attractor-side realization.

The labels describe the experiment contrast, not authorship proof. The material is either a synthetic matched probe derived from current Somatic semantic units or a task-relevant Somatic realization already preserved as detector/mechanism research. It is not publication copy.

Six pairs are training pairs. Two are calibration-only and never contribute to the vector. The three generation prompts are held out entirely:

1. `afterward`
2. `words come late`
3. `the story is already understood`

The third fragment comes from the current Somatic task's bodily-survival-activation / thought-alone-limit unit. None of the three fragments appears in the paired realizations.

## Activation extraction

For each pair and side:

1. Render the fixed system instruction, the pair's fixed shared instruction, and the labeled response with the model's native chat template.
2. Teacher-force the full sequence with `output_hidden_states=True` and no sampling.
3. For every decoder block `l = 0..23`, take the block-output residual stream (`hidden_states[l + 1]`).
4. Select only response tokens after the assistant generation cue; exclude chat-control/special tokens.
5. Mean-pool those response-token activations to obtain `h(side, pair, l)`.
6. Compute `d(pair, l) = h(positive, pair, l) - h(negative, pair, l)`.
7. Compute the raw steering vector `v(l) = mean_training_pairs d(pair, l)`.

No PCA, learned classifier, prompt vector, or weight update is used. Raw vector norms and calibration projections are recorded for all 24 layers. Calibration reports the signed projection gap on the two untouched pairs but does not alter the predeclared sweep.

## Intervention

Sweep layers: decoder block outputs 6, 12, and 18 (zero-based). These sample early-middle, middle, and late-middle depth without post-result layer selection.

Intervention point: `model.model.layers[L]` forward output, after the full transformer block and before block `L+1`. The hook preserves every tuple member other than the first hidden-state tensor.

Token positions affected: the final assistant-generation cue token and every generated-token position in the current full-prefix forward pass. System and user-content positions are never changed. At an affected position:

`residual_post = residual_pre + alpha * v(L)`

Primary alphas:

`[-1.0, -0.5, 0.0, 0.25, 0.5, 1.0, 2.0]`

The zero baseline is stored once per prompt. A zero-valued active hook must be logit- and text-identical to the unhooked run under the same seed/config. Negative alphas supply sign reversal.

Negative control: a deterministic Gaussian random unit vector, generated independently per swept layer and rescaled to exactly match `||v(L)||`. It is tested at layer 12 with alpha `-1.0` and `+1.0` on all held-out prompts.

## Generation and causal telemetry

The fixed generation prompt and decoding settings are in `experiment_config.json`. Generation is manual autoregressive decoding with the pinned model's native KV cache and a two-row paired batch:

1. row 0 carries the unsteered causal state for the exact current text prefix;
2. row 1 carries the steered causal state for that same text prefix;
3. the same sampled token is appended to both rows before the next step.

On the initial prefill the hook changes only the assistant-generation cue position. On cached one-token decoding steps it changes the current generated-token position; prior steered/unsteered states remain separately preserved in their cache rows. This is a stronger accumulated-intervention comparison than recomputing prior generated tokens from scratch and remains literal-prefix matched.

The sampled next token comes only from the steered distribution (or unsteered distribution for baseline). Per step, record:

- projection of the current final-position residual onto the unit steering direction before and after injection;
- actual projection displacement;
- KL divergence `KL(P_steered || P_unsteered)` on the same prefix;
- unsteered and steered top-token IDs/text;
- whether the top token changed;
- sampled token ID;
- affected-position count.

Per candidate, record exact prompt ID, condition, layer, alpha, direction kind, seed, decoding config, generated token IDs, exact text, SHA-256, stop reason, elapsed time, mean/max KL, mean projection displacement, and top-token-change fraction.

## Non-editorial analysis

The analysis may report only mechanical/causal quantities:

- vector norms and calibration projection gaps;
- alpha versus mean projection-displacement slope;
- alpha versus mean KL/top-token-change fraction;
- candidate token/word/sentence counts and hashes;
- exact-text equality/difference relative to baseline;
- random-control comparison.

It must not label any candidate Human, AI, good, bad, natural, publishable, or Pangram-eligible. Dose response means internal/behavioral movement with alpha; it is not an editorial success claim.

## Blinding

Every exact candidate receives an opaque ID derived from a secret-free experiment salt and its condition record. `BLINDED-EVALUATION-PACKET.md` and `.json` contain only opaque ID, held-out prompt label, exact generated text, and a blinded non-editorial telemetry row. Model identity, layer, alpha, direction kind, and condition labels are absent.

The unblinded mapping is stored separately in `CONDITION-MAP.json`. Chat must evaluate the blinded packet before consulting the map.

## Deterministic gates and stopping rule

Before the sweep:

- unit tests for tuple-preserving hooks, alpha-zero identity, sign reversal, hashing, and manifest validation must pass;
- actual-model alpha-zero smoke must match unsteered logits/text exactly;
- actual-model sign reversal must move residual projection in opposite directions;
- model identity and weight-file SHA-256 must be recorded.

After the sweep:

- verify every candidate hash and all manifest references;
- verify all predeclared primary and control conditions exist exactly once;
- generate the blinded packet from the raw manifest, never by hand;
- run repository tests and integrity checks relevant to the task;
- stop after this single bounded sweep.

No Pangram call is authorized. No second model, alternate family, article mutation, candidate promotion, or follow-on sweep begins automatically.
