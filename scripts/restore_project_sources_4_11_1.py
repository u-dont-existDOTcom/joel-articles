#!/usr/bin/env python3
"""Restore and verify the owner-supplied 4.11.1 Project Source baseline.

Example:
    python scripts/restore_project_sources_4_11_1.py \
        --zip /path/to/Joel-Articles-4.11.1-Project-Sources.zip

The migration is intentionally conservative: it accepts only the exact
owner-supplied ZIP, archives all 40 historical members byte-for-byte, restores
only the 31 members without newer active successors, and refuses to overwrite
any differing active or archived payload.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Restore or verify the exact owner-supplied 4.11.1 Project Source "
            "snapshot without replacing newer active sources."
        )
    )
    parser.add_argument(
        "--zip",
        required=True,
        type=Path,
        help="path to the exact Joel-Articles-4.11.1-Project-Sources.zip",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the completed archive and active restoration without writing",
    )
    return parser.parse_args()


def load_zip(zip_path: Path) -> tuple[bytes, str, dict[str, bytes]]:
    if not zip_path.is_file():
        fail(f"ZIP does not exist or is not a file: {zip_path}")

    zip_bytes = zip_path.read_bytes()
    actual_zip_sha = sha256(zip_bytes)
    if actual_zip_sha != EXPECTED_ZIP_SHA256:
        fail(f"ZIP SHA-256 mismatch: expected {EXPECTED_ZIP_SHA256}, got {actual_zip_sha}")

    try:
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            infos = zf.infolist()
            if len(infos) != EXPECTED_COUNT:
                fail(f"Expected exactly {EXPECTED_COUNT} ZIP entries, found {len(infos)}")
            if any(info.is_dir() for info in infos):
                fail("ZIP contains a directory entry; only the exact 40 files are allowed")

            names = [info.filename for info in infos]
            if len(names) != len(set(names)):
                fail("ZIP contains duplicate filenames")
            if set(names) != EXPECTED_NAMES:
                missing = sorted(EXPECTED_NAMES - set(names))
                extra = sorted(set(names) - EXPECTED_NAMES)
                fail(f"Inventory mismatch; missing={missing}; extra={extra}")

            bad = zf.testzip()
            if bad:
                fail(f"ZIP CRC failure at {bad}")
            source_bytes = {name: zf.read(name) for name in names}
    except zipfile.BadZipFile as exc:
        fail(f"Invalid ZIP: {exc}")

    return zip_bytes, actual_zip_sha, source_bytes


def build_manifest(actual_zip_sha: str, source_bytes: dict[str, bytes]) -> dict[str, object]:
    files = []
    for name in sorted(source_bytes):
        data = source_bytes[name]
        superseded = name in SUPERSEDED
        active_destination = None
        disposition = "archive_only_superseded_by_newer_active_content"
        if not superseded:
            active_destination = (ACTIVE / active_name(name)).relative_to(ROOT).as_posix()
            disposition = "restored_active_and_archived"

        files.append(
            {
                "original_filename": name,
                "bytes": len(data),
                "sha256": sha256(data),
                "archive_path": (ARCHIVE / "sources" / name).relative_to(ROOT).as_posix(),
                "active_destination": active_destination,
                "disposition": disposition,
                "superseded_by_newer_active_content": superseded,
            }
        )

    return {
        "format": "joel-articles-project-source-snapshot-v1",
        "version": "4.11.1",
        "owner_supplied_date": "2026-08-17",
        "zip_sha256": actual_zip_sha,
        "historical_file_count": len(files),
        "restored_active_count": sum(
            file["active_destination"] is not None for file in files
        ),
        "superseded_archive_only_count": sum(
            file["superseded_by_newer_active_content"] for file in files
        ),
        "authority_note": "Newer active Project/GitHub versions supersede same-named 4.11.1 files. This snapshot is rollback/provenance evidence, not article authority.",
        "files": files,
    }


def build_readme(actual_zip_sha: str, manifest: dict[str, object]) -> str:
    return f"""# Joel Articles Project Source snapshot — 4.11.1

This directory preserves the exact owner-supplied pre-deletion Project Source package recovered on 2026-08-17.

- Exact ZIP SHA-256: `{actual_zip_sha}`
- Historical source count: `{manifest['historical_file_count']}`
- Restored active sources: `{manifest['restored_active_count']}`
- Archive-only sources superseded by newer active versions: `{manifest['superseded_archive_only_count']}`

The archive is noncanonical historical evidence. Current root skill/map, current `project-sources/`, and registered article authority control active work.

`VOICE-REFERENCE(1).md` retains its exact historical filename in this snapshot; its restored active path is `project-sources/VOICE-REFERENCE.md`.
"""


def build_sha256sums(actual_zip_sha: str, source_bytes: dict[str, bytes]) -> str:
    lines = [f"{actual_zip_sha}  Joel-Articles-4.11.1-Project-Sources.zip"]
    lines.extend(
        f"{sha256(source_bytes[name])}  sources/{name}" for name in sorted(source_bytes)
    )
    return "\n".join(lines) + "\n"


def require_same_if_present(path: Path, expected: bytes, description: str) -> None:
    if not path.exists():
        return
    if not path.is_file():
        fail(f"Expected a file at {path.relative_to(ROOT)}")
    if path.read_bytes() != expected:
        fail(f"Refusing to overwrite differing {description} at {path.relative_to(ROOT)}")


def verify_preconditions(zip_bytes: bytes, source_bytes: dict[str, bytes]) -> None:
    require_same_if_present(
        ARCHIVE / "Joel-Articles-4.11.1-Project-Sources.zip",
        zip_bytes,
        "archived ZIP",
    )
    for name, data in source_bytes.items():
        require_same_if_present(ARCHIVE / "sources" / name, data, "archived source")
        target = ACTIVE / active_name(name)
        if name in SUPERSEDED:
            if not target.is_file():
                fail(f"Expected newer active successor is missing: {target.relative_to(ROOT)}")
        else:
            require_same_if_present(target, data, "active source")


def expected_outputs(
    zip_bytes: bytes,
    actual_zip_sha: str,
    source_bytes: dict[str, bytes],
    manifest: dict[str, object],
) -> dict[Path, bytes]:
    outputs = {
        ARCHIVE / "Joel-Articles-4.11.1-Project-Sources.zip": zip_bytes,
        ARCHIVE / "MANIFEST.json": (
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
        ).encode("utf-8"),
        ARCHIVE / "README.md": build_readme(actual_zip_sha, manifest).encode("utf-8"),
        ARCHIVE / "SHA256SUMS.txt": build_sha256sums(
            actual_zip_sha, source_bytes
        ).encode("utf-8"),
    }
    for name, data in source_bytes.items():
        outputs[ARCHIVE / "sources" / name] = data
        if name not in SUPERSEDED:
            outputs[ACTIVE / active_name(name)] = data
    return outputs


def write_or_check(outputs: dict[Path, bytes], check: bool) -> None:
    for path, expected in outputs.items():
        if check:
            if not path.is_file():
                fail(f"Required output is missing: {path.relative_to(ROOT)}")
            if path.read_bytes() != expected:
                fail(f"Output differs from expected bytes: {path.relative_to(ROOT)}")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_bytes() != expected:
            path.write_bytes(expected)


def main() -> int:
    args = parse_args()
    zip_bytes, actual_zip_sha, source_bytes = load_zip(args.zip)
    manifest = build_manifest(actual_zip_sha, source_bytes)
    if manifest["historical_file_count"] != 40:
        fail("Internal count error: historical source count is not 40")
    if manifest["restored_active_count"] != 31:
        fail("Internal count error: restored active source count is not 31")
    if manifest["superseded_archive_only_count"] != 9:
        fail("Internal count error: superseded archive-only count is not 9")

    verify_preconditions(zip_bytes, source_bytes)
    outputs = expected_outputs(zip_bytes, actual_zip_sha, source_bytes, manifest)
    write_or_check(outputs, args.check)

    print(json.dumps({
        "status": "pass",
        "mode": "check" if args.check else "restore",
        "zip_sha256": actual_zip_sha,
        "historical": manifest["historical_file_count"],
        "restored_active": manifest["restored_active_count"],
        "archive_only_superseded": manifest["superseded_archive_only_count"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
