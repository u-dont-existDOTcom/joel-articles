# Substack Helper Compatibility Regression

- Current helper format: `joel-substack-transfer-helper-v4`
- Current profile: `Opera local-file native-object helper with native-video segmentation`
- Current browser/path: `Opera` / `downloaded local HTML file opened directly`
- Current payload mode: `single_rich_html`
- Current native uploaded-video count: 0
- Current wrapper: `div[dir=auto].body.markup`
- Clipboard path: immediate `ClipboardItem`, silent off-screen-contenteditable `execCommand` fallback.

## Prior helper

- File: `Copy-to-Substack-r03.html`
- SHA-256: `cc6eaeb427c1c07903f69b29bacdd6c0a9520c58668af64a1e2404eb99166af2`
- Format: `joel-substack-transfer-helper-v4`
- Profile: `Opera local-file native-object helper with native-video segmentation`
- Payload mode: `single_rich_html`
- Browser/path: `Opera` / `downloaded local HTML file opened directly`

## Intended compatibility change

- Standalone native Substack-uploaded video is now excluded from clipboard payloads and creates ordered manual-insertion boundaries.
- Substack video-post embeds remain inside the current segment as canonical post URLs and never create a split by themselves.
- Unrelated confirmed image, digest, YouTube, comment, Share, Subscribe, wrapper, and clipboard-path behavior remains independently governed by the profile.

## Destination status

- Static regression comparison only. A final Opera-to-disposable-Substack-draft test is still required.
