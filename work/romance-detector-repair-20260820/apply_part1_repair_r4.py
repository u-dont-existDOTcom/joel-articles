#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_part1_repair_r1 as base

SOURCE_MASTER_SHA = "485726dc6c5215903050a0d5893805ba48e556974569dbef3dc2cec6ddaa877d"
SOURCE_P1_SHA = "9ea0f9b15415292835c1e8eeff32757940fb05b304eeef6e1ac63b95fedbbd3b"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

ORDINARY_OLD = "At some point, more questions mostly teach me what the person says about themself. Then I need ordinary time. Ten profound conversations in one weekend may tell me we can have profound conversations. They don't tell me what she's like on a boring day, or when she's annoyed and doesn't have an answer prepared."
ORDINARY_NEW = "After a while, more questions mostly teach me what the person says about themself, and I need ordinary time. We might spend a whole weekend having incredibly profound conversations; then I want to see a boring day, or what happens when she's annoyed and hasn't already thought through an answer."

SLOW_P1_OLD = """We don't live in tribes anymore, and usually nobody around us knows both of us well enough to slow us down while we figure out what this actually is.

Since I know avoidance won't work every time, Gandarussa matters too."""
SLOW_P1_NEW = """We don't live in tribes anymore, where people around us might know both of us well enough to slow this down. Mostly I have to build my own brakes before I'm alone with her, and they still fail sometimes.

That's where Gandarussa matters to me."""
SLOW_MASTER_OLD = """We don't live in tribes anymore, and usually nobody around us knows both of us well enough to slow us down while we figure out what this actually is.

Since I know avoidance won't work every time, [Gandarussa](https://thediplomat.com/2013/09/a-male-contraceptive-pill-for-indonesia/) matters too."""
SLOW_MASTER_NEW = """We don't live in tribes anymore, where people around us might know both of us well enough to slow this down. Mostly I have to build my own brakes before I'm alone with her, and they still fail sometimes.

That's where [Gandarussa](https://thediplomat.com/2013/09/a-male-contraceptive-pill-for-indonesia/) matters to me."""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_exact(text: str, label: str, old: str, new: str) -> tuple[str, dict[str, object]]:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
    return text.replace(old, new, 1), {"label": label, "old_sha256": sha256_text(old), "new_sha256": sha256_text(new)}


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

    master2, m1 = replace_exact(master, "ordinary-time-not-mirrored-verdict", ORDINARY_OLD, ORDINARY_NEW)
    part1_2, p1 = replace_exact(part1, "ordinary-time-not-mirrored-verdict", ORDINARY_OLD, ORDINARY_NEW)
    master2, m2 = replace_exact(master2, "slow-community-to-gandarussa-causal", SLOW_MASTER_OLD, SLOW_MASTER_NEW)
    part1_2, p2 = replace_exact(part1_2, "slow-community-to-gandarussa-causal", SLOW_P1_OLD, SLOW_P1_NEW)

    if sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 r4 repair")

    checks = base.audit(master, master2)
    extra = {
        "ordinary-boring-day": "then I want to see a boring day",
        "slow-own-brakes": "Mostly I have to build my own brakes before I'm alone with her",
        "gandarussa-causal-link": "That's where [Gandarussa]",
    }
    missing = [name for name, anchor in extra.items() if anchor not in master2]
    checks["r4_required_missing"] = missing
    checks["r4_old_spans_absent"] = ORDINARY_OLD not in master2 and SLOW_MASTER_OLD not in master2
    checks["passed"] = bool(checks["passed"]) and not missing and checks["r4_old_spans_absent"]
    if not checks["passed"]:
        raise RuntimeError(f"Part 1 r4 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "part1_selective_residual_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": [m1, m2], "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": [p1, p2]},
            "part2": {"sha256": sha256_text(part2), "word_count_whitespace": len(part2.split()), "operations": [], "unchanged": True},
        },
        "selection_rationale": {
            "source_r2_aggregate_human": 0.9847978949546814,
            "r3_aggregate_human": 0.980210542678833,
            "kept_from_r3": ["ordinary-time-not-mirrored-verdict", "slow-community-to-gandarussa-causal"],
            "reverted_from_r3": ["casual-opening-lived-causality", "casual-honesty-limit-spoken"],
            "reason": "r3 eliminated the ordinary-time and Gandarussa residuals but worsened Casual and lowered aggregate Human score; r4 isolates the two apparent winners against exact r2 source.",
        },
        "detector_plan": {"part1": "fresh exact aggregate measurement"},
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
