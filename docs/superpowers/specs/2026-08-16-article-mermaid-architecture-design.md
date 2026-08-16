# Article Mermaid Architecture Design

Date: 2026-08-16

## Goal

Make article placement, protected rhetorical function, cross-section dependencies, owner supersession, and cross-article interlink relationships visually recoverable so a fresh worker does not have to reconstruct topology from prose or chat.

## Repository-wide architecture

`joel-articles` will maintain two related but non-authoritative visual control surfaces:

1. `articles/ARTICLE-META-MAP.md` — one repository-wide Mermaid graph showing every registered article and meaningful article-to-article relationships such as explicit links, shared concepts, likely deduplication collisions, and useful interlink opportunities.
2. `articles/<article-id>/ARCHITECTURE.md` — one canonical article-local Mermaid map showing section order, each section's protected job, important setup/payoff dependencies, owner-final/supersession routing, and unresolved placement questions when they materially affect editing.

The graphs index canonical prose/evidence state; they do not replace it. If a graph conflicts with registered authority, the graph must be repaired.

## Article-local map requirements

Every registered article must inventory exactly one `additional_artifacts` entry with role `architecture_map` and path `articles/<article-id>/ARCHITECTURE.md`.

The file must contain:

- a plain GitHub-compatible ` ```mermaid ` fenced graph with no custom fence attributes;
- an `<!-- article-id: <article-id> -->` marker for deterministic validation;
- section/order nodes at a structural level rather than paragraph-by-paragraph mega-graph detail;
- protected job/function labels for sections whose placement matters;
- dotted or labeled dependency edges for non-linear setup/payoff relationships where useful;
- explicit owner-final/superseded/unresolved labels when topology depends on authority state;
- a short prose note naming the authoritative article state/master the graph indexes.

For long articles, use an overview plus focused drill-down graphs in the same file rather than one unreadable diagram.

## Repository meta-map requirements

`articles/ARTICLE-META-MAP.md` is a reserved physical repository file and is allowed even while the repository remains an empty governance incubator.

For every registered article it must contain exactly one `<!-- article-id: <article-id> -->` marker. The Mermaid graph may then show:

- explicit published/internal article links;
- shared-concept relationships;
- likely duplicate coverage that should be audited;
- source/detail relationships where one article should link to another rather than repeat it;
- deliberate non-links where similar topics must remain distinct.

The map is editorially maintained rather than mechanically inferred because interlink opportunity and duplication are semantic judgments.

## Update contract

Update the article-local map in the same substantive change when section order, protected function placement, owner supersession routing, or a meaningful setup/payoff dependency changes.

Update the repository meta-map in the same change when an article is registered/removed, a durable inter-article link is added/removed, or a new deduplication/interlink relationship becomes editorially important.

Cosmetic prose edits do not require graph churn.

## Validation

The content validator will fail when:

- `articles/ARTICLE-META-MAP.md` is missing or is a symlink;
- the meta-map lacks a plain Mermaid fence;
- a registered article is absent from the meta-map marker set;
- an article has no `architecture_map` artifact, has more than one, or points it anywhere except `articles/<id>/ARCHITECTURE.md`;
- the article architecture file lacks its matching article-id marker or plain Mermaid fence.

The validator does not attempt full Mermaid semantic parsing. Syntax rendering remains a separate optional CI concern; deterministic structural checks prevent the specific unsupported-fence failure seen in chat while avoiding a Mermaid runtime dependency.

## Bootstrap state

Because `joel-articles` currently has no registered article families, the repository meta-map will render a single `No registered articles yet` node and contain no article-id markers.

The live Romance map remains in private `pangram-humanization-lab` assembly work until Romance is formally imported into `joel-articles`. At import time it becomes `articles/romance/ARCHITECTURE.md` and Romance is added to the repository meta-map.

## Privacy and authority

The public `joel-articles` repository must not receive private article prose merely to satisfy the graph requirement. Article-local maps enter only with an owner-authorized article family. Until then, private working maps stay in the private working repository.
