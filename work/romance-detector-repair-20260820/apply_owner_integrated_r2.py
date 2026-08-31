#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import apply_owner_integrated_r1 as base

SOURCE_MASTER_SHA = "9b85666d8f1b18fa6ae659f8b7fbe39b55572553f0ef9cdd5b82c1beb0333f3f"
SOURCE_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
SOURCE_P2_SHA = "5cb6e7fa7aee66aed6addf43f15c1fce45c0bc4d0eba4f01a57d4fe1d1884afd"

PRIMAL_OLD = """A woman shouldn’t have to act soft, helpless, or cute every minute either. She can get pushed in the opposite direction too: if she’s spent years worrying that she isn’t beautiful enough, or that she’s too emotional, too difficult, not logical enough, or too needy, she may overcorrect into needing nobody. Then receiving care or letting a man lead starts to feel like weakness."""

PRIMAL_NEW = """I don't want a woman pretending to be helpless so I can feel masculine, but if she's spent years being told she's too needy or too emotional, she may decide that needing anyone is embarrassing and start refusing help even when she wants it."""

PSYCHEDELIC_OLD = """The intimacy can be completely real. You can leave feeling like this person understands you better than anyone you've ever met, and then a week later you're both sober and fighting over money, and you realize you still barely know how the two of you make decisions together."""

PSYCHEDELIC_NEW = """The intimacy can be completely real without telling you whether the two of you actually work together sober."""

REPLACEMENTS = [
    ("not-a-performance-overcorrection-to-refused-help", PRIMAL_OLD, PRIMAL_NEW),
    ("psychedelic-intimacy-does-not-answer-sober-fit", PSYCHEDELIC_OLD, PSYCHEDELIC_NEW),
]

REQUIRED = {
    "primal-performance": "The moment I have to prove that I’m the man, something has already become fake.",
    "primal-no-helpless-performance": "I don't want a woman pretending to be helpless so I can feel masculine",
    "primal-overcorrection": "start refusing help even when she wants it",
    "primal-toft": "Toft says that after fifty years he still tells his wife she’s beautiful",
    "primal-anami": "Anami talks a lot about women learning to receive.",
    "community-passed-r1": "the other becomes the whole backup system",
    "community-owner": "That's not abstract to me: I'm sure B. and I would still be together",
    "psychedelic-key": "But it was especially her higher self I was getting to know.",
    "psychedelic-sober-fit": "whether the two of you actually work together sober",
    "psychedelic-hd": "like I had with H.D.",
    "owner-exclusivity": "It's hard to find sexually monogamous animals, have you ever looked?",
    "owner-pinkest": "When did you two last dance?",
    "bear-close": "Bear, sex can be what you do when you’re older",
}


def audit(source: str, candidate: str) -> dict[str, object]:
    missing_protected = [
        name for name, anchor in base.base.base.helper.PROTECTED_ANCHORS.items() if anchor not in candidate
    ]
    missing_required = [name for name, anchor in REQUIRED.items() if anchor not in candidate]
    checks: dict[str, object] = {
        "headings_identical": base.base.base.helper.headings(source) == base.base.base.helper.headings(candidate),
        "native_markers_identical": base.base.base.helper.native_markers(source) == base.base.base.helper.native_markers(candidate),
        "markdown_link_destinations_identical": base.base.base.helper.markdown_links(source) == base.base.base.helper.markdown_links(candidate),
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
    parser = argparse.ArgumentParser(description="Materialize Romance owner-integrated residual repair r2.")
    parser.add_argument("--source-master", type=Path, required=True)
    parser.add_argument("--source-part1", type=Path, required=True)
    parser.add_argument("--source-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.source_master.read_text(encoding="utf-8")
    part1 = args.source_part1.read_text(encoding="utf-8")
    part2 = args.source_part2.read_text(encoding="utf-8")
    observed = {
        "master": base.base.base.helper.sha256_text(master),
        "part1": base.base.base.helper.sha256_text(part1),
        "part2": base.base.base.helper.sha256_text(part2),
    }
    expected = {"master": SOURCE_MASTER_SHA, "part1": SOURCE_P1_SHA, "part2": SOURCE_P2_SHA}
    if observed != expected:
        raise RuntimeError(f"r1 source hash mismatch: expected={expected} observed={observed}")

    candidate_master, master_ops = base.base.base.helper.apply_replacements(master, REPLACEMENTS)
    candidate_part2, p2_ops = base.base.base.helper.apply_replacements(part2, REPLACEMENTS)
    candidate_part1 = part1
    if base.base.base.helper.sha256_text(candidate_part1) != SOURCE_P1_SHA:
        raise RuntimeError("Part 1 changed during r2")

    checks = audit(master, candidate_master)
    if not checks["passed"]:
        raise RuntimeError(f"r2 invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    out_master.write_text(candidate_master, encoding="utf-8")
    out_p1.write_text(candidate_part1, encoding="utf-8")
    out_p2.write_text(candidate_part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "owner_integrated_residual_candidate_r2_not_owner_final_article",
        "source_r1": observed,
        "candidate": {
            "master": {
                "path": out_master.name,
                "sha256": base.base.base.helper.sha256_text(candidate_master),
                "word_count_whitespace": len(candidate_master.split()),
                "operations": master_ops,
                "invariant_audit": checks,
            },
            "part1": {
                "path": out_p1.name,
                "sha256": base.base.base.helper.sha256_text(candidate_part1),
                "word_count_whitespace": len(candidate_part1.split()),
                "operations": [],
                "unchanged": True,
            },
            "part2": {
                "path": out_p2.name,
                "sha256": base.base.base.helper.sha256_text(candidate_part2),
                "word_count_whitespace": len(candidate_part2.split()),
                "operations": p2_ops,
            },
        },
        "local_detector_state_before_r2": {
            "primal-not-a-performance": {
                "paid_section_calls": 1,
                "fraction_human": 0.7653250694274902,
                "remaining_ai_window": "A woman shouldn't have to act soft/helpless... through receiving care/leadership feels weak",
            },
            "community-two-pillars": {
                "paid_section_calls": 1,
                "fraction_human": 1.0,
                "status": "passed_no_more_local_calls_needed",
            },
            "psychedelic-relationship-discernment": {
                "paid_section_calls": 1,
                "fraction_human": 0.9445738196372986,
                "remaining_ai_window": "invented week-later sober/fighting-over-money scenario",
            },
        },
        "next_detector_plan": "measure only primal-not-a-performance and psychedelic-relationship-discernment at their same natural section boundaries; each will be call 2/6; do not retest community",
    }
    (args.output_dir / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
