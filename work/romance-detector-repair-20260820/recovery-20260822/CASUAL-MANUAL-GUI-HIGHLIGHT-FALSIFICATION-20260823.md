# Casual opening manual-GUI highlight falsification — 2026-08-23

Status: diagnostic evidence only. No article prose authority change.

## Context

In a 211-word Pangram 4 GUI test of the current `Can Casual Sex or a Situationship Actually Be Honest?` opening, Joel observed that only the beginning and ending were highlighted AI while the middle was Human (overall about 40% AI in the GUI screenshot).

The assistant hypothesized that the highlighted ends were polished conceptual wrappers and proposed changing only those wrappers while preserving the Human middle.

## Owner-reported falsification

Joel tested that assistant wrapper-only candidate manually and reported:

> `that whole thing is now 100% high conf ai!`

The candidate changed only the displayed-red beginning and ending; the previously Human middle was intentionally preserved.

## Consequence

This falsifies the assumption that the GUI-highlighted red spans were sufficient causal edit loci. On this small natural boundary, changing only the ends was enough to reclassify the unchanged middle as high-confidence AI. Therefore:

- do not promote the assistant wrapper rewrite;
- do not use GUI highlight extent as the preservation/edit scope;
- preserve the registered-main/r19 Casual opening until direct owner wording or a stronger source realization supersedes it;
- if further diagnostics are worthwhile, change one variable at a time on the original 211-word boundary and keep every other byte fixed;
- Casual's assistant-run local paid loop remains closed at 6/6 unless Joel explicitly changes the budget.

Durable detector incident is recorded in `u-dont-existDOTcom/pangram-humanization-lab:automation/pangram-fixed-batch/state/ROMANCE-CASUAL-LOCAL-HIGHLIGHT-NONCAUSAL-INCIDENT-2026-08-23.md`.
