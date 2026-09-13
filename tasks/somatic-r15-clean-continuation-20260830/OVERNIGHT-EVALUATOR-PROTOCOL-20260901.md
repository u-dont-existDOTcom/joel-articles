# Somatic Introduction Overnight Evaluator Protocol — 2026-09-01

Status: ACTIVE owner-directed protocol for the overnight physical-isolation experiment. Chat owns all editorial/strategy reasoning. Codex owns mechanics. GitHub remains canonical.

## `eval` input contract

During the overnight experiment, Codex sends the evaluator Chat:

```text
eval

<EXACT CANDIDATE ONLY>
```

The message must not include writer identity, runtime/model lane, writer rationale, PASS counters, Pangram state, prior critic rationale, or what a PASS would trigger.

The evaluator recovers article/task authority fresh but follows `BLINDED-EVAL-VERDICT-GATE-20260901.md`: **freeze the literal prose verdict before reading `OVERNIGHT-HUMANIZATION-STATE-20260901.json` counters or consequences.**

## Verdict

Return and internally freeze one of:

- `PASS`
- `FAIL`
- `UNCERTAIN`

PASS burden remains high: Chat must actually believe the candidate looks naturally human and would be genuinely surprised by an immediate neutral owner challenge that it looks visibly AI-shaped.

FAIL requires a concrete literal defect Chat actually believes is visible.

UNCERTAIN is non-qualifying and receives no Pangram call.

## After verdict is frozen

Only then read the overnight state and current mechanism/strategy artifacts.

### On FAIL / UNCERTAIN

1. Identify the strongest literal defect.
2. Diagnose the causal generation/architecture failure.
3. Decide whether this is:
   - local mechanism evidence inside the current physical-isolation epoch; or
   - an early trigger for `STRATEGY-META-AUDIT-AND-RADICAL-RESET-20260901.md`.
4. Do not automatically add another local prose prohibition. The current epoch was created specifically to test architecture-level isolation.
5. Persist the verdict, causal diagnosis, counters, strategy-audit due state, and the next **minimal positive writer packet** into `OVERNIGHT-HUMANIZATION-STATE-20260901.json`.
6. Do **not** write the retry candidate in the evaluator Chat. Candidate generation belongs to a fresh isolated writer execution.
7. No Pangram authorization.

### On PASS

1. Do not modify the writer mechanism merely because the candidate passed.
2. Persist the exact candidate SHA-256/text/word count and set:

   `pending_pangram_authorization.status = PANGRAM_AUTHORIZED_FOR_EXACT_HASH`

3. Do not generate the next candidate yet.
4. Codex runs the exact candidate through Pangram 4 under current lab safety rules.
5. Wait for a separate detector-result message before deciding the next writer packet/strategy move.

## Detector-result input contract

After an authorized Pangram run, Codex sends:

```text
PANGRAM_RESULT_FOR_COLD_PASS
candidate_sha256: <exact sha>
pangram_version: 4.0
human: <fraction>
ai: <fraction>
ai_assisted: <fraction>
confidence/status: <if available>
```

No extra Codex interpretation.

## Handling detector results

### Pangram Human

Treat as a joint editorial+detector success **for this short experimental boundary only**.

- Record result and counters.
- Freeze the generation architecture unless there is an independent editorial reason to change it.
- Create the next minimal positive writer packet for another physically isolated candidate.
- Do not promote or semantically reconcile the candidate.

### Pangram AI / Mixed

Treat as an editorial-detector mismatch, not a command to token-hunt.

- Preserve the exact detector evidence.
- Diagnose whether the cold evaluator missed a structural signal or whether the short-boundary detector result is plausibly noisy/contextual.
- A second cold-PASS/Pangram-AI-or-Mixed mismatch in the same strategy epoch triggers an immediate strategy meta-audit.
- Do not generate one-variable lexical variants unless a later explicit detector-research experiment authorizes them.
- Persist the next strategy decision/writer packet only after the diagnosis.

## Meta-audit timing

Run a strategy audit when either:

- `completed_eval_cycles_since_strategy_audit >= 7`; or
- any early trigger in `OVERNIGHT-HUMANIZATION-STATE-20260901.json` is met.

The strategy audit asks whether the whole architecture is paying off. It may decide `CONTINUE_CURRENT_ARCHITECTURE`, `SIMPLIFY_OR_ROLL_BACK`, `RADICAL_RESET`, or `ABANDON_LANE`.

Before the final strategy disposition, use the Hermes shadow strategist when mechanically available. Hermes advice is evidence only; Chat owns the decision.

## Handoff

At 20 completed eval cycles in one evaluator Chat, or earlier if the strategy auditor declares context saturation, Codex opens a genuinely fresh evaluator Chat and transfers only a GitHub-canonical recovery packet plus the exact pending candidate/event needed next.

Do not transfer prior chat rationales unless a currently active GitHub protocol requires them.

## Hard boundaries

- No registered-master edit.
- No article promotion.
- No source reconciliation during this experiment unless Joel explicitly changes the task.
- No invented autobiography/factual specificity.
- No unrelated Human donor prose.
- No Pangram on FAIL/UNCERTAIN.
- No repeated/ambiguous Pangram call.
- No more new paid Pangram calls than the current overnight state cap.
- Short-paragraph Pangram success is research evidence, not article-level certification.