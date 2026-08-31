#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import apply_owner_integrated_r2 as base

SOURCE_MASTER_SHA = "5bada64b833a36c6995c5de062571dd18d51075daa7486ba5f1abfa9200601ab"
SOURCE_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
SOURCE_P2_SHA = "1aba86e2706943467418c56fa7b21515a216bcef25dc71c1784138349ad2f841"

PRIMAL_OLD = """I don't want a woman pretending to be helpless so I can feel masculine, but if she's spent years being told she's too needy or too emotional, she may decide that needing anyone is embarrassing and start refusing help even when she wants it.

Toft says that after fifty years he still tells his wife she’s beautiful, including finding new kinds of beauty as she ages. Anami talks a lot about women learning to receive. Sometimes that’s as ordinary as a woman who knows perfectly well how to drive asking me to drive because she likes how it feels when I do; she’s choosing the experience."""

PRIMAL_NEW = """A woman can receive without acting helpless, but after years of proving she doesn't need anybody, she may have trouble letting someone do something for her even when she wants it. Anami talks a lot about women learning to receive. Toft says that after fifty years he still tells his wife she’s beautiful and keeps finding new kinds of beauty as she ages."""

REPLACEMENTS = [
    ("not-a-performance-receiving-without-helplessness", PRIMAL_OLD, PRIMAL_NEW),
]

REQUIRED = {
    "primal-performance": "The moment I have to prove that I’m the man, something has already become fake.",
    "primal-receive-not-helpless": "A woman can receive without acting helpless",
    "primal-overcorrection": "after years of proving she doesn't need anybody",
    "primal-wanted-help": "even when she wants it",
    "primal-anami": "Anami talks a lot about women learning to receive.",
    "primal-toft": "Toft says that after fifty years he still tells his wife she’s beautiful",
    "primal-intuitive-invite": "Honey, how do you see this intuitively?",
    "community-passed": "the other becomes the whole backup system",
    "psychedelic-passed": "The intimacy can be completely real without telling you whether the two of you actually work together sober.",
    "owner-exclusivity": "It's hard to find sexually monogamous animals, have you ever looked?",
    "owner-pinkest": "When did you two last dance?",
    "bear-close": "Bear, sex can be what you do when you’re older",
}


def audit(source: str, candidate: str) -> dict[str, object]:
    helper = base.base.base.base.helper
    missing_protected = [name for name, anchor in helper.PROTECTED_ANCHORS.items() if anchor not in candidate]
    missing_required = [name for name, anchor in REQUIRED.items() if anchor not in candidate]
    checks: dict[str, object] = {
        "headings_identical": helper.headings(source) == helper.headings(candidate),
        "native_markers_identical": helper.native_markers(source) == helper.native_markers(candidate),
        "markdown_link_destinations_identical": helper.markdown_links(source) == helper.markdown_links(candidate),
        "protected_anchors_missing": missing_protected,
        "required_missing": missing_required,
    }
    checks["passed"] = (
        bool(checks["headings_identical"])
        and bool(checks["native_markers_identical"])
        and bool(checks["markdown_link_destinations_identical"])
        and not missing_protected
        and not missing_required
    )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize Romance owner-integrated residual repair r3.")
    parser.add_argument("--source-master", type=Path, required=True)
    parser.add_argument("--source-part1", type=Path, required=True)
    parser.add_argument("--source-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    helper = base.base.base.base.helper
    master = args.source_master.read_text(encoding="utf-8")
    part1 = args.source_part1.read_text(encoding="utf-8")
    part2 = args.source_part2.read_text(encoding="utf-8")
    observed = {"master": helper.sha256_text(master), "part1": helper.sha256_text(part1), "part2": helper.sha256_text(part2)}
    expected = {"master": SOURCE_MASTER_SHA, "part1": SOURCE_P1_SHA, "part2": SOURCE_P2_SHA}
    if observed != expected:
        raise RuntimeError(f"r2 source hash mismatch: expected={expected} observed={observed}")

    candidate_master, master_ops = helper.apply_replacements(master, REPLACEMENTS)
    candidate_part2, p2_ops = helper.apply_replacements(part2, REPLACEMENTS)
    candidate_part1 = part1
    if helper.sha256_text(candidate_part1) != SOURCE_P1_SHA:
        raise RuntimeError("Part 1 changed during r3")

    checks = audit(master, candidate_master)
    if not checks["passed"]:
        raise RuntimeError(f"r3 invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    out_master.write_text(candidate_master, encoding="utf-8")
    out_p1.write_text(candidate_part1, encoding="utf-8")
    out_p2.write_text(candidate_part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "owner_integrated_residual_candidate_r3_not_owner_final_article",
        "source_r2": observed,
        "candidate": {
            "master": {"path": out_master.name, "sha256": helper.sha256_text(candidate_master), "word_count_whitespace": len(candidate_master.split()), "operations": master_ops, "invariant_audit": checks},
            "part1": {"path": out_p1.name, "sha256": helper.sha256_text(candidate_part1), "word_count_whitespace": len(candidate_part1.split()), "operations": [], "unchanged": True},
            "part2": {"path": out_p2.name, "sha256": helper.sha256_text(candidate_part2), "word_count_whitespace": len(candidate_part2.split()), "operations": p2_ops},
        },
        "local_detector_state_before_r3": {
            "primal-not-a-performance": {"paid_section_calls": 2, "fraction_human_r2": 0.6025727987289429, "next_call": "3_of_6"},
            "community-two-pillars": {"paid_section_calls": 1, "fraction_human": 1.0, "status": "locked_pass"},
            "psychedelic-relationship-discernment": {"paid_section_calls": 2, "fraction_human": 1.0, "status": "locked_pass"},
        },
        "next_detector_plan": "measure only primal-not-a-performance at the same natural section boundary; call 3/6; do not retest passed sections",
    }
    (args.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
