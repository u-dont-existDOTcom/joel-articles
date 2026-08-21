#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_pass5 as helper
import apply_part1_semantic_restore_r6 as r6

SOURCE_MASTER_SHA = "2830b1906ce1515edcb36b4d9a6ebe75fc6e2cf59e953a7072c8dc2890b62134"
SOURCE_P1_SHA = "35dea0c3fc5e1723a3d8d1f0c8192447525758dfb953910e1e0d353ae3dcf4d9"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

QUEEN_OPEN_MASTER_OLD = """## The Queen of Orgasms

Women have shown me that the cervix can open during sex and become intensely pleasurable for both of us."""
QUEEN_OPEN_MASTER_NEW = """## The Queen of Orgasms

Many people are not even aware of how incredible sex can be when the polarity, trust, love & safety are all where they should be. Women have shown me that the cervix can open during sex and become intensely pleasurable for both of us."""
QUEEN_OPEN_P2_OLD = QUEEN_OPEN_MASTER_OLD.replace("## The Queen of Orgasms", "The Queen of Orgasms")
QUEEN_OPEN_P2_NEW = QUEEN_OPEN_MASTER_NEW.replace("## The Queen of Orgasms", "The Queen of Orgasms")

QUEEN_LAB_OLD = """because the vagus nerve can carry the signal without using the spinal route that clitoral orgasms use. Kim Anami, Diana Richardson, and other popular educators and promoters of cervical orgasms further claim"""
QUEEN_LAB_NEW = """because the vagus nerve can carry the signal without using the spinal route that clitoral orgasms use. That laboratory evidence establishes the uniqueness of the phenomenon. Kim Anami, Diana Richardson, and other popular educators and promoters of cervical orgasms further claim"""

NOT_PERFORMANCE_MASTER_OLD = """## Not A Performance

The moment I have to prove that I’m the man, something has already become fake.

I don’t actually walk around thinking I’m some super-masculine guy. I cry, I need help, I get things wrong. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

When a woman appreciates that masculine side of me, it tends to come out by itself.

Toft says that after fifty years he still tells his wife she’s beautiful, including finding new kinds of beauty as she ages. Anami talks a lot about women learning to receive. Sometimes that’s as ordinary as a woman who knows perfectly well how to drive asking me to drive because she likes how it feels when I do; she’s choosing the experience. I might ask, “Honey, how do you see this intuitively?” because I actually want her to go there, and she might ask me to help think through the practical side because she wants that from me.

That's called invitational: Would you rather go to a party where you were invited or a war you got drafted into?

When a woman doesn't know how to gently invite a man to lead, she may manufacture a crisis until the man is forced to take charge to get the same outward result.

Unfortunately, I've seen a lot of the latter."""

NOT_PERFORMANCE_MASTER_NEW = """## Not A Performance

The moment I have to prove that I’m the man, something has already become fake.

I don’t actually walk around thinking I’m some super-masculine guy. I cry, I need help, I get things wrong. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

When a woman appreciates that masculine side of me, it tends to come out by itself.

The same is true for a woman. She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine.

Women can get pulled in two directions here. She may worry that I don’t find her beautiful enough, or that she’s too emotional, too difficult, not logical enough, or too needy. Then she can overcorrect into needing nobody and make receiving care or letting a man lead feel like weakness.

Toft says that after fifty years he still tells his wife she’s beautiful, including finding new kinds of beauty as she ages. Anami talks a lot about women learning to receive. Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless. A man receiving care doesn’t make him a child either. Sometimes that’s as ordinary as a woman who knows perfectly well how to drive asking me to drive because she likes how it feels when I do; she’s choosing the experience. I might ask, “Honey, how do you see this intuitively?” because I actually want her to go there, and she might ask me to help think through the practical side because she wants that from me.

That's called invitational: Would you rather go to a party where you were invited or a war you got drafted into?

When a woman doesn't know how to gently invite a man to lead, she may manufacture a crisis until the man is forced to take charge to get the same outward result.

Unfortunately, I've seen a lot of the latter."""

NOT_PERFORMANCE_P2_OLD = NOT_PERFORMANCE_MASTER_OLD.replace("## Not A Performance", "Not A Performance")
NOT_PERFORMANCE_P2_NEW = NOT_PERFORMANCE_MASTER_NEW.replace("## Not A Performance", "Not A Performance")

AFTER_LEAVING_OLD = "A therapist, pastor, or even a stranger may see the evidence more clearly than a lifelong friend."
AFTER_LEAVING_NEW = AFTER_LEAVING_OLD + " Even the curiosity itself can be therapeutic for you."

P2_SEMANTIC_REQUIREMENTS = {
    "queen-polarity-trust-love-safety": "Many people are not even aware of how incredible sex can be when the polarity, trust, love & safety are all where they should be.",
    "queen-lab-uniqueness": "That laboratory evidence establishes the uniqueness of the phenomenon.",
    "performance-female-anti-performance": "She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine.",
    "performance-overcorrection": "she can overcorrect into needing nobody and make receiving care or letting a man lead feel like weakness.",
    "performance-strong-woman-receiving": "Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless.",
    "performance-man-receiving": "A man receiving care doesn’t make him a child either.",
    "after-leaving-curiosity": "Even the curiosity itself can be therapeutic for you.",
}

OWNER_AUTHORITY_ANCHORS = {
    "owner-muses": "What attracts me is the feminine intuitive leap, because it's hard for me to understand, seems often absurd, yet many times more accurate than what I could have figured.",
    "owner-leadership": "She may know much more than I do about some particular field, including a traditionally non-feminine one, and in that case I want her help.",
    "owner-exclusivity": "Sexclusivity started gaining sway around the time we started planting carrots and peas, and owning land.",
    "owner-pinkest": "When did you two last dance? And not the “we dance around our problems” joke (LOL)..",
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
    checks = r6.semantic_audit(source, candidate)
    missing_p2 = [name for name, anchor in P2_SEMANTIC_REQUIREMENTS.items() if anchor not in candidate]
    missing_owner = [name for name, anchor in OWNER_AUTHORITY_ANCHORS.items() if anchor not in candidate]
    checks["part2_semantic_required_missing"] = missing_p2
    checks["owner_authority_missing"] = missing_owner
    checks["passed"] = bool(checks["passed"]) and not missing_p2 and not missing_owner
    return checks


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

    master2 = master
    part2_2 = part2
    mops: list[dict[str, object]] = []
    pops: list[dict[str, object]] = []

    for label, old, new in [
        ("queen-polarity-trust-love-safety-r7", QUEEN_OPEN_MASTER_OLD, QUEEN_OPEN_MASTER_NEW),
        ("queen-lab-uniqueness-r7", QUEEN_LAB_OLD, QUEEN_LAB_NEW),
        ("not-performance-semantic-restore-r7", NOT_PERFORMANCE_MASTER_OLD, NOT_PERFORMANCE_MASTER_NEW),
        ("after-leaving-curiosity-r7", AFTER_LEAVING_OLD, AFTER_LEAVING_NEW),
    ]:
        master2, op = replace_exact(master2, label, old, new)
        mops.append(op)

    for label, old, new in [
        ("queen-polarity-trust-love-safety-r7", QUEEN_OPEN_P2_OLD, QUEEN_OPEN_P2_NEW),
        ("queen-lab-uniqueness-r7", QUEEN_LAB_OLD, QUEEN_LAB_NEW),
        ("not-performance-semantic-restore-r7", NOT_PERFORMANCE_P2_OLD, NOT_PERFORMANCE_P2_NEW),
        ("after-leaving-curiosity-r7", AFTER_LEAVING_OLD, AFTER_LEAVING_NEW),
    ]:
        part2_2, op = replace_exact(part2_2, label, old, new)
        pops.append(op)

    if sha256_text(part1) != SOURCE_P1_SHA:
        raise RuntimeError("Part 1 changed during Part 2 semantic restoration")

    checks = semantic_audit(master, master2)
    if not checks["passed"]:
        raise RuntimeError(f"r7 semantic invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2_2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "whole_article_semantic_restoration_candidate_not_owner_final_article",
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
            "source_ledger": "SEMANTIC-TRACEABILITY-R6.json",
            "restored_unsuperseded_units": 7,
            "remaining_known_unsuperseded_lost_units": 0,
            "owner_authority_spans_preserved": True,
        },
        "detector_plan": {
            "status": "semantic_gate_first",
            "part1_affection_local": "hard-capped 6/6; no more local calls",
            "part2_paid_baseline": "recover exact already-reserved owner-integrated-r2 result; never resubmit duplicate",
            "next": "materialize exact r7 and build final traceability before any new aggregate measurement",
        },
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
