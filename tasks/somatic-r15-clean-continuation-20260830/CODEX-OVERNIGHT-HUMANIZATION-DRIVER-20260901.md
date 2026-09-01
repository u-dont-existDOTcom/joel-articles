# Codex Overnight Humanization Driver — Somatic Introduction — 2026-09-01

Status: OWNER-DIRECTED MECHANICAL OVERNIGHT DRIVER.

Codex executes mechanics. The assigned evaluator Chat owns prose judgment, causal diagnosis, strategy, and writer-packet authoring. Fresh isolated writer contexts produce experimental prose. GitHub is canonical.

## Owner outcome for this run

Determine whether the Somatic Introduction generation problem can make real progress overnight when:

1. candidate generation is physically isolated from evaluation;
2. Pangram 4 is checked only after the evaluator Chat genuinely cold-PASSes a candidate;
3. the whole strategy is audited every 5–10 eval turns (default: every 7), with authority to radically reset rather than endlessly tweak local rules;
4. n8n and Nous Research Hermes Agent are actually trialed as experimental orchestration/independent-agent components.

Do not claim article humanization success from a short paragraph. This is a mechanism-discovery experiment.

## Canonical repositories

### Article / task authority

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Read fresh in the current `SKILL.md` / `CANONICAL-REPO-MAP.md` order, then at minimum:

- `articles/somatic-therapies/CURRENT-STATE.md`
- `tasks/somatic-r15-clean-continuation-20260830/HUMANIZATION-CONTROL-STATE-20260831.json`
- `tasks/somatic-r15-clean-continuation-20260830/BLINDED-EVAL-VERDICT-GATE-20260901.md`
- `tasks/somatic-r15-clean-continuation-20260830/STRATEGY-META-AUDIT-AND-RADICAL-RESET-20260901.md`
- `tasks/somatic-r15-clean-continuation-20260830/PHYSICALLY-ISOLATED-WRITER-EXPERIMENT-20260901.md`
- `tasks/somatic-r15-clean-continuation-20260830/OVERNIGHT-EVALUATOR-PROTOCOL-20260901.md`
- `tasks/somatic-r15-clean-continuation-20260830/OVERNIGHT-HUMANIZATION-STATE-20260901.json`

### Detector authority

Repository: `u-dont-existDOTcom/pangram-humanization-lab`

Read fresh:

1. `README.md`
2. `state/CURRENT-STATE.md`
3. `state/WORKING-LESSONS.md`
4. exact cache/reservation/history material required for a candidate before any paid call.

Never infer detector availability, call count, or ambiguity from chat.

## Hard role boundary

### Evaluator/supervisor Chat alone may

- cold-PASS / cold-FAIL / mark UNCERTAIN;
- diagnose why generation failed;
- author the next minimal positive writer packet;
- decide strategy audit disposition;
- accept/reject Hermes strategy advice;
- authorize Pangram for an exact candidate after PASS;
- decide whether an editorial/Pangram mismatch changes strategy.

### Codex may

- operate browser/Chat/terminal mechanics;
- read/write experiment state exactly as authorized by Chat protocols;
- launch fresh writer contexts with exact packets;
- capture exact writer output without editing;
- compute hashes/word counts mechanically;
- submit exact authorized Pangram measurements under the lab safeguards;
- set up/run n8n and Hermes shadow infrastructure;
- perform evaluator handoffs;
- stop on inconsistency.

### Codex may not

- judge prose;
- rewrite candidate text;
- invent a writer packet;
- decide a strategy audit result;
- token-hunt after Pangram;
- promote article prose;
- alter registered master/locks/evidence/article hashes;
- import unrelated Human donor prose.

## Phase 0 — recover and verify

1. Recover GitHub state fresh.
2. Confirm the registered Somatic master remains unchanged authority.
3. Confirm `OVERNIGHT-HUMANIZATION-STATE-20260901.json` says `READY_TO_START` or a later resumable state.
4. Recover exact Pangram cache/reservation state before any call.
5. Reuse the current evaluator Chat if this driver is starting from the current thread. Do not feed it old rejected rationales beyond GitHub-required recovery.

## Phase 1 — set up the shadow infrastructure

This setup must not block the primary fresh-Chat writer loop if an optional component fails.

### n8n

Purpose: deterministic workflow/state separation, not editorial intelligence.

1. If a working n8n instance already exists, use it only after verifying it is the intended local/private instance.
2. Otherwise create a disposable/self-hosted **localhost-only** n8n experiment using the current official n8n installation guidance. Do not expose it to the public Internet and do not create an unauthenticated public webhook.
3. Create a small project/workflow family for this experiment with separate executions/sub-workflows representing:
   - `writer_request`
   - `writer_result`
   - `cold_verdict_recorded`
   - `pangram_if_authorized`
   - `strategy_audit_due`
   - `handoff_due`
4. GitHub remains source of truth. Store only execution IDs, hashes, lane labels, counters, and non-secret routing metadata in n8n unless a current GitHub protocol explicitly permits more.
5. Do not put Pangram/OpenRouter/GitHub/API secrets in the repository or Chat messages.

Current n8n capability expected from official documentation includes sub-workflow execution, AI/tool workflow nodes, MCP exposure/access, and worker/queue execution. Use only the minimum needed here.

### Hermes Agent

Use the official Nous Research Hermes Agent distribution/documentation only.

1. If Hermes already exists, verify its version/configuration and create a **dedicated clean experimental home/workspace** for this run so prior memories/skills cannot contaminate the writer.
2. If installation is required, use the current official installation method and keep credentials outside Git.
3. Hermes currently supports isolated/subagent workflows and multiple model providers including OpenRouter and OpenAI Codex/ChatGPT OAuth. Prefer the same intended model/provider as the fresh-Chat writer when available; otherwise label the lane as an alternate-model experiment.
4. For n8n integration, Hermes currently provides a Nous-approved n8n MCP catalog entry (`hermes mcp install n8n`). Use it only against the local/private experiment instance.
5. Writer trials must use a fresh/segregated context with persistent learning/memory disabled or isolated. If that cannot be guaranteed, mark the writer trial `CONTAMINATED` and do not use it as evidence for physical isolation.
6. Hermes strategy-adviser and Hermes writer contexts must be separate from each other.

If n8n or Hermes setup requires a new owner login/credential interaction that cannot be completed unattended, record `OPTIONAL_SHADOW_SETUP_BLOCKED` and continue the primary fresh-Chat writer loop. Do not improvise credentials.

## Phase 2 — primary candidate/eval loop

Repeat until a stop condition.

### Step A — obtain the next writer packet

Read `OVERNIGHT-HUMANIZATION-STATE-20260901.json` fresh.

The `next_writer_packet` must have been authored/persisted by the evaluator Chat. Codex does not modify its semantics.

### Step B — launch an isolated writer

Default lane: `FRESH_CHAT_SAME_MODEL`.

1. Open a genuinely fresh Chat thread for the writer, using the same Joel Article Project only if necessary for access, but do not include prior conversation history.
2. Use the same intended reasoning model/configuration as the evaluator/writer baseline when available.
3. Send only the exact writer packet plus the generic role boundary in `PHYSICALLY-ISOLATED-WRITER-EXPERIMENT-20260901.md`.
4. Capture exactly one complete >=50-word candidate.
5. Do not ask the writer to self-evaluate, humanize against a blacklist, or explain its reasoning.
6. Do not send writer rationale/scratch to the evaluator.

At least once in each strategy epoch, run a `HERMES_SAME_MODEL_OR_PROVIDER` shadow writer from the **same writer packet**. Record it separately; do not silently substitute it for the primary lane. If exact model equivalence is unavailable, label `HERMES_ALTERNATE_MODEL`.

Within the first three writer cycles of epoch 1, ensure at least one usable Hermes shadow candidate is produced if setup permits.

### Step C — record exact candidate identity

Mechanically compute word count and SHA-256. Record:

- candidate text;
- exact hash;
- word count;
- writer lane/runtime/model/provider;
- writer packet ID;
- strategy epoch.

Do not alter the text.

### Step D — send candidate to evaluator Chat

Send exactly:

```text
eval

<exact candidate>
```

Do not include lane identity, writer rationale, Pangram state, counters, expected verdict, or strategy consequences.

Wait for the evaluator Chat to finish all GitHub writes before reading state again.

### Step E — act on persisted verdict

Read state fresh.

#### FAIL / UNCERTAIN

- no Pangram call;
- verify the evaluator persisted the causal diagnosis and next writer packet;
- increment mechanical counters only after persisted state is coherent;
- continue to the next isolated writer unless strategy audit/handoff is due.

#### PASS

- verify the evaluator persisted exact-hash Pangram authorization;
- do not generate another candidate yet;
- proceed to Phase 3.

## Phase 3 — Pangram after genuine cold PASS

Owner authorization for this overnight experiment: **Pangram may be run on an exact candidate only after Chat has frozen a genuine cold PASS and persisted exact-hash authorization.**

### Safety

1. Read Pangram lab current state and exact cache/reservation state fresh.
2. Reuse a completed exact Pangram-4 result if present; count it as a cache hit, not a paid call.
3. Resume a checkpointed/ambiguous exact request rather than buying a repeat.
4. Never repeat an ambiguous GUI/API action without recovery.
5. Require Pangram 4 / returned version `4.0`.
6. Preserve exact submitted UTF-8 text/hash/word count.
7. Maximum **6 new paid Pangram calls** for this overnight experiment unless Joel explicitly expands the existing cap. Cache hits do not count as new paid calls.

### Transport

This is repeated programmatic overnight work, not an explicit request to watch the GUI.

- Prefer the current normal trusted programmatic/self-hosted Pangram route documented by `pangram-humanization-lab` when operational.
- If that route is unavailable and the existing authenticated local Playwright route is the supported recoverable option, use the current dedicated Pangram automation profile and the owner's background/reuse-tab preference.
- Do not invent a new transport and do not use the legacy GitHub-hosted API origin known to have the 401 incompatibility.

### Return result to evaluator

Send only:

```text
PANGRAM_RESULT_FOR_COLD_PASS
candidate_sha256: <sha>
pangram_version: 4.0
human: <fraction>
ai: <fraction>
ai_assisted: <fraction>
confidence/status: <if available>
```

No Codex interpretation.

Wait for the evaluator Chat to persist the resulting strategy/writer-packet state before continuing.

## Phase 4 — strategy meta-audit every 7 eval cycles

Run after every 7 completed eval cycles since the previous strategy audit, within the owner-requested 5–10 range.

Run earlier on any trigger recorded in overnight state.

### Mechanical audit packet

Construct an outcome-only packet from GitHub:

- verdict sequence;
- Pangram results on cold-PASS candidates;
- false-PASS retractions;
- strategy/mechanism changes;
- recurring failure families;
- number of new local gates;
- whether any mechanism/architecture survived >=3 trials unchanged;
- fresh-Chat versus Hermes lane results;
- whether any candidate achieved cold PASS + Pangram Human.

Do not ask Codex to decide strategy.

### Hermes shadow strategist

If available, run a **clean Hermes strategy context** on this outcome packet and current high-level architecture. Ask for:

- `CONTINUE`
- `SIMPLIFY`
- `RADICAL_RESET`
- `ABANDON_LANE`

plus strongest causal reason and one bounded alternative if reset is recommended.

Record the raw advice as experimental evidence. Do not let Hermes mutate article/task authority.

### Evaluator strategy decision

Then send the evaluator Chat:

```text
STRATEGY_META_AUDIT_DUE
<outcome packet>

HERMES_SHADOW_ADVICE
<exact advice or SETUP_BLOCKED>
```

The evaluator Chat must issue the authoritative strategy disposition under `STRATEGY-META-AUDIT-AND-RADICAL-RESET-20260901.md`.

If `CONTINUE`, resume.

If `SIMPLIFY_OR_ROLL_BACK`, execute only the exact persisted architectural change.

If `RADICAL_RESET`, stop normal candidate generation until Chat persists a genuinely different architecture. Do not turn it into another wording ban.

If `ABANDON_LANE`, stop and report unless another next lane is already explicitly authorized.

## Phase 5 — evaluator Chat handoff

At **20 completed eval cycles in one evaluator Chat**, hand off before another `eval`.

Handoff earlier if the strategy auditor records context saturation or fresh-context verification is otherwise required.

### Handoff packet

Rebuild from GitHub fresh. Include only:

- `THIS PACKET IS NOT AUTHORITY; GITHUB IS CANONICAL`;
- repo/branch;
- canonical recovery order;
- active overnight evaluator/strategy/physical-isolation protocols;
- overnight state path;
- exact pending candidate/event if one exists;
- counters and current strategy epoch;
- exact hard boundaries;
- instruction to perform the pending eval/event immediately after recovery.

Do not transplant the old conversation's critic rationales into the new evaluator unless required by a current GitHub file.

Reset per-chat counter after the new evaluator completes its first action.

## Overnight stopping conditions

Stop and leave a precise GitHub checkpoint when the first of these occurs:

1. the current strategy produces a convincing repeated breakthrough and Chat records a stop/review point;
2. the six-new-paid-call Pangram cap is reached;
3. 60 completed eval cycles are reached across evaluator handoffs;
4. GitHub canonical state becomes unavailable/contradictory;
5. Pangram ambiguity cannot be safely recovered;
6. evaluator Chat requests an owner decision;
7. strategy disposition becomes `ABANDON_LANE` with no authorized successor;
8. browser/runtime failure makes reliable continuation impossible;
9. n8n/Hermes setup would require exposing secrets or unauthorized public network access.

Optional n8n/Hermes setup failure alone does **not** stop the main fresh-Chat writer / evaluator / Pangram loop.

## End-of-run receipt

Persist and report:

- total eval cycles;
- evaluator handoffs;
- strategy audits and dispositions;
- candidate counts by writer lane;
- cold PASS/FAIL/UNCERTAIN counts;
- false-PASS retractions;
- exact Pangram results and paid/cache counts;
- whether n8n setup succeeded and what it actually orchestrated;
- whether Hermes setup succeeded, models/providers used, strategy advice, and writer outcomes;
- strongest evidence that the system improved or remained stuck;
- current recommended next architecture;
- confirmation that no registered-master edit, article promotion, or unrelated Human donor insertion occurred.