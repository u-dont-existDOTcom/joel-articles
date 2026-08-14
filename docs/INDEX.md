# Article documentation index

Status: **BLOCKED governance incubator.** No article is canonical in this repository yet.

## Read order

1. `../state/CODEX-CURRENT-STATE.md` — repository checkpoint and exact blockers
2. `../articles/INDEX.json` — registered article packages and hashes; currently empty
3. `CONTENT-AUTHORITY-AND-IMPORT.md` — authority model and required per-article family
4. `SUPPLIED-SOURCE-PACKET-MANIFEST.md` — external packet provenance and non-import status
5. the target article's registered current state, owner locks, master, evidence, and review records, once an article exists

## General article protocols

- `HUMANIZATION-ARCHITECTURE-GATE.md` — blocking article-wide architecture regression for humanization/detector work. Run before detector testing and after every detector-driven edit; 100% Human never overrides heading fit, paragraph jobs, live-question continuity, protected functions, owner-realization placement, or fidelity.
- `EDITORIAL-SCOPE-AND-PLACEMENT.md` — separates protected rhetorical function from placement, preserves owner-approved thought architecture from synthetic source prose, and prevents an editing/humanization pass from turning into unsolicited fact-checking.
- `CODEX-GITHUB-COMPLIANCE-2026-08-14.md` — repository/hosted-control audit and exact blocked status

The required article-local family is defined centrally and enforced by `scripts/validate_content_repository.py`. Current owner instructions and verified, registered article files outrank stale summaries, detached helper files, external packets, or remembered chat context.
