#!/usr/bin/env python3
"""Fail-closed R15 and owner-source checks for the final source-native candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_somatic_r15_articlewide as r15


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "articles/somatic-therapies/experiments/R15-DIRECT-OWNER-VOICE-CANDIDATE-20260830.md"

OWNER_SOURCE_BLOBS = {
    "r05": "28832dcd9e677ab4e25622d0085411f88334b897",
    "r06": "fd90bcc918a32dd2df8406a2e9dec30cb8b68c6f",
    "adult-child-trust": "7cf9c3a46a0ca0e6ce0cd13c20560b689c820cea",
    "heart-loop": "1512fa9247db7333ed711f21496461b73494a00e",
    "somatic-prep": "473eb5d886411047dd2aa7a1dd2534f873b699b1",
    "witness-protector-hypnosis": "e54e44702ba2f61b55e83bfcbf3581669bb848e0",
}

# The prior checker encoded exact wording from the now-negative-control article-wide
# candidate. These patterns preserve the same R15 functions while allowing the
# supervisor-authorized direct-owner realization.
REQUIRED_MARKERS = {
    **r15.REQUIRED_MARKERS,
    "tre-nonresponse": r"TRE (?:itself )?did nothing for him|TRE did nothing for him",
    "shaking-price": r"\$10 (?:per|a) month on Skool",
    "shaking-firsthand-boundary": r"I (?:haven't|didn't|did not) (?:try|tried) the (?:linked|Shaking Qigong) class",
    "shaking-range-provenance": r"did not learn that range from the linked class|not a duration I learned from or tested in Louka's class",
    "between-session-stress": r"(?:stress that )?(?:keeps )?(?:accumulat(?:es|ing)|piles up) between therapy sessions",
    "subcortical-boundary": r"material (?:is arriving|arrived) before (?:the|its) story",
    "brainspotting-finger": r"finger (?:and eyes|to (?:direct|guide) my gaze)",
    "nlp-limit": r"(?:rule|mapping).*(?:did not hold up|has not held up|not supported).*controlled research",
    "brainspotting-self-limit": r"deepest trauma (?:alone|as a solo experiment)",
    "brainspotting-applications": r"diffuse developmental trauma.*pre-verbal or body-held",
    "emdr-memory": r"there it is[;,] that is the memory",
    "emdr-boring-day": r"day to be almost boring|almost boring day",
    "forgiveness-qualified": r"forgiveness.{0,3}when forgiveness is actually relevant",
    "peripheral-claim-limit": r"research is more complicated(?: than that)?",
}

DIRECT_OWNER_MARKERS = {
    "love-seems-unsafe": r"love seems unsafe",
    "adult-outcome-objection": r"doesn't look like things went well for us",
    "adult-child-war": r"internal war|at war with the younger version",
    "owner-credibility-line": r"big fuckity whoopty doo",
    "protector-real-action": r"Protector creates real-world safety",
    "neutral-witness": r"neutral witness",
    "borrowed-adulthood-detail": r"borrow one sentence, boundary, or direction",
    "hypnosis-no-forced-memory": r"self-hypnosis.*force memories",
    "heart-hand": r"one hand.*(?:center of the chest|heart chakra)",
    "solar-plexus-hand": r"other.*solar plexus",
    "slap-owner-example": r"one slap there hurts",
    "infinite-loop": r"infinite beautiful loop",
    "eft-regulation-distraction": r"EFT is very nice for regulation.*distraction",
    "shaking-right-thing": r"right thing is shaken the right way",
    "owner-expertise-joke": r"Just try lots of stuff till it works.*expertise",
    "brainspotting-intuitive": r"It was intuitive",
    "brainspotting-democratic": r"democratic like EFT",
    "housemate-yelled": r"housemate.*moldy clothes.*dress.*yelled",
    "one-hour-durability": r"hour later",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_blob_exists(blob: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{blob}^{{blob}}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def audit(candidate: Path = CANDIDATE) -> dict[str, object]:
    failures: list[str] = []
    if not candidate.is_file():
        return {"status": "FAIL", "failures": ["CANDIDATE_MISSING"]}

    if sha256(r15.BASE) != r15.BASE_SHA256:
        failures.append("BASE_IDENTITY_CHANGED")
    if sha256(r15.MASTER) != r15.MASTER_SHA256:
        failures.append("REGISTERED_MASTER_CHANGED")
    for name, blob in OWNER_SOURCE_BLOBS.items():
        if not git_blob_exists(blob):
            failures.append(f"OWNER_SOURCE_BLOB_MISSING:{name}:{blob}")

    base = r15.BASE.read_text(encoding="utf-8")
    text = candidate.read_text(encoding="utf-8")
    article = r15.reader_text(text)

    if r15.HEADING_RE.findall(article) != r15.HEADING_RE.findall(r15.reader_text(base)):
        failures.append("R15_HEADING_ROUTE_CHANGED")

    base_links = r15.LINK_RE.findall(r15.reader_text(base))
    candidate_links = r15.LINK_RE.findall(article)
    if len(base_links) != 16 or len(candidate_links) != 16:
        failures.append(f"LINK_COUNT_CHANGED:{len(base_links)}:{len(candidate_links)}")
    if Counter(base_links) != Counter(candidate_links):
        failures.append("LINK_MULTISET_CHANGED")

    base_objects = [line for line in base.splitlines() if line.startswith("**[EXISTING ")]
    candidate_objects = [line for line in text.splitlines() if line.startswith("**[EXISTING ")]
    if len(base_objects) != 7 or candidate_objects != base_objects:
        failures.append("NATIVE_PLACEHOLDER_IDENTITY_ORDER_CHANGED")

    for name, pattern in {**REQUIRED_MARKERS, **DIRECT_OWNER_MARKERS}.items():
        if not re.search(pattern, article, re.IGNORECASE | re.DOTALL):
            failures.append(f"PRESERVATION_MARKER_MISSING:{name}")

    if re.search(r"(?i)\bjob\s*[1-5]\b", article):
        failures.append("FIVE_JOB_TAXONOMY_PRESENT")
    if re.search(r"\bp[iī]ti\b", article, re.IGNORECASE):
        failures.append("OWNER_TERMINOLOGY_REVERTED")
    if "R15-ARTICLE-WIDE-HUMANIZATION-CANDIDATE" in article:
        failures.append("NEGATIVE_CONTROL_REFERENCE_IN_READER_TEXT")

    return {
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "baseSha256": sha256(r15.BASE),
        "candidateSha256": sha256(candidate),
        "candidateWords": len(article.split()),
        "ordinaryLinks": len(candidate_links),
        "nativePlaceholders": len(candidate_objects),
        "headings": len(r15.HEADING_RE.findall(article)),
        "r15PreservationMarkers": len(REQUIRED_MARKERS),
        "directOwnerMarkers": len(DIRECT_OWNER_MARKERS),
        "ownerSourceBlobs": OWNER_SOURCE_BLOBS,
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
        print("SOMATIC_R15_DIRECT_OWNER_PASS" if result["status"] == "PASS" else "SOMATIC_R15_DIRECT_OWNER_FAIL")
        for failure in result["failures"]:
            print(failure)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
