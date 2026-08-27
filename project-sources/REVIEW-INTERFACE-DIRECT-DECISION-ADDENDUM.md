# Review Interface Direct-Decision and Context Addendum

Status: **ACTIVE owner correction** to `REVIEW-INTERFACE-SPEC.md` for substantial Joel-byline review artifacts. Where this addendum conflicts with older modal-first decision behavior, this addendum controls.

Promoted: 2026-08-27 after Romance move/dedup review on Android exposed avoidable friction and ambiguity.

## 1. Approval is a first-class inline action

A reviewer must not have to open a comment/reasoning modal to make the routine accept/non-accept decision.

Every substantive review relation/card must expose, directly on the card:

- a visible red **`Not approved yet`** state, which is the default for every new relation;
- a visible green **`Approve`** action;
- a separate comment action.

`Not approved yet` means pending/non-accepted, **not an affirmative rejection**. Only an explicit approval counts as approved. A reviewer may return an approved item to `Not approved yet` without opening a modal.

For an already-applied candidate change, `Approve` means keep that candidate change. For an unapplied proposal, `Approve` means authorize applying that proposal. The interface must make that distinction visible so `Keep R5` cannot ambiguously mean either accepting or rejecting an unapplied proposal.

Preserve a separate `touched/reviewed` signal when needed so a default red pending state is not mistaken for an explicit owner rejection.

## 2. Comments are optional and relation-scoped

Comments are secondary to the direct decision controls.

For moved, consolidated, or otherwise multi-location changes, the comment/decision belongs to the **semantic relation**, not independently to each endpoint. Opening the comment from either endpoint must return the same shared record.

Preserve comment history, decision history, timestamps, source/revised identities, and exact relation id in export. Existing review JSON must be migratable without requiring Joel to redo completed decisions or comments.

## 3. Context navigation must preserve review position

`See context` must never throw the reviewer into a full article view and then return them to the top/all-items display.

Use an overlay, drawer, or equivalent reversible context view that:

- leaves the underlying review item/scroll position intact;
- names the active relation id in the context header;
- provides an explicit `Back to <relation id>` control;
- on close/back returns to the exact review item;
- allows switching between original/before context and revised/current context without losing the review item;
- highlights the relation's actual source/destination block(s) inside a small amount of surrounding prose.

Long-distance moves should use jump/context navigation rather than giant page-spanning connector lines.

## 4. Explanations must describe the operation, not merely its rationale

Each substantive review card must answer four distinct questions in plain language:

1. **WHAT CHANGED** — literal operation: what sentence/paragraph/function was removed, inserted, moved, rewritten, consolidated, or renamed.
2. **WHY I PROPOSED IT** — editorial rationale.
3. **WHAT STAYS / WHERE** — unique claims, examples, functions, links, or qualifications that survive and their destination when relevant.
4. **WHAT YOU'RE DECIDING** — one concrete approval question.

A vague instruction such as `shorten the community explanation` or `reduce repetition` is insufficient. For a proposed wording change, show the exact proposed replacement or exact cut boundary. For a move, show both the source-site deletion and destination-site insertion. For a consolidation, explicitly state when no literal word-for-word move exists.

## 5. Show lexical change inside the structural relation

Structural classification and word-level diff are separate layers and both are required when wording changed.

- ordinary rewrite: before/after paragraph with removed words and added words visibly marked;
- moved + edited: two local diffs, one at the old location and one at the new location;
- consolidation: source units + destination result, with clear statement that this is many-to-one rather than a literal move;
- heading-only normalization: classify separately and hide by default when it would distract from substantive review;
- lower-confidence proposal: label `UNAPPLIED` and keep it visually distinct from candidate changes already present in the revised article.

## 6. Sequential review

For long review sets, provide Previous/Next or Previous/Next Unapproved navigation so the owner can review methodically without repeatedly returning to an index.

The approval count must reflect explicit green approvals only.

## 7. Mobile readability

On narrow screens:

- preserve ordinary article paragraph spacing and generous line height;
- stack before/after lexical diff cells vertically if side-by-side would become cramped;
- keep direct approval and non-approval controls visible without opening another panel;
- context/back controls must remain sticky/obvious;
- do not compress complete article paragraphs into dense diff-document blocks merely to fit more material on screen.

## 8. Required regression tests added by this correction

In addition to the base review-interface tests, verify:

- every new relation begins `Not approved yet` unless a migrated explicit approval exists;
- approval is one click/tap and does **not** open a comment modal;
- toggling back to not-approved is one click/tap;
- approval progress counts explicit approvals only;
- an existing relation-scoped comment survives migration/reload;
- context opens without changing the review-list position;
- `Back to <relation id>` returns to the exact card;
- before/current context switching works inside the context view;
- vague proposals are rejected by the artifact generator/review authoring process until exact operation/replacement is supplied;
- lower-confidence unapplied proposals cannot be mistaken for already-applied candidate changes.

## Provenance / triggering findings

Romance v2 review feedback showed three concrete failures:

- basic approval required opening the comment/decision window;
- leaving a review item for article context lost the reviewer's place;
- at least one proposal (`P3`, Gaslighting/community witness compression) did not state the actual proposed wording clearly enough to evaluate.

The same review also showed why `what survives` is mandatory: on `E18`, a dedup explanation treated the removed outside-help/community sentence as generic support material, while Joel identified a unique function in it — relying on friends for intimate relationship help is itself part of **creating community**, not merely receiving help from an already-existing community.
