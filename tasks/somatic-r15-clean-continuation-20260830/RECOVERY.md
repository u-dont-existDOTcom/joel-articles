# Somatic R15 clean continuation — recovery checkpoint

Status: **ACTIVE / EXCLUSIVE / INCOMPLETE**

Task id: `somatic-r15-clean-continuation-20260830`

Required branch: `task/somatic-r15-clean-continuation-20260830`

Draft recovery PR: #73

Baseline: current canonical `main` at `6d78c638e1e7edd7e937e5992b328c0212dfbfe2`

## Authority and exact frontier

The registered `articles/somatic-therapies/master.html` remains article authority at SHA-256 `1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202`.

The only active reconstruction frontier is the historical non-authoritative R15 candidate:

- path: `articles/somatic-therapies/experiments/R15-PANGRAM-LOCALIZED-REWRITE-CANDIDATE-20260825.md`;
- exact Git blob: `e6210eb2742de156f0bd7b01fdde269f9b9625c6`;
- exact UTF-8 SHA-256: `e7a541e75cf06878c206bcd7d78440bb73593a0a5a2169df1446ce42ad7186ee`;
- historical checkpoint blob: `18136e5205cae3317bb41417a633a402aba902da`;
- preservation/cold-audit receipt blob: `9bba365c498bc9f51bd16fe2761455a6b233d1bf`.

The exact current whole-document Pangram input was deterministically materialized directly from the immutable R15 candidate. Its identity chain is R15 candidate blob `e6210eb2742de156f0bd7b01fdde269f9b9625c6` -> deterministic materialization -> exact R15 boundary SHA-256 `9a81bd04252a2ee851dd111040c600837bdf0a7bbf71c42c293e3b763c99a707`.

The historical R16 boundary was used only to regression-test the general extraction convention. It is not an identity oracle for R15, and the two boundary blobs are not claimed to be identical.

- boundary path: `articles/somatic-therapies/experiments/R15-WHOLE-ARTICLE-PANGRAM-BOUNDARY-20260830.txt`;
- SHA-256: `9a81bd04252a2ee851dd111040c600837bdf0a7bbf71c42c293e3b763c99a707`;
- 3,548 whitespace words;
- 21,087 UTF-8 bytes;
- 20,989 Unicode characters;
- final blank line preserved.

The one supervisor-authorized exact Pangram GUI measurement has now been taken and durably bound to this boundary. No semantic edit has followed it.

## Mandatory quarantine

- R16 is excluded from candidate/source assembly because it begins the forbidden Cancer-corpus grammatical-route method.
- R17–R58 are owner-stopped and quarantined as production prose. Their detector results and negative methodological findings remain historical evidence only.
- R59–R65 and draft PR #72 are superseded failed working history, not a candidate, baseline, assembly source, or detector target.
- Later prose may enter a new candidate only after explicit supervising-Chat approval and exact same-function source-integrity proof independent of Pangram.

The durable disposition is recorded in `articles/somatic-therapies/experiments/R59-R65-PR72-SUPERSESSION-20260830.md`.

## Supervisor bridge

There is one executor/controller: the Codex Pro conversation that created this branch. The editorial supervisor is the existing authenticated ChatGPT conversation whose visible recent history contains Joel's literal correction:

`no R65 was not the frontier it was a long failed branch you forgot`

Before any Pangram submission, send and resolve exactly one matching bootstrap request:

`WORKER_SUPERVISION_REQUEST SOMATIC-R15-BOOTSTRAP-001`

Only one monotonically numbered supervision request may be outstanding. A timeout after sending requires exact request-id recovery in the same conversation before any resend.

The request was recovered in the exact conversation after a browser timeout, without resending. The matching assistant response began `SUPERVISOR_DECISION SOMATIC-R15-BOOTSTRAP-001` and authorized cold preflight, exhaustive read-only detector recovery, and exactly one whole-document Pangram 4 GUI measurement only if the exact action is proven never submitted. The decision and its required provenance correction are recorded in `SUPERVISION.md`.

## Current step

1. `SUPERVISOR_DECISION SOMATIC-R15-READER-003` authorized four bounded repair scopes and explicit exclusions.
2. Freeze separate source/provenance ledgers, change whitelists, touched preservation units, and forbidden side effects before drafting.
3. Draft only the minimum combined source-grounded repair, then prove forward/reverse traceability, zero unexplained substantive deltas, architecture/multiscale, cold-audit, link, and native-placeholder gates.
4. Run one new genuinely separate detector-blind reader on the repaired candidate and return `WORKER_SUPERVISION_REQUEST SOMATIC-R15-REPAIR-004`; no Pangram call or `master.html` promotion is authorized.

Bootstrap durability completed: clean branch pushed; draft recovery PR #73 opened; superseded PR #72 closed with its branch/history retained.

Cold production preflight is durably **PASS / PROVISIONAL SAME-CONTEXT AUDIT** in `R15-PRODUCTION-PREFLIGHT-20260830.md`. No concrete high-confidence defect was found and no semantic edit was made.

Exact detector recovery and the authorized GUI measurement are complete in Pangram-lab draft PR #144 at `0d03264302bb7deaf168dae0842c97b7b80ccb57`. The durable current classification is **`EXACT_R15_RESULT_EXISTS`** for reader-visible boundary `9a81bd…`; see `DETECTOR-STATE.json` and `R15-EXACT-PANGRAM-RESULT-20260830.md`.

Historical `d5101f…` is valid near-boundary evidence for the same immutable R15 candidate, but it retained four source-only Markdown italics asterisks and had one fewer terminal newline. It is not exact or accepted-transport-normalized evidence for `9a81bd…`. Related paid-call history remains counted.

The exact Pangram 4.0 result is Human `0.1547368467`, AI `0.8452631831`, AI-assisted `0.0`, `STAGE_SUCCESS`, with exact UTF-8 History binding. The single authorized new call is consumed; the related ledger totals three calls and no further paid action is authorized. No detector-driven rewrite has begun.

The independent reader input article is bound at SHA-256 `460dc342…`, its transmitted packet at `6cc91944…`, and its response at `3d9d96d…`. It identified multiple high-confidence editorial questions and several secondary ones. The controller adjudicated them against R15 preservation and architecture; `FINAL-READER.md` records the privacy-safe gate receipt, while the detailed local ledger and exact response remain outside the public branch. No reader-suggested change has been applied.

## Completion boundary

Ordinary tests and a high Pangram score do not complete this task. `python scripts/check_somatic_r15_task.py --acceptance` must pass, the supervisor must propose/approve `READY_FOR_OWNER_REVIEW`, and the final candidate must satisfy every source-integrity, preservation, semantic, architecture, multiscale, cold-audit, independent-reader, exact detector-binding, link, and native-placeholder gate. Registered `master.html` stays unchanged until a later explicit approval; Substack publication is outside this task's automatic authority.
