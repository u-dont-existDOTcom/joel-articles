# Joel-byline revision-trajectory retrieval protocol — 2026-09-09

Status: **ACTIVE EXPERIMENTAL RETRIEVAL PROTOCOL / PRODUCTION-SUPERVISOR AID / NOT ARTICLE PROSE / NOT A WRITER PROMPT LIBRARY / NO PANGRAM AUTHORIZATION**

Seed ledger:
`articles/somatic-therapies/experiments/trajectories/JOEL-BYLINE-REVISION-TRAJECTORY-SEED-LEDGER-20260909.json`

Parent strategy:
`articles/somatic-therapies/experiments/SOMATIC-HUMANIZATION-STRATEGY-V3-ROUTER-AND-OWNER-COGNITION-20260909.md`

Fallback design:
`articles/somatic-therapies/experiments/JOEL-BYLINE-REVISION-TRAJECTORY-LEARNING-FALLBACK-20260909.md`

Feasibility audit:
`articles/somatic-therapies/experiments/JOEL-BYLINE-REVISION-TRAJECTORY-CORPUS-FEASIBILITY-AUDIT-20260909.md`

## Recommendation

Use trajectory retrieval as a **supervisor-side routing and strategy aid**, not as additional prose instructions shown wholesale to the writer.

The live failure should first be diagnosed from the current literal span. Then retrieve at most one primary structurally analogous correction trajectory, with one optional counterexample/secondary trajectory only when it discriminates between two plausible failure mechanisms.

The writer should normally receive **none of the historical rejected prose, detector labels, anti-pattern tags, or owner criticism from the retrieved trajectory**. The writer receives only the current span's source thought, literal local context, authorized semantic delta, and whatever positive local relation the supervisor has selected.

This preserves the value of case-based learning without rebuilding the over-constrained rule environment that V3 is trying to escape.

## Why retrieval is supervisor-side

The current evidence shows a widening critic–generator gap: the system can identify increasingly specific failure patterns while generation continues to reproduce deeper model priors. If every retrieved correction becomes another `do not do X` instruction in the writer's context, retrieval simply enlarges the prohibition set.

Therefore separate roles functionally even when the same model performs them in one production context:

- **retrieval/supervision:** diagnose failure stage, compare analogues, select route, decide boundary and stopping policy;
- **writing:** realize the current source thought with minimal historical baggage;
- **audit:** test the literal candidate afterward.

Same-context role separation is **not independent evidence**. This separation is an operational production architecture only. Any claim that retrieval improves generation requires prospective held-out evidence.

## Retrieval target

Retrieve a **transformation relation**, not a similar topic or similar prose sample.

Good retrieval target:

`owner/source functions were correct -> model serialized them into compact program -> owner rejected topology -> next operation should stop consuming inventory and recover one live relation`

Bad retrieval target:

`Yoga is a body practice, massage is a body practice, so retrieve the Yoga paragraph.`

Topic overlap is weak evidence. Failure-stage and thought-architecture overlap control retrieval.

## Step 1 — freeze the live case before retrieval

Before looking at trajectory lessons, record a compact live-case diagnosis from the current literal article/source context.

Required fields:

```text
live_case_id:
article / natural boundary:
current authority/source identity:
V3 route: 0 / 1 / 2 / 3 / 4 / 5
literal problem span or empty slot:
what is already correct/preserved:
observed failure or missing function:
primary suspected failure_stage:
primary evidence for that stage:
strongest competing failure_stage:
what observation would discriminate them:
owner thought topology available: yes / partial / no
operation currently under consideration:
```

Do not encode the desired retrieval result into the diagnosis. In particular, do not call something `owner-thought atomization` merely because the aquatic trajectory is known to contain that label. Describe the live observation first.

## Step 2 — causal/specificity check before retrieval

Ask whether the suspected feature distinguishes the live failure from tolerated/working controls.

Examples:

- `contains a list` is weak because legitimate SIBAM/five-stage lists exist;
- `owner supplied the ideas` is weak because owner-rich Stage-1 attempts still failed;
- `the model reorganized one asymmetric connected thought into equal editorial cards` is stronger because it predicts the rejected massage/aquatic candidate and distinguishes the successful redistributed candidate;
- `there is contrast` is weak; `the sentence supplies an opposite category only to complete conceptual space after the live thought already landed` is stronger.

Down-rank a failure hypothesis when the same feature is common in tolerated controls unless dose/form/mechanism explains selectivity.

## Step 3 — candidate retrieval set

Start from the seed ledger and exclude:

1. the same natural-boundary trajectory as the live case;
2. any source explicitly retracted/quarantined;
3. synthetic probes unless the live task is explicitly generator research;
4. trajectories whose only similarity is topic vocabulary;
5. a detector-only trajectory when the live problem is editorial/semantic and no semantic equivalence was established.

For article production, cross-article trajectories are allowed when the transformation relation is genuinely analogous. They remain process evidence, never prose insertion authority.

## Step 4 — deterministic first-pass scoring

With the current seven-cluster corpus, prefer a transparent deterministic score over embeddings or a trained retriever. The corpus is too small for similarity machinery to earn trust, and embeddings may overweight topic/style words.

Score each eligible trajectory:

- +5 exact primary `failure_stage` match;
- +3 exact secondary/competing `failure_stage` match;
- +3 per genuinely equivalent failure tag **after semantic interpretation**, maximum +6;
- +2 operation-type match (e.g. minimum-dose rewrite, delete scaffold, restore unique function, recover owner topology);
- +2 compatible owner-thought-topology state (`yes`, `partial`, `no`) when that state changes the appropriate intervention;
- +2 same genre/function class when materially relevant (e.g. narrative realization vs technical finite list), not merely same topic;
- +1 cross-article bonus when the analogy survives topic change, because that is stronger evidence of a reusable transformation relation;
- −5 if the apparent similarity depends mainly on topic/entity words;
- −5 if applying its lesson would require importing historical prose or facts;
- exclude entirely if later owner correction/retraction invalidates its lesson.

The numbers are an initial deterministic routing heuristic, **not calibrated weights**. Record score components so later evidence can revise them. Do not tune weights against Pangram outcomes.

## Step 5 — select at most one primary trajectory

Default: retrieve **one** highest-scoring trajectory whose causal relation remains plausible after the specificity check.

Do not expose the top three simply because three are available. Multiple retrieved lessons can recreate the prohibition-stack problem and make it impossible to know which intervention mattered.

Retrieve a second trajectory only for one of two reasons:

1. **disconfirmation/control:** it shares a superficial feature with the live case but had a different disposition, helping prevent an overbroad rule;
2. **mechanism discrimination:** two failure stages remain genuinely plausible and the second trajectory predicts a different next operation.

When a second trajectory is used, state the discriminating observation before acting.

## Step 6 — supervisor extraction envelope

From the selected trajectory expose only:

```text
trajectory_id
why structurally analogous
historical failure_stage
abstract transformation lesson
historical operation that worked / failed
what must NOT be generalized
prediction for the live case
cheapest discriminating test, if still uncertain
```

Do not copy the historical article passage into the production writing context unless it independently passes ordinary source-integrity rules for the live article function.

Detector status is normally withheld from the writer and is unnecessary for production routing.

## Step 7 — choose the live operation before prose

The retrieved case must change or confirm a concrete operation. If it does neither, retrieval added no value and should be ignored.

Possible operations under V3:

- preserve exact / no action;
- recover one owner cognition;
- realize one bounded source relation;
- reduce model architectural freedom;
- split a preservation bank across later destinations;
- minimum-dose rewrite of surviving assistant surface;
- restore a unique function swallowed by consolidation;
- delete/consolidate empty scaffold;
- preserve technical finite structure;
- stop current method and escalate to learned reviser/fresh-context research.

Never translate a retrieved lesson directly into `use different wording` unless the failure is actually realization-only and the semantic route is already sound.

## Step 8 — writer packet

The writer packet should be deliberately smaller than the supervisor context.

Normally include only:

- literal current preceding prose / natural local boundary;
- current source thought or owner cognition needed for this movement;
- exact claims/provenance/certainty that must survive;
- the single intended local relation or live pressure;
- authorized change boundary;
- explicit stop condition if source-derived and necessary;
- necessary genre/safety constraints.

Normally exclude:

- historical trajectory IDs and rejected prose;
- Pangram results;
- long anti-pattern lists;
- every preservation unit not currently reached by the live thought;
- alternative candidate routes rejected by the supervisor;
- explanations of why the prior model failed;
- unrelated Joel voice examples.

The preservation inventory remains available to the **post-generation verifier**, not as a composition outline.

## Step 9 — post-generation receipt

After literal candidate generation, record:

```text
live_case_id:
trajectory_retrieved:
retrieval_score_components:
operation_selected:
writer saw historical lesson: yes/no
candidate identity/hash if durable:
preservation status:
provenance status:
primary predicted failure recurred: yes/no/unclear
new failure appeared:
owner judgment if available:
owner correction burden:
retrieval lesson disposition: supported / null / contradicted / confounded
next strategy:
```

Do not call a retrieval successful merely because the candidate feels better to the same saturated context. Strong evidence requires Joel judgment, a genuinely fresh reader where relevant, or repeated prospective performance across independent boundaries.

## Prospective A/B evaluation

The retrieval system should be evaluated prospectively, not by replaying the same seven examples until it reproduces their known corrections.

### Condition A — router only

Use V3 route classification and current project protocols without retrieving a historical trajectory lesson.

### Condition B — router + retrieval supervisor

Use the same current source/authority, but allow one trajectory retrieval under this protocol before the operation/writer packet is chosen.

### Important isolation rule

A single saturated conversation cannot produce independent A/B candidates after seeing both methods and then call the comparison blinded. For a genuine method comparison, use separate fresh contexts or future independent live boundaries assigned prospectively.

If true parallel isolation is unavailable, use the method prospectively in production and log owner corrections rather than manufacturing a pseudo-experiment.

### Primary outcomes

Rank outcomes in this order:

1. semantic/preservation fidelity;
2. owner judgment/acceptance;
3. recurrence of the predicted failure class;
4. amount of owner rewriting/correction required;
5. provenance/actor/certainty mistakes;
6. unnecessary scaffold/overcompletion;
7. candidate quality from genuinely fresh final-reader audit where required;
8. Pangram only when separately authorized and only as exact-boundary secondary evidence.

The method fails if it improves a detector while worsening any higher-priority production outcome.

## Negative-transfer checks

A retrieved trajectory is harmful when it causes any of the following:

- the writer imitates historical wording or cadence;
- a legitimate finite list is broken because a prior case warned about lists;
- a necessary contrast disappears because another case warned about contrast completion;
- an owner function is deleted because a prior case rewarded compression;
- the current source topology is forced to resemble the retrieved topology;
- the supervisor diagnoses the current problem using the retrieved label instead of the literal evidence;
- multiple trajectory lessons accumulate into another global style rule stack.

Any of these should mark the retrieval `contradicted/negative-transfer` and down-rank that retrieval relation for future use.

## When retrieval should be skipped

Skip trajectory retrieval when:

- Route 0 exact protected/known-green prose has no real editorial defect;
- the operation is straightforward P1 correction;
- the live issue is a factual/citation question rather than humanization architecture;
- owner intent is already explicit and the required edit is mechanically exact;
- no trajectory has a plausible failure-stage/operation relation after specificity checks;
- retrieval would only produce a topic-similar example.

`No useful retrieval` is a valid result and preferable to forced analogy.

## Promotion threshold

Do not promote this protocol project-wide merely because it sounds plausible or retrieves known historical examples correctly.

Promotion requires prospective evidence that, across multiple independent natural boundaries, retrieval supervision materially reduces recurring model-shaped failures or owner correction burden without increasing fidelity/provenance errors.

Until then this remains a Somatic/Joel-byline experimental production aid.

## Immediate next use

For the next genuinely unresolved Somatic humanization boundary:

1. freeze the live case before consulting this seed corpus;
2. route it under V3;
3. retrieve at most one structurally analogous cluster;
4. choose the operation;
5. send the writer a minimal current-source packet, not the retrieved history;
6. log the result prospectively.

Do not rerun or rewrite the exact aquatic Human/medium candidate, the compact tested SE boundary, or another Route-0 boundary merely to test this protocol.

No Pangram call is authorized or required by this protocol.
