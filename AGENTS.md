# Joel Articles agent map

## Authority

1. Current owner instructions and the article-specific acceptance criteria
2. `articles/INDEX.json` for registered article authority and exact hashes
3. `docs/INDEX.md` and the registered article's current-state read order
4. The registered master, owner-lock manifest, and exact source evidence
5. Exact citation/editorial/detector records and Git history
6. Relevant current patterns from `u-dont-existDOTcom/universal-dev-architecture`

This repository is an incubator until article files and their authority maps are imported. Do not claim it already contains a canonical article.

## Recovery before editing

Read `state/CODEX-CURRENT-STATE.md`, `articles/INDEX.json`, and the target article's registered current state before changing prose. Verify every registered SHA-256 first. If the registry is empty, stop content editing: governance work may continue, but no article master may be inferred from chat, filenames, summaries, or an external packet.

## Validation

- Unit and policy regressions: `python -m unittest discover -s tests`
- Authority, hash, privacy, and export checks: `python scripts/validate_content_repository.py --root .`
- Repository and workflow audit: `python scripts/audit_codex_github.py --root . --fail-on error`
- Patch hygiene: `git diff --check`

The validator proves registered structure and hashes, not article truth or editorial quality. Run the registered article's semantic, source, citation, detector, publication, and lesson-closeout checks in addition.

## Workflow

Use one article-scoped task branch/worktree and a pull request. Keep owner-final prose, reconstruction state, source evidence, detector experiments, and promoted lessons distinguishable. Persist decisions and recovery state in Git before ending a substantive pass.

For humanization/detector work, `docs/HUMANIZATION-ARCHITECTURE-GATE.md` is blocking: re-run the article-wide architecture regression after every detector-driven edit. Do not narrow the editorial field of view to the last detector window.

## Branch roles

- `main`: accepted article governance and canonical state
- task branches: article-specific editorial, research, detector, or reconstruction changes

## Code review rules

- Never silently soften, balance, or change the owner's argument. Disagreement must be raised directly rather than hidden in an edit.
- Preserve every unique claim, step, joke, protected rhetorical function, and owner-final passage unless a proposed cut has explicit owner approval or genuine semantic equivalence.
- Treat deletions and consolidations as explicit proposals. Record the original text and destination or owner approval so the change is reversible; do not silently discard apparently redundant material.
- Owner-lock manifests contain exact protected passages. A passing hash check is necessary but not sufficient: review the master article-wide for function, sequence, agency, and meaning preservation.
- Keep claim-level source provenance local. Mark unsupported, inaccessible, disputed, or owner-only claims precisely; never fabricate a citation or flatten the author's position to make sourcing easier.
- Detector results are evidence, not editorial authority; passing a detector never licenses distortion of meaning or voice.
- A 100% Human detector result is still invalid if heading promise, paragraph jobs, live-question continuity, owner-realization placement, protected functions, or fidelity fail the architecture regression.

Treat chat as disposable working memory. A fresh worker must recover the correct article state, constraints, and next action from Git.

## Stop conditions

Stop and obtain an owner decision before choosing a copyright/license posture, selecting between competing canonical masters, making substantive prose changes without a registered authority package, publishing/exporting, or releasing source material that may contain private personal or health facts. Routine schema, index, state, template, validation, and governance maintenance may proceed when it preserves these boundaries.
