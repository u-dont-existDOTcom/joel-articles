# Comment Resolution Ledger Template

Preserve the user’s raw comments unchanged in `review/source-comments.json`. Use this ledger to interpret, reconcile, and resolve them. Every source comment receives a stable issue ID even when it is later retracted or superseded.

## Review metadata

- **Project ID:**
- **Current candidate revision:**
- **Last approved baseline filename:**
- **Last approved baseline SHA-256:**
- **Raw comments filename:**
- **Raw comments SHA-256:**
- **Raw comment count:**
- **Ledger updated UTC:**

## Status counts

- **Implemented:**
- **Partially implemented:**
- **Needs clarification:**
- **Not implemented with reason:**
- **Superseded/retracted:**
- **Open issues accepted by Joel:**

A delivery is not complete while an issue remains unresolved unless Joel explicitly accepts the open issue and the project state records that acceptance.

## Issue ledger

| Issue ID | Source order/time | Row/side/quote or target passage | Requested correction | Classification | Underlying judgment | Dependencies and required context | Resolution status | Exact revised location | Adjacent-transition/orphan audit | Supersedes / superseded by | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CMT-001 |  |  |  | factual / structural / voice / terminology / citation / link / humor / safety / interface |  |  | implemented / partially implemented / needs clarification / not implemented / superseded |  | pass / repair needed |  |  |

## Reconciliation rules

1. Order comments and decisions chronologically. Later corrections, retractions, and `never mind` instructions control while the prior item remains in history.
2. Preserve the quoted target, row ID, side, selected-text offsets, and text hash when available.
3. Treat each comment as evidence of a judgment, not automatically as a literal replacement.
4. A nearby edit does not resolve a comment unless the exact issue and its dependencies were addressed.
5. After every insertion, deletion, or move, inspect the paragraph before and after it for broken transitions, orphaned pronouns, duplicated setup, displaced definitions, media-anchor damage, and conclusions that no longer follow.
6. Classify every changed unit as Rewritten, Moved, Consolidated, Structurally removed, Owner-deleted, or Preserved. Record movement and consolidation destinations.
7. Keep evidence disputes outside article prose until substantive authority is granted.
8. Reconcile terminology, links, and style rules globally rather than only in the annotated paragraph.
