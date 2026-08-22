# Owner correction — Pangram six-call cap is section-only — 2026-08-21

Status: **direct Joel owner correction; supersedes conflicting task metadata immediately.**

Joel clarified that the six-paid-call hard cap is per **genuine local repair section**, not per article, article half, or other aggregate certification boundary.

## Romance consequence

The historical Part-2 ledger reached six paid aggregate Part-2 measurements through pass 6. Those measurements remain valid accounting and detector evidence, but **6/6 is not a current blocker** because `Part 2` is a roughly 10k-word multi-section article half, not one repair section.

Therefore the following older task statements are superseded wherever they appear:

- `no automatic paid call_audit_cap_exhausted_6_of_6` for the owner-integrated Part 2;
- `any seventh full-Part2 call requires explicit owner authorization`;
- descriptions of pass 6 as the final permissible Part-2 measurement under a Part-2-wide cap.

The owner-integrated Part-2 candidate remains:

- SHA-256 `9dc539ca99f8c747ecd5a551f2c72ad476c87671919863d2ad469acf6c6e696f`
- 9,804 whitespace words
- Part 1 unchanged SHA-256 `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`

A fresh exact aggregate Part-2 measurement is now allowed when editorially warranted. It must still use exact cache/recovery/checkpoint/version gates and must not repeat an already completed exact hash.

## Local section caps remain

Each actual repair section still has a hard maximum of six new paid Pangram POSTs per stable audit + section + model/version unless Joel explicitly authorizes otherwise. Renaming/rebatching/retransporting the same local section does not reset that local cap.

## Harness state

`u-dont-existDOTcom/pangram-humanization-lab:automation/pangram-fixed-batch` now distinguishes `budget_scope: "section"` (capped) from `budget_scope: "aggregate"` (accounted but not section-capped), and the fixed-batch safety gate passed after the correction.
