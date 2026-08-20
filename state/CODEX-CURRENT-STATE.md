# Joel Articles Codex Current State

Updated: 2026-08-20

## Current posture

The 4.11.1 Project-source recovery and GitHub migration are complete. GitHub is the durable authority for governance, protocols, tooling, and any future registered article family.

GitHub hosted readback on 2026-08-20 confirms:

- repository visibility: **public**;
- default branch: `main`;
- `main` is **not protected** (`protected: false`; protection disabled).

The current ChatGPT Project instruction block presented to the worker matches the body of the archived minimal GitHub-canonical loader at `archive/chatgpt-project-retirement-2026-08-17/MINIMAL-PROJECT-INSTRUCTIONS.md`. No further Project-instruction rewrite is required on the evidence available here. The GitHub connector cannot inspect or delete ChatGPT Project Source files, so their current UI deletion state remains external to this repository; the last durable checkpoint reported 10 redundant Project Sources.

`u-dont-existDOTcom/AskRigor-lessons` remains outside this repository's public-disclosure boundary and private.

## Authority / baseline

- Repository: `u-dont-existDOTcom/joel-articles`
- Default branch: `main`
- Owner ZIP SHA-256:
  `c0b6b0ce4d95b303a00cc44d75fdf54e4433fa72e39e9e866c84b856fde965b1`.
- Newer same-named Project/GitHub sources supersede their 4.11.1 copies.
- `articles/INDEX.json` remains the only article-authority registry and is still empty.

## Completed

- Archived the exact ZIP and all 40 exact source members under
  `archive/project-source-snapshots/4.11.1/` with manifest, README, and checksums.
- Restored 31 absent baseline sources active and preserved all nine newer active successors byte-for-byte.
- Preserved historical `VOICE-REFERENCE(1).md` in the archive and restored its active destination as `project-sources/VOICE-REFERENCE.md`.
- Removed the obsolete Action/chunk transport and made the local-ZIP recovery CLI reproducible and idempotently verifiable.
- Expanded `CANONICAL-REPO-MAP.md` with least-set routes for article modes, humanization, research, voice/corpus, review packages, publishing, and interlinking.
- Recovered the optional `html_diff.py.txt` from Joel's File Library, added it to active `project-sources/`, and preserved the same Git blob under `archive/project-source-snapshots/optional-maintenance/`.
- Completed the repository-local reference scan. Final unresolved repository-local Project-source references: **0**.
- Required repository gates passed for the recovery: 84 unit tests; content and architecture-map validators; repository audit with 0 errors/4 existing governance warnings; patch hygiene; recovery/checksum/protected-file checks; supported tool self-tests.
- Exact-head GitHub Actions run for PR #11 passed all `content-integrity` steps.
- PR #11 merged successfully into `main` at `eea01a44608fe39f7a472be2a5c7c7757dd22bad`.
- Public-visibility transition completed 2026-08-19 after the repository credential/private-key audit passed.
- Current Project instructions now use the GitHub-canonical minimal loader; no additional instruction migration is required.
- Hosted-controls issue #3 was refreshed on 2026-08-20 so stale private-repository assumptions no longer masquerade as article blockers.

## Current checkpoint

- Project-source recovery and GitHub migration: **complete**.
- Exact baseline accounting: `40 archived / 31 restored active / 9 superseded archive-only`.
- Optional referenced tool recovery: `html_diff.py.txt` restored active and archived separately.
- Unresolved repository-local Project-source references: **0**.
- Project instruction cutover: **complete on the current runtime evidence**.
- Project Source-file deletion: **not observable through the GitHub connector**; last durable checkpoint reported 10 redundant UI sources.
- Repository visibility: **public**.
- Default-branch protection: **disabled** by fresh 2026-08-20 branch readback.
- Article registry/master authority changes: none; no article is canonical yet.

## Remaining work that actually matters

### 1. ChatGPT Project UI cleanup

If the ten redundant Project Source files reported by the prior checkpoint are still present, remove them from the Project UI. The instruction replacement itself is already complete. No source migration or restoration should be repeated.

This is a UI-only cleanup. Failure to delete those redundant copies does not make them authoritative; GitHub remains canonical.

### 2. Hosted GitHub hardening

Track in issue #3. These are operational safeguards, not prerequisites for article authority:

- enable a default-branch ruleset/branch protection for `main` requiring pull requests and the stable `content-integrity` check; block force pushes and branch deletion;
- verify secret scanning and push protection and enable them when available/appropriate;
- verify Actions default permissions are read-only and keep fork-origin workflow permissions conservative;
- verify hosted Dependabot alert posture; `.github/dependabot.yml` exists, but hosted alert enablement has not been directly read back;
- decide whether code scanning adds enough value for the current Python/tooling surface, then either enable it or record a reasoned not-applicable disposition.

Private vulnerability reporting is no longer treated as an article/governance blocker. A security-reporting channel may still be chosen separately if useful.

### 3. Owner policy decisions

Copyright/license posture remains an owner decision. Public visibility does not imply a license. Do not add a license or all-rights-reserved notice by inference.

### 4. First article authority import

Before substantive article editing or any claim that a repository article is canonical, import one complete owner-authorized article family through the registered authority process. The repository must not choose among competing masters or reconstruct one from chat, Project Sources, filenames, detached packets, or memory.

This is the only current blocker to repository-backed canonical article editing.

## Evidence / artifacts

- Recovery audit: `docs/PROJECT-SOURCE-4.11.1-RECOVERY-AUDIT.md`
- Final closeout: `docs/PROJECT-SOURCE-4.11.1-RECOVERY-CLOSEOUT.md`
- Historical hosted-controls report: `docs/CODEX-GITHUB-COMPLIANCE-2026-08-14.md`
- Current hosted-controls tracker: issue #3
- Snapshot manifest: `archive/project-source-snapshots/4.11.1/MANIFEST.json`
- Snapshot checksums: `archive/project-source-snapshots/4.11.1/SHA256SUMS.txt`
- Optional maintenance archive: `archive/project-source-snapshots/optional-maintenance/html_diff.py.txt`
- Canonical loader: `CANONICAL-REPO-MAP.md`
- Minimal Project instructions: `archive/chatgpt-project-retirement-2026-08-17/MINIMAL-PROJECT-INSTRUCTIONS.md`
- Article registry: `articles/INDEX.json`
- Recovery CLI: `scripts/restore_project_sources_4_11_1.py`
- Recovery merge: PR #11 / `eea01a44608fe39f7a472be2a5c7c7757dd22bad`
- Public visibility preparation merge: `f7876a7d8056219106227806570c6823c3f9d29c`

## Next safe action

- Do not repeat Project-source restoration or rewrite the Project loader again.
- Remove redundant Project Source files in the ChatGPT Project UI if they are still present.
- Harden hosted GitHub settings when direct settings access is available; do not falsely report unverified settings as enabled.
- When Joel identifies the exact owner-authorized article master to import, follow `docs/CONTENT-AUTHORITY-AND-IMPORT.md` and register the resulting complete hash-bound article family in `articles/INDEX.json`.

## Recovery rule

After interruption, read `SKILL.md`, `CANONICAL-REPO-MAP.md`, this state file, and the article registry fresh. Do not repeat Project-source restoration; the recovery is complete and durable on `main` once this refresh is merged.
