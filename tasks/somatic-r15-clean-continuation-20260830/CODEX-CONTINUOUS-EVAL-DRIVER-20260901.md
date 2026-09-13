# Codex Continuous Eval Driver — Somatic Introduction — 2026-09-01

Status: OWNER-DIRECTED MECHANICAL DRIVER. Codex executes browser/message/handoff mechanics only. Chat owns all prose, evaluation, causal diagnosis, mechanism repair, and qualification decisions.

## Objective

Keep presenting the current pending Somatic Introduction exploratory candidate to the assigned Chat with the command `eval` until GitHub state records `QUALIFIED_CONSISTENT`, while preserving the current fail-closed boundaries and handing off to a fresh Chat at the required intervals.

This driver does **not** authorize Codex to evaluate writing, generate prose, run Pangram, mutate article authority, or infer missing editorial state.

## Canonical recovery before starting

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Read fresh, in this order:

1. `SKILL.md`
2. `CANONICAL-REPO-MAP.md`
3. `AGENTS.md`
4. `docs/INDEX.md`
5. `state/CODEX-CURRENT-STATE.md`
6. `articles/INDEX.json`
7. `articles/somatic-therapies/CURRENT-STATE.md`
8. `tasks/somatic-r15-clean-continuation-20260830/HUMANIZATION-CONTROL-STATE-20260831.json`
9. `tasks/somatic-r15-clean-continuation-20260830/HUMAN-CONSISTENCY-QUALIFICATION-PROTOCOL-20260901.md`
10. `tasks/somatic-r15-clean-continuation-20260830/HUMAN-CONSISTENCY-QUALIFICATION-STATE-20260901.json`

Load only additional mechanism files named by current state when needed for handoff integrity. Do not substitute chat history for GitHub state.

## Role boundary

### Chat alone may

- cold-evaluate the literal candidate;
- return PASS or FAIL;
- decide whether a defect is credible;
- diagnose the causal generation failure;
- decide and write a mechanism repair;
- write the next exploratory candidate;
- update qualification/editorial state;
- decide whether the frozen mechanism changed and therefore whether a PASS streak resets.

### Codex may only

- send messages to Chat;
- wait for the full reply;
- read GitHub state after the reply;
- verify that the expected state transition was persisted;
- count completed eval cycles;
- create/open a fresh Chat when handoff is due;
- construct a non-authoritative handoff packet from GitHub-recorded facts;
- stop and report a mechanical/state inconsistency.

Codex must never perform editorial reasoning as a fallback.

## Main loop

One **eval cycle** = one Codex/user message containing `eval` plus the completed Chat reply.

Repeat:

1. Read `HUMAN-CONSISTENCY-QUALIFICATION-STATE-20260901.json` fresh.
2. Confirm `pending_eval_candidate` exists and status is not `QUALIFIED_CONSISTENT`.
3. Confirm the Chat is idle and its prior reply is complete.
4. Send exactly:

   `eval`

5. Wait until Chat's response is fully complete. Do not interrupt it and do not send another `eval` while tools/writes are still running.
6. Re-read the qualification state fresh from GitHub.
7. Verify that the completed cycle produced one mechanically coherent transition:
   - PASS -> streak incremented, frozen mechanism unchanged, and a new `pending_eval_candidate` exists; or
   - FAIL -> streak reset, Chat persisted any causal mechanism repair, and a new retry candidate exists; or
   - qualification became `FRESH_CONTEXT_VERIFICATION_REQUIRED` / equivalent; or
   - qualification became `QUALIFIED_CONSISTENT`; or
   - Chat recorded an explicit blocker/owner decision.
8. Increment the local completed-eval-cycle counter only after the GitHub transition is readable.
9. Continue automatically unless a stop or handoff condition below applies.

Do not parse prose quality yourself. GitHub state and Chat's persisted verdict control the loop.

## PASS handling

If GitHub records PASS:

- do not praise, critique, or reinterpret the candidate;
- do not alter any mechanism file;
- do not ask Chat for justification;
- do not resend the same candidate;
- use the newly persisted `pending_eval_candidate` as the next target and send the next `eval` automatically.

When the same-context streak reaches 5 consecutive PASSes under one frozen mechanism, **handoff immediately** for fresh-context verification even if fewer than 20 eval cycles have occurred in the current Chat.

## FAIL handling

If GitHub records FAIL:

- do not diagnose why;
- do not propose the fix;
- confirm Chat reset the streak and persisted the mechanism repair/retry as required by the qualification protocol;
- if those persisted artifacts exist, send the next `eval` automatically;
- if they do not, stop with `STATE_TRANSITION_MISSING` rather than inventing state.

A mechanism change invalidates the prior consecutive-PASS streak. Codex does not decide whether two mechanism versions are equivalent.

## Handoff rule

### Ordinary limit

A single Chat may process at most **20 completed eval cycles** under this driver.

At cycle 20, hand off before sending another `eval`.

### Early qualification handoff

Handoff immediately when the same-context qualification streak reaches 5 PASSes, because the next phase requires a genuinely fresh Chat. Do not wait for cycle 20.

### Handoff construction

Immediately before handoff:

1. Re-read all canonical recovery/state files listed above.
2. Read the exact pending candidate and all counters from `HUMAN-CONSISTENCY-QUALIFICATION-STATE-20260901.json`.
3. Do **not** copy old chat rationales, rejected prose, detector history, or the accumulated anti-pattern catalog unless the current GitHub read order explicitly requires a named mechanism file.
4. Create a concise handoff packet containing:
   - explicit statement: `THIS PACKET IS NOT AUTHORITY; GITHUB IS CANONICAL`;
   - repository and active branch;
   - required fresh recovery order;
   - qualification protocol/state paths;
   - current qualification phase and exact streak counters;
   - frozen mechanism identity/path list as recorded in state;
   - exact current `pending_eval_candidate` text, SHA-256, and word count;
   - exact hard boundaries: no Pangram, no promotion, no registered-master edit, no invented autobiography/factual specificity;
   - instruction that `eval` means the full current GitHub-defined eval loop;
   - instruction: `After recovery, immediately perform the pending eval. Do not merely summarize this packet.`
5. Open a **new Chat in the same Joel article Project** using the same intended reasoning model/configuration when available.
6. Paste the handoff packet as the first user message.
7. Wait for that Chat to complete the pending eval before resuming the ordinary `eval` loop.
8. Reset the local per-chat eval-cycle counter to zero after the handoff Chat has completed its first response.

The handoff packet is transport only. If it conflicts with fresh GitHub state, GitHub and current owner instructions win.

## Fresh-context verification

When GitHub state says the phase is fresh-context verification:

- the generation mechanism must remain frozen at the exact qualification identity;
- require 3 consecutive additional PASSes in the fresh Chat;
- each PASS must leave a new fresh pending candidate for the next `eval`;
- any FAIL resets qualification and returns to ADAPTATION; continue the normal loop from the repaired mechanism;
- do not treat the prior 5-PASS streak as sufficient after a fresh-context FAIL.

## Completion

Stop automatically when GitHub records `QUALIFIED_CONSISTENT`.

Return to the owner only a compact receipt containing:

- `QUALIFIED_CONSISTENT`;
- frozen mechanism identity;
- same-context PASS streak;
- fresh-context PASS streak;
- total eval cycles used;
- number of handoffs;
- confirmation: no Pangram call, no article promotion, no registered-master edit.

Do not continue generating candidates after qualification unless Joel explicitly asks.

## Hard stop conditions

Stop rather than improvise if any of these occurs:

- GitHub cannot be read;
- `pending_eval_candidate` is missing when another eval is required;
- Chat reply completed but required GitHub qualification state did not update;
- branch/current task changes unexpectedly;
- Chat asks for an owner decision;
- browser/Chat automation cannot reliably determine whether a response finished;
- a tool would require exposing credentials/secrets;
- any action would run Pangram/detector work or mutate registered article authority.

Report the exact blocker and last confirmed GitHub state.

## Browser interaction discipline

- Reuse the current Chat tab/session during a <=20-cycle run.
- Do not steal focus unnecessarily.
- Never send a second message while Chat is still generating or writing GitHub state.
- A handoff must use a genuinely new Chat thread, not a second prompt in the saturated thread.
- Do not delete old chats; the new thread is the continuation target.

## What Codex must never do

- Never write `PASS` or `FAIL` on its own.
- Never edit the candidate.
- Never ask another model to judge the prose instead of the assigned Chat.
- Never change a generation protocol because a phrase looks suspicious.
- Never run Pangram, call a detector, or spend detector credits.
- Never promote the exploratory candidate into `articles/somatic-therapies/master.html`.
- Never alter `OWNER-LOCKS.json`, `SOURCE-EVIDENCE.json`, detector evidence, or registered article hashes for this loop.
- Never silently reduce the 5+3 consistency threshold.
- Never continue past `QUALIFIED_CONSISTENT` without a new owner instruction.