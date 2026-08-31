# Slow Steady r11 — completed detector checkpoint

Updated: 2026-08-22

## Authority and scope

- Canonical Romance authority on `main` remains unchanged. This is task-branch detector-repair state only.
- Source boundary: `work/romance-detector-repair-20260820/materialized-preservation-r10-part1/candidate-part-1.txt`.
- Source Part-1 SHA-256: `4ab1ad34f171bb75d2f93e261757cca469a655b629508eb3b91ab05ebc83c0ef`.
- Changed natural section: `Slow steady may win the race, but turtles have problems too!`.
- Exact local candidate: `recovery-20260822/slow-steady-r11-local-reader-visible.txt`.
- Candidate SHA-256: `2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4`.
- Candidate word count: 540.
- Preservation proof: `recovery-20260822/preservation-proof-slow-steady-r11.json`.
- Preservation proof status: forward PASS; reverse PASS; provenance PASS; architecture/dependency PASS; unexplained substantive deltas 0.

The only authorized semantic edit is deletion of the abstract preview sentence `But the first night isn’t necessarily the final ceiling either.` Its unique function is preserved by the immediately following Bee development anecdote. No other wording or function changes in this local candidate.

## Exact fixed-batch request

Public spec:

`u-dont-existDOTcom/pangram-humanization-lab:automation/pangram-fixed-batch/experiments/romance-detector-repair-20260820-slow-steady-r11-20260822.json`

Public spec commit:

`4f62a38f9bbe92d9191c5fa8ef4a3e2b3c2f1518`

Private executor request:

`u-dont-existDOTcom/pangram-private-executor:main/requests/romance-detector-repair-20260820-slow-steady-r11-20260822.json`

Private request commit:

`1c0e40a5fc5a418be5ff6c34b69c9d3f0c936b74`

Durable result wrapper:

`u-dont-existDOTcom/pangram-humanization-lab:automation/pangram-fixed-batch/state/experiments/romance-detector-repair-20260820-slow-steady-r11-20260822-results.json`

## Pangram 4.0 result — PASS

Exact candidate result:

- Human `1.0`;
- AI `0.0`;
- AI-assisted `0.0`;
- one 540-word Human-written window;
- no AI or assisted segments.

The result wrapper reports `part1-slow-steady` at **2/6 paid local calls** and identifies this r11 measurement as the first Human result for the section. This is therefore a valid accepted local realization under the section budget.

## Acceptance consequence

Slow Steady r11 is accepted for the next preservation candidate because:

1. the edit had a complete preservation proof with zero unexplained deltas before detector submission;
2. the deleted abstract preview performs no unique surviving function beyond the immediately following lived Bee development evidence;
3. the exact resulting natural section measured Pangram 4.0 `1.0 Human / 0 AI / 0 assisted`;
4. the edit does not touch Talk, Affection, Casual, Part 2, source links, native objects, or owner-final authority.

The accepted local result still does **not** certify the full Part-1 aggregate. Local Human evidence is non-compositional; the exact newly materialized Part-1 boundary must be certified after all accepted r11 operations are assembled.

## Aggregate context

The preservation-r10 aggregate immediately before this accepted local repair was:

- Part 1: Human `0.9456760883331299`, AI `0.05432389676570892`, assisted `0.0`;
- Part 2: Human `1.0`, AI `0.0`, assisted `0.0`.

Part 2 remains byte-preserved. The next candidate also applies the separately preservation-proved patient cross-split green rollback, whose exact 247-word boundary already has reusable 100%-Human evidence and requires no new local paid call.
