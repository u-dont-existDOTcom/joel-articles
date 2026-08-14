# Joel Articles agent map

## Authority

1. Current owner instructions and the article-specific acceptance criteria
2. `docs/INDEX.md` for the current article, source, lesson, and detector read order
3. The article's owner-final/master file and its project-local state/lesson index
4. Exact source evidence, detector records, and Git history
5. Relevant current patterns from `u-dont-existDOTcom/universal-dev-architecture`

This repository is an incubator until article files and their authority maps are imported. Do not claim it already contains a canonical article.

## Validation

Until article-specific gates exist:

- Patch hygiene: `git diff --check`
- Verify all referenced files exist
- Run the article project's established semantic, source, detector, and lesson-closeout gates before promotion

Add deterministic checks with the first substantive article import; do not invent empty CI theater.

## Workflow

Use one article-scoped task branch/worktree and a pull request. Keep owner-final prose, reconstruction state, source evidence, detector experiments, and promoted lessons distinguishable. Persist decisions and recovery state in Git before ending a substantive pass.

## Branch roles

- `main`: accepted article governance and canonical state
- task branches: article-specific editorial, research, detector, or reconstruction changes

## Code review rules

- Never silently soften, balance, or change the owner's argument. Disagreement must be raised directly rather than hidden in an edit.
- Preserve every unique claim, step, joke, protected rhetorical function, and owner-final passage unless a proposed cut has explicit owner approval or genuine semantic equivalence.
- Detector results are evidence, not editorial authority; passing a detector never licenses distortion of meaning or voice.

Treat chat as disposable working memory. A fresh worker must recover the correct article state, constraints, and next action from Git.
