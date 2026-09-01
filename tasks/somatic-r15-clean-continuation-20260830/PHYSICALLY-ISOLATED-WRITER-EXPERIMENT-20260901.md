# Somatic Introduction Physically Isolated Writer Experiment — 2026-09-01

Status: ACTIVE RADICAL-RESET EXPERIMENT. Non-authoritative. No article promotion, registered-master edits, source reconciliation, or detector-driven publication changes are authorized.

## Why this experiment exists

The prior lane attempted to simulate writer/critic/scheduler separation inside one saturated Chat context. It accumulated many increasingly specific controls, yet new candidates continued to exhibit adjacent forms of model-shaped closure and the evaluator produced one false PASS. The current strategy meta-audit therefore selected a physical architecture change rather than another same-context prose rule.

## Core hypothesis

A major part of the failure may come from **information contamination** rather than an insufficient blacklist: the same model context knows the source obligations, rejected patterns, evaluator criteria, minimum length, prior failures, and desired outcome even when prompts tell individual roles to ignore them.

Test whether genuinely separate executions improve prose by physically isolating:

1. strategy/supervision;
2. candidate generation;
3. cold evaluation;
4. detector measurement.

## Roles

### A. Supervisor / evaluator Chat

The assigned Joel Article Chat owns:

- the cold human/AI-shape verdict;
- causal diagnosis after FAIL or detector mismatch;
- strategy decisions;
- semantic/editorial authority;
- the minimal positive writer packet;
- any decision to freeze, continue, simplify, or replace a mechanism.

It does **not** produce the candidate it will immediately evaluate during this experiment.

Before a cold verdict it must follow `BLINDED-EVAL-VERDICT-GATE-20260901.md`: no PASS counters, Pangram consequences, writer rationale, or writer scratch before verdict freeze.

### B. Isolated writer

Each candidate is generated in a **fresh context/process**. Preferred implementations, in order of experimental comparability:

1. fresh Chat thread using the same intended reasoning model/configuration when mechanically available;
2. Hermes Agent clean per-run writer using the same model through an available provider when possible;
3. another explicitly recorded model only as a separate lane, never silently treated as equivalent.

The writer receives only:

- this is exploratory Somatic Introduction prose;
- the currently authorized semantic field or one small positive live-pressure packet supplied by the supervisor;
- no invented autobiography, symptoms, chronology, evidence, or unauthorized factual specificity;
- no requirement to cover all source functions in this discovery pass;
- source reconciliation occurs later;
- one complete candidate is required and must be at least 50 words.

The writer must **not** receive:

- prior rejected candidates;
- AI-pattern/failure catalog;
- Pangram scores or detector words;
- qualification counters;
- expected PASS/FAIL outcome;
- critic rationale;
- source-coverage checklist;
- strategy-audit rationale;
- a request to imitate unrelated Human prose.

### C. Codex mechanical orchestrator

Codex:

- reads GitHub canonical state;
- creates the fresh writer context/process;
- sends the exact supervisor-authored writer packet;
- captures the exact returned candidate without editing it;
- computes/records exact text identity mechanically;
- delivers only the candidate to the evaluator Chat for `eval`;
- runs Pangram only after an explicit persisted cold PASS authorization;
- performs handoffs and invokes strategy-audit mechanics.

Codex never evaluates or rewrites prose.

### D. n8n experimental orchestrator

n8n is tested in **shadow/orchestration mode** first. It is not the source of truth.

Create a localhost-only experimental workflow that can represent these state transitions as separate sub-workflows/executions:

1. `writer_request`
2. `writer_result`
3. `cold_verdict_recorded`
4. `pangram_if_authorized`
5. `strategy_audit_due`
6. `handoff_due`

GitHub remains canonical. n8n stores only execution IDs, hashes, role/lane labels, and non-secret routing metadata unless a task artifact explicitly authorizes more.

Use n8n sub-workflows where useful so writer, strategy-audit, and mechanical detector routing are separate executions. Do not give an n8n AI Agent authority to decide PASS/FAIL or article state.

Bind n8n to localhost/private network only for this experiment. Do not expose an unauthenticated public webhook.

### E. Hermes experimental runtime

Use Nous Research Hermes Agent in two bounded shadow functions:

#### Independent strategy challenger
At each 7-cycle strategy meta-audit, run a clean Hermes strategy context. Supply:

- outcome-level history since the last audit;
- current high-level architecture;
- mechanism churn counts;
- Pangram results only for cold-PASS candidates;
- the owner outcome and hard safety/authority boundaries.

Ask Hermes to return one of `CONTINUE`, `SIMPLIFY`, `RADICAL_RESET`, or `ABANDON_LANE`, plus the strongest causal reason and one bounded alternative architecture if reset is recommended.

The supervisor Chat independently decides whether to accept that recommendation.

#### Shadow writer
At least once per strategy epoch, generate one candidate through a clean Hermes writer context using the same minimal positive writer packet as the fresh-Chat writer lane. Label the runtime/model/provider exactly. Do not let Hermes memory/skills from critic or strategy tasks leak into the writer lane.

Use a fresh workspace/agent identity or otherwise disable/segregate persistent learning and conversation memory for writer trials. If that cannot be guaranteed, label the trial contaminated and do not use it to judge physical isolation.

## Candidate routing

A normal cycle under this experiment is:

1. Supervisor persists a minimal positive `writer_packet` and mechanism/epoch identity.
2. Codex creates a fresh writer execution.
3. Writer returns one exact >=50-word candidate.
4. Codex records exact text + hash and sends only the candidate with `eval` to the evaluator Chat.
5. Evaluator freezes PASS/FAIL/UNCERTAIN before reading outcome counters.
6. FAIL/UNCERTAIN -> no Pangram; supervisor diagnoses at mechanism/strategy level and persists the next writer packet.
7. PASS -> supervisor persists `PANGRAM_AUTHORIZED_FOR_EXACT_HASH`.
8. Codex performs one cache-safe Pangram 4 measurement for that exact hash.
9. Result returns to supervisor as a separate detector-evidence event.
10. Supervisor either freezes the successful mechanism or diagnoses the editorial/detector mismatch. No phrase hunting.

## A/B identity

Do not silently mix writer runtimes.

Each candidate record must name one lane:

- `FRESH_CHAT_SAME_MODEL`
- `HERMES_SAME_MODEL_OR_PROVIDER`
- `HERMES_ALTERNATE_MODEL`
- `LEGACY_SAME_CONTEXT_BASELINE`

Comparisons across lanes are exploratory. A stronger Hermes result does not prove that its runtime should become publication authority.

## First-night benchmark

The overnight goal is not to finish the article. It is to determine whether physical isolation produces a qualitatively different outcome from the saturated same-context baseline.

Minimum useful evidence before concluding anything:

- at least 3 physically isolated writer candidates if execution permits;
- at least one Hermes shadow candidate;
- blinded cold verdicts for each;
- Pangram on every genuine cold PASS, subject to paid-call safety;
- one strategy meta-audit after 7 eval cycles or earlier trigger;
- explicit comparison against the legacy same-context failure pattern.

## Success signal

Strong evidence for this architecture would be:

- multiple fresh writer candidates that cold-PASS without same-context rule accretion;
- at least one cold PASS also scoring Human on Pangram 4;
- fewer mechanism mutations per candidate;
- evaluator verdicts that survive neutral owner-style challenge;
- no need to expose the writer to the failure catalog.

## Failure signal

Physical isolation is not automatically successful. Treat the architecture as falsified/weak if fresh writers reproduce the same polished closure structures, or if Hermes/n8n add operational complexity without better cold/Pangram outcomes.

Then the next meta-audit should consider a different representation/model/objective rather than merely more orchestration.