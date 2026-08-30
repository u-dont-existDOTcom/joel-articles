#!/usr/bin/env python3
"""Fail-closed structural and owner-constraint checks for the R15-wide candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "articles/somatic-therapies/experiments/R15-PANGRAM-LOCALIZED-REWRITE-CANDIDATE-20260825.md"
CANDIDATE = ROOT / "articles/somatic-therapies/experiments/R15-ARTICLE-WIDE-HUMANIZATION-CANDIDATE-20260830.md"
MASTER = ROOT / "articles/somatic-therapies/master.html"

BASE_SHA256 = "e7a541e75cf06878c206bcd7d78440bb73593a0a5a2169df1446ce42ad7186ee"
MASTER_SHA256 = "1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202"

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,3} .+)$", re.MULTILINE)

HEADING_ROUTES = {
    "# Sky Hypnosis and Vagal Blitz": "# Optional High-Intensity Practices: Sky Hypnosis and Vagal Blitz"
}

REQUIRED_MARKERS = {
    "physical-neuroinflammation": r"physical neuroinflammation",
    "low-dose-naltrexone": r"low-dose naltrexone",
    "phosphatidylserine": r"phosphatidylserine",
    "dmso": r"\bDMSO\b",
    "ozonated-zeolite": r"Ozonated zeolite",
    "ozonated-charcoal": r"ozonated charcoal water",
    "chaotic-fields": r"chaotic energy fields",
    "professor-baby-sheep": r"Professor Baby Sheep",
    "head-shaving": r"shaving my head",
    "loveyhuasca": r"loveyhuasca",
    "borrowed-adulthood": r"borrow adulthood|borrowed adulthood",
    "nurturer-protector": r"Nurturer and Protector",
    "heart-solar-loop": r"heart.*solar plexus|solar plexus.*heart",
    "se-range": r"Three to six months|three to six months",
    "yoga-choice": r"choice disappears|can't choose",
    "whiplash": r"whip back and forth",
    "eft-owner-attribution": r"I think of the different tapping points",
    "louka": r"My friend Louka",
    "tre-nonresponse": r"TRE itself did nothing for him",
    "shaking-price": r"\$10 per month on Skool",
    "shaking-firsthand-boundary": r"I haven't tried the linked class myself|I did not try the linked class",
    "shaking-range": r"10 to 45 minutes|10–45 minutes",
    "shaking-range-provenance": r"not a duration I learned from or tested in Louka's class",
    "chronic-freeze": r"chronic freeze",
    "nonverbal": r"emotional material with no words|non-verbal emotional processing",
    "between-session-stress": r"piles up between therapy sessions|accumulating between therapy sessions",
    "after-deeper-work": r"after deeper work",
    "stop-settle": r"stop and settle afterward",
    "mechanism-uncertainty": r"I don't know exactly|I do not know exactly",
    "stuck-qi": r"stuck qi",
    "catharsis": r"catharsis competition",
    "severe-ptsd": r"severe PTSD",
    "dissociation-instability": r"dissociative or unstable",
    "subcortical-boundary": r"material is arriving before its story",
    "brainspotting-finger": r"finger to guide my gaze",
    "nlp-limit": r"controlled research has not supported",
    "edging": r"feather-touch",
    "democratic": r"democratic,? like EFT",
    "brainspotting-self-limit": r"deepest trauma.*solo experiment",
    "brainspotting-applications": r"diffuse, developmental, pre-verbal",
    "emdr-memory": r"there it is\. That is the memory",
    "emdr-targets": r"accident.*assault memory.*military trauma.*distinct flashback.*specific trigger network",
    "emdr-effectiveness": r"highly effective",
    "emdr-boring-day": r"boring day",
    "emdr-stack": r"stack Brainspotting, EMDR, intense shaking, and deep yin",
    "cbt-beliefs": r"revisit old beliefs",
    "forgiveness-qualified": r"forgiveness when forgiveness is actually relevant",
    "restimulation": r"restimulation",
    "moldy-clothes": r"moldy clothes",
    "blissful-tingles": r"blissful tingles",
    "peripheral-claim-limit": r"research is more complicated than that",
    "hour-later": r"an hour later",
    "intervention-wake": r"watch the wake",
    "research-boundary": r"size of a literature",
    "kundalini": r"awaken kundalini",
    "sky-lightheaded": r"Sky Hypnosis can make me lightheaded",
    "vagal-lying": r"Vagal Blitz is for lying down only",
    "cardiovascular": r"cardiovascular and mental-health cautions",
    "fainting": r"Fainting and loss of consciousness are not goals",
    "wow-not-result": r"“wow” (?:as )?a result",
    "avoidance-test": r"dodge grief, conflict, practical problems, or deeper relational healing",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reader_text(text: str) -> str:
    return text[text.index("# Introduction") :]


def exact_calibration_blocks(base: str) -> list[str]:
    return [
        base[
            base.index("My friend Louka is why I am linking this particular class.") :
            base.index("I did not try the Shaking Qigong class")
        ],
        base[
            base.index("My outcome measure is boring:") :
            base.index("I care more about the hour-later version")
        ],
    ]


def audit(candidate: Path = CANDIDATE) -> dict[str, object]:
    failures: list[str] = []
    if not candidate.is_file():
        return {"status": "FAIL", "failures": ["CANDIDATE_MISSING"]}
    if sha256(BASE) != BASE_SHA256:
        failures.append("BASE_IDENTITY_CHANGED")
    if sha256(MASTER) != MASTER_SHA256:
        failures.append("REGISTERED_MASTER_CHANGED")

    base = BASE.read_text(encoding="utf-8")
    text = candidate.read_text(encoding="utf-8")
    article = reader_text(text)

    base_headings = HEADING_RE.findall(reader_text(base))
    candidate_headings = HEADING_RE.findall(article)
    expected_headings = [HEADING_ROUTES.get(heading, heading) for heading in base_headings]
    if candidate_headings != expected_headings:
        failures.append("HEADING_ROUTE_CHANGED")

    base_links = LINK_RE.findall(reader_text(base))
    candidate_links = LINK_RE.findall(article)
    if len(base_links) != 16 or len(candidate_links) != 16:
        failures.append(f"LINK_COUNT_CHANGED:{len(base_links)}:{len(candidate_links)}")
    if Counter(base_links) != Counter(candidate_links):
        failures.append("LINK_MULTISET_CHANGED")

    base_objects = [line for line in base.splitlines() if line.startswith("**[EXISTING ")]
    candidate_objects = [line for line in text.splitlines() if line.startswith("**[EXISTING ")]
    if len(base_objects) != 7 or candidate_objects != base_objects:
        failures.append("NATIVE_PLACEHOLDER_IDENTITY_ORDER_CHANGED")

    for index, block in enumerate(exact_calibration_blocks(base), start=1):
        if block not in article:
            failures.append(f"CALIBRATION_ISLAND_CHANGED:{index}")

    for name, pattern in REQUIRED_MARKERS.items():
        if not re.search(pattern, article, re.IGNORECASE | re.DOTALL):
            failures.append(f"PRESERVATION_MARKER_MISSING:{name}")

    if re.search(r"(?i)\bjob\s*[1-5]\b", article):
        failures.append("FIVE_JOB_TAXONOMY_PRESENT")
    if re.search(r"\bp[iī]ti\b", article, re.IGNORECASE):
        failures.append("OWNER_TERMINOLOGY_REVERTED")
    if article.rstrip().endswith("conclusion"):
        failures.append("GENERIC_POST_EMBED_CONCLUSION")

    return {
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "baseSha256": sha256(BASE),
        "candidateSha256": sha256(candidate),
        "candidateWords": len(article.split()),
        "ordinaryLinks": len(candidate_links),
        "nativePlaceholders": len(candidate_objects),
        "headings": len(candidate_headings),
        "preservationMarkers": len(REQUIRED_MARKERS),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--candidate", type=Path, default=CANDIDATE)
    args = parser.parse_args()
    result = audit(args.candidate)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("SOMATIC_R15_ARTICLEWIDE_PASS" if result["status"] == "PASS" else "SOMATIC_R15_ARTICLEWIDE_FAIL")
        for failure in result["failures"]:
            print(failure)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
