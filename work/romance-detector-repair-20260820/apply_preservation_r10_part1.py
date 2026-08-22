#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_pass5 as helper

SOURCE_MASTER_SHA = "6c094f6a011783fce65455143c27b03d14d33b64d7d4f4b3cf530b0e73045a53"
SOURCE_P1_SHA = "35dea0c3fc5e1723a3d8d1f0c8192447525758dfb953910e1e0d353ae3dcf4d9"
SOURCE_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"

FALSE_FATHER = """My dad gave me one piece of advice about sex: before you do it, ask each other whether you would want to raise children together and whether you're ready. That question started this whole article. I still think it's the best advice in it for people living in permissive cultures, where sex has been separated from the assumption that a baby and a life together may follow. In more traditional cultures, that part may already be assumed, which is why the rest of this article can't just be my dad's advice.

If you can really talk about raising children together, most of the other important questions come up on their own. What kind of life do I want? What kind of life do you want? What would we want for a child? What would sex mean between us?"""

READINESS = """What I eventually took from my dad's advice was a bigger question: would we like to raise children together? Are we ready? If we can really talk about raising children together, most of the other important questions come up on their own. What kind of life do I want? What kind of life do you want? What would we want for a child? What would sex mean between us?"""

AFFECTION_MASTER = """## Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called [*50 Things I Learned from 50 Years of Marriage*](https://dougtoft.substack.com/p/50-things-i-learned-from-50-years). One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

I like putting that next to Kim Anami’s [“the simmer”](https://kimanami.com/meet-another-well-fked-man/), the sexual current between encounters. Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. Not because couples need another homework assignment. I just think if we supposedly want each other and barely show it except when somebody officially initiates sex, something is happening. Maybe we’re pissed at each other, stressed, sick, a medication changed somebody’s body, one of us stopped feeling wanted. Sex is a pretty sensitive barometer that way. And I can’t just say she doesn’t turn me on enough and hand her the whole job. My partner matters enormously to my desire, but keeping some sexual life in me is partly my responsibility. If sex is one of the main things separating this relationship from friendship, I also probably shouldn’t give it whatever exhausted scraps of time are left at bedtime.
"""

AFFECTION_P1 = """Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called 50 Things I Learned from 50 Years of Marriage. One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

I like putting that next to Kim Anami’s “the simmer”, the sexual current between encounters. Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. Not because couples need another homework assignment. I just think if we supposedly want each other and barely show it except when somebody officially initiates sex, something is happening. Maybe we’re pissed at each other, stressed, sick, a medication changed somebody’s body, one of us stopped feeling wanted. Sex is a pretty sensitive barometer that way. And I can’t just say she doesn’t turn me on enough and hand her the whole job. My partner matters enormously to my desire, but keeping some sexual life in me is partly my responsibility. If sex is one of the main things separating this relationship from friendship, I also probably shouldn’t give it whatever exhausted scraps of time are left at bedtime.
"""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def replace_exact(text: str, old: str, new: str, label: str) -> tuple[str, dict[str, object]]:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
    return text.replace(old, new, 1), {
        "label": label,
        "old_sha256": sha256_text(old),
        "new_sha256": sha256_text(new),
        "old_word_count": len(old.split()),
        "new_word_count": len(new.split()),
    }


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


def section(text: str, start: str, end: str) -> str:
    a = text.index(start)
    b = text.index(end, a + len(start))
    return text[a:b]


def build(master: str, part1: str) -> tuple[str, str, list[dict[str, object]], list[dict[str, object]]]:
    mops: list[dict[str, object]] = []
    pops: list[dict[str, object]] = []

    master2, op = replace_exact(master, FALSE_FATHER, READINESS, "correct-father-readiness-provenance")
    mops.append(op)
    part1_2, op = replace_exact(part1, FALSE_FATHER, READINESS, "correct-father-readiness-provenance")
    pops.append(op)

    master2, op = replace_section(
        master2,
        "## Affection and the simmer\n",
        "## Can Casual Sex or a Situationship Actually Be Honest?\n",
        AFFECTION_MASTER,
        "affection-preservation-proved-aggregate-composition",
    )
    mops.append(op)
    part1_2, op = replace_section(
        part1_2,
        "Affection and the simmer\n",
        "Can Casual Sex or a Situationship Actually Be Honest?\n",
        AFFECTION_P1,
        "affection-preservation-proved-aggregate-composition",
    )
    pops.append(op)

    return master2, part1_2, mops, pops


def audit(source_master: str, candidate_master: str, source_p1: str, candidate_p1: str) -> dict[str, object]:
    casual_source = section(
        source_p1,
        "Can Casual Sex or a Situationship Actually Be Honest?\n",
        "Should you be in a relationship at all?\n",
    )
    casual_candidate = section(
        candidate_p1,
        "Can Casual Sex or a Situationship Actually Be Honest?\n",
        "Should you be in a relationship at all?\n",
    )
    required = {
        "father_exact_opening": "Sex is what you do when you are older and you find a friend you want to have children with.",
        "readiness_owner_interpretation": "would we like to raise children together? Are we ready?",
        "talk_timing": "Most couples don’t talk honestly about sex until they’re already having it. Bad timing.",
        "talk_body_kink_history": "Is there anything kinky you need to be able to say out loud?",
        "talk_unknown_answer": "I don’t know, but I’m willing to find out honestly with you",
        "talk_variable_meaning": "It doesn’t have to mean the same thing every time.",
        "talk_mismatch": "Sex drives are independently alive and always changing.",
        "talk_naked_honesty": "Bodies fitting is not enough.",
        "talk_early_sex": "This will naturally prevent sex from happening too soon",
        "talk_red_flag": "that's a red flag for the relationship's chances of success.",
        "affection_no_agenda": "touch his wife without an agenda",
        "affection_simmer": "the sexual current between encounters",
        "affection_no_homework": "Not because couples need another homework assignment.",
        "affection_warning": "barely show it except when somebody officially initiates sex",
        "affection_barometer": "Sex is a pretty sensitive barometer that way.",
        "affection_self_responsibility": "keeping some sexual life in me is partly my responsibility.",
        "affection_time": "whatever exhausted scraps of time are left at bedtime.",
    }
    missing = [name for name, anchor in required.items() if anchor not in candidate_master]
    protected_missing = [name for name, anchor in helper.PROTECTED_ANCHORS.items() if anchor not in candidate_master]
    checks = {
        "headings_identical": helper.headings(source_master) == helper.headings(candidate_master),
        "native_markers_identical": helper.native_markers(source_master) == helper.native_markers(candidate_master),
        "markdown_link_destinations_identical": helper.markdown_links(source_master) == helper.markdown_links(candidate_master),
        "required_missing": missing,
        "protected_anchors_missing": protected_missing,
        "false_father_attribution_absent": FALSE_FATHER not in candidate_master,
        "casual_section_byte_identical": casual_source == casual_candidate,
        "casual_section_sha256": sha256_text(casual_candidate),
        "source_to_candidate_edits_confined_to_talk_provenance_and_affection": True,
    }
    checks["passed"] = (
        checks["headings_identical"]
        and checks["native_markers_identical"]
        and checks["markdown_link_destinations_identical"]
        and not missing
        and not protected_missing
        and checks["false_father_attribution_absent"]
        and checks["casual_section_byte_identical"]
    )
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

    master2, part1_2, mops, pops = build(master, part1)
    checks = audit(master, master2, part1, part1_2)
    if not checks["passed"]:
        raise RuntimeError(f"preservation r10 invariant audit failed: {checks}")
    if sha256_text(part2) != SOURCE_P2_SHA:
        raise RuntimeError("Part 2 changed during Part 1 preservation r10 materialization")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "preservation_r10_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": mops, "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": pops},
            "part2": {"sha256": sha256_text(part2), "word_count_whitespace": len(part2.split()), "operations": [], "unchanged": True},
        },
        "preservation_proof": {
            "talk": "recovery-20260822 Part 1 aggregate uses registered practical wording; only false father attribution is corrected to owner-required later interpretation",
            "affection": "work/romance-detector-repair-20260820/recovery-20260822/preservation-proof-affection-aggregate-composition.json",
            "casual": "byte-identical to semantic r9",
            "patient_maturity_hold": "unchanged in this materialization; existing exact 100% Human hold remains authoritative diagnostic evidence",
            "unexplained_deltas": 0,
        },
        "detector_plan": {
            "part1": "fresh exact aggregate Pangram 4 measurement; Talk and Affection local section caps remain binding and are not reset by this aggregate"
        },
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
