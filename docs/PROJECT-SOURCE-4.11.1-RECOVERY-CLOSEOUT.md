# Project Source recovery closeout — 4.11.1 baseline

Date: 2026-08-17

This closeout supersedes only the **final unresolved-count statement** in
`PROJECT-SOURCE-4.11.1-RECOVERY-AUDIT.md`. The audit remains the historical
record of the Codex recovery run and its original validation evidence.

## Final result

- Owner-supplied historical baseline: **40 exact files**.
- Exact baseline files archived: **40**.
- Baseline files restored active: **31**.
- Baseline files retained archive-only because newer active versions supersede
  them: **9**.
- Current ChatGPT Project source count remains **10**.
- Current article-authority changes: **0**; `articles/INDEX.json` remains
  controlling and empty.
- Final unresolved repository-local Project-source references: **0**.

## Optional-tool gap resolution

The Codex recovery correctly reported one unresolved reference after processing
the exact 40-file owner ZIP: `html_diff.py.txt`. That file was not a member of
the 40-file package.

A prior exact Project Source named `html_diff.py.txt` was subsequently recovered
from Joel's ChatGPT File Library. It is the optional quick static diff tool
explicitly referenced by `TOOLING-IN-PROJECT-SOURCES.md` and the interlinking/
review protocol. It has now been added as:

- active authority: `project-sources/html_diff.py.txt`
- provenance archive: `archive/project-source-snapshots/optional-maintenance/html_diff.py.txt`

It remains optional and may never substitute for the interactive review
interface. Because it was outside the owner-supplied forty-file baseline, its
recovery does not change the `40 / 31 / 9` baseline accounting.

## Baseline validation inherited from the recovery run

Before this optional-tool closeout, Codex recorded these passing gates on the
completed 40-file restoration:

- `python -m unittest discover -s tests` — PASS, 84 tests.
- `python scripts/validate_content_repository.py --root .` — PASS.
- `python scripts/validate_article_architecture_maps.py --root .` — PASS.
- `python scripts/audit_codex_github.py --root . --fail-on error` — PASS with
  0 errors and 4 pre-existing governance warnings.
- `git diff --check` — PASS.
- recovery CLI `--check` — PASS with exact `40 / 31 / 9` counts.
- snapshot `SHA256SUMS.txt` — PASS for the ZIP and all 40 source members.
- all nine newer active successors and `articles/INDEX.json` remained
  byte-identical.
- interactive-review, review-package, and Substack-transfer-helper supported
  self-tests — PASS.

The final recovery PR must run GitHub Actions against the exact post-closeout
head before merge. A green exact-head CI run is the final repository gate.
