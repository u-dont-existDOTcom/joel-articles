#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_semantic_restore_r7 as r7

SOURCE_MASTER_SHA = "00698c96b42b5f4a24ea1078c6fbcb8ff068a403720d3bc38e091e1656db8c3c"
SOURCE_P1_SHA = "35dea0c3fc5e1723a3d8d1f0c8192447525758dfb953910e1e0d353ae3dcf4d9"
SOURCE_P2_SHA = "c7f96beaae57d7f9e70502ae5869cd592d5753746c7e3ac07f0f8842a6d44d06"

MALE_OLD = "The moment I have to prove that I’m the man, something has already become fake."
MALE_NEW = MALE_OLD + " Then I have to defend the identity every time I hesitate, cry, need help, or get something wrong."

FEMALE_OLD = "The same is true for a woman. She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine."
FEMALE_NEW = FEMALE_OLD + " Surrender means so much more when she could take control but prefers not to at that moment."

R8_REQUIREMENTS = {
    "performance-identity-defense": "Then I have to defend the identity every time I hesitate, cry, need help, or get something wrong.",
    "performance-chosen-surrender": "Surrender means so much more when she could take control but prefers not to at that moment.",
}


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


def semantic_audit(source: str, candidate: str) -> dict[str, object]:
    checks = r7.semantic_audit(source, candidate)
    missing_r8 = [name for name, anchor in R8_REQUIREMENTS.items() if anchor not in candidate]
    missing_owner = [name for name, anchor in r7.OWNER_AUTHORITY_ANCHORS.items() if anchor not in candidate]
    checks["r8_semantic_required_missing"] = missing_r8
    checks["owner_authority_missing"] = sorted(set(checks.get("owner_authority_missing", [])) | set(missing_owner))
    checks["passed"] = bool(checks["passed"]) and not missing_r8 and not checks["owner_authority_missing"]
    return checks


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

    master2 = master
    part2_2 = part2
    mops: list[dict[str, object]] = []
    pops: list[dict[str, object]] = []

    for label, old, new in [
        ("not-performance-identity-defense-r8", MALE_OLD, MALE_NEW),
        ("not-performance-chosen-surrender-r8", FEMALE_OLD, FEMALE_NEW),
    ]:
        master2, op = replace_exact(master2, label, old, new)
        mops.append(op)
        part2_2, op = replace_exact(part2_2, label, old, new)
        pops.append(op)

    if sha256_text(part1) != SOURCE_P1_SHA:
        raise RuntimeError("Part 1 changed during r8 Part 2 semantic restoration")

    checks = semantic_audit(master, master2)
    if not checks["passed"]:
        raise RuntimeError(f"r8 semantic invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (args.output_dir / "candidate-part-1.txt").write_text(part1, encoding="utf-8")
    (args.output_dir / "candidate-part-2.txt").write_text(part2_2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "whole_article_semantic_restoration_r8_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {
                "sha256": sha256_text(master2),
                "word_count_whitespace": len(master2.split()),
                "operations": mops,
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
                "operations": pops,
            },
        },
        "traceability": {
            "registered_lost_units_corrected_total": 9,
            "restored_in_r7": 7,
            "restored_in_r8": 2,
            "remaining_known_unsuperseded_lost_units": 0,
            "r7_correction_note": "SEMANTIC-FIDELITY-R7-ADDENDUM-20260821.md",
            "owner_authority_spans_preserved": True,
        },
        "detector_plan": {
            "status": "do_not_dispatch_until_final_registered_to_r8_traceability_passes",
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
