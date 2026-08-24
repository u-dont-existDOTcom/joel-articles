# Somatic Therapies r07 — execution state

Status: **R07B MEASURED; CALL 5/6 COMPLETE; OWNER-WORDING HELPED BUT DELIVERY GATE FAILED; CALL 6 RESERVED FOR NEW OWNER REALIZATION ONLY**

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

A later replay control targeted that same immutable request. Neither invalid identity produced a durable reservation/result.

This invalid spec cannot create a paid Pangram call even if one of its dormant executor jobs later starts: the canonical fixed-batch runner resolves and SHA-verifies `github_blob` text sources before it reads `PANGRAM_API_KEY`, constructs a detector client, probes auth, or enters call accounting. The stale hash must therefore fail closed before detector access.

Do not mutate or repurpose the old spec/request. They remain provenance for the identity bug.

## Corrected r07b identity and result

Corrected Pangram spec:

`u-dont-existDOTcom/pangram-humanization-lab@automation/pangram-fixed-batch:experiments/somatic-therapies-r07b-job2-to-end-20260824-a.json`

It pins the same immutable Git blob `01825fbd...` with the correct raw-byte SHA `91dd31d6...` under the **same stable audit/section and section budget**.

Corrected private immutable request:

`u-dont-existDOTcom/pangram-private-executor@main:requests/somatic-therapies-r07b-job2-to-end-20260824-a.json`

Request commit: `81d97b8a8e047081462097c8e32dc29578ab38e5`.

Pangram 4 / returned version 4.0 result:

- stage: `STAGE_SUCCESS`;
- prediction headline: `AI Detected`;
- Human fraction: **0.16262315213680267**;
- AI fraction: **0.8373768329620361**;
- AI-assisted fraction: **0.0**;
- Human segments: 3;
- AI segments: 4.

This fails Joel's 100%-Human delivery gate, but is the strongest measured Job2→end movement in the current audit:

- r03 Human `0.0`;
- r04 Human `0.0`;
- r05 Human `0.0570236444` after fresh owner semantics;
- r06 Human `0.0834549144` after more fresh owner semantics/source rollback;
- r07b Human `0.1626231521` after minimum-edit restoration toward Joel's actual wording/thought route.

Stable call accounting after r07b:

- paid calls: **5 / 6**;
- estimated credits: **12**;
- estimated cost: **~$0.60**;
- cache hits: 0;
- pending resumes: 0.

## Localization

High-confidence Human regions include:

1. the EFT tapping/head-massage material, 65 words;
2. the Louka/Shaking opening through Joel's explanation of spontaneous animal-like shaking, energetic blockage, and the beginning of his TRE-standardization thought, 165 words;
3. the `How I Judge` housemate/self-Brainspotting/restimulation passage through the start of the broader dose check, 249 words.

The long High-confidence AI window begins **inside Joel's own near-direct Shaking wording**, at the continuation `Obviously, if you could get more angles...`, then covers direct owner qigong material, the technical Shaking scaffold, Brainspotting, EMDR, neurological de-armoring, post-session integration, and Job 5 until the housemate example begins.

That is decisive evidence that Pangram's red window is contextual/distributed here. It is **not** authority to rewrite the owner-authored sentences inside that window. A second AI window covers the optional Sky/Vagal section after the Human restimulation passage.

## Decision

1. Do **not** spend call 6 on another model-only paraphrase, phrase tweak, or attempt to rewrite Joel's own red-window language.
2. Do not interpret the large red window as sentence-level evidence that the owner wording itself is AI-shaped.
3. r07b establishes that fresh owner realization and lower rewrite dose materially improve detector outcome, but the remaining registered technical/integration scaffold still dominates the long natural boundary.
4. Call 6 remains available only if the source pool changes with genuinely fresh owner realization for the still-model-realized technical/integration jobs, and a preservation/architecture/preflight pass identifies one coherent production candidate.
5. If no such owner source is supplied, suspend this Job2→end detector lane at 5/6 rather than manufacturing pseudo-owner prose.
6. `master.html` remains unchanged.

Durable raw result:

`u-dont-existDOTcom/pangram-humanization-lab@automation/pangram-fixed-batch:state/experiments/somatic-therapies-r07b-job2-to-end-20260824-a-results.json`.

Durable detector/tooling incident: `u-dont-existDOTcom/pangram-humanization-lab@automation/pangram-fixed-batch:state/SOMATIC-R07-TEXT-SOURCE-HASH-IDENTITY-INCIDENT-2026-08-24.md`.
