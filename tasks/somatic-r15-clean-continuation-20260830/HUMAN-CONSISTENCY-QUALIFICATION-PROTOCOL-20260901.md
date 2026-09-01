# Somatic Introduction Human-Consistency Qualification Protocol — 2026-09-01

Status: ACTIVE owner-directed extension of the non-authoritative Somatic Introduction live-composition experiment. This protocol does not authorize Pangram, candidate promotion, registered-master edits, source reconciliation, publication, or owner-final status.

## Trigger

The exploratory candidate beginning `Sometimes there is just nothing useful left to explain...` received a literal cold-read **PASS / human-leaning** on 2026-09-01: no credible AI-shaped defect could be justified without manufacturing one.

A single PASS does not establish repeatability. Continuing to force a defect from a passing candidate would also create a new failure mode: critic overfitting / manufactured objections.

## Independent conception snapshot before existing-work scan

- **Problem:** determine whether the repaired generation mechanism can produce human-looking exploratory paragraphs repeatedly rather than once by chance.
- **Mechanism candidate:** freeze the mechanism after a PASS; generate fresh candidates under that unchanged mechanism; apply the same cold `eval`; require a consecutive streak; then verify in a fresh Chat context to reduce same-context anchoring.
- **Constraints:** Chat remains the sole prose evaluator/writer/strategy owner; Codex is mechanical only; no Pangram; no article-authority mutation; retries remain >=50 words; handoff after at most 20 completed eval cycles in one Chat; direct owner instructions outrank this protocol.
- **Risk:** an unlimited same-model self-eval loop can teach the critic to manufacture increasingly fine objections or become self-preferential, so the qualification phase needs a fixed pass rule and context reset.

## Existing-work scan and build decision

Classification: **COMPOSE / ADAPT EXISTING MECHANISMS**, not a claimed novel evaluation framework.

Relevant established work:

- Madaan et al., *Self-Refine: Iterative Refinement with Self-Feedback* (2023), demonstrates useful iterative feedback/refinement without weight updates.
- Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning* (2023), demonstrates episodic linguistic feedback improving repeated task performance.
- LLM-as-a-judge bias studies including Chen et al. (2024) and Ye et al. (2024) show that model judgments remain vulnerable to systematic biases; subjective prose evaluation is therefore not safe to treat as infallible ground truth.
- The repository's existing independent-final-reader rule already recognizes saturated-context anchoring and requires genuinely fresh context when its marginal value matters.

Repository scan found no existing Somatic-specific continuous `eval`/20-turn handoff protocol to reuse directly.

Decision: reuse the current `eval` repair loop, current Chat/Codex role boundary, current GitHub-canonical recovery model, and fresh-context audit principle. Add only a small qualification state machine and mechanical Codex driver.

## Qualification state machine

### A. ADAPTATION

Entered whenever the current candidate cold-FAILs.

1. Run the standing full `eval`: literal defect -> causal generation diagnosis -> smallest reusable mechanism repair -> GitHub persistence -> fresh >=50-word retry.
2. Reset all consecutive-PASS streaks to zero.
3. The retry becomes the next exact eval target.
4. Do not run Pangram or promote prose.

### B. SAME-CONTEXT QUALIFICATION

Entered when a candidate cold-PASSes with no credible AI-shaped defect.

1. **Do not invent a defect and do not modify the mechanism.**
2. Freeze the complete active generation mechanism identity for the qualification streak.
3. Count the PASS.
4. Immediately generate one fresh >=50-word exploratory candidate under the **unchanged frozen mechanism**. Do not evaluate that new candidate in the same response; it becomes the next `eval` target.
5. Repeat until **5 consecutive cold PASSes** exist under the same mechanism identity.
6. Any FAIL invalidates the streak and returns to ADAPTATION.

### C. FRESH-CONTEXT VERIFICATION

As soon as the fifth consecutive same-context PASS is recorded, hand off immediately to a new Chat even if the ordinary 20-cycle handoff limit has not been reached.

The fresh Chat must:

1. recover GitHub canonical state fresh;
2. receive the exact pending candidate but not the prior critic rationales except what current GitHub recovery requires;
3. keep the generation mechanism frozen;
4. run the same literal `eval` rule;
5. require **3 consecutive additional cold PASSes** under that unchanged mechanism.

Any FAIL resets the qualification result and returns to ADAPTATION in the current fresh context.

### D. QUALIFIED_CONSISTENT

Set only when all are true:

- 5 consecutive PASSes occurred under one frozen mechanism before fresh-context verification;
- 3 consecutive additional PASSes occurred in a genuinely fresh Chat under the exact same frozen mechanism;
- no mechanism repair occurred anywhere inside those eight consecutive PASSes;
- every evaluated candidate was a fresh complete >=50-word exploratory candidate;
- no candidate was detector-tested or promoted during qualification.

`QUALIFIED_CONSISTENT` means only: **this internal cold-eval protocol has observed repeatable human-leaning paragraph generation across two Chat contexts.** It does not prove human authorship, detector success, publication readiness, semantic reconciliation, or article-level fidelity.

## Standing `eval` semantics during qualification

During this qualification phase, `eval` retains the existing FAIL behavior but gains one explicit PASS continuation rule:

- **FAIL:** diagnose -> repair -> persist -> retry >=50 words; reset streak.
- **PASS:** do not diagnose or repair; increment streak; immediately produce a fresh >=50-word candidate under the unchanged mechanism for the next eval.

The fresh candidate at the end of a PASS response is **not evaluated in that same response**. This prevents a hidden multi-candidate self-selection loop.

## Candidate diversity boundary

Qualification should not prove only that one sentence pattern can be reproduced.

- Fresh candidates may begin from different genuinely live pre-propositional pressures within the permitted exploratory Somatic Introduction field.
- Do not use the source-function list as a coverage schedule.
- Do not deliberately vary syntax, vocabulary, or topics merely to game diversity.
- The existing source-card occlusion, provisional-buffer, writer-blind controller, and contrastive-attention rules remain controlling.

## Handoff policy

- Define one **eval cycle** as one owner/Codex `eval` message plus the completed Chat reply.
- A single Chat may process at most **20 completed eval cycles** before handoff.
- Handoff earlier when the 5-PASS same-context threshold is reached, because fresh-context verification is then required.
- The handoff packet is never authority. It must tell the new Chat to read GitHub fresh and include only the minimum exact pending candidate/counter state needed to resume.
- The new Chat starts by performing the pending `eval`, not by summarizing the packet.

## Codex boundary

Codex may mechanically:

- send `eval`;
- wait for the reply to finish;
- read GitHub qualification state;
- count completed eval cycles;
- construct a handoff packet from GitHub-recorded state;
- open a new Chat and paste that packet when required.

Codex may **not**:

- judge whether prose is human/AI-shaped;
- diagnose a failure;
- choose or repair the generation mechanism;
- generate or rewrite article prose;
- decide whether a PASS is legitimate;
- run Pangram or any detector;
- alter registered article authority/master/locks/evidence;
- infer missing state from remembered UI/chat when GitHub disagrees or is unavailable.

## Stop conditions

The mechanical loop stops on the first of:

1. qualification state becomes `QUALIFIED_CONSISTENT`;
2. Joel explicitly stops or changes the task;
3. GitHub canonical state cannot be read;
4. Chat returns an explicit owner-decision blocker;
5. a mechanical/browser failure prevents reliable continuation or handoff.

On a stop, Codex reports the exact state and does not invent a workaround.