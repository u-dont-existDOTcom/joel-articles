# Article documentation index

Status: **BLOCKED governance incubator.** No article is canonical in this repository yet.

## Read order

1. `../state/CODEX-CURRENT-STATE.md` — repository checkpoint and exact blockers
2. `../articles/INDEX.json` — registered article packages and hashes; currently empty
3. `../ARTICLE-META-MAP.md` — repository-wide Mermaid index for article relationships, interlinks, and deduplication opportunities
4. `CONTENT-AUTHORITY-AND-IMPORT.md` — authority model and required per-article family
5. `ARTICLE-ARCHITECTURE-MAPS.md` — required per-article Mermaid architecture maps plus meta-map update/validation contract
6. `SUPPLIED-SOURCE-PACKET-MANIFEST.md` — external packet provenance and non-import status
7. the target article's registered `ARCHITECTURE.md`, current state, owner locks, master, evidence, and review records, once an article exists

## General article protocols

- `HUMANIZATION-ARCHITECTURE-GATE.md` — blocking article-wide architecture regression for humanization/detector work. Run before detector testing and after every detector-driven edit; 100% Human never overrides heading fit, paragraph jobs, live-question continuity, protected functions, owner-realization placement, or fidelity.
- `IDIOLECT-PRESERVATION.md` — active named-byline guard against detector-driven or generic-polish erasure of Joel-specific authorship signal; enforces minimum transformation and provenance hygiene while keeping quantitative authorship scoring provisional until the Pangram lab calibration passes.
- `ARTICLE-ARCHITECTURE-MAPS.md` — requires one living Mermaid section/function map per article plus the repository article meta-map. Use them to prevent placement drift, orphaned protected functions, stale owner-supersession routing, missed interlinks, and duplicate coverage.
- `EDITORIAL-SCOPE-AND-PLACEMENT.md` — separates protected rhetorical function from placement, preserves owner-approved thought architecture from synthetic source prose, and prevents an editing/humanization pass from turning into unsolicited fact-checking.
- `CODEX-GITHUB-COMPLIANCE-2026-08-14.md` — repository/hosted-control audit and exact blocked status

The required article-local family is defined centrally and enforced by `scripts/validate_content_repository.py`; Mermaid map structure is enforced by `scripts/validate_article_architecture_maps.py`. Current owner instructions and verified, registered article files outrank maps, stale summaries, detached helper files, external packets, or remembered chat context.
