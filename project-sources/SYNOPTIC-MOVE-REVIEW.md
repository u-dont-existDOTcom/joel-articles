# Synoptic Move Review — long-document structural comparison

Status: active companion pattern for substantial article reviews where paragraphs, subsections, or functions moved or consolidated across a long document.

This pattern composes `REVIEW-INTERFACE-SPEC.md`, `REVIEW-WORKFLOW-RULES.md`, the source–meaning–context–destination ledger, and the multiscale editorial ledger. It does not replace the ordinary commentable diff.

## When to use

Use synoptic move review when ordinary line/unified diffs make structural edits hard to understand, especially when:

- a semantic block moved far from its original location;
- several source blocks consolidated into one destination or one source split into several destinations;
- substantial reordering makes aligned row-by-row reading misleading;
- the owner needs to judge the whole article in context while still tracing provenance.

## Display model

Use two spatially separate complete witnesses:

- left pane: the exact selected source/before version;
- right pane: the exact revised/after version;
- narrow relation rail: one stable semantic relation per change/move.

Keep the panes independently scrollable by default. Do not draw giant page-spanning arrows. A relation badge at either endpoint must jump the opposite pane to the paired endpoint and highlight both. Short visible connectors are optional only while both endpoints are simultaneously visible.

For every relation assign one stable `relation_id` and one classification:

- `moved` — substantially the same semantic unit appears elsewhere;
- `moved_and_rewritten` — destination preserves the moved function but wording also changed;
- `consolidated` — several source units feed one destination or one source feeds several destinations;
- `rewritten_in_place`;
- `structurally_removed` — parent architecture changed and unique functions are accounted for elsewhere;
- `owner_correction`;
- `proposal_unapplied` — diagnostic comparison only; not part of the revised article.

Never label a conceptual consolidation as a literal move merely because the topics overlap.

## Alignment order

Do not begin with word highlighting. Use two stages:

1. establish semantic block correspondence and relation classification across the complete article;
2. only inside an established one-to-one moved/rewritten pair, show token/word differences when useful.

The relation ledger is upstream of visualization. The renderer must not infer provenance from visual proximity.

## Shared relation comments

A move/consolidation is one editorial decision even though it has multiple visible endpoints. Therefore every relation has one shared review record accessible from either side.

Required relation-review fields:

- `relation_id`;
- classification;
- source block id(s);
- destination block id(s);
- concise reason / intended function;
- owner comment;
- relation decision;
- timestamped decision/comment history;
- exact source/revised file identities and hashes.

Recommended relation decisions for this mode:

- `keep_revised` — keep the revised placement/realization;
- `restore_source` — undo this move/change and restore the prior realization/placement;
- `brainstorm` — neither side accepted; produce alternatives;
- empty/no decision.

Opening the comment from `Moved From` or `Moved To` must load the same record. Do not create duplicate comments for the two ends of one move. For one-to-many or many-to-one consolidations, all endpoints share the same relation record unless the owner explicitly splits the issue.

Cell/selected-text comments remain available for wording-specific notes and are distinct from relation-level comments. A relation comment answers `Was this structural change right?`; a selected-text comment answers `What about these exact words?`.

## Persistence and export

Persist relation reviews locally when the review is a standalone HTML artifact. Export at least JSON and preferably Markdown.

The JSON export must preserve:

- artifact/review format version;
- exact source/revised filenames and SHA-256 values;
- relation catalog;
- relation comments and decisions;
- decision/comment history;
- any selected-text/cell comments if the host review interface provides them.

Imported review JSON must refuse or visibly warn on source/revised hash mismatch.

## Review ergonomics

For long articles:

- keep both complete article panes available;
- provide a relation/change index or minimap;
- allow filtering to reviewed/unreviewed relations and unapplied proposals;
- search both versions;
- on relation selection, scroll both panes to the relevant source/destination rather than synchronizing by percentage;
- do not force moved text into the same vertical row when the move is long-distance;
- do not inject faded duplicate prose into the revised article as the primary display model.

## Validation

Test the exact packaged review for:

- source→destination and destination→source jump;
- shared relation comment opened from either endpoint;
- save, reopen, edit, clear;
- decision state;
- timestamped history;
- reload persistence when local-file browser behavior is available;
- JSON/Markdown export and JSON parse;
- import with correct hashes and rejection/warning on wrong hashes;
- relation filtering/search;
- no console/page errors.

When local-file or loopback navigation is blocked by the execution environment, test behavior with `page.set_content` and state the limitation. That proves interface logic, not local-file persistence in the owner’s browser.

## Provenance

Promoted after the 2026-08-27 Romance dedup review. A first attempt embedded faded old passages and long arrows inside one revised article. The owner found it hard to use. Existing-work review showed that established collation/diff practice and the repository’s own review specification favor separate witnesses, semantic alignment, destination jumps, and explicit moved/consolidated classifications. The follow-up owner request added relation-level comments shared across both endpoints of each move/change.