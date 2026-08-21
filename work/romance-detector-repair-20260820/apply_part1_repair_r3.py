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

REPLACEMENTS = [
    (
        "casual-opening-lived-causality",
        "Your body doesn’t know that you picked someone up at a bar and agreed it was only for fun. Oxytocin, vasopressin, and the rest can start attaching you anyway. Then the next morning, you’re wondering why they didn’t call. Well, not getting pulled in any further is the best outcome still available, actually, since you just played Russian Roulette with a potential life bond to a stranger.",
        "You can agree it's “only for fun” all you want, and then wake up the next morning wondering why they didn't call. Your body wasn't part of the agreement; oxytocin, vasopressin, and the rest have already started doing their thing. If you don't get pulled in any further, that's actually the best outcome still available, since you just played Russian Roulette with a possible life bond to a stranger.",
    ),
    (
        "casual-honesty-limit-spoken",
        "That may be candid about what you expect now. It doesn’t settle what either of you will owe if the act creates something neither of you expected.",
        "Okay, that's honest as far as it goes. But then you have sex, and what if it creates something neither of you planned for?",
    ),
    (
        "ordinary-time-not-mirrored-verdict",
        "At some point, more questions mostly teach me what the person says about themself. Then I need ordinary time. Ten profound conversations in one weekend may tell me we can have profound conversations. They don't tell me what she's like on a boring day, or when she's annoyed and doesn't have an answer prepared.",
        "After a while, more questions mostly teach me what the person says about themself, and I need ordinary time. We might spend a whole weekend having incredibly profound conversations; then I want to see a boring day, or what happens when she's annoyed and hasn't already thought through an answer.",
    ),
    (
        "slow-community-to-gandarussa-causal",
        "We don't live in tribes anymore, and usually nobody around us knows both of us well enough to slow us down while we figure out what this actually is.\n\nSince I know avoidance won't work every time, Gandarussa matters too.",
        "We don't live in tribes anymore, where people around us might know both of us well enough to slow this down. Mostly I have to build my own brakes before I'm alone with her, and they still fail sometimes.\n\nThat's where Gandarussa matters to me.",
    ),
]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def apply(text: str) -> tuple[str, list[dict[str, object]]]:
    ops: list[dict[str, object]] = []
    for label, old, new in REPLACEMENTS:
        count = text.count(old)
        if count != 1:
            raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
        text = text.replace(old, new, 1)
        ops.append({
            "label": label,
            "old_sha256": sha256_text(old),
            "new_sha256": sha256_text(new),
        })
    return text, ops


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

    master2, mops = apply(master)
    part1_2, pops = apply(part1)
    if sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 r3 repair")

    checks = base.audit(master, master2)
    extra = {
        "casual-body-agreement": "Your body wasn't part of the agreement",
        "casual-honesty-limit": "Okay, that's honest as far as it goes.",
        "ordinary-boring-day": "then I want to see a boring day",
        "slow-own-brakes": "Mostly I have to build my own brakes before I'm alone with her",
        "gandarussa-preserved": "That's where Gandarussa matters to me.",
    }
    missing = [name for name, anchor in extra.items() if anchor not in master2]
    checks["r3_required_missing"] = missing
    checks["r3_old_spans_absent"] = all(old not in master2 for _, old, _ in REPLACEMENTS)
    checks["passed"] = bool(checks["passed"]) and not missing and checks["r3_old_spans_absent"]
    if not checks["passed"]:
        raise RuntimeError(f"Part 1 r3 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "part1_final_residual_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": mops, "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": pops},
            "part2": {"sha256": sha256_text(part2), "word_count_whitespace": len(part2.split()), "operations": [], "unchanged": True},
        },
        "source_aggregate_result": {
            "part1_sha256": SOURCE_P1_SHA,
            "pangram4_fraction_human": 0.9847978949546814,
            "residual_ai_segments": 4,
        },
        "detector_plan": {"part1": "fresh exact aggregate measurement; aggregate is authoritative over local short diagnostics"},
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
