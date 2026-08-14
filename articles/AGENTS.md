# `articles/` agent instructions

- `INDEX.json` is the only repository-wide article registry. Never add an entry until the owner identifies the authoritative master and the complete artifact family exists.
- Keep every article inside `articles/<article-id>/`; do not share mutable authority files across articles.
- Do not create detached top-level source/evidence/experiment/publication families or use symlinks. Every approved supporting file belongs inside one article directory and must appear in that article's `additional_artifacts` inventory.
- Register SHA-256 hashes for the master, owner locks, source/evidence index, unincorporated-ideas ledger, current state, citation record, detector evidence, editorial status, and every export.
- Owner-lock manifests preserve exact passages and protected rhetorical functions, and record a durable owner-review disposition. Never alter or remove a lock or mark review confirmed merely to make a candidate pass validation; obtain an owner decision.
- Treat every deletion, condensation, and relocation as a reversible proposal. Preserve the original text and record its disposition.
- Citation records must distinguish verified, inaccessible, disputed, owner-only, unresolved, and not-applicable claims. Never invent a source or erase a claim merely to obtain a clean citation state.
- Detector records are passage-, model-, and run-specific evidence. They do not outrank the master, owner locks, meaning, or article-wide architecture.
- A publication/export record must identify its destination, exact bytes, status, and source authority. Raw editor/source HTML may outrank rendered previews when the registered publication protocol says so.
- If competing masters, missing source files, privacy uncertainty, or an unapproved publication action appears, stop and record the blocker in the article and repository current state.
