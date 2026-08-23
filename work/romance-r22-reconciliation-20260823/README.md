# Romance r22 reconciliation

Purpose: reconcile the exact detector-green r22 working candidate into registered Romance authority without merging the historical detector task branch.

Registered canonical master remains `main:articles/romance/master.md`, SHA-256 `af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`, until deliberate owner reconciliation changes the registered article family.

Leading working candidate is again the exact r22 source:
`task/romance-detector-repair-20260820:work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/candidate-master.md`, Git blob `9f6bf7ed77093569a98fe606fda96ac277839f99`, SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`, 20,282 words.

Detector evidence for that exact working candidate:
- Part 1 SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`: Pangram 4.0 Human `1.0`, AI `0.0`, AI-assisted `0.0`, zero AI windows;
- retained Part 2 SHA-256 `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`: Pangram 4.0 Human `1.0`.

The first clean PR #46 comparison proved that r22 contains 16 changed semantic sections / 140 changed lines relative to registered canonical prose. That means canonical promotion still requires owner reconciliation, but it does **not** mean those rewrites should be reverted merely because they are assistant-produced or not yet registered.

Joel corrected that mistake on 2026-08-23. The owner rule is now:

> Keep an exact detector-green, preservation-proved working rewrite as the leading prose unless the older/canonical realization actually reads better **and** is detector-safe. Canonical authority controls what is registered; it does not automatically prove that older wording is editorially superior.

See `OWNER-CORRECTION-KNOWN-GREEN-RECALIBRATION-20260823.md`.

The prior conservative materialization remains historical reconciliation evidence only. Its subjective `PRODUCTION-AI-SHAPE-AUDIT.md` is superseded as a reason to reopen r22, and `HOLISTIC-REPAIR-PROPOSALS.md` is rejected: Joel tested the six-proposal bundle in Pangram 4.0 and it returned 59.5% AI / 40.5% Human over 2,347 words, including several high-confidence AI runs.

## Current reconciliation method

1. Start from exact r22, not the conservative rollback hybrid.
2. For every canonical→r22 hunk, check semantic fidelity, provenance, architecture, voice, and actual reading quality.
3. Default **keep r22** when it is faithful and at least as good editorially, because its exact current half boundary is already known Human.
4. Revert a r22 hunk only when the canonical realization is materially better and detector safety for that rollback is affirmatively known or deliberately re-established.
5. A real editorial defect in green prose may still be fixed, but name the defect directly; do not call a known-green passage `AI-shaped` based only on pattern resemblance.
6. Keep owner-final/direct-owner corrections above both candidates.
7. Do not merge PR #29 wholesale and do not publish/export.

PR #46 is an owner-reconciliation/edit-review lane, not a detector-repair lane. No new Pangram work is justified merely to `improve` already-green r22 prose.