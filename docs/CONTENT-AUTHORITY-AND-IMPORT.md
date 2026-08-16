# Content authority and import protocol

## Current truth

No article master or source package is currently imported. `articles/INDEX.json` is intentionally empty and the repository remains a governance incubator. A passing repository gate confirms that this absence is represented truthfully; it does not elevate scaffolding, chat, detached files, or an external packet into article authority.

## Authority order

For a registered article, read and resolve conflicts in this order:

1. current explicit owner instructions and article acceptance criteria;
2. the article entry and exact hashes in `articles/INDEX.json`;
3. the registered article current state and owner-lock manifest;
4. the registered master;
5. registered source/evidence, citation, editorial, and detector records;
6. publication/export provenance and Git history;
7. article-local `ARCHITECTURE.md` and repository `ARTICLE-META-MAP.md` as visual indexes over the authority above;
8. relevant Universal patterns, which govern process but never article facts or wording.

An older draft, summary, review package, helper script, rendered preview, Mermaid map, or remembered conversation cannot outrank a registered current master. If two candidates plausibly claim canonical status, stop for an owner decision; do not merge them by inference.

## Required article family

Each imported article uses `articles/<article-id>/` and must register the following files with lowercase SHA-256 hashes:

| Role | Conventional path | Required contents |
|---|---|---|
| Current master | `master.md` or an owner-approved source format | Exact authoritative prose and structure |
| Owner locks | `OWNER-LOCKS.json` | Exact locked passages with their own hashes; protected rhetorical functions; durable owner-review status/evidence |
| Source/evidence index | `SOURCE-EVIDENCE.json` | Claim/source relationships, access status, uncertainty, and provenance |
| Unincorporated ideas | `UNINCORPORATED-IDEAS.md` | Ideas not in the master and their disposition; never silently reconstructed |
| Article state | `CURRENT-STATE.md` | Goal, authority, completed work, checkpoint, remaining work, blockers, evidence, next safe action |
| Article architecture | `ARCHITECTURE.md` | Living Mermaid overview/drill-downs of section order, protected jobs, important setup/payoff dependencies, owner supersession routing, and real stopping point; register as `additional_artifacts` role `architecture_map` |
| Citation record | `CITATIONS.json` | Exact claim dispositions and link/access results |
| Detector evidence | `DETECTOR-EVIDENCE.json` | Exact passage, model/service/version where known, timestamp, result, and limitations |
| Editorial status | `EDITORIAL-STATUS.json` | Meaning, structure, fidelity, curious-reader, and owner-lock review disposition |
| Publication exports | Article-local files plus registry entries | Exact hash, destination, source authority, and draft/published/superseded status |
| Additional artifacts | Article-local files plus `additional_artifacts` registry entries | Exact hash and nonblank role for every approved supporting asset |

The repository also maintains root `ARTICLE-META-MAP.md`, which must include every registered article and accepted cross-article relationships useful for interlinking, reading paths, or deduplication review. The meta-map is editorially maintained; keyword overlap alone does not create an edge.

The validator enforces structure, file presence, hashes, exact locked-passage presence, protected-function records, owner-review confirmation before owner-final/published status, article-state headings, internal/registry review-status parity, privacy boundaries, a reciprocal incubator/active status, complete article-family inventory, and export provenance. It rejects symlinks—including the canonical registry and reserved article policy—and detached top-level `sources/`, `evidence/`, `experiments/`, or `publish/` families so mutable authority cannot escape its article boundary. `scripts/validate_article_architecture_maps.py` separately enforces the required article-local map, canonical path/marker/plain Mermaid fence, root repository meta-map, and meta-map membership. Human review still owns truth, meaning, whether graph arrows are semantically correct, article-wide architecture, citations, and publication readiness.

## Lossless editing and reversible deletion

- Inventory the master, owner locks, unique claims, examples, jokes, steps, transitions, and protected functions before editing.
- Inspect `ARCHITECTURE.md` before moving or deleting a passage. A cut or relocation is blocked if it would orphan a protected function, setup/payoff dependency, or stopping-point role without an approved destination.
- A cut or consolidation is a proposed transformation, not silent cleanup. Record original text, proposed destination or semantic equivalent, and explicit owner approval when meaning is not exact.
- Keep rejected cuts and unincorporated ideas outside the master but inside the article family, with status and provenance.
- Re-run the article-wide architecture gate after every detector-driven edit. A detector-green candidate still fails if it loses meaning, agency, heading promise, live-question continuity, or a protected function.
- Update `ARCHITECTURE.md` in the same change when detector repair or owner correction materially changes topology/function routing; update root `ARTICLE-META-MAP.md` when cross-article interlink/dedup relationships materially change.
- Update hashes only after the associated semantic and source review passes; never update the registry merely to silence a mismatch.

## Citation and evidence discipline

Evidence attaches to claims, not to convenient paragraphs. Record source identity, exact support, access date/status, conflicts, and local uncertainty. Owner testimony, inaccessible material, disputed claims, and not-applicable citations must remain distinguishable. Unsupported does not mean false, and sourcing difficulty does not authorize flattening Joel's argument.

## Source-format and publication authority

Publication tooling is destination-specific. When an owner-approved protocol names editor/source HTML as authority, verify native objects, editor/source structure, and transfer artifacts separately; a rendered preview alone is not proof. Retest destination assumptions before reuse. No workflow, helper, or export may publish without an explicit owner action and a registered export record.

## First-import procedure

1. Owner identifies one article and its authoritative master.
2. Inventory every candidate and source file without changing prose.
3. Resolve competing-master, privacy, licensing, and publication questions with the owner.
4. Create the complete article family, including `ARCHITECTURE.md` from `templates/ARTICLE-ARCHITECTURE.md`; register every file (including supporting assets) and exact hashes.
5. Add the article's marker/node to root `ARTICLE-META-MAP.md` and add only known, semantically justified cross-article relationships.
6. Set repository status to `active` and add the registry entry.
7. Run repository gates, `scripts/validate_article_architecture_maps.py`, plus article-specific semantic, citation, link, detector, fidelity, and publication checks.
8. Review unique-claim preservation and every deletion/relocation against the article map.
9. Update both current-state layers and merge through a focused pull request.

Until these steps are complete, content import remains **BLOCKED**.
