# Joel Articles Codex Current State

Updated: 2026-08-14

## Goal

- Make long-form article work resumable and loss-resistant while preserving Joel's actual arguments, owner-locked passages, source provenance, and article-specific editorial/detector evidence.

## Authority / baseline

- Repository: `u-dont-existDOTcom/joel-articles`
- Branch: `main`
- Current explicit owner wording/argument corrections outrank older drafts and summaries.
- Project-specific article state and evidence remain here; general workflow lessons belong in `u-dont-existDOTcom/universal-dev-architecture`.

## Completed

- Recovered live GitHub and branch state before editing; the stale unfinished `codex-governance` branch was not reused because `main` is the later governance superset.
- Verified the repository contains governance files only: no canonical master, source package, owner-final decisions, citation/detector/editorial record, or per-article state is imported.
- Added an empty canonical article registry, complete hash-bound import family, exact owner-lock checks, reversible-deletion rules, citation/detector limits, publication provenance, privacy boundaries, and deterministic tests.
- Added the current Universal repository/workflow auditor and portable workflow-policy template with regression coverage.
- Added one stable least-privilege `content-integrity` workflow and exact local commands.
- Recorded the external ten-file packet by received name/hash/size/disposition without copying its contents or publishing potentially sensitive facts.
- Verified hosted truth: default-branch rules disabled; private vulnerability reporting disabled; Dependabot alerts disabled; secret scanning, push protection, code scanning, and Actions defaults unverified.
- Opened GitHub issue #3 as the durable owner/hosted-control blocker ledger.

## Current checkpoint

- Current step: verify the evidence-only closeout head, mark PR #4 ready, and merge if repository policy permits.
- Recovered baseline: `main@5f0585f1a9fe5a3d5c2622f5bcaa84ffc025a71d`.
- Active task branch: `codex/github-compliance-2026-08-14`.
- Verified code-bearing head/tree: `dcde124ef2f983c5027d85481f9aa33b2c353d9b` / `aa48d3bbf5bdeba852ee2c191bbc5c5be6af3ab4`.
- Exact GitHub Actions run/job: `31785508088` / `94720404470` — success; 56 tests, truthful empty-incubator validation, repository audit 0 errors/4 warnings.
- Independent exact-head review: Ready; no remaining Critical, Important, or Minor finding.

## Remaining

- Complete review and merge the verified governance baseline if no actionable finding remains.
- Promote the bounded editorial authority/owner-lock/lossless-editing lesson to `universal-dev-architecture` with exact Joel provenance.
- Obtain the owner copyright/license decision; do not infer it.
- Enable a private vulnerability-reporting channel and a default-branch ruleset requiring pull requests and `content-integrity`; verify remaining hosted security/Actions controls.
- Import one complete, owner-authorized article family before performing substantive article editing or claiming canonical content.

## Blockers / unresolved

- Overall status remains **BLOCKED** even when repository checks pass.
- No article authority exists in the repository. Do not reconstruct a master from the external packet, filenames, summaries, or chat.
- The supplied `CANON-FACTS.md` may contain sensitive personal/health facts and is not approved for this public repository.
- Licensing/copyright, competing canonical masters, substantive prose changes, privacy release, and publication require owner decisions.
- Never silently soften or replace Joel's arguments. Detector results remain evidence, not editorial authority.

## Evidence / artifacts

- Repository profile: `.github/codex-repository.json`
- Canonical article registry: `articles/INDEX.json`
- Authority/import protocol: `docs/CONTENT-AUTHORITY-AND-IMPORT.md`
- External packet manifest: `docs/SUPPLIED-SOURCE-PACKET-MANIFEST.md`
- Compliance report: `docs/CODEX-GITHUB-COMPLIANCE-2026-08-14.md`
- Durable blocker ledger: https://github.com/u-dont-existDOTcom/joel-articles/issues/3
- Universal operating standard: `patterns/codex-github-operating-system.md` in `universal-dev-architecture`

## Next safe action

- Inspect PR #4 at the verified code-bearing baseline. If independent review and the evidence-only closeout run are green, mark ready and merge without changing content logic; otherwise repair the exact finding and re-verify.

## Recovery rule

After interruption, a fresh thread, context compaction, or model switch, inspect actual repository and article state first. Identify exactly what survived, preserve owner-locked text, repair stale routing, and resume without repeating completed editorial work.
