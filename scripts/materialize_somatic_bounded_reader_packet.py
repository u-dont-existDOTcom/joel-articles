#!/usr/bin/env python3
"""Materialize the bounded blind-verification packet for Somatic repair blocks."""

from __future__ import annotations

import argparse
from pathlib import Path


FIRST_START = "# What I Use Between Deeper Sessions"
FIRST_END = "\n---\n\n# When the Body Knows More Than the Story"
SECOND_START = "# How I Know Whether It Actually Helped"
SKY_PLACEHOLDER = (
    "**[EXISTING SKY HYPNOSIS NATIVE EMBED — exact object retained in HTML promotion]**"
)
SKY_REPLACEMENT = "_[Native media: Sky Hypnosis guide.]_"

REQUEST = """Read the two literal excerpts below as a fresh blind verifier. They come from the same first-person practical article for readers considering somatic approaches.

Diagnose only. Do not rewrite, suggest replacement prose, research the claims, or expand into medium/low-confidence style preferences.

Return PASS or FAIL for each bounded question, citing the exact sentence only for a FAIL:

1. EFT attribution: Does the brain/tapping sentence now read as the author's own interpretation rather than an established scientific mechanism? Did it introduce any new high-confidence logic or referent defect?
2. Shaking section: Are the friend's class report, the author's firsthand experience, and the author's hypotheses clearly distinct without disproportionate repetition? Is the 10–45-minute range introduced with a clear antecedent and a clear boundary from the untried linked class? Did compression introduce any new high-confidence logic or referent defect?
3. Optional ending: Does the late Sky/Vagal section remain clearly optional while avoiding a second full explanation of the preceding event-versus-diffuse outcome framework? Did compression introduce any new high-confidence logic, referent, or placement defect?

End with exactly one overall disposition: BOUNDED_VERIFICATION_PASS or BOUNDED_VERIFICATION_FAIL. This is diagnostic only and grants no edit authority.

--- EXCERPT 1 BEGINS ---

"""


def material_from_source(source: str) -> str:
    first_start = source.index(FIRST_START)
    first_end = source.index(FIRST_END, first_start)
    second_start = source.index(SECOND_START)

    first = source[first_start:first_end].strip()
    second = source[second_start:].strip()
    if second.count(SKY_PLACEHOLDER) != 1:
        raise ValueError("expected one exact Sky native placeholder in second excerpt")
    second = second.replace(SKY_PLACEHOLDER, SKY_REPLACEMENT)

    material = (
        first
        + "\n\n--- EXCERPT 1 ENDS / EXCERPT 2 BEGINS ---\n\n"
        + second
        + "\n"
    )
    forbidden = ("Pangram", "detector", "R15", "R16", "R65", "preservation")
    leaked = [term for term in forbidden if term in material]
    if leaked:
        raise ValueError(f"bounded blind material leaked withheld context: {leaked!r}")
    return material


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("material_output", type=Path)
    parser.add_argument("packet_output", type=Path)
    args = parser.parse_args()

    material = material_from_source(args.source.read_text(encoding="utf-8"))
    args.material_output.write_text(material, encoding="utf-8")
    args.packet_output.write_text(REQUEST + material, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
