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

The exact current whole-document Pangram input was independently materialized from the immutable R15 candidate using the historical GUI-boundary convention. The generator reproduces the frozen R16 GUI boundary byte-for-byte before it is trusted for R15.

- boundary path: `articles/somatic-therapies/experiments/R15-WHOLE-ARTICLE-PANGRAM-BOUNDARY-20260830.txt`;
- SHA-256: `9a81bd04252a2ee851dd111040c600837bdf0a7bbf71c42c293e3b763c99a707`;
- 3,548 whitespace words;
- 21,087 UTF-8 bytes;
- 20,989 Unicode characters;
- final blank line preserved.

No Pangram action for this exact boundary has been taken by this task.

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

## Current step

1. Verify the exact supervisor conversation and complete bootstrap request `SOMATIC-R15-BOOTSTRAP-001`.
2. Cold-read literal R15 under current production gates.
3. Recover exact-boundary cache, reservations, Pangram application History, browser recovery state, and GitHub detector evidence.
4. Persist one of `EXACT_R15_RESULT_EXISTS`, `EXACT_R15_ACTION_AMBIGUOUS`, or `EXACT_R15_NEVER_SUBMITTED` before any click.

Bootstrap durability completed: clean branch pushed; draft recovery PR #73 opened; superseded PR #72 closed with its branch/history retained.

## Completion boundary

Ordinary tests and a high Pangram score do not complete this task. `python scripts/check_somatic_r15_task.py --acceptance` must pass, the supervisor must propose/approve `READY_FOR_OWNER_REVIEW`, and the final candidate must satisfy every source-integrity, preservation, semantic, architecture, multiscale, cold-audit, independent-reader, exact detector-binding, link, and native-placeholder gate. Registered `master.html` stays unchanged until a later explicit approval; Substack publication is outside this task's automatic authority.
