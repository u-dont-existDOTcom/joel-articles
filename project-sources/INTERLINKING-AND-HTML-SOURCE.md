# Interlinking, Raw Substack Source, Transfer-Ready Native Objects, and Diff Delivery

## Natural interlinking

1. Read `CANON-FACTS.md` and `ARTICLE-INDEX.md`.
2. Add only earlier pieces that genuinely help at the point of mention.
3. Use exact verified URLs. Never guess or rebuild a slug.
4. Repeated links may be intentional when the later context asks the reader to act, gives a different reason to click, or appears after the reader now understands the relevance. Do not deduplicate mechanically.
5. Zero links is acceptable; one to three often fits an essay; a guide may need more.
6. Refresh the index from a new sitemap before publication when supplied.

## Linked references as progressive disclosure

A link may intentionally carry background that would burden the current passage. Do not reproduce the destination article inside the referring sentence.

Use this hierarchy:

1. **Linked term alone** for a peripheral reference.
2. **Small orientation gloss** when comprehension requires it.
3. **One concise explanation** when the current argument depends on it.
4. **Full definition or technical treatment** only when the section is teaching that subject or Joel approved the insertion.

Apply these levels just in time. Do not delay a definition past the first sentence that depends on it, and do not define a linked peripheral term merely because it is unfamiliar. See `PROGRESSIVE-DISCLOSURE-EXAMPLES.md` for concrete before/after examples involving Hearthwork, *pl/ork*, *nāda*, acronyms, linked protocols, and source biographies.

Flag **link echo** when a linked phrase is followed by an unnecessary definition, mechanism, miniature biography, guide summary, or technical recipe. Canon facts protect accuracy; they do not force exposition. Any substantive explanation absent from the source—including a canon-fact insertion—must be shown for approval.

## Attribute only source-specific material

Do not credit a reviewer or lecturer merely because they supplied an explanation of a broadly established idea. Common developmental concepts may be integrated without attribution, including the inherited/internalized parent, the human-doer pattern, experimentation in identity development, externalized worth, and permission to be a beginner.

Name a source when the article depends on that source's distinctive term, original framework, quotation, evidence, historical claim, or source-specific interpretation. If a distinctive source term conflicts with Joel's vocabulary, name it once, explain the adopted article term and distinction, then use the adopted term consistently.

## Raw editor HTML is the sole authority

For an existing Substack article, the original raw editor HTML—not TXT, PDF extraction, screenshots, browser-rendered HTML, a prior helper, or a reconstructed preview—is the authority for:

- every `href`, including intentional repeated links;
- native-object identity and complete metadata;
- images, captions, dimensions, source sets, and placement;
- digest post previews, comments, Share, Subscribe, YouTube, native Substack-uploaded video, Substack video-post embeds, paywalls, and unknown objects;
- headings, emphasis, lists, blockquotes, section order, and media anchors.

Extract the editor body only. Exclude page-level scripts, analytics, advertisements, navigation, sidebars, and publication chrome. The raw editor HTML establishes identity and metadata. An approved editorial revision may move an intact object. The exact final archival HTML then becomes the source for transfer conversion.

## Inventory semantic objects before editing

Restore `html_islands.py.txt` from Project Sources as `html_islands.py`, then run:

```bash
python html_islands.py inventory original.html --out objects.json
```

Inventory each object by:

| Order | Type | Exact source hash | Canonical URL/node ID | Preceding anchor | Following anchor | Editorial function | Approved destination | Archival treatment | Transfer treatment | Destination result |
|---|---|---|---|---|---|---|---|---|---|---|

Do not report “all islands preserved” as a substitute. A frozen count says how many raw spans were protected; it does not establish identity, placement, transfer behavior, or destination reconstruction. Also audit heading hierarchy and table-of-contents nesting after any move.

## Archival HTML and transfer-ready HTML are separate products

### Archival Substack HTML

Preserve the editor body and native-object markup exactly wherever not explicitly edited. Use `html_islands.py` for source preservation:

```bash
python html_islands.py freeze original.html --out editable.html --manifest islands.json
python html_islands.py restore edited.html --out archival-final.html --manifest islands.json
python html_islands.py verify archival-final.html --manifest islands.json
```

A checksum proves source-level island fidelity only.

### Transfer-ready payload

Raw editor HTML is not automatically valid clipboard HTML. Build a separate payload from the exact final archival HTML for the confirmed browser path.

For Opera opening a downloaded local helper:

1. Extract only the editor body.
2. Wrap the transferable article in `<div dir="auto" class="body markup">`; do not copy the nested `contenteditable="true"` ProseMirror editor root.
3. Remove `contenteditable="false"` and `draggable="true"` from transferable native objects in the payload only.
4. Preserve complete object classes, children, `data-component-name`, `data-attrs`, placeholders, URLs, dimensions, captions, order, and placement.
5. Invoke `navigator.clipboard.write()` with `ClipboardItem` directly from the click handler, with the silent off-screen-contenteditable `document.execCommand("copy")` fallback.
6. Do not await image loading, decoding, timers, requests, or other asynchronous work before clipboard access.
7. Transform only known wrapper attributes and native-object locks. Do not parse and reserialize the fragile document.
8. Prefer one complete payload except for a standalone native Substack-uploaded video. Each native uploaded video is excluded from clipboard HTML and forces an ordered split plus a manual insertion step at its recorded anchors. A Substack video-post preview/card does not force a split; replace it with its canonical post URL alone at the same source position inside the current segment.
9. Include manual paywall placement only when a genuine paywall marker exists in the raw source.
10. Leave unknown native objects unverified until their actual path is tested.

## Native-object transfer matrix

| Object type | Archival treatment | Transfer conversion | Destination status |
|---|---|---|---|
| Image/picture/caption block | Preserve exact source island | Remove editor locks; retain figure/picture/source/img/srcset/data/dimensions/caption/CDN URLs; retain or add `can-restack` only under the confirmed profile | Confirmed path; verify every regenerated final |
| `digest-post-embed` preview | Preserve complete native preview | Remove editor locks; retain outer classes, `data-component-name`, `data-attrs`, all children, preview image, author/title/subtitle/publication metadata, placeholder and canonical URLs | Confirmed candidate; verify each article/destination |
| YouTube | Preserve complete source block | Remove editor locks; retain iframe/native metadata, dimensions, canonical URL, wrapper classes, and placement | Confirmed where tested |
| Native Substack-uploaded video | Preserve the complete raw native-video island, upload/media ID, player metadata, poster/source data, dimensions, wrappers, and placement | Exclude the island from clipboard HTML; split into ordered rich-HTML segments around it; require manual native-video insertion using its exact identity and anchors | Owner-confirmed nonportable; destination succeeds only after manual insertion and draft verification |
| Substack video-post embed | Preserve the complete post-preview island exactly | Replace the rendered card with its canonical post URL alone at the same source position inside the current segment; do not split solely for it | Owner-confirmed strategy; verify reconstruction each final |
| Share | Preserve exact `ButtonCreateButton` source | Remove editor locks; retain full `data-attrs`, `%%share_url%%`, visible label, children, and placement | Destination-confirmed |
| Subscribe | Preserve exact `SubscribeWidgetToDOM` source | Remove editor locks; retain `subscription-widget-wrap-editor`, full metadata, `%%checkout_url%%`, text, language, form, children, and placement | Rich-HTML candidate; destination test required |
| Rendered Substack comment card | Preserve rendered source only in archive | Replace the complete card with its canonical URL alone in its own paragraph at the same source position inside the current payload segment | Confirmed strategy; verify final reconstruction |
| Paywall | Preserve genuine marker | Omit nonportable marker from payload and provide a manual native insertion/verification instruction at its recorded anchors | Only when source marker exists |
| Instagram/unknown native object | Preserve exact source | Isolate and test; no inferred strategy | Unverified |

Do not replace a digest preview with an ordinary link merely because one transfer attempt failed. Do not classify Subscribe as manual-only before the cleaned rich-HTML path fails. A comment reconstructing correctly says nothing about whether images or previews survived.

### Video classification and split rule

Classify the enclosing semantic object before descendant media tags:

1. Detect `DigestPostEmbed` / `digest-post-embed` before checking for `<video>`.
2. A video-bearing Substack post preview is `substack_video_post_embed`, not `native_video`; preserve it in the archive and use its canonical post URL in the current payload segment.
3. A standalone `native-video-embed`, `VideoEmbedPlayer`, or native upload/media ID is `native_video`; preserve it in the archive, exclude it from clipboard HTML, split the helper at that position, and require manual insertion.
4. Keep YouTube/external video separate.

A generic `<video>` descendant must never override the enclosing post-preview classification. With `N` standalone native uploaded videos, the helper normally emits `N + 1` ordered rich-HTML segments and `N` manual insertion steps; empty leading or trailing segments may be suppressed only when the sequence remains explicit.

## Object-type isolation

When one native type fails:

1. identify the exact type;
2. inspect its raw source and transfer conversion;
3. preserve unrelated working types unchanged;
4. test the smallest correction to that type;
5. recheck its approved placement, anchors, and heading logic;
6. verify the actual Substack draft.

Do not remove all media, abandon one-paste for an unrelated object failure, split around comments without evidence, convert every object to a URL, infer unrelated failures, or treat a successful clipboard operation as successful publication transfer. The owner-confirmed standalone native-uploaded-video exception still requires its exact ordered splits.

A button reporting **Copied** proves only that clipboard writing completed.

## Three independent validation planes

### 1. Source fidelity

Record:

- original raw editor HTML hash;
- exact final archival HTML hash;
- editor-body extraction boundary;
- ordered semantic-object inventory;
- byte-identical object markup where unchanged;
- approved object moves;
- preserved links, captions, headings, anchors, and hierarchy.

### 2. Transfer conversion

Record:

- `body markup` wrapper conversion;
- editor-lock removal;
- comment-card-to-canonical-URL substitution;
- Substack video-post-card-to-canonical-post-URL substitution inside the current segment;
- standalone native uploaded-video exclusion, segment boundaries, manual insertion identities, and anchors;
- any approved `can-restack` addition;
- per-object transfer treatment;
- paywall manual step when present;
- any intentional omission.

### 3. Destination result

In a blank or disposable Substack draft, verify independently:

- images;
- digest post previews;
- YouTube;
- native Substack-uploaded video insertion and playback;
- Substack video-post reconstruction from its canonical URL;
- Share;
- Subscribe;
- comment reconstruction;
- paywall placement;
- source order and section placement;
- captions, links, atomic editing, playback, and widget behavior.

Checksums and source hashes prove identity. They do not prove clipboard compatibility or destination reconstruction.

## Helper compatibility profile and regression gate

Restore `substack_transfer_helper.py.txt` as `substack_transfer_helper.py` and use `CONFIRMED-SUBSTACK-HELPER.json`.

```bash
python substack_transfer_helper.py init archival-final.html \
  --plan transfer-plan.json --inventory objects.json \
  --compat-profile CONFIRMED-SUBSTACK-HELPER.json

python substack_transfer_helper.py build archival-final.html \
  --plan transfer-plan.json --compat-profile CONFIRMED-SUBSTACK-HELPER.json \
  --out final-transfer-helper.html --report transfer-report.md \
  --against last-confirmed-helper.html --compat-report compatibility-regression.md

python substack_transfer_helper.py verify archival-final.html \
  --plan transfer-plan.json --compat-profile CONFIRMED-SUBSTACK-HELPER.json \
  --helper final-transfer-helper.html --against last-confirmed-helper.html \
  --compat-report compatibility-regression.md
```

After every regeneration verify:

- source and editor-body hashes match the exact final archival source;
- when there is no native uploaded video, one payload covers the editor body exactly once after recorded conversions;
- when native uploaded video exists, ordered rich-HTML segments plus the excluded preserved native-video islands cover the editor body exactly once; no native-video markup occurs in any clipboard payload;
- the wrapper is exactly `div[dir=auto].body.markup`;
- visible control count, labels, and order match the profile;
- immediate ClipboardItem and silent contenteditable fallback remain;
- no unauthorized visible manual fallback UI appears;
- only known editor locks were removed;
- comments and Substack video-post embeds are canonical URLs at their original positions and their rendered card HTML is absent from clipboard payloads;
- standalone native uploaded videos create only the required ordered splits and manual insertion steps, with identity and preceding/following anchors retained;
- rich object types preserve their complete metadata and order;
- paywall instructions appear only when a source marker exists;
- unknown objects remain unverified;
- the downloaded file is opened directly in Opera and pasted into a disposable Substack draft.

Static verification and runtime destination testing are separate. A source revision does not authorize rebuilding compatibility decisions from scratch.

## Complete HTML deliverables

For a substantial revision, return:

1. complete authoritative archival HTML;
2. an interactive side-by-side review HTML for substantial revisions;
3. an optional lightweight static changed-passages diff only when requested;
4. the minimal transfer helper built from the exact final archival HTML when native objects exist, unless Joel declines it;
5. a transfer report separating source fidelity, transfer conversion, compatibility regression, and destination result;
6. article-only HTML when useful.

Do not provide only fragments unless Joel asks for fragments.

## Interactive review and optional quick diff

For every substantial revision, restore both Project Sources:

```bash
cp interactive_review.py.txt interactive_review.py
cp review_interface_template.html.txt review_interface_template.html
python interactive_review.py original.html revised.html \
  --template review_interface_template.html \
  --out article-commentable-side-by-side.html \
  --title "Article — Original vs Revised" \
  --baseline-type original-vs-current
```

After a repair, run it again with the previous delivery and corrected revision using `--baseline-type previous-delivery-vs-corrected`. The interface must retain one semantic block per box, comments, Keep/Remove/Brainstorm, reasoning, four second-line rhetoric sliders labeled Humor, Technical detail, Length, and Bluntness, local persistence, search, changed-only filtering, and JSON/Markdown exports. Run `python interactive_review.py --selftest --template review_interface_template.html` and browser interaction tests. Generate the complete current-draft review separately:

```bash
python interactive_review.py --full-draft revised.html \
  --template review_interface_template.html \
  --out article-full-draft-commentable.html \
  --title "Article — Full Draft Review" \
  --new-version rNN-candidate
```

This one-column artifact makes every semantic block commentable and preserves exact selected-text quote/offset notes.

`html_diff.py` remains available only for an optional quick static view:

```bash
python html_diff.py original.html revised.html --out changes.quick-diff.html
```

The quick diff may show yellow additions and collapsed deletions. It must not overwrite, replace, or be mislabeled as the interactive review interface.

## Artifact-family regression

Treat the archival article, diff, transfer-ready payload, helper, self-hosted page, Ghost fragment, app, manual, and sibling guide as one artifact family. After every change:

1. identify affected destinations;
2. rebuild the payload/helper from the exact final archival HTML;
3. preserve every confirmed object conversion and approved placement unless Joel changes it;
4. regression-check object types independently;
5. record intentional omissions;
6. report source fidelity, transfer conversion, and destination result separately.

Merge newly supplied files and links into the active source packet. Compare URLs by canonical value, not descriptive labels. Never invent a native embed from an ordinary page URL.

## Three publication modes

### 1. Archival Substack HTML

Preserve the editor body and native markup exactly under the island/object workflow. This is the publication archive, not a portable page.

### 2. Substack transfer helper

Implement only the confirmed Opera local-file-to-editor path. Build a separate payload from the exact final archival HTML: one-paste when no standalone native uploaded video is present, or ordered copy segments plus manual native-video insertion steps when one is present. Test the final helper in a blank Substack draft.

### 3. Self-hosted standalone HTML

Build a fresh document. Remove former-host scripts, CSS, analytics, metadata, ads, comments, recommendation panels, upload controls, subscription chrome, and provider UI. Preserve author-created navigation, diagrams, cards, and local scripts. Replace metadata and rehost assets.

Before delivery, verify:

- no former-host dependency remains in HTML, CSS, JS, images, source sets, actions, or metadata;
- every ID is unique;
- every internal anchor resolves;
- mobile and print behavior survive;
- owned title, description, canonical URL, and metadata are present;
- no former-host interface chrome remains.

Use `html_publish_modes.py` for conservative adaptation and validation. A real hosted-page test remains the destination result.

## Ghost HTML-card mode

Treat the artifact as an embedded fragment:

1. remove document tags and metadata;
2. return one fragment with scoped styles, one unique root, content, and local script;
3. namespace every class and selector beneath the root;
4. escape Ghost's narrow canvas explicitly when full width is required;
5. prefer grid with sticky desktop navigation over fixed positioning;
6. hide duplicate Ghost title/comments/recommendations only through root-conditional selectors;
7. use fixed pixel sizes with `!important` for critical embedded navigation typography where theme inheritance changes it;
8. validate document-tag absence, unique IDs, anchors, diagrams/cards, responsive navigation, namespacing, and root scoping;
9. treat a real Ghost upload and screenshot/computed-style inspection as the destination test;
10. propagate a confirmed adapter to sibling artifacts and record each result;
11. provide files/download links only.

## No previews

Never render, embed, open, generate, or offer previews of HTML or web-app deliverables. Provide files/download links only.
