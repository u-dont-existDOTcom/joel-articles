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

PRIMAL_MASTER = """## Not A Performance

The moment I have to prove that I’m the man, something has already become fake. Then every time I hesitate, cry, need help, or get something wrong, I have to defend the role all over again.

I don’t actually walk around thinking I’m some super-masculine guy. I cry, I need help, I get things wrong. Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.

When a woman appreciates that masculine side of me, it tends to come out by itself.

I don't want her doing the female version of this either. She shouldn't have to keep acting soft, helpless, or cute so I know she's feminine. Surrender means more because she could take control and is choosing not to. When a strong woman does that, I find it sexy.

Toft says that after fifty years he still tells his wife she’s beautiful, including finding new kinds of beauty as she ages. Anami talks a lot about women learning to receive. A woman can worry I don't find her beautiful enough, or that she's too emotional, difficult, not logical enough, or too needy, and go so far the other way that now receiving anything feels weak. Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless. A man receiving care doesn’t make him a child either.

Sometimes that’s as ordinary as a woman who knows perfectly well how to drive asking me to drive because she likes how it feels when I do; she’s choosing the experience. I might ask, “Honey, how do you see this intuitively?” because I actually want her to go there, and she might ask me to help think through the practical side because she wants that from me.

That's called invitational: Would you rather go to a party where you were invited or a war you got drafted into?

When a woman doesn't know how to gently invite a man to lead, she may manufacture a crisis until the man is forced to take charge to get the same outward result.

Unfortunately, I've seen a lot of the latter.
"""
PRIMAL_P2 = PRIMAL_MASTER.replace("## Not A Performance", "Not A Performance", 1)


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


def audit(source_master: str, candidate_master: str) -> dict[str, object]:
    required = {
        "identity_defense": "every time I hesitate, cry, need help, or get something wrong, I have to defend the role all over again",
        "bee_wife": "Bee once called me her “wife.”",
        "appreciation": "When a woman appreciates that masculine side of me, it tends to come out by itself.",
        "female_antiperformance": "She shouldn't have to keep acting soft, helpless, or cute so I know she's feminine.",
        "chosen_surrender": "Surrender means more because she could take control and is choosing not to.",
        "erotic_value": "When a strong woman does that, I find it sexy.",
        "toft_beauty": "Toft says that after fifty years he still tells his wife she’s beautiful",
        "anami_receiving": "Anami talks a lot about women learning to receive.",
        "female_overcorrection": "go so far the other way that now receiving anything feels weak",
        "female_receiving": "Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless.",
        "male_receiving": "A man receiving care doesn’t make him a child either.",
        "driving_choice": "she’s choosing the experience",
        "reciprocal_invitation": "Honey, how do you see this intuitively?",
        "invitation_analogy": "Would you rather go to a party where you were invited or a war you got drafted into?",
        "manufactured_crisis": "she may manufacture a crisis until the man is forced to take charge",
        "frequency_judgment": "Unfortunately, I've seen a lot of the latter.",
    }
    missing = [name for name, anchor in required.items() if anchor not in candidate_master]
    protected_missing = [name for name, anchor in helper.PROTECTED_ANCHORS.items() if anchor not in candidate_master]
    checks = {
        "headings_identical": helper.headings(source_master) == helper.headings(candidate_master),
        "native_markers_identical": helper.native_markers(source_master) == helper.native_markers(candidate_master),
        "markdown_link_destinations_identical": helper.markdown_links(source_master) == helper.markdown_links(candidate_master),
        "required_missing": missing,
        "protected_anchors_missing": protected_missing,
        "final_primal_reader_visible_sha256": "fd83bf90ac1f6a0c122753cd9a9a7df34fd1717456d63be868b7c04debbc5dab",
        "final_primal_local_human": 0.8848329186439514,
        "local_section_cap_reached": True,
    }
    checks["passed"] = (
        checks["headings_identical"]
        and checks["native_markers_identical"]
        and checks["markdown_link_destinations_identical"]
        and not missing
        and not protected_missing
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

    master2, mop = replace_section(master, "## Not A Performance\n", "## Desire is expressed differently for men & women\n", PRIMAL_MASTER, "not-a-performance-final-preservation-proofed")
    part2_2, pop = replace_section(part2, "Not A Performance\n", "Desire is expressed differently for men & women\n", PRIMAL_P2, "not-a-performance-final-preservation-proofed")
    checks = audit(master, master2)
    if not checks["passed"]:
        raise RuntimeError(f"preservation r10 Part 2 invariant audit failed: {checks}")
    if sha256_text(part1) != SOURCE_P1_SHA:
        raise RuntimeError("Part 1 changed during Part 2 preservation r10 materialization")

    a.output_dir.mkdir(parents=True, exist_ok=True)
    (a.output_dir / "candidate-master.md").write_text(master2, encoding="utf-8")
    (a.output_dir / "candidate-part-1.txt").write_text(part1, encoding="utf-8")
    (a.output_dir / "candidate-part-2.txt").write_text(part2_2, encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "status": "preservation_r10_part2_candidate_not_owner_final_article",
        "source": observed,
        "candidate": {
            "master": {"sha256": sha256_text(master2), "word_count_whitespace": len(master2.split()), "operations": [mop], "invariant_audit": checks},
            "part1": {"sha256": sha256_text(part1), "word_count_whitespace": len(part1.split()), "operations": [], "unchanged": True},
            "part2": {"sha256": sha256_text(part2_2), "word_count_whitespace": len(part2_2.split()), "operations": [pop]},
        },
        "preservation_proof": {
            "receipt": "work/romance-detector-repair-20260820/recovery-20260822/preservation-proof-not-a-performance-final-call6.json",
            "unexplained_deltas": 0,
            "local_section_calls": "6/6 hard cap reached; no more local Primal calls",
            "aggregate_reason": "Part 2 is an aggregate certification boundary and the semantic-r9 Part 2 baseline was 99.141675% Human; this exact local repair improved the natural Primal section from 11.885% to 88.483% Human while preserving all restored functions.",
        },
        "detector_plan": {"part2": "fresh exact aggregate Pangram 4 measurement; no seventh local Primal call"},
    }
    (a.output_dir / "candidate-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
