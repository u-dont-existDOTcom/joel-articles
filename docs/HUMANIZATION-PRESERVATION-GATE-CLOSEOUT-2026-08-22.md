# Humanization preservation gate closeout — 2026-08-22

Status: **implemented and promoted to `main`**

## Trigger

Joel observed that the humanization process repeatedly caught itself changing or deleting material it should have preserved. The immediate Romance example was especially diagnostic: a recovery rewrite correctly removed a false attribution to Joel's father but simultaneously deleted Joel's distinct readiness/co-parenting question and its early-sex/red-flag function. The existing cold/fidelity audit caught the error only after the candidate had been generated and detector work had already been dispatched.

## Design response

The workflow was changed from a primarily post-hoc fidelity model:

`generate → audit → detector → catch semantic loss`

to a preservation-proof model:

`freeze authority → preservation units + authorized-change whitelist → draft → bidirectional source↔candidate proof → architecture/cold audit → detector`

The proof repeats after every detector-driven semantic edit.

## Existing-work decision

A bounded prior-art scan was completed after preserving an independent conception snapshot. Decision: **COMPOSE + ADAPT**, drawing on:

- requirements baselines, bidirectional traceability, change-impact analysis, and orphan/extra-element detection;
- translation validation's per-transformation correctness check;
- mutation testing for validator adequacy;
- text style-transfer evaluation's separation of content preservation from style/naturalness;
- the repository's existing authority, source/meaning/context/destination, whole-argument, architecture, and idiolect controls.

No new semantic-similarity score was invented.

Design record: `docs/HUMANIZATION-PRESERVATION-GATE-DESIGN-2026-08-22.md`.

## Canonical implementation

Merged by PR #30 as:

`4c412f8b7c048a39ad9795ee44d49d69b17ec4e9`

Added/routed:

- `docs/HUMANIZATION-PRESERVATION-GATE.md` — blocking editorial protocol;
- `docs/HUMANIZATION-PRESERVATION-TOOLING.md` — receipt/validator workflow;
- `project-sources/PRESERVATION-PROOF-TEMPLATE.json` — machine-readable receipt template;
- `scripts/validate_preservation_proof.py` — structural fail-closed validator;
- `tests/test_validate_preservation_proof.py` — causal mutation regressions;
- `SKILL.md`, `CANONICAL-REPO-MAP.md`, `AGENTS.md`, `docs/INDEX.md`, and `docs/HUMANIZATION-ARCHITECTURE-GATE.md` — startup/execution routing.

This closeout follow-up also makes the tooling path directly discoverable from `docs/INDEX.md`.

## Blocking invariants

A substantive rewritten candidate is detector-ineligible until:

- its authoritative source boundary and exact identity are frozen;
- its changed-scope preservation units are enumerated;
- the authorized-change whitelist is frozen before drafting;
- every unsuperseded source unit maps to an exact candidate realization or pre-authorized disposition;
- every substantive target delta maps back to the whitelist or explicit owner/source authority;
- there are **zero unexplained substantive deltas**;
- source wording, later interpretation, and synthesis retain correct provenance;
- architecture/dependency and cold audits pass.

`Inferable`, `redundant`, `smoother`, and `better for Pangram` are not deletion authority.

If a detector result already exists for prose that later fails preservation review, the paid/result evidence remains valid as detector history but the prose is labeled `diagnostic-only / fidelity-rejected` and cannot be promoted.

## Verification

PR #30 exact head:

`c813f097c370acf89e38486f7314109c80d62265`

GitHub Actions run:

`32540561558`

Result:

- 99/99 unit tests passed;
- content repository authority/integrity validation passed;
- article architecture-map validation passed;
- repository audit: 0 errors; 5 pre-existing/nonblocking warnings.

The mutation regressions deliberately reject representative failures including:

- a unique source unit left pending/deleted;
- `redundant` used as deletion authority;
- provenance separation failure;
- actor/agency change without authority;
- unknown change-whitelist reference;
- unexplained model-written addition;
- movement without destination;
- owner deletion without authority evidence;
- reverse-traceability failure presented as detector-eligible;
- duplicate preservation-unit IDs.

## Universal promotion

The transferable source→target architecture was promoted separately to `u-dont-existDOTcom/universal-dev-architecture` as:

`patterns/transformation-preservation-proof.md`

Universal PR #32 merged as:

`c59dd24f4f18814cae4af516d17f46087fd839a1`

Its exact-head universal compliance run `32540594665` passed 108/108 tests and reported `PASS: no findings`.

The universal pattern deliberately excludes Joel-specific prose, Romance evidence, and Pangram thresholds.

## Limits

The machine-readable validator enforces completeness of the **recorded** proof. It does not automatically discover every important semantic unit or prove natural-language semantic equivalence. A careless/incomplete ledger can still be wrong. The mitigation is whole-source/whole-argument reconstruction, owner authority, scoped independent review, and mutation testing of the validator—not pretending the schema itself is semantic intelligence.

The gate is intentionally scoped to the changed natural section plus load-bearing dependencies for local work so preservation rigor does not become article-wide bureaucracy on every sentence edit.

## Article authority impact

No Romance canonical master, owner lock, article review status, detector score, or publication export was changed by this protocol promotion.
