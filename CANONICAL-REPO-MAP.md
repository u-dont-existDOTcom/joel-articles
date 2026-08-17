# Canonical repository map

This file is the fast loader for ChatGPT and other workers. It does not replace `articles/INDEX.json`, `AGENTS.md`, or article-local authority.

## Current repository status

- Repository: `u-dont-existDOTcom/joel-articles`
- Default branch: `main`
- Current content posture: governance + editorial skill/tooling home.
- Article authority: **none unless registered in `articles/INDEX.json`.** An empty registry means no article master is canonical here yet.

## Always read for substantial work

1. `SKILL.md`
2. `AGENTS.md`
3. `docs/INDEX.md`
4. `state/CODEX-CURRENT-STATE.md`
5. `articles/INDEX.json`
6. the target article's registered current state/master/locks/evidence if and only if the registry contains that article

## Task-specific active sources

### Recurring facts, naming, and links
- `project-sources/CANON-FACTS.md`
- the registered/current article index when one exists

### Research-heavy or contested argument work
- `project-sources/ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md`
- `project-sources/ARGUMENT-LEDGER-QUICKSTART.md` when threshold-triggered

### Artifact families and review packages
- `project-sources/ARTIFACT-FAMILY-LEDGER-TEMPLATE.md`
- `project-sources/review_package.py.txt`

### Existing Substack article source/publishing
- `project-sources/INTERLINKING-AND-HTML-SOURCE.md`
- `project-sources/CONFIRMED-SUBSTACK-HELPER.json`
- `project-sources/html_islands.py.txt`
- `project-sources/substack_transfer_helper.py.txt`
- video regression tests under `tests/`

### Humanization/detector work
Read the relevant current repo governance plus the private detector repository:
- `u-dont-existDOTcom/pangram-humanization-lab/README.md`
- `state/WORKING-LESSONS.md`
- relevant case study
- newest relevant case/history

## Article-local authority once imported

`articles/INDEX.json` is the only repository-wide article registry. For a registered article, follow `docs/CONTENT-AUTHORITY-AND-IMPORT.md` and that article's current-state read order. Article-local authority, exact hashes, owner locks, evidence, architecture map, detector records, and publication provenance outrank generic skill files.

## Historical Project retirement archive

The exact pre-cutover ChatGPT Project instruction block, exact ten Project Source files, source hashes, local migration ledger, and owner-final native-video correction are preserved under:

`archive/chatgpt-project-retirement-2026-08-17/`

Those files are historical evidence only. Active work uses the root skill/map and current `project-sources/` files.

## Conflict rules

- Joel's current direct correction beats repository text and must then be made durable.
- Registered article authority beats generic project protocols on article-specific state/content.
- Current `project-sources/` beats archived Project copies.
- Repository governance beats remembered chat/process assumptions.
- Pangram output never outranks article meaning, owner authority, or architecture.
- If two plausible article masters compete and the registry does not resolve them, stop for an owner decision instead of merging by inference.
