# Joel Articles

Durable, loss-resistant home for Joel Rosenblum's article-specific canonical state, sources, owner decisions, review evidence, publication provenance, and lessons.

## Current status

**BLOCKED governance incubator.** No article is canonical here. The repository contains governance and validation only; it does not contain an imported master, owner-final decision set, source package, citation record, detector record, or per-article recovery checkpoint.

The public repository also has no owner-selected license or copyright notice. Public visibility does not imply permission to reuse the contents. The owner decision and remaining hosted controls are tracked in [GitHub issue #3](https://github.com/u-dont-existDOTcom/joel-articles/issues/3).

## Authority map

- `articles/INDEX.json` — only registry allowed to declare an article package
- `docs/CONTENT-AUTHORITY-AND-IMPORT.md` — required package and read order
- `docs/SUPPLIED-SOURCE-PACKET-MANIFEST.md` — hashes and disposition of the external packet; no packet contents are published here
- `state/CODEX-CURRENT-STATE.md` — single repository recovery checkpoint
- `docs/HUMANIZATION-ARCHITECTURE-GATE.md` — blocking article-wide regression for detector-driven editing

## Exact checks

```sh
python -m unittest discover -s tests
python scripts/validate_content_repository.py --root .
python scripts/audit_codex_github.py --root . --fail-on error
git diff --check
```

Passing these checks validates repository structure and recorded hashes. It does not make an article accurate, owner-final, publishable, detector-approved, or licensed.
