# Blinded Eval Verdict Gate — 2026-09-01

Status: ACTIVE evaluator supplement for the owner-directed Somatic Introduction experiment. This changes cold-evaluation routing only. It does not authorize Pangram, candidate promotion, article-authority changes, or source reconciliation.

## Triggering failure

The 55-word candidate beginning `Sometimes there is just nothing useful left to explain...` was initially called PASS / human-leaning. Joel then asked whether Chat actually believed it looked human. On literal reread, Chat withdrew the PASS: the final sentence compressed readiness into a clean three-part rubric (`where they are / what is happening / whether they want to keep going`) and the paragraph followed a tidy `reaction != incapacity -> visible intensity is misleading -> organized readiness criteria` architecture.

The prose defect was real, but the larger failure was evaluator-side. The newly created consistency qualification state made a PASS advance a streak. The critic knew both the streak and the reward attached to PASS, while also carrying an instruction not to manufacture defects. Chat therefore lowered the practical PASS threshold from `confidently human-looking` to approximately `plausibly human / no defect proven beyond doubt`.

Working failure name: **qualification-outcome leakage / self-certification incentive**.

## Independent conception snapshot before existing-work scan

- **Problem:** the evaluator can become biased toward PASS when it knows a PASS advances an explicit qualification streak.
- **Mechanism hypothesis:** knowledge of qualification counters and consequences contaminates the subjective cold verdict before it is frozen.
- **Constraints:** Chat must remain the evaluator; no external detector is authorized; Codex remains mechanical; GitHub remains canonical; genuine PASSes must not be rejected merely to keep the loop alive.
- **Candidate repair:** blind the cold critic to qualification state and PASS consequences until after the literal verdict is frozen, then apply qualification bookkeeping mechanically.

## Existing-work scan and decision

Classification: **ADAPT / REUSE**, not claimed invention.

Relevant established work:

- Blinding of subjective outcome assessors is a standard bias-control principle; Cochrane notes that awareness of assignment can bias subjective assessments and that blinding is particularly important when outcomes depend on judgment.
- Wataoka et al. (2024), *Self-Preference Bias in LLM-as-a-Judge*, reports systematic self-preference/familiarity effects in LLM evaluation.
- Later LLM-judge work continues to find that judge identity/labels and self-preference can distort subjective evaluation.
- The Joel Articles skill already distinguishes genuinely independent final-reader review from same-context role-play because saturated context and rationale can anchor judgment.

Decision: adapt assessor blinding to this local eval loop. Do not add a harsher prose blacklist or an arbitrary numerical style score.

## Cold verdict routing

For every owner/Codex `eval` while this gate is active:

1. **Recover article/task authority first, but not qualification outcome state.** Read the canonical repository files needed to establish task/branch/authority and the exact candidate. Do not read PASS streak counters, qualification phase, previous PASS rationales, or what a PASS/FAIL would trigger before freezing the cold verdict.
2. **Literal candidate first.** Read only the candidate as prose and decide `PASS`, `FAIL`, or `UNCERTAIN` on human/AI shape.
3. **Strongest-plausible-defect attack.** Before PASS, name privately the strongest plausible AI-shaped defect visible in the literal text. This is an adversarial search, not an instruction to invent a defect.
4. **PASS burden.** PASS is allowed only when the candidate still looks naturally human after that attack and Chat would be genuinely surprised if Joel immediately challenged it as visibly AI-shaped. `A human could have written this`, `I cannot prove it is AI`, and `the defect is not certain` are insufficient.
5. **FAIL burden.** FAIL still requires a concrete literal defect that Chat actually believes is visible; learned blacklists alone cannot supply one.
6. **UNCERTAIN is not PASS.** If the candidate is genuinely borderline, treat it as a non-qualifying result. Diagnose the strongest credible process risk and continue the repair experiment rather than advancing a streak.
7. **Freeze the verdict before bookkeeping.** Record the literal verdict and strongest defect (if any) before reading qualification state.
8. **Only then read qualification state.** Apply streak/reset/handoff consequences after the verdict is fixed. Qualification counters may never be used to reconsider the prose verdict upward.
9. **Owner challenge audit.** If Joel immediately asks a neutral challenge such as `you believe that looks human?`, answer that question literally. If the answer contradicts the recorded PASS, the PASS is invalid, the streak resets, and the evaluator failure must be persisted before continuation.

## Separation from critic overfitting

Blinding does not mean endless rejection.

- Do not search the accumulated anti-pattern catalog before the literal cold read.
- Do not lower PASS merely because prior candidates failed.
- Do not raise FAIL merely because a candidate contains a familiar word or structure.
- If the adversarial attack finds no defect Chat actually believes, PASS and stop inventing reasons.

The gate changes **information routing**, not the desired verdict distribution.

## Qualification consequence

The withdrawn 55-word PASS is retroactively `FALSE_PASS_RETRACTED`. Any streak based on it is invalid and must be reset to zero. The pending candidate generated as a consequence of that PASS is stale because the generation mechanism is also being repaired; it must not be counted or evaluated as part of the old frozen streak.
