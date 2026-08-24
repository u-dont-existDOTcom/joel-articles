#!/usr/bin/env python3
"""Materialize Romance r23r2 from the exact measured r23 evidence files.

This tool performs no detector or network action. It accepts the checked-out
`work/romance-r23-gui-20260824-a` directory from the Pangram evidence branch,
verifies all three r23 identities, and changes only Joel's owner-final Two
Pillars realization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work/romance-r22-reconciliation-20260823"
OUT = WORK / "materialized-r23r2-owner-final"

SOURCE_REPOSITORY = "u-dont-existDOTcom/pangram-humanization-lab"
SOURCE_REF = "evidence/romance-r23-gui-20260824-a"
SOURCE_COMMIT = "f4f2d6404e7362441c9ac0969dfc79313bea6ba1"

R23_MASTER_SHA = "322953b5d6f6ad49f7a3b41e5c6795b36404508f7768669cdcc72223f2f21a0d"
R23_PART1_SHA = "620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b"
R23_PART2_SHA = "a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3"
R23_MASTER_WORDS = 20364
R23_PART1_WORDS = 10296
R23_PART2_WORDS = 9917

R23_TWO_PILLARS = (
    "Maybe an unusually strong couple can get away without much community. "
    "I think that's rare. Community isn't magic either; if both people are "
    "falling apart, there is only so much anyone else can do.\n\n"
    "But sometimes a friend who actually knows us both sees the pattern before "
    "either of us does."
)

R23R2_TWO_PILLARS = (
    "Maybe an unusually strong couple can get away without much community. "
    "I think that's rare.  But sometimes a friend who actually knows us both "
    "sees the pattern before either of us does. On the other hand, If both "
    "people are falling apart, there is only so much anyone else can do."
)

OWNER_FINAL_TEXT_SHA = "cd8de93fda39fcdf13c4b1f6ba2f9250c11c40f8c8298f281055e37bafed6291"
EXPECTED_NATIVE_OBJECTS = 11
EXPECTED_MARKDOWN_LINKS = 22

PROTECTED_ANCHORS = [
    "Sex is what you do when you are older and you find a friend you want to have children with.",
    "[Gandarussa](https://thediplomat.com/2013/09/a-male-contraceptive-pill-for-indonesia/)",
    "Never recruit children into the adult war.",
    "It might be that I wrote this whole article for my son, Bear",
    "I believe Rumi was right: A sacred relationship will open and purify your hearts regardless of whether it ends.",
]


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_text(text: str) -> str:
    return sha_bytes(text.encode("utf-8"))


def words(text: str) -> int:
    return len(text.split())


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exact r23 span once, found {count}")
    candidate = text.replace(old, new, 1)
    if old in candidate:
        raise SystemExit(f"{label}: superseded r23 span remains after replacement")
    if candidate.count(new) != 1:
        raise SystemExit(f"{label}: owner-final r23r2 span is not unique")
    return candidate


def extract(text: str, start: str, end: str) -> str:
    first = text.index(start)
    last = text.index(end, first)
    return text[first:last].rstrip() + "\n"


def verify_source(path: Path, expected_sha: str, expected_words: int, label: str) -> str:
    data = path.read_bytes()
    actual_sha = sha_bytes(data)
    if actual_sha != expected_sha:
        raise SystemExit(f"{label}: SHA mismatch {actual_sha} != {expected_sha}")
    text = data.decode("utf-8")
    actual_words = words(text)
    if actual_words != expected_words:
        raise SystemExit(f"{label}: word mismatch {actual_words} != {expected_words}")
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-dir",
        required=True,
        type=Path,
        help="Path to work/romance-r23-gui-20260824-a on the exact evidence branch",
    )
    args = parser.parse_args()
    source = args.source_dir.resolve()

    master_path = source / "candidate-master.md"
    part1_path = source / "candidate-part-1.txt"
    part2_path = source / "candidate-part-2.txt"

    r23_master = verify_source(master_path, R23_MASTER_SHA, R23_MASTER_WORDS, "r23 master")
    r23_part1 = verify_source(part1_path, R23_PART1_SHA, R23_PART1_WORDS, "r23 Part 1")
    r23_part2 = verify_source(part2_path, R23_PART2_SHA, R23_PART2_WORDS, "r23 Part 2")

    if sha_text(R23R2_TWO_PILLARS) != OWNER_FINAL_TEXT_SHA:
        raise SystemExit("owner-final Two Pillars frozen-text SHA mismatch")
    if R23_TWO_PILLARS in r23_part1 or R23R2_TWO_PILLARS in r23_part1:
        raise SystemExit("Two Pillars realization unexpectedly appears in r23 Part 1")

    candidate_master = replace_once(r23_master, R23_TWO_PILLARS, R23R2_TWO_PILLARS, "master")
    candidate_part2 = replace_once(r23_part2, R23_TWO_PILLARS, R23R2_TWO_PILLARS, "Part 2")

    headings_source = [line for line in r23_master.splitlines() if line.startswith("#")]
    headings_candidate = [line for line in candidate_master.splitlines() if line.startswith("#")]
    if headings_source != headings_candidate:
        raise SystemExit("heading order/content changed")

    native_source = r23_master.count("[NATIVE ")
    native_candidate = candidate_master.count("[NATIVE ")
    if native_source != EXPECTED_NATIVE_OBJECTS or native_candidate != EXPECTED_NATIVE_OBJECTS:
        raise SystemExit(
            f"native object count mismatch source={native_source} candidate={native_candidate}"
        )

    link_re = re.compile(r"\[[^\]]+\]\([^\)]+\)")
    links_source = len(link_re.findall(r23_master))
    links_candidate = len(link_re.findall(candidate_master))
    if links_source != EXPECTED_MARKDOWN_LINKS or links_candidate != EXPECTED_MARKDOWN_LINKS:
        raise SystemExit(
            f"Markdown link count mismatch source={links_source} candidate={links_candidate}"
        )

    missing = [anchor for anchor in PROTECTED_ANCHORS if anchor not in candidate_master]
    if missing:
        raise SystemExit(f"protected anchors missing: {missing}")

    if not candidate_part2.startswith('Key at first asked me innocently, "Can you be my guru?"'):
        raise SystemExit("Part 2 start boundary changed")
    if 'Key at first asked me innocently, "Can you be my guru?"' in r23_part1:
        raise SystemExit("Part 2 content leaked into Part 1")

    two_pillars = extract(
        candidate_master,
        "# Two Pillars Don't Hold The Roof Up",
        "# What are you actually choosing together?",
    )

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "candidate-master.md").write_text(candidate_master, encoding="utf-8")
    shutil.copyfile(part1_path, OUT / "candidate-part-1.txt")
    (OUT / "candidate-part-2.txt").write_text(candidate_part2, encoding="utf-8")
    (OUT / "boundary-two-pillars.txt").write_text(two_pillars, encoding="utf-8")

    output_paths = {
        "master": OUT / "candidate-master.md",
        "part1": OUT / "candidate-part-1.txt",
        "part2": OUT / "candidate-part-2.txt",
        "two_pillars": OUT / "boundary-two-pillars.txt",
    }
    candidate = {
        name: {
            "path": str(path.relative_to(ROOT)),
            "sha256": sha_bytes(path.read_bytes()),
            "word_count_whitespace": words(path.read_text(encoding="utf-8")),
        }
        for name, path in output_paths.items()
    }

    if candidate["part1"]["sha256"] != R23_PART1_SHA:
        raise SystemExit("r23r2 Part 1 is not byte-identical to r23 Part 1")
    if candidate["master"]["word_count_whitespace"] != R23_MASTER_WORDS:
        raise SystemExit("unexpected r23r2 master word-count change")
    if candidate["part2"]["word_count_whitespace"] != R23_PART2_WORDS:
        raise SystemExit("unexpected r23r2 Part-2 word-count change")

    manifest = {
        "format": "romance-r23r2-owner-final-materialization-v1",
        "candidate_id": "romance-r23r2-owner-final-20260824",
        "source": {
            "repository": SOURCE_REPOSITORY,
            "ref": SOURCE_REF,
            "commit": SOURCE_COMMIT,
            "master": {"sha256": R23_MASTER_SHA, "word_count_whitespace": R23_MASTER_WORDS},
            "part1": {"sha256": R23_PART1_SHA, "word_count_whitespace": R23_PART1_WORDS},
            "part2": {"sha256": R23_PART2_SHA, "word_count_whitespace": R23_PART2_WORDS},
        },
        "authorized_delta": {
            "id": "R23R2-01",
            "scope": "Two Pillars local realization only",
            "old_sha256": sha_text(R23_TWO_PILLARS),
            "new_sha256": sha_text(R23R2_TWO_PILLARS),
            "new_text": R23R2_TWO_PILLARS,
            "owner_authority": "Joel direct correction and owner-reported Human/low-confidence test accepted as good enough on 2026-08-24",
            "older_r23r1_four_word_deletion_applied": False,
            "r23r1_r03_fallback_applied": False,
        },
        "candidate": candidate,
        "invariants": {
            "part1_byte_identical_to_r23": True,
            "headings_exactly_unchanged": True,
            "native_objects": {"source": native_source, "candidate": native_candidate},
            "markdown_links": {"source": links_source, "candidate": links_candidate},
            "protected_anchors_missing": [],
            "unexplained_substantive_deltas": 0,
        },
        "detector": {
            "new_run_performed": False,
            "owner_report": "Exact r23r2 Two Pillars wording tested Human, low confidence, and explicitly accepted as good enough.",
            "full_part2_recertification_required_before_working-master_promotion": False,
        },
    }
    (OUT / "materialization.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
