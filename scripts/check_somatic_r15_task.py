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
HUMANIZATION_CONTROL_PATH = (
    ROOT
    / "tasks"
    / "somatic-r15-clean-continuation-20260830"
    / "HUMANIZATION-CONTROL-STATE-20260831.json"
)
HUMANIZATION_CONTROL_VALIDATOR = ROOT / "scripts" / "validate_humanization_control.py"
EXPECTED_TASK = "somatic-r15-clean-continuation-20260830"
EXPECTED_BRANCH = "task/somatic-r15-clean-continuation-20260830"
EXPECTED_MASTER_SHA256 = "1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202"
EXPECTED_OWNER_OUTCOME_SHA256 = "d851f7ac7cd7289947b6766600c490e3344b48aac652aece20a645b7b0f3200a"
EXPECTED_TASK_CONTRACT_SHA256 = "52c0ce0bebb03adc51a32b8f4832523d01e643dedccee1735a05f987391ce7b8"
EXPECTED_TARGET_HUMAN = 1.0
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


def humanization_control_failures() -> list[str]:
    """Require the exact task-local control to be in a structurally valid state."""
    if not HUMANIZATION_CONTROL_PATH.is_file() or not HUMANIZATION_CONTROL_VALIDATOR.is_file():
        return ["HUMANIZATION_CONTROL_MISSING"]
    result = subprocess.run(
        [
            "python3",
            str(HUMANIZATION_CONTROL_VALIDATOR),
            str(HUMANIZATION_CONTROL_PATH),
            "--root",
            str(ROOT),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return [] if result.returncode == 0 else ["HUMANIZATION_CONTROL_INVALID"]


def preflight() -> list[str]:
    failures: list[str] = []
    failures.extend(humanization_control_failures())
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    if lock.get("taskId") != EXPECTED_TASK:
        failures.append("TASK_ID_MISMATCH")
    if lock.get("status") not in {"active", "owner_outcome_achieved"} or lock.get("exclusive") is not True:
        failures.append("ACTIVE_EXCLUSIVE_LOCK_MISSING")
    if lock.get("requiredBranch") != EXPECTED_BRANCH or git("branch", "--show-current") != EXPECTED_BRANCH:
        failures.append("REQUIRED_BRANCH_MISMATCH")
    if set(lock.get("suspendedTaskSources", [])) != SUSPENDED:
        failures.append("SUSPENDED_TASK_SOURCES_MISMATCH")

    owner_outcome = lock.get("ownerOutcome", {})
    if owner_outcome.get("sha256") != EXPECTED_OWNER_OUTCOME_SHA256:
        failures.append("OWNER_OUTCOME_IDENTITY_MISMATCH")

    task_contract = lock.get("taskContract", {})
    contract_path = ROOT / task_contract.get("path", "")
    if (
        not contract_path.is_file()
        or task_contract.get("sha256") != EXPECTED_TASK_CONTRACT_SHA256
        or sha256(contract_path) != EXPECTED_TASK_CONTRACT_SHA256
    ):
        failures.append("TASK_CONTRACT_IDENTITY_MISMATCH")

    reconciliation = lock.get("objectiveReconciliation", {})
    reconciliation_path = ROOT / reconciliation.get("path", "")
    if not reconciliation_path.is_file():
        failures.append("OBJECTIVE_RECONCILIATION_MISSING")
    else:
        reconciliation_record = json.loads(reconciliation_path.read_text(encoding="utf-8"))
        alignment = reconciliation_record.get("alignment", {})
        if alignment.get("contractToOwner", {}).get("status") != "MATCH":
            failures.append("CONTRACT_TO_OWNER_NOT_MATCH")
        if reconciliation_record.get("ownerSource", {}).get("sha256") != EXPECTED_OWNER_OUTCOME_SHA256:
            failures.append("RECONCILIATION_OWNER_SOURCE_MISMATCH")

    receipt_path = ROOT / owner_outcome.get("sourceReceipt", "")
    if not receipt_path.is_file():
        failures.append("OWNER_SOURCE_RECEIPT_MISSING")
    else:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        if receipt.get("ownerOutcomeSha256") != EXPECTED_OWNER_OUTCOME_SHA256:
            failures.append("OWNER_SOURCE_RECEIPT_MISMATCH")

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


def outcome_acceptance_failures(lock: dict, reconciliation: dict) -> list[str]:
    """Return fail-closed owner-outcome findings for already-loaded records."""
    failures: list[str] = []
    if lock.get("status") != "owner_outcome_achieved":
        failures.append("OWNER_OUTCOME_NOT_ACHIEVED")
    if lock.get("objectiveReconciliation", {}).get("typedCompletionClaim") != "OWNER_OUTCOME_ACHIEVED":
        failures.append("COMPLETION_CLAIM_NOT_OWNER_OUTCOME_ACHIEVED")
    if reconciliation.get("completionClaim", {}).get("type") != "OWNER_OUTCOME_ACHIEVED":
        failures.append("RECONCILIATION_COMPLETION_CLAIM_MISMATCH")
    terminal = reconciliation.get("terminalComparator", {})
    if terminal.get("rootTerminalizationAllowed") is not True or terminal.get("unmetOutcomeIds") != []:
        failures.append("TERMINAL_COMPARATOR_REJECTED")

    final_outcome = lock.get("finalOutcome", {})
    pangram = final_outcome.get("pangram", {})
    if pangram.get("fractionHuman") != EXPECTED_TARGET_HUMAN:
        failures.append("PANGRAM_100_PERCENT_HUMAN_MISSING")
    if not pangram.get("exactBoundarySha256") or pangram.get("candidateSha256") != final_outcome.get("candidateSha256"):
        failures.append("FINAL_PANGRAM_CANDIDATE_BINDING_MISSING")
    gates = final_outcome.get("gates", {})
    required_pass_gates = {
        "sourceIntegrity",
        "forwardTraceability",
        "reverseTraceability",
        "semanticSanity",
        "architectureMultiscale",
        "coldAudit",
        "independentFinalReader",
        "linksAndNativeObjects",
        "failedBranchContamination",
    }
    for gate in required_pass_gates:
        if gates.get(gate) != "PASS":
            failures.append(f"FINAL_GATE_NOT_PASS:{gate}")
    if final_outcome.get("unexplainedSubstantiveDeltas") != 0:
        failures.append("UNEXPLAINED_SUBSTANTIVE_DELTAS")
    delivery = final_outcome.get("chatDelivery", {})
    if not delivery.get("conversationUrl"):
        failures.append("FINAL_CHAT_URL_MISSING")
    if not delivery.get("finalDraftSha256") or not delivery.get("commentableDiffSha256"):
        failures.append("FINAL_CHAT_ARTIFACT_BINDING_MISSING")
    return failures


def acceptance() -> list[str]:
    failures = preflight()
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    reconciliation_path = ROOT / lock.get("objectiveReconciliation", {}).get("path", "")
    reconciliation = (
        json.loads(reconciliation_path.read_text(encoding="utf-8"))
        if reconciliation_path.is_file()
        else {}
    )
    failures.extend(outcome_acceptance_failures(lock, reconciliation))
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
