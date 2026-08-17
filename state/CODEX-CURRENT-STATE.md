# Joel Articles Codex Current State

Updated: 2026-08-17

## Goal

- Recover the complete owner-supplied 4.11.1 Project Source baseline into
  GitHub without overwriting newer active sources or changing article
  authority.

## Authority / baseline

- Repository: `u-dont-existDOTcom/joel-articles`
- Active branch: `migration/restore-4.11.1-project-sources-2026-08-17`
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
  `archive/project-source-snapshots/optional-maintenance/`. It was not one of
  the owner-supplied 40 baseline files and therefore does not change the
  `40 / 31 / 9` recovery counts.
- Completed the repository-local reference scan. The final unresolved
  repository-local source-reference count is **0**.
- Before the optional-tool closeout, required repository gates passed: 84 unit
  tests; content and architecture-map validators; repository audit with 0
  errors/4 existing governance warnings; patch hygiene. Recovery/checksum/
  protected-file checks and three supported tool self-tests also passed.
- The current ChatGPT Project still contains 10 sources; nothing was restored
  into the Project UI.

## Current checkpoint

- Exact-byte baseline restoration is complete at `40 archived / 31 restored
  active / 9 superseded archive-only`.
- Optional referenced tool recovery: `html_diff.py.txt` restored active and
  archived separately.
- Article registry/master authority changes: none.
- Unresolved repository-local source references: **0**.
- Current step: open the recovery PR, verify exact-head CI, and merge if green.

## Remaining

- Verify GitHub Actions on the exact current branch head and merge the recovery
  PR if all required checks pass.
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
- Article registry: `articles/INDEX.json`
- Recovery CLI: `scripts/restore_project_sources_4_11_1.py`

## Next safe action

- Verify the exact pushed branch head through a pull request and GitHub Actions.
  Merge only if required checks are green.

## Recovery rule

After interruption, inspect the branch, snapshot manifest, audit, closeout, and
CI before continuing. Preserve the nine current successors and empty article
registry; do not repeat baseline restoration if the recovery CLI `--check`
already passes.
