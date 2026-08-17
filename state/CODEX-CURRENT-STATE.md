# Joel Articles Codex Current State

Updated: 2026-08-17

## Goal

- Recover the complete owner-supplied 4.11.1 Project Source baseline into
  GitHub without overwriting newer active sources or changing article
  authority.

## Authority / baseline

- Repository: `u-dont-existDOTcom/joel-articles`
- Active branch: `migration/restore-4.11.1-project-sources-2026-08-17`
- Preserved pre-run head:
  `5fbdac8f4344a5bfeb4c96b5e0ce9a7b8f6b0837`.
- Owner ZIP SHA-256:
  `c0b6b0ce4d95b303a00cc44d75fdf54e4433fa72e39e9e866c84b856fde965b1`.
- Newer same-named Project/GitHub sources supersede their 4.11.1 copies.
- `articles/INDEX.json` remains the only article-authority registry and is
  still empty.

## Completed

- Recovered the existing remote branch and preserved its three prior commits.
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
- Completed the repository-local reference scan and recorded its
  classifications in `docs/PROJECT-SOURCE-4.11.1-RECOVERY-AUDIT.md`.
- Required repository gates pass: 84 unit tests; content and architecture-map
  validators; repository audit with 0 errors/4 existing warnings; patch
  hygiene. Recovery/checksum/protected-file checks and three supported tool
  self-tests also pass.
- The current ChatGPT Project still contains 10 sources; nothing was restored
  into the Project UI.

## Current checkpoint

- Exact-byte restoration is complete at `40 archived / 31 restored active / 9
  superseded archive-only`.
- Article registry/master authority changes: none.
- Unresolved repository-local source references: 1.
- Current step: commit all recovery changes, push this branch, and hand the
  exact branch-head SHA to the ChatGPT worker.

## Remaining

- ChatGPT worker inspects the pushed commit, opens/reviews the PR, verifies CI,
  and merges if accepted. This recovery worker must not merge it.
- Joel may supply `html_diff.py.txt` later if the optional quick-diff tool is
  still wanted; do not reconstruct it from prose.
- Existing repository-governance follow-up remains separate: default-branch
  rules, hosted secret controls, and license posture.
- Import one complete owner-authorized article family before substantive
  article editing or claiming canonical article content.

## Blockers / unresolved

- `html_diff.py.txt` is referenced by restored protocols but is absent from the
  exact 40-file package and repository. This is the single unresolved recovery
  reference; the baseline files themselves are fully recovered.
- No article authority exists in the repository. Do not infer a master from
  project sources, filenames, summaries, or chat.
- Licensing/copyright, privacy release, publication, and competing article
  masters remain owner-decision boundaries.

## Evidence / artifacts

- Recovery audit: `docs/PROJECT-SOURCE-4.11.1-RECOVERY-AUDIT.md`
- Snapshot manifest:
  `archive/project-source-snapshots/4.11.1/MANIFEST.json`
- Snapshot checksums:
  `archive/project-source-snapshots/4.11.1/SHA256SUMS.txt`
- Canonical loader: `CANONICAL-REPO-MAP.md`
- Article registry: `articles/INDEX.json`
- Recovery CLI: `scripts/restore_project_sources_4_11_1.py`

## Next safe action

- Commit all verified changes on the existing recovery branch, push it, and
  report the exact pushed SHA and `40 / 31 / 9 / 1` recovery counts. Do not
  merge to `main`.

## Recovery rule

After interruption, inspect the branch, worktree, snapshot manifest, and audit
before continuing. Preserve the nine current successors and empty article
registry; do not repeat restoration if the recovery CLI `--check` already
passes.
