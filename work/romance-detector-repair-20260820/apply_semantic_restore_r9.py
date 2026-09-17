#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_semantic_restore_r8 as r8

SOURCE_MASTER_SHA = "184b37c612c78d565c4c1a23691f38e0c0ceb2e7d9041ef1c98adee3ce48961f"
SOURCE_P1_SHA = "35dea0c3fc5e1723a3d8d1f0c8192447525758dfb953910e1e0d353ae3dcf4d9"
SOURCE_P2_SHA = "9b1fbe32be4429baddbda636d2eb8861d5cc7163fa8bee764dc235502c027005"

OLD = "Surrender means so much more when she could take control but prefers not to at that moment."
NEW = OLD + " When a strong woman surrenders, she is choosing to, which is sexy."
REQUIRED = "When a strong woman surrenders, she is choosing to, which is sexy."


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
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-master", type=Path, required=True)
    parser.add_argument("--source-part1", type=Path, required=True)
    parser.add_argument("--source-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.source_master.read_text(encoding="utf-8")
    part1 = args.source_part1.read_text(encoding="utf-8")
    part2 = args.source_part2.read_text(encoding="utf-8")
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

    master2, mop = replace_exact(master, "not-performance-erotic-value-r9", OLD, NEW)
    part2_2, pop = replace_exact(part2, "not-performance-erotic-value-r9", OLD, NEW)
    if sha256_text(part1) != SOURCE_P1_SHA:
        raise RuntimeError("Part 1 changed during r9 Part 2 semantic restoration")

    checks = r8.semantic_audit(master, master2)
    checks["r9_erotic_value_present"] = REQUIRED in master2
    checks["passed"] = bool(checks["passed"]) and checks["r9_erotic_value_present"]
    if not checks["passed"]:
        raise RuntimeError(f"r9 semantic invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (args.output_dir / "candidate-part-1.txt").write_text(part1, encoding="utf-8")
    (args.output_dir / "candidate-part-2.txt").write_text(part2_2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "whole_article_semantic_restoration_r9_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {
                "sha256": sha256_text(master2),
                "word_count_whitespace": len(master2.split()),
                "operations": [mop],
                "semantic_invariant_audit": checks,
            },
            "part1": {
                "sha256": sha256_text(part1),
                "word_count_whitespace": len(part1.split()),
                "operations": [],
                "unchanged_from_semantic_r6": True,
            },
            "part2": {
                "sha256": sha256_text(part2_2),
                "word_count_whitespace": len(part2_2.split()),
                "operations": [pop],
            },
        },
        "traceability": {
            "registered_lost_units_corrected_total": 10,
            "restored_in_r7": 7,
            "restored_in_r8": 2,
            "restored_in_r9": 1,
            "remaining_known_unsuperseded_lost_units": 0,
            "r8_correction_note": "SEMANTIC-FIDELITY-R8-ADDENDUM-20260821.md",
            "owner_authority_spans_preserved": True,
        },
        "detector_plan": {
            "status": "do_not_dispatch_until_final_registered_to_r9_traceability_passes",
            "part1_affection_local": "hard-capped 6/6; no more local calls",
            "part2_paid_baseline": "recover exact already-reserved owner-integrated-r2 result; never resubmit duplicate",
        },
    }
    (args.output_dir / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
