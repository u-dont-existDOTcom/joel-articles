# Somatic Therapies r07 — execution state

Status: **IMMUTABLE PAID REQUEST CREATED; PRE-RESERVATION / NO BILLING EVIDENCE YET**

Candidate: `R07-JOB2-TO-END-OWNER-WORDING-CANDIDATE-20260824.md`.

Preservation: PASS, controlling 72-unit ledger 72/72, zero unexplained substantive deltas.

Production preflight: PASS.

Exact detector boundary: `R07-JOB2-TO-END-PANGRAM-BOUNDARY-20260824.txt`.

Git blob: `01825fbd46497c17eac14aa709e29429f5caf05b`.

Text SHA-256: `6091db45d7ddf80f027cc591396abd75ab7b144c206e28befee86b2f5d3589ec`.

Word count: 2,690.

Stable audit/section: `somatic-therapies-r03-job2-to-end-20260824` / `job2-to-end`.

Pangram spec: `u-dont-existDOTcom/pangram-humanization-lab@automation/pangram-fixed-batch:experiments/somatic-therapies-r07-job2-to-end-20260824-a.json`.

Spec SHA-256: `9cd154057eb8ed6a0c031b40483e9c0b0d3012e68a2b890ebd5724304935dec9`.

Private immutable request: `u-dont-existDOTcom/pangram-private-executor@main:requests/somatic-therapies-r07-job2-to-end-20260824-a.json`, request commit `b0a760615389a5d1b0dfb42f2c63dcf3c403cc66`.

A metadata-only workflow-status request also exists at `workflow-status-requests/somatic-r07-job2-end-20260824-a.json`; it has no detector-submission capability.

Latest durable ledger observation after the request: **4/6 paid calls**, 9 estimated credits / ~$0.45, zero cache hits, zero pending resumes. Therefore r07 has **not** crossed the paid reservation boundary at this checkpoint.

Current active Pangram owner cost policy (2026-08-24) classifies `budget_scope: section` inputs as API-eligible by default; `aggregate` boundaries default to GUI. r07 remains section-scoped, so the existing request is correctly routed and must not be replaced merely because it is queued.

## Safety rule

Do not create another r07 request or submit the exact SHA through another transport while this immutable request exists. First establish one of:

1. the stable ledger records the r07 reservation/result; or
2. exact workflow metadata proves a pre-run cancellation/no execution, after which the exact existing workflow may be rerun rather than creating a second measurement identity.

Missing result/cache alone is not repeat authorization.

`master.html` remains unchanged.
