#!/usr/bin/env python3
"""Restore the owner-supplied 4.11.1 Project Source baseline losslessly.

This migration is intentionally conservative:
- reconstruct the exact owner-supplied ZIP from staged base64 chunks;
- verify the ZIP SHA-256 and exact 40-file inventory;
- archive every historical file byte-for-byte;
- restore only historical files that do not have a newer active replacement;
- never overwrite a newer active source;
- preserve the odd historical VOICE-REFERENCE(1).md name in the archive while
  restoring it canonically as project-sources/VOICE-REFERENCE.md.
"""
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
import shutil
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT / ".migration" / "4.11.1"
ARCHIVE = ROOT / "archive" / "project-source-snapshots" / "4.11.1"
ACTIVE = ROOT / "project-sources"
EXPECTED_ZIP_SHA256 = "c0b6b0ce4d95b303a00cc44d75fdf54e4433fa72e39e9e866c84b856fde965b1"
EXPECTED_COUNT = 40

SUPERSEDED = {
    "ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md",
    "ARGUMENT-LEDGER-QUICKSTART.md",
    "ARTIFACT-FAMILY-LEDGER-TEMPLATE.md",
    "CANON-FACTS.md",
    "CONFIRMED-SUBSTACK-HELPER.json",
    "INTERLINKING-AND-HTML-SOURCE.md",
    "html_islands.py.txt",
    "review_package.py.txt",
    "substack_transfer_helper.py.txt",
}

EXPECTED_NAMES = {
    "ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md",
    "ARGUMENT-LEDGER-QUICKSTART.md",
    "ARTICLE-INDEX.md",
    "ARTIFACT-FAMILY-LEDGER-TEMPLATE.md",
    "BANNED-PATTERNS.md",
    "CANON-FACTS.md",
    "COMMENT-RESOLUTION-LEDGER-TEMPLATE.md",
    "CONFIRMED-SUBSTACK-HELPER.json",
    "CONTROVERSIAL-TOPIC-EVIDENCE-AUDIT.md",
    "EDIT-CONTRACT-AND-LEDGERS.md",
    "FACTS-HEALTH-FORMATTING.md",
    "FINGERPRINT-PASS.md",
    "HUMANIZATION-AND-COHERENCE.md",
    "INTERLINKING-AND-HTML-SOURCE.md",
    "MASTER-INSTRUCTIONS.md",
    "PROGRESSIVE-DISCLOSURE-EXAMPLES.md",
    "PROJECT-STATE-TEMPLATE.md",
    "QUALITY-FORECAST-AND-PASS-REVIEW.md",
    "REVIEW-INTERFACE-SPEC.md",
    "REVIEW-PACKAGE-REGRESSION.md",
    "REVIEW-WORKFLOW-RULES.md",
    "STRUCTURAL-HUMANITY.md",
    "TASK-MODES.md",
    "TOOLING-IN-PROJECT-SOURCES.md",
    "TRANSFORMATION-CASE-STUDY.md",
    "VISUAL-EDITORIAL-PROTOCOL.md",
    "VOICE-LEXICON.md",
    "VOICE-REFERENCE(1).md",
    "WORKER-CHAT-HANDOFF-RULES.md",
    "argument_ledger.py.txt",
    "cancer-and-research-samples.txt",
    "community-before.txt",
    "html_islands.py.txt",
    "html_publish_modes.py.txt",
    "interactive_review.py.txt",
    "review_interface_browser_test.py.txt",
    "review_interface_template.html.txt",
    "review_package.py.txt",
    "substack_transfer_helper.py.txt",
    "tender-video-transcript.txt",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def active_name(historical_name: str) -> str:
    if historical_name == "VOICE-REFERENCE(1).md":
        return "VOICE-REFERENCE.md"
    return historical_name


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    parts = sorted(STAGE.glob("source.zip.b64.part*"))
    if not parts:
        fail("No staged source.zip.b64.part* files found")
    if not (STAGE / "READY").is_file():
        fail("READY marker is missing")

    encoded = "".join(p.read_text(encoding="ascii").strip() for p in parts)
    try:
        zip_bytes = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        fail(f"Base64 reconstruction failed: {exc}")

    actual_zip_sha = sha256(zip_bytes)
    if actual_zip_sha != EXPECTED_ZIP_SHA256:
        fail(f"ZIP SHA-256 mismatch: expected {EXPECTED_ZIP_SHA256}, got {actual_zip_sha}")

    temp_zip = STAGE / "Joel-Articles-4.11.1-Project-Sources.zip"
    temp_zip.write_bytes(zip_bytes)

    with zipfile.ZipFile(temp_zip) as zf:
        bad = zf.testzip()
        if bad:
            fail(f"ZIP CRC failure at {bad}")
        infos = [i for i in zf.infolist() if not i.is_dir()]
        names = [i.filename for i in infos]
        if len(names) != EXPECTED_COUNT:
            fail(f"Expected {EXPECTED_COUNT} files, found {len(names)}")
        if set(names) != EXPECTED_NAMES:
            missing = sorted(EXPECTED_NAMES - set(names))
            extra = sorted(set(names) - EXPECTED_NAMES)
            fail(f"Inventory mismatch; missing={missing}; extra={extra}")
        source_bytes = {name: zf.read(name) for name in names}

    # Fail closed on any unexpected active collision. Newer superseding files are
    # intentionally untouched; historical missing files must not silently replace
    # independently created current files.
    for name, data in source_bytes.items():
        if name in SUPERSEDED:
            continue
        target = ACTIVE / active_name(name)
        if target.exists() and target.read_bytes() != data:
            fail(f"Unexpected non-identical active collision at {target.relative_to(ROOT)}")

    archive_sources = ARCHIVE / "sources"
    archive_sources.mkdir(parents=True, exist_ok=True)
    ACTIVE.mkdir(parents=True, exist_ok=True)

    manifest_files = []
    for name in sorted(source_bytes):
        data = source_bytes[name]
        archive_target = archive_sources / name
        archive_target.write_bytes(data)

        disposition = "archive_only_newer_active_supersedes"
        active_path = None
        if name not in SUPERSEDED:
            active_target = ACTIVE / active_name(name)
            active_target.write_bytes(data)
            active_path = active_target.relative_to(ROOT).as_posix()
            disposition = "restored_active_and_archived"

        manifest_files.append(
            {
                "historical_name": name,
                "size_bytes": len(data),
                "sha256": sha256(data),
                "archive_path": archive_target.relative_to(ROOT).as_posix(),
                "active_path": active_path,
                "disposition": disposition,
            }
        )

    exact_zip_target = ARCHIVE / "Joel-Articles-4.11.1-Project-Sources.zip"
    exact_zip_target.write_bytes(zip_bytes)

    manifest = {
        "format": "joel-articles-project-source-snapshot-v1",
        "version": "4.11.1",
        "owner_supplied_date": "2026-08-17",
        "zip_sha256": actual_zip_sha,
        "historical_file_count": len(manifest_files),
        "restored_active_count": sum(f["active_path"] is not None for f in manifest_files),
        "superseded_archive_only_count": sum(f["active_path"] is None for f in manifest_files),
        "authority_note": "Newer active Project/GitHub versions supersede same-named 4.11.1 files. This snapshot is rollback/provenance evidence, not article authority.",
        "files": manifest_files,
    }
    (ARCHIVE / "MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    readme = f"""# Joel Articles Project Source snapshot — 4.11.1

This directory preserves the exact owner-supplied pre-deletion Project Source package recovered on 2026-08-17.

- Exact ZIP SHA-256: `{actual_zip_sha}`
- Historical source count: `{len(manifest_files)}`
- Restored active sources: `{manifest['restored_active_count']}`
- Archive-only sources superseded by newer active versions: `{manifest['superseded_archive_only_count']}`

The archive is noncanonical historical evidence. Current root skill/map, current `project-sources/`, and registered article authority control active work.

`VOICE-REFERENCE(1).md` retains its exact historical filename in this snapshot; its restored active path is `project-sources/VOICE-REFERENCE.md`.
"""
    (ARCHIVE / "README.md").write_text(readme, encoding="utf-8")

    # Keep migration tooling reproducible, but remove staged transport bytes so the
    # branch does not retain redundant base64 chunks after the exact ZIP is archived.
    for part in parts:
        part.unlink()
    (STAGE / "READY").unlink(missing_ok=True)
    temp_zip.unlink(missing_ok=True)
    try:
        STAGE.rmdir()
        STAGE.parent.rmdir()
    except OSError:
        pass

    print(json.dumps({
        "status": "pass",
        "zip_sha256": actual_zip_sha,
        "historical": len(manifest_files),
        "restored_active": manifest["restored_active_count"],
        "archive_only_superseded": manifest["superseded_archive_only_count"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
