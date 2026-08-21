#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_part1_repair_r1 as base

SOURCE_MASTER_SHA = "1f2f25ce4f3f1c696ef5a66fadbf382caeef968e49812a24627102346bc82a59"
SOURCE_P1_SHA = "ae48e720cd84eb88da3430a44e240d18bd7731d7ce0a40469e455027c43a7062"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

AFFECTION_MASTER = """## Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called [*50 Things I Learned from 50 Years of Marriage*](https://dougtoft.substack.com/p/50-things-i-learned-from-50-years). One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

Kim Anami calls the sexual charge between encounters [“the simmer”](https://kimanami.com/meet-another-well-fked-man/). If we stop flirting with each other for months, I’m not going to assume our problem magically begins at bedtime. Sex is a pretty sensitive barometer for resentment, stress, health, medication, and feeling wanted. My partner matters enormously to my desire, but I don’t want to make her manufacture all of it.
"""
AFFECTION_P1 = """Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called 50 Things I Learned from 50 Years of Marriage. One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

Kim Anami calls the sexual charge between encounters “the simmer.” If we stop flirting with each other for months, I’m not going to assume our problem magically begins at bedtime. Sex is a pretty sensitive barometer for resentment, stress, health, medication, and feeling wanted. My partner matters enormously to my desire, but I don’t want to make her manufacture all of it.
"""

STI_OLD = """The STI part is easy: say what you know, or say you don’t know. Feelings aren’t. You can both mean it when you say this is only sex and still have one of you get attached afterward. If you’re both really numb or robotic about sex, maybe not."""
STI_NEW = """You can test for STIs and tell each other what you know. Attachment is less cooperative. Both of you can mean it when you say this is only sex, and then one of you wakes up attached anyway. If you’re both really numb or robotic about sex, maybe not."""

PATIENT_OLD = """All three women told me at some point that they felt like my patient. Which is true, I really was the one they asked about almost every medical, mental-health, and practical problem:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

Of course I helped. Saying, “I’m not your doctor or therapist,” every time would have been cold. But enough moments become a pattern."""
PATIENT_NEW = """All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them. They asked me about almost every medical, mental-health, and practical problem:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

I usually had some idea, so of course I answered."""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_section(text: str, start: str, end: str, replacement: str, label: str) -> tuple[str, dict[str, object]]:
    if text.count(start) != 1:
        raise RuntimeError(f"{label}: expected one start marker, found {text.count(start)}")
    a = text.index(start)
    b = text.index(end, a + len(start))
    old = text[a:b]
    new = replacement.rstrip() + "\n\n"
    return text[:a] + new + text[b:], {
        "label": label,
        "old_sha256": sha256_text(old),
        "new_sha256": sha256_text(new),
        "old_word_count": len(old.split()),
        "new_word_count": len(new.split()),
    }


def replace_exact(text: str, old: str, new: str, label: str) -> tuple[str, dict[str, object]]:
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

    master2 = master
    part1_2 = part1
    mops: list[dict[str, object]] = []
    pops: list[dict[str, object]] = []

    master2, op = replace_section(master2, "## Affection and the simmer\n", "## Can Casual Sex or a Situationship Actually Be Honest?\n", AFFECTION_MASTER, "affection-r4-compressed-functions")
    mops.append(op)
    part1_2, op = replace_section(part1_2, "Affection and the simmer\n", "Can Casual Sex or a Situationship Actually Be Honest?\n", AFFECTION_P1, "affection-r4-compressed-functions")
    pops.append(op)

    for label, old, new in [
        ("casual-sti-attachment-causal", STI_OLD, STI_NEW),
        ("maturity-patient-remove-aftercare", PATIENT_OLD, PATIENT_NEW),
    ]:
        master2, op = replace_exact(master2, old, new, label)
        mops.append(op)
        part1_2, op = replace_exact(part1_2, old, new, label)
        pops.append(op)

    if sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 r2 repair")

    checks = base.audit(master, master2)
    extra_required = {
        "affection-compressed": "I’m not going to assume our problem magically begins at bedtime",
        "sti-attachment": "Attachment is less cooperative.",
        "patient-no-aftercare": "I usually had some idea, so of course I answered.",
    }
    extra_missing = [name for name, anchor in extra_required.items() if anchor not in master2]
    checks["r2_required_missing"] = extra_missing
    checks["old_sti_antithesis_absent"] = STI_OLD not in master2
    checks["old_patient_aftercare_absent"] = "But enough moments become a pattern." not in master2
    checks["passed"] = bool(checks["passed"]) and not extra_missing and checks["old_sti_antithesis_absent"] and checks["old_patient_aftercare_absent"]
    if not checks["passed"]:
        raise RuntimeError(f"Part 1 r2 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "part1_residual_repair_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": mops, "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": pops},
            "part2": {"sha256": sha256_text(part2), "word_count_whitespace": len(part2.split()), "operations": [], "unchanged": True},
        },
        "source_aggregate_result": {
            "part1_sha256": SOURCE_P1_SHA,
            "pangram4_fraction_human": 0.9666589498519897,
            "residual_ai_segments": 3,
        },
        "detector_plan": {"part1": "fresh aggregate measurement on exact changed Part1; local residual probes are diagnostic"},
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
