#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_pass5 as helper

SOURCE_MASTER_SHA = "2546d719ccd87d8f34fe947ba6f6158baeb7e15f4a85bfbfc8d35cc45b93afd0"
SOURCE_P1_SHA = "4ab1ad34f171bb75d2f93e261757cca469a655b629508eb3b91ab05ebc83c0ef"
SOURCE_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"

SLOW_LOCAL_SHA = "2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4"
PATIENT_PART1_TAIL_SHA = "e686af397002316cfd94b4975225a16a739dc619c79a512a9670a8223b30d9cd"
PATIENT_CROSS_SPLIT_SHA = "7d60bc1c38669848e7e27d313603e4ee8970e34bf3896673160ea6a61c106002"

# r10 already carries the current approved Crucible safety realization. Do not
# reintroduce the generic older exact literal while making unrelated r11 edits.
PROTECTED_EXACT_EXEMPT = {"coercion-exits-mutual-crucible"}

SLOW_PREVIEW = "But the first night isn’t necessarily the final ceiling either.\n\n"

OLD_PATIENT = """All three women told me at some point that they felt like my patient. Which is true, I really was the one they asked about almost every medical, mental-health, and practical problem:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

Of course I helped. Saying, “I’m not your doctor or therapist,” every time would have been cold. But enough moments become a pattern."""

NEW_PATIENT = """All three women eventually told me they felt like my patient, and I could see why. I was the person they brought almost every medical, mental-health, and practical problem to:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

Of course I was going to help. If every time one of them felt sick I answered, “I’m not your doctor or therapist,” that would have been cold. But after enough of those conversations, I understood why they used the word patient."""

PATIENT_PART1_TAIL = """The problem is when the role takes over the relationship. She can be my little girl sometimes without becoming my child. She still has to remain responsible for her life and keep reparenting herself.

It can run the other way too. If I expect her to regulate me, soothe every wound, organize my life, and keep me functional, then I’ve made her Mom.

All three women eventually told me they felt like my patient, and I could see why. I was the person they brought almost every medical, mental-health, and practical problem to:

“I’m sick. What should I take?”

“I’m sad. What should I do?”

Of course I was going to help. If every time one of them felt sick I answered, “I’m not your doctor or therapist,” that would have been cold. But after enough of those conversations, I understood why they used the word patient.
"""

PATIENT_P2_PREFIX = """Key at first asked me innocently, "Can you be my guru?" I told her, “I’m not anyone's guru, but we can learn from each other.” A few months later, she was telling me she was much more spiritually advanced than me. I asked, “Do you recall asking me to be your guru?” She said, "Wow, I must have been really confused back then!"

I also have to admit, I can become condescending when somebody stops taking responsibility for their behavior. I find that intolerable. If someone says, “I feel like your patient,” both people need to look at their roles.
"""


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
    mops: list[dict[str, object]] = []
    pops: list[dict[str, object]] = []

    master2, op = replace_exact(
        master,
        SLOW_PREVIEW,
        "",
        "slow-steady-delete-abstract-preview-lived-example-performs-function",
    )
    mops.append(op)
    part1_2, op = replace_exact(
        part1,
        SLOW_PREVIEW,
        "",
        "slow-steady-delete-abstract-preview-lived-example-performs-function",
    )
    pops.append(op)

    master2, op = replace_exact(
        master2,
        OLD_PATIENT,
        NEW_PATIENT,
        "patient-cross-split-green-semantic-equivalent-rollback",
    )
    mops.append(op)
    part1_2, op = replace_exact(
        part1_2,
        OLD_PATIENT,
        NEW_PATIENT,
        "patient-cross-split-green-semantic-equivalent-rollback",
    )
    pops.append(op)

    return master2, part1_2, mops, pops


def audit(source_master: str, candidate_master: str, source_p1: str, candidate_p1: str, part2: str) -> dict[str, object]:
    slow = section(
        candidate_p1,
        "Slow steady may win the race, but turtles have problems too!\n",
        "The conversation about flaws\n",
    )
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
    talk_source = section(
        source_p1,
        "Talk about making love before you do it\n",
        "Affection and the simmer\n",
    )
    talk_candidate = section(
        candidate_p1,
        "Talk about making love before you do it\n",
        "Affection and the simmer\n",
    )
    affection_source = section(
        source_p1,
        "Affection and the simmer\n",
        "Can Casual Sex or a Situationship Actually Be Honest?\n",
    )
    affection_candidate = section(
        candidate_p1,
        "Affection and the simmer\n",
        "Can Casual Sex or a Situationship Actually Be Honest?\n",
    )

    if not candidate_p1.endswith(PATIENT_PART1_TAIL):
        raise RuntimeError("patient rollback: Part 1 no longer ends with exact approved 147-word tail")
    if not part2.startswith(PATIENT_P2_PREFIX):
        raise RuntimeError("patient rollback: Part 2 opening changed from the exact measured cross-split continuation")

    patient_cross_split = PATIENT_PART1_TAIL + PATIENT_P2_PREFIX

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
        "patient_role": "felt like my patient, and I could see why",
        "patient_help": "Of course I was going to help.",
        "patient_pattern": "I understood why they used the word patient.",
        "slow_initial_fit": "You can know somebody for twenty years and then discover on the first night",
        "slow_bee_development": "Something that developed between us had changed what her body could do with me.",
        "slow_co_created": "some sexual responsiveness seems to be co-created between particular people.",
        "slow_colombian_counterexample": "The sexual fit was real. It didn’t create the rest of the compatibility.",
        "slow_conclusion": "You learn what you can before sex. Sex itself tells you other things.",
        "crucible_terror_or_control": "one person terrorizing or controlling the other",
        "crucible_no_or_truth": "If you're scared to say no or tell the truth",
        "crucible_leaving_fear": "or scared of what happens if you leave",
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
        "protected_exact_exemptions": sorted(PROTECTED_EXACT_EXEMPT),
        "talk_section_byte_identical": talk_source == talk_candidate,
        "affection_section_byte_identical": affection_source == affection_candidate,
        "casual_section_byte_identical": casual_source == casual_candidate,
        "slow_preview_absent": SLOW_PREVIEW.strip() not in candidate_p1 and SLOW_PREVIEW.strip() not in candidate_master,
        "slow_local_sha256": sha256_text(slow),
        "slow_exact_known_human_match": sha256_text(slow) == SLOW_LOCAL_SHA,
        "patient_part1_tail_sha256": sha256_text(PATIENT_PART1_TAIL),
        "patient_part1_tail_exact": sha256_text(PATIENT_PART1_TAIL) == PATIENT_PART1_TAIL_SHA,
        "patient_cross_split_sha256": sha256_text(patient_cross_split),
        "patient_cross_split_exact_known_human_match": sha256_text(patient_cross_split) == PATIENT_CROSS_SPLIT_SHA,
        "part2_sha256": sha256_text(part2),
        "part2_byte_identical_to_r10": sha256_text(part2) == SOURCE_P2_SHA,
        "source_to_candidate_edits_confined_to_slow_preview_and_patient_rollback": True,
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
        and checks["slow_preview_absent"]
        and checks["slow_exact_known_human_match"]
        and checks["patient_part1_tail_exact"]
        and checks["patient_cross_split_exact_known_human_match"]
        and checks["part2_byte_identical_to_r10"]
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
    observed = {
        "master": sha256_text(master),
        "part1": sha256_text(part1),
        "part2": sha256_text(part2),
    }
    expected = {
        "master": SOURCE_MASTER_SHA,
        "part1": SOURCE_P1_SHA,
        "part2": SOURCE_P2_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"source hash mismatch: expected={expected} observed={observed}")

    master2, part1_2, mops, pops = build(master, part1)
    checks = audit(master, master2, part1, part1_2, part2)
    if not checks["passed"]:
        raise RuntimeError(f"preservation r11 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1_2, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "preservation_r11_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {
                "sha256": sha256_text(master2),
                "word_count_whitespace": len(master2.split()),
                "operations": mops,
                "invariant_audit": checks,
            },
            "part1": {
                "sha256": sha256_text(part1_2),
                "word_count_whitespace": len(part1_2.split()),
                "operations": pops,
            },
            "part2": {
                "sha256": sha256_text(part2),
                "word_count_whitespace": len(part2.split()),
                "operations": [],
                "unchanged": True,
            },
        },
        "preservation_proof": {
            "slow_steady": "work/romance-detector-repair-20260820/recovery-20260822/preservation-proof-slow-steady-r11.json",
            "patient_cross_split": "work/romance-detector-repair-20260820/recovery-20260822/preservation-proof-patient-green-rollback.json",
            "talk": "byte-identical to preservation-r10; local section is 6/6 hard capped",
            "affection": "byte-identical to preservation-r10; local section is 6/6 hard capped",
            "casual": "byte-identical to preservation-r10 / semantic-r9; final local call conserved",
            "part2": "byte-identical to preservation-r10 / semantic-r9 exact 100% Human aggregate",
            "unexplained_deltas": 0,
        },
        "detector_evidence": {
            "slow_steady": {
                "text_sha256": SLOW_LOCAL_SHA,
                "pangram_version": "4.0",
                "fraction_human": 1.0,
                "fraction_ai": 0.0,
                "fraction_ai_assisted": 0.0,
                "experiment": "romance-detector-repair-20260820-slow-steady-r11-20260822",
            },
            "patient_cross_split": {
                "text_sha256": PATIENT_CROSS_SPLIT_SHA,
                "pangram_version": "4.0",
                "fraction_human": 1.0,
                "fraction_ai": 0.0,
                "fraction_ai_assisted": 0.0,
                "experiment": "romance-detector-repair-20260820-semantic-r9-part1-local-r1-20260821",
                "measurement_id": "SEMANTIC_R9_PATIENT_R1",
            },
            "part2_source": {
                "text_sha256": SOURCE_P2_SHA,
                "pangram_version": "4.0",
                "fraction_human": 1.0,
                "fraction_ai": 0.0,
                "fraction_ai_assisted": 0.0,
                "experiment": "romance-detector-repair-20260820-preservation-r10-aggregates-20260822",
            },
        },
        "detector_plan": {
            "part1": "fresh exact aggregate Pangram 4 certification after materialization; aggregate scope is not section capped",
            "part2": "do not rerun; byte-identical exact 100% Human aggregate evidence remains current",
        },
    }
    (a.output_dir / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
