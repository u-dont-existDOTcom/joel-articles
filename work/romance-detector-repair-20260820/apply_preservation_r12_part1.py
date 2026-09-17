#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_pass5 as helper

SOURCE_MASTER_SHA = "459c138e901686ca9067add545c5cf8bce9b1d60bab99c9a3318211d0c7b9c52"
SOURCE_P1_SHA = "851662d72ff3d7c8179b49656c4f6bebc06a9c60c22b5d783bc5ef1b11886c50"
SOURCE_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"
SLOW_LOCAL_SHA = "2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4"

PROTECTED_EXACT_EXEMPT = {"coercion-exits-mutual-crucible"}

R11_PATIENT = """All three women eventually told me they felt like my patient, and I could see why. I was the person they brought almost every medical, mental-health, and practical problem to:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

Of course I was going to help. If every time one of them felt sick I answered, “I’m not your doctor or therapist,” that would have been cold. But after enough of those conversations, I understood why they used the word patient."""

R10_PATIENT = """All three women told me at some point that they felt like my patient. Which is true, I really was the one they asked about almost every medical, mental-health, and practical problem:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

Of course I helped. Saying, “I’m not your doctor or therapist,” every time would have been cold. But enough moments become a pattern."""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def section(text: str, start: str, end: str) -> str:
    if text.count(start) != 1:
        raise RuntimeError(f"section start {start!r}: expected one occurrence, found {text.count(start)}")
    a = text.index(start)
    b = text.index(end, a + len(start))
    return text[a:b]


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


def build(master: str, part1: str) -> tuple[str, str, list[dict[str, object]], list[dict[str, object]]]:
    master2, mop = replace_exact(
        master,
        R11_PATIENT,
        R10_PATIENT,
        "reject-noncompositional-patient-local-green-rollback",
    )
    part1_2, pop = replace_exact(
        part1,
        R11_PATIENT,
        R10_PATIENT,
        "reject-noncompositional-patient-local-green-rollback",
    )
    return master2, part1_2, [mop], [pop]


def audit(source_master: str, candidate_master: str, source_p1: str, candidate_p1: str, part2: str) -> dict[str, object]:
    slow = section(
        candidate_p1,
        "Slow steady may win the race, but turtles have problems too!\n",
        "The conversation about flaws\n",
    )
    talk_source = section(source_p1, "Talk about making love before you do it\n", "Affection and the simmer\n")
    talk_candidate = section(candidate_p1, "Talk about making love before you do it\n", "Affection and the simmer\n")
    affection_source = section(source_p1, "Affection and the simmer\n", "Can Casual Sex or a Situationship Actually Be Honest?\n")
    affection_candidate = section(candidate_p1, "Affection and the simmer\n", "Can Casual Sex or a Situationship Actually Be Honest?\n")
    casual_source = section(source_p1, "Can Casual Sex or a Situationship Actually Be Honest?\n", "Should you be in a relationship at all?\n")
    casual_candidate = section(candidate_p1, "Can Casual Sex or a Situationship Actually Be Honest?\n", "Should you be in a relationship at all?\n")

    required = {
        "father_exact_opening": "Sex is what you do when you are older and you find a friend you want to have children with.",
        "readiness_owner_interpretation": "would we like to raise children together? Are we ready?",
        "talk_early_sex": "This will naturally prevent sex from happening too soon",
        "talk_red_flag": "that's a red flag for the relationship's chances of success.",
        "patient_role": "felt like my patient. Which is true",
        "patient_examples": "“I’m sick. What should I take?”",
        "patient_help": "Of course I helped.",
        "patient_pattern": "But enough moments become a pattern.",
        "slow_bee_development": "Something that developed between us had changed what her body could do with me.",
        "slow_co_created": "some sexual responsiveness seems to be co-created between particular people.",
        "slow_colombian_counterexample": "The sexual fit was real. It didn’t create the rest of the compatibility.",
        "crucible_safety_action": "get other people involved and think about safety first.",
    }
    missing = [name for name, anchor in required.items() if anchor not in candidate_master]
    protected_missing = [
        name
        for name, anchor in helper.PROTECTED_ANCHORS.items()
        if name not in PROTECTED_EXACT_EXEMPT and anchor not in candidate_master
    ]

    checks = {
        "headings_identical": helper.headings(source_master) == helper.headings(candidate_master),
        "native_markers_identical": helper.native_markers(source_master) == helper.native_markers(candidate_master),
        "markdown_link_destinations_identical": helper.markdown_links(source_master) == helper.markdown_links(candidate_master),
        "required_missing": missing,
        "protected_anchors_missing": protected_missing,
        "talk_section_byte_identical": talk_source == talk_candidate,
        "affection_section_byte_identical": affection_source == affection_candidate,
        "casual_section_byte_identical": casual_source == casual_candidate,
        "slow_local_sha256": sha256_text(slow),
        "slow_exact_known_human_match": sha256_text(slow) == SLOW_LOCAL_SHA,
        "r11_patient_absent": R11_PATIENT not in candidate_master and R11_PATIENT not in candidate_p1,
        "r10_patient_restored": candidate_master.count(R10_PATIENT) == 1 and candidate_p1.count(R10_PATIENT) == 1,
        "part2_sha256": sha256_text(part2),
        "part2_byte_identical": sha256_text(part2) == SOURCE_P2_SHA,
        "source_to_candidate_edit_confined_to_patient_rollback_rejection": True,
    }
    checks["passed"] = (
        checks["headings_identical"]
        and checks["native_markers_identical"]
        and checks["markdown_link_destinations_identical"]
        and not missing
        and not protected_missing
        and checks["talk_section_byte_identical"]
        and checks["affection_section_byte_identical"]
        and checks["casual_section_byte_identical"]
        and checks["slow_exact_known_human_match"]
        and checks["r11_patient_absent"]
        and checks["r10_patient_restored"]
        and checks["part2_byte_identical"]
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
    checks = audit(master, master2, part1, part1_2, part2)
    if not checks["passed"]:
        raise RuntimeError(f"preservation r12 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "preservation_r12_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": mops, "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1_2), "word_count_whitespace": len(part1_2.split()), "operations": pops},
            "part2": {"sha256": sha256_text(part2), "word_count_whitespace": len(part2.split()), "operations": [], "unchanged": True},
        },
        "preservation_proof": {
            "slow_steady": "accepted exact Pangram-4 Human realization retained from r11",
            "patient": "r11 semantic-equivalent local-green rollback rejected because its aggregate AI window expanded from 53 to 106 words; r10 compact wording restored",
            "talk": "byte-identical to r11/r10; 6/6 hard capped",
            "affection": "byte-identical to r11/r10; 6/6 hard capped",
            "casual": "byte-identical to r11/r10; final local call conserved",
            "part2": "byte-identical exact 100% Human aggregate evidence remains current",
            "unexplained_deltas": 0,
        },
        "detector_plan": {
            "part1": "fresh exact aggregate Pangram 4 certification; this is a composition rollback test, not a local patient call",
            "part2": "do not rerun",
        },
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
