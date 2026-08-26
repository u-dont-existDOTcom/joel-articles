#!/usr/bin/env python3
"""Extend the canonical Substack helper conservatively for native uploaded audio.

This migration edits the ACTUAL canonical parser/profile/generator files in the current
worktree. It does not create an alternate clipboard helper. Native audio is classified
explicitly and omitted from rich-HTML payloads with a recorded manual re-insertion step.

Intended for a disposable/iteration worktree until the Opera -> Substack destination path
has been verified. Re-running is idempotent.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def patch_once(path: Path, old: str, new: str, label: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if new in text:
        print(f"already applied: {label}")
        return False
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected one exact patch anchor in {path}, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print(f"patched: {label}")
    return True


def patch_parser(path: Path) -> None:
    patch_once(
        path,
        '    "native-video-embed",\n    "videoembedplayer",\n    "mediauploadid",',
        '    "native-video-embed",\n    "native-audio-embed",\n    "videoembedplayer",\n    "audioembedplayer",\n    "mediauploadid",',
        "native-audio island markers",
    )
    patch_once(
        path,
        'PROTECTED_TAGS = {"figure", "picture", "iframe", "video"}\nMEDIA_TRIGGER_TAGS = {"img", "source", "figure", "picture", "iframe", "video"}',
        'PROTECTED_TAGS = {"figure", "picture", "iframe", "video", "audio"}\nMEDIA_TRIGGER_TAGS = {"img", "source", "figure", "picture", "iframe", "video", "audio"}',
        "protect audio tags",
    )
    native_video_comment = '''    # Standalone native uploaded video must be checked before image because its
    # source block may contain a poster <img>. Digest/video-post cards were
    # already handled above and therefore cannot fall through to this branch.
    native_video_markers = (
'''
    audio_then_video = '''    # Native Substack-uploaded audio is conservatively treated as nonportable
    # until a real destination test proves a richer transfer path. Preserve the
    # source island and require manual re-insertion after the rich-HTML paste.
    native_audio_markers = (
        "native-audio-embed", "audioembedplayer", "<audio",
    )
    if any(marker in low for marker in native_audio_markers):
        return "native_audio", "manual_native_if_present"

    # Standalone native uploaded video must be checked before image because its
    # source block may contain a poster <img>. Digest/video-post cards were
    # already handled above and therefore cannot fall through to this branch.
    native_video_markers = (
'''
    patch_once(path, native_video_comment, audio_then_video, "classify native audio before generic unknown embeds")

    old_identity = '''def native_media_identity(raw: str, object_type: str = "native_video") -> str | None:
    """Extract a stable upload/media identity from escaped or literal source metadata."""
    keys = (
        ("mediaUploadId", "media_upload_id", "media-upload-id", "data-video-id", "videoUploadId", "video_upload_id")
        if object_type == "native_video"
        else ("video_upload_id", "videoUploadId", "data-video-id")
    )
    return embedded_metadata_value(raw, keys)
'''
    new_identity = '''def native_media_identity(raw: str, object_type: str = "native_video") -> str | None:
    """Extract a stable upload/media identity from escaped or literal source metadata."""
    if object_type == "native_video":
        keys = ("mediaUploadId", "media_upload_id", "media-upload-id", "data-video-id", "videoUploadId", "video_upload_id")
    elif object_type == "native_audio":
        keys = ("mediaUploadId", "media_upload_id", "media-upload-id", "data-audio-id", "audioUploadId", "audio_upload_id")
    else:
        keys = ("video_upload_id", "videoUploadId", "data-video-id")
    return embedded_metadata_value(raw, keys)
'''
    patch_once(path, old_identity, new_identity, "extract native-audio media identity")
    patch_once(
        path,
        'media_identity = native_media_identity(raw, object_type) if object_type in {"native_video", "substack_video_post_embed"} else None',
        'media_identity = native_media_identity(raw, object_type) if object_type in {"native_video", "native_audio", "substack_video_post_embed"} else None',
        "inventory native-audio media identity",
    )


def patch_profile(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    objects = data.setdefault("native_objects", {})
    expected = {
        "strategy": "manual_native_if_present",
        "status": "conservative_manual_until_destination_test",
        "archival_rule": "preserve_exact_source_island",
        "clipboard_rule": "exclude_native_audio_markup_and_reinsert_from_original_editor",
        "placement_evidence": ["source_sha256", "upload_or_media_id", "preceding_anchor", "following_anchor"],
    }
    if objects.get("native_audio") != expected:
        objects["native_audio"] = expected
        print("patched: compatibility profile native_audio")
    invariants = data.setdefault("locked_invariants", [])
    rule = "native Substack-uploaded audio remains exact in archival source, is omitted from clipboard payloads, and is manually reinserted at recorded anchors until destination transfer is proven"
    if rule not in invariants:
        invariants.append(rule)
    if "native audio" not in data.get("profile_name", "").lower():
        data["profile_name"] = data.get("profile_name", "Opera local-file native-object helper") + " + conservative manual native audio"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def patch_generator(path: Path) -> None:
    patch_once(
        path,
        'if object_type in {"native_video", "substack_video_post_embed"}\n            else None',
        'if object_type in {"native_video", "native_audio", "substack_video_post_embed"}\n            else None',
        "source_objects native-audio media identity",
    )

    old_manual = '''        elif strategy == "manual_native_if_present":
            manual_steps.append({
                "kind": "manual_native_object",
                "object_id": obj["id"],
                "type": obj["type"],
                "instruction": "Insert or verify the native Substack paywall at the recorded source anchors after pasting.",
                "preceding_anchor": obj.get("preceding_anchor"),
                "following_anchor": obj.get("following_anchor"),
                "source_sha256": obj["source_sha256"],
            })
'''
    new_manual = '''        elif strategy == "manual_native_if_present":
            if obj["type"] == "native_audio":
                instruction = (
                    "Copy this native Substack-uploaded audio directly from the original Substack editor, "
                    "then insert it at the recorded source anchors after pasting the article parts. "
                    "Native audio markup is excluded from the clipboard payload."
                )
            elif obj["type"] == "paywall":
                instruction = "Insert or verify the native Substack paywall at the recorded source anchors after pasting."
            else:
                instruction = "Insert or verify this native Substack object at the recorded source anchors after pasting."
            manual_steps.append({
                "kind": "manual_native_object",
                "object_id": obj["id"],
                "type": obj["type"],
                "instruction": instruction,
                "preceding_anchor": obj.get("preceding_anchor"),
                "following_anchor": obj.get("following_anchor"),
                "source_sha256": obj["source_sha256"],
                "media_id": pobj.get("media_id") or obj.get("media_id"),
            })
'''
    patch_once(path, old_manual, new_manual, "type-specific manual native-audio instruction")

    old_video_check = '''        if "native-video-embed" in payload.lower() or "videoembedplayer" in payload.lower():
            raise ValueError(f"Segment {segment['index']} contains forbidden native uploaded-video markup")
'''
    new_media_check = '''        if "native-video-embed" in payload.lower() or "videoembedplayer" in payload.lower():
            raise ValueError(f"Segment {segment['index']} contains forbidden native uploaded-video markup")
        if "native-audio-embed" in payload.lower() or "audioembedplayer" in payload.lower():
            raise ValueError(f"Segment {segment['index']} contains forbidden native uploaded-audio markup")
'''
    patch_once(path, old_video_check, new_media_check, "verify native audio omitted from clipboard payload")


def run_audio_selftest(repo: Path) -> None:
    helper = repo / "project-sources" / "substack_transfer_helper.py.txt"
    compat = repo / "project-sources" / "CONFIRMED-SUBSTACK-HELPER.json"
    fixture = (
        '<div dir="auto" class="body markup">'
        '<h2>Before audio</h2><p>A</p>'
        '<div class="native-audio-embed" data-attrs="{&quot;mediaUploadId&quot;:&quot;audio-1&quot;}">'
        '<div data-component-name="AudioEmbedPlayer"><audio src="/api/v1/audio/upload/audio-1/src"></audio></div></div>'
        '<p>B</p><h2>After audio</h2></div>'
    )
    with tempfile.TemporaryDirectory(prefix="substack-native-audio-selftest-") as tmp:
        root = Path(tmp)
        source = root / "fixture.html"
        plan = root / "plan.json"
        inventory = root / "inventory.json"
        out = root / "helper.html"
        report = root / "report.md"
        source.write_text(fixture, encoding="utf-8")
        base = [sys.executable, str(helper)]
        subprocess.run(base + ["init", str(source), "--plan", str(plan), "--inventory", str(inventory), "--compat-profile", str(compat)], check=True)
        plan_data = json.loads(plan.read_text(encoding="utf-8"))
        objects = plan_data["objects"]
        if len(objects) != 1 or objects[0]["type"] != "native_audio" or objects[0]["strategy"] != "manual_native_if_present":
            raise AssertionError(f"native audio plan mismatch: {objects}")
        subprocess.run(base + ["build", str(source), "--plan", str(plan), "--compat-profile", str(compat), "--out", str(out), "--report", str(report)], check=True)
        subprocess.run(base + ["verify", str(source), "--plan", str(plan), "--compat-profile", str(compat), "--helper", str(out)], check=True)
        helper_text = out.read_text(encoding="utf-8")
        if "native Substack-uploaded audio" not in helper_text:
            raise AssertionError("helper lacks explicit native-audio manual insertion instruction")
        manifest_marker = '<script id="hva-transfer-manifest" type="application/json">'
        if manifest_marker not in helper_text:
            raise AssertionError("helper manifest missing")
    print("native-audio conservative transfer self-test: PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.expanduser().resolve()
    parser_path = repo / "project-sources" / "html_islands.py.txt"
    profile_path = repo / "project-sources" / "CONFIRMED-SUBSTACK-HELPER.json"
    generator_path = repo / "project-sources" / "substack_transfer_helper.py.txt"
    for path in (parser_path, profile_path, generator_path):
        if not path.is_file():
            raise FileNotFoundError(path)
    patch_parser(parser_path)
    patch_profile(profile_path)
    patch_generator(generator_path)
    run_audio_selftest(repo)
    print("Canonical helper files now have conservative native-audio manual-insertion support in this worktree.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
