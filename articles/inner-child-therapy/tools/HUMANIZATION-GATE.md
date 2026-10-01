# Moved: docs/HUMANIZATION-GATE.md

This lane's humanization gate is now the shared one, `docs/HUMANIZATION-GATE.md` at the repo root (2026-10-01). Every article's humanization runs it, and every chat edits that file, not this one. The rules this copy had through commit `4a4c2e11` are merged into it.

The tools are in `tools/humanization/` (`tools/humanization/README.md`). This article keeps its own reviewer targets (`tools/targets/`), side-by-side maps (`tools/in-context/`) and predictions (`tools/PREDICTIONS.md`).

To read the old copy: `git show 4a4c2e11:articles/inner-child-therapy/tools/HUMANIZATION-GATE.md`.
