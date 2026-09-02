#!/usr/bin/env python3
"""Materialize the detector-blind Somatic final-reader article and request."""

from __future__ import annotations

import argparse
from pathlib import Path


INTRODUCTION = "# Introduction"
PLACEHOLDERS = {
    "**[EXISTING PROFESSOR BABY SHEEP NATIVE EMBED — exact object retained in HTML promotion]**":
        "_[Native media: Professor Baby Sheep example.]_",
    "**[EXISTING SHARE BUTTON — exact object retained in HTML promotion]**":
        "_[Native share control.]_",
    "**[EXISTING SOMATIC EXPERIENCING YOUTUBE EMBED — exact object retained in HTML promotion]**":
        "_[Native media: Somatic Experiencing video.]_",
    "**[EXISTING TRE YOUTUBE EMBED — exact object retained in HTML promotion]**":
        "_[Native media: TRE video.]_",
    "**[EXISTING BRAINSPOTTING YOUTUBE EMBED — exact object retained in HTML promotion]**":
        "_[Native media: Brainspotting video.]_",
    "**[EXISTING EMDR YOUTUBE EMBED — exact object retained in HTML promotion]**":
        "_[Native media: EMDR video.]_",
    "**[EXISTING SKY HYPNOSIS NATIVE EMBED — exact object retained in HTML promotion]**":
        "_[Native media: Sky Hypnosis guide.]_",
}

REQUEST = """Read the article below as a genuinely fresh independent reader.

It is a first-person practical article for readers considering somatic approaches. Diagnose only; do not rewrite it and do not propose replacement prose.

Report:

1. the strongest real weakness in the article;
2. passages that feel generic or model-shaped on textual grounds alone;
3. logic gaps, skipped assumptions, or broken causal/chronological movement;
4. unclear referents or terms;
5. places where curiosity or attention drops;
6. unnecessary recap, interpretive aftercare, or false completion;
7. prose that feels unsupported by the author's own preceding thought;
8. whether any issue is high-confidence enough that repairing it would actually improve the article.

Rank findings by confidence, identify the exact implicated passage or natural section, and distinguish real editorial defects from unusual but coherent authorial choices. If no high-confidence repairable defect exists, say that plainly.

--- ARTICLE BEGINS ---

"""


def article_from_source(source: str) -> str:
    lines = source.splitlines()
    starts = [index for index, line in enumerate(lines) if line == INTRODUCTION]
    if len(starts) != 1:
        raise ValueError(f"expected one exact {INTRODUCTION!r} line, found {len(starts)}")

    article_lines = lines[starts[0] :]
    seen: set[str] = set()
    for index, line in enumerate(article_lines):
        replacement = PLACEHOLDERS.get(line)
        if replacement is not None:
            article_lines[index] = replacement
            seen.add(line)

    missing = set(PLACEHOLDERS) - seen
    if missing:
        raise ValueError(f"missing expected native placeholders: {sorted(missing)!r}")

    article = "\n".join(article_lines).strip() + "\n"
    forbidden = ("Pangram", "detector", "R15", "R16", "R65", "preservation")
    leaked = [term for term in forbidden if term in article]
    if leaked:
        raise ValueError(f"blind article leaked withheld context: {leaked!r}")
    return article


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("article_output", type=Path)
    parser.add_argument("packet_output", type=Path)
    args = parser.parse_args()

    article = article_from_source(args.source.read_text(encoding="utf-8"))
    args.article_output.write_text(article, encoding="utf-8")
    args.packet_output.write_text(REQUEST + article, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
