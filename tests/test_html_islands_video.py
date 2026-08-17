#!/usr/bin/env python3
from __future__ import annotations
import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path
import tempfile
import unittest
import sys

SOURCE_DIR = Path(__file__).resolve().parents[1] / "project-sources"
MODULE_PATH = SOURCE_DIR / "html_islands.py"
if not MODULE_PATH.is_file():
    MODULE_PATH = SOURCE_DIR / "html_islands.py.txt"
loader = SourceFileLoader("html_islands", str(MODULE_PATH))
spec = importlib.util.spec_from_loader(loader.name, loader)
assert spec and spec.loader
html_islands = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = html_islands
spec.loader.exec_module(html_islands)


class SubstackVideoClassificationTests(unittest.TestCase):
    def test_standalone_native_video_forces_split(self) -> None:
        raw = '<div class="native-video-embed" data-component-name="VideoEmbedPlayer" data-attrs=\'{"mediaUploadId":"m-123"}\'><video></video></div>'
        self.assertEqual(
            html_islands.classify_object(raw),
            ("native_video", "split_payload_manual_native_video_insertion"),
        )

    def test_data_video_id_is_native_media_identity_fallback(self) -> None:
        raw = '<div class="native-video-embed"><video data-video-id="fallback-123"></video></div>'
        self.assertEqual(html_islands.native_media_identity(raw, "native_video"), "fallback-123")

    def test_extracts_substack_editor_root_without_copying_wrapper(self) -> None:
        inner = '<h2>Heading</h2><p>Article text.</p>'
        source = (
            '<html><body><div contenteditable="true" data-testid="document-editor" '
            'class="tiptap ProseMirror tiptap-editor-content">' + inner + '</div></body></html>'
        )
        body, boundary = html_islands.extract_editor_body(source)
        self.assertEqual(body, inner)
        self.assertEqual(boundary["mode"], "substack-editor-root")

    def test_video_post_embed_does_not_become_native_video(self) -> None:
        raw = '<div class="digest-post-embed" data-component-name="DigestPostEmbed" data-attrs=\'{"video_upload_id":"v-123"}\'><a href="https://example.substack.com/p/video-post">Post</a><video></video></div>'
        self.assertEqual(
            html_islands.classify_object(raw),
            ("substack_video_post_embed", "canonical_url_in_payload"),
        )

    def test_nonvideo_digest_stays_rich_html(self) -> None:
        raw = '<div class="digest-post-embed" data-component-name="DigestPostEmbed"><a href="https://example.substack.com/p/text-post">Post</a></div>'
        self.assertEqual(html_islands.classify_object(raw), ("digest_post_embed", "rich_html"))

    def test_youtube_remains_separate(self) -> None:
        raw = '<div class="node-youtube"><iframe src="https://www.youtube.com/embed/abc"></iframe></div>'
        self.assertEqual(html_islands.classify_object(raw), ("youtube", "rich_html"))

    def test_inventory_records_video_post_url_without_split(self) -> None:
        text = '<h2>Before</h2><div class="digest-post-embed" data-component-name="DigestPostEmbed" data-attrs=\'{"video_upload_id":"v-123"}\'><a href="https://example.substack.com/p/video-post">Post</a><video></video></div><h2>After</h2>'
        data = html_islands.inventory_data(text, "fixture.html", html_islands.sha256(text.encode()))
        self.assertEqual(data["object_count"], 1)
        obj = data["objects"][0]
        self.assertEqual(obj["type"], "substack_video_post_embed")
        self.assertEqual(obj["canonical_url"], "https://example.substack.com/p/video-post")
        self.assertFalse(obj["forces_payload_split"])
        self.assertFalse(obj["manual_insertion_required"])

    def test_inventory_records_native_split_and_anchors(self) -> None:
        text = '<h2>Before</h2><div class="native-video-embed" data-component-name="VideoEmbedPlayer" data-attrs=\'{"mediaUploadId":"m-123"}\'><video></video></div><h2>After</h2>'
        data = html_islands.inventory_data(text, "fixture.html", html_islands.sha256(text.encode()))
        obj = data["objects"][0]
        self.assertEqual(obj["type"], "native_video")
        self.assertTrue(obj["forces_payload_split"])
        self.assertTrue(obj["manual_insertion_required"])
        self.assertEqual(obj["preceding_anchor"], "Before")
        self.assertEqual(obj["following_anchor"], "After")


if __name__ == "__main__":
    unittest.main(verbosity=2)
