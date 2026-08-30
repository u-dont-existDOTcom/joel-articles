#!/usr/bin/env python3
"""Deterministic structural checks for the bounded Somatic R15 repair."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "articles/somatic-therapies/experiments/R15-PANGRAM-LOCALIZED-REWRITE-CANDIDATE-20260825.md"
CANDIDATE = ROOT / "articles/somatic-therapies/experiments/R15-CLEAN-REPAIR-CANDIDATE-20260830.md"
MASTER = ROOT / "articles/somatic-therapies/master.html"

BASE_SHA256 = "e7a541e75cf06878c206bcd7d78440bb73593a0a5a2169df1446ce42ad7186ee"
MASTER_SHA256 = "1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202"

AUTHORIZED_HEADINGS = {
    "## Your Physical State Can Change What Therapy Does": (
        "## Your Physical State Can Change What Therapy Does"
    ),
    "# Somatic Work and Inner-Child Reparenting": "# Somatic Work and Inner-Child Reparenting",
    "## [Shaking Qigong](http://shakingclass.innersignalselfhypnosis.com/) / Shaking Medicine": (
        "## [Shaking Qigong](http://shakingclass.innersignalselfhypnosis.com/) / Shaking Medicine"
    ),
    "# How I Know Whether It Actually Helped": "# How I Know Whether It Actually Helped",
    "# Sky Hypnosis and Vagal Blitz": (
        "# Optional High-Intensity Practices: Sky Hypnosis and Vagal Blitz"
    ),
}

PROTECTED_PHRASES = (
    "blissful tingles",
    "Professor Baby Sheep",
    "loveyhuasca",
    "Nurturer and Protector",
    "borrowed adulthood",
    "three to six months",
    "10–45-minute range",
    "catharsis competition",
    "rest of the day to be almost boring",
    "moldy clothes",
    "lying-down-only",
    "I do not chase fainting or loss of consciousness",
)

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,3} .+)$", re.MULTILINE)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def heading_sections(text: str) -> list[tuple[str, str]]:
    matches = list(HEADING_RE.finditer(text))
    sections: list[tuple[str, str]] = []
    prefix = text[: matches[0].start()] if matches else text
    sections.append(("<preamble>", prefix))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1), text[match.start() : end]))
    return sections


def audit() -> dict[str, object]:
    failures: list[str] = []
    if not CANDIDATE.is_file():
        return {"status": "FAIL", "failures": ["CANDIDATE_MISSING"]}
    if sha256(BASE) != BASE_SHA256:
        failures.append("BASE_IDENTITY_CHANGED")
    if sha256(MASTER) != MASTER_SHA256:
        failures.append("REGISTERED_MASTER_CHANGED")

    base_text = BASE.read_text(encoding="utf-8")
    candidate_text = CANDIDATE.read_text(encoding="utf-8")
    base_sections = heading_sections(base_text)
    candidate_sections = heading_sections(candidate_text)
    if len(base_sections) != len(candidate_sections):
        failures.append("HEADING_SECTION_COUNT_CHANGED")
    else:
        for (base_heading, base_section), (candidate_heading, candidate_section) in zip(
            base_sections, candidate_sections, strict=True
        ):
            if base_heading in AUTHORIZED_HEADINGS:
                if candidate_heading != AUTHORIZED_HEADINGS[base_heading]:
                    failures.append(f"AUTHORIZED_HEADING_ROUTE_CHANGED:{base_heading}")
            elif base_heading != candidate_heading or base_section != candidate_section:
                failures.append(f"OUTSIDE_WHITELIST_CHANGED:{base_heading}")

    base_links = LINK_RE.findall(base_text)
    candidate_links = LINK_RE.findall(candidate_text)
    if len(base_links) != 16 or len(candidate_links) != 16:
        failures.append(f"LINK_COUNT_CHANGED:{len(base_links)}:{len(candidate_links)}")
    if Counter(base_links) != Counter(candidate_links):
        failures.append("LINK_MULTISET_CHANGED")

    base_objects = [line for line in base_text.splitlines() if line.startswith("**[EXISTING ")]
    candidate_objects = [
        line for line in candidate_text.splitlines() if line.startswith("**[EXISTING ")
    ]
    if len(base_objects) != 7 or candidate_objects != base_objects:
        failures.append("NATIVE_PLACEHOLDER_IDENTITY_ORDER_CHANGED")

    reader_text = candidate_text[candidate_text.index("# Introduction") :]
    for phrase in PROTECTED_PHRASES:
        if phrase not in reader_text:
            failures.append(f"PROTECTED_PHRASE_MISSING:{phrase}")
    if re.search(r"(?i)\bjob\s*[1-5]\b", reader_text):
        failures.append("FIVE_JOB_TAXONOMY_PRESENT")
    if "pīti" in reader_text or "piti" in reader_text:
        failures.append("OWNER_TERMINOLOGY_REVERTED")

    return {
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "baseSha256": sha256(BASE),
        "candidateSha256": sha256(CANDIDATE),
        "candidateWords": len(candidate_text.split()),
        "baseWords": len(base_text.split()),
        "ordinaryLinks": len(candidate_links),
        "nativePlaceholders": len(candidate_objects),
        "authorizedSections": len(AUTHORIZED_HEADINGS),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = audit()
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("SOMATIC_R15_REPAIR_PASS" if result["status"] == "PASS" else "SOMATIC_R15_REPAIR_FAIL")
        for failure in result["failures"]:
            print(failure)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
