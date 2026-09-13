# Substack helper parser incidents found in Inner Signal raw editor HTML

Date: 2026-08-26
Status: durable tooling repair findings; active source-file changes still require application of the sibling `.patch` files.

## 1. `youtube-nocookie.com` fell through as an unverified iframe

The owner-supplied raw Substack editor HTML for the Inner Signal hypnosis guide contains a native YouTube iframe with:

`https://www.youtube-nocookie.com/embed/c1SIEWq0HOc?...`

The current `project-sources/html_islands.py.txt` YouTube classifier recognizes `youtube.com`, `youtu.be`, `node-youtube`, and component-name markers, but not `youtube-nocookie.com`. The exact raw block therefore fell through to `iframe_embed`, whose compatibility strategy is `unverified`, causing `substack_transfer_helper.py` to fail closed under the current delivery gate.

### Minimal repair

Add `"youtube-nocookie.com" in low` to the existing YouTube classifier condition. Exact diff:

`patches/html-islands-youtube-nocookie-20260826.patch`

## 2. Checkout-backed `ButtonCreateButton` was mislabeled as Share

The same raw editor HTML contains a `Subscribe now` control represented as `data-component-name="ButtonCreateButton"` with both `href="%%checkout_url%%"` and `%%checkout_url%%` in its `data-attrs`.

The current classifier checks generic `ButtonCreateButton` before it checks checkout/Subscribe markers. That makes this real Subscribe button inventory as `share`. The transfer strategy happens to remain rich HTML either way, so markup survives, but object identity and the delivery receipt are wrong.

### Minimal repair

Check `subscribewidgettodom`, `subscription-widget-wrap-editor`, or `%%checkout_url%%` before the generic `ButtonCreateButton`/`%%share_url%%` Share branch. Exact diff:

`patches/html-islands-subscribe-button-classifier-20260826.patch`

## Validation against the triggering source

With both narrow classifier changes, the source inventory resolves exactly seven objects with no unverified types:

- 3 `image`
- 1 `subscribe`
- 1 `share`
- 1 `youtube`
- 1 `substack_video_post_embed`

Ordered source identities are:

1. `subscribe`
2. `image`
3. `share`
4. `youtube`
5. `substack_video_post_embed`
6. `image`
7. `image`

The seven source islands remained byte-identical and in source order after editorial edits. The current `substack_transfer_helper.py.txt` self-test passed, and its `init -> build -> verify` flow produced one rich-HTML `Copy Article` segment, zero standalone native-video manual steps, and one canonical-URL conversion for the Substack video-post embed.

Destination status remains separate: Opera -> disposable Substack draft reconstruction was not tested in this worker.

## Durable rules

1. Treat both ordinary YouTube hosts and YouTube's privacy-enhanced `youtube-nocookie.com` embed host as the same `youtube` native-object family. Do not downgrade the privacy-enhanced host to a generic unverified iframe.
2. When a generic `ButtonCreateButton` contains `%%checkout_url%%`, classify it as Subscribe before applying the generic Share/ButtonCreateButton fallback.
