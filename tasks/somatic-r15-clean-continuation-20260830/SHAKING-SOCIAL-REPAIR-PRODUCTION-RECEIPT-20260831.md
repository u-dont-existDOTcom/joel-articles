# Shaking Social Repair Production Receipt — 2026-08-31

Task: `somatic-r15-clean-continuation-20260830`

Directive: `SOMATIC-R15-APPLY-SHAKING-SOCIAL-001`

Status: **PASS / NON-AUTHORITATIVE CANDIDATE ONLY**

## Identity

- starting packet head: `35ebdb263ba90ac36f345af2560f13c6d711459d`
- source candidate: `articles/somatic-therapies/experiments/R15-EFT-REPAIR-CANDIDATE-20260831.md`
- source Git blob: `6f9251f51d79a6b322b8c6f6cae95a9a5d80f760`
- source SHA-256: `5a6226ca0056610b4492de7713a43bb152dde1079d81b5c05896c70fcf138679`
- source counts: `4000` whitespace words / `24526` Unicode characters / `24634` UTF-8 bytes / terminal newline present
- output candidate: `articles/somatic-therapies/experiments/R15-EFT-SHAKING-SOCIAL-REPAIR-CANDIDATE-20260831.md`
- output Git blob: `22126723d8c585ca8bde54f00c4ade6c925f354e`
- output SHA-256: `1e08284ce544b851b516eebdf38f3f8efb2497e477a0104270880f49aab7d81e`
- output counts: `3987` whitespace words / `24446` Unicode characters / `24554` UTF-8 bytes / terminal newline present
- reader-visible boundary: `articles/somatic-therapies/experiments/R15-EFT-SHAKING-SOCIAL-REPAIR-BOUNDARY-20260831.txt`
- boundary Git blob: `cced74d65de28cc7d04903f519ec6f4356da82f6`
- boundary SHA-256: `d5c0b510a89ab6f7c97d9cdbe6069cccd197cd6470eac5ddc4a86ffcb14735bb`
- boundary counts: `3807` whitespace words / `22414` Unicode characters / `22504` UTF-8 bytes / materializer-required final blank line present
- exact diff: `tasks/somatic-r15-clean-continuation-20260830/SHAKING-SOCIAL-REPAIR-DIFF-20260831.patch`
- diff Git blob: `b3199ab413b7e0255ddef8e7688d80b96fd55be2`
- diff SHA-256: `539913c5440155bb3d1ca6d3d00b9350221825cf55694e1b173fd2689abff4bb`

## Exact replacement

- deleted paragraph: `35` whitespace words / `205` Unicode characters / `205` UTF-8 bytes
- deleted paragraph SHA-256: `3a96a5bb9b7dd0d670f36b16ccaceca355243a7878b69afa753c847e78c2f349`
- inserted paragraph: `22` whitespace words / `125` Unicode characters / `125` UTF-8 bytes
- inserted paragraph SHA-256: `6667faded75427a60fd82b7eadeb834966074f7b45712a10e5aec380b3c6f4ec`
- deleted paragraph occurrence before/after: `1 / 0` — PASS
- inserted production paragraph is byte-identical to Variant A's exact appended tail — PASS
- source candidate mutations: `0`
- bytes outside the one replaced paragraph: byte-identical — PASS
- exact patch: one complete paragraph deletion and one complete paragraph insertion — PASS

## Preservation and source integrity

- complete current Human Shaking anchor through `completely unstructured shaking.`: byte-identical — PASS
- social/with-other-people-rather-than-alone function: preserved — PASS
- seeing-other-people-get-results-may-help function: preserved — PASS
- Louka standard-TRE nonresponse and linked-class benefit: explicitly preserved upstream — PASS
- multiple movements and positions: explicitly preserved upstream — PASS
- more-angles/blockage function: explicitly preserved upstream — PASS
- guided without full standardization: explicitly preserved upstream — PASS
- predictable-TRE/unstructured-shaking middle ground: explicitly preserved upstream — PASS
- forward traceability: PASS
- reverse traceability: PASS
- unexplained substantive deltas: `0`
- exact changed-scope source integrity: PASS
- article-wide semantic sanity: PASS
- article-wide architecture/multiscale regression: PASS
- heading identity and order: unchanged — PASS
- ordinary-link URL multiset: `16 / 16`, byte-identical — PASS
- reader-visible native placeholders: `7 / 7`, byte-identical and in the same order — PASS
- R16–R65 exact inserted-paragraph scan: zero hits — PASS
- PR #72 failed-branch exact inserted-paragraph scan: zero hits — PASS
- failed-branch contamination introduced: `0`

## Detector evidence — read only

- detector head: `a2442fb343e43247b445d5884eaa8f7daa44a514`
- result packet: `state/experiments/somatic-r15-shaking-current-anchor-residual-social-tail-20260831/RESULT-PACKET.json`
- result-packet SHA-256: `43ab4bb70fb65a5c2a810782b6b5125c515e69592cddbc6416d51f85e6084b85`
- H0 SHA-256: `b36e1e46c06d764a080d407dce5412defe76ccb9202deb1a8a14e265acf40370`
- H0: Pangram 4.0 / `STAGE_SUCCESS` / Human `1.0` / AI `0.0` / AI-assisted `0.0` / exact UTF-8 History binding — PASS
- Variant A SHA-256: `03037241afe8827df5b1ca2b81bc877704d5e198229a9759237b76245807ecd1`
- Variant A: exact H0 + two linefeeds + inserted paragraph / Pangram 4.0 / `STAGE_SUCCESS` / Human `1.0` / AI `0.0` / AI-assisted `0.0` / High / exact UTF-8 History binding — PASS
- Variant B: unsubmitted — PASS
- residual-social family: `CLOSED_A_HUMAN_1_0_B_NOT_SUBMITTED`

## Artifact registration

- new candidate registered in `articles/INDEX.json` as `non_authoritative_supervisor_authorized_repair_candidate` with SHA-256 `1e08284ce544b851b516eebdf38f3f8efb2497e477a0104270880f49aab7d81e` — PASS
- new boundary registered as `exact_non_authoritative_repair_candidate_detector_input_boundary` with SHA-256 `d5c0b510a89ab6f7c97d9cdbe6069cccd197cd6470eac5ddc4a86ffcb14735bb` — PASS
- additional-artifact entries added: `2`
- registered Somatic master path/hash: unchanged — PASS
- article status: unchanged — PASS
- publication exports: unchanged — PASS
- canonical authority: unchanged — PASS

## Repository validation

- `python scripts/check_somatic_r15_task.py --preflight` — PASS
- exact application/preservation/source-integrity script — PASS
- exact-candidate direct-owner/source-integrity audit — PASS (`61` R15 markers / `19` direct-owner markers / `16` links / `7` native placeholders)
- legacy pre-direct-owner articlewide checker: its exact `17` historical mismatch findings, heading count, link count, placeholder count and preservation-marker count are identical on source and output; changed-scope regression — PASS
- article-wide semantic/architecture/multiscale regression — PASS
- `python -m unittest discover -s tests` — PASS (`118` tests)
- `python scripts/validate_article_architecture_maps.py --root .` — PASS
- `python scripts/validate_content_repository.py --root .` — expected pre-existing-only nonzero result: six exact findings remain for Romance and three older unregistered Somatic artifacts; the new candidate and boundary inventory checks PASS
- `python scripts/audit_codex_github.py --root . --fail-on error` — PASS (`0` errors / `4` repository-policy warnings)
- raw staged `git diff --check` reports only the established materializer-required final blank line in the reader-visible boundary; `git -c core.whitespace=-blank-at-eof diff --cached --check` — PASS
- execution-script compile — PASS

## Mutations and calls

- source candidate mutations: `0`
- registered-master mutations: `0`
- paid detector calls: `0`
- detector reservations: `0`
- GUI actions: `0`
- whole-document detector calls: `0`

## Carried CI disposition

- `FULL_HISTORY_FIX: PASS`
- `REMAINING_VALIDATOR_FINDINGS: PRE_EXISTING_UNRELATED_MERGE_DEBT`
- `HUMANIZATION_EXECUTION_BLOCKED: NO`
- `MERGE_BLOCKED_UNTIL_RECONCILED: YES`

Article authority remains the registered `master.html`; this candidate is not promoted.
