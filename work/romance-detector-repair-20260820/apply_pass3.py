#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PASS2_MASTER_SHA = "91b2186d1759fb5ff248363572de94354a12dacd5039c014e529efd1e72fb12e"
PASS2_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
PASS2_P2_SHA = "679daa77fb92ea71bb85716e6ece671e093b49412b149e2f5129079a204d24d2"
REGISTERED_P1_SHA = PASS2_P1_SHA

QUEEN_OPEN_OLD = """Many people are not even aware of how incredible sex can be when the polarity, trust, love & safety are all where they should be. Women have shown me that the cervix can open during sex and become intensely pleasurable for both of us. In fact, after you experience cervical sex, regular sex doesn't even seem like it's really \"sex\" anymore. It seems more like foreplay."""
QUEEN_OPEN_NEW = """Women have shown me that the cervix can open during sex and become intensely pleasurable for both of us. After you experience cervical sex, regular sex doesn't even seem like it's really \"sex\" anymore. It seems more like foreplay."""

QUEEN_DESC_OLD = """Women describe cervical and whole-body orgasms very differently from the ordinary ones based on building friction toward release. Instead, cervical orgasms are more like being taken over by a profound energy running through the whole body."""
QUEEN_DESC_NEW = """Women describe cervical and whole-body orgasms as something very different from building friction toward release—more like being taken over by a profound energy running through the whole body."""

QUEEN_LAB_OLD = """Although the peanut gallery critics and lazy fact-checkers often cry fiction on this topic, Komisaruk and Whipple showed that cervical stimulation can produce orgasm even in women with a severed spinal cord, because the vagus nerve can carry the signal without using the spinal route that clitoral orgasms use. That laboratory evidence establishes the uniqueness of the phenomenon. Kim Anami, Diana Richardson, and other popular educators and promoters of cervical orgasms further claim that these can provide days of afterglow, as well as spiritual and physical healings."""
QUEEN_LAB_NEW = """Although the peanut gallery critics and lazy fact-checkers often cry fiction on this topic, Komisaruk and Whipple showed that cervical stimulation can produce orgasm even in women with a severed spinal cord, because the vagus nerve can carry the signal without using the spinal route that clitoral orgasms use. Kim Anami, Diana Richardson, and other popular educators and promoters of cervical orgasms further claim that these can provide days of afterglow, as well as spiritual and physical healings."""

TWO_OPEN_OLD = """Even if you find your twin flame, she’s still only one person, and that's more of a problem than it seems at first. Polarity does not make two people sufficient for each other. A couple still needs friends and community."""
TWO_OPEN_NEW = """Even if I found my twin flame, she'd still be one person. The polarity could be perfect and we'd still need other people around us."""

TWO_BURDEN_OLD = """When you rely on your partner to provide nearly all the friendship, family, therapy, and spiritual meaning, the burden is overwhelming. That's too many hats to wear even for a hat model. Besides all that, there's no security when two people have to cover all the life essentials: housing, money, children, emotional, health, and other crises. Who even has time for the relationship itself at that point?"""
TWO_BURDEN_NEW = """There's a practical side too. Two people covering housing, money, children, health, emotional crises, everything—there's no backup when one of them goes down. Who even has time for the relationship itself at that point?"""

TWO_CAVEAT_OLD = """A very strong couple without much trauma can often do well without community, although it’s a struggle and I think it’s rare. A weak couple might not work even with a community if both people are too weak individually. It depends on the couple."""
TWO_CAVEAT_NEW = """Maybe an unusually strong couple can get away without much community. I think that's rare, and community can't rescue a relationship if both people are falling apart anyway."""

TWO_SHARED_OLD = """But having more people around the relationship changes what the two people have to carry. Mutual friends can notice patterns neither person sees. Somebody else can comfort your partner when you have become the wrong person to do it. And when people actually know both of you, they have some chance of telling when the story they’re hearing does not match the person they know."""
TWO_SHARED_NEW = """What we were missing wasn't just more friends on each side. We needed people who actually knew both of us. Mutual friends can notice patterns neither person sees. Somebody else can comfort your partner when you've become the wrong person to do it. And if somebody knows both of you, they have a chance of noticing when the story they're hearing doesn't match the person they know."""

P2_REPLACEMENTS = [
    ("queen-remove-generic-setup", QUEEN_OPEN_OLD, QUEEN_OPEN_NEW),
    ("queen-collapse-taxonomy", QUEEN_DESC_OLD, QUEEN_DESC_NEW),
    ("queen-remove-result-aftercare", QUEEN_LAB_OLD, QUEEN_LAB_NEW),
    ("two-pillars-personal-opening", TWO_OPEN_OLD, TWO_OPEN_NEW),
    ("two-pillars-route-practical-burden", TWO_BURDEN_OLD, TWO_BURDEN_NEW),
    ("two-pillars-simplify-caveat", TWO_CAVEAT_OLD, TWO_CAVEAT_NEW),
    ("two-pillars-shared-reality-check", TWO_SHARED_OLD, TWO_SHARED_NEW),
]

PROTECTED_ANCHORS = {
    "opening-father-question": "I asked my dad about sex when I was five",
    "bear-terminal-callback": "Bear, sex can be what you do when you’re older",
    "agape-eros-distinction": "Agape or divine love does two jobs at once to rescue the erotic love.",
    "coercion-exits-mutual-crucible": "If you're scared to say no, scared to tell the truth, or scared of what happens if you leave",
    "children-survive-romance": "Never recruit children into the adult war.",
    "community-around-dyad": "Two Pillars Don't Hold The Roof Up",
    "primal-owner-argument": "Primal attraction: channeling the Divine Masculine & Feminine",
    "gandarussa-preserved": "Gandarussa",
    "identity-hale-not-heidi": "A friend of mine was talking about PTSD recently",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def apply_replacements(text: str, replacements: list[tuple[str, str, str]]) -> tuple[str, list[dict[str, object]]]:
    audit: list[dict[str, object]] = []
    for label, old, new in replacements:
        count = text.count(old)
        if count != 1:
            raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
        text = text.replace(old, new, 1)
        audit.append({
            "label": label,
            "source_occurrences": count,
            "old_sha256": sha256_text(old),
            "new_sha256": sha256_text(new),
        })
    return text, audit


def headings(text: str) -> list[str]:
    return [line for line in text.splitlines() if re.match(r"^#{1,6}\s", line)]


def native_markers(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.startswith("[NATIVE ")]


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\]\(([^)]+)\)", text)


def audit_master(source: str, candidate: str) -> dict[str, object]:
    missing = [name for name, anchor in PROTECTED_ANCHORS.items() if anchor not in candidate]
    checks = {
        "headings_identical": headings(source) == headings(candidate),
        "native_markers_identical": native_markers(source) == native_markers(candidate),
        "markdown_link_destinations_identical": markdown_links(source) == markdown_links(candidate),
        "protected_anchors_missing": missing,
    }
    checks["passed"] = (
        checks["headings_identical"]
        and checks["native_markers_identical"]
        and checks["markdown_link_destinations_identical"]
        and not missing
    )
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize Romance detector-repair pass 3.")
    parser.add_argument("--pass2-master", type=Path, required=True)
    parser.add_argument("--pass2-part1", type=Path, required=True)
    parser.add_argument("--pass2-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.pass2_master.read_text(encoding="utf-8")
    part1 = args.pass2_part1.read_text(encoding="utf-8")
    part2 = args.pass2_part2.read_text(encoding="utf-8")

    observed = {
        "master": sha256_text(master),
        "part1": sha256_text(part1),
        "part2": sha256_text(part2),
    }
    expected = {
        "master": PASS2_MASTER_SHA,
        "part1": PASS2_P1_SHA,
        "part2": PASS2_P2_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"pass-2 source hash mismatch: expected={expected} observed={observed}")

    master3, master_ops = apply_replacements(master, P2_REPLACEMENTS)
    part2_3, p2_ops = apply_replacements(part2, P2_REPLACEMENTS)
    part1_3 = part1

    if sha256_text(part1_3) != REGISTERED_P1_SHA:
        raise RuntimeError("Part 1 changed during pass 3; detector submission is forbidden")

    checks = audit_master(master, master3)
    if not checks["passed"]:
        raise RuntimeError(f"pass-3 master invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    manifest_path = args.output_dir / "candidate-manifest.json"

    out_master.write_text(master3, encoding="utf-8")
    out_p1.write_text(part1_3, encoding="utf-8")
    out_p2.write_text(part2_3, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "candidate_not_owner_final",
        "source_pass2": observed,
        "candidate": {
            "master": {
                "path": out_master.name,
                "sha256": sha256_text(master3),
                "word_count_whitespace": len(master3.split()),
                "operations": master_ops,
                "invariant_audit": checks,
            },
            "part1": {
                "path": out_p1.name,
                "sha256": sha256_text(part1_3),
                "word_count_whitespace": len(part1_3.split()),
                "operations": [],
                "reuses_registered_detector_result": True,
            },
            "part2": {
                "path": out_p2.name,
                "sha256": sha256_text(part2_3),
                "word_count_whitespace": len(part2_3.split()),
                "operations": p2_ops,
            },
        },
        "detector_plan": {
            "part1": "no_new_call_exact_registered_hash_unchanged",
            "part2": "one_new_pangram4_measurement_only",
        },
        "editorial_note": (
            "Pass 3 targets the five likely residual Part-2 AI segments: two Queen-of-Orgasms windows and "
            "three Two-Pillars/community windows. The Two-Pillars edits remove duplication of the earlier "
            "whole-world section while preserving the practical-resilience caveat and shared-reality-check function."
        ),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
