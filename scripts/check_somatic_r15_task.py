#!/usr/bin/env python3
"""Preflight and acceptance checks for the exclusive Somatic R15 task."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "tasks/ACTIVE-TASK.json"
EXPECTED_TASK = "somatic-r15-clean-continuation-20260830"
EXPECTED_BRANCH = "task/somatic-r15-clean-continuation-20260830"
EXPECTED_MASTER_SHA256 = "1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202"
EXPECTED_FILES = {
    "articles/somatic-therapies/experiments/R15-PANGRAM-LOCALIZED-REWRITE-CANDIDATE-20260825.md": (
        "e7a541e75cf06878c206bcd7d78440bb73593a0a5a2169df1446ce42ad7186ee"
    ),
    "articles/somatic-therapies/experiments/R15-PRESERVATION-AND-COLD-AUDIT-RECEIPT-20260825.md": (
        "be2b848cfa483425c994eb2fe1fafc8cd6e3221632bac608d9940b6550fa4367"
    ),
    "articles/somatic-therapies/experiments/R15-WHOLE-ARTICLE-PANGRAM-BOUNDARY-20260830.txt": (
        "9a81bd04252a2ee851dd111040c600837bdf0a7bbf71c42c293e3b763c99a707"
    ),
}
EXPECTED_BLOBS = {
    "articles/somatic-therapies/experiments/R15-PANGRAM-LOCALIZED-REWRITE-CANDIDATE-20260825.md": (
        "e6210eb2742de156f0bd7b01fdde269f9b9625c6"
    ),
    "articles/somatic-therapies/experiments/R15-PRESERVATION-AND-COLD-AUDIT-RECEIPT-20260825.md": (
        "9bba365c498bc9f51bd16fe2761455a6b233d1bf"
    ),
}
SUSPENDED = {
    "R16",
    "R17-R58",
    "R59-R65",
    "PR #72",
    "stale Codex-V5 instructions",
    "old Work/Codex conversations",
    "generic roadmaps",
    "historical Shaking reservations unrelated to the exact R15 candidate",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def preflight() -> list[str]:
    failures: list[str] = []
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    if lock.get("taskId") != EXPECTED_TASK:
        failures.append("TASK_ID_MISMATCH")
    if lock.get("status") != "active" or lock.get("exclusive") is not True:
        failures.append("ACTIVE_EXCLUSIVE_LOCK_MISSING")
    if lock.get("requiredBranch") != EXPECTED_BRANCH or git("branch", "--show-current") != EXPECTED_BRANCH:
        failures.append("REQUIRED_BRANCH_MISMATCH")
    if set(lock.get("suspendedTaskSources", [])) != SUSPENDED:
        failures.append("SUSPENDED_TASK_SOURCES_MISMATCH")

    checkpoint = ROOT / lock.get("currentStatePath", "")
    checkpoint_text = checkpoint.read_text(encoding="utf-8") if checkpoint.is_file() else ""
    if EXPECTED_TASK not in checkpoint_text:
        failures.append("RECOVERY_TASK_ID_MISSING")
    if lock.get("completionCommand", "") not in checkpoint_text:
        failures.append("COMPLETION_COMMAND_MISSING_FROM_RECOVERY")

    for relative, expected in EXPECTED_FILES.items():
        path = ROOT / relative
        if not path.is_file() or sha256(path) != expected:
            failures.append(f"SHA256_MISMATCH:{relative}")
    for relative, expected in EXPECTED_BLOBS.items():
        path = ROOT / relative
        if not path.is_file() or git("hash-object", str(path)) != expected:
            failures.append(f"GIT_BLOB_MISMATCH:{relative}")
    if sha256(ROOT / "articles/somatic-therapies/master.html") != EXPECTED_MASTER_SHA256:
        failures.append("REGISTERED_MASTER_CHANGED")
    return failures


def acceptance() -> list[str]:
    failures = preflight()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    if lock.get("status") != "ready_for_owner_review":
        failures.append("TASK_NOT_READY_FOR_OWNER_REVIEW")
    for category in ("requiredArtifacts", "requiredDocumentation"):
        for relative in lock.get("acceptance", {}).get(category, []):
            if not (ROOT / relative).is_file():
                failures.append(f"REQUIRED_ARTIFACT_MISSING:{relative}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--acceptance", action="store_true")
    args = parser.parse_args()

    failures = preflight() if args.preflight else acceptance()
    if failures:
        for failure in failures:
            print(failure)
        return 1
    print("SOMATIC_R15_TASK_PREFLIGHT_PASS" if args.preflight else "SOMATIC_R15_TASK_ACCEPTANCE_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
