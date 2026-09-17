#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_part1_repair_r1 as base

SOURCE_MASTER_SHA = "95ae5d3b7d75eac2d79fc57de017d60dfa8088cd46ead69b0dde3a4a1f28e2ba"
SOURCE_P1_SHA = "7f0f9a526506f1cc57b2a20c30f3c7ecaf6d7345fceb9ea8839effdba4c049b6"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

STI_OLD = "You can test for STIs and tell each other what you know. Attachment is less cooperative. Both of you can mean it when you say this is only sex, and then one of you wakes up attached anyway. If you’re both really numb or robotic about sex, maybe not."
STI_NEW = "The STI part is easy: say what you know, or say you don’t know. Feelings aren’t. You can both mean it when you say this is only sex and still have one of you get attached afterward. If you’re both really numb or robotic about sex, maybe not."


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_exact(text: str, label: str, old: str, new: str) -> tuple[str, dict[str, object]]:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
    return text.replace(old, new, 1), {
        "label": label,
        "old_sha256": sha256_text(old),
        "new_sha256": sha256_text(new),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source-master", type=Path, required=True)
    p.add_argument("--source-part1", type=Path, required=True)
    p.add_argument("--source-part2", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    a = p.parse_args()

    master = a.source_master.read_text(encoding="utf-8")
    part1 = a.source_part1.read_text(encoding="utf-8")
    part2 = a.source_part2.read_text(encoding="utf-8")
    observed = {
        "master": sha256_text(master),
        "part1": sha256_text(part1),
        "part2": sha256_text(part2),
    }
    expected = {
        "master": SOURCE_MASTER_SHA,
        "part1": SOURCE_P1_SHA,
        "part2": SOURCE_P2_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"source hash mismatch: expected={expected} observed={observed}")

    master2, m1 = replace_exact(master, "restore-casual-owner-sti-realization", STI_OLD, STI_NEW)
    part1_2, p1 = replace_exact(part1, "restore-casual-owner-sti-realization", STI_OLD, STI_NEW)

    if sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 r5 restoration")

    checks = base.audit(master, master2)
    checks["r5_owner_sti_present"] = STI_NEW in master2
    checks["r5_superseded_sti_absent"] = STI_OLD not in master2
    checks["passed"] = (
        bool(checks["passed"])
        and checks["r5_owner_sti_present"]
        and checks["r5_superseded_sti_absent"]
    )
    if not checks["passed"]:
        raise RuntimeError(f"Part 1 r5 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "part1_owner_wording_restoration_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {
                "sha256": sha256_text(master2),
                "word_count_whitespace": len(master2.split()),
                "operations": [m1],
                "invariant_audit": checks,
            },
            "part1": {
                "sha256": sha256_text(part1_2),
                "word_count_whitespace": len(part1_2.split()),
                "operations": [p1],
            },
            "part2": {
                "sha256": sha256_text(part2),
                "word_count_whitespace": len(part2.split()),
                "operations": [],
                "unchanged": True,
            },
        },
        "selection_rationale": {
            "source_r4_aggregate_human": 0.992400050163269,
            "source_r4_aggregate_ai": 0.007599963806569576,
            "casual_full_r3_human": 1.0,
            "casual_full_r3_text_sha256": "268165f899b11e7e56bffa18d80006d0b322c432a3a409195fe69e407f85061c",
            "casual_r5_interaction_human": 0.7899810671806335,
            "reason": "The complete Casual section had already passed Pangram 4 at 100% Human on section call 3. Aggregate r4 later altered its STI/attachment realization and residual AI reappeared at the section opening. Restore the registered/higher-authority wording that recreates the exact already-passing Casual section instead of spending the sixth local-section call on another paraphrase.",
        },
        "detector_plan": {
            "part1": "fresh exact aggregate measurement; local Casual call 6 remains unused"
        },
    }
    (a.output_dir / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
