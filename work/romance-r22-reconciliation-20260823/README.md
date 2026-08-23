# Romance r22 reconciliation

Purpose: cleanly reconcile the detector-repair work into registered Romance authority without merging the historical detector task branch.

Registered canonical master remains `main:articles/romance/master.md`, SHA-256 `af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`, until this reconciliation is deliberately merged.

Reference r22 source: `task/romance-detector-repair-20260820:work/romance-detector-repair-20260820/materialized-preservation-r22-patient-affection/candidate-master.md`, Git blob `9f6bf7ed77093569a98fe606fda96ac277839f99`, SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`, 20,282 words.

The first clean PR #46 comparison proved that r22 contains 16 changed semantic sections / 140 changed lines relative to registered canonical prose. The exact r22 detector pass therefore does **not** authorize wholesale promotion.

Authority dispositions are frozen in `RECONCILIATION-LEDGER.md`. The conservative rule is: retain r22 wording only where direct owner prose, owner-final prose, explicit owner acceptance, or an explicit owner-authorized deletion/supersession outranks the registered master; restore registered canonical wording everywhere the r22 difference is merely assistant rephrasing/compression/detector optimization.

Hash-gated materializer: `materialize_conservative_reconciliation.py`. It starts from exact registered canonical bytes, reads exact r22 only as an authority-supported source for named spans, applies nine authorized operations, preserves the heading sequence/native objects/link destinations/protected anchors, rejects specified unaccepted r22 realizations if they survive, and writes a manifest before the candidate becomes eligible for further editorial review.

Do not merge based on detector status alone. Do not merge PR #29 wholesale. Any byte changes produced by conservative reconciliation invalidate the prior r22 half measurements for the new candidate; detector re-certification comes only after preservation, architecture, and holistic AI-shape preflight pass.