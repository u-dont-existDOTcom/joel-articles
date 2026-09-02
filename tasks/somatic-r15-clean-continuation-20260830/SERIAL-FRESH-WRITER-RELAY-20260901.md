# Somatic Introduction Serial Fresh-Writer Relay — 2026-09-01

Status: ACTIVE RADICAL-RESET EXPERIMENT. Non-authoritative. No article promotion, registered-master edit, source reconciliation, or detector-driven publication change is authorized.

## Trigger

Three primary physically isolated same-model whole-paragraph writers all cold-FAILed:

1. supplied thesis -> balanced qualification + three-part rubric;
2. atomized fragment `words come late` -> metaphor + repeated abstraction + conceptual closure;
3. lower-information fragment `afterward` -> lexical challenge + conceptual complication + polished paradoxical landing.

No candidate was eligible for Pangram. The third failure satisfies the early strategy-audit trigger `THREE_CONSECUTIVE_COLD_FAILS_WITHOUT_UNCHANGED_MECHANISM_SURVIVAL` and shows that **whole-paragraph generation itself gives the model enough horizon to manufacture a mini-essay**, even when context is fresh and the seed is extremely thin.

Strategy disposition: `RADICAL_RESET`.

## Architectural change

Stop asking any one writer execution to produce a whole >=50-word paragraph.

Instead, construct the candidate through a **serial relay of physically fresh one-sentence writers**. No writer sees the length target, remaining word count, qualification state, detector state, prior critic rationale, or future paragraph job. No writer is allowed to decide the paragraph ending.

The external controller owns only assembly, minimum-length checking, and STOP/CONTINUE. The evaluator sees only the final frozen paragraph.

This is not the earlier same-context microburst protocol. The crucial change is **physical context reset at every sentence boundary**.

## Roles

### Relay controller — Codex mechanical only

Codex may:

- read the current relay state from GitHub;
- open a genuinely fresh writer context for each sentence;
- send the exact sentence-writer packet;
- capture exactly one sentence;
- append it byte-for-byte to the relay buffer;
- compute word count mechanically;
- decide only `CONTINUE` or `STOP` from the hidden minimum-length rule;
- freeze the final paragraph and send it to evaluator Chat.

Codex may not judge prose, choose themes, rewrite sentences, or repair coherence.

### Sentence writer — fresh context for every sentence

Each sentence writer receives only:

1. the literal relay buffer so far, or for sentence 1 the initial seed;
2. one instruction: produce **exactly one next sentence** that follows whatever local thought is live;
3. no numerical length target;
4. no statement about whether this is the first, middle, or likely final sentence;
5. no prior failure catalog, evaluator rationale, Pangram information, source-function checklist, or desired takeaway;
6. no invented autobiography, symptoms, chronology, evidence, clinical facts, or unauthorized factual specificity;
7. no unrelated Human donor prose.

The writer returns exactly one sentence and nothing else.

### Hidden length controller

After each sentence is appended:

- if total candidate length is below the owner floor, return `CONTINUE` mechanically and launch a fresh sentence writer;
- at the **first sentence boundary** at or above the floor, return `STOP` and freeze the paragraph;
- never tell a writer the count, distance to threshold, or that STOP is near;
- never ask a writer for an ending, conclusion, summary, or final sentence.

The owner floor remains >=50 words for a complete exploratory candidate.

### Evaluator Chat

The evaluator receives only:

```text
eval

<exact frozen relay paragraph>
```

and applies the existing blinded verdict protocol. Writer identities, sentence count, relay metadata, and stop position remain hidden until the verdict is frozen.

## Initial relay seed

For epoch 2, start from the lexical fragment:

`afterward`

Do not reuse the failed trial-003 paragraph. The seed is the same only to isolate the effect of **whole-paragraph horizon vs per-sentence fresh-context relay**.

## Sentence-writer packet

For sentence 1:

```text
You are a physically isolated writer for one non-authoritative exploratory Somatic Introduction sentence.

Starting fragment: `afterward`

Write exactly one prose sentence that follows whatever local thought occurs from that fragment. Do not try to cover the Introduction, explain the whole idea, or land a takeaway. Do not invent autobiography, symptoms, chronology, evidence, clinical facts, or factual specificity not supplied. Do not imitate unrelated Human prose. Return only one sentence.
```

For sentence 2+:

```text
You are a physically isolated writer contributing exactly one next sentence to a non-authoritative exploratory Somatic Introduction paragraph.

Literal text so far:

<BUFFER>

Write exactly one next prose sentence that follows the most locally live thought from the literal text. Do not summarize the paragraph, explain why the previous sentence matters, manufacture a takeaway, or try to complete the Introduction. Do not invent autobiography, symptoms, chronology, evidence, clinical facts, or factual specificity not supplied. Do not imitate unrelated Human prose. Return only one sentence.
```

The sentence writer is not told the paragraph minimum, remaining distance, sentence ordinal, or whether another writer will follow.

## Mechanical validation

Codex rejects and reruns a sentence-writer execution only for mechanical contract failure:

- output contains more than one sentence;
- output contains labels/rationale/markdown instead of one prose sentence;
- output is empty;
- output introduces prohibited explicit metadata about AI/detectors/experiment/evaluator;
- output cannot be appended as prose.

Codex does **not** reject because a sentence looks AI-shaped. That remains evaluator authority after the paragraph freezes.

## Why this is a radical reset

The prior architecture isolated whole-paragraph writers but still let one autoregressive process see enough horizon to:

- establish a premise;
- qualify it;
- introduce metaphor/contrast;
- harvest a concept;
- land a payoff.

The relay removes paragraph-level planning continuity from the writer process itself. Every sentence continuation is generated by a context that did not produce the earlier sentences and cannot know whether it will be allowed to write again.

If polished mini-essay closure still emerges reliably under this architecture, that is much stronger evidence that the model can reconstruct the same rhetorical attractor from literal text alone, and the next strategy audit should consider changing model/runtime or abandoning generative reconstruction as the main lane.

## A/B benchmark

Compare epoch-2 relay output against trial 003, which used the same seed `afterward` but one fresh writer generated the whole paragraph.

Do not Pangram either candidate merely for comparison. Pangram remains authorized only after a genuine blinded cold PASS.

## Hermes / n8n role

- n8n may shadow the relay state machine with one execution per sentence, but GitHub remains canonical.
- Hermes remains an optional alternate-runtime sentence-writer/strategy-shadow lane when a model provider becomes available. Do not block the primary relay on Hermes setup.

## Success signal

A meaningful success is a relay paragraph that cold-PASSes without any sentence writer having seen the paragraph horizon or ending position. If it cold-PASSes, authorize Pangram for the exact frozen hash under the existing overnight detector rules.

## Failure / next audit

If **two relay paragraphs** cold-FAIL with the same broad mini-essay/closure family, trigger another strategy meta-audit immediately rather than adding sentence-level bans.

If the relay fails by incoherence rather than polished closure, that is also architecture evidence: consider a different representation/runtime rather than inserting an editorial bridge layer that would recreate centralized planning.