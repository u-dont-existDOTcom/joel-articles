# SOMATIC DSMR — FRESH ARCHITECTURE AUDIT 001

Task: `somatic-r15-clean-continuation-20260830`

Role: **fresh adversarial reasoning auditor**

Review type: **pre-execution architecture audit**

Implementation authority: **none unless verdict is exact ACCEPT; even ACCEPT only releases the already-frozen pilot state machine and authorizes no article/detector mutation**

Do not write or rewrite article prose.

## Evidence you must receive

Read the exact current contents of:

1. `SUPERVISOR-CORRECTION-SOMATIC-HUMANIZATION-REASONING-004.md`
2. `OWNER-OBSERVATION-DELIBERATIVE-MICROREWRITE-20260831.md`
3. `SOMATIC-DELIBERATIVE-SEQUENTIAL-MICROREALIZATION-005.md`
4. `SOMATIC-INTRO-P1-PRESERVATION-ESCROW-001.md`
5. `SOMATIC-INTRO-P1-DELIBERATIVE-WRITER-001.md`
6. `SOMATIC-INTRO-P1-SEMANTIC-AUDITOR-001.md`
7. `SOMATIC-INTRO-P1-COLD-SHAPE-READER-001.md`
8. the blocking rules in `docs/HUMANIZATION-PRESERVATION-GATE.md` needed to adjudicate pre-draft preservation, deletion/change authority, and forward/reverse traceability.

Treat Joel's recorded process observation as local empirical evidence, not as proof that Pro/Ultra will work on this exact paragraph. Treat prior whole-document Pro/Extra-High failures as negative evidence, but distinguish their different scope/search condition.

## Questions you must answer

Audit the strategy as a causal mechanism, not as a well-written protocol.

1. Is `small scope × high-compute repeated private revision × no future coverage plan` genuinely an untested mechanism relative to the failed one-shot whole-document direct rewrites, or merely `try harder` under another name?
2. Does exposing the exact AI source paragraph to the writer likely preserve enough source skeleton to make the causal distinction illusory? If it is a risk rather than a fatal flaw, say why the pilot can falsify it.
3. Does the frozen escrow satisfy the repository's requirement that preservation units and the change whitelist exist before drafting while keeping the writer from servicing a complete visible checklist?
4. Is the writer instruction sufficiently bounded to prevent invented autobiography/facts while still allowing a genuinely new realization?
5. Is the internal-iteration stopping rule useful as a search treatment despite being unobservable, or does the strategy depend on unverifiable compliance in a way that invalidates the experiment?
6. Does the semantic-auditor gate certify preservation independently enough, including the one-defect retry rule?
7. Does cold-shape failure causally change Candidate 2's generation input, or does feeding one `STRONGEST_DEFECT` simply recreate the failed anti-pattern-prompt loop?
8. Can Codex route all branches mechanically from typed outputs without making semantic/editorial decisions?
9. Is the two-candidate shared budget enough to falsify the family without killing a plausible method on ordinary sampling noise?
10. If the pilot succeeds, is the proposed sequential scaling rule capable in principle of preserving section/article movement, or does paragraph-level optimization predictably create a new localism problem?
11. Is Joel sufficiently shielded from low-quality intermediate candidates?
12. Name any contradiction with the current task-local/repository authority that would make execution unsafe.

## Required verdict standard

Return `ACCEPT` only if you would actually permit the first 43-word pilot to run under the frozen state machine without another architecture change.

Return `ACCEPT_WITH_REVISION` if the mechanism is worth testing but any contract must change first.

Return `REJECT` if the causal distinction is not real, the protocol violates authority/preservation, or the experiment cannot produce interpretable evidence.

Do not choose `ACCEPT` merely because the pilot is low risk.

## Required output

Begin exactly:

`SOMATIC_DSMR_ARCHITECTURE_AUDIT 001`

Then return exactly these fields, with concise reasoning after each field where requested:

`VERDICT: ACCEPT | ACCEPT_WITH_REVISION | REJECT`

`CAUSAL_DISTINCTION: PASS | FAIL — <reason>`

`SOURCE_ANCHORING: TOLERABLE_TEST_RISK | FATAL — <reason>`

`PRE_DRAFT_PRESERVATION: PASS | FAIL — <reason>`

`WRITER_TREATMENT: PASS | FAIL — <reason>`

`ITERATION_OBSERVABILITY: ACCEPTABLE_TREATMENT_LIMITATION | FATAL — <reason>`

`SEMANTIC_GATE: PASS | FAIL — <reason>`

`FAILURE_FEEDBACK: ACTIONABLE | REJECTION_ONLY | ANTIPATTERN_LOOP — <reason>`

`CODEX_MECHANICAL_ROUTING: PASS | FAIL — <reason>`

`ATTEMPT_BUDGET: PASS | FAIL — <reason>`

`SCALING_LOGIC: PASS | FAIL — <reason>`

`OWNER_SHIELDING: PASS | FAIL — <reason>`

`AUTHORITY_CONFLICTS: NONE | <exact conflict>`

`STRONGEST_DEFECT: <one issue or NONE>`

`EXECUTION_AUTHORIZED: YES | NO`

Rules:

- `EXECUTION_AUTHORIZED: YES` is valid only with exact `VERDICT: ACCEPT` and every blocking authority/preservation field passing.
- Do not supply revised article prose.
- For `ACCEPT_WITH_REVISION` or `REJECT`, stop after the required fields. Do not design another strategy in the same response.
