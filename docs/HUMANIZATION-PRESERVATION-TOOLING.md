# Humanization preservation proof tooling

This tooling enforces the **structural completion** of `HUMANIZATION-PRESERVATION-GATE.md`. It cannot infer whether the preservation ledger itself captured every important semantic unit, and it cannot prove natural-language equivalence. Those remain editorial judgments.

## Files

- Protocol: `docs/HUMANIZATION-PRESERVATION-GATE.md`
- Receipt template: `project-sources/PRESERVATION-PROOF-TEMPLATE.json`
- Validator: `scripts/validate_preservation_proof.py`
- Causal regressions: `tests/test_validate_preservation_proof.py`

## Per-candidate workflow

1. Copy the JSON template into the article/task working area.
2. Replace the placeholder source identity with the exact authoritative path, revision, and SHA-256.
3. Populate the preservation units **before drafting**.
4. Populate the authorized-change whitelist **before drafting**.
5. After drafting, map every preserved/moved/consolidated unit to its exact candidate destination.
6. Classify every substantive candidate delta and map it to the whitelist or an explicit owner/source authority.
7. Leave `unexplained_deltas` non-empty and `detector_eligibility` blocked while any delta is unresolved.
8. Only after substantive review concludes that forward and reverse traceability pass should the receipt be changed to the all-pass/eligible state and validated.

Validate:

```bash
python scripts/validate_preservation_proof.py path/to/PRESERVATION-PROOF.json
```

A successful structural receipt prints `PASS`. A failure prints machine-readable findings and exits nonzero.

## What the validator blocks

The validator fails closed when, among other conditions:

- a preservation unit is missing a terminal disposition;
- a supposedly preserved/moved/consolidated unit has no candidate mapping;
- an owner-deleted or owner-superseded unit lacks authority evidence;
- a generic assistant-convenience disposition such as `redundant` is used;
- a substantive candidate delta lacks authority;
- a delta points to a nonexistent whitelist item;
- `unexplained_deltas` is non-empty;
- forward traceability, reverse traceability, provenance separation, or architecture/dependency review has not passed;
- the receipt attempts to mark the candidate detector-eligible before those gates pass.

## Mutation/regression gate

Run:

```bash
python -m unittest tests.test_validate_preservation_proof -v
```

The current regression suite deliberately mutates preservation state to confirm that the validator rejects representative failure classes, including:

- a unique source unit left pending after deletion;
- `redundant` used as deletion authority;
- provenance separation failure;
- an actor/agency change without authority;
- an unknown whitelist reference;
- an unexplained model-written addition;
- movement without a destination;
- owner deletion without an authority reference;
- failed reverse traceability presented as detector-eligible;
- duplicate preservation-unit IDs.

These tests validate the **receipt validator**, not the completeness or truth of a human-written preservation ledger.

## Detector boundary

Pangram submission remains a later gate. A structurally valid preservation receipt means only that the candidate has a complete recorded preservation proof. It does not predict Pangram, prove authorship, or establish article authority.

If a paid detector result already exists for prose that later fails preservation review, keep the detector record and paid-call accounting but mark the prose/result relationship `diagnostic-only / fidelity-rejected`.
