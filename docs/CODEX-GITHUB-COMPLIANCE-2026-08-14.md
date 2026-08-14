# Codex + GitHub compliance report — 2026-08-14

## Outcome

Repository governance baseline: **verified at the exact code-bearing task-branch head**.

Overall repository/content status: **BLOCKED**. No canonical article package is imported, the owner has not selected a copyright/license posture, and required hosted controls remain disabled or unverified. This report does not call the repository compliant merely because local checks pass.

## Recovered baseline

- Repository: `u-dont-existDOTcom/joel-articles`
- Visibility/risk: public, active, long-running, high-risk content
- Default branch before this work: `main@5f0585f1a9fe5a3d5c2622f5bcaa84ffc025a71d`
- Pre-existing unfinished branch: `codex-governance@a9f858adfe834537d5cc2b9367b6ff85c60180aa`, four commits ahead and ten behind `main`; not reused because `main` is the later governance superset
- Superseded lesson branch: `lesson/humanization-architecture-regression-2026-08-14@14a0bdbe476412a596df4fee7b48e97c5a9901a6`, content-equivalent to recovered `main`
- Pre-existing canonical article/source packages: none

## Implemented boundary

- canonical empty article registry and complete per-article authority schema;
- hash-bound masters, owner locks, evidence, state, review records, and exports;
- exact locked-passage preservation and reversible-deletion rules;
- claim-local citation uncertainty and detector-evidence limits;
- deterministic content/privacy/export validator with regression tests;
- current Universal repository/workflow auditor, portable policy template, and regression tests;
- stable least-privilege content-integrity workflow;
- single canonical recovery checkpoint and compatibility pointer;
- public security/contribution guidance and expanded CODEOWNERS;
- exact external packet manifest without publishing packet contents;
- expanded pull-request boundary/provenance/integrity/lesson closeout.

No article prose, private facts, source packet contents, credentials, paid API calls, detector calls, or publication actions are included.

## Hosted control evidence

Verified through GitHub on 2026-08-14:

| Control | State | Evidence/impact |
|---|---|---|
| Default-branch rules | Disabled | `main` reports `protected: false`; repository rulesets response is empty |
| Private vulnerability reporting | Disabled | Repository private-reporting endpoint returned `enabled: false` |
| Dependabot alerts | Disabled | Alerts endpoint reported alerts disabled |
| Secret scanning | Unverified | Available integration could not read the setting |
| Push protection | Unverified | Available integration could not read the setting |
| Code scanning/default setup | Unverified | Available integration could not read the setting; validator code now exists |
| Actions default permissions | Unverified | Available integration could not read the setting |

Exact owner and hosted follow-up is tracked in [GitHub issue #3](https://github.com/u-dont-existDOTcom/joel-articles/issues/3). No unavailable setting is represented as enabled.

## Copyright/license

No `LICENSE` file or copyright notice was added. Choosing between an owner-approved license and an explicit all-rights-reserved posture is an owner decision and remains blocking in issue #3. Public visibility alone is not treated as a license.

## Verification evidence

- Exact code-bearing head: `3d77e88dde52015bbc66276940e1b58ec3622da3`
- Exact code tree: `2607a11ee27a863ef4d04918d1cb42779ddfb701`
- GitHub Actions run/job: `31785153880` / `94719318290` — success

- `python -m unittest discover -s tests`: 53 tests passed in GitHub Actions
- `python scripts/validate_content_repository.py --root .`: passed; `governance_incubator`, 0 registered articles, canonical content import remains BLOCKED
- `python scripts/audit_codex_github.py --root . --fail-on error`: 0 errors, 4 truthful warnings
- `git diff --check`: passed locally before publication
- Workflow steps for checkout, regression tests, content validation, and repository audit all concluded success
- Review-remediation coverage rejects registered/unregistered incubator mismatches, detached/unregistered article files, detached legacy content roots, and symlink traversal outside article families; approved extra files require hash-bound `additional_artifacts` entries

The four audit warnings are the intended truthful state: disabled default-branch rules, unverified secret scanning, unverified push protection, and absent owner-selected license. They are blockers or follow-up items, not hidden green claims.

## Residual blockers

1. Owner copyright/license decision.
2. Private vulnerability reporting channel.
3. Default-branch pull-request/ruleset enforcement.
4. Hosted security and Actions settings verification/enablement.
5. One complete owner-authorized article authority family.

Until all are resolved, recovery must preserve status **BLOCKED**.
