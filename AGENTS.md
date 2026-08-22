# Joel Articles agent map

## Authority

1. Current owner instructions and the article-specific acceptance criteria
2. `articles/INDEX.json` for registered article authority and exact hashes
3. `docs/INDEX.md` and the registered article's current-state read order
4. The registered master, owner-lock manifest, and exact source evidence
5. Exact citation/editorial/detector records and Git history
6. Relevant current patterns from `u-dont-existDOTcom/universal-dev-architecture`

This repository is active and currently registers Romance as a working canonical article. Do not substitute historical Romance branches, chat reconstruction, detached packets, or filenames for its registered article family.

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

For P2S/P3/P4 humanization, D3/D4 reconstruction, or detector-driven semantic edits, `docs/HUMANIZATION-PRESERVATION-GATE.md` is blocking **before detector submission**. Freeze the authoritative changed scope, enumerate preservation units and the authorized-change whitelist before drafting, then require bidirectional source↔candidate traceability with **zero unexplained substantive deltas**. Re-run that proof after every detector-driven semantic edit. A detector-green candidate that fails preservation is fidelity-rejected and cannot be promoted.

For humanization/detector work, `docs/HUMANIZATION-ARCHITECTURE-GATE.md` is also blocking: re-run the article-wide architecture regression after every detector-driven edit. Do not narrow the editorial field of view to the last detector window.

Use `docs/EDITORIAL-SCOPE-AND-PLACEMENT.md` when deciding where protected invitation/de-escalation language belongs or when an owner-approved AI/synthetic draft carries useful thought architecture. Protected function and correct placement are separate judgments.

## Branch roles

- `main`: accepted article governance and canonical state
- task branches: article-specific editorial, research, detector, or reconstruction changes

## Code review rules

- Never silently soften, balance, or change the owner's argument. Disagreement must be raised directly rather than hidden in an edit.
- Preserve every unique claim, step, joke, protected rhetorical function, and owner-final passage unless a proposed cut has explicit owner approval or genuine semantic equivalence.
- Treat deletions and consolidations as explicit proposals. Record the original text and destination or owner approval so the change is reversible; do not silently discard apparently redundant material.
- For substantial rewrites, every protected source unit must have a candidate mapping or an already-authorized non-preservation disposition, and every substantive candidate delta must map back to the change whitelist or owner authority. `Inferable`, `redundant`, `smoother`, and `better for Pangram` are never sufficient deletion authority.
- Owner-lock manifests contain exact protected passages. A passing hash check is necessary but not sufficient: review the master article-wide for function, sequence, agency, and meaning preservation.
- Keep claim-level source provenance local. Mark unsupported, inaccessible, disputed, or owner-only claims precisely; never fabricate a citation or flatten the author's position to make sourcing easier.
- During a requested editing or humanization pass, do not turn the task into unsolicited fact-checking or claim review. Research/verify when Joel asks, or flag a claim only when there is a concrete material reason under the article protocol; empirical or contestable language alone is not such a reason.
- Detector results are evidence, not editorial authority; passing a detector never licenses distortion of meaning or voice.
- A 100% Human detector result is still invalid if preservation proof, heading promise, paragraph jobs, live-question continuity, owner-realization placement, protected functions, or fidelity fail.

Treat chat as disposable working memory. A fresh worker must recover the correct article state, constraints, and next action from Git.

## Stop conditions

Stop and obtain an owner decision before choosing a copyright/license posture, selecting between competing canonical masters, making substantive prose changes without a registered authority package, publishing/exporting, or releasing source material that may contain private personal or health facts. Routine schema, index, state, template, validation, and governance maintenance may proceed when it preserves these boundaries.
