# Article Review Interface Specification

## Implementation and non-regression

The working implementation is `interactive_review.py` plus `review_interface_template.html`. This pair was reconstructed from the exact previously working Somatic Article interface supplied by Joel. For a substantial revision, the implementation—not a static diff—is mandatory. Preserve the interface as a locked derivative artifact: side-by-side desktop and stacked mobile layout, one semantic block per cell, selected-text and whole-cell comments, Keep/Remove/Brainstorm, reasoning, Humor/Technical detail/Length/Bluntness sliders on a dedicated second line below the compact ID/action row, Copy JSON, Copy Markdown, JSON/Markdown file export, local persistence, search, and changed-only filtering. The export/interface contract remains `joel-commentable-diff-review-v4`-compatible unless Joel explicitly approves a migration. `html_diff.py` is a separate optional quick-diff tool. Never overwrite an interactive review with its output.

## Layout

- Side-by-side desktop layout: source/original on the left, revised/corrected on the right.
- Responsive stacked layout on narrow screens.
- One semantic block per cell: one heading, paragraph, list item, blockquote, caption, embed, or native control.
- Section labels remain visible only while at least one row in that section is visible.
- Support changed-only filtering and text search.
- For large articles, generate a changed-passages-only row set with `--changed-passages-only` after full semantic alignment. Preserve exact source/revised file hashes and baseline type; row scope is separate metadata. Do not remove interface functions to reduce load.
- Preserve ordinary reading typography in full-article views: paragraph boundaries must remain visually obvious, line height must be comfortable on mobile, and comparison UI must not collapse source paragraphs into dense prose blocks.

## Audience contract

The review artifact records the project-level audience contract:

- primary reader role/identity;
- expected knowledge level;
- relationship to the writer/subject;
- intended reader action or decision;
- stakes and publication venue;
- register and technical-vocabulary allowance;
- explicitly excluded audiences;
- deliberate section-level audience shifts.

A compact status control shows `Audience: stable`, `Audience: deliberate shift`, or `Audience drift`. Changed-only review may also filter by drift type: role, expertise, goal, relationship, scope, action, register, assumed knowledge, stakes, or venue.

## Cell header

Use two lines so controls remain legible:

1. `Original · r0123` or `Revised · r0123`, relation status when present, then direct decision controls, `?`, and `＋`.
2. `Humor`, `Technical detail`, `Length`, and `Bluntness` sliders.

The slider line may wrap responsively; it must never be horizontally clipped or hidden behind an overflow container.

## Native objects

Represent objects semantically and atomically:

- `[image]`
- `[video embed]`
- `[post preview]`
- `[share button]`
- `[subscribe widget]`
- `[comment card]`
- `[paywall marker]`
- `[unknown native object]`

Never display editor overlay text such as “Double click to interact with video” as article prose.

## Comments

- One editable primary comment per cell or semantic change relation.
- For moved/consolidated material, both source and destination must open the same shared relation comment record rather than creating duplicate side-specific comments.
- Reopening `+` loads the existing note rather than creating a duplicate.
- Selected-text comments preserve the exact quote and character offsets. Snapshot the selection on selection change, mouse/touch release, and the `＋` button's pointer-down event so clicking the control cannot erase the highlighted phrase.
- Whole-cell comments preserve row ID, side, semantic block type, and current text hash.
- Enter submits; Shift+Enter inserts a newline; Escape cancels without saving.
- Local persistence is required.

## Decisions

Routine decisions must be direct controls on the change itself; do not require opening a comment/reasoning modal merely to approve or reject a change.

Distinguish at least these states when the review task uses approval semantics:

- **Pending / not reviewed** — the default; visually red or otherwise clearly unapproved, but not equivalent to an explicit rejection.
- **Approved** — explicit green acceptance of the current proposed change.
- **Rejected / keep current** — explicit reviewed rejection; visually distinct from untouched pending state.
- **Needs revision / clarification** — reviewed but unresolved; use for comments such as `modify`, `brainstorm`, or an explicit statement that the proposal itself is unclear.

For the legacy Keep/Remove/Brainstorm contract:

- **Keep:** lock the current passage against casual later rewriting.
- **Remove:** authorize removal subject to dependency and orphan repair.
- **Brainstorm:** request alternatives without changing or approving the authoritative article.

A later decision supersedes an earlier one while retaining timestamped history in exports.

### Review-state migration is mandatory

Regenerating, repairing, or upgrading a review interface must not reset work the owner already completed.

When a prior review export exists for the same source/revision identities, or a deterministic relation-ID migration exists:

- import prior comments, decisions, and history;
- map prior explicit decisions into the new status model;
- mark those relations reviewed/resolved as appropriate;
- preserve `modify`, `brainstorm`, or comment-only records as unresolved review states rather than erasing them;
- exclude already resolved items from `next unresolved` / `unreviewed only` navigation;
- never force Joel to re-approve unchanged review relations merely because the UI was regenerated.

If relation identities changed, provide an explicit migration map or leave the old record unresolved with a warning; do not silently attach it to a guessed new relation.

## Reasoning panel and decision clarity

A review explanation must make the actual operation independently understandable. Do not rely on a generic rationale such as `reduce duplication` when the user still has to infer what will be deleted, retained, moved, or rewritten.

For substantive changes, show as applicable:

1. **Proposed operation** — e.g. `MOVE + REWRITE`, `DELETE`, `COMPRESS 4→1`, `RENAME HEADING`, `REWRITE ONE PARAGRAPH`.
2. **What changed** — the concrete source span and destination/replacement.
3. **Why it was proposed** — the editorial diagnosis, kept separate from the operation.
4. **What stays / where unique material goes** — especially for consolidation and deletion.
5. **What the owner is deciding** — the exact choice between current and proposed states.
6. **Exact replacement prose** when the proposal is a wording rewrite; `shorten this` or `refer back to X` is insufficient.

The `?` panel may additionally show:

- change classification;
- source/origin of the change;
- controlling instruction or owner judgment;
- claim/certainty impact;
- movement or consolidation destination;
- known uncertainty;
- intended audience before and after the change;
- any deliberate audience shift or suspected drift type.

## Change classifications

- Rewritten
- Moved → jump to destination
- Moved + edited → show both the source-location deletion and destination-location insertion/rewrite
- Consolidated → show source unit(s), destination(s), and retained unique function
- Structurally removed → show replaced parent architecture and retained function
- Owner-deleted
- Preserved

For word-level editing, display the specific removed and added words inside the paired paragraph. A move is not adequately explained by merely marking two distant paragraphs as related.

## Context navigation and return

Context inspection must be reversible and must not destroy the reviewer's place.

- Opening `Old context` or `Revised context` stores the exact relation/card and current review position.
- Context must be generated from stable source/revised anchors, recorded line/semantic-block IDs, hashes, or an equivalent deterministic source mapping. Do not depend on hidden-view DOM IDs that may disappear or be duplicated after regeneration.
- A moved relation with distant source and destination anchors may show multiple local context windows instead of one huge span.
- The context view must provide a prominent `Back to <relation ID>` action.
- Returning from context must restore the **top of the exact review card**, not the top of the review list and not an arbitrary midpoint inside a tall card.
- Previous/next navigation must preserve decision state and must not force a decision before moving on.

## Rhetoric sliders

Default set:

- Humor
- Technical detail
- Length
- Bluntness

Static HTML records settings only. A future app may regenerate wording, but regeneration must preserve locked claims, evidence, certainty, recommendations, attribution, causal meaning, links, and native-object placement, then pass the same semantic audits.

## Review baselines and full-draft mode

A substantial rewrite generates:

1. original source vs current revision;
2. previous delivered revision vs corrected revision when a repair occurred;
3. a one-column full-draft commentable interface for the complete current article.

In full-draft mode, every semantic block has comments, decisions, reasoning, and sliders. A comment on a heading may address its entire section; a highlighted phrase creates an exact selected-text note. The changed-only control is hidden because there is no comparison baseline.

## Export

JSON and Markdown exports include:

- interface format and generator version;
- artifact and monotonic source/revised version IDs;
- exact source/revised filenames;
- baseline type and row scope;
- row/relation ID;
- side when applicable;
- section;
- semantic block type;
- selected quote and offsets when available;
- current text;
- comment;
- explicit review status (`pending`, `approved`, `rejected`, `needs_revision`, `needs_clarification`, or compatible legacy state);
- decision and supersession history;
- slider values;
- reasoning-request state;
- change classification and destination;
- timestamp;
- current text hash;
- applicable audience-contract fields;
- audience status and drift type, if any.

Downloads must be browser-tested. Run the generator selftest and a real interaction test after every implementation change. When local-file navigation is unavailable in automation, state that limitation and still test controls and exports with `page.set_content`; Opera/local Android `content://` behavior remains a destination-specific check.

## Required browser tests

- create, reopen, edit, and delete a comment;
- selected-text and whole-cell/relation comments, including a test that clears the live browser selection after pointer-down but before click;
- Enter, Shift+Enter, and Escape;
- direct approve/reject without opening a comment modal;
- pending vs explicit rejection visual/status distinction;
- prior-review state migration with comments, approvals, rejections, modify/brainstorm, and unresolved records preserved;
- `unresolved only` / next-unresolved navigation excludes already resolved imported decisions;
- every slider and confirmation that the slider line begins below the ID/action line;
- reasoning display;
- exact proposed-operation display and exact replacement text for wording proposals;
- moved/consolidated destination jump;
- old and revised context opening from stable anchors;
- multi-window context for a move with distant anchors;
- `Back to <relation ID>` returns to the top of the exact card;
- changed-only filter;
- search;
- audience status and drift filter;
- Copy JSON;
- Copy Markdown;
- JSON export and parse;
- Markdown export;
- reload and local persistence;
- full-draft one-column mode;
- no console or page errors.

Record the test path and limitation. Run `review_interface_browser_test.py` on the exact packaged local file when available. `page.set_content` or equivalent proves interface behavior only; it does not prove local-file navigation, download behavior in the user’s browser, or publication-platform behavior. Confirm comments remain verbatim in parsed exported JSON, the selected quote offsets survive, and the review requires no external script, stylesheet, CDN, or network request.

## Delivery

Do not render review HTML in chat. Provide files. Package substantial review families in one authoritative ZIP containing the candidate article, review file(s), immutable source comments, project state, changelog, README, manifest, checksums, and applicable ledgers/test reports. Follow `REVIEW-PACKAGE-REGRESSION.md`.
