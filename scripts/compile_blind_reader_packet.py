#!/usr/bin/env python3
"""Compile an exact source file into sequential blind-reader windows.

The compiler is intentionally editorially dumb. It verifies the exact source
bytes, splits them into contiguous line windows, hashes every window, and
writes a deterministic manifest. It does not inspect article meaning or
produce reader questions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compile_packet(
    source: Path,
    out_dir: Path,
    *,
    expected_sha256: str,
    lines_per_window: int = 90,
) -> dict[str, object]:
    if lines_per_window < 1:
        raise ValueError("lines_per_window must be >= 1")
    if len(expected_sha256) != 64 or any(ch not in "0123456789abcdef" for ch in expected_sha256):
        raise ValueError("expected_sha256 must be a lowercase 64-character SHA-256")

    source_bytes = source.read_bytes()
    observed_sha256 = sha256_bytes(source_bytes)
    if observed_sha256 != expected_sha256:
        raise ValueError(
            f"source SHA-256 mismatch: expected {expected_sha256}, observed {observed_sha256}"
        )

    # Fail before mutating the destination if the source is not UTF-8 text.
    source_bytes.decode("utf-8")
    lines = source_bytes.splitlines(keepends=True)
    if not lines and source_bytes:
        lines = [source_bytes]

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    windows: list[dict[str, object]] = []
    reconstructed = bytearray()

    for index, start in enumerate(range(0, len(lines), lines_per_window), start=1):
        chunk_lines = lines[start : start + lines_per_window]
        chunk = b"".join(chunk_lines)
        start_line = start + 1
        end_line = start + len(chunk_lines)
        filename = f"window-{index:03d}-lines-{start_line:04d}-{end_line:04d}.md"
        (out_dir / filename).write_bytes(chunk)
        reconstructed.extend(chunk)
        windows.append(
            {
                "index": index,
                "filename": filename,
                "start_line": start_line,
                "end_line": end_line,
                "line_count": len(chunk_lines),
                "byte_count": len(chunk),
                "sha256": sha256_bytes(chunk),
            }
        )

    reconstructed_bytes = bytes(reconstructed)
    if reconstructed_bytes != source_bytes:
        raise RuntimeError("internal coverage failure: concatenated windows do not reproduce source bytes")

    manifest: dict[str, object] = {
        "schema_version": 1,
        "mode": "sequential-blind-reader-packet",
        "source": {
            "path": source.as_posix(),
            "expected_sha256": expected_sha256,
            "observed_sha256": observed_sha256,
            "byte_count": len(source_bytes),
            "line_count": len(lines),
        },
        "windowing": {
            "lines_per_window": lines_per_window,
            "window_count": len(windows),
            "coverage": "exact-contiguous-nonoverlapping",
            "reconstructed_sha256": sha256_bytes(reconstructed_bytes),
        },
        "windows": windows,
        "reader_isolation": {
            "rule": "Reveal exactly one window at a time. Do not give the reader access to unrevealed windows, the source file, GitHub, prior audits, or sibling experiment files.",
            "full_hindsight_allowed_after_window": len(windows),
        },
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--lines-per-window", type=int, default=90)
    args = parser.parse_args(argv)

    try:
        manifest = compile_packet(
            args.source,
            args.out_dir,
            expected_sha256=args.expected_sha256,
            lines_per_window=args.lines_per_window,
        )
    except (OSError, UnicodeError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        "Compiled blind-reader packet: "
        f"{manifest['windowing']['window_count']} window(s), "
        f"source SHA-256 {manifest['source']['observed_sha256']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
