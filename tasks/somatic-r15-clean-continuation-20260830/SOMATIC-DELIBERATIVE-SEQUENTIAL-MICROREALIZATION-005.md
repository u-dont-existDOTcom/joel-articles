# SOMATIC HUMANIZATION STRATEGY 005 — DELIBERATIVE SEQUENTIAL MICRO-REALIZATION

Date: 2026-08-31

Task: `somatic-r15-clean-continuation-20260830`

Strategy ID: `SOMATIC-DSMR-005`

Disposition: **CANDIDATE FOR FRESH ADVERSARIAL ARCHITECTURE AUDIT**

Execution status: **NOT AUTHORIZED UNTIL A FRESH AUDITOR RETURNS EXACT ACCEPT**

## 0. Why this strategy exists

The previous source-bound topology strategy was revoked by `SUPERVISOR-CORRECTION-SOMATIC-HUMANIZATION-REASONING-004.md` after a fresh audit found authority, preservation-order, deletion-authority, causal-design, and failure-feedback defects.

Joel then supplied materially new process evidence: his best model-only humanization progress occurs in Pro and Work Ultra when the model is given approximately one paragraph and told to iterate repeatedly until it believes the paragraph is done. A single paragraph can consume roughly ten minutes of model work, and Joel estimates such passes can reach roughly `70% humanized` by his own reading. This is recorded separately in `OWNER-OBSERVATION-DELIBERATIVE-MICROREWRITE-20260831.md`; it is not a Pangram score.

The existing fresh Pro and Extra-High Somatic runs did **not** test that condition. They each received a roughly 4,500-word whole-article instruction/input and returned one complete article. Those runs tested high-compute whole-document realization, not high-compute repeated micro-revision.

This strategy therefore tests one new causal interaction rather than adding another anti-AI prompt:

> **small visible scope × high inference-time effort × repeated private rewriting × no future coverage problem**

External reasoning gates protect fidelity; they do not substitute for the writer's search.

## 1. Core hypothesis

The repeated Somatic failure may not mean the strongest model cannot produce substantially more natural prose. It may mean that when many semantic obligations are simultaneously visible, the model spends its effort solving a coverage/planning problem and then emits that plan as polished explanatory architecture.

For a single paragraph, the semantic search space is small enough that a high-compute model can spend much more of its inference budget on realization choice, discard plausible-but-model-shaped drafts, and restart from the thought rather than merely paraphrasing the source.

The critical difference from prior direct paraphrase is not source visibility by itself. The difference is that the writer:

- owns only one tiny natural unit;
- cannot see future paragraph obligations or a complete semantic inventory;
- is explicitly allowed and encouraged to repeatedly rebuild the unit before emitting anything;
- is judged only on its one final visible output;
- cannot self-certify semantic fidelity.

This is an empirical hypothesis, not a claim that more compute universally produces Human prose.

## 2. Research support and limitation

The general use of iterative model feedback/refinement is supported by work such as Madaan et al., *Self-Refine: Iterative Refinement with Self-Feedback* (NeurIPS 2023; arXiv:2303.17651), which found iterative refinement improved outputs across several tasks relative to one-step generation.

The limitation is equally important. Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet* (ICLR 2024; arXiv:2310.01798), found that intrinsic self-correction can fail or degrade reasoning without reliable external feedback. Wu et al., *Large Language Models Can Self-Correct with Key Condition Verification* (EMNLP 2024; DOI `10.18653/v1/2024.emnlp-main.714`) showed that correction improves when the verification target is made more checkable.

Therefore this strategy uses internal iteration for **search**, while semantic preservation remains an external, explicit, pre-frozen verification problem.

## 3. Pilot scope

The pilot is only the first 43-word prose paragraph of the Introduction.

Authoritative source identity and the complete pre-draft preservation ledger are frozen in:

`SOMATIC-INTRO-P1-PRESERVATION-ESCROW-001.md`

Source paragraph SHA-256:

`b2cbeec01b3a209a845911c99e3d4810d3ccbcc5ebd77ee38a4e221fcb44a1c9`

The preservation escrow is **not writer input**.

No later Introduction paragraph is part of the pilot. No article mutation and no Pangram action are authorized.

## 4. Writer information boundary

The writer receives only:

1. the exact `# Introduction` heading as placement context;
2. the exact 43-word target paragraph;
3. a compact preservation instruction: preserve every substantive meaning, example, scope/certainty, and the fact that the claims remain general rather than invented Joel autobiography;
4. the deep-deliberation process instruction;
5. the output contract: one final paragraph only.

The writer does **not** receive:

- the preservation escrow or semantic-unit IDs;
- later Introduction paragraphs or their semantic obligations;
- the complete article;
- Pangram results, windows, scores, or detector vocabulary;
- rejected Somatic candidates;
- the failed-strategy catalogue;
- unrelated Joel prose, owner-Human examples, donor prose, or style exemplars;
- a list of suspicious words, sentence patterns, rhetorical devices, or known Pangram flips;
- an instruction to imitate Joel's corpus.

This avoids converting the hidden preservation ledger into a visible outline while keeping the exact source paragraph available as semantic authority.

## 5. Writer mode and search process

Preferred generation surface: **Work Ultra** when a genuinely fresh isolated writing context is available. Otherwise use **GPT-5.6 Sol Pro, 5 of 5**.

This preference is based on Joel's direct process observation, not a claim that a product label guarantees quality.

The writer is told not to optimize for speed and not to return its first acceptable rewrite. It performs repeated private rewrite/read/rewrite cycles. It may restart completely from the paragraph's thought rather than edit the immediately preceding draft. It stops only when another full private read no longer reveals a change it actually believes would improve natural thought movement without risking meaning.

No chain-of-thought, draft history, self-critique transcript, candidate pool, or iteration count is requested or exposed. The only visible writer output is the final paragraph.

The hidden iteration itself is not auditable proof. Mode, exact prompt/input identity, timestamps, and final output are recorded as treatment metadata. The visible candidate must pass downstream gates regardless of how long generation took.

## 6. Why this is not the previous failed direct-rewrite experiment

The previous Pro/Extra-High direct runs had to preserve and realize an entire article at once. The model could see every future obligation and every inherited paragraph, making global coverage and source-skeleton following the dominant optimization problem.

`SOMATIC-DSMR-005` removes that global task. The first writer can see only one paragraph and no future obligations. The first visible output is produced only after an explicitly deliberative private search.

This does **not** assume source anchoring has disappeared. Source anchoring is the main falsifiable risk of the pilot. If the final output remains a sentence-by-sentence descendant after deep micro-deliberation, the hypothesis is weakened directly rather than rescued by a larger prompt.

## 7. Gate order

The pilot gate order is fixed:

1. **PRE-DRAFT PRESERVATION — already frozen.** Verify exact source identity and `SOMATIC-INTRO-P1-PRESERVATION-ESCROW-001.md` before writer launch.
2. **WRITER — one fresh high-compute context.** Capture exactly one final paragraph.
3. **SEMANTIC CUSTODY.** A separate reasoning context receives source + escrow + candidate and performs forward/reverse traceability. It does not rewrite.
4. **COLD SHAPE READ.** Only after semantic PASS, a separate fresh context receives `# Introduction` + candidate only. It does not see source, strategy, producer, detector data, or preservation ledger.
5. **SUPERVISOR READ.** The controlling reasoning context checks the literal candidate and the two receipts.
6. **OWNER READ.** Only an internally admitted paragraph is shown to Joel.
7. **PANGRAM — zero calls in this pilot.** A one-paragraph detector result would not establish the whole-document goal.

## 8. Semantic-custody contract

The semantic custodian must map every `P1-U01` through `P1-U04` to exact candidate spans and classify every substantive candidate delta against the frozen whitelist.

Required pass:

- forward traceability: PASS;
- reverse traceability: PASS;
- unexplained substantive deltas: `0`;
- general-claim / autobiography separation: PASS;
- all six reaction examples retained: PASS.

The semantic custodian returns no wording advice.

### Semantic failure feedback

A first candidate may receive exactly one corrective generation cycle only if the semantic failure is **one isolated unit or one exact scope/attribution defect**.

Candidate 2 is produced by a **fresh high-compute writer**, starting from the original source paragraph rather than patching Candidate 1. It receives the original writer packet plus one exact non-negotiable correction stating the single preservation failure. It does not receive Candidate 1.

If Candidate 1 loses/changes two or more preservation units, or Candidate 2 has any substantive preservation failure, kill the pilot family for this paragraph. Do not add a semantic checklist.

## 9. Cold-shape contract

The fresh cold reader receives only:

`# Introduction`

plus the semantically valid candidate paragraph.

It answers only:

- `MOVEMENT: LIVE | PRECOMMITTED`
- `STRONGEST_DEFECT: <one concrete description or NONE>`
- `EARLIEST_POINT: <short exact candidate span or NONE>`

The reader judges the literal movement of thought, not authorship and not Pangram likelihood. It must not rewrite.

### Shape failure feedback

If Candidate 1 is semantically valid but returns `PRECOMMITTED`, exactly one corrective generation cycle is allowed.

Candidate 2 is produced by a **fresh high-compute writer** from the original source paragraph, not Candidate 1. It receives the original writer packet plus only the cold reader's single `STRONGEST_DEFECT` as new information. It does not receive the reader's rationale, a catalogue of anti-patterns, or any detector data.

This is the key answer to the owner's earlier hard-rejection objection: a failure does not merely block release. It changes the next generator's information by one concrete observed defect while preserving a fresh search from the authoritative source.

If Candidate 2 receives the same materially equivalent `PRECOMMITTED` defect, kill this strategy family for the paragraph. Do not produce Candidate 3 or lengthen the prompt.

## 10. Total writer budget and collision rule

Maximum visible writer candidates for the paragraph: `2`.

There is one shared corrective slot, not one semantic retry plus one shape retry.

- If Candidate 1 fails semantics in an eligible one-defect way, Candidate 2 spends the slot on that defect.
- If Candidate 1 passes semantics but fails cold shape, Candidate 2 spends the slot on that defect.
- If Candidate 2 fails any blocking gate, the pilot ends.

No best-of-N pool, ranking tournament, or same-prompt sample fishing is allowed.

## 11. Owner protection and owner feedback

Joel sees at most one internally admitted paragraph from this pilot.

If Joel says the admitted paragraph is still obviously model-shaped, that is binding strategy evidence. Do not defend the validators or ask him to test Pangram.

If Joel gives a specific authorial correction, that correction becomes new owner authority and is handled separately under normal preservation rules. If his reaction is only that the prose remains AI-shaped, the micro-deliberation pilot is classified unsuccessful for this paragraph and no third same-family writer is created.

If Joel says the paragraph is materially better but not done, record that outcome precisely rather than converting it into PASS or FAIL by inference. A successor reasoning decision may then test a genuinely different refinement mechanism; it may not simply repeat the identical prompt indefinitely.

## 12. Pilot success and scale rule

Pilot success does **not** mean Pangram success and does not establish whole-article completion.

The strategy earns permission for a larger sequential test only if:

- semantic custody passes with zero unexplained deltas;
- cold shape returns `LIVE`;
- supervisor finds no known defect it actually believes should be repaired;
- Joel judges the paragraph materially more naturally authored than the source and worth continuing from.

If that occurs, scale sequentially rather than returning to whole-document realization:

1. classify/freeze the next editable paragraph's provenance and preservation escrow before writing;
2. writer receives the accepted preceding reader-visible paragraph for local continuity plus the exact next AI target, but no future targets or full semantic inventory;
3. repeat deep private micro-revision;
4. run semantic custody before shape reading;
5. after a natural section is assembled, run an adjacent-boundary/section cold audit and repair only a specifically authorized micro-boundary if necessary;
6. preserve frozen owner/unknown spans untouched;
7. after the complete article is assembled, run whole-document preservation, architecture, links, native-object, and cold-reader gates;
8. only then consider one exact whole-document Pangram 4 measurement under separate detector authority.

Paragraph-by-paragraph detector testing is not part of this production strategy.

## 13. Kill conditions

Kill `SOMATIC-DSMR-005` for the pilot paragraph if any of the following occurs:

- the fresh architecture auditor rejects the causal distinction or protocol safety;
- exact source/escrow identity cannot be verified;
- Candidate 1 has two or more substantive preservation failures;
- Candidate 2 has any substantive preservation failure;
- Candidate 2 reproduces the materially same cold-shape defect;
- the writer adds invented autobiography, examples, mechanisms, facts, or certainty;
- output requires exposing the full semantic ledger or future paragraph plan to get preservation;
- the process begins generating multiple candidates and choosing the most Human-looking one;
- a detector result is used to direct paragraph wording;
- Joel rejects the internally admitted result as obviously model-shaped without identifying new owner content that would change the semantic source.

After kill, do not add more instructions to this family. The next reasoning decision must compare a genuinely different mechanism, including the previously identified adaptive semantic-escrow/progressive-disclosure direction, or conclude that current model-only constraints are insufficient.

## 14. Architecture-audit requirement

Because recent supervisor reasoning produced multiple logical failures, this strategy is not self-authorizing.

Before any writer transport, one genuinely fresh high-compute reasoning context must adversarially audit this exact file plus:

- `SUPERVISOR-CORRECTION-SOMATIC-HUMANIZATION-REASONING-004.md`;
- `SOMATIC-INTRO-P1-PRESERVATION-ESCROW-001.md`;
- the blocking preservation rules needed to evaluate it;
- `OWNER-OBSERVATION-DELIBERATIVE-MICROREWRITE-20260831.md`.

The auditor must test especially:

1. whether this really differs causally from failed direct paraphrase rather than merely asking the model to try harder;
2. whether writer source visibility fatally preserves the source skeleton;
3. whether the hidden-ledger / visible-source split satisfies pre-draft preservation without recreating a coverage checklist;
4. whether one-defect feedback genuinely changes the next generation process;
5. whether the two-candidate budget is scientifically informative;
6. whether Codex can orchestrate the state machine mechanically without making semantic decisions;
7. whether owner shielding can fail in a way that wastes Joel's time;
8. whether the scale rule would create paragraph-local quality at the expense of section/article movement.

Only exact `VERDICT: ACCEPT` authorizes the pilot writer. `ACCEPT_WITH_REVISION`, `REJECT`, or unresolved contradiction returns to Chat reasoning and authorizes no prose generation.
