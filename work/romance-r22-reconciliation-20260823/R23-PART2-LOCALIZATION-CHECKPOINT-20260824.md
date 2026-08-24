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

## Current no-cost recovery route

Private executor PR #23, merged as `45b4dfcac56d68d7546da94b1c75e08532c04e99`, adds `inspect-pangram-report-dom.yml` plus trusted private `scripts/inspect_pangram_report_dom.py`.

The inspector:
- reads only the already-completed Pangram 4 result;
- validates exact input SHA and stored report URL;
- opens the already-paid stored report in the dedicated authenticated browser profile;
- records only visible DOM elements carrying highlight/segment metadata or red-ish visual styling, with bounded surrounding text;
- omits cookies, browser storage, headers, credentials, and full HTML;
- contains no detector submission command and no Pangram API-key path.

Next evidence branch to create:
`evidence/pangram-report-dom/romance-r23-part2-20260824-a`.

## Editorial gate remains unchanged

Until the single residual is localized or Joel explicitly accepts it:
- r23 remains a reconciliation candidate, not registered article authority;
- registered `main:articles/romance/master.md` remains unchanged;
- preservation proof remains PASS with zero unexplained substantive deltas for the current r23 candidate;
- exact r22 remains the known-green rollback anchor;
- if a prose repair is justified, preserve the authorized r23 feature/function, use the smallest natural edit scope, rerun preservation/architecture checks, and certify the changed Part-2 composition boundary through GUI under the current long-boundary cost policy.
