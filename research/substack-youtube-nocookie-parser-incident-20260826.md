# Substack helper parser incident — `youtube-nocookie.com`

Date: 2026-08-26
Status: durable tooling repair finding; active source file patch still requires application of the sibling `.patch` file.

## Trigger

The owner-supplied raw Substack editor HTML for the Inner Signal hypnosis guide contains a native YouTube iframe with:

`https://www.youtube-nocookie.com/embed/c1SIEWq0HOc?...`

The current `project-sources/html_islands.py.txt` YouTube classifier recognizes `youtube.com`, `youtu.be`, `node-youtube`, and component-name markers, but not `youtube-nocookie.com`. The exact raw block therefore fell through to `iframe_embed`, whose compatibility strategy is `unverified`, causing `substack_transfer_helper.py` to fail closed under the current delivery gate.

## Minimal repair

Add `"youtube-nocookie.com" in low` to the existing YouTube classifier condition. The exact one-line unified diff is preserved at:

`patches/html-islands-youtube-nocookie-20260826.patch`

## Validation against the triggering source

With only that classifier change, the source inventory resolves seven objects with no unverified types:

- 3 `image`
- 2 `share`
- 1 `youtube`
- 1 `substack_video_post_embed`

The seven source islands remained byte-identical and in source order after editorial edits. The canonical `substack_transfer_helper.py.txt` self-test passed, and its `init -> build -> verify` flow produced one rich-HTML `Copy Article` segment, zero standalone native-video manual steps, and one canonical-URL conversion for the Substack video-post embed.

Destination status remains separate: Opera -> disposable Substack draft reconstruction was not tested in this worker.

## Durable rule

Treat both ordinary YouTube hosts and YouTube's privacy-enhanced `youtube-nocookie.com` embed host as the same `youtube` native-object family. Do not downgrade the privacy-enhanced host to a generic unverified iframe.
