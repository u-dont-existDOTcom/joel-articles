# Romance r23 Part 2 localization checkpoint — 2026-08-24

## Exact measured boundary

- r23 Part 2 SHA-256: `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`
- words: 9,917
- Pangram 4.0 / `STAGE_SUCCESS`
- Human `0.9965084195`
- AI `0.0034915956`
- AI-assisted `0.0`
- stored report: exactly one AI-generated segment
- exact result/evidence branch: `u-dont-existDOTcom/pangram-humanization-lab@evidence/romance-r23-gui-20260824-a`

Do not resubmit this exact half merely to localize the residual.

## Read-only localization attempts

### History-list attempt

Evidence branch: `evidence/pangram-history-localization/romance-r23-part2-20260824-a`.

- exact already-paid input/result identity verified before browser work;
- browser tooling install initially failed once because runner DNS could not resolve PyPI; rerun succeeded;
- History scan saw 10 candidates;
- exact record did not bind;
- failed at `bind_exact_history_record`;
- `detector_submission_attempted: false`.

### Direct stored-report attempt

Evidence branch: `evidence/pangram-history-localization/romance-r23-part2-direct-20260824-a`.

- exact already-paid input/result identity verified;
- exact stored `report_url` from the completed SHA-bound result was validated and requested directly;
- `direct_report_requested: true`;
- structured History record still did not bind;
- failed at `bind_exact_history_record`;
- `detector_submission_attempted: false`.

This reproduces Pangram lab issue #110 on a fresh r23 boundary. Do not buy a detector call to debug History localization.

## Stored-report DOM attempt

The first standalone stored-report DOM inspection completed successfully on Actions run `32759869533`, exact evidence branch:
`evidence/pangram-report-dom/romance-r23-part2-20260824-a`.

It made no detector submission. However its v1 visual heuristic produced a false positive: the only retained candidates were Pangram's orange active `Overview` / `Details` navigation tabs. It did **not** identify the residual article segment. Those DOM candidates are diagnostic evidence only and must not be treated as localization authority.

Private executor PR #26 hardens the inspector so navigation controls are excluded and bounded AI-Highlight ancestry, pseudo-element styling, visual candidates, and rare text-style signatures are collected. It also adds immutable `report-inspection-requests/*.json` push dispatch so connected GitHub automation can request this read-only recovery without requiring Joel to run `gh workflow run` manually.

A v2 request is now durably committed in the private executor for a new evidence branch:
`evidence/pangram-report-dom/romance-r23-part2-v2-20260824-a`.

## Workflow correction

The larger architecture problem is fixed independently of this legacy recovery.

The original paid GUI execution already had the exact stored report available, but persisted aggregate result/body/PDF and then released the browser/runner without preserving the highlight needed for the next editorial decision. That forced a second queued recovery job through unreliable History state.

Private executor PR #25 changes the Romance long-GUI execution path so any completed non-green exact result receives free report-DOM post-processing in the **same self-hosted GUI job before the runner is released**. Exact-green results skip it. The auxiliary capture cannot override or ambiguate a completed paid score and has no detector-submission path.

Pangram lab PR #139 records the general rule: evidence needed to interpret a paid GUI result should be captured at score time; post-hoc History recovery is fallback for legacy/interrupted runs, not the normal production path.

## Editorial gate remains unchanged

Until the single residual is localized or Joel explicitly accepts it:
- r23 remains a reconciliation candidate, not registered article authority;
- registered `main:articles/romance/master.md` remains unchanged;
- preservation proof remains PASS with zero unexplained substantive deltas for the current r23 candidate;
- exact r22 remains the known-green rollback anchor;
- if a prose repair is justified, preserve the authorized r23 feature/function, use the smallest natural edit scope, rerun preservation/architecture checks, and certify the changed Part-2 composition boundary through GUI under the current long-boundary cost policy.
