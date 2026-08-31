# SUPERVISOR DECISION — SOMATIC HUMANIZATION FRESH REASONING 003

Date: 2026-08-31

Task: `somatic-r15-clean-continuation-20260830`

Disposition: **REVISE_STRATEGY**

Decision ID: `SOMATIC-INTRO-SOURCE-BOUND-NULL-FIRST-001`

Status: **CONTROLLING FOR THE NEXT BOUNDED INTRODUCTION EXPERIMENT**

This decision supersedes, for generation authority, both:

- `FRESH-WRITER-LOW-STRUCTURE-BRIEF-002.md`
- `FRESH-WRITER-LOW-STRUCTURE-BRIEF-002-SUPERVISOR-GATE.md`

Those files remain preserved as rejected-strategy evidence. They must not be sent to another writer.

This decision does not change registered `master.html`, promote an article candidate, authorize a detector call, or establish whole-document completion.

## Direct ruling

The proposed semantic-custodian / fresh-writer / blind-shape-validator architecture contains two useful separations:

1. the writer should not own semantic certification;
2. the evaluator should not see detector history, prior candidates, or the semantic checklist.

Its **generation mechanism is not outside the failed family**. The compressed five-concept brief still gives a complete ordered inventory to an instruction-following model and asks it to realize the inventory as one short coherent exposition. Calling the inventory rough notes and declaring its order irrelevant does not remove the latent coverage plan.

The replacement is not another complete-section generation prompt. It is a source-bound, null-first discourse-operation surgery on the exact four-paragraph `AI_TARGET`.

## 1. Deepest causal diagnosis

The repeated failure is best explained as **coverage-induced discourse planning under one-pass realization**.

The model is not merely paraphrasing sentences. It is solving a constrained coverage problem:

1. turn the supplied semantic units into a plan;
2. place each unit where it can be visibly accounted for;
3. announce relations to prevent ambiguity;
4. balance apparent alternatives;
5. close the paragraph and then close the set.

Hiding the source removes sentence anchoring but leaves this objective intact. Compressing the ledger changes its length, not its function. Anti-pattern lists add more constraints for the same planner to service. A fresh context removes conversational residue but does not remove the model prior or the externally fixed semantic macroplan.

The deeper mismatch is not that human writers never plan. Human writing research treats planning, text production, and review as recursive and responsive to the growing text. Here the writer receives a nearly complete externally authored goal network and is asked for one polished realization. The prose therefore tends to exhibit the finished plan rather than the movement by which one thought created the need for the next.

## 2. Existing-work scan and build/adapt/reuse decision

An independent conception snapshot was frozen before this scan in:

`SOMATIC-HUMANIZATION-INDEPENDENT-CONCEPTION-SNAPSHOT-003.md`

### Already solved or mature enough to reuse

- Content planning and plan realization can improve coherence, coverage, faithfulness, and controllability. Relevant baselines include Plan-and-Write and plan/realization separation in data-to-text generation.
- Hard or explicit constraints can improve mention coverage, with an acknowledged quality/constraint tradeoff.
- Edit-based style-transfer work establishes a useful separation between content-bearing material and spans treated as style-bearing operations.
- Separate evaluation and semantic verification are established architectural patterns.

### Partially solved

- Text style transfer can balance style change and content preservation in benchmark settings.
- Authorship transfer can be improved with target-author examples, authorship embeddings, fine-tuning, or few-shot exemplars.
- Multi-agent planners and self-checkers can improve benchmark style strength and content preservation.

### Incompatible with this task

- Target-author examples, retrieval, donor prose, or learned authorship embeddings violate the no-donor boundary or are unavailable for this experiment.
- Full planning, constrained realization, and multi-agent checklist servicing optimize the same coverage behavior implicated in the failure.
- Best-of-N generation selected by an imperfect style judge risks proxy over-optimization and does not make same-prompt samples causally independent.
- Pairwise LLM judging introduces ordering and model-family preference risks; it is not a safe primary authorship signal.

### Genuinely unresolved here

No established method was found that guarantees all three simultaneously:

1. complete preservation of an abstract semantic inventory;
2. no access to target-author prose or fresh owner language;
3. discourse movement that does not reveal one-pass model planning.

### Decision

**ADAPT + BOUNDED EXPERIMENT.** Reuse the separation principle from edit-based generation, but discard retrieval, donor transfer, whole-section generation, and detector-led selection. Test a strict null-first source edit whose unit is the discourse operation in context.

Primary research references:

- Flower & Hayes, *A Cognitive Process Theory of Writing* (1981), DOI `10.58680/ccc198115885`.
- Yao et al., *Plan-and-Write* (AAAI 2019), DOI `10.1609/aaai.v33i01.33017378`.
- Moryossef et al., *Step-by-Step: Separating Planning from Realization* (NAACL 2019), DOI `10.18653/v1/N19-1236`.
- Li et al., *Delete, Retrieve, Generate* (NAACL 2018), DOI `10.18653/v1/N18-1169`.
- Wang et al., *Mention Flags* (ACL 2021), DOI `10.18653/v1/2021.acl-long.9`.
- Horvitz et al., *TinyStyler* (EMNLP Findings 2024), DOI `10.18653/v1/2024.findings-emnlp.781`.
- Zhang et al., *A Decoupled Multi-Agent Framework for Complex Text Style Transfer* (EMNLP Findings 2025), DOI `10.18653/v1/2025.findings-emnlp.1166`.
- Shi et al., *Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge* (2024), arXiv `2406.07791`.
- Jinnai et al., *Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment* (2024), arXiv `2404.01054`.

## 3. Strategy family

Strategy family: **SOURCE-BOUND NULL-FIRST DISCOURSE-OPERATION SURGERY**

The complete semantic carrier already exists in the exact R15-derived target. The writer is not asked to reconstruct it from a concept list. The writer may only remove or relocate existing realization operations while retaining the source wording that carries unique meaning.

Cycle 1 permits:

- deletion of an existing complete sentence or independent clause only when its substantive function remains unambiguously elsewhere in the candidate;
- relocation of an existing complete sentence or independent clause intact;
- changes to paragraph boundaries;
- punctuation and capitalization changes strictly required by deletion or relocation.

Cycle 1 forbids:

- new lexical tokens;
- synonym substitution;
- rewriting a retained proposition;
- a new bridge, summary, taxonomy, contrast, metaphor, example, mechanism, authority, treatment claim, or autobiographical fact;
- detector-directed editing;
- editing beyond the four target paragraphs;
- changing either heading or the exact inner-child link destination.

The operative pressure is singular:

> Remove only language that tells the reader how to organize a relation the neighboring material already makes available. Prefer leaving an implication unannounced to replacing it with another explanation.

This is not a phrase blacklist and not a request to make the passage casual, irregular, or less polished.

## 4. Why this is causally different

The failed families asked a model to create a complete text that visibly accounts for multiple abstract requirements. This family does not supply a semantic inventory for realization and does not permit new connective prose. It starts with complete content and restricts the intervention to the topology and accumulation of existing discourse operations.

The Pangram lab's Human-to-AI minimal-pair work found that the relevant causal unit can be a combination of neighboring editorial operations: a taxonomy or bridge may survive alone while their stacked package changes the result. The same work recommends removing connective tissue when it only announces a relationship the reader can already see. That evidence does not prove this candidate will work, but it justifies one bounded whole-section topology experiment rather than another paraphrase.

Prior Somatic surface experiments used local fragments and detector outcomes as the optimization loop. This experiment is different in experimental unit and signal:

- exact unit: the complete four-paragraph Introduction target;
- primary signal: blind reading of thought movement and Joel's judgment;
- detector signal: unavailable during the experiment;
- no known-Human anchor, short-window calibration, or fragment score is admissible evidence.

## 5. Provenance boundary

Under the current direct owner instruction, the operational provenance map for this experiment is:

- `# Introduction`: `UNKNOWN_FROZEN`; byte-locked.
- the four prose paragraphs before `## Your Physical State Can Change What Therapy Does`: `AI_TARGET`; editable only under this decision.
- `## Your Physical State Can Change What Therapy Does` and all later material: `UNKNOWN_FROZEN`; byte-locked and out of scope.

`AI_TARGET` here is an operational scope classification. It does not authorize crediting any retained phrase as owner-Human evidence. If later authoritative provenance identifies an `OWNER_LOCK` inside this block, the experiment fails closed until the map is corrected.

## 6. Writer information boundary

The writer receives only:

1. the exact repository/branch/source identity and bounded target;
2. the provenance boundary above;
3. the allowed/forbidden edit algebra;
4. the single operative pressure;
5. the required output contract.

The writer must not receive:

- either low-structure brief;
- an extracted semantic checklist or function ledger;
- prior rewrite candidates or owner Human exemplars;
- unrelated Joel prose;
- Pangram scores, windows, labels, or detector lessons;
- the catalogue of prior model-shaped symptoms;
- blind-validator outputs from another candidate;
- instructions to sound human, conversational, personal, rough, surprising, or casual.

The writer necessarily sees the exact source because this is an edit operation, not a regeneration operation.

## 7. Model/context policy

Use one genuinely fresh reasoning/writing context for Cycle 1. Do not ask it to generate alternatives, critique itself, revise itself, or choose its best version.

A different model may diversify surface output, but it does not by itself change the failed objective. Model diversity is therefore optional; architecture change is mandatory.

No best-of-N pool is authorized. A second writer context is allowed only under the narrow Cycle 2 rule below. A same-context retry is not independent and is forbidden.

## 8. Blind validator boundary

Two fresh validator contexts independently receive only:

- the exact candidate;
- `SOMATIC-INTRO-BLIND-MOTION-VALIDATOR-001.md`.

They do not see the source, edit script, semantic ledger, strategy, producer identity, other validator output, prior candidates, owner reaction, or detector data.

They do not judge authorship and do not count AI markers. They report the earliest point at which the rhetorical job of the next move became structurally precommitted, what they expected, whether the prose serviced that expectation, and whether the section's movement remained live or became governed by a visible plan.

No pairwise comparison or ranking is allowed. The candidate survives only if both validators independently return `SECTION_MOVEMENT: LIVE`. Disagreement blocks admission; it does not authorize averaging.

## 9. Semantic preservation without writer checklist servicing

The exhaustive semantic/provenance ledger is held only by the downstream custodian in:

`SOMATIC-INTRO-SEMANTIC-CUSTODIAN-001.md`

Only a blind-shape survivor reaches that gate. The custodian compares source and candidate and reports exact lost, weakened, altered, or added functions. It does not suggest wording or patch the candidate.

Because Cycle 1 is source-bound and adds no words, preservation is achieved by keeping the semantic carrier rather than regenerating it from a list. A deletion is admissible only when the same function remains explicit or unambiguously available elsewhere. Merely deciding that a function is unnecessary is not preservation.

## 10. Maximum cycle budget and kill condition

Maximum budget for this strategy family:

- writer candidates: `2` maximum;
- fresh blind validators: `2` per candidate;
- semantic-custodian audits: `1` per blind-shape survivor;
- Pangram calls: `0` under this decision.

Cycle 2 is allowed only when all of the following hold:

1. Cycle 1 passed the mechanical zero-new-token contract;
2. Cycle 1 either:
   - failed semantic custody on exactly one protected function because one source span was deleted; or
   - failed blind motion at one exact topology interaction for which a materially different allowed source-only arrangement exists;
3. the new writer receives no prior prose recommendation and no cumulative semantic checklist;
4. at most one exact source span may be added as a non-deletable lock.

Kill the family immediately if any of the following occurs:

- a writer introduces new lexical prose or paraphrases retained meaning;
- both validators locate materially the same visible-plan defect as the source and no source-only topology change remains;
- a blind-shape survivor loses, weakens, or changes more than one protected function;
- Cycle 2 reproduces the same earliest visible-plan defect;
- semantic completeness would require two or more added constraints, a bridge, or a fresh complete realization;
- Joel rejects an internally admitted candidate as still obviously AI-shaped;
- any owner/unknown-frozen span is changed;
- any Pangram result is used to choose the next edit.

After kill, do not lengthen the prompt, create a third candidate, switch models while retaining the same task, or return to low-structure regeneration. The next supervisor must return `NO_VALID_STRATEGY` unless it can identify a genuinely new source of discourse motion or a new method compatible with the no-donor/no-owner-labor boundary.

## 11. Admission and downstream measurement

Internal admission requires, in order:

1. mechanical edit-algebra pass;
2. two independent `LIVE` blind-motion verdicts;
3. semantic/provenance preservation pass with zero unexplained substantive deltas;
4. current supervisor read;
5. Joel's read.

No Pangram call is authorized for this bounded experiment. A short-section detector label would not establish the whole-document result and must not be used as a prose-design oracle. Any later detector authorization must bind the admitted replacement into an exact whole-document candidate and be issued separately.

## Exact next artifacts

- Writer packet: `SOMATIC-INTRO-NULL-FIRST-WRITER-001.md`
- Blind validator packet: `SOMATIC-INTRO-BLIND-MOTION-VALIDATOR-001.md`
- Semantic custodian packet: `SOMATIC-INTRO-SEMANTIC-CUSTODIAN-001.md`
- Codex execution packet: `SOMATIC-INTRO-NULL-FIRST-CODEX-001.md`
