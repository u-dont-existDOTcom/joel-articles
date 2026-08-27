# Move-Aware Inline Diff Review Gate

Status: required when a substantial article review includes moved, consolidated, or materially rewritten prose.

## Why this exists

A side-by-side source/revision view is not enough by itself. In a long article, a relation badge can say that two passages correspond while still leaving the reviewer unable to understand **how** one became the other. Mobile stacking can make this worse because the source and destination may be separated by many screens.

The review therefore needs two levels at once: readable whole-article context and a paired local change explanation.

## 1. Ordinary rewrites: align the block, then show the word diff

For an aligned paragraph, heading, list item, or other semantic block, show the source and revised versions together and mark the exact lexical delta inside the block:

- removed words/phrases visibly deleted;
- added words/phrases visibly inserted;
- unchanged language left visually quiet;
- paragraph boundaries preserved.

Do not make the reviewer infer a paragraph rewrite from two large unmarked text blocks.

## 2. Moves: show two local diffs

A real move is a relation between **two editing sites**, not merely between two passages.

For `Moved` or `Moved + edited`, show:

1. **old location** — the local before/after diff showing what disappeared there;
2. **new location** — the local before/after diff showing what appeared there;
3. one stable move/relation ID shared by both sites;
4. explicit `old context` and `new context` navigation;
5. one shared comment/decision record for the move relation.

If the moved text was edited at the destination, the second local diff must show those edits. Do not draw a giant page-spanning arrow and call that sufficient explanation.

## 3. Consolidations are not automatically moves

When source material is removed because its function already exists elsewhere, do **not** fake a word-for-word moved-text mapping.

Label the relation `Consolidated` and state whether:

- text was literally moved into one destination;
- several source passages were merged into one new passage;
- one source passage was distributed across several destinations; or
- the wording was deleted because the unique function was already present elsewhere.

Show the relevant destination context(s), but only run word-level source→destination diff when a genuine textual correspondence exists.

## 4. Whole-article readability

The review artifact must remain readable as an article, not only as a diff data structure.

- Preserve semantic paragraph breaks even when a Markdown source uses single newlines rather than blank-line paragraph separators.
- Do not let a Markdown renderer collapse several authorial paragraphs into one giant visual block.
- Use comfortable reading line height and visible paragraph spacing.
- On narrow/mobile screens, prefer a normal one-column article-reading mode plus a separate change-review mode over two full documents stacked into small fixed-height panes.
- The reviewer must be able to switch to the full source article and full revised article at any time.

## 5. Change review mode

For long articles, provide a dedicated sequential change-review view. Each change card should contain:

- relation/change ID;
- semantic classification;
- concise explanation of the operation;
- exact before/after block with inline word diff when applicable;
- source/destination context navigation;
- comment and decision controls;
- distinction between applied changes and unapplied/lower-confidence proposals.

Heading-level normalization and other low-stakes structural fixes may be hidden by default behind a filter so substantive edits remain easy to review.

## 6. Relation-level comments

Comments on a move or consolidation attach to the **relation**, not independently to the source and destination cells. Opening the relation from either end must load the same comment, decision, and history.

Exports must preserve the stable relation ID, classification, source/destination IDs, comment, decision, and decision history so a later worker can apply the review without guessing which side the owner meant.

## 7. Validation

For the exact delivered HTML when practical, test at minimum:

- mobile-sized readable article view;
- paragraph separation and line height;
- ordinary inline rewrite diff;
- moved-text two-site explanation;
- source/destination navigation;
- relation comment create/reopen/edit;
- decision persistence within the running page and normal local persistence when the browser scheme permits it;
- JSON/Markdown export;
- filters for structural fixes and unapplied proposals;
- no page/console errors.

If `file://` or another local scheme is blocked in automation, use `page.set_content` to test interaction behavior and state the local-scheme limitation separately.

## Provenance

Promoted 2026-08-27 after Romance review feedback showed two concrete failures: a synoptic source/revision interface marked C1 as related but did not make the move understandable, and the prose renderer collapsed source single-newline paragraph boundaries into visually dense blocks. The corrected Romance review demonstrates the required pattern: a normal readable R5 view plus change cards with lexical diffs; C1 is represented as one move through two local diffs, one at the source location and one at the destination.
