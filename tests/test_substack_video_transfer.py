#!/usr/bin/env python3
from __future__ import annotations

import base64
import importlib.util
from importlib.machinery import SourceFileLoader
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "project-sources"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
COMPAT = SOURCE_DIR / "CONFIRMED-SUBSTACK-HELPER.json"


def load_module(name: str, path: Path):
    if not path.is_file() and path.suffix == ".py":
        path = path.with_suffix(".py.txt")
    loader = SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


html_islands = load_module("html_islands", SOURCE_DIR / "html_islands.py")
helper = load_module("substack_transfer_helper", SOURCE_DIR / "substack_transfer_helper.py")


class SubstackVideoTransferTests(unittest.TestCase):
    def state_for(self, fixture_name: str):
        source = FIXTURES / fixture_name
        temp = tempfile.TemporaryDirectory(prefix="substack-video-test-")
        root = Path(temp.name)
        plan = root / "plan.json"
        inventory = root / "inventory.json"
        helper.init_plan(source, plan, inventory, COMPAT)
        state = helper.transfer_state(source, plan, COMPAT)
        return temp, source, plan, inventory, state

    def payload_text(self, state) -> str:
        return "\n".join(helper.unb64(item["html_b64"]) for item in state["segments"])

    def state_for_text(self, body: str):
        temp = tempfile.TemporaryDirectory(prefix="substack-video-inline-")
        root = Path(temp.name)
        source = root / "source.html"
        source.write_text(
            '<div contenteditable="true" data-testid="document-editor" class="tiptap ProseMirror tiptap-editor-content">'
            + body + '</div>',
            encoding="utf-8",
        )
        plan = root / "plan.json"
        inventory = root / "inventory.json"
        helper.init_plan(source, plan, inventory, COMPAT)
        state = helper.transfer_state(source, plan, COMPAT)
        return temp, source, plan, inventory, state

    def test_native_uploaded_video_splits_and_is_never_copied(self):
        temp, _, _, _, state = self.state_for("native-video-only.html")
        self.addCleanup(temp.cleanup)
        self.assertEqual(state["native_video_count"], 1)
        self.assertEqual(state["segment_count"], 2)
        self.assertEqual(len([s for s in state["manual_steps"] if s["kind"] == "manual_native_video_insertion"]), 1)
        self.assertNotIn("native-video-embed", self.payload_text(state))
        step = [s for s in state["manual_steps"] if s["kind"] == "manual_native_video_insertion"][0]
        self.assertEqual(step["media_id"], "native-001")
        self.assertEqual(step["preceding_anchor"], "Before Native")
        self.assertEqual(step["following_anchor"], "After Native")

    def test_video_post_embed_becomes_url_without_split(self):
        temp, _, _, _, state = self.state_for("video-post-only.html")
        self.addCleanup(temp.cleanup)
        self.assertEqual(state["native_video_count"], 0)
        self.assertEqual(state["segment_count"], 1)
        self.assertEqual(state["substack_video_post_embed_count"], 1)
        payload = self.payload_text(state)
        self.assertIn("https://example.substack.com/p/my-video-post?r=abc", payload)
        self.assertNotIn("DigestPostEmbed", payload)
        self.assertNotIn("video_upload_id", payload)
        self.assertFalse(any(step["kind"] == "manual_native_video_insertion" for step in state["manual_steps"]))

    def test_two_native_videos_produce_three_segments(self):
        temp, _, _, _, state = self.state_for("two-native-videos.html")
        self.addCleanup(temp.cleanup)
        self.assertEqual(state["native_video_count"], 2)
        self.assertEqual(state["segment_count"], 3)
        steps = [s for s in state["manual_steps"] if s["kind"] == "manual_native_video_insertion"]
        self.assertEqual([s["media_id"] for s in steps], ["native-101", "native-102"])
        self.assertNotIn("native-video-embed", self.payload_text(state))

    def test_boundary_native_videos_preserve_explicit_empty_edges(self):
        temp, _, _, _, state = self.state_for("boundary-native-videos.html")
        self.addCleanup(temp.cleanup)
        self.assertEqual(state["segment_count"], 3)
        self.assertTrue(state["segments"][0]["empty"])
        self.assertFalse(state["segments"][1]["empty"])
        self.assertTrue(state["segments"][2]["empty"])
        required = [item["required"] for item in state["sequence"] if item["kind"] == "copy_segment"]
        self.assertEqual(required, [False, True, False])

    def test_mixed_types_keep_unrelated_conversions_independent(self):
        temp, _, _, _, state = self.state_for("mixed-native-objects.html")
        self.addCleanup(temp.cleanup)
        self.assertEqual(state["native_video_count"], 1)
        self.assertEqual(state["segment_count"], 2)
        payload = self.payload_text(state)
        self.assertIn("youtube.com/embed/abc", payload)
        self.assertIn("captioned-image-container", payload)
        self.assertIn("can-restack", payload)
        self.assertIn("https://example.substack.com/p/video-post", payload)
        self.assertIn("https://substack.com/@writer/note/c-123", payload)
        self.assertNotIn("native-video-embed", payload)
        self.assertNotIn("Paywall", payload)
        kinds = [step["kind"] for step in state["manual_steps"]]
        self.assertIn("manual_native_video_insertion", kinds)
        self.assertIn("manual_native_object", kinds)

    def test_adjacent_native_objects_are_not_merged(self):
        text = (
            '<div class="native-video-embed" data-attrs="{&quot;mediaUploadId&quot;:&quot;a&quot;}"><video></video></div>'
            '<div class="native-video-embed" data-attrs="{&quot;mediaUploadId&quot;:&quot;b&quot;}"><video></video></div>'
        )
        spans = html_islands.find_protected_spans(text)
        self.assertEqual(len(spans), 2)

    def test_real_escaped_metadata_is_decoded(self):
        text = (FIXTURES / "video-post-only.html").read_text(encoding="utf-8")
        body, _ = html_islands.extract_editor_body(text)
        data = html_islands.inventory_data(body, "fixture.html", html_islands.sha256(body.encode()))
        obj = data["objects"][0]
        self.assertEqual(obj["type"], "substack_video_post_embed")
        self.assertEqual(obj["canonical_url"], "https://example.substack.com/p/my-video-post?r=abc")
        self.assertEqual(obj["video_upload_id"], "vpost-001")
        self.assertFalse(obj["forces_payload_split"])

    def test_freeze_restore_keeps_exact_native_video_island(self):
        source = FIXTURES / "native-video-only.html"
        with tempfile.TemporaryDirectory(prefix="html-islands-roundtrip-") as temp:
            root = Path(temp)
            editable = root / "editable.html"
            manifest = root / "islands.json"
            restored = root / "restored.html"
            html_islands.freeze(source, editable, manifest)
            html_islands.restore(editable, restored, manifest)
            self.assertEqual(source.read_bytes(), restored.read_bytes())

    def test_stale_profile_native_video_rich_html_is_rejected(self):
        data = json.loads(COMPAT.read_text(encoding="utf-8"))
        data["native_objects"]["native_video"]["strategy"] = "rich_html"
        with tempfile.TemporaryDirectory(prefix="stale-profile-") as temp:
            path = Path(temp) / "profile.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "native_video must force split"):
                helper.load_compat(path)

    def test_plain_video_post_url_remains_literal_without_embed_conversion(self):
        url = "https://example.substack.com/p/video-post"
        temp, _, _, _, state = self.state_for_text(f"<p>{url}</p>")
        self.addCleanup(temp.cleanup)
        self.assertEqual(state["native_video_count"], 0)
        self.assertEqual(state["substack_video_post_embed_count"], 0)
        self.assertEqual(state["segment_count"], 1)
        self.assertIn(url, self.payload_text(state))
        self.assertEqual(state["transformations"], [])

    def test_paywall_is_manual_post_paste_but_not_native_video_split(self):
        paywall = '<div class="paywall-marker" data-component-name="Paywall"></div>'
        temp, _, _, _, state = self.state_for_text(f"<p>A</p>{paywall}<p>B</p>")
        self.addCleanup(temp.cleanup)
        self.assertEqual(state["native_video_count"], 0)
        self.assertEqual(state["segment_count"], 1)
        self.assertNotIn("paywall-marker", self.payload_text(state))
        self.assertTrue(any(step["kind"] == "manual_native_object" for step in state["manual_steps"]))

    def test_manifest_payload_tampering_is_detected(self):
        temp, _, _, _, state = self.state_for("native-video-only.html")
        self.addCleanup(temp.cleanup)
        original = helper.unb64(state["segments"][0]["html_b64"])
        payload = original[:-len(helper.WRAPPER_SUFFIX)] + "<p>tampered</p>" + helper.WRAPPER_SUFFIX
        state["segments"][0]["html_b64"] = base64.b64encode(payload.encode("utf-8")).decode("ascii")
        with self.assertRaisesRegex(ValueError, "payload checksum mismatch"):
            helper.verify_manifest_invariants(state)

    def test_generated_helper_reverifies_against_source(self):
        temp, source, plan, _, _ = self.state_for("mixed-native-objects.html")
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        out = root / "helper.html"
        report = root / "report.md"
        helper.build(source, plan, COMPAT, out, report)
        helper.verify(source, plan, COMPAT, out)
        manifest = helper.extract_manifest(out)
        helper.verify_manifest_invariants(manifest)
        self.assertIn("pending final downloaded-helper-in-Opera", report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
