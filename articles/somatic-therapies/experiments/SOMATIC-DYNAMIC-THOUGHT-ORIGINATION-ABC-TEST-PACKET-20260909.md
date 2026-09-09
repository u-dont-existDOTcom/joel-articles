# Dynamic thought origination — A/B/C fresh-context test packet — 2026-09-09

Status: **EXPERIMENT DESIGN / NO PANGRAM AUTHORIZATION / REQUIRES GENUINELY FRESH CONTEXTS / NOT ARTICLE PROSE**

Parent strategy:
`SOMATIC-HUMANIZATION-STRATEGY-V2-DYNAMIC-THOUGHT-ORIGINATION-20260909.md`

## Purpose

Test the specific causal hypothesis that **premature global conceptual commitment**, rather than sentence polish alone, is a major source of model-shaped independent prose.

The comparison must hold the topic fixed and keep owner cognition out of every condition.

Do not execute this inside one saturated conversation while pretending the roles are independent. Each box marked `FRESH CONTEXT` requires genuine informational isolation from the other generation/evaluation boxes except for the exact payload explicitly passed into it.

## Topic selection

Use at least three ordinary nontechnical topics with no Joel-specific content. Avoid topics that strongly invite a known five-part explainer, factual research summary, or moral argument.

Do not use the prior `walking at night` topic as the only test because its existing result can anchor evaluation. It may be retained as one replication topic only if the new generators/evaluators do not see the earlier passage or result.

Freeze all topics before generation.

## Condition A — direct one-shot baseline

### A1 — FRESH CONTEXT

```text
You are writing an independent short reflective passage.

Topic: <TOPIC>

Write one contiguous prose passage of roughly 250–400 words. Develop whatever seems genuinely worth saying about the topic. Do not mention this instruction, AI, evaluation, or an experiment. Return only the passage.
```

Purpose: reproduce ordinary bare-topic autonomous generation without supplying a thought route.

## Condition B — static-plan baseline

### B1 planner — FRESH CONTEXT

```text
Topic: <TOPIC>

Plan one coherent 250–400 word reflective passage about this topic. Decide the complete conceptual route before prose is written: the main claim or pressure, the major moves in order, and where the passage should end.

Return only a concise outline for another writer. Do not write the passage itself.
```

Freeze the exact outline.

### B2 writer — FRESH CONTEXT

Give the writer only:

```text
Write a 250–400 word reflective prose passage from the following fixed plan.

<EXACT B1 OUTLINE>

Follow the plan faithfully. Do not mention the plan, AI, evaluation, or an experiment. Return only the passage.
```

Purpose: strong planning baseline. This is not expected to be bad writing; it tests whether a complete precommitted conceptual allocation retains the suspected model-shapedness.

## Condition C — dynamic thought origination

### C1 seed generators — MULTIPLE FRESH CONTEXTS

Run 5–8 independent seed calls. Each call receives the same bare topic and **does not see any other seed**.

```text
Topic: <TOPIC>

Give exactly one raw thought seed that could be worth following: one observation, tension, causal relation, practical curiosity, social consequence, or other locally alive thought.

Do not cover the topic. Do not give alternatives or an outline. Do not write a finished paragraph or a takeaway. One or two sentences only.
```

The example categories above describe admissible seed forms; a seed does not need to fit a named category. Do not later require category coverage.

Freeze all seeds before selection.

### C2 selector — FRESH CONTEXT

The selector receives only the topic and frozen seeds, with no detector results or prior prose.

```text
Topic: <TOPIC>

Below are independent thought seeds. Choose the one that has the strongest local pressure for real prose.

Prefer a seed that:
- notices or relates something specific rather than summarizing the topic;
- has reality contact;
- leaves something genuinely unresolved enough to continue;
- does not already contain a complete thesis/caveat/takeaway package;
- does not try to cover the whole topic.

<SEEDS WITH NEUTRAL IDS>

Return only the chosen seed ID.
```

Do not pass the selector's rationale to the writer. If desired for research, a separate selector-annotation run may explain the choice after the ID is frozen.

### C3 local writer — FRESH CONTEXT

The writer receives only the selected seed. Do not give it the unused seeds, selection criteria, anti-pattern library, detector history, or full-topic outline.

```text
Develop the thought below into one bounded piece of reflective prose. Stay with this thought rather than trying to cover the whole topic. Stop when this particular thought naturally stops.

<SELECTED SEED>

Return only the prose.
```

Do **not** impose a word target on this first movement. Record its natural length.

### C4 next-thought generator — FRESH CONTEXT

Only if a longer natural boundary is needed, give a fresh context the literal C3 prose and nothing about the hidden experiment hypothesis:

```text
Read the literal prose below.

<EXACT C3 PROSE>

What is the single most locally live thought that follows from what is actually on the page? Return one raw thought seed only. Do not summarize the passage, explain why it matters, manufacture a takeaway, or try to complete the topic. If the thought has genuinely stopped, return exactly: STOP
```

### C5 continuation writer — FRESH CONTEXT

If C4 returned a seed, give a new writer only the exact current prose plus that seed:

```text
Literal prose so far:

<EXACT CURRENT PROSE>

Next thought seed:
<NEXT SEED>

Continue the prose only through this locally live thought. Do not summarize earlier prose or try to complete the overall topic. Stop when this thought stops. Return only the continuation.
```

Repeat C4/C5 only until a natural boundary of useful comparison length exists. Record every call and exact payload. Do not force continuation merely to hit a target word count.

## Optional Condition D — diversified seed origination

Use only after A/B/C if C fails or seed convergence is obvious.

Assign each fresh C1 seed generator one distinct **cognitive stance**, not a prose persona or demographic stereotype. Examples:

- notice an ordinary physical detail;
- notice a social interaction;
- follow a causal mechanism;
- follow a contradiction or failed expectation;
- follow a practical consequence;
- look for what changes over time.

Each generator still returns only one seed. The final writer never sees the stance label.

Purpose: test whether diversity must be injected upstream at thought origination rather than by temperature/style prompting.

## Evaluation — no detector required initially

### E1 thought-topology audit — FRESH CONTEXT

Blind the evaluator to condition labels and generation history. Give the three passages in randomized order.

Ask it to diagnose, not rewrite:

```text
Read these passages as finished prose. For each passage, identify its hidden conceptual movement paragraph by paragraph and sentence cluster by sentence cluster.

Judge specifically:
- whether it decomposes the topic into neat coverage categories;
- whether neighboring thoughts receive suspiciously equal rhetorical duration;
- whether mini-essays repeatedly close before the next conceptual job starts;
- whether caveats, significance, or takeaways arrive because the form expects them;
- whether the prose seems to discover/continue locally or execute a pre-completed route;
- whether any sentence merely explains why the previous sentence mattered.

Do not infer which passage was produced by which method. Do not rewrite. Rank the passages from least to most globally pre-completed, and anchor every diagnosis to literal text.
```

### E2 ordinary-reader quality audit — FRESH CONTEXT

Separately assess coherence, interest, specificity, and whether the passage earns its ending. Do not tell this evaluator that AI-shape is the target.

### E3 owner judgment

Joel's judgment remains high-value external feedback, but record it separately from the fresh-model audits.

### E4 Pangram

**Do not run unless Joel explicitly asks.** If later authorized, freeze exact natural boundaries, hashes, model/version/History identity where available, and do not transfer results across changed boundaries.

## Primary hypotheses

H1: Condition B may improve coherence relative to A but retain or intensify complete conceptual allocation.

H2: Condition C will show less category coverage, less equalized paragraph function, and fewer nested closures than A/B while remaining coherent.

H3: If C fails because its seeds are already generic mini-theses, the bottleneck is thought origination/selection rather than prose realization.

H4: If seeds are good but C3/C5 reconstitute the same global mini-essay shape, the bottleneck is realization and the next strategy should move away from prompting toward learned adaptation/training.

## Disconfirmation rules

Do not call the strategy successful because one C passage sounds better.

Down-rank or reject the causal hypothesis if:

- A/B and C have the same hidden topology under blind analysis;
- C is only less polished/shorter rather than less globally pre-completed;
- C's apparent advantage disappears on multiple topics;
- C improves only when owner knowledge or human prose leaks into the independent condition;
- C requires the selector/evaluator to know the target or detector result;
- condition labels can be predicted only from superficial wording rather than thought movement.

## Production firewall

The A/B/C independent experiment is **not** the Somatic article-writing engine while unvalidated. Somatic production continues under owner-thought realization/source integrity. Experimental prose cannot enter the article merely because it tests Human.
