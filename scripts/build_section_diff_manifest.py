#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Section:
    ordinal: int
    level: int
    heading: str
    marker: str
    text: str


def split_sections(text: str) -> tuple[str, list[Section]]:
    lines = text.splitlines(keepends=True)
    starts: list[tuple[int, int, str, str]] = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.rstrip("\n"))
        if m:
            starts.append((i, len(m.group(1)), m.group(2), m.group(0)))
    if not starts:
        return text, []
    preamble = "".join(lines[: starts[0][0]])
    sections: list[Section] = []
    for ordinal, (start, level, heading, marker) in enumerate(starts):
        end = starts[ordinal + 1][0] if ordinal + 1 < len(starts) else len(lines)
        sections.append(Section(ordinal, level, heading, marker, "".join(lines[start:end])))
    return preamble, sections


def manifest(source: str, candidate: str) -> dict[str, object]:
    source_preamble, source_sections = split_sections(source)
    candidate_preamble, candidate_sections = split_sections(candidate)
    source_signature = [(s.level, s.heading) for s in source_sections]
    candidate_signature = [(s.level, s.heading) for s in candidate_sections]
    if source_signature != candidate_signature:
        raise RuntimeError("heading sequence differs; section alignment is unsafe")
    rows: list[dict[str, object]] = []
    if source_preamble != candidate_preamble:
        rows.append({
            "ordinal": -1,
            "level": 0,
            "heading": "<preamble>",
            "source_sha256": sha256_text(source_preamble),
            "candidate_sha256": sha256_text(candidate_preamble),
            "source_words": len(source_preamble.split()),
            "candidate_words": len(candidate_preamble.split()),
        })
    for old, new in zip(source_sections, candidate_sections):
        if old.text == new.text:
            continue
        rows.append({
            "ordinal": old.ordinal,
            "level": old.level,
            "heading": old.heading,
            "source_sha256": sha256_text(old.text),
            "candidate_sha256": sha256_text(new.text),
            "source_words": len(old.text.split()),
            "candidate_words": len(new.text.split()),
        })
    return {
        "schema_version": 1,
        "alignment": "exact_markdown_heading_sequence",
        "source_sha256": sha256_text(source),
        "candidate_sha256": sha256_text(candidate),
        "heading_count": len(source_sections),
        "changed_section_count": len(rows),
        "changed_sections": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a deterministic changed-section manifest for two Markdown article realizations.")
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = manifest(args.source.read_text(encoding="utf-8"), args.candidate.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
