# Provisional Burst Buffer Gate — 2026-09-01

Status: ACTIVE supplement for the owner-directed Somatic Introduction live-composition experiment. This changes exploratory writer routing only. It does not change article authority, preservation requirements, detector authorization, owner locks, or the registered master.

## Failure that triggered this gate

The writer-blind length controller removed the numerical stopping horizon, but the next 55-word candidate still compressed into a three-sentence miniature essay:

- premise: the story can be understood while the body is doing something else;
- polished restatement: danger/explanation can be settled while the reaction continues;
- abstract harvest: further explanation asks the "wrong part" of the person to solve it.

The strongest defect was not length leakage. The writer was still being asked to produce a sentence and immediately evaluate whether that sentence changed the thought, opened a question, changed case/time/premise/consequence, or added a genuinely new relation. That local acceptance rule selected for proposition-bearing, high-information sentences and discarded ordinary connective/exploratory material before it could participate in later composition.

This is **sentence-level insight-density selection**.

## Independent conception snapshot before existing-work scan

- **Problem:** every surviving sentence carries a complete semantic job, producing premise -> restatement -> abstraction even without a paragraph plan or visible length horizon.
- **Mechanism hypothesis:** immediate sentence-level review plus the requirement that a sentence "change the thought" acts as a semantic-density ratchet.
- **Constraints:** source-card coverage remains occluded during discovery; no invented autobiography/factual specificity; controller still enforces the owner's hidden minimum; critic remains separate; no detector action.
- **Candidate insight:** allow several sentences to remain provisional inside one production burst before conceptual review, instead of making each sentence individually justify its existence.

## Existing-work scan and build decision

Classification: **ADAPT / REUSE**, not claimed invention.

Relevant established writing-process work separates planning, text production/translation, and reviewing rather than treating review as mandatory after every sentence. Empirical writing-process research also describes text production as uneven **bursts** of words/phrases/clauses/sentences between pauses, with burst structure related to fluency and writing quality. Relevant foundations include Hayes & Flower's cognitive-process models; Chenoweth & Hayes on production bursts; Baaijen, Galbraith & de Glopper (2012) on pauses, bursts, and revisions; and later burst-process studies summarized in the writing-process literature.

What is already solved: human writing is usefully modeled as recursive but separable planning/production/review processes, and production commonly spans chunks larger or smaller than one sentence.

What remains task-specific: how to approximate that process inside one LLM context while retaining the owner's fail-closed constraints and hidden minimum-length controller.

Decision: adapt the established separation by adding a **provisional production buffer**. Do not invent another wording blacklist or sentence-level scoring metric.

## Writer mechanism

While this gate is active:

1. **Sentences are provisional during production.** A sentence ending is punctuation, not an automatic editorial checkpoint.
2. **Suspend conceptual acceptance after each sentence.** During the writer pass, do not ask whether the just-written sentence changed the thought, added a fresh relation, earned its place, or should be deleted for overexplanation. The sentence-level overexplanation-kill rule in `LIVE-MUTATIONAL-COMPOSITION-PROTOCOL-20260831.md` is temporarily deferred to the post-buffer critic for this experiment.
3. **Local checks are narrow.** Immediate interruption is allowed only for a material semantic/provenance violation, invented fact/autobiography, unintelligibility that blocks continuation, or a hard owner boundary. Mere plainness, repetition risk, low information density, or lack of insight is not enough to interrupt production.
4. **Continue from the literal buffer.** The writer may read the text-so-far for language continuation, but does not classify the rhetorical job of each sentence or summarize the argument between sentences.
5. **Allow low-load material.** Ordinary connective tissue, partial elaboration, wording drift, and sentences that are not individually quotable may remain provisional. They are not padding by default; the critic decides later whether they became redundant.
6. **Controller remains nonsemantic.** After each provisional sentence boundary, the writer-blind controller may privately return only `CONTINUE` or `STOP` based on the owner's hidden minimum. It does not accept/reject prose or reveal count/horizon.
7. **`CONTINUE` does not trigger review.** It means only that production resumes from the existing buffer. Do not reread the preceding sentence as a critic before continuing.
8. **`STOP` freezes the whole buffer.** Only then does the critic reopen the accumulated structural gates and evaluate the complete passage for AI shape, repetition, conceptual harvesting, cumulative convergence, source/provenance violations, and true stopping point.
9. **Critic may reject the entire buffer.** Do not rescue a failed buffer by line-editing it under the writer role. The next `eval` changes the mechanism if the failure is causal and reusable.

## Boundary with existing rules

- Source-card occlusion remains active.
- Writer-blind length control remains active.
- Post-repair anchor eviction remains active when a genuine clarification occurs.
- The writer-critic firewall remains active.
- The sentence-level overexplanation/novelty gate is **deferred during production** and applied only after the buffer freezes.
- This does not authorize meaningless filler or random wandering. It removes premature conceptual review; it does not remove the later critic.

## `eval` consequence

If a future candidate still consists almost entirely of semantically complete, insight-bearing sentences, inspect whether the writer actually kept sentences provisional or silently resumed sentence-by-sentence conceptual acceptance. Do not answer by adding another ban on abstract sentences.
