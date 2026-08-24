# Substack Clipboard Helper Delivery Gate

Status: **ACTIVE / BLOCKING.**

This gate exists because a hand-built replacement clipboard helper can look structurally plausible while silently breaking Substack native-object reconstruction. A worker must never improvise a new helper implementation when the repository already contains a confirmed generator and compatibility profile.

## Hard rule

For every user-facing Substack clipboard helper:

1. Use the exact current `project-sources/substack_transfer_helper.py.txt` as the generator authority, materialized only for execution when necessary.
2. Use the exact current `project-sources/html_islands.py.txt` for editor-body extraction and native-object classification.
3. Use the exact current `project-sources/CONFIRMED-SUBSTACK-HELPER.json` compatibility profile.
4. Use raw Substack editor HTML as native-object/link/markup authority. Do not reconstruct native objects from Markdown markers, memory, screenshots, or a model-generated template.
5. Run the generator's `init`, `build`, and `verify` path. A helper is not deliverable merely because it contains a Copy button or valid-looking native markup.
6. When a previously destination-confirmed helper exists, use it as the `--against` regression baseline whenever the current generator supports that comparison.
7. Before giving the helper to Joel, inspect its embedded `hva-transfer-manifest` and require the current canonical helper format, source/editor-body hashes, compatibility-profile hash, native-object signatures/order/anchors, transfer strategy, and static verification result.
8. If the canonical generator cannot be executed or verified, **do not hand-build a fallback helper.** Report the execution blocker or give the already confirmed prior helper only when it is still bound to the exact intended archival source.

## Explicitly prohibited

- Writing a new Python/JavaScript clipboard helper ad hoc for a specific article.
- Converting the registered Markdown master to HTML with a custom parser and calling that a Substack helper.
- Recreating image, YouTube, Share, Subscribe, digest-preview, comment, paywall, or native-video markup from remembered structure or inferred metadata.
- Treating a plausible-looking `<div class="body markup">` payload as evidence that the confirmed transfer path was used.
- Saying embeds are preserved unless the native-object source islands passed the canonical generator/verify path and destination status is reported separately.
- Replacing a failed canonical build with an improvised helper merely to produce a downloadable artifact.

## Delivery receipt

A worker delivering a helper must be able to state:

- archival source identity and SHA-256;
- editor-body SHA-256;
- canonical generator path;
- compatibility-profile path and SHA-256;
- helper manifest format;
- native-object count/types/order;
- payload/segment count and any manual native-video steps;
- canonical `verify` result;
- destination-test status separately.

If any of those are unavailable, the helper is **not verified for delivery**.

## Incident that promoted this gate

On 2026-08-24, during Romance r23r2 publication preparation, the assistant bypassed the existing confirmed generator and wrote replacement helper logic by hand. The generated file attempted to reconstruct native objects and consequently failed to preserve working embeds. The correct response was to recover and use the established `substack_transfer_helper.py.txt` path and the previously confirmed helper behavior. This incident is the counterexample: metadata recovery is not permission to reimplement the transport layer.
