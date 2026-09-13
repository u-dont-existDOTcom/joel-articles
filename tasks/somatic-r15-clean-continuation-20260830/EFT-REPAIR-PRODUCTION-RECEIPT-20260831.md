# EFT Repair Production Receipt — 2026-08-31

Task: `somatic-r15-clean-continuation-20260830`

Status: **PASS / NON-AUTHORITATIVE CANDIDATE ONLY**

## Identity

- live packet head: `97c36c3765835e8153e2598701cb1ff1a6cf9fc4`
- required source ancestor: `ac1570f3e8945fecf80585d8fbe336c2a19ffbd6` — PASS
- source candidate: `articles/somatic-therapies/experiments/R15-DIRECT-OWNER-VOICE-CANDIDATE-20260830.md`
- source Git blob: `442349c82d92ac844447f27208924b720d9fa92a`
- source SHA-256: `9c2e8fe57335d51ac925bc9b63cee8125c24e471e2b9b8fda50cc44cf28f5b31`
- source counts: `4006` words / `24575` Unicode characters / `24681` UTF-8 bytes
- output candidate: `articles/somatic-therapies/experiments/R15-EFT-REPAIR-CANDIDATE-20260831.md`
- output Git blob: `6f9251f51d79a6b322b8c6f6cae95a9a5d80f760`
- output SHA-256: `5a6226ca0056610b4492de7713a43bb152dde1079d81b5c05896c70fcf138679`
- output counts: `4000` words / `24526` Unicode characters / `24634` UTF-8 bytes
- reader-visible boundary: `articles/somatic-therapies/experiments/R15-EFT-REPAIR-BOUNDARY-20260831.txt`
- boundary Git blob: `0a370fea174cf86796a821b48bfc0fb7b8814420`
- boundary SHA-256: `16cb68d7694dda6e1c088fc0a7c615eafb211b5ce44bc5e111ec4357052bb6f0`
- boundary counts: `3820` words / `22494` Unicode characters / `22584` UTF-8 bytes
- deleted paragraph SHA-256: `775a30e2c6b70da2fb57b57444283973acced07cb13528da10529b3351409b6a`
- inserted paragraph SHA-256: `d8ec8ac01f177f00e90bad897996bb1236762938c871d4faa0ad22ed8ad1aa81`

## Exact-scope assertions

- deleted paragraph occurrence before/after: `1 / 0` — PASS
- inserted paragraph occurrence before/after: `0 / 1` — PASS
- bytes outside the one replaced paragraph: byte-identical — PASS
- attribution-correct EFT anchor: byte-identical — PASS
- portability, hard-conversation, immediate-trigger, mind/body loop, pressure-reduction and deeper-trauma distinction functions: PASS
- heading identity/order: PASS
- ordinary-link URL multiset: `16 / 16`, byte-identical — PASS
- reader-visible native placeholders: `7 / 7`, byte-identical and ordered — PASS
- R16–R65 and PR #72 exact inserted-prose scan: zero hits — PASS
- forward traceability: PASS
- reverse traceability: PASS
- unexplained substantive deltas: `0`
- source integrity: PASS
- registered `master.html` SHA-256: `1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202` — unchanged / PASS

## Detector evidence (read-only)

- detector head: `ede777c4455d699f64f46e7850e92c707fa31378`
- Candidate E SHA-256: `e9d2969aadbdd648ccd6b5aa36d6b7712b059a5b24a2acfcf95d29a4d458b7eb`
- result packet: `state/experiments/somatic-r15-eft-human-anchor-tail-factorial-20260831/RESULT-PACKET-E.json`
- result packet SHA-256: `70b69c55c66117813af3b8d5832fb2da9aab2dc1541d279e0582283099a46756`
- Pangram 4.0 / `STAGE_SUCCESS` / Human `1.0` / AI `0.0` / AI-assisted `0.0` / High — exact binding PASS
- EFT family: `CLOSED_6_OF_6`

## Mutations and calls

- source candidate mutations: `0`
- article artifact-inventory entries added: `2` (new candidate and boundary only)
- registered-master mutations: `0`
- paid detector calls: `0`
- detector reservations: `0`
- GUI actions: `0`
- whole-document calls: `0`

## Repository validation

- `python scripts/check_somatic_r15_task.py --preflight` — PASS
- exact-candidate direct-owner/source-integrity audit — PASS (`61` R15 markers, `19` direct-owner markers, `16` links, `7` native placeholders)
- `python -m unittest discover -s tests` — PASS (`117` tests)
- `python scripts/validate_content_repository.py --root .` — expected pre-existing-only nonzero result: six exact findings remain for Romance and three older unregistered Somatic artifacts; the new candidate and boundary inventory checks PASS
- `python scripts/audit_codex_github.py --root . --fail-on error` — PASS (`0` errors; four repository-policy warnings)
- raw staged `git diff --check` reports only the materializer-required final blank line in the reader-visible boundary; `git -c core.whitespace=-blank-at-eof diff --cached --check` — PASS with that established transport exception
- execution-script compile — PASS

Article authority remains the registered `master.html`; this candidate is not promoted.
