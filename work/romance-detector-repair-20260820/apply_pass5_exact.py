#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import apply_pass5 as base

MASTER_MUSES_OLD = base.MUSES_OLD.replace("the old Men Are from Mars, Women Are from Venus problem", "the old *Men Are from Mars, Women Are from Venus* problem")
MASTER_MUSES_NEW = base.MUSES_NEW.replace("the old Men Are from Mars, Women Are from Venus problem", "the old *Men Are from Mars, Women Are from Venus* problem")
PRIMAL_OLD_BEFORE, PRIMAL_OLD_AFTER = base.PRIMAL_PERFORMANCE_OLD.split("\nNot A Performance\n\n", 1)
PRIMAL_NEW_BEFORE, PRIMAL_NEW_AFTER = base.PRIMAL_PERFORMANCE_NEW.split("\nNot A Performance\n\n", 1)

MASTER_REPLACEMENTS = [
    ("anami-stories-solo-progression", base.ANAMI_OLD, base.ANAMI_NEW),
    ("muses-listening-safety-competence-chain", MASTER_MUSES_OLD, MASTER_MUSES_NEW),
    ("primal-lived-chain-before-heading", PRIMAL_OLD_BEFORE, PRIMAL_NEW_BEFORE),
    ("not-a-performance-lived-chain-after-heading", PRIMAL_OLD_AFTER, PRIMAL_NEW_AFTER),
    ("choosing-same-words-different-futures", base.CHOOSING_OLD, base.CHOOSING_NEW),
    ("exclusivity-history-conversational", base.EXCLUSIVITY_HISTORY_OLD, base.EXCLUSIVITY_HISTORY_NEW),
]

def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize exact Romance detector-repair pass 5 across Markdown master and plaintext detector boundary.")
    parser.add_argument("--pass4-master", type=Path, required=True)
    parser.add_argument("--pass4-part1", type=Path, required=True)
    parser.add_argument("--pass4-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.pass4_master.read_text(encoding="utf-8")
    part1 = args.pass4_part1.read_text(encoding="utf-8")
    part2 = args.pass4_part2.read_text(encoding="utf-8")
    observed = {"master": base.sha256_text(master), "part1": base.sha256_text(part1), "part2": base.sha256_text(part2)}
    expected = {"master": base.PASS4_MASTER_SHA, "part1": base.PASS4_P1_SHA, "part2": base.PASS4_P2_SHA}
    if observed != expected:
        raise RuntimeError(f"pass-4 source hash mismatch: expected={expected} observed={observed}")

    master5, master_ops = base.apply_replacements(master, MASTER_REPLACEMENTS)
    part2_5, p2_ops = base.apply_replacements(part2, base.P2_REPLACEMENTS)
    part1_5 = part1
    if base.sha256_text(part1_5) != base.REGISTERED_P1_SHA:
        raise RuntimeError("Part 1 changed during pass 5; detector submission is forbidden")
    checks = base.audit_master(master, master5)
    if not checks["passed"]:
        raise RuntimeError(f"pass-5 master invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    out_master.write_text(master5, encoding="utf-8")
    out_p1.write_text(part1_5, encoding="utf-8")
    out_p2.write_text(part2_5, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "candidate_not_owner_final",
        "source_pass4": observed,
        "candidate": {
            "master": {"path": out_master.name, "sha256": base.sha256_text(master5), "word_count_whitespace": len(master5.split()), "operations": master_ops, "invariant_audit": checks},
            "part1": {"path": out_p1.name, "sha256": base.sha256_text(part1_5), "word_count_whitespace": len(part1_5.split()), "operations": [], "reuses_registered_detector_result": True},
            "part2": {"path": out_p2.name, "sha256": base.sha256_text(part2_5), "word_count_whitespace": len(part2_5.split()), "operations": p2_ops},
        },
        "detector_plan": {"part1": "no_new_call_exact_registered_hash_unchanged", "part2": "one_new_pangram4_measurement_via_private_selfhost"},
        "editorial_note": "Pass 5 targets the five exact AI windows returned by the successful self-hosted pass-4 Pangram-4 result. The source-format master preserves Markdown italics and the untouched Not A Performance heading while the detector boundary receives the semantically identical plaintext changes.",
    }
    (args.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
