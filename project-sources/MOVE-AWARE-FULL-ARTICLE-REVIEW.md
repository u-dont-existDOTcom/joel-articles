# Move-Aware Full-Article Review

Status: reusable extension of the existing article review interface for revisions where paragraph/section movement or consolidation is hard to understand in a conventional diff.

Use this with `REVIEW-INTERFACE-SPEC.md`, `REVIEW-WORKFLOW-RULES.md`, and the ordinary source–meaning–context–destination and artifact-family controls. It does not replace the standard side-by-side commentable review when that artifact is required.

## Purpose

A unified or side-by-side diff can make moved prose look like unrelated deletion plus insertion. For a long article, that forces the reviewer to rediscover where material went. When movement/consolidation is a material part of the edit, provide a **whole-article move-aware view** in addition to the ordinary comparison artifact.

## Required presentation

The primary reading column is the **complete current article in natural reading order**, not a changed-passages summary.

For every consequential moved or consolidated source unit:

- leave a faded/lightened **ghost** of the prior text at its old location;
- place a matching stable marker/circle on the destination text;
- make the old marker jump to the new location and the new marker jump back to the old location;
- where practical on desktop, draw a visible gutter arrow old → new;
- if one source unit consolidates into several destinations, expose all destinations rather than pretending it was a one-to-one move;
- keep the current text visually primary and make the ghost unmistakably historical/non-current.

Arrows are supplemental. Bidirectional click navigation is required even when arrows are hidden on mobile or unavailable in print.

## Semantic classifications

Do not present every deletion/addition pair as a move. Distinguish at least:

- `Moved` — substantially the same unit changed location;
- `Consolidated` — unique functions from the old unit were redistributed or merged into one or more destinations;
- `Rewrite in place` — the location/function stayed but the realization changed;
- `Owner correction` — current owner instruction superseded the prior candidate;
- `Proposal / not applied` — a review idea only; it must be visually distinct from current prose and from completed movement.

A consolidation arrow shows functional provenance, not verbatim text identity. Label it accordingly.

## Lower-confidence proposals

When the reviewer needs to judge uncertain structural cuts/moves in context, keep the current article unchanged and overlay the proposal separately:

- use a distinct visual treatment from applied edits;
- mark it `NOT APPLIED` or equivalent;
- connect the candidate source to the proposed primary home/comparison location;
- show the proposed replacement/cut in a collapsible note where useful;
- never make a proposal look owner-approved merely because it appears in the full-article view.

## Native objects

Native images, videos, previews, buttons, paywalls, and other editor objects remain atomic semantic units. A prose-only export may omit the object while retaining its textual anchor. Before diagnosing a colon, blank line, setup, or transition as orphaned, check the authoritative raw editor/native-object source.

When the move-aware view is generated from prose-only material and an authoritative native object is known to occupy that location, show a typed placeholder such as `[video embed]` rather than inventing prose or treating the anchor as incomplete.

## Navigation and usability

Provide:

- a compact legend for movement/consolidation/rewrite/owner/proposal states;
- toggles to hide/show old ghosts, arrows, and unapplied proposals when useful;
- a move/proposal index for long articles;
- normal article heading navigation;
- visible focus/flash feedback after a jump so the destination is easy to locate.

The article must remain readable with all annotations visible. Avoid placing movement controls over the prose itself.

## Validation

Before delivery:

1. verify every marker/target ID is unique;
2. verify every old → new and new → old target resolves;
3. verify multi-destination consolidations expose every intended target;
4. verify ghost blocks are historical only and do not become part of the candidate article text/export;
5. verify proposal overlays are explicitly unapplied;
6. verify native-object placeholders against authoritative source when available;
7. test click navigation and toggles in a browser when the environment permits it;
8. if local-file or loopback browser automation is blocked, record that limitation and do not claim interaction-tested status merely from static validation.

## Delivery

For a long article, deliver the HTML as a file/ZIP rather than rendering it inline in chat. Include the current candidate/source identity and a short README explaining the legend and validation status.

## Provenance

Promoted after the 2026-08-27 Romance dedup review. A conventional unified diff made moved prose difficult to distinguish from deletion/insertion, and a summary-only visual review did not let Joel judge the changes in the full article context. Joel requested the complete article with old locations faded, arrows showing provenance, and bidirectional old ↔ new click navigation. This pattern preserves that requirement for future structural reviews.
