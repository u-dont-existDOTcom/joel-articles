# Exact Git write handoff for Article work

Status: **ACTIVE FALLBACK ROUTE / NORMAL CONNECTOR WRITES STILL PREFERRED**

Use this only when an ordinary connected GitHub mutation is unavailable while repository reads and independent GitHub access remain healthy.

Canonical reusable implementation currently lives in `u-dont-existDOTcom/universal-dev-architecture` on branch `task/exact-git-write-handoff-20260911`, commit `4850583ad19eb915f15212199bd5b32750512e4b`.

Relevant files:
- `patterns/exact-git-write-handoff.md`
- `templates/EXACT-GIT-WRITE-MANIFEST.json`
- `scripts/git_exact_manifest.py`
- `scripts/git_exact_repo.py`
- `scripts/git_exact_write.py`
- `tests/test_git_exact_write.py`

## Routing rule

1. Attempt the ordinary GitHub connector write first.
2. If the mutation is rejected before a GitHub commit exists, do not infer repository/auth failure when reads remain healthy.
3. Freeze the exact operation in the universal manifest: repository, branch, path, base commit/blob, payload SHA-256/byte count, expected postimage SHA-256, and commit message.
4. Route only the mechanical local Git operation to an authorized local execution surface. The helper validates the clean worktree, branch/base/blob, payload identity, exact one-path staging, `git diff --cached --check`, and emits a local-commit receipt.
5. Push the resulting exact commit normally from the local checkout.
6. Chat then reads the remote ref/path and verifies the expected bytes before treating GitHub durability as complete.

A local artifact or local commit is never canonical merely because the connector path was unavailable. Remote GitHub readback remains the completion boundary.

Do not use encoding, encryption, fragmentation, or another content transformation merely to make a rejected connector mutation pass. If literal bytes cannot be carried through the normal connector, keep them exact and use the mechanical local-Git route instead.

## Current verification

The universal implementation was installed from an exact local bundle and pushed on 2026-09-12. Connected GitHub readback verified the remote branch and executable source. The branch commit contains exactly six intended added files and is based directly on the then-current universal `main` commit `568c8c288fc8ba6736a46d0f3435fd7a636bf20a`.

The bundled focused regression suite contained 12 tests covering create/update/delete, payload mismatch, dirty worktree, wrong branch/base/blob, path traversal, receipt placement, rollback after post-write validation failure, and credential-safe origin mismatch handling.

This fallback changes transport/execution only. It does not change article authority, semantic review, owner locks, preservation requirements, publication authority, or detector policy.
