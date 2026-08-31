#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_part1_repair_r1 as base

SOURCE_MASTER_SHA = "d205393b1724256416291050fdeb41c18afb9669fddc45cf713559e9ecd9e406"
SOURCE_P1_SHA = "e6b9e546bb2f07af8e18fc65fb6883d27bf0106d93f5f02d6674a88e034d572d"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

AFF_MASTER_OLD = "Kim Anami calls the sexual current between encounters [“the simmer”](https://kimanami.com/meet-another-well-fked-man/). If we stop flirting with each other for months, I’m not going to assume our problem magically begins at bedtime. Sex is a pretty sensitive barometer for resentment, stress, health, medication, and feeling wanted. My partner matters enormously to my desire, but I don’t want to make her manufacture all of it."
AFF_MASTER_NEW = "Kim Anami calls the sexual current between encounters [“the simmer”](https://kimanami.com/meet-another-well-fked-man/). If we supposedly want each other but only show it when somebody officially initiates sex, I think something is already going wrong."
AFF_P1_OLD = "Kim Anami calls the sexual current between encounters “the simmer.” If we stop flirting with each other for months, I’m not going to assume our problem magically begins at bedtime. Sex is a pretty sensitive barometer for resentment, stress, health, medication, and feeling wanted. My partner matters enormously to my desire, but I don’t want to make her manufacture all of it."
AFF_P1_NEW = "Kim Anami calls the sexual current between encounters “the simmer.” If we supposedly want each other but only show it when somebody officially initiates sex, I think something is already going wrong."


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
    observed = {"master": sha256_text(master), "part1": sha256_text(part1), "part2": sha256_text(part2)}
    expected = {"master": SOURCE_MASTER_SHA, "part1": SOURCE_P1_SHA, "part2": SOURCE_P2_SHA}
    if observed != expected:
        raise RuntimeError(f"source hash mismatch: expected={expected} observed={observed}")

    master2, m1 = replace_exact(master, "affection-transition-stop-at-live-thought", AFF_MASTER_OLD, AFF_MASTER_NEW)
    part1_2, p1 = replace_exact(part1, "affection-transition-stop-at-live-thought", AFF_P1_OLD, AFF_P1_NEW)

    if sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 r6 repair")

    checks = base.audit(master, master2)
    checks["r6_affection_new_present"] = AFF_MASTER_NEW in master2
    checks["r6_affection_old_absent"] = AFF_MASTER_OLD not in master2
    checks["passed"] = bool(checks["passed"]) and checks["r6_affection_new_present"] and checks["r6_affection_old_absent"]
    if not checks["passed"]:
        raise RuntimeError(f"Part 1 r6 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "part1_affection_transition_repair_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": [m1], "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": [p1]},
            "part2": {"sha256": sha256_text(part2), "word_count_whitespace": len(part2.split()), "operations": [], "unchanged": True},
        },
        "detector_evidence": {
            "transition_experiment": "romance-detector-repair-20260820-part1-affection-transition-r6-20260821",
            "transition_text_sha256": "f1798598a2ab68535f63261296e590f584b6afc337af9b862052b85070faea18",
            "transition_words": 274,
            "pangram4_fraction_human": 1.0,
            "affection_section_calls_used": 6,
            "affection_section_cap": 6,
        },
        "selection_rationale": {
            "source_r5_aggregate_human": 0.9838229417800903,
            "source_r5_residual": "156-word AI window crossing Affection ending into Casual opening",
            "reason": "The 274-word widened transition boundary reached 100% Human only after stopping Affection after its two live source-derived observations instead of adding the generalized barometer/responsibility wrap-up. Casual opening remains unchanged.",
        },
        "detector_plan": {"part1": "fresh exact aggregate measurement; no further Affection section calls allowed"},
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
