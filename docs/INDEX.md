# Article documentation index

Status: **ACTIVE.** `articles/INDEX.json` currently registers Romance and Somatic Therapies as working canonical articles.

## Read order

1. `../state/CODEX-CURRENT-STATE.md` — repository checkpoint and exact current posture
2. `../articles/INDEX.json` — registered article packages and hashes
3. the target registered article's `CURRENT-STATE.md`, then its registered owner locks, architecture, master, source evidence, detector/citation/editorial records as required by the task
4. `../ARTICLE-META-MAP.md` — repository-wide Mermaid index for article relationships, interlinks, and deduplication opportunities
5. `CONTENT-AUTHORITY-AND-IMPORT.md` — authority model and required per-article family
6. `ARTICLE-ARCHITECTURE-MAPS.md` — required per-article Mermaid architecture maps plus meta-map update/validation contract
7. `SUPPLIED-SOURCE-PACKET-MANIFEST.md` — external packet provenance and non-import status

Historical branches and packets may remain useful provenance/evidence, but they do not override a registered article family.

## General article protocols

- `HUMANIZATION-PRESERVATION-GATE.md` — **blocking pre-detector preservation proof** for P2S/P3/P4 reconstruction and detector-driven semantic edits. Freeze changed-scope preservation units and an authorized-change whitelist before drafting; then require bidirectional source↔candidate traceability and zero unexplained substantive deltas before a paid/certification detector call. Re-run after every detector-driven semantic edit.
- `HUMANIZATION-PRESERVATION-TOOLING.md` — machine-readable receipt/template/validator path for the preservation gate. A passing receipt proves recorded gate completion, not semantic equivalence; substantive unit selection and mappings remain editorial judgments.
- `HUMANIZATION-ARCHITECTURE-GATE.md` — blocking article-wide architecture regression for humanization/detector work. Run before detector testing and after every detector-driven edit; 100% Human never overrides preservation proof, heading fit, paragraph jobs, live-question continuity, protected functions, owner-realization placement, or fidelity.
- `HUMANIZATION-KNOWN-GREEN-CALIBRATION.md` — **known-green guard** for production humanization. Exact Pangram-Human passages are calibration anchors: do not reopen them for detector reasons merely because they resemble a learned AI-shape pattern, and do not revert detector-green working rewrites merely because older wording has higher registration authority. Real editorial defects may still justify changes, but name them directly and keep detector likelihood separate from style intuition.
- `../project-sources/IDIOLECT-PRESERVATION-PROTOCOL.md` — minimum-dose humanization, three-axis fidelity/detector/authorship-retention separation, corpus provenance, Joel-only retention proxy, true closed-set IER boundary, privacy, and anti-gaming rules.
- `IDIOLECT-VALIDATION-STATUS.md` — current calibration status for the fast retention proxy and routing to the Pangram lab's paper-faithful SVM/LUAR/topic-control validation lane. Until a register is validated there, local retention output remains directional evidence only.
- `ARTICLE-ARCHITECTURE-MAPS.md` — requires one living Mermaid section/function map per article plus the repository article meta-map. Use them to prevent placement drift, orphaned protected functions, stale owner-supersession routing, missed interlinks, and duplicate coverage.
- `EDITORIAL-SCOPE-AND-PLACEMENT.md` — separates protected rhetorical function from placement, preserves owner-approved thought architecture from synthetic source prose, and prevents an editing/humanization pass from turning into unsolicited fact-checking.
- `CODEX-GITHUB-COMPLIANCE-2026-08-14.md` — historical hosted-control audit; current hosted-control follow-up is operational hardening, not article authority

The required article-local family is defined centrally and enforced by `scripts/validate_content_repository.py`; Mermaid map structure is enforced by `scripts/validate_article_architecture_maps.py`. Current owner instructions and verified, registered article files outrank maps, stale summaries, detached helper files, external packets, remembered chat context, detector results, or idiolect measurements.
