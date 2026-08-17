# Joel Articles Codex Current State

Updated: 2026-08-17

## Goal

- Recover the complete owner-supplied 4.11.1 Project Source baseline into
  GitHub without overwriting newer active sources or changing article
  authority, then complete the ChatGPT Project-source cutover.

## Authority / baseline

- Repository: `u-dont-existDOTcom/joel-articles`
- Default branch: `main`
- Owner ZIP SHA-256:
  `c0b6b0ce4d95b303a00cc44d75fdf54e4433fa72e39e9e866c84b856fde965b1`.
- Newer same-named Project/GitHub sources supersede their 4.11.1 copies.
- `articles/INDEX.json` remains the only article-authority registry and is
  still empty.

## Completed

- Archived the exact ZIP and all 40 exact source members under
  `archive/project-source-snapshots/4.11.1/` with manifest, README, and
  checksums.
- Restored 31 absent baseline sources active and preserved all nine newer
  active successors byte-for-byte.
- Preserved historical `VOICE-REFERENCE(1).md` in the archive and restored its
  active destination as `project-sources/VOICE-REFERENCE.md`.
- Removed the obsolete Action/chunk transport and made the local-ZIP recovery
  CLI reproducible and idempotently verifiable.
- Expanded `CANONICAL-REPO-MAP.md` with least-set routes for article modes,
  humanization, research, voice/corpus, review packages, publishing, and
  interlinking.
- Recovered the optional `html_diff.py.txt` from Joel's File Library, added it
  to active `project-sources/`, and preserved the same Git blob under
  `archive/project-source-snapshots/optional-maintenance/`.
- Completed the repository-local reference scan. Final unresolved
  repository-local Project-source references: **0**.
- Required repository gates passed: 84 unit tests; content and architecture-map
  validators; repository audit with 0 errors/4 existing governance warnings;
  patch hygiene; recovery/checksum/protected-file checks; supported tool
  self-tests.
- Exact-head GitHub Actions run for PR #11 passed all `content-integrity`
  steps.
- PR #11 merged successfully into `main` at
  `eea01a44608fe39f7a472be2a5c7c7757dd22bad`.
- The current ChatGPT Project still contains 10 sources; nothing was restored
  into the Project UI.

## Current checkpoint

- Project-source recovery and GitHub migration are **complete**.
- Exact baseline accounting: `40 archived / 31 restored active / 9 superseded
  archive-only`.
- Optional referenced tool recovery: `html_diff.py.txt` restored active and
  archived separately.
- Article registry/master authority changes: none.
- Unresolved Project-source references: **0**.
- Current Project cleanup is safe: the remaining 10 Project Sources are now
  redundant with GitHub authority/archive and may be removed from the ChatGPT
  Project after replacing Project Instructions with the minimal GitHub loader.

## Remaining

- ChatGPT Project UI cleanup only: replace Project Instructions with the minimal
  GitHub-canonical loader and remove the 10 redundant Project Source files.
- Existing repository-governance follow-up remains separate: default-branch
  rules, hosted secret controls, and license posture.
- Import one complete owner-authorized article family before substantive
  article editing or claiming canonical article content.

## Blockers / unresolved

- No Project-source recovery blocker remains.
- No article authority exists in the repository. Do not infer a master from
  project sources, filenames, summaries, or chat.
- Licensing/copyright, privacy release, publication, and competing article
  masters remain owner-decision boundaries.

## Evidence / artifacts

- Recovery audit: `docs/PROJECT-SOURCE-4.11.1-RECOVERY-AUDIT.md`
- Final closeout: `docs/PROJECT-SOURCE-4.11.1-RECOVERY-CLOSEOUT.md`
- Snapshot manifest:
  `archive/project-source-snapshots/4.11.1/MANIFEST.json`
- Snapshot checksums:
  `archive/project-source-snapshots/4.11.1/SHA256SUMS.txt`
- Optional maintenance archive:
  `archive/project-source-snapshots/optional-maintenance/html_diff.py.txt`
- Canonical loader: `CANONICAL-REPO-MAP.md`
- Minimal Project instructions:
  `archive/chatgpt-project-retirement-2026-08-17/MINIMAL-PROJECT-INSTRUCTIONS.md`
- Article registry: `articles/INDEX.json`
- Recovery CLI: `scripts/restore_project_sources_4_11_1.py`
- Recovery merge: PR #11 / `eea01a44608fe39f7a472be2a5c7c7757dd22bad`.

## Next safe action

- Complete only the ChatGPT Project UI cleanup. No further source migration is
  required unless Joel supplies a newer source that should supersede current
  GitHub authority.

## Recovery rule

After interruption, read `SKILL.md`, `CANONICAL-REPO-MAP.md`, this state file,
and the article registry fresh. Do not repeat Project-source restoration; the
recovery is complete and durable on `main`.
