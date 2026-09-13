# WORKER_SUPERVISION_REQUEST SOMATIC-R15-PROGRESS-AUDIT-012

Task: `somatic-r15-clean-continuation-20260830`

Status: `DECIDED / OWNER-TRANSCRIPT RECONSTRUCTION REQUIRED`

Matching response: `SUPERVISOR_DECISION SOMATIC-R15-PROGRESS-AUDIT-012`

Exact response SHA-256: `0f089d536fa2dca7c63d5bddf2a61b5dcda50f9d4f58feb62d18c723679e5022` (`11,973` Unicode characters / `12,017` UTF-8 bytes)

Branch/head at send: `task/somatic-r15-clean-continuation-20260830 @ cb2a05f`

Reason: Joel correctly required progress to be judged against exact Pangram Human `1.0`. The evidence shows no detector improvement: exact R15 `0.1547368467`, micro candidate `0.1381948739`, article-wide reconstruction `0.1231321841`. The frozen direct-owner candidate is unmeasured because the production surprise gate was honestly `NO`.

Request: diagnose the root methodological failure, identify work that must stop, and choose a concrete replacement method most likely to reach exact Human `1.0` without violating preservation/source/safety locks. Explicitly adjudicate fresh owner-language acquisition versus a genuinely fresh meaning-preserving rewrite, measuring the current candidate, or another method. If owner source is required, return one compact batch of content-only prompts.

Current state:

- `worker_to_contract_alignment: GREEN`
- `contract_to_owner_alignment: MATCH`
- `completion_claim: WORKING`
- `terminal_comparator: OWNER_OUTCOME_UNMET`
- sixth Pangram call: `UNUSED / INELIGIBLE`
- no prose, reservation, or paid action pending

Exact next action: execute the replacement method automatically after the matching decision; ask Joel only if genuinely missing owner source is required input.

Decision: the model-led preservation-clean rewrite method is falsified by the downward detector sequence. Stop measuring/refining the frozen candidate and stop treating R15 surface text as a wording substrate. Acquire one article-scale rough owner-language batch, then reconstruct from owner verbatim/minimum normalization plus at most one necessary bridge sentence per natural section. No intact R15 paragraph may remain in a previously unresourced section. The compact source request is frozen in `OWNER-LANGUAGE-ACQUISITION-PROMPT-20260831.md`.
