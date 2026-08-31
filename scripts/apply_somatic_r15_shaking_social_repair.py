#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from materialize_somatic_r15_boundary import materialize


ROOT = Path(__file__).resolve().parents[1]
DETECTOR = Path(
    "/mnt/hdd/home/joel/Téléchargements/pangram-worktrees/"
    "somatic-r15-articlewide-20260830"
)
LIVE_HEAD = "35ebdb263ba90ac36f345af2560f13c6d711459d"
SOURCE_REL = Path(
    "articles/somatic-therapies/experiments/"
    "R15-EFT-REPAIR-CANDIDATE-20260831.md"
)
OUTPUT_REL = Path(
    "articles/somatic-therapies/experiments/"
    "R15-EFT-SHAKING-SOCIAL-REPAIR-CANDIDATE-20260831.md"
)
BOUNDARY_REL = Path(
    "articles/somatic-therapies/experiments/"
    "R15-EFT-SHAKING-SOCIAL-REPAIR-BOUNDARY-20260831.txt"
)
DIFF_REL = Path(
    "tasks/somatic-r15-clean-continuation-20260830/"
    "SHAKING-SOCIAL-REPAIR-DIFF-20260831.patch"
)
INDEX_REL = Path("articles/INDEX.json")
SOURCE_BLOB = "6f9251f51d79a6b322b8c6f6cae95a9a5d80f760"
SOURCE_SHA = "5a6226ca0056610b4492de7713a43bb152dde1079d81b5c05896c70fcf138679"
MASTER_SHA = "1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202"
DETECTOR_HEAD = "a2442fb343e43247b445d5884eaa8f7daa44a514"
DETECTOR_RESULT_REL = Path(
    "state/experiments/"
    "somatic-r15-shaking-current-anchor-residual-social-tail-20260831/"
    "RESULT-PACKET.json"
)
DETECTOR_RESULT_SHA = "43ab4bb70fb65a5c2a810782b6b5125c515e69592cddbc6416d51f85e6084b85"
H0_REL = Path(
    "tasks/somatic-r15-clean-continuation-20260830/"
    "surface-experiment-008/C-current-anchor.txt"
)
A_REL = Path(
    "tasks/somatic-r15-clean-continuation-20260830/"
    "surface-experiment-009/A-current-anchor-source-social-tail.txt"
)
H0_SHA = "b36e1e46c06d764a080d407dce5412defe76ccb9202deb1a8a14e265acf40370"
A_SHA = "03037241afe8827df5b1ca2b81bc877704d5e198229a9759237b76245807ecd1"
OLD = (
    "That could suit somebody who wants guidance but gets nothing from standard TRE. "
    "It is social too. Many people do better when they see other people getting results "
    "instead of doing the whole practice alone."
)
NEW = (
    "It is social too. Many people do better when they see other people getting results "
    "instead of doing the whole practice alone."
)
OLD_SHA = "3a96a5bb9b7dd0d670f36b16ccaceca355243a7878b69afa753c847e78c2f349"
NEW_SHA = "6667faded75427a60fd82b7eadeb834966074f7b45712a10e5aec380b3c6f4ec"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6} .+)$", re.MULTILINE)
R_NUMBER = re.compile(r"^R(\d+)(?:\D|$)")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git(*args: str, root: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=root, text=True, capture_output=True, check=check
    )


def git_text(*args: str, root: Path = ROOT) -> str:
    return git(*args, root=root).stdout.strip()


def counts(raw: bytes) -> dict[str, int | bool]:
    text = raw.decode("utf-8")
    return {
        "words": len(text.split()),
        "unicode_characters": len(text),
        "utf8_bytes": len(raw),
        "terminal_newline": text.endswith("\n"),
    }


def main() -> int:
    allowed_dirty = ["?? scripts/apply_somatic_r15_shaking_social_repair.py"]
    if git_text("rev-parse", "HEAD") != LIVE_HEAD:
        raise SystemExit("article live head mismatch")
    if git_text("status", "--porcelain").splitlines() != allowed_dirty:
        raise SystemExit("article worktree has unexpected mutations")

    source_raw = (ROOT / SOURCE_REL).read_bytes()
    source_text = source_raw.decode("utf-8")
    if git_text("hash-object", SOURCE_REL.as_posix()) != SOURCE_BLOB or sha(source_raw) != SOURCE_SHA:
        raise SystemExit("source candidate identity mismatch")
    master_raw = (ROOT / "articles/somatic-therapies/master.html").read_bytes()
    if sha(master_raw) != MASTER_SHA:
        raise SystemExit("registered master identity mismatch")
    old_raw = OLD.encode("utf-8")
    new_raw = NEW.encode("utf-8")
    if counts(old_raw) != {
        "words": 35,
        "unicode_characters": 205,
        "utf8_bytes": 205,
        "terminal_newline": False,
    } or sha(old_raw) != OLD_SHA:
        raise SystemExit("deleted paragraph identity mismatch")
    if counts(new_raw) != {
        "words": 22,
        "unicode_characters": 125,
        "utf8_bytes": 125,
        "terminal_newline": False,
    } or sha(new_raw) != NEW_SHA:
        raise SystemExit("inserted paragraph identity mismatch")
    if source_text.count(OLD) != 1:
        raise SystemExit("deleted paragraph occurrence count is not exactly one")

    if git_text("rev-parse", "HEAD", root=DETECTOR) != DETECTOR_HEAD:
        raise SystemExit("detector head mismatch")
    if git_text("status", "--porcelain", root=DETECTOR):
        raise SystemExit("detector evidence worktree is dirty")
    packet_raw = (DETECTOR / DETECTOR_RESULT_REL).read_bytes()
    packet = json.loads(packet_raw.decode("utf-8"))
    h0 = packet["variants"]["H0"]
    a = packet["variants"]["A"]
    if not (
        sha(packet_raw) == DETECTOR_RESULT_SHA
        and packet["family_state"] == "CLOSED_A_HUMAN_1_0_B_NOT_SUBMITTED"
        and h0["input_sha256"] == H0_SHA
        and h0["result"]["detector_version"] == "4.0"
        and h0["result"]["detector_stage"] == "STAGE_SUCCESS"
        and h0["result"]["summary"]["fraction_human"] == 1.0
        and h0["result"]["summary"]["fraction_ai"] == 0.0
        and h0["result"]["summary"]["fraction_ai_assisted"] == 0.0
        and h0["history_api_exact_identity"]["transport_match_mode"] == "exact_utf8"
        and a["input_sha256"] == A_SHA
        and a["result"]["detector_version"] == "4.0"
        and a["result"]["detector_stage"] == "STAGE_SUCCESS"
        and a["result"]["summary"]["fraction_human"] == 1.0
        and a["result"]["summary"]["fraction_ai"] == 0.0
        and a["result"]["summary"]["fraction_ai_assisted"] == 0.0
        and a["confidence"] == "High"
        and a["history_api_exact_identity"]["transport_match_mode"] == "exact_utf8"
        and packet["variants"]["B"]["detector_submission_attempted"] is False
    ):
        raise SystemExit("detector result binding mismatch")
    h0_raw = (ROOT / H0_REL).read_bytes()
    a_raw = (ROOT / A_REL).read_bytes()
    if sha(h0_raw) != H0_SHA or sha(a_raw) != A_SHA or a_raw != h0_raw + b"\n\n" + new_raw:
        raise SystemExit("A boundary or appended-tail binding mismatch")

    prefix, suffix = source_text.split(OLD)
    output_text = prefix + NEW + suffix
    output_raw = output_text.encode("utf-8")
    if source_raw != prefix.encode("utf-8") + old_raw + suffix.encode("utf-8"):
        raise SystemExit("source split identity mismatch")
    if output_raw != prefix.encode("utf-8") + new_raw + suffix.encode("utf-8"):
        raise SystemExit("outside-scope bytes changed")

    h0_heading = "## [Shaking Qigong](http://shakingclass.innersignalselfhypnosis.com/) / Shaking Medicine"
    h0_end = "Guided shaking plus qigong also seems like a middle ground between a fully predictable TRE structure and completely unstructured shaking."
    start = source_text.index(h0_heading)
    end = source_text.index(h0_end, start) + len(h0_end)
    if output_text[start:end].encode("utf-8") != source_text[start:end].encode("utf-8"):
        raise SystemExit("complete current Human Shaking anchor changed")
    required_upstream = (
        "TRE did nothing for him. Nothing helped much until he got into this class",
        "all kinds of movements and positions",
        "approach the stuck place from more angles",
        "Guided shaking plus qigong",
        "middle ground between a fully predictable TRE structure and completely unstructured shaking",
    )
    if not all(marker in source_text[start:end] for marker in required_upstream):
        raise SystemExit("deleted-sentence function is not preserved upstream")
    if not all(marker in NEW for marker in ("social", "other people", "instead of doing the whole practice alone", "see other people getting results")):
        raise SystemExit("residual social functions not preserved")
    if HEADING_RE.findall(output_text) != HEADING_RE.findall(source_text):
        raise SystemExit("heading order changed")
    source_links = LINK_RE.findall(source_text)
    output_links = LINK_RE.findall(output_text)
    if len(source_links) != 16 or len(output_links) != 16 or Counter(source_links) != Counter(output_links):
        raise SystemExit("ordinary-link URL multiset changed")
    source_objects = [line for line in source_text.splitlines() if line.startswith("**[EXISTING ")]
    output_objects = [line for line in output_text.splitlines() if line.startswith("**[EXISTING ")]
    if len(source_objects) != 7 or output_objects != source_objects:
        raise SystemExit("native-placeholder identity/order changed")

    quarantine_hits: list[str] = []
    for path in (ROOT / "articles/somatic-therapies/experiments").iterdir():
        match = R_NUMBER.match(path.name)
        if match and 16 <= int(match.group(1)) <= 65 and path.is_file():
            if NEW in path.read_text(encoding="utf-8", errors="replace"):
                quarantine_hits.append(path.relative_to(ROOT).as_posix())
    failed_ref = "origin/experiment/somatic-source-clean-recovery-20260829"
    if git("rev-parse", "--verify", failed_ref, check=False).returncode == 0:
        scan = git("grep", "-F", "-e", NEW, failed_ref, "--", "articles/somatic-therapies", check=False)
        if scan.returncode == 0:
            quarantine_hits.append("PR72_FAILED_BRANCH")
        elif scan.returncode != 1:
            raise SystemExit("PR #72 quarantine scan failed")
    if quarantine_hits:
        raise SystemExit(f"failed-branch prose contamination: {quarantine_hits}")

    boundary_raw = materialize(output_text).encode("utf-8")
    (ROOT / OUTPUT_REL).write_bytes(output_raw)
    (ROOT / BOUNDARY_REL).write_bytes(boundary_raw)
    diff_run = git(
        "diff",
        "--no-index",
        "--no-color",
        "--unified=0",
        "--",
        SOURCE_REL.as_posix(),
        OUTPUT_REL.as_posix(),
        check=False,
    )
    if diff_run.returncode != 1:
        raise SystemExit("failed to generate exact one-paragraph diff")
    if diff_run.stdout.count("@@") != 2 or diff_run.stdout.count("-" + OLD) != 1 or diff_run.stdout.count("+" + NEW) != 1:
        raise SystemExit("diff scope mismatch")
    (ROOT / DIFF_REL).write_text(diff_run.stdout, encoding="utf-8")

    index_path = ROOT / INDEX_REL
    index = json.loads(index_path.read_text(encoding="utf-8"))
    article = next(item for item in index["articles"] if item["id"] == "somatic-therapies")
    protected = deepcopy({key: value for key, value in article.items() if key != "additional_artifacts"})
    existing_paths = {item["path"] for item in article["additional_artifacts"]}
    if OUTPUT_REL.as_posix() in existing_paths or BOUNDARY_REL.as_posix() in existing_paths:
        raise SystemExit("new artifact path already registered")
    article["additional_artifacts"].extend(
        [
            {
                "path": OUTPUT_REL.as_posix(),
                "sha256": sha(output_raw),
                "role": "non_authoritative_supervisor_authorized_repair_candidate",
            },
            {
                "path": BOUNDARY_REL.as_posix(),
                "sha256": sha(boundary_raw),
                "role": "exact_non_authoritative_repair_candidate_detector_input_boundary",
            },
        ]
    )
    if {key: value for key, value in article.items() if key != "additional_artifacts"} != protected:
        raise SystemExit("protected Somatic registry fields changed")
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "PASS",
                "source": {"path": SOURCE_REL.as_posix(), "blob": SOURCE_BLOB, "sha256": SOURCE_SHA, **counts(source_raw)},
                "output": {"path": OUTPUT_REL.as_posix(), "blob": git_text("hash-object", OUTPUT_REL.as_posix()), "sha256": sha(output_raw), **counts(output_raw)},
                "boundary": {"path": BOUNDARY_REL.as_posix(), "blob": git_text("hash-object", BOUNDARY_REL.as_posix()), "sha256": sha(boundary_raw), **counts(boundary_raw)},
                "diff": {"path": DIFF_REL.as_posix(), "blob": git_text("hash-object", DIFF_REL.as_posix()), "sha256": sha(diff_run.stdout.encode("utf-8"))},
                "deleted": {"sha256": OLD_SHA, **counts(old_raw)},
                "inserted": {"sha256": NEW_SHA, **counts(new_raw)},
                "links": 16,
                "native_placeholders": 7,
                "forward_traceability": "PASS",
                "reverse_traceability": "PASS",
                "unexplained_substantive_deltas": 0,
                "source_integrity": "PASS",
                "quarantine_hits": quarantine_hits,
                "artifact_registration": "PASS_2_ADDITIONAL_ARTIFACTS_ONLY",
                "registered_master_sha256": sha(master_raw),
                "detector_calls": 0,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
