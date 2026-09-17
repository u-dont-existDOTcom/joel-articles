#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PASS3_MASTER_SHA = "4f354ee1c0d87075912077b910f0c68de3d624d8a8453175bdf35047b041e07f"
PASS3_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
PASS3_P2_SHA = "c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c"
REGISTERED_P1_SHA = PASS3_P1_SHA

MONEY_OLD = """Micromanaging everything is totally different and not attractive.

If she keeps taking over with “Let me do it,” I start feeling useless. Money can make the same thing worse. A woman earning more than her man isn’t the problem. But if it turns into, “I make more, so I’m the competent adult here,” she can effeminate him in the relationship and then wonder where the polarity went. A man can wreck it from the other side by needing a successful woman to shrink so he can feel masculine.

A woman can lead wherever the man is less sure. She may know more about any particular field, even a traditionally non-feminine one. The way she leads can still preserve the polarity of roles.

“Honey, let me help you with this,” is still sexy, but pushing him out of the way is not."""
MONEY_NEW = """If she keeps taking over with “Let me do it,” I start feeling useless. Money can make the same thing worse. A woman earning more than me isn’t the problem; turning it into “I make more, so I’m the competent adult here” can effeminate me in the relationship. A man can wreck it from the other side by needing a successful woman to shrink so he can feel masculine.

She may know more than I do about any particular field, including a traditionally non-feminine one. Then I want her help. “Honey, let me help you with this,” is still sexy. Pushing me out of the way isn’t."""

GUIDANCE_OLD = """She can also receive his guidance without pretending he's always right. She might say, “Thank you, I’ll consider that. What do you think about doing it this way?” as a kind of gentle, almost hypnotic leadership. She is still influencing the direction he goes in without turning every disagreement into a contest over who is driving.

In my experience, women often prefer stronger and more direct leadership from a man:

“This is where I want to go. This is what I think we should do. Are you game?”

The woman may argue with the plan, change it, improve it, or refuse it. The masculine charge comes partly from directly offering a direction."""
GUIDANCE_NEW = """She doesn't have to pretend I'm always right either. “Thank you, I’ll consider that. What do you think about doing it this way?” can be a kind of gentle leadership: she changes the direction without making every disagreement a contest over who is driving.

In my experience, women often prefer a man to say what he wants more directly:

“This is where I want to go. This is what I think we should do. Are you game?”

She may argue with the plan, change it, improve it, or refuse it. The masculine charge comes partly from directly offering a direction."""

EXCLUSIVITY_OLD = """Those origins still matter. Property and inheritance are still built into marriage, even while modern vows ask the same institution to guarantee a permanent romantic feeling.

I haven't done any of this perfectly. At one point I tried a more radical answer: changing attraction itself. B. wanted to marry me, but I was still attracted to other women."""
EXCLUSIVITY_NEW = """Marriage still carries the property-and-inheritance structure while modern vows also ask it to guarantee a permanent romantic feeling.

At one point I tried a more literal solution: stop being attracted to anyone else. B. wanted to marry me, but I was still attracted to other women."""

P2_REPLACEMENTS = [
    ("primal-money-competence-concrete", MONEY_OLD, MONEY_NEW),
    ("primal-guidance-transition-concrete", GUIDANCE_OLD, GUIDANCE_NEW),
    ("exclusivity-history-to-personal-transition", EXCLUSIVITY_OLD, EXCLUSIVITY_NEW),
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
    parser = argparse.ArgumentParser(description="Materialize Romance detector-repair pass 4.")
    parser.add_argument("--pass3-master", type=Path, required=True)
    parser.add_argument("--pass3-part1", type=Path, required=True)
    parser.add_argument("--pass3-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.pass3_master.read_text(encoding="utf-8")
    part1 = args.pass3_part1.read_text(encoding="utf-8")
    part2 = args.pass3_part2.read_text(encoding="utf-8")

    observed = {
        "master": sha256_text(master),
        "part1": sha256_text(part1),
        "part2": sha256_text(part2),
    }
    expected = {
        "master": PASS3_MASTER_SHA,
        "part1": PASS3_P1_SHA,
        "part2": PASS3_P2_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"pass-3 source hash mismatch: expected={expected} observed={observed}")

    master4, master_ops = apply_replacements(master, P2_REPLACEMENTS)
    part2_4, p2_ops = apply_replacements(part2, P2_REPLACEMENTS)
    part1_4 = part1

    if sha256_text(part1_4) != REGISTERED_P1_SHA:
        raise RuntimeError("Part 1 changed during pass 4; detector submission is forbidden")

    checks = audit_master(master, master4)
    if not checks["passed"]:
        raise RuntimeError(f"pass-4 master invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    manifest_path = args.output_dir / "candidate-manifest.json"

    out_master.write_text(master4, encoding="utf-8")
    out_p1.write_text(part1_4, encoding="utf-8")
    out_p2.write_text(part2_4, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "candidate_not_owner_final",
        "source_pass3": observed,
        "candidate": {
            "master": {
                "path": out_master.name,
                "sha256": sha256_text(master4),
                "word_count_whitespace": len(master4.split()),
                "operations": master_ops,
                "invariant_audit": checks,
            },
            "part1": {
                "path": out_p1.name,
                "sha256": sha256_text(part1_4),
                "word_count_whitespace": len(part1_4.split()),
                "operations": [],
                "reuses_registered_detector_result": True,
            },
            "part2": {
                "path": out_p2.name,
                "sha256": sha256_text(part2_4),
                "word_count_whitespace": len(part2_4.split()),
                "operations": p2_ops,
            },
        },
        "detector_plan": {
            "part1": "no_new_call_exact_registered_hash_unchanged",
            "part2": "one_new_pangram4_measurement_via_private_selfhost",
        },
        "editorial_note": (
            "Pass 4 targets the three historically AI-labeled Part-2 regions that pass 3 never edited: "
            "money/competence polarity, the female-influence to direct-male-leadership transition, and the "
            "historical-exclusivity to personal-experiment transition. The edits remove generic explanation, "
            "make the polarity claims more lived/first-person, and preserve the owner's substantive masculine/feminine argument."
        ),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
