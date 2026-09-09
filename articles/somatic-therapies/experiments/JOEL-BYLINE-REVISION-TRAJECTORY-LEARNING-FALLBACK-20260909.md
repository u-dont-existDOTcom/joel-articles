# Joel-byline humanization fallback — learn from revision trajectories, not finished prose alone — 2026-09-09

Status: **POST-PROMPTING FALLBACK DESIGN / EXPERIMENTAL / NOT ARTICLE PROSE / NOT YET PROMOTED PROJECT-WIDE / NO PANGRAM AUTHORIZATION**

Trigger strategy:
`SOMATIC-HUMANIZATION-STRATEGY-V3-ROUTER-AND-OWNER-COGNITION-20260909.md`

Independent-generation test:
`SOMATIC-DYNAMIC-THOUGHT-ORIGINATION-ABC-TEST-PACKET-20260909.md`

## Decision

If dynamic thought origination or Route-1/2 realization repeatedly fails in the same way, stop adding prompt prohibitions. The next materially different architecture should **learn from Joel's correction trajectories**.

Do not begin with `fine-tune on Joel's finished prose` and do not begin with detector-label optimization.

The highest-information data already being produced are trajectories such as:

`authorial/source context -> model candidate -> Joel rejection/correction -> accepted/revised realization`

Those trajectories reveal the transformation the system must learn: what the model did with a valid thought, exactly what Joel rejected, what judgment the correction protected, and what changed in the accepted output.

## Existing-work scan

A bounded academic scan was performed before adopting this fallback.

### Established work that overlaps

1. **PEER: A Collaborative Language Model** trains from edit histories and models writing/editing/explaining edits/planning as collaborative operations. This is strong precedent for treating revision histories as training data rather than learning only from terminal documents.
2. **Learning to Revise with a Critic** separates criticism from revision and trains those capabilities rather than assuming prompted self-critique will self-correct reliably.
3. **Second Thoughts are Best: Learning to Re-Align With User Feedback** trains on sequential edit history and reports improved ability to incorporate user corrections. This is directly adjacent to Joel's repeated correction trajectories.
4. Work on **feedback-driven SFT** and **natural-language-feedback alignment** shows that critique/rewrite data can improve revision behavior, including in relatively data-efficient regimes in some tasks. These results are task-dependent and do not establish a sample threshold for Joel-byline writing.
5. Fine-grained feedback/preference research supports retaining localized human feedback rather than collapsing every judgment into one scalar preference.
6. Preference-optimization literature also supplies a warning: reward/preference optimization can overfit the proxy or depend strongly on the quality/distribution of preference data. Therefore detector scores and coarse binary accept/reject labels should not be the first or only learning target.

### Explicit disposition

- **Reuse:** edit-history learning, critic/reviser separation, supervised feedback conditioning, held-out evaluation.
- **Adapt:** encode Joel's owner corrections as revision trajectories with preservation/provenance metadata.
- **Compose:** route different failure stages to retrieval, selection, revision, or generation models rather than fine-tuning one monolithic writer.
- **Do not start with:** DPO-only preference learning, Pangram-as-reward, or terminal-prose imitation.

This is an adaptation/composition of established methods, not a claim of a novel ML architecture.

## Why finished-prose fine-tuning is a weak first move

Finished prose tells the model what Joel wrote. It often does **not** tell the model:

- which model default Joel objected to;
- what the rejected candidate was trying to do;
- whether the problem was cognition, placement, provenance, cadence, or overcompletion;
- what was intentionally left out;
- which exact owner correction changed the judgment;
- which model prose was accepted despite differing from natural owner syntax;
- whether a Human detector result came from owner substitution rather than generator improvement.

A trajectory contains these contrasts directly.

## Required trajectory schema

Store examples at the natural-boundary or bounded-edit level. Do not atomize every sentence merely because it is easy to label.

Minimum fields:

```text
trajectory_id
article_id
section_id / exact boundary
source_revision / hashes
input_context_identity
source_thought_or_function
source_provenance
owner_thought_topology_available: yes/no/partial
model_candidate_exact
candidate_origin_model/method
owner_feedback_exact
owner_feedback_interpretation
owner_corrected_or_accepted_text_exact
accepted_status
operation: rewrite/move/delete/consolidate/insert/stop
failure_stage
failure_tags
preservation_status
unexplained_delta_count
detector_evidence_exact_boundary_or_none
generator_contribution
owner_contribution
retrieved_source_contribution
notes_on_what_must_not_be_learned
```

### Failure-stage labels

At minimum:

- `THOUGHT_ORIGINATION`
- `ROUTE_SELECTION`
- `REALIZATION`
- `PLACEMENT`
- `PROVENANCE`
- `SEMANTIC_FIDELITY`
- `OVERCOMPLETION_STOPPING`
- `TECHNICAL_GENRE_MISCLASSIFICATION`
- `EMPTY_SCAFFOLD`
- `DETECTOR_BOUNDARY_ONLY_OR_UNRESOLVED`

### Useful failure tags

Examples already earned by current evidence:

- preservation-unit serialization;
- owner-thought atomization;
- nested enumeration;
- compact program shape;
- significance staging;
- source-type reset;
- invented first-person/autobiography;
- forced subsection completeness;
- objection completion;
- explanatory aftercare;
- equalized thought duration;
- procedural staircase;
- actor/provenance drift;
- research diary leakage;
- false placement/heading pressure.

Tags are diagnostic metadata, not a prompt blacklist.

## Staged fallback architecture

### Stage 1 — retrieval-only case-based assistance

Before parameter training, test whether the revision corpus itself can improve decisions through retrieval.

Given an unresolved span:

1. classify the failure stage;
2. retrieve 1–3 structurally analogous correction trajectories based on failure relation, not topic words;
3. expose the current worker to the **abstract correction relation** and exact owner judgment only where source integrity permits;
4. do not transplant unrelated Human prose into the article;
5. generate the current span from its own source thought.

Example retrieval target:

`owner supplied irregular sequence -> model split into modality cards -> owner rejected topology -> accepted realization preserved asymmetry`

The retrieval target is the transformation lesson, not Hale's wording.

Why first: this is cheap, reversible, interpretable, and tests whether the stored corrections contain enough information before training parameters.

### Stage 2 — learned selector / reranker

If the independent A/B/C test shows multiple seed candidates include good thoughts but the selector routinely chooses polished generic ones, do not train the writer yet.

Train or calibrate a selector on Joel preference/correction data to rank:

- thought seeds;
- route choices;
- stopping decisions;
- alternative bounded realizations.

Primary labels should come from Joel judgments or accepted correction trajectories. Pangram may be recorded as secondary evaluation metadata but should not be the optimization target at this stage.

### Stage 3 — learned reviser/editor

If thought seeds/routes are sound but local writers repeatedly convert them into mini-essays, lists, aftercare, or source-type cards, train the **reviser**, not the originator.

Preferred supervised form:

```text
INPUT:
- literal source/current context
- model draft
- owner critique or compact learned critique representation
- preservation/provenance locks

TARGET:
- owner-corrected or owner-accepted revised boundary
```

Where Joel directly rewrote only part of the candidate, preserve exact delta boundaries so the model learns minimum edit dose rather than whole-boundary regeneration.

The reviser must never infer deletion authority from style preference. Preservation/authorized-delta validation remains an external gate.

### Stage 4 — optional preference optimization after supervised revision

Only after a supervised/retrieval baseline exists and enough matched pairs are available, evaluate preference optimization on **meaning-matched** alternatives.

A useful pair should hold approximately fixed:

- substantive claim/function;
- provenance/actor assignment;
- factual content;
- required evidence/safety;
- natural boundary.

Then preference can target realization differences.

Do not use pairs where the preferred text simply contains more owner cognition or where the rejected text lost a claim; that would confound style/realization with content authority.

Do not train directly on `Pangram Human > Pangram AI` as a preference relation. That creates detector gaming risk and collapses editorial quality, authorship signal, and classifier behavior.

### Stage 5 — thought-seed/origination adaptation only if seed-stage failure remains

If A/B/C shows that independent seeds themselves are generic complete mini-theses, a post-editor cannot solve the missing cognition without becoming a generator.

Only then train or retrieve for **thought origination**.

Possible target data:

- bare topic/context;
- model's generic seed;
- Joel's better substantive angle or correction when he supplied one;
- reason the original angle was generic/wrong;
- accepted thought seed stripped of publication syntax where possible.

This must remain separate from production owner-thought realization. A model trained on Joel's ideas may become better at predicting Joel, but that is not evidence of independent cognition in the stronger sense.

## Failure-stage router after the A/B/C experiment

### Case A — all independent seeds are generic mini-theses

Bottleneck: `THOUGHT_ORIGINATION`.

Next move:
- diversified-seed ablation if not already run;
- retrieval/learned seed generator;
- do not waste effort on paragraph humanization.

### Case B — seed pool contains good seeds, selector chooses bad one

Bottleneck: `ROUTE_SELECTION`.

Next move:
- improve/train selector or use owner choice;
- keep writer unchanged for the discriminating test.

### Case C — selected seed is strong, writer turns it into a complete model essay

Bottleneck: `REALIZATION`.

Next move:
- revision-trajectory retrieval;
- learned reviser/editor;
- do not add another dozen generation bans.

### Case D — local movements are good but assembly becomes regular/complete

Bottleneck: dynamic continuation/assembly.

Next move:
- train/evaluate stopping/continuation selection separately;
- inspect whether repeated fresh contexts are independently choosing the same closure prior;
- use trajectory examples specifically containing owner `stop here / don't explain this` corrections.

### Case E — production owner-thought spans still fail despite faithful route preservation

Bottleneck: likely realization/idiosyncratic style signal or a narrower false hypothesis.

Next move:
- learned reviser and idiolect-retention evaluation;
- consider topology-vs-surface ablation;
- do not claim owner topology alone solves humanization.

## Evaluation design

### Primary test is held-out owner judgment / editorial fidelity

For production:
- does Joel prefer/accept the output as faithful article prose?
- did preservation/source/architecture gates pass?
- did the model require less owner rewriting on held-out boundaries?

For independent generation:
- does the system improve thought topology and prose shape on topics absent from training?
- can it do so without retrieving/copying Joel's substantive ideas?

### Holdout discipline

Avoid random sentence splits. They leak passage architecture and vocabulary.

Prefer increasingly strict holdouts:

1. whole natural boundary held out;
2. whole section held out;
3. topic/failure-instance held out;
4. cross-article evaluation when enough Romance/Somatic examples exist;
5. future article/domain holdout for the strongest generalization claim.

Near-duplicate revisions of the same passage must remain in one split.

### Multi-axis scoring

Keep separate:

1. semantic/preservation fidelity;
2. Joel owner preference/acceptance;
3. failure-tag recurrence;
4. thought-topology quality;
5. idiolect-retention measure where applicable;
6. Pangram exact-boundary result only when explicitly authorized;
7. amount of direct owner content in the candidate;
8. amount of owner correction still required.

A system that gets Pangram Human by copying owner text or deleting difficult claims has not improved the generator.

## Data contamination and source-integrity safeguards

- Never use unrelated Human article prose as a production insertion source merely because it appears in the training/retrieval corpus.
- For retrieval, separate `lesson representation` from `prose donor` explicitly.
- Do not retrieve exact owner prose from the same held-out boundary.
- Keep detector experiments and synthetic probes tagged as such; do not let them become publication authority.
- Keep the retracted aquatic split record excluded from training labels and evaluation claims.
- Preserve owner correction chronology; later corrections/retractions supersede earlier local feedback.
- Do not convert an owner edit into a generic rule until multiple cases justify promotion.

## Minimum useful dataset before parameter training

Do not invent a universal sample threshold from adjacent research.

Instead measure the current corpus:

- count trajectories by failure stage;
- count independent natural boundaries;
- count direct owner rewrites versus mere accept/reject labels;
- count articles/domains represented;
- identify near-duplicate revision chains;
- estimate how many examples survive strict held-out splitting.

If the corpus is sparse for a failure stage, retrieval/case-based assistance is preferable to a brittle fine-tune.

## Cheap implementation order

1. Build the trajectory ledger from already existing GitHub evidence. No prose generation required.
2. Run data-quality audit and exclusion list.
3. Establish retrieval-only baseline on held-out corrections.
4. Run V2 A/B/C independent-generation experiment separately when genuine fresh contexts are available.
5. Route failures by stage.
6. Train a selector or reviser only where the evidence says the bottleneck lives.
7. Compare against retrieval-only and ordinary prompting baselines.
8. Consider preference optimization only if supervised/retrieval methods leave a stable realization preference gap.

## Stop conditions

Stop or change architecture when:

- training improves detector score but worsens owner preference/fidelity;
- held-out performance collapses when same-passage revision chains are kept together;
- retrieval works as well as parameter training;
- the learned reviser starts changing claims/provenance not criticized by Joel;
- the selector learns to prefer generic polished prose;
- failure tags migrate rather than decline;
- owner correction burden stays flat despite local benchmark gains.

## Current recommendation

Do **not** train anything yet.

First use the V3 production router to finish/review Somatic spans and continue collecting high-information correction trajectories. Run the already-designed fresh-context A/B/C experiment when true isolation is available. In parallel, build the trajectory ledger from existing GitHub history so the fallback is ready if dynamic prompting fails.

No Pangram call is authorized or required by this design.
