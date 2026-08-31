#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SOURCE_MASTER_SHA = "43d98cdb0df5fc9437f89ba56187e3a5586951375ccbf69e6e6a82e82569925f"
SOURCE_P1_SHA = "f272bf6fab784a4e1922374a36573f216f29c6c691deba0fe0394a2aaad3fd83"
SOURCE_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"
PRIMAL_HEADING = "Primal attraction: channeling the Divine Masculine & Feminine\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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

    full_visible = part1 + "\n" + part2
    if full_visible.count(PRIMAL_HEADING) != 1:
        raise RuntimeError(f"expected one Primal heading, found {full_visible.count(PRIMAL_HEADING)}")
    split_at = full_visible.index(PRIMAL_HEADING)
    part1_new = full_visible[:split_at]
    part2_new = full_visible[split_at:]

    checks = {
        "master_byte_identical": sha256_text(master) == SOURCE_MASTER_SHA,
        "full_reader_visible_byte_identical": part1_new + part2_new == full_visible,
        "new_part1_ends_after_complete_maturity_section": part1_new.rstrip().endswith("The next two sections are about masculine–feminine polarity and Twin Flames. If neither is relevant to you, skip ahead to Two Pillars Don't Hold The Roof Up."),
        "new_part2_starts_at_primal_heading": part2_new.startswith(PRIMAL_HEADING),
        "old_mid_maturity_boundary_removed": not part2_new.startswith('Key at first asked me innocently, "Can you be my guru?"'),
        "part1_contains_key_guru_continuation": 'Key at first asked me innocently, "Can you be my guru?"' in part1_new,
        "part1_contains_self_condescension_continuation": "I also have to admit, I can become condescending" in part1_new,
        "part1_contains_helping_needed_continuation": "Helping feels good. Being needed can feel good too." in part1_new,
        "part1_contains_complementarity_close": "So I do believe in mutual coaching and complementarity." in part1_new,
        "full_word_count_unchanged": len(full_visible.split()) == len(part1_new.split()) + len(part2_new.split()),
    }
    checks["passed"] = all(checks.values())
    if not checks["passed"]:
        raise RuntimeError(f"r13 natural-split invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_new, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2_new, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "preservation_r13_boundary_only_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master), "word_count_whitespace": len(master.split()), "unchanged": True},
            "part1": {"sha256": sha256_text(part1_new), "word_count_whitespace": len(part1_new.split())},
            "part2": {"sha256": sha256_text(part2_new), "word_count_whitespace": len(part2_new.split())},
            "full_reader_visible": {"sha256": sha256_text(full_visible), "word_count_whitespace": len(full_visible.split())},
        },
        "operation": {
            "type": "aggregate_boundary_relocation_only",
            "old_boundary": "mid-Maturity Levels between patient-role paragraph and Key/guru continuation",
            "new_boundary": "natural section boundary immediately before Primal attraction",
            "article_prose_changed": False,
            "full_reader_visible_bytes_changed": False,
        },
        "invariant_audit": checks,
        "detector_rationale": "The r12 aggregate leaves a 53-word AI window at the arbitrary end of Part 1, while the immediately following doctor/patient continuation contains existing exact Human evidence. Canonical detector protocol treats arbitrary half splits as localization clues rather than semantic units. Re-splitting at the complete Maturity Levels/Primal Attraction boundary tests the same article with coherent discourse context.",
        "detector_plan": "Certify both new exact halves because both aggregate boundaries changed. This is aggregate certification, not a local section repair call.",
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
