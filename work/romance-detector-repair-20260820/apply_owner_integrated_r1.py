#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import apply_owner_integrated as base

SOURCE_MASTER_SHA = "dee776ada0db4dc2940d3815b9512ad5034e3224b0c569a9d29f6a69d9bb75a9"
SOURCE_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
SOURCE_P2_SHA = "9dc539ca99f8c747ecd5a551f2c72ad476c87671919863d2ad469acf6c6e696f"

PRIMAL_OLD = """Toft’s advice after fifty years is simple: tell her she’s beautiful, and keep noticing new kinds of beauty as she ages. Anami emphasizes learning to receive. Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless. A man receiving care doesn’t make him a child either.

We can invite these energies out of each other:
“Honey, how do you see this intuitively?”
or, “Can you help me think through the practical side for a minute?”

When a strong woman surrenders, she is choosing to. She knows she could drive; she asks me to drive because she likes how it feels when I do. That’s sexy."""

PRIMAL_NEW = """Toft says that after fifty years he still tells his wife she’s beautiful, including finding new kinds of beauty as she ages. Anami talks a lot about women learning to receive. Sometimes that’s as ordinary as a woman who knows perfectly well how to drive asking me to drive because she likes how it feels when I do; she’s choosing the experience. I might ask, “Honey, how do you see this intuitively?” because I actually want her to go there, and she might ask me to help think through the practical side because she wants that from me."""

COMMUNITY_OLD = """Some of the friends may even be exes who want us to break up. By then, the outside support isn’t really shared support anymore.

There's a practical side too. Two people covering housing, money, children, health, emotional crises, everything—there's no backup when one of them goes down. Who even has time for the relationship itself at that point?"""

COMMUNITY_NEW = """Some of the friends may even be exes who want us to break up. Eventually neither of us wants to talk to the other's friends anymore, which is a pretty terrible time to be trying to run the rest of life with two people. Housing, money, children, health, emotional crises—if one person goes down, the other becomes the whole backup system. Who even has time for the relationship itself at that point?"""

PSYCHEDELIC_OLD = """The intimacy can be completely real. You may feel that this person understands you more deeply than anyone ever has. There is still a lot you don’t know: what happens when you’re sober, irritated, jealous, broke, bored, or trying to make a difficult decision together?"""

PSYCHEDELIC_NEW = """The intimacy can be completely real. You can leave feeling like this person understands you better than anyone you've ever met, and then a week later you're both sober and fighting over money, and you realize you still barely know how the two of you make decisions together."""

REPLACEMENTS = [
    ("not-a-performance-receiving-as-lived-invitation", PRIMAL_OLD, PRIMAL_NEW),
    ("community-support-to-backup-system-causal-chain", COMMUNITY_OLD, COMMUNITY_NEW),
    ("psychedelic-intimacy-to-sober-decision-consequence", PSYCHEDELIC_OLD, PSYCHEDELIC_NEW),
]

REQUIRED = {
    "muses-owner": "I'm referring more to feminine vs masculine archetypes.",
    "crucible": "that’s the Crucible safety problem I already talked about.",
    "money-authority": "My house, my rules",
    "leadership": "This is where I want to go. This is what I think we should do. Are you game?",
    "not-performance": "The moment I have to prove that I’m the man, something has already become fake.",
    "toft-beauty": "Toft says that after fifty years he still tells his wife she’s beautiful",
    "anami-receive": "Anami talks a lot about women learning to receive.",
    "chosen-receiving": "she’s choosing the experience",
    "intuitive-invitation": "Honey, how do you see this intuitively?",
    "practical-invitation": "help think through the practical side",
    "community-backup": "the other becomes the whole backup system",
    "community-caveat": "Community isn't magic either",
    "exclusivity-owner": "It's hard to find sexually monogamous animals, have you ever looked?",
    "sexclusivity": "Sexclusivity started gaining sway",
    "psychedelic-owner-key": "But it was especially her higher self I was getting to know.",
    "psychedelic-sober-consequence": "a week later you're both sober and fighting over money",
    "pinkest-owner": "When did you two last dance?",
    "outside-help": "Outside help can sometimes break the loop fast",
    "bear-close": "Bear, sex can be what you do when you’re older",
}


def audit(source: str, candidate: str) -> dict[str, object]:
    missing_protected = [
        name for name, anchor in base.base.helper.PROTECTED_ANCHORS.items() if anchor not in candidate
    ]
    missing_required = [name for name, anchor in REQUIRED.items() if anchor not in candidate]
    checks: dict[str, object] = {
        "headings_identical": base.base.helper.headings(source) == base.base.helper.headings(candidate),
        "native_markers_identical": base.base.helper.native_markers(source) == base.base.helper.native_markers(candidate),
        "markdown_link_destinations_identical": base.base.helper.markdown_links(source) == base.base.helper.markdown_links(candidate),
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
    parser = argparse.ArgumentParser(description="Materialize Romance owner-integrated residual repair r1.")
    parser.add_argument("--source-master", type=Path, required=True)
    parser.add_argument("--source-part1", type=Path, required=True)
    parser.add_argument("--source-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.source_master.read_text(encoding="utf-8")
    part1 = args.source_part1.read_text(encoding="utf-8")
    part2 = args.source_part2.read_text(encoding="utf-8")
    observed = {
        "master": base.base.helper.sha256_text(master),
        "part1": base.base.helper.sha256_text(part1),
        "part2": base.base.helper.sha256_text(part2),
    }
    expected = {"master": SOURCE_MASTER_SHA, "part1": SOURCE_P1_SHA, "part2": SOURCE_P2_SHA}
    if observed != expected:
        raise RuntimeError(f"owner-integrated source hash mismatch: expected={expected} observed={observed}")

    candidate_master, master_ops = base.base.helper.apply_replacements(master, REPLACEMENTS)
    candidate_part2, p2_ops = base.base.helper.apply_replacements(part2, REPLACEMENTS)
    candidate_part1 = part1
    if base.base.helper.sha256_text(candidate_part1) != SOURCE_P1_SHA:
        raise RuntimeError("Part 1 changed during owner-integrated residual repair")

    checks = audit(master, candidate_master)
    if not checks["passed"]:
        raise RuntimeError(f"owner-integrated residual invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    out_master.write_text(candidate_master, encoding="utf-8")
    out_p1.write_text(candidate_part1, encoding="utf-8")
    out_p2.write_text(candidate_part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "owner_integrated_residual_candidate_not_owner_final_article",
        "source_owner_integrated": observed,
        "candidate": {
            "master": {
                "path": out_master.name,
                "sha256": base.base.helper.sha256_text(candidate_master),
                "word_count_whitespace": len(candidate_master.split()),
                "operations": master_ops,
                "invariant_audit": checks,
            },
            "part1": {
                "path": out_p1.name,
                "sha256": base.base.helper.sha256_text(candidate_part1),
                "word_count_whitespace": len(candidate_part1.split()),
                "operations": [],
                "unchanged": True,
            },
            "part2": {
                "path": out_p2.name,
                "sha256": base.base.helper.sha256_text(candidate_part2),
                "word_count_whitespace": len(candidate_part2.split()),
                "operations": p2_ops,
            },
        },
        "source_detector": {
            "source_part2_sha256": SOURCE_P2_SHA,
            "pangram_version": "4.0",
            "fraction_human": 0.9761735796928406,
            "fraction_ai": 0.02382640726864338,
            "fraction_ai_assisted": 0.0,
            "residual_ai_segments": 3,
        },
        "next_detector_plan": {
            "local_sections": "measure three distinct natural sections with 200+ contiguous reader-visible context; each section has its own six-paid-call cap",
            "aggregate_part2": "defer fresh aggregate measurement until local section diagnostics pass or materially inform next edit",
        },
    }
    (args.output_dir / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
