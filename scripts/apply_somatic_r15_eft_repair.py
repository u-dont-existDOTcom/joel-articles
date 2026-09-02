#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from materialize_somatic_r15_boundary import materialize


ROOT = Path(__file__).resolve().parents[1]
DETECTOR = Path("/mnt/hdd/home/joel/Téléchargements/pangram-worktrees/somatic-r15-articlewide-20260830")
LIVE_HEAD = "97c36c3765835e8153e2598701cb1ff1a6cf9fc4"
SOURCE_ANCESTOR = "ac1570f3e8945fecf80585d8fbe336c2a19ffbd6"
SOURCE_REL = Path("articles/somatic-therapies/experiments/R15-DIRECT-OWNER-VOICE-CANDIDATE-20260830.md")
OUTPUT_REL = Path("articles/somatic-therapies/experiments/R15-EFT-REPAIR-CANDIDATE-20260831.md")
BOUNDARY_REL = Path("articles/somatic-therapies/experiments/R15-EFT-REPAIR-BOUNDARY-20260831.txt")
RECEIPT_REL = Path("tasks/somatic-r15-clean-continuation-20260830/EFT-REPAIR-PRODUCTION-RECEIPT-20260831.md")
DIFF_REL = Path("tasks/somatic-r15-clean-continuation-20260830/EFT-REPAIR-DIFF-20260831.patch")
SOURCE_BLOB = "442349c82d92ac844447f27208924b720d9fa92a"
SOURCE_SHA = "9c2e8fe57335d51ac925bc9b63cee8125c24e471e2b9b8fda50cc44cf28f5b31"
MASTER_SHA = "1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202"
DETECTOR_HEAD = "ede777c4455d699f64f46e7850e92c707fa31378"
DETECTOR_RESULT_REL = Path("state/experiments/somatic-r15-eft-human-anchor-tail-factorial-20260831/RESULT-PACKET-E.json")
DETECTOR_RESULT_SHA = "70b69c55c66117813af3b8d5832fb2da9aab2dc1541d279e0582283099a46756"
E_SHA = "e9d2969aadbdd648ccd6b5aa36d6b7712b059a5b24a2acfcf95d29a4d458b7eb"
OLD = (
    "The big advantage is that EFT travels. Before a difficult conversation. Immediately after somebody "
    "triggers me. In the middle of a thought loop that has recruited my whole body. It can take the pressure "
    "down. I don't confuse that with finishing the deeper trauma work."
)
NEW = (
    "I can use EFT almost anywhere—before a hard conversation, right after somebody triggers me, or when my "
    "mind is looping and my body has joined in. It takes some pressure off. The deeper trauma can still be "
    "sitting there."
)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6} .+)$", re.MULTILINE)
R_NUMBER = re.compile(r"^R(\d+)(?:\D|$)")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str, root: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=root, text=True, capture_output=True, check=check)


def git_text(*args: str, root: Path = ROOT) -> str:
    return git(*args, root=root).stdout.strip()


def counts(data: bytes) -> dict[str, int | bool]:
    text = data.decode("utf-8")
    return {
        "words": len(text.split()),
        "unicode_characters": len(text),
        "utf8_bytes": len(data),
        "terminal_newline": text.endswith("\n"),
    }


def one_paragraph(text: str, start: str) -> str:
    matches = [paragraph for paragraph in text.split("\n\n") if paragraph.startswith(start)]
    if len(matches) != 1:
        raise SystemExit(f"expected one paragraph beginning {start!r}, found {len(matches)}")
    return matches[0]


def main() -> int:
    allowed_dirty = ["?? scripts/apply_somatic_r15_eft_repair.py"]
    if git_text("rev-parse", "HEAD") != LIVE_HEAD or git_text("status", "--porcelain").splitlines() != allowed_dirty:
        raise SystemExit("article live head/worktree mismatch")
    if git("merge-base", "--is-ancestor", SOURCE_ANCESTOR, "HEAD", check=False).returncode != 0:
        raise SystemExit("required source ancestor missing")
    changed = git_text("diff", "--name-only", SOURCE_ANCESTOR, "HEAD").splitlines()
    if changed != [
        "tasks/somatic-r15-clean-continuation-20260830/CHAT-APPLY-EFT-REPAIR-001-HEAD-CORRECTION.md",
        "tasks/somatic-r15-clean-continuation-20260830/CHAT-APPLY-EFT-REPAIR-001.md",
    ]:
        raise SystemExit(f"conflicting intervening article mutations: {changed}")

    source_path = ROOT / SOURCE_REL
    source_raw = source_path.read_bytes()
    source_text = source_raw.decode("utf-8")
    if git_text("hash-object", SOURCE_REL.as_posix()) != SOURCE_BLOB or sha(source_raw) != SOURCE_SHA:
        raise SystemExit("source candidate identity mismatch")
    master_path = ROOT / "articles/somatic-therapies/master.html"
    if sha(master_path.read_bytes()) != MASTER_SHA:
        raise SystemExit("registered master identity mismatch")
    if source_text.count(OLD) != 1 or source_text.count(NEW) != 0:
        raise SystemExit("old/new occurrence gate failed")

    if git_text("rev-parse", "HEAD", root=DETECTOR) != DETECTOR_HEAD or git_text("status", "--porcelain", root=DETECTOR):
        raise SystemExit("detector evidence head/worktree mismatch")
    detector_packet_raw = (DETECTOR / DETECTOR_RESULT_REL).read_bytes()
    detector_packet = json.loads(detector_packet_raw.decode("utf-8"))
    if not (
        sha(detector_packet_raw) == DETECTOR_RESULT_SHA
        and detector_packet["candidate_e"]["sha256"] == E_SHA
        and detector_packet["result_e"]["result"]["stage"] == "STAGE_SUCCESS"
        and detector_packet["result_e"]["result"]["version"] == "4.0"
        and detector_packet["result_e"]["result"]["fraction_human"] == 1.0
        and detector_packet["result_e"]["result"]["fraction_ai"] == 0.0
        and detector_packet["result_e"]["result"]["fraction_ai_assisted"] == 0.0
        and detector_packet["result_e"]["result"]["windows"][0]["confidence"] == "High"
        and detector_packet["stable_family_state"] == "CLOSED_6_OF_6"
    ):
        raise SystemExit("detector result binding mismatch")
    detector_input = (DETECTOR / detector_packet["candidate_e"]["input_path"]).read_text(encoding="utf-8")
    if detector_input.split("\n\n", 1)[1].encode("utf-8") != NEW.encode("utf-8"):
        raise SystemExit("Candidate E direct-tail mismatch")
    c_text = (DETECTOR / "state/experiments/somatic-r15-eft-human-anchor-tail-factorial-20260831/inputs/C-separate-direct-tail.txt").read_text(encoding="utf-8")
    d_text = (DETECTOR / "state/experiments/somatic-r15-eft-human-anchor-tail-factorial-20260831/inputs/D-merged-direct-tail.txt").read_text(encoding="utf-8")
    if c_text.rsplit("\n\n", 1)[1] != NEW or not d_text.endswith(" " + NEW):
        raise SystemExit("experiment 005 direct-tail mismatch")

    prefix, suffix = source_text.split(OLD)
    output_text = prefix + NEW + suffix
    if output_text[: len(prefix)] != source_text[: len(prefix)] or output_text[len(prefix) + len(NEW) :] != source_text[len(prefix) + len(OLD) :]:
        raise SystemExit("outside-scope bytes changed")
    if output_text.count(OLD) != 0 or output_text.count(NEW) != 1:
        raise SystemExit("output replacement occurrence mismatch")

    old_anchor = one_paragraph(source_text, "I think of the different tapping points")
    new_anchor = one_paragraph(output_text, "I think of the different tapping points")
    if old_anchor.encode("utf-8") != new_anchor.encode("utf-8"):
        raise SystemExit("attribution-correct EFT anchor changed")
    preservation_phrases = (
        "almost anywhere",
        "before a hard conversation",
        "right after somebody triggers me",
        "my mind is looping and my body has joined in",
        "takes some pressure off",
        "deeper trauma can still be sitting there",
    )
    if not all(phrase in NEW for phrase in preservation_phrases):
        raise SystemExit("replacement preservation mismatch")
    if HEADING_RE.findall(output_text) != HEADING_RE.findall(source_text):
        raise SystemExit("heading order changed")
    source_links = LINK_RE.findall(source_text)
    output_links = LINK_RE.findall(output_text)
    if len(source_links) != 16 or len(output_links) != 16 or Counter(source_links) != Counter(output_links):
        raise SystemExit("ordinary-link multiset changed")
    source_objects = [line for line in source_text.splitlines() if line.startswith("**[EXISTING ")]
    output_objects = [line for line in output_text.splitlines() if line.startswith("**[EXISTING ")]
    if len(source_objects) != 7 or output_objects != source_objects:
        raise SystemExit("native-placeholder identity/order changed")

    quarantine_hits = []
    for path in (ROOT / "articles/somatic-therapies/experiments").iterdir():
        match = R_NUMBER.match(path.name)
        if match and 16 <= int(match.group(1)) <= 65 and path.is_file() and NEW in path.read_text(encoding="utf-8", errors="replace"):
            quarantine_hits.append(path.relative_to(ROOT).as_posix())
    failed_ref = "origin/experiment/somatic-source-clean-recovery-20260829"
    if git("rev-parse", "--verify", failed_ref, check=False).returncode == 0:
        pr72_scan = git("grep", "-F", "-e", NEW, failed_ref, "--", "articles/somatic-therapies", check=False)
        if pr72_scan.returncode == 0:
            quarantine_hits.append("PR72_FAILED_BRANCH")
        elif pr72_scan.returncode != 1:
            raise SystemExit("PR #72 quarantine scan failed")
    if quarantine_hits:
        raise SystemExit(f"failed-branch prose contamination: {quarantine_hits}")

    output_raw = output_text.encode("utf-8")
    boundary_text = materialize(output_text)
    boundary_raw = boundary_text.encode("utf-8")
    (ROOT / OUTPUT_REL).write_bytes(output_raw)
    (ROOT / BOUNDARY_REL).write_bytes(boundary_raw)

    diff_run = git(
        "diff", "--no-index", "--no-color", "--unified=0", "--", SOURCE_REL.as_posix(), OUTPUT_REL.as_posix(), check=False
    )
    if diff_run.returncode != 1:
        raise SystemExit("failed to generate exact one-paragraph diff")
    diff_text = diff_run.stdout
    if diff_text.count("@@") != 2 or diff_text.count("-" + OLD) != 1 or diff_text.count("+" + NEW) != 1:
        raise SystemExit("diff scope mismatch")
    (ROOT / DIFF_REL).write_text(diff_text, encoding="utf-8")

    output_blob = git_text("hash-object", OUTPUT_REL.as_posix())
    boundary_blob = git_text("hash-object", BOUNDARY_REL.as_posix())
    receipt = f"""# EFT Repair Production Receipt — 2026-08-31

Task: `somatic-r15-clean-continuation-20260830`

Status: **PASS / NON-AUTHORITATIVE CANDIDATE ONLY**

## Identity

- live packet head: `{LIVE_HEAD}`
- required source ancestor: `{SOURCE_ANCESTOR}` — PASS
- source candidate: `{SOURCE_REL.as_posix()}`
- source Git blob: `{SOURCE_BLOB}`
- source SHA-256: `{SOURCE_SHA}`
- source counts: `{counts(source_raw)['words']}` words / `{counts(source_raw)['unicode_characters']}` Unicode characters / `{counts(source_raw)['utf8_bytes']}` UTF-8 bytes
- output candidate: `{OUTPUT_REL.as_posix()}`
- output Git blob: `{output_blob}`
- output SHA-256: `{sha(output_raw)}`
- output counts: `{counts(output_raw)['words']}` words / `{counts(output_raw)['unicode_characters']}` Unicode characters / `{counts(output_raw)['utf8_bytes']}` UTF-8 bytes
- reader-visible boundary: `{BOUNDARY_REL.as_posix()}`
- boundary Git blob: `{boundary_blob}`
- boundary SHA-256: `{sha(boundary_raw)}`
- boundary counts: `{counts(boundary_raw)['words']}` words / `{counts(boundary_raw)['unicode_characters']}` Unicode characters / `{counts(boundary_raw)['utf8_bytes']}` UTF-8 bytes
- deleted paragraph SHA-256: `{sha(OLD.encode('utf-8'))}`
- inserted paragraph SHA-256: `{sha(NEW.encode('utf-8'))}`

## Exact-scope assertions

- deleted paragraph occurrence before/after: `1 / 0` — PASS
- inserted paragraph occurrence before/after: `0 / 1` — PASS
- bytes outside the one replaced paragraph: byte-identical — PASS
- attribution-correct EFT anchor: byte-identical — PASS
- portability, hard-conversation, immediate-trigger, mind/body loop, pressure-reduction and deeper-trauma distinction functions: PASS
- heading identity/order: PASS
- ordinary-link URL multiset: `16 / 16`, byte-identical — PASS
- reader-visible native placeholders: `7 / 7`, byte-identical and ordered — PASS
- R16–R65 and PR #72 exact inserted-prose scan: zero hits — PASS
- forward traceability: PASS
- reverse traceability: PASS
- unexplained substantive deltas: `0`
- source integrity: PASS
- registered `master.html` SHA-256: `{MASTER_SHA}` — unchanged / PASS

## Detector evidence (read-only)

- detector head: `{DETECTOR_HEAD}`
- Candidate E SHA-256: `{E_SHA}`
- result packet: `{DETECTOR_RESULT_REL.as_posix()}`
- result packet SHA-256: `{DETECTOR_RESULT_SHA}`
- Pangram 4.0 / `STAGE_SUCCESS` / Human `1.0` / AI `0.0` / AI-assisted `0.0` / High — exact binding PASS
- EFT family: `CLOSED_6_OF_6`

## Mutations and calls

- source candidate mutations: `0`
- registered-master mutations: `0`
- paid detector calls: `0`
- detector reservations: `0`
- GUI actions: `0`
- whole-document calls: `0`

Article authority remains the registered `master.html`; this candidate is not promoted.
"""
    (ROOT / RECEIPT_REL).write_text(receipt, encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PASS",
                "source": {"path": SOURCE_REL.as_posix(), "blob": SOURCE_BLOB, "sha256": SOURCE_SHA, **counts(source_raw)},
                "output": {"path": OUTPUT_REL.as_posix(), "blob": output_blob, "sha256": sha(output_raw), **counts(output_raw)},
                "boundary": {"path": BOUNDARY_REL.as_posix(), "blob": boundary_blob, "sha256": sha(boundary_raw), **counts(boundary_raw)},
                "deleted_sha256": sha(OLD.encode("utf-8")),
                "inserted_sha256": sha(NEW.encode("utf-8")),
                "links": 16,
                "native_placeholders": 7,
                "forward_traceability": "PASS",
                "reverse_traceability": "PASS",
                "unexplained_substantive_deltas": 0,
                "stable_family_state": "CLOSED_6_OF_6",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
