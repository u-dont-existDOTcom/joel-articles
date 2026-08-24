# Somatic Therapies r07 — execution state

Status: **ORIGINAL R07 IDENTITY PRE-DETECTOR INVALID; CORRECTED R07B REQUEST CREATED; NO CALL-5 RESERVATION YET**

Candidate: `R07-JOB2-TO-END-OWNER-WORDING-CANDIDATE-20260824.md`.

Preservation: PASS, controlling 72-unit ledger 72/72, zero unexplained substantive deltas.

Production preflight: PASS editorially. The first detector bookkeeping identity recorded in that preflight was later proven wrong and is superseded by this state file.

Exact detector boundary file: `R07-JOB2-TO-END-PANGRAM-BOUNDARY-20260824.txt`.

Immutable Git blob: `01825fbd46497c17eac14aa709e29429f5caf05b`.

Exact **raw file-byte SHA-256**: `91dd31d6519e76f30831780789d9a13c2761378978d153f2cc3f602c4b5b0b87`.

The file ends with one terminal newline. The same bytes with only that final newline removed hash to `06d068603b3a9c0d26bd9537240550ab18ae589ea795aa6bc2f443bffb96451b`.

The earlier recorded hash `6091db45d7ddf80f027cc591396abd75ab7b144c206e28befee86b2f5d3589ec` matches **neither** identity. Hosted CI mechanically proved these relationships in `tests/test_somatic_r07_promotion_fragment.py`.

Word count: 2,690.

Stable audit/section: `somatic-therapies-r03-job2-to-end-20260824` / `job2-to-end`.

## Invalid original r07 identity

Old Pangram spec:

`u-dont-existDOTcom/pangram-humanization-lab@automation/pangram-fixed-batch:experiments/somatic-therapies-r07-job2-to-end-20260824-a.json`

It pins Git blob `01825fbd...` but stale `text_sha256=6091db45...` and is therefore **pre-detector invalid**.

Original immutable private request:

`u-dont-existDOTcom/pangram-private-executor@main:requests/somatic-therapies-r07-job2-to-end-20260824-a.json`

Original request blob: `3c32a20165e6244b058ae89ed4b08d734948ae98`.

A later replay control targeted that same immutable request. Neither identity produced a durable reservation/result.

This invalid spec cannot create a paid Pangram call even if one of its dormant executor jobs later starts: the canonical fixed-batch runner resolves and SHA-verifies `github_blob` text sources before it reads `PANGRAM_API_KEY`, constructs a detector client, probes auth, or enters call accounting. The stale hash must therefore fail closed before detector access.

Do not mutate or repurpose the old spec/request. They remain provenance for the identity bug.

## Corrected r07b identity

Corrected Pangram spec:

`u-dont-existDOTcom/pangram-humanization-lab@automation/pangram-fixed-batch:experiments/somatic-therapies-r07b-job2-to-end-20260824-a.json`

It pins the same immutable Git blob `01825fbd...` with the correct raw-byte SHA `91dd31d6...` under the **same stable audit/section and section budget**.

Corrected private immutable request:

`u-dont-existDOTcom/pangram-private-executor@main:requests/somatic-therapies-r07b-job2-to-end-20260824-a.json`

Request commit: `81d97b8a8e047081462097c8e32dc29578ab38e5`.

At the latest durable read after that request:

- paid calls: **4 / 6**;
- estimated accounting: **9 credits / ~$0.45**;
- cache hits: 0;
- pending resumes: 0;
- exact corrected r07b cache: MISS.

Therefore r07/r07b has **not** crossed the call-5 paid reservation boundary at this checkpoint.

## Safety rule

1. Do not create another r07/r07b detector spec/request merely because execution is delayed.
2. The obsolete r07 identity is closed invalid, not a paid attempt.
3. r07b is the only live corrected measurement identity.
4. If r07b later reserves, it is call 5/6 under the existing audit.
5. If r07b remains overwhelmingly AI, do not rewrite Joel's own wording away. Call 6 remains unused unless the exact result exposes one genuinely faithful, decision-changing operation.
6. `master.html` remains unchanged.

Durable detector/tooling incident: `u-dont-existDOTcom/pangram-humanization-lab@automation/pangram-fixed-batch:state/SOMATIC-R07-TEXT-SOURCE-HASH-IDENTITY-INCIDENT-2026-08-24.md`.
