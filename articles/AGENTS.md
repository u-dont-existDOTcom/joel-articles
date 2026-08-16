# `articles/` agent instructions

- `INDEX.json` is the only repository-wide article registry. Never add an entry until the owner identifies the authoritative master and the complete artifact family exists.
- `ARTICLE-META-MAP.md` is the repository-wide Mermaid visual index. Every registered article must appear there exactly once via its `<!-- article-id: ... -->` marker, with accepted interlink/dedup relationships updated in the same substantive change.
- Keep every article inside `articles/<article-id>/`; do not share mutable authority files across articles.
- Every registered article must contain `articles/<article-id>/ARCHITECTURE.md`, registered in `additional_artifacts` with role `architecture_map`. Create it from `templates/ARTICLE-ARCHITECTURE.md` and update it whenever section topology, protected-function placement, owner supersession routing, setup/payoff dependencies, or the real stopping point materially change.
- Treat Mermaid maps as visual indexes over authority, never as authority themselves. If a map conflicts with `INDEX.json`, article current state, owner locks, or the master, repair the map.
- Do not create detached top-level source/evidence/experiment/publication families or use symlinks. Every approved supporting file belongs inside one article directory and must appear in that article's `additional_artifacts` inventory.
- Register SHA-256 hashes for the master, owner locks, source/evidence index, unincorporated-ideas ledger, current state, citation record, detector evidence, editorial status, every architecture map, and every export.
- Owner-lock manifests preserve exact passages and protected rhetorical functions, and record a durable owner-review disposition. Never alter or remove a lock or mark review confirmed merely to make a candidate pass validation; obtain an owner decision.
- Treat every deletion, condensation, and relocation as a reversible proposal. Preserve the original text and record its disposition. Before moving/deleting, inspect `ARCHITECTURE.md` and verify every protected function still has a destination.
- Citation records must distinguish verified, inaccessible, disputed, owner-only, unresolved, and not-applicable claims. Never invent a source or erase a claim merely to obtain a clean citation state.
- Detector records are passage-, model-, and run-specific evidence. They do not outrank the master, owner locks, meaning, or article-wide architecture. A detector-red span may indicate wrong routing; inspect the article map before local paraphrase when placement/function could be involved.
- A publication/export record must identify its destination, exact bytes, status, and source authority. Raw editor/source HTML may outrank rendered previews when the registered publication protocol says so.
- If competing masters, missing source files, privacy uncertainty, an orphaned protected function, or an unapproved publication action appears, stop and record the blocker in the article and repository current state.
