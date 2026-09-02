# Contrastive Attention Scheduler Gate — 2026-09-01

Status: ACTIVE experimental supplement for the owner-directed Somatic Introduction live-composition experiment. This changes exploratory attention routing only. It does not change article authority, preservation requirements, detector authorization, owner locks, or the registered master.

## Triggering failure

The provisional burst buffer removed immediate sentence-level conceptual review, but the next 62-word passage remained in one semantic orbit. Nearly every sentence was a paraphrastic descendant of the same proposition: cognitive understanding can be complete while bodily reaction continues, therefore another explanation may be irrelevant.

The pre-search independent diagnosis is preserved in `SEMANTIC-ORBIT-DIAGNOSTIC-SNAPSHOT-20260901.md`.

The key implementation mismatch was already visible in task control: the high-level method called for a small parallel pool of pre-propositional pressures, while the actual writer instruction supplied only **one** small snag. With review suspended, that seed monopolized the autoregressive continuation until the hidden length controller stopped the buffer.

Working failure name: **single-seed attentional monopoly / semantic orbit**.

## Existing-work scan

Classification: **ADAPT + EXPERIMENT**, not claimed invention.

Relevant established work:

- Holtzman et al., *The Curious Case of Neural Text Degeneration* (ICLR 2020), documents bland/repetitive degeneration in open-ended autoregressive generation and shows that decoding policy materially changes repetition/diversity.
- Su & Collier, *Contrastive Search Is What You Need For Neural Text Generation* (TMLR 2023), and the preceding contrastive-generation work balance model confidence against a degeneration penalty based on similarity to prior context.
- Hugging Face Transformers implements contrastive search as a mature generation strategy using `penalty_alpha` and `top_k`, explicitly describing it as reducing repetition while retaining coherent generation.

What is already solved: decoder-level methods can penalize continuations that are too similar to prior context while preserving likely/coherent text.

What is incompatible here: this Chat context does not expose token-level decoder control, hidden-state similarity, or generation parameters. The observed failure is also discourse-level semantic paraphrase, not merely lexical/token repetition.

Decision: **adapt the contrastive principle at the attention/burst level** rather than inventing a phrase blacklist or pretending to implement token-level contrastive search. Benchmark the next frozen passage against the 62-word semantic-orbit baseline by cold editorial audit only; Pangram remains unauthorized.

## Scheduler architecture

Keep three roles separate:

1. **Writer** — produces provisional prose from literal text and currently exposed pre-propositional pressure. It does not see the rejection catalog, length floor, scheduler diagnosis, similarity judgment, source-coverage map, or reason for any attention shift.
2. **Length controller** — returns only `CONTINUE` or `STOP` at provisional sentence boundaries using the hidden owner minimum.
3. **Contrastive attention scheduler** — may alter which already-live pressure is exposed to the writer, but does not write article prose and does not supply a semantic conclusion.

## Scheduler mechanism

1. **Maintain a genuinely pre-propositional reserve.** Before prose begins, hold two or three incomplete pressures/fragments. A reserve item must not be a bullet-ready article claim, source-unit label, treatment recommendation, matched opposite, or planned paragraph job.
2. **One active pressure at a time.** The writer receives only one exposed pressure, not the whole reserve, so it cannot plan a multi-card sequence.
3. **Check semantic orbit only after provisional sentences.** The scheduler asks whether the newest sentence and the immediately preceding one are substantially interchangeable as realizations of the same proposition. Use a strict standard: if deleting either sentence leaves essentially the same live semantic state, orbit risk is present.
4. **No general quality scoring.** The scheduler does not ask whether a sentence is elegant, insightful, human, useful, or detector-safe. It checks only local semantic redundancy.
5. **Mask the dominant center on orbit.** When orbit risk is present, temporarily make the proposition driving the redundant pair non-generative for the next continuation burst. The writer may still see the literal text for grammar/coherence but may not continue because of that same proposition's example, restatement, consequence, or abstraction.
6. **Prefer a peripheral literal anchor.** First expose a different unresolved pressure already present in the literal buffer: an actor, verb, temporal edge, odd word, consequence, or relation that is not merely another realization of the masked proposition.
7. **Fallback to the reserve, not source coverage.** If no peripheral literal pressure is viable, expose one dormant pre-propositional reserve item. Do not consult uncovered source obligations or create a new semantic card because continuation is required.
8. **No bridge instruction.** The scheduler does not tell the writer to explain the shift or relate the two pressures. Juxtaposition may remain if intelligible.
9. **No forced divergence.** If the alternative pressure cannot enter coherently without fabricated facts, random wandering, a source-card reset, or explanatory bridge machinery, do not force it. A later `CONTINUE` may expose another dormant pressure; the current semantic center remains temporarily masked.
10. **Reactivation requires intervening cognition.** The masked center may become generative again only after a materially different provisional sentence has landed.
11. **Length remains writer-blind.** The scheduler receives no count/horizon signal beyond whether the controller has already stopped the pass.
12. **Critic remains post-buffer.** After `STOP`, the normal critic decides whether the complete passage is still repetitive, card-like, overcompleted, incoherent, or AI-shaped. The scheduler cannot self-certify success.

## Why this is not the failed multi-seed/card mechanism

The earlier multi-seed failure prepackaged several complete propositions and concatenated them. This gate keeps reserve items pre-propositional, exposes only one at a time, and invokes another pressure only after local semantic redundancy appears. It does not build a coverage outline or complementary set of claims.

## Benchmark

Baseline: the 62-word candidate beginning `You can understand the trauma perfectly...`, cold-rejected for semantic orbit.

Next-pass success condition for this mechanism is modest: the frozen passage must not consist primarily of interchangeable paraphrases of one proposition, and any attention shift must remain coherent without a source-card bridge. This is an editorial process benchmark only, not detector evidence.

## `eval` consequence

If semantic orbit recurs, inspect whether the scheduler actually masked the dominant center and exposed a genuinely different pre-propositional pressure. If the result instead becomes bridge-free semantic-card succession or arbitrary wandering, the scheduler itself is falsified or needs revision; do not fix the prose with surface wording changes.
