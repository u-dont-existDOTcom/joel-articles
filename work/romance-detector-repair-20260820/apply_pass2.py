#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PASS1_MASTER_SHA = "97fdacfa54492b6ae7e977725532457830585c5401c3383ce96a27aeba38b554"
PASS1_P1_SHA = "51f4823cab86943cfa022c9139f97ed9f871cf4e7a5318ee8212816171f84e00"
PASS1_P2_SHA = "30f61fb0c490ec1275f3c39c834a38a956041865b63e5592c270d51cc22d5498"
REGISTERED_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"

P1_CANDIDATE = """Sex drives have lives of their own, and they change. For a while one of you may want more, less, or something different. That mismatch can turn into a lot of quiet resentment. Talk about what you’ll do when it happens before either person is already hurt. It won’t solve it in advance, but at least you’ll have somewhere to begin."""
P1_REGISTERED = """Sex drives are independently alive and always changing. For some stretch, one of you will want more, less, or something different. When the discordance comes, it's one of the saddest sources of quiet resentment. Talk about what you’ll do when that happens before either person is already hurt. It won’t solve it in advance, but at least you’ll have somewhere to begin."""

AFTER_LEAVING_CANDIDATE = """A breakup can expose things you genuinely couldn't see while you were bonded. Look at what you contributed, but also try to understand whatever was true in your ex's perspective, including the conflicts they were carrying inside themselves. Don't flatten them into one character just because the relationship ended."""
AFTER_LEAVING_PASS2 = """A breakup can expose things you genuinely couldn't see while you were bonded. Look at what you contributed, but also try to understand whatever was true in your ex's perspective, including the conflicts they were carrying inside themselves, rather than one-dimensionalizing them."""

AFTERCARE = " Staying curious about what happened can be therapeutic in itself."

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


def replace_once(text: str, old: str, new: str, label: str) -> tuple[str, dict[str, object]]:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, found {count}")
    return text.replace(old, new, 1), {
        "label": label,
        "source_occurrences": count,
        "old_sha256": sha256_text(old),
        "new_sha256": sha256_text(new),
    }


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
    parser = argparse.ArgumentParser(description="Materialize Romance detector-repair pass 2.")
    parser.add_argument("--pass1-master", type=Path, required=True)
    parser.add_argument("--pass1-part1", type=Path, required=True)
    parser.add_argument("--pass1-part2", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    master = args.pass1_master.read_text(encoding="utf-8")
    part1 = args.pass1_part1.read_text(encoding="utf-8")
    part2 = args.pass1_part2.read_text(encoding="utf-8")

    observed = {
        "master": sha256_text(master),
        "part1": sha256_text(part1),
        "part2": sha256_text(part2),
    }
    expected = {
        "master": PASS1_MASTER_SHA,
        "part1": PASS1_P1_SHA,
        "part2": PASS1_P2_SHA,
    }
    if observed != expected:
        raise RuntimeError(f"pass-1 source hash mismatch: expected={expected} observed={observed}")

    master2, m1 = replace_once(master, P1_CANDIDATE, P1_REGISTERED, "restore-registered-part1-paragraph")
    master2, m2 = replace_once(master2, AFTER_LEAVING_CANDIDATE, AFTER_LEAVING_PASS2, "restore-one-dimensionalizing")
    master2, m3 = replace_once(master2, AFTERCARE, "", "remove-after-leaving-interpretive-aftercare")

    part1_2, p1 = replace_once(part1, P1_CANDIDATE, P1_REGISTERED, "restore-registered-part1-paragraph")
    if sha256_text(part1_2) != REGISTERED_P1_SHA:
        raise RuntimeError(
            "Part 1 did not return exactly to registered detector boundary: "
            f"expected={REGISTERED_P1_SHA} actual={sha256_text(part1_2)}"
        )

    part2_2, p2a = replace_once(part2, AFTER_LEAVING_CANDIDATE, AFTER_LEAVING_PASS2, "restore-one-dimensionalizing")
    part2_2, p2b = replace_once(part2_2, AFTERCARE, "", "remove-after-leaving-interpretive-aftercare")

    checks = audit_master(master, master2)
    if not checks["passed"]:
        raise RuntimeError(f"pass-2 master invariant audit failed: {checks}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_master = args.output_dir / "candidate-master.md"
    out_p1 = args.output_dir / "candidate-part-1.txt"
    out_p2 = args.output_dir / "candidate-part-2.txt"
    manifest_path = args.output_dir / "candidate-manifest.json"

    out_master.write_text(master2, encoding="utf-8")
    out_p1.write_text(part1_2, encoding="utf-8")
    out_p2.write_text(part2_2, encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "status": "candidate_not_owner_final",
        "source_pass1": observed,
        "candidate": {
            "master": {
                "path": out_master.name,
                "sha256": sha256_text(master2),
                "word_count_whitespace": len(master2.split()),
                "operations": [m1, m2, m3],
                "invariant_audit": checks,
            },
            "part1": {
                "path": out_p1.name,
                "sha256": sha256_text(part1_2),
                "word_count_whitespace": len(part1_2.split()),
                "operations": [p1],
                "reuses_registered_detector_result": sha256_text(part1_2) == REGISTERED_P1_SHA,
            },
            "part2": {
                "path": out_p2.name,
                "sha256": sha256_text(part2_2),
                "word_count_whitespace": len(part2_2.split()),
                "operations": [p2a, p2b],
            },
        },
        "detector_plan": {
            "part1": "no_new_call_exact_registered_hash_restored",
            "part2": "one_new_pangram4_measurement_only",
        },
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
