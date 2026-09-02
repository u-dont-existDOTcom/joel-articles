# Owner Teaching-Trajectory Escape Experiment — 2026-09-02

Status: ACTIVE DESIGN / READY FOR OWNER DISCOVERY EPISODE. Non-authoritative. This experiment runs in parallel with, but does not modify, the separate activation/representation-steering experiment. It does not authorize registered-master edits, article promotion, Pangram calls, unrelated Human donor prose, or automated generation outside the protocol.

## Owner observation and hypothesis

Joel has observed that during some prior step-by-step teaching conversations, ChatGPT occasionally produced prose that he regarded as genuinely human-looking, even though the same model repeatedly falls back into a recurrent model-shaped completion attractor.

Possible explanations:

1. **Stochastic escape:** a rare good sample happened by chance and the teaching sequence was not causal.
2. **Instruction-content effect:** the accumulated explicit rules mattered, but their order/path did not.
3. **Trajectory/path-dependent in-context effect:** the exact sequence of corrections, examples, challenges, analogies, and local successes induced a transient latent writing mode that a compressed instruction summary does not reproduce.
4. **Evaluator/owner anchoring:** the apparent escape was partly a judgment artifact rather than a generation change.
5. **Prompt/task specificity:** the trajectory worked only for one prompt and did not generalize.

The experiment is designed to distinguish these possibilities rather than assume a conversational `task vector` exists.

## Research motivation — not proof

Mechanistic ICL research motivates the experiment but does not establish that this phenomenon occurs in ChatGPT prose generation:

- Hendel, Geva & Globerson (2023), *In-Context Learning Creates Task Vectors*, report that some ICL tasks can be represented by compact task vectors derived from demonstrations.
- Todd et al. (ICLR 2024), *Function Vectors in Large Language Models*, identify compact causal internal representations of demonstrated functions in several autoregressive transformer models.
- Demonstration-order research shows that ICL behavior and internal prompt representations can depend materially on example ordering.

Important limitation: these results are primarily from open/interceptable models and benchmark tasks. They are not evidence that conversational coaching reliably creates a `human writing` state in ChatGPT. Prior attempts discussed with Joel had limited GPT success. Therefore this protocol treats the hypothesis as uncertain and requires replay/ablation evidence.

## Separation from other attractor experiments

Do not collapse this experiment into:

- **n8n/process isolation** — changes information routing but not the model's internal activations directly;
- **ELOQUENT structural-OOD** — probes output/detector distribution shifts;
- **activation steering** — directly perturbs hidden activations in an open/interceptable model.

This experiment asks whether **natural conversational teaching itself** induces a reproducible transient state. A later mechanistic bridge may test whether an analogous state is visible as an activation direction in an open model.

## Phase A — natural discovery episode

### Purpose

Capture a teaching episode without contaminating Joel's natural coaching behavior with a pre-scripted experimental checklist.

### Setup

1. Use a genuinely fresh ChatGPT learner/writer conversation with the same intended model/configuration whenever possible.
2. Give only the ordinary writing task/semantic boundary needed to begin.
3. Joel teaches naturally, exactly as he would if trying to make the model write better: corrections, objections, analogies, examples, challenges, deletions, `that still sounds AI`, etc.
4. Do **not** inject experiment labels, Pangram scores, prior failure catalogs, hidden evaluator rationales, or a predetermined teaching script into the learner unless Joel himself naturally introduces them.
5. The learner may respond normally. Preserve the exact conversational sequence.

### Freeze event

If Joel judges a candidate as a genuine apparent escape — e.g. `yes, that actually looks human` or equivalent — freeze the episode immediately as a **SUCCESS-CANDIDATE DISCOVERY EPISODE** before further teaching changes the state.

Freeze:

- exact ordered user turns;
- exact ordered assistant turns;
- exact successful candidate text/hash;
- nearest preceding failed candidate text/hash;
- model/config identity if available;
- timestamps/turn ordinals;
- Joel's exact owner judgment;
- whether a separate cold evaluator agrees.

Do not infer causality from this success.

If the session never escapes, preserve it as a failure/control episode; failed trajectories are useful evidence.

## Phase B — post-hoc descriptive tagging

Only after the discovery episode freezes, tag Joel's teaching turns descriptively. Tags are analysis features, not presumed causes.

Suggested tag vocabulary:

- `SEMANTIC_CORRECTION`
- `LITERAL_AI_SHAPE_REJECTION`
- `PROCESS_RULE`
- `POSITIVE_EXAMPLE`
- `NEGATIVE_EXAMPLE`
- `ANALOGY_OR_METAPHOR`
- `ATTRACTOR_AVERSION_CUE`
- `ANTI_PULL_NON_OBEDIENCE`
- `NON_SERIAL_PARALLEL_THOUGHT`
- `MUTATION_RECOMBINATION`
- `DELETE_OVEREXPLANATION`
- `STOP_WITHOUT_CLOSURE`
- `PERSONA_OR_STANCE_INDUCTION`
- `OWNER_CHALLENGE`
- `META_EVALUATION`
- `OTHER`

Multiple tags may apply. Preserve exact turn order and distance from the candidate.

Do not rewrite Joel's turn into a cleaner rule before storing it. The literal trajectory is the experimental object.

## Phase C — baseline

Before attributing success to teaching, obtain a same-task/same-model fresh-chat baseline with no teaching trajectory.

Target baseline: 5 fresh independent candidates if mechanically feasible.

Each candidate receives blinded cold evaluation. Joel judgment may also be recorded separately.

Do not Pangram baseline prose by default.

## Phase D — exact/prefix replay

After a discovery success, replay the trajectory in genuinely fresh conversations.

### D1. Increasing-prefix replay

Replay increasing prefixes of Joel's **exact user teaching turns** followed by the fixed probe task.

Use at least 3 fresh-chat replicates per informative prefix initially. Expand to 5 when a threshold appears plausible.

Two distinct replay modes may be tested and must not be conflated:

1. **Interactive user-turn replay:** replay Joel's exact teaching interventions while the fresh assistant's intermediate responses are allowed to vary naturally.
2. **Transcript-conditioning replay:** where technically feasible, condition on the exact frozen user+assistant transcript prefix before the probe. This tests the full conversational state rather than Joel's interventions alone.

### D2. Threshold localization

Find the earliest trajectory prefix after which cold-PASS frequency materially exceeds baseline.

Never call one turn `the cause` from a single replay.

## Phase E — causal controls

Around any candidate threshold, run:

### E1. Turn ablation

Remove one Joel teaching intervention at a time while preserving the surrounding order. Compare PASS frequency.

### E2. Order control

Use the same teaching turns in a scrambled/permuted order. This distinguishes sequence/path effects from a bag of instructions.

### E3. Compression control

Replace the whole teaching trajectory with a concise summary containing the same explicit rules/lessons.

If the literal trajectory works but the summary does not, that is evidence for path-dependent conditioning rather than merely explicit instruction content.

### E4. Semantic-only control

Provide the same Somatic meaning/task without the teaching trajectory.

### E5. Negative-history control

Where useful, replay a comparable-length sequence of failed corrections that did not precede an escape.

## Phase F — persistence / decay

Immediately after a trajectory condition that appears successful, ask for multiple fresh same-domain outputs **without further coaching**.

Recommended probe positions: first, second, third, and fifth post-teaching generation.

Measure whether the apparent state:

- persists;
- gradually decays;
- disappears immediately;
- strengthens with use;
- is specific to the original prompt.

This directly tests the owner's observation that the model can sometimes `get it` and then later fall back into the attractor.

## Phase G — transfer

Probe at least one held-out Somatic prompt/fragment not used during teaching.

A trajectory that only improves the exact training prompt is not evidence for a general writing mode.

Prefer multiple held-out prompts if the first trajectory appears promising.

## Evaluation separation

### Learner/writer

The learner is never asked to decide whether it escaped.

### Owner

Joel's owner judgment is recorded independently and remains important evidence of whether the output meets the intended writing quality.

### Blinded cold evaluator

A separate evaluator receives only the exact candidate, with condition/trajectory/model-history withheld, and returns:

- `PASS`
- `FAIL`
- `UNCERTAIN`

plus the strongest literal defect when non-PASS.

Do not reveal replay condition until the verdict freezes.

### Pangram

No Pangram by default. A later explicit owner/Chat authorization may test an exact cold-PASS candidate, but detector status cannot define an escape episode.

## Provisional reproducibility criterion

A discovery success becomes a **REPRODUCIBLE TRAJECTORY CANDIDATE** only if there is affirmative replay evidence, not one lucky paragraph.

Initial practical criterion:

- baseline <= 1/5 blinded cold PASSes;
- exact or near-threshold trajectory replay >= 3/5 blinded cold PASSes;
- at least one held-out transfer prompt cold-PASSes;
- no hidden evaluator/Pangram feedback entered the learner before generation.

With small N, report raw counts and uncertainty; do not claim statistical significance from these thresholds alone.

If exact replay does not outperform baseline, classify the original event as `STOCHASTIC_OR_NONREPRODUCIBLE_ESCAPE` rather than inventing a causal explanation.

## Pair analysis

For every success candidate, pair it with:

1. nearest preceding failed candidate in the same discovery conversation;
2. fresh-chat baseline candidates from the same probe;
3. failed/negative teaching trajectories of comparable length when available.

Analyze differences in **trajectory and state**, not only surface vocabulary.

## Bridge to activation steering

If a teaching trajectory reproduces on ChatGPT, a later open-model mechanistic experiment can test a stronger hypothesis:

1. replay the successful teaching trajectory on one fixed open/interceptable model;
2. replay matched failed/control trajectories;
3. at the same target writing prompt, capture hidden activations across layers;
4. test whether successful trajectory conditioning induces a reproducible latent direction/state distinct from controls;
5. test whether injecting that direction without the transcript reproduces the writing effect;
6. compare/compose it with the separate contrastive activation-steering direction.

This would connect the natural conversational phenomenon to representation engineering.

Important: success on an open model would not prove that proprietary ChatGPT uses the identical internal representation.

## Operational rule for future discovery chats

Joel should not have to perform experiment bookkeeping while teaching.

The discovery chat remains natural. Once Joel says an output genuinely escaped, a mechanical observer should freeze/export the exact episode and update this experiment registry afterward.

Do not make Joel teach from this protocol. The protocol is for the observer/researcher, not the teacher.

## Stop conditions

Stop or pause the experiment when:

- Joel says the teaching procedure is becoming artificial because of the experiment;
- model/config identity becomes too ambiguous for replay comparison;
- exact transcript recovery is unavailable;
- the learner receives condition/evaluator leakage;
- repeated exact replays show no lift over baseline;
- owner changes the task.

## Authority boundary

This experiment studies generation behavior only. No discovery/replay candidate is article authority or publication-ready by virtue of success. Normal semantic reconciliation, preservation, owner approval, and article gates remain required before any article use.