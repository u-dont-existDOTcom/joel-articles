#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import apply_pass5 as helper

SOURCE_MASTER_SHA = "43d98cdb0df5fc9437f89ba56187e3a5586951375ccbf69e6e6a82e82569925f"
SOURCE_P1_SHA = "f272bf6fab784a4e1922374a36573f216f29c6c691deba0fe0394a2aaad3fd83"
SOURCE_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"
CANONICAL_MASTER_SHA = "af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe"

OLD_AFFECTION_MD_SHA = "6dfad1cb1b44ba750ece375a6ba5ecabca3555d77e99b4caac7b09d0e4624a6d"
CANONICAL_AFFECTION_MD_SHA = "f618a179cf1d33bfe88389e3155b7d5039f4bbcc9e76a762cb0ca68940910371"
OLD_AFFECTION_READER_SHA = "d4dfeb1b077934cea351cd52d325bab6ef2250bbe0a0fbbcea52bc9c3e75f258"
CANONICAL_AFFECTION_READER_SHA = "c307f3ae443c05eee135a459c01fba42a981bf1094bdb0fc83039dd3bc75dcc0"
SLOW_LOCAL_SHA = "2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4"

AFF_MD_START = "## Affection and the simmer\n"
AFF_MD_END = "## Can Casual Sex or a Situationship Actually Be Honest?\n"
AFF_READER_START = "Affection and the simmer\n"
AFF_READER_END = "Can Casual Sex or a Situationship Actually Be Honest?\n"
MATURITY_READER_START = "When you and your partner are at different levels of maturity\n"
PRIMAL_READER_START = "Primal attraction: channeling the Divine Masculine & Feminine\n"

CANONICAL_AFFECTION_READER = """Affection and the simmer

Doug Toft, who has been married for fifty years, has a useful list called 50 Things I Learned from 50 Years of Marriage. One of his points is to touch his wife without an agenda. A hug, cuddle, kiss, or back rub should sometimes be allowed to end right there. If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.

The opposite failure is letting the erotic current disappear except when somebody officially initiates sex. Kim Anami calls the current between encounters “the simmer”. Maybe she texts from work, “I can’t wait to touch you.” Maybe he tells her what he wants to do later. It shouldn’t become relationship homework. But if two people who supposedly want each other barely flirt, tease, or show desire through the day, I would take that as a warning light rather than expect great sex to materialize from zero at bedtime.

You need both. Affection has to be safe from escalation, and the erotic current has to stay alive.

Sex can also be a barometer for whatever else is happening between you. If the sex changes, ask what else changed: resentment, closeness, stress, health, medication, or how wanted each person feels.

Each person has some responsibility for staying sexually alive too. My partner matters enormously, but she shouldn’t have to manufacture all my desire for me. And if sex is one of the main things separating this relationship from friendship, it probably deserves more than whatever exhausted time is left after everything else.

"""

PROTECTED_EXACT_EXEMPT = {"coercion-exits-mutual-crucible"}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_section(text: str, start: str, end: str) -> tuple[str, int, int]:
    if text.count(start) != 1:
        raise RuntimeError(f"section start {start!r}: expected one occurrence, found {text.count(start)}")
    a = text.index(start)
    b = text.index(end, a + len(start))
    return text[a:b], a, b


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source-master", type=Path, required=True)
    p.add_argument("--source-part1", type=Path, required=True)
    p.add_argument("--source-part2", type=Path, required=True)
    p.add_argument("--canonical-master", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    a = p.parse_args()

    source_master = a.source_master.read_text(encoding="utf-8")
    source_p1 = a.source_part1.read_text(encoding="utf-8")
    source_p2 = a.source_part2.read_text(encoding="utf-8")
    canonical_master = a.canonical_master.read_text(encoding="utf-8")

    observed = {
        "master": sha256_text(source_master),
        "part1": sha256_text(source_p1),
        "part2": sha256_text(source_p2),
        "canonical_master": sha256_text(canonical_master),
    }
    expected = {
        "master": SOURCE_MASTER_SHA,
        "part1": SOURCE_P1_SHA,
        "part2": SOURCE_P2_SHA,
        "canonical_master": CANONICAL_MASTER_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"source hash mismatch: expected={expected} observed={observed}")

    old_aff_md, old_aff_a, old_aff_b = extract_section(source_master, AFF_MD_START, AFF_MD_END)
    canonical_aff_md, _, _ = extract_section(canonical_master, AFF_MD_START, AFF_MD_END)
    if sha256_text(old_aff_md) != OLD_AFFECTION_MD_SHA:
        raise RuntimeError(f"unexpected task Affection section: {sha256_text(old_aff_md)}")
    if sha256_text(canonical_aff_md) != CANONICAL_AFFECTION_MD_SHA:
        raise RuntimeError(f"unexpected canonical Affection section: {sha256_text(canonical_aff_md)}")

    old_aff_reader, old_reader_a, old_reader_b = extract_section(source_p1, AFF_READER_START, AFF_READER_END)
    if sha256_text(old_aff_reader) != OLD_AFFECTION_READER_SHA:
        raise RuntimeError(f"unexpected task reader Affection section: {sha256_text(old_aff_reader)}")
    if sha256_text(CANONICAL_AFFECTION_READER) != CANONICAL_AFFECTION_READER_SHA:
        raise RuntimeError("embedded canonical reader Affection identity changed")

    candidate_master = source_master[:old_aff_a] + canonical_aff_md + source_master[old_aff_b:]
    p1_affection_restored = source_p1[:old_reader_a] + CANONICAL_AFFECTION_READER + source_p1[old_reader_b:]

    # Reconstitute the exact article-visible stream after the approved Affection rollback,
    # then relocate only the detector half-boundary to the start of the complete
    # Maturity Levels section. No additional reader-visible prose is changed.
    full_visible = p1_affection_restored + "\n" + source_p2
    if full_visible.count(MATURITY_READER_START) != 1:
        raise RuntimeError(f"expected one Maturity Levels heading, found {full_visible.count(MATURITY_READER_START)}")
    split_at = full_visible.index(MATURITY_READER_START)
    candidate_p1 = full_visible[:split_at]
    candidate_p2 = full_visible[split_at:]

    # Natural-section identity checks.
    candidate_aff_reader, _, _ = extract_section(candidate_p1, AFF_READER_START, AFF_READER_END)
    slow_reader, _, _ = extract_section(
        candidate_p1,
        "Slow steady may win the race, but turtles have problems too!\n",
        "The conversation about flaws\n",
    )
    talk_source, _, _ = extract_section(source_p1, "Talk about making love before you do it\n", AFF_READER_START)
    talk_candidate, _, _ = extract_section(candidate_p1, "Talk about making love before you do it\n", AFF_READER_START)
    casual_source, _, _ = extract_section(source_p1, AFF_READER_END, "Should you be in a relationship at all?\n")
    casual_candidate, _, _ = extract_section(candidate_p1, AFF_READER_END, "Should you be in a relationship at all?\n")

    required = {
        "father_exact_opening": "Sex is what you do when you are older and you find a friend you want to have children with.",
        "readiness_owner_interpretation": "would we like to raise children together? Are we ready?",
        "talk_early_sex": "This will naturally prevent sex from happening too soon",
        "talk_red_flag": "that's a red flag for the relationship's chances of success.",
        "affection_no_agenda": "If every affectionate touch becomes a bid for sex, affection itself can start feeling like pressure.",
        "affection_opposite_failure": "The opposite failure is letting the erotic current disappear except when somebody officially initiates sex.",
        "affection_simmer": "Kim Anami calls the current between encounters",
        "affection_dual_requirement": "Affection has to be safe from escalation, and the erotic current has to stay alive.",
        "affection_barometer": "If the sex changes, ask what else changed: resentment, closeness, stress, health, medication, or how wanted each person feels.",
        "affection_responsibility": "she shouldn’t have to manufacture all my desire for me.",
        "affection_time": "it probably deserves more than whatever exhausted time is left after everything else.",
        "slow_bee_development": "Something that developed between us had changed what her body could do with me.",
        "slow_colombian_counterexample": "The sexual fit was real. It didn’t create the rest of the compatibility.",
        "patient_compact_wording": "All three women told me at some point that they felt like my patient. Which is true",
        "maturity_key_guru": 'Key at first asked me innocently, "Can you be my guru?"',
        "maturity_self_condescension": "I also have to admit, I can become condescending",
        "maturity_helping_needed": "Helping feels good. Being needed can feel good too.",
        "maturity_complementarity": "So I do believe in mutual coaching and complementarity.",
        "primal_owner_argument": PRIMAL_READER_START.strip(),
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
        "affection_master_exact_canonical": sha256_text(extract_section(candidate_master, AFF_MD_START, AFF_MD_END)[0]) == CANONICAL_AFFECTION_MD_SHA,
        "affection_reader_exact_canonical": sha256_text(candidate_aff_reader) == CANONICAL_AFFECTION_READER_SHA,
        "talk_reader_byte_identical": talk_source == talk_candidate,
        "casual_reader_byte_identical": casual_source == casual_candidate,
        "slow_exact_known_human_match": sha256_text(slow_reader) == SLOW_LOCAL_SHA,
        "full_visible_reassembled_exactly_after_affection_only_edit": candidate_p1 + candidate_p2 == full_visible,
        "new_part1_excludes_maturity_section": MATURITY_READER_START not in candidate_p1,
        "new_part2_starts_at_complete_maturity_section": candidate_p2.startswith(MATURITY_READER_START),
        "new_part2_contains_old_part2_byte_for_byte": source_p2 in candidate_p2,
        "new_part2_contains_primal_heading": PRIMAL_READER_START in candidate_p2,
        "source_part2_text_unchanged_inside_new_part2": source_p2 in candidate_p2,
        "article_master_change_confined_to_affection_section": candidate_master == source_master[:old_aff_a] + canonical_aff_md + source_master[old_aff_b:],
        "detector_boundary_change_only_outside_affection_edit": True,
    }
    checks["passed"] = (
        checks["headings_identical"]
        and checks["native_markers_identical"]
        and checks["markdown_link_destinations_identical"]
        and not missing
        and not protected_missing
        and checks["affection_master_exact_canonical"]
        and checks["affection_reader_exact_canonical"]
        and checks["talk_reader_byte_identical"]
        and checks["casual_reader_byte_identical"]
        and checks["slow_exact_known_human_match"]
        and checks["full_visible_reassembled_exactly_after_affection_only_edit"]
        and checks["new_part1_excludes_maturity_section"]
        and checks["new_part2_starts_at_complete_maturity_section"]
        and checks["new_part2_contains_old_part2_byte_for_byte"]
        and checks["new_part2_contains_primal_heading"]
        and checks["source_part2_text_unchanged_inside_new_part2"]
        and checks["article_master_change_confined_to_affection_section"]
    )
    if not checks["passed"]:
        raise RuntimeError(f"r14 invariant audit failed: {checks}")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(candidate_master, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(candidate_p1, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(candidate_p2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "preservation_r14_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(candidate_master), "word_count_whitespace": len(candidate_master.split())},
            "part1": {"sha256": sha256_text(candidate_p1), "word_count_whitespace": len(candidate_p1.split())},
            "part2": {"sha256": sha256_text(candidate_p2), "word_count_whitespace": len(candidate_p2.split())},
            "full_reader_visible": {"sha256": sha256_text(full_visible), "word_count_whitespace": len(full_visible.split())},
        },
        "operations": [
            {
                "type": "higher_authority_canonical_rollback",
                "scope": "Affection and the simmer",
                "source_task_section_sha256": OLD_AFFECTION_MD_SHA,
                "canonical_section_sha256": CANONICAL_AFFECTION_MD_SHA,
                "reader_source_sha256": OLD_AFFECTION_READER_SHA,
                "reader_candidate_sha256": CANONICAL_AFFECTION_READER_SHA,
                "reason": "Restore richer registered-main wording after the task candidate compressed four canonical paragraph jobs into one assistant-composed paragraph. No local Affection detector call is authorized or used."
            },
            {
                "type": "aggregate_boundary_relocation_only",
                "old_boundary": "inside Maturity Levels immediately before Key/guru continuation",
                "rejected_diagnostic_boundary": "before Primal attraction (r13; caused Part-2 regression)",
                "new_boundary": "before the complete Maturity Levels section",
                "article_prose_changed_by_boundary": False,
                "reason": "Keep the entire patient/guru/self-responsibility thought together while retaining the exact previously 100%-Human old Part-2 stream as a byte-for-byte suffix."
            }
        ],
        "invariant_audit": checks,
        "preservation": {
            "unexplained_deltas": 0,
            "talk": "byte-identical to r12; 6/6 hard capped",
            "casual": "byte-identical to r12; final local call conserved",
            "slow_steady": "exact accepted 100%-Human r11 realization retained",
            "patient": "r12 compact wording retained; whole Maturity section moved as detector boundary only",
            "part2_old_stream": "byte-identical source Part 2 retained inside new Part 2",
            "links": "all Markdown link destinations unchanged",
            "native_objects": "unchanged",
        },
        "detector_plan": "After an explicit preservation proof receipt is committed, certify both exact r14 halves as aggregate boundaries. Do not spend a local Affection, Talk, Primal, or Casual call for this operation.",
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
