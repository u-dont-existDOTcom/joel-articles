#!/usr/bin/env python3
"""Deterministic structural checks for the bounded Somatic R15 repair."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "articles/somatic-therapies/experiments/R15-PANGRAM-LOCALIZED-REWRITE-CANDIDATE-20260825.md"
CANDIDATE = ROOT / "articles/somatic-therapies/experiments/R15-CLEAN-REPAIR-CANDIDATE-20260830.md"
MASTER = ROOT / "articles/somatic-therapies/master.html"

BASE_SHA256 = "e7a541e75cf06878c206bcd7d78440bb73593a0a5a2169df1446ce42ad7186ee"
MASTER_SHA256 = "1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202"
PRE_MICRO_BLOB = "91054075329b51b566535881e5ea9a64775798a1"
PRE_MICRO_SHA256 = "85c09a28036a80ff25afd3e3474ad6160fe162f2e120db711fe8ce7c7bc9ea00"
PRE_MICRO_MANIFEST = (
    ROOT
    / "tasks/somatic-r15-clean-continuation-20260830/PRE-MICRO-SECTION-IDENTITY-MANIFEST.json"
)

AUTHORIZED_HEADINGS = {
    "## Your Physical State Can Change What Therapy Does": (
        "## Your Physical State Can Change What Therapy Does"
    ),
    "# Somatic Work and Inner-Child Reparenting": "# Somatic Work and Inner-Child Reparenting",
    "## EFT / Tapping": "## EFT / Tapping",
    "## [Shaking Qigong](http://shakingclass.innersignalselfhypnosis.com/) / Shaking Medicine": (
        "## [Shaking Qigong](http://shakingclass.innersignalselfhypnosis.com/) / Shaking Medicine"
    ),
    "# How I Know Whether It Actually Helped": "# How I Know Whether It Actually Helped",
    "# Sky Hypnosis and Vagal Blitz": (
        "# Optional High-Intensity Practices: Sky Hypnosis and Vagal Blitz"
    ),
}

MICRO_AUTHORIZED_HEADINGS = {
    "## EFT / Tapping",
    "## [Shaking Qigong](http://shakingclass.innersignalselfhypnosis.com/) / Shaking Medicine",
    "# Optional High-Intensity Practices: Sky Hypnosis and Vagal Blitz",
}

PROTECTED_PHRASES = (
    "blissful tingles",
    "Professor Baby Sheep",
    "loveyhuasca",
    "Nurturer and Protector",
    "borrowed adulthood",
    "three to six months",
    "10–45 minutes",
    "$10-per-month Skool class",
    "TRE did nothing for him",
    "many movements and positions",
    "combined with tremoring",
    "teachable en masse",
    "Just try lots of stuff till it works",
    "I did not try the linked class",
    "guided but not completely standardized",
    "benefits from seeing others get results",
    "chronic freeze",
    "non-verbal emotional processing",
    "stress accumulating between therapy sessions",
    "activation left after deeper work",
    "stop and settle afterward",
    "stuck qi is moving again",
    "catharsis competition",
    "severe PTSD",
    "highly dissociative or unstable",
    "rest of the day to be almost boring",
    "moldy clothes",
    "lying-down-only",
    "I do not chase fainting or loss of consciousness",
    "but not prerequisites for healing",
    "ordinary-life test above",
    "mainly helping me avoid",
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


def git_blob_text(blob: str) -> str:
    result = subprocess.run(
        ["git", "cat-file", "blob", blob],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout.decode("utf-8")


def section_identities(text: str) -> list[tuple[str, str]]:
    return [
        (heading, hashlib.sha256(section.encode("utf-8")).hexdigest())
        for heading, section in heading_sections(text)
    ]


def pre_micro_section_identities() -> tuple[list[tuple[str, str]], str]:
    """Load exact pre-micro identities from Git, with a shallow-clone-safe manifest."""
    try:
        text = git_blob_text(PRE_MICRO_BLOB)
    except (subprocess.CalledProcessError, UnicodeDecodeError):
        manifest = json.loads(PRE_MICRO_MANIFEST.read_text(encoding="utf-8"))
        if (
            manifest.get("schemaVersion") != 1
            or manifest.get("gitBlob") != PRE_MICRO_BLOB
            or manifest.get("sha256") != PRE_MICRO_SHA256
            or not isinstance(manifest.get("sections"), list)
        ):
            raise ValueError("invalid pre-micro section identity manifest")
        identities = [
            (record["heading"], record["sha256"])
            for record in manifest["sections"]
            if isinstance(record, dict)
            and isinstance(record.get("heading"), str)
            and re.fullmatch(r"[0-9a-f]{64}", str(record.get("sha256", "")))
        ]
        if len(identities) != len(manifest["sections"]):
            raise ValueError("invalid pre-micro section identity record")
        return identities, "manifest"
    if hashlib.sha256(text.encode("utf-8")).hexdigest() != PRE_MICRO_SHA256:
        raise ValueError("pre-micro Git blob SHA-256 mismatch")
    return section_identities(text), "git_blob"


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
    try:
        pre_micro_identities, pre_micro_identity_source = pre_micro_section_identities()
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        pre_micro_identities = []
        pre_micro_identity_source = "unavailable"
        failures.append("PRE_MICRO_IDENTITY_UNAVAILABLE")
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

    micro_changed_sections: list[str] = []
    if pre_micro_identities:
        candidate_identities = section_identities(candidate_text)
        if len(pre_micro_identities) != len(candidate_identities):
            failures.append("MICRO_HEADING_SECTION_COUNT_CHANGED")
        else:
            for (pre_heading, pre_hash), (candidate_heading, candidate_hash) in zip(
                pre_micro_identities, candidate_identities, strict=True
            ):
                if pre_heading in MICRO_AUTHORIZED_HEADINGS:
                    if candidate_heading != pre_heading:
                        failures.append(f"MICRO_AUTHORIZED_HEADING_CHANGED:{pre_heading}")
                    if candidate_hash != pre_hash:
                        micro_changed_sections.append(pre_heading)
                elif pre_heading != candidate_heading or pre_hash != candidate_hash:
                    failures.append(f"OUTSIDE_MICRO_WHITELIST_CHANGED:{pre_heading}")
        if set(micro_changed_sections) != MICRO_AUTHORIZED_HEADINGS:
            failures.append("MICRO_CHANGED_SECTION_SET_MISMATCH")

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
    if "the 10–45-minute range" in reader_text:
        failures.append("ORPHANED_RANGE_REFERENCE_PRESENT")
    if "I did not learn or test that range in the linked class." not in reader_text:
        failures.append("RANGE_PROVENANCE_BOUNDARY_MISSING")
    if "I think of tapping different points as activating different parts of the brain" not in reader_text:
        failures.append("EFT_OWNER_ATTRIBUTION_MISSING")
    if "With a discrete event, can I remember it later with less restimulation?" in reader_text:
        failures.append("CODA_DUPLICATES_DISCRETE_DIFFUSE_TEST")

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
        "microChangedSections": micro_changed_sections,
        "preMicroIdentitySource": pre_micro_identity_source,
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
