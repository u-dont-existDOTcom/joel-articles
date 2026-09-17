#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_part1_repair_r1 as base

SOURCE_MASTER_SHA = "53790d7234df72f9f48678c331debff9b89eb238007af0b68cd69a6aa90669f7"
SOURCE_P1_SHA = "ff3c6d77a848d36c51776f76a6643aaae2262b4cffa458b1f54319dfe54971eb"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

FLAWS_OLD = '''Spiritual depth also doesn't tell me how dependable somebody is. She may meditate for two hours and still not show up for boring work, sickness, or something she promised yesterday. I may be seeing the divine archetype while ignoring the adult I would actually have to build a life with.

So hold your horses a bit more than you’d like to. See if your partner still praises you after a cold feud.

Ask what flaws she sees in you from time to time. Notice whether either of you is relating to a real human being or just to the divine archetypal energy the other person temporarily opened.

I’ve been through the wringer so much with idealization that now no matter who praises me I’m basically like, “Okay, thanks.” I try to do my best.'''
FLAWS_NEW = '''I’ve been through the wringer so much with idealization that now no matter who praises me I’m basically like, “Okay, thanks.” I try to do my best.'''

SLOW_OLD = '''Going slowly can show you how somebody’s moods move over time, how they treat you, and how they treat other people. It still can’t tell you how good the sex will be or how either of you will act afterward.

You can know somebody for twenty years and then discover on the first night that the polarity isn’t there, touch feels wrong, smell feels wrong, your desire levels or kinks don’t fit, one person is sexually shut down, or the bodies just don’t connect.

But the first night isn’t necessarily the final ceiling either.'''
SLOW_NEW = '''I could know a woman for twenty years and still get into bed with her for the first time knowing almost nothing about how our bodies will relate. Polarity, touch, smell, desire levels, kinks, sexual openness—conversation only goes so far.'''


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

    master2, m1 = replace_exact(master, "conversation-flaws-delete-duplicate-wrapup", FLAWS_OLD, FLAWS_NEW)
    master2, m2 = replace_exact(master2, "slow-steady-live-uncertainty", SLOW_OLD, SLOW_NEW)
    part1_2, p1 = replace_exact(part1, "conversation-flaws-delete-duplicate-wrapup", FLAWS_OLD, FLAWS_NEW)
    part1_2, p2 = replace_exact(part1_2, "slow-steady-live-uncertainty", SLOW_OLD, SLOW_NEW)

    if sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 r7 repair")

    checks = base.audit(master, master2)
    checks["r7_flaws_duplicate_absent"] = "Spiritual depth also doesn't tell me how dependable somebody is." not in master2
    checks["r7_flaws_owner_stop_present"] = FLAWS_NEW in master2
    checks["r7_slow_new_present"] = SLOW_NEW in master2
    checks["r7_slow_old_absent"] = SLOW_OLD not in master2
    checks["passed"] = (
        bool(checks["passed"])
        and checks["r7_flaws_duplicate_absent"]
        and checks["r7_flaws_owner_stop_present"]
        and checks["r7_slow_new_present"]
        and checks["r7_slow_old_absent"]
    )
    if not checks["passed"]:
        raise RuntimeError(f"Part 1 r7 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "part1_residual_repairs_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": [m1, m2], "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": [p1, p2]},
            "part2": {"sha256": sha256_text(part2), "word_count_whitespace": len(part2.split()), "operations": [], "unchanged": True},
        },
        "local_detector_evidence": {
            "part1-conversation-flaws": {
                "calls_used": 3,
                "fraction_human": 1.0,
                "result": "romance-detector-repair-20260820-part1-conversation-flaws-r3-20260821",
                "text_sha256": "c221837f9fa3cc699d8696cddb78c3fbf6a4890fd3c919a07625b422fe07728c"
            },
            "part1-slow-steady": {
                "calls_used": 1,
                "fraction_human": 1.0,
                "result": "romance-detector-repair-20260820-part1-residual-natural-r1b-20260821",
                "text_sha256": "114de8d6f9e9b5fa708ac53f715a1a311f9a085434083e93763ae607bad7da0f"
            }
        },
        "detector_plan": {"part1": "fresh exact aggregate measurement after repository/architecture gates"}
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
