# Somatic Introduction Human-Consistency Qualification Protocol — 2026-09-01

Status: ACTIVE owner-directed extension of the non-authoritative Somatic Introduction live-composition experiment. This protocol does not authorize Pangram, candidate promotion, registered-master edits, source reconciliation, publication, or owner-final status.

## Corrected trigger

The 55-word exploratory candidate beginning `Sometimes there is just nothing useful left to explain...` was initially recorded as PASS / human-leaning. Joel's immediate neutral challenge — whether Chat actually believed it looked human — exposed that the PASS was false. Literal reread showed a tidy `reaction != incapacity -> visible intensity is misleading -> three-part readiness rubric` architecture.

That PASS is retracted and cannot seed qualification. The evaluator failure is governed by `BLINDED-EVAL-VERDICT-GATE-20260901.md`.

A future genuine PASS still does not establish repeatability. Qualification begins only after a candidate survives the blinded cold-verdict procedure.

## Existing-work basis

Classification: **COMPOSE / ADAPT EXISTING MECHANISMS**, not a claimed novel evaluation framework.

Relevant established work already scanned for this task includes iterative self-feedback/refinement (Self-Refine; Reflexion), documented LLM-as-judge bias/self-preference, standard blinded-assessor bias control for subjective judgments, and the repository's own independent-final-reader rule for saturated-context anchoring.

Decision: reuse the current `eval` repair loop, current Chat/Codex role boundary, GitHub-canonical recovery, blinded verdict-first evaluation, and fresh-context verification. Do not use an unlimited self-critique loop or a prose-style score.

## Mandatory evaluator gate

Every qualification `eval` must apply:

`tasks/somatic-r15-clean-continuation-20260830/BLINDED-EVAL-VERDICT-GATE-20260901.md`

The critical ordering is:

1. recover canonical article/task authority and exact candidate;
2. **do not read qualification counters, PASS streak, phase, or consequences yet**;
3. cold-read the literal candidate;
4. freeze PASS / FAIL / UNCERTAIN and the strongest credible defect if one exists;
5. only then read qualification state and apply bookkeeping.

PASS means the passage still looks naturally human after the strongest-plausible-defect attack and Chat would be genuinely surprised by an immediate owner challenge that it looks visibly AI-shaped. `A human could have written this` is insufficient.

UNCERTAIN does not advance a streak.

If a neutral owner challenge immediately exposes that Chat does not actually believe its recorded PASS, retract the PASS, reset the streak, persist the evaluator failure, and return to ADAPTATION.

## Qualification state machine

### A. ADAPTATION

Entered whenever the current candidate cold-FAILs, is UNCERTAIN, or a prior PASS is retracted.

1. Run the standing full `eval`: literal defect -> causal generation diagnosis -> smallest reusable mechanism repair -> GitHub persistence -> fresh >=50-word retry.
2. Reset all consecutive-PASS streaks to zero.
3. Any mechanism repair invalidates the prior frozen mechanism identity.
4. The retry becomes the next exact eval target.
5. Do not run Pangram or promote prose.

### B. SAME-CONTEXT QUALIFICATION

Entered only after a candidate genuinely cold-PASSes under the blinded verdict gate.

1. Do not invent a defect and do not modify the mechanism after a genuine PASS.
2. Freeze the complete active generation mechanism identity for the qualification streak.
3. Count the PASS.
4. Immediately generate one fresh >=50-word exploratory candidate under the **unchanged frozen mechanism**. Do not evaluate that new candidate in the same response; it becomes the next `eval` target.
5. Repeat until **5 consecutive cold PASSes** exist under the same mechanism identity.
6. Any FAIL or UNCERTAIN invalidates the streak and returns to ADAPTATION.

### C. FRESH-CONTEXT VERIFICATION

As soon as the fifth consecutive same-context PASS is recorded, hand off immediately to a genuinely fresh Chat even if the ordinary 20-cycle limit has not been reached.

The fresh Chat must:

1. recover GitHub canonical state fresh;
2. receive the exact pending candidate but not prior critic rationales beyond what current GitHub recovery requires;
3. keep the generation mechanism frozen;
4. apply the blinded verdict gate before seeing counters/consequences;
5. require **3 consecutive additional cold PASSes** under that unchanged mechanism.

Any FAIL or UNCERTAIN resets qualification and returns to ADAPTATION in the fresh context.

### D. QUALIFIED_CONSISTENT

Set only when all are true:

- 5 consecutive PASSes occurred under one frozen mechanism before fresh-context verification;
- 3 consecutive additional PASSes occurred in a genuinely fresh Chat under the exact same frozen mechanism;
- no mechanism repair occurred anywhere inside those eight consecutive PASSes;
- every evaluated candidate was a fresh complete >=50-word exploratory candidate;
- every PASS used the blinded verdict-first ordering;
- no candidate was detector-tested or promoted during qualification.

`QUALIFIED_CONSISTENT` means only: **this internal cold-eval protocol has observed repeatable human-leaning paragraph generation across two Chat contexts.** It does not prove human authorship, detector success, publication readiness, semantic reconciliation, or article-level fidelity.

## Standing `eval` semantics during qualification

- **FAIL:** diagnose -> repair -> persist -> retry >=50 words; reset streak.
- **UNCERTAIN:** treat as non-qualifying -> diagnose strongest credible process risk -> repair when causal -> retry >=50 words; reset streak.
- **PASS:** do not diagnose or repair; increment streak; immediately produce a fresh >=50-word candidate under the unchanged mechanism for the next eval.

The fresh candidate at the end of a PASS response is **not evaluated in that same response**. This prevents hidden multi-candidate self-selection.

## Candidate diversity boundary

Qualification should not prove only that one sentence pattern can be reproduced.

- Fresh candidates may begin from different genuinely live pre-propositional pressures within the permitted exploratory Somatic Introduction field.
- Do not use the source-function list as a coverage schedule.
- Do not deliberately vary syntax, vocabulary, or topics merely to game diversity.
- Source-card occlusion, provisional buffering, writer-blind length control, contrastive attention, and reserve atomization remain controlling when active.

## Handoff policy

- One eval cycle = one owner/Codex `eval` message plus the completed Chat reply.
- A single Chat may process at most **20 completed eval cycles** before handoff.
- Handoff earlier when the 5-PASS same-context threshold is reached.
- The handoff packet is never authority. It must tell the new Chat to read GitHub fresh and include only the minimum exact pending candidate/counter state needed to resume.
- The new Chat starts by performing the pending `eval`, not by summarizing the packet.

## Codex boundary

Codex may mechanically send `eval`, wait for completion, read GitHub state, count cycles, construct a handoff from recorded state, and open/paste into a fresh Chat when required.

Codex may not judge prose, diagnose failure, choose/repair the mechanism, generate/rewrite article prose, decide whether a PASS is legitimate, run Pangram/detectors, alter article authority/master/locks/evidence, or infer missing state when GitHub disagrees or is unavailable.

## Stop conditions

The mechanical loop stops on the first of:

1. qualification becomes `QUALIFIED_CONSISTENT`;
2. Joel explicitly stops or changes the task;
3. GitHub canonical state cannot be read;
4. Chat returns an explicit owner-decision blocker;
5. a mechanical/browser failure prevents reliable continuation or handoff.

On stop, Codex reports exact state and does not invent a workaround.