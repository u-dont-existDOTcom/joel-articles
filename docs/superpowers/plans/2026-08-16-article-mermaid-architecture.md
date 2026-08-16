# Article Mermaid Architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Require one canonical Mermaid architecture map per registered article plus one repository-wide article meta-map, with fail-closed validation and private Romance bootstrap mapping.

**Architecture:** Keep Mermaid maps as non-authoritative visual indexes over registered prose/evidence. Enforce their presence, canonical location, article-id markers, and plain GitHub-compatible Mermaid fences with a focused architecture-map validator invoked by the existing content-integrity workflow. Keep the repository meta-map at root `ARTICLE-META-MAP.md`; keep Romance's actual map private until formal article import.

**Tech Stack:** Python 3 standard library, unittest, Markdown/Mermaid, existing GitHub Actions content-integrity gate.

## Global Constraints

- Never move private Romance prose into `joel-articles` merely to satisfy mapping.
- Mermaid fences must be plain ` ```mermaid ` with no attributes.
- Maps do not override article authority, owner locks, or current state.
- Per-article map updates are required only for material topology/function/authority-routing changes, not cosmetic wording edits.
- Meta-map relationships are semantic/editorial judgments, not automatically inferred from keywords.

---

### Task 1: Specify map validation behavior

**Files:**
- Create: `tests/test_article_architecture_maps.py`

**Interfaces:**
- Consumes: `validate_architecture_maps(root: Path) -> list[dict[str, str]]`
- Produces: regression expectations for `article.architecture.*` and `index.meta-map.*` findings.

- [x] **Step 1: Write failing tests** for missing/symlinked/invalid root meta-map, missing article membership, missing/canonical-path article architecture map, and article marker/plain Mermaid fence.
- [x] **Step 2: Run CI and verify RED.** Content-integrity run `31946547091`, job `95163349236`, failed in regression tests before implementation.

### Task 2: Implement minimal validator support

**Files:**
- Create: `scripts/validate_article_architecture_maps.py`
- Modify: `.github/workflows/content-integrity.yml`
- Test: `tests/test_article_architecture_maps.py`

**Interfaces:**
- `ARTICLE_META_MAP_PATH = "ARTICLE-META-MAP.md"`
- `ARCHITECTURE_ROLE = "architecture_map"`
- `_has_plain_mermaid_fence(text: str) -> bool`
- `validate_architecture_maps(root: Path) -> list[dict[str, str]]`

- [x] **Step 1: Implement plain-fence detection** using literal `"```mermaid\n"`; no Mermaid runtime dependency.
- [x] **Step 2: Implement per-article validation.** Require exactly one `architecture_map` artifact at `articles/<article-id>/ARCHITECTURE.md`, exact article-id marker, and plain Mermaid fence.
- [x] **Step 3: Implement root meta-map validation.** Require physical root `ARTICLE-META-MAP.md`, plain Mermaid fence, and exactly one marker for every registered article.
- [x] **Step 4: Invoke the validator from `content-integrity.yml`.**
- [x] **Step 5: Verify GREEN for the feature tests.** A post-implementation CI checkpoint passed regression tests before later bootstrap integration exposed the separate incubator-path conflict.

### Task 3: Add governance docs, template, and bootstrap meta-map

**Files:**
- Create: `docs/ARTICLE-ARCHITECTURE-MAPS.md`
- Create: `templates/ARTICLE-ARCHITECTURE.md`
- Create: `ARTICLE-META-MAP.md`
- Modify: `articles/AGENTS.md`
- Modify: `docs/INDEX.md`
- Modify: `docs/CONTENT-AUTHORITY-AND-IMPORT.md`

**Interfaces:**
- `ARTICLE-ARCHITECTURE-MAPS.md` is the normative map protocol.
- `templates/ARTICLE-ARCHITECTURE.md` is the copyable per-article starting point.
- root `ARTICLE-META-MAP.md` is the canonical repository-wide visual map.

- [x] **Step 1: Add the protocol** covering authority limits, update triggers, article-local requirements, meta-map relationships, detector routing, and anti-mega-graph guidance.
- [x] **Step 2: Add a conservative GitHub-renderable template** using `flowchart`, quoted labels, simple arrows, and dotted dependency arrows.
- [x] **Step 3: Add the empty-incubator root meta-map:**

```mermaid
flowchart LR
    empty["No registered articles yet"]
```

- [x] **Step 4: Update article instructions/import protocol/index** so article creation/import creates/registers `ARCHITECTURE.md` and updates root `ARTICLE-META-MAP.md` in the same change.
- [ ] **Step 5: Run final full repository verification on the exact completed head:**

```bash
python -m unittest discover -s tests -v
python scripts/validate_content_repository.py --root .
python scripts/validate_article_architecture_maps.py --root .
python scripts/audit_codex_github.py --root . --fail-on error
```

The first integrated bootstrap attempt placed the meta-map under `articles/`; CI correctly rejected it as unregistered article-family content in the governance incubator. The implementation now keeps the meta-map at repository root instead of weakening the existing content-boundary invariant. Final verification must confirm this exact repaired topology.

### Task 4: Add the current private Romance architecture map

**Repository:** `u-dont-existDOTcom/pangram-humanization-lab`
**Branch:** `agent/romance-architecture-map-2026-08-16`, based on the current Romance assembly branch.

**Files:**
- Create: `work/romance-current-assembly/ARCHITECTURE.md`

- [x] **Step 1: Create an overview graph** showing article order through Tough Love/Bear.
- [x] **Step 2: Add focused dependency/community drill-downs.**
- [x] **Step 3: Record Aug. 16 authority drift** for Psychedelics, `If you're already in it`, Children/Ending placement, Tough Love, and the terminal close.
- [x] **Step 4: Keep this task map-only.** Article bytes are reconciled in the next assembly task.

### Task 5: Close out the Tough Love owner correction

**Repository:** `u-dont-existDOTcom/pangram-humanization-lab`

- [x] **Step 1: Replace `But pathology it festers...` with owner-final `But pathology festers...`.**
- [x] **Step 2: Record Joel's retest:** corrected full section remains fully Human / High confidence; no invented numeric result.
- [x] **Step 3: Preserve exact pre-repair Pangram evidence:** 689 words, 76.2% Human / 23.8% AI, with 98-word and 66-word Fully AI / High confidence windows.
- [x] **Step 4: Preserve the semantic lesson and defer further paid calls until exact full-article reassembly.

### Task 6: Reconcile the Romance assembly against the living map

**Repository:** `u-dont-existDOTcom/pangram-humanization-lab`
**Branch:** continue from `agent/romance-architecture-map-2026-08-16`.

**Files:**
- Modify: `work/romance-current-assembly/assembly-spec.json`
- Create/modify only authoritative replacement files needed for current Psychedelics, `If you're already in it`, Children/Ending placement, Doing-it-consciously boundary, and complete Tough Love.
- Regenerate: `current-master.md`, manifest, diff, reader-visible text/manifest.

- [ ] **Step 1: Recover exact highest-authority text for every stale graph node before changing the assembly spec.** Do not generate missing owner prose.
- [ ] **Step 2: Add failing assembly tests/invariants for each stale node and protected placement.**
- [ ] **Step 3: Update exact replacements/spec and regenerate deterministically.**
- [ ] **Step 4: Run two whole-article cold audits against the architecture map.**
- [ ] **Step 5: Only after coherence/fidelity is clean, submit the exact reader-visible whole-article boundary for final Pangram certification.
