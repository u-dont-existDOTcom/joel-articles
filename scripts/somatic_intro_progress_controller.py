#!/usr/bin/env python3
"""Deterministic, fail-closed Somatic Introduction progress controller.

The controller stores externally supplied semantic judgments.  It never writes,
scores, ranks, or edits article prose.  Raw samples remain quarantined until a
hash-bound verifier receipt satisfies the promotion interlock.
"""

from __future__ import annotations

import argparse
import contextlib
import copy
import fcntl
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterator


SCHEMA_VERSION = 1
CONTROLLER_VERSION = "1.0.0"
DEFAULT_CONTROLLER_DIR = Path(
    "articles/somatic-therapies/experiments/somatic-intro-progress-controller"
)
DEFAULT_SEMANTIC_TASK = Path(
    "articles/somatic-therapies/experiments/"
    "SOMATIC-INTRO-CURRENT-MANUAL-TASK-20260831.md"
)
DEFAULT_LESSON_CONTRACT = Path(
    "articles/somatic-therapies/experiments/"
    "SOMATIC-INTRO-ACTIVE-LESSON-CONTRACT-20260831.md"
)
SAMPLE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
STATUS_VALUES = {
    "QUARANTINED",
    "ADJUDICATED",
    "PROMOTED",
    "RETAINED_ALT",
    "REJECTED",
}
COMPARISONS = {"DOMINATES", "NONDOMINATED", "REGRESSES", "INCOMPARABLE"}


class ControllerError(RuntimeError):
    """A fail-closed controller error suitable for a stable CLI response."""


def _canonical_json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode(
        "utf-8"
    )


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _nonblank(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_sha(value: object, field: str) -> str:
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ControllerError(f"{field} must be a lowercase SHA-256")
    return value


def _validate_id(value: object, field: str) -> str:
    if not isinstance(value, str) or not SAMPLE_ID_RE.fullmatch(value):
        raise ControllerError(f"{field} must match {SAMPLE_ID_RE.pattern}")
    return value


def _require_fields(value: dict[str, Any], fields: tuple[str, ...], label: str) -> None:
    missing = [field for field in fields if field not in value]
    if missing:
        raise ControllerError(f"{label} is missing required fields: {', '.join(missing)}")


def _repo_path(root: Path, relative: str | Path) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise ControllerError(f"repository path must be safe and relative: {relative}")
    resolved_root = root.resolve()
    resolved = (resolved_root / rel).resolve()
    if resolved != resolved_root and resolved_root not in resolved.parents:
        raise ControllerError(f"repository path escapes root: {relative}")
    return resolved


def _relative_to_root(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise ControllerError(f"path must be within repository root: {path}") from exc


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ControllerError(f"missing JSON file: {path}") from exc
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ControllerError(f"invalid JSON file: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ControllerError(f"JSON root must be an object: {path}")
    return value


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if temporary.exists():
            temporary.unlink()


def _write_immutable(path: Path, content: bytes) -> bool:
    """Create exact bytes once; return False for an identical idempotent replay."""

    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() == content:
            return False
        raise ControllerError(f"immutable identity conflict: {path}")
    try:
        with path.open("xb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError:
        if path.read_bytes() == content:
            return False
        raise ControllerError(f"immutable identity conflict: {path}")
    return True


def _append_jsonl_once(path: Path, identity_field: str, identity: str, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                existing = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ControllerError(f"invalid append-only history at {path}:{number}") from exc
            if isinstance(existing, dict) and existing.get(identity_field) == identity:
                if existing == value:
                    return
                raise ControllerError(
                    f"append-only identity conflict for {identity_field}={identity} in {path}"
                )
    line = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(line)
        handle.flush()
        os.fsync(handle.fileno())


@contextlib.contextmanager
def _controller_lock(controller: Path) -> Iterator[None]:
    controller.mkdir(parents=True, exist_ok=True)
    lock_path = controller / ".controller.lock"
    with lock_path.open("a+b") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _authority_identity(root: Path, relative_path: str | Path) -> dict[str, str]:
    path = _repo_path(root, relative_path)
    if not path.is_file():
        raise ControllerError(f"authority file does not exist: {relative_path}")
    return {"path": _relative_to_root(root, path), "sha256": sha256_file(path)}


def _validate_authority_identity(root: Path, identity: object, label: str) -> dict[str, str]:
    if not isinstance(identity, dict):
        raise ControllerError(f"{label} must be an object")
    _require_fields(identity, ("path", "sha256"), label)
    if not _nonblank(identity.get("path")):
        raise ControllerError(f"{label}.path must be nonblank")
    expected = _validate_sha(identity.get("sha256"), f"{label}.sha256")
    path = _repo_path(root, identity["path"])
    if not path.is_file():
        raise ControllerError(f"{label} file is missing: {identity['path']}")
    actual = sha256_file(path)
    if actual != expected:
        raise ControllerError(
            f"{label} is stale: expected {expected}, current file is {actual}"
        )
    return {"path": identity["path"], "sha256": expected}


def initial_frontier(
    root: Path,
    *,
    semantic_task: str | Path = DEFAULT_SEMANTIC_TASK,
    lesson_contract: str | Path = DEFAULT_LESSON_CONTRACT,
    next_search_target: dict[str, str] | None = None,
) -> dict[str, Any]:
    target = next_search_target or {
        "id": "reasoning-chat-controller-review",
        "kind": "CONTROLLER_REVIEW",
        "description": (
            "Review the controller implementation before supplying an initial bounded "
            "generation search target or running any real candidate."
        ),
    }
    _validate_search_target(target, allow_review=True)
    return {
        "schema_version": SCHEMA_VERSION,
        "controller_version": CONTROLLER_VERSION,
        "article_id": "somatic-therapies",
        "scope": {
            "heading": "# Introduction",
            "end_before": "## Your Physical State Can Change What Therapy Does",
        },
        "semantic_task": _authority_identity(root, semantic_task),
        "active_lesson_contract": _authority_identity(root, lesson_contract),
        "best_promoted_owner_facing_candidate": None,
        "retained_nondominated_alternatives": [],
        "semantic_provenance_hard_constraint_status": "UNASSESSED",
        "cleared_dimensions": [],
        "unresolved_defects": [],
        "strongest_known_generative_failure_pattern": None,
        "next_search_target": target,
        "last_promotion_receipt": None,
        "append_only_history": {
            "samples": "history/samples.jsonl",
            "adjudications": "history/adjudications.jsonl",
            "promotions": "history/promotions.jsonl",
            "controller_decisions": "history/controller-decisions.jsonl",
        },
        "revision": 0,
    }


def initialize_controller(
    root: Path,
    controller_dir: Path = DEFAULT_CONTROLLER_DIR,
    *,
    semantic_task: str | Path = DEFAULT_SEMANTIC_TASK,
    lesson_contract: str | Path = DEFAULT_LESSON_CONTRACT,
    next_search_target: dict[str, str] | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    controller = _repo_path(root, controller_dir)
    state_path = controller / "frontier.json"
    expected = initial_frontier(
        root,
        semantic_task=semantic_task,
        lesson_contract=lesson_contract,
        next_search_target=next_search_target,
    )
    with _controller_lock(controller):
        if state_path.exists():
            existing = _read_json(state_path)
            validate_frontier(root, existing)
            return existing
        for name in ("samples", "adjudications", "promotions", "decisions", "history"):
            (controller / name).mkdir(parents=True, exist_ok=True)
        _atomic_write(state_path, _canonical_json_bytes(expected))
    return expected


def _validate_dimension_list(value: object, field: str) -> list[str]:
    if not isinstance(value, list):
        raise ControllerError(f"{field} must be an array")
    result: list[str] = []
    for index, item in enumerate(value):
        if not _nonblank(item):
            raise ControllerError(f"{field}[{index}] must be nonblank")
        if item in result:
            raise ControllerError(f"{field} must not contain duplicate dimension IDs")
        result.append(item)
    return result


def _validate_defects(value: object, field: str = "unresolved_defects") -> list[dict[str, Any]]:
    if not isinstance(value, list):
        raise ControllerError(f"{field} must be an array")
    defects: list[dict[str, Any]] = []
    ranks: set[int] = set()
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise ControllerError(f"{field}[{index}] must be an object")
        _require_fields(item, ("rank", "dimension_id", "description"), f"{field}[{index}]")
        rank = item["rank"]
        if not isinstance(rank, int) or isinstance(rank, bool) or rank < 1 or rank in ranks:
            raise ControllerError(f"{field}[{index}].rank must be a unique positive integer")
        ranks.add(rank)
        if not _nonblank(item["dimension_id"]) or not _nonblank(item["description"]):
            raise ControllerError(
                f"{field}[{index}] dimension_id and description must be nonblank"
            )
        defects.append(copy.deepcopy(item))
    if defects and sorted(ranks) != list(range(1, len(defects) + 1)):
        raise ControllerError(f"{field} ranks must be contiguous starting at 1")
    return sorted(defects, key=lambda item: item["rank"])


def _validate_search_target(value: object, *, allow_review: bool = False) -> dict[str, str]:
    if not isinstance(value, dict):
        raise ControllerError("next_search_target must be an object")
    _require_fields(value, ("id", "kind", "description"), "next_search_target")
    if not all(_nonblank(value.get(field)) for field in ("id", "kind", "description")):
        raise ControllerError("next_search_target fields must be nonblank")
    allowed = {"GENERATION"}
    if allow_review:
        allowed.add("CONTROLLER_REVIEW")
    if value["kind"] not in allowed:
        raise ControllerError(
            f"next_search_target.kind must be one of {', '.join(sorted(allowed))}"
        )
    return {field: value[field] for field in ("id", "kind", "description")}


def _validate_candidate_identity(value: object, field: str, *, nullable: bool) -> dict[str, str] | None:
    if value is None and nullable:
        return None
    if not isinstance(value, dict):
        raise ControllerError(f"{field} must be an object" + (" or null" if nullable else ""))
    _require_fields(value, ("sample_id", "sha256", "candidate_path"), field)
    if not _nonblank(value["candidate_path"]):
        raise ControllerError(f"{field}.candidate_path must be nonblank")
    return {
        "sample_id": _validate_id(value["sample_id"], f"{field}.sample_id"),
        "sha256": _validate_sha(value["sha256"], f"{field}.sha256"),
        "candidate_path": value["candidate_path"],
    }


def validate_frontier(root: Path, state: dict[str, Any]) -> None:
    _require_fields(
        state,
        (
            "schema_version",
            "controller_version",
            "article_id",
            "scope",
            "semantic_task",
            "active_lesson_contract",
            "best_promoted_owner_facing_candidate",
            "retained_nondominated_alternatives",
            "semantic_provenance_hard_constraint_status",
            "cleared_dimensions",
            "unresolved_defects",
            "strongest_known_generative_failure_pattern",
            "next_search_target",
            "last_promotion_receipt",
            "append_only_history",
            "revision",
        ),
        "frontier",
    )
    if state["schema_version"] != SCHEMA_VERSION:
        raise ControllerError("unsupported frontier schema_version")
    if state["controller_version"] != CONTROLLER_VERSION:
        raise ControllerError("unsupported controller_version")
    if state["article_id"] != "somatic-therapies":
        raise ControllerError("frontier article_id must be somatic-therapies")
    if state["scope"] != {
        "heading": "# Introduction",
        "end_before": "## Your Physical State Can Change What Therapy Does",
    }:
        raise ControllerError("frontier scope must be the exact Introduction boundary")
    _validate_authority_identity(root, state["semantic_task"], "semantic_task")
    _validate_authority_identity(
        root, state["active_lesson_contract"], "active_lesson_contract"
    )
    _validate_candidate_identity(
        state["best_promoted_owner_facing_candidate"],
        "best_promoted_owner_facing_candidate",
        nullable=True,
    )
    alternatives = state["retained_nondominated_alternatives"]
    if not isinstance(alternatives, list):
        raise ControllerError("retained_nondominated_alternatives must be an array")
    for index, item in enumerate(alternatives):
        _validate_candidate_identity(item, f"retained_nondominated_alternatives[{index}]", nullable=False)
    if state["semantic_provenance_hard_constraint_status"] not in {
        "UNASSESSED",
        "PASS",
        "FAIL",
    }:
        raise ControllerError("invalid semantic_provenance_hard_constraint_status")
    _validate_dimension_list(state["cleared_dimensions"], "cleared_dimensions")
    _validate_defects(state["unresolved_defects"])
    strongest = state["strongest_known_generative_failure_pattern"]
    if strongest is not None and not _nonblank(strongest):
        raise ControllerError("strongest_known_generative_failure_pattern must be nonblank or null")
    _validate_search_target(state["next_search_target"], allow_review=True)
    if not isinstance(state["append_only_history"], dict):
        raise ControllerError("append_only_history must be an object")
    if not isinstance(state["revision"], int) or isinstance(state["revision"], bool) or state["revision"] < 0:
        raise ControllerError("frontier revision must be a nonnegative integer")


def load_frontier(root: Path, controller_dir: Path = DEFAULT_CONTROLLER_DIR) -> dict[str, Any]:
    root = root.resolve()
    state = _read_json(_repo_path(root, controller_dir) / "frontier.json")
    validate_frontier(root, state)
    return state


def _sample_paths(controller: Path, sample_id: str) -> tuple[Path, Path, Path]:
    sample_dir = controller / "samples" / sample_id
    return sample_dir / "candidate.txt", sample_dir / "record.json", sample_dir / "status.json"


def register_sample(
    root: Path,
    candidate_path: Path,
    sample_id: str,
    *,
    controller_dir: Path = DEFAULT_CONTROLLER_DIR,
    writer_identity: str | None = None,
    writer_context: str | None = None,
    created_at: str,
) -> dict[str, Any]:
    root = root.resolve()
    sample_id = _validate_id(sample_id, "sample_id")
    if not _nonblank(created_at):
        raise ControllerError("created_at must be a nonblank externally supplied timestamp")
    if writer_identity is not None and not _nonblank(writer_identity):
        raise ControllerError("writer_identity must be nonblank when supplied")
    if writer_context is not None and not _nonblank(writer_context):
        raise ControllerError("writer_context must be nonblank when supplied")
    controller = _repo_path(root, controller_dir)
    content = candidate_path.read_bytes()
    candidate_sha = _sha256_bytes(content)
    candidate_target, record_path, status_path = _sample_paths(controller, sample_id)
    with _controller_lock(controller):
        state = load_frontier(root, controller_dir)
        record = {
            "schema_version": SCHEMA_VERSION,
            "sample_id": sample_id,
            "candidate_sha256": candidate_sha,
            "candidate_path": _relative_to_root(root, candidate_target),
            "writer": {
                "identity": writer_identity,
                "context_id": writer_context,
            },
            "created_at": created_at,
            "initial_status": "QUARANTINED",
            "semantic_task": state["semantic_task"],
            "active_lesson_contract": state["active_lesson_contract"],
        }
        record_bytes = _canonical_json_bytes(record)
        if record_path.exists():
            existing = _read_json(record_path)
            if existing != record or candidate_target.read_bytes() != content:
                raise ControllerError(f"sample identity conflict: {sample_id}")
            if not status_path.exists():
                status = {
                    "schema_version": SCHEMA_VERSION,
                    "sample_id": sample_id,
                    "candidate_sha256": candidate_sha,
                    "current_status": "QUARANTINED",
                    "verifier_receipt": None,
                }
                _atomic_write(status_path, _canonical_json_bytes(status))
            _load_sample(root, controller, sample_id)
            history = {
                "event": "SAMPLE_REGISTERED",
                "sample_id": sample_id,
                "candidate_sha256": candidate_sha,
                "record_path": _relative_to_root(root, record_path),
                "created_at": created_at,
            }
            _append_jsonl_once(
                controller / "history" / "samples.jsonl", "sample_id", sample_id, history
            )
            return existing
        _write_immutable(candidate_target, content)
        _write_immutable(record_path, record_bytes)
        status = {
            "schema_version": SCHEMA_VERSION,
            "sample_id": sample_id,
            "candidate_sha256": candidate_sha,
            "current_status": "QUARANTINED",
            "verifier_receipt": None,
        }
        _atomic_write(status_path, _canonical_json_bytes(status))
        history = {
            "event": "SAMPLE_REGISTERED",
            "sample_id": sample_id,
            "candidate_sha256": candidate_sha,
            "record_path": _relative_to_root(root, record_path),
            "created_at": created_at,
        }
        _append_jsonl_once(controller / "history" / "samples.jsonl", "sample_id", sample_id, history)
    return record


def _load_sample(root: Path, controller: Path, sample_id: str) -> tuple[dict[str, Any], dict[str, Any], bytes]:
    candidate_path, record_path, status_path = _sample_paths(controller, sample_id)
    record = _read_json(record_path)
    status = _read_json(status_path)
    content = candidate_path.read_bytes()
    actual_sha = _sha256_bytes(content)
    if record.get("sample_id") != sample_id or status.get("sample_id") != sample_id:
        raise ControllerError(f"sample identity is inconsistent: {sample_id}")
    expected = _validate_sha(record.get("candidate_sha256"), "sample.candidate_sha256")
    if actual_sha != expected or status.get("candidate_sha256") != expected:
        raise ControllerError(f"sample bytes/hash mismatch: {sample_id}")
    if status.get("current_status") not in STATUS_VALUES:
        raise ControllerError(f"invalid sample status: {sample_id}")
    return record, status, content


def _update_sample_status(
    root: Path,
    controller: Path,
    sample_id: str,
    new_status: str,
    receipt_identity: dict[str, str] | None,
) -> None:
    _, status_path_record, status_path = _sample_paths(controller, sample_id)
    del status_path_record
    status = _read_json(status_path)
    current = status.get("current_status")
    if new_status not in STATUS_VALUES:
        raise ControllerError(f"invalid requested sample status: {new_status}")
    if current == new_status:
        if receipt_identity is not None and status.get("verifier_receipt") != receipt_identity:
            raise ControllerError("sample status replay has a different verifier receipt")
        return
    allowed = {
        "QUARANTINED": {"ADJUDICATED", "REJECTED"},
        "ADJUDICATED": {"PROMOTED", "RETAINED_ALT", "REJECTED"},
        "RETAINED_ALT": {"PROMOTED"},
        "REJECTED": set(),
        "PROMOTED": set(),
    }
    if new_status not in allowed.get(current, set()):
        raise ControllerError(f"invalid sample status transition: {current} -> {new_status}")
    updated = copy.deepcopy(status)
    updated["current_status"] = new_status
    if receipt_identity is not None:
        existing = status.get("verifier_receipt")
        if existing is not None and existing != receipt_identity:
            raise ControllerError("sample already refers to a different verifier receipt")
        updated["verifier_receipt"] = receipt_identity
    _atomic_write(status_path, _canonical_json_bytes(updated))


def _validate_frontier_binding(value: object) -> dict[str, str | None]:
    if not isinstance(value, dict):
        raise ControllerError("current_frontier must be an object")
    _require_fields(value, ("sample_id", "sha256"), "current_frontier")
    sample_id = value["sample_id"]
    sha = value["sha256"]
    if sample_id is None or sha is None:
        if sample_id is not None or sha is not None:
            raise ControllerError("current_frontier sample_id and sha256 must both be null or both set")
        return {"sample_id": None, "sha256": None}
    return {
        "sample_id": _validate_id(sample_id, "current_frontier.sample_id"),
        "sha256": _validate_sha(sha, "current_frontier.sha256"),
    }


def _frontier_binding(state: dict[str, Any]) -> dict[str, str | None]:
    current = state["best_promoted_owner_facing_candidate"]
    if current is None:
        return {"sample_id": None, "sha256": None}
    return {"sample_id": current["sample_id"], "sha256": current["sha256"]}


def validate_verifier_receipt(
    root: Path,
    receipt: dict[str, Any],
    state: dict[str, Any],
    sample_record: dict[str, Any],
) -> None:
    _require_fields(
        receipt,
        (
            "schema_version",
            "receipt_id",
            "candidate",
            "current_frontier",
            "semantic_task",
            "active_lesson_contract",
            "hard_constraints",
            "regressions",
            "improvements",
            "cleared_dimensions_after",
            "unresolved_defects",
            "strongest_blocking_defect",
            "strongest_known_generative_failure_pattern_after",
            "frontier_comparison",
            "next_search_target",
            "promotion",
            "verifier",
        ),
        "verifier receipt",
    )
    if receipt["schema_version"] != SCHEMA_VERSION:
        raise ControllerError("verifier receipt schema_version must be 1")
    _validate_id(receipt["receipt_id"], "receipt_id")
    candidate = receipt["candidate"]
    if not isinstance(candidate, dict):
        raise ControllerError("candidate must be an object")
    _require_fields(candidate, ("sample_id", "sha256"), "candidate")
    sample_id = _validate_id(candidate["sample_id"], "candidate.sample_id")
    sample_sha = _validate_sha(candidate["sha256"], "candidate.sha256")
    if sample_id != sample_record["sample_id"] or sample_sha != sample_record["candidate_sha256"]:
        raise ControllerError("verifier receipt candidate identity/hash does not match sample")
    binding = _validate_frontier_binding(receipt["current_frontier"])
    if binding != _frontier_binding(state):
        raise ControllerError("verifier receipt is bound to a stale or different current frontier")
    if receipt["semantic_task"] != state["semantic_task"]:
        raise ControllerError("verifier receipt semantic_task identity is stale or different")
    if receipt["active_lesson_contract"] != state["active_lesson_contract"]:
        raise ControllerError("verifier receipt active_lesson_contract identity is stale or different")
    _validate_authority_identity(root, receipt["semantic_task"], "receipt.semantic_task")
    _validate_authority_identity(
        root, receipt["active_lesson_contract"], "receipt.active_lesson_contract"
    )
    if receipt["hard_constraints"] not in {"PASS", "FAIL"}:
        raise ControllerError("hard_constraints must be PASS or FAIL")
    regressions = _validate_dimension_list(receipt["regressions"], "regressions")
    improvements = receipt["improvements"]
    if not isinstance(improvements, list):
        raise ControllerError("improvements must be an array")
    improvement_ids: set[str] = set()
    for index, item in enumerate(improvements):
        if not isinstance(item, dict):
            raise ControllerError(f"improvements[{index}] must be an object")
        _require_fields(item, ("dimension_id", "description"), f"improvements[{index}]")
        if not _nonblank(item["dimension_id"]) or not _nonblank(item["description"]):
            raise ControllerError(f"improvements[{index}] fields must be nonblank")
        if item["dimension_id"] in improvement_ids:
            raise ControllerError("improvements must not repeat dimension IDs")
        improvement_ids.add(item["dimension_id"])
    _validate_dimension_list(receipt["cleared_dimensions_after"], "cleared_dimensions_after")
    _validate_defects(receipt["unresolved_defects"])
    if not _nonblank(receipt["strongest_blocking_defect"]):
        raise ControllerError("strongest_blocking_defect must be nonblank")
    if not _nonblank(receipt["strongest_known_generative_failure_pattern_after"]):
        raise ControllerError(
            "strongest_known_generative_failure_pattern_after must be nonblank"
        )
    if receipt["frontier_comparison"] not in COMPARISONS:
        raise ControllerError("invalid frontier_comparison")
    _validate_search_target(receipt["next_search_target"])
    if receipt["promotion"] not in {"ALLOW", "BLOCK"}:
        raise ControllerError("promotion must be ALLOW or BLOCK")
    verifier = receipt["verifier"]
    if not isinstance(verifier, dict):
        raise ControllerError("verifier must be an object")
    _require_fields(verifier, ("identity", "context_id"), "verifier")
    if not _nonblank(verifier["identity"]) or not _nonblank(verifier["context_id"]):
        raise ControllerError("verifier identity and context_id must be nonblank")
    writer = sample_record.get("writer")
    if isinstance(writer, dict):
        writer_identity = writer.get("identity")
        writer_context = writer.get("context_id")
        same_known_context = writer_context is not None and writer_context == verifier["context_id"]
        indistinguishable_without_context = (
            writer_context is None
            and writer_identity is not None
            and writer_identity == verifier["identity"]
        )
        if same_known_context or indistinguishable_without_context:
            raise ControllerError("verifier must be distinguishable from the supplied writer context")
    if receipt["frontier_comparison"] == "DOMINATES" and state[
        "best_promoted_owner_facing_candidate"
    ] is not None and not improvements:
        raise ControllerError("DOMINATES requires at least one described improvement")
    if receipt["hard_constraints"] == "FAIL" and receipt["promotion"] != "BLOCK":
        raise ControllerError("hard_constraints FAIL requires promotion BLOCK")
    if receipt["frontier_comparison"] == "REGRESSES" and not regressions:
        raise ControllerError("REGRESSES requires at least one regression dimension")


def record_verifier_receipt(
    root: Path,
    receipt_path: Path,
    *,
    controller_dir: Path = DEFAULT_CONTROLLER_DIR,
) -> dict[str, Any]:
    root = root.resolve()
    controller = _repo_path(root, controller_dir)
    raw_receipt = _read_json(receipt_path)
    receipt_id = _validate_id(raw_receipt.get("receipt_id"), "receipt_id")
    candidate = raw_receipt.get("candidate")
    if not isinstance(candidate, dict):
        raise ControllerError("candidate must be an object")
    sample_id = _validate_id(candidate.get("sample_id"), "candidate.sample_id")
    with _controller_lock(controller):
        state = load_frontier(root, controller_dir)
        record, status, _ = _load_sample(root, controller, sample_id)
        validate_verifier_receipt(root, raw_receipt, state, record)
        canonical = _canonical_json_bytes(raw_receipt)
        receipt_sha = _sha256_bytes(canonical)
        target = controller / "adjudications" / f"{receipt_id}.json"
        created = _write_immutable(target, canonical)
        identity = {
            "receipt_id": receipt_id,
            "sha256": receipt_sha,
            "path": _relative_to_root(root, target),
        }
        existing_identity = status.get("verifier_receipt")
        if existing_identity is not None and existing_identity != identity:
            raise ControllerError("sample already has a different verifier receipt")
        del created
        history = {
            "event": "VERIFIER_RECEIPT_RECORDED",
            "receipt_id": receipt_id,
            "receipt_sha256": receipt_sha,
            "sample_id": sample_id,
            "candidate_sha256": record["candidate_sha256"],
            "frontier_comparison": raw_receipt["frontier_comparison"],
            "promotion": raw_receipt["promotion"],
            "receipt_path": identity["path"],
        }
        _append_jsonl_once(
            controller / "history" / "adjudications.jsonl",
            "receipt_id",
            receipt_id,
            history,
        )
        rejected = (
            raw_receipt["hard_constraints"] == "FAIL"
            or raw_receipt["promotion"] == "BLOCK"
            or raw_receipt["frontier_comparison"] == "REGRESSES"
        )
        new_status = "REJECTED" if rejected else "ADJUDICATED"
        if status["current_status"] == "QUARANTINED":
            _update_sample_status(root, controller, sample_id, new_status, identity)
        elif status["current_status"] != new_status and status["current_status"] not in {
            "PROMOTED",
            "RETAINED_ALT",
        }:
            raise ControllerError("sample status conflicts with verifier receipt")
    return identity


def _load_receipt(root: Path, controller: Path, receipt_id: str) -> tuple[dict[str, Any], dict[str, str]]:
    path = controller / "adjudications" / f"{receipt_id}.json"
    receipt = _read_json(path)
    canonical = _canonical_json_bytes(receipt)
    identity = {
        "receipt_id": receipt_id,
        "sha256": _sha256_bytes(canonical),
        "path": _relative_to_root(root, path),
    }
    if receipt.get("receipt_id") != receipt_id:
        raise ControllerError("receipt filename and receipt_id differ")
    if path.read_bytes() != canonical:
        raise ControllerError("stored verifier receipt is not canonical exact JSON")
    return receipt, identity


def attempt_promotion(
    root: Path,
    receipt_id: str,
    *,
    controller_dir: Path = DEFAULT_CONTROLLER_DIR,
) -> dict[str, Any]:
    root = root.resolve()
    receipt_id = _validate_id(receipt_id, "receipt_id")
    controller = _repo_path(root, controller_dir)
    state_path = controller / "frontier.json"
    with _controller_lock(controller):
        state_bytes = state_path.read_bytes()
        state = load_frontier(root, controller_dir)
        receipt, receipt_identity = _load_receipt(root, controller, receipt_id)
        sample_id = _validate_id(receipt["candidate"]["sample_id"], "candidate.sample_id")
        record, status, _ = _load_sample(root, controller, sample_id)

        current = state["best_promoted_owner_facing_candidate"]
        if (
            current is not None
            and current["sample_id"] == sample_id
            and state["last_promotion_receipt"] == receipt_identity
        ):
            transition_id = f"promotion-{receipt_id}"
            transition_path = controller / "promotions" / f"{transition_id}.json"
            transition = _read_json(transition_path)
            if transition.get("to_frontier_sha256") != _sha256_bytes(state_bytes):
                raise ControllerError("completed promotion transition does not match frontier bytes")
            _update_sample_status(root, controller, sample_id, "PROMOTED", receipt_identity)
            history = {
                "event": "FRONTIER_PROMOTED",
                "promotion_id": transition_id,
                "sample_id": sample_id,
                "candidate_sha256": record["candidate_sha256"],
                "receipt_id": receipt_id,
                "from_frontier_sha256": transition["from_frontier_sha256"],
                "to_frontier_sha256": transition["to_frontier_sha256"],
                "promotion_path": _relative_to_root(root, transition_path),
            }
            _append_jsonl_once(
                controller / "history" / "promotions.jsonl",
                "promotion_id",
                transition_id,
                history,
            )
            return state

        validate_verifier_receipt(root, receipt, state, record)
        if status["verifier_receipt"] != receipt_identity:
            raise ControllerError("sample is not bound to this verifier receipt")
        failures: list[str] = []
        if status["current_status"] not in {"ADJUDICATED", "RETAINED_ALT"}:
            failures.append("sample status is not promotion-eligible")
        if receipt["hard_constraints"] != "PASS":
            failures.append("hard_constraints must PASS")
        if receipt["promotion"] != "ALLOW":
            failures.append("verifier promotion must ALLOW")
        if current is not None and receipt["frontier_comparison"] != "DOMINATES":
            failures.append("existing frontier can only be replaced by DOMINATES")
        regressions = set(receipt["regressions"])
        cleared_before = set(state["cleared_dimensions"])
        if regressions & cleared_before:
            failures.append("a currently cleared dimension appears in regressions")
        cleared_after = set(receipt["cleared_dimensions_after"])
        if not cleared_before.issubset(cleared_after):
            failures.append("cleared_dimensions_after is not monotonic")
        if failures:
            if state_path.read_bytes() != state_bytes:
                raise ControllerError("frontier changed during failed promotion")
            raise ControllerError("promotion blocked: " + "; ".join(failures))

        candidate_identity = {
            "sample_id": sample_id,
            "sha256": record["candidate_sha256"],
            "candidate_path": record["candidate_path"],
        }
        updated = copy.deepcopy(state)
        updated["best_promoted_owner_facing_candidate"] = candidate_identity
        updated["semantic_provenance_hard_constraint_status"] = "PASS"
        updated["cleared_dimensions"] = receipt["cleared_dimensions_after"]
        updated["unresolved_defects"] = receipt["unresolved_defects"]
        updated["strongest_known_generative_failure_pattern"] = receipt[
            "strongest_known_generative_failure_pattern_after"
        ]
        updated["next_search_target"] = receipt["next_search_target"]
        updated["last_promotion_receipt"] = receipt_identity
        updated["revision"] = state["revision"] + 1
        validate_frontier(root, updated)
        updated_bytes = _canonical_json_bytes(updated)
        transition_id = f"promotion-{receipt_id}"
        transition = {
            "schema_version": SCHEMA_VERSION,
            "promotion_id": transition_id,
            "from_frontier_sha256": _sha256_bytes(state_bytes),
            "to_frontier_sha256": _sha256_bytes(updated_bytes),
            "sample_id": sample_id,
            "candidate_sha256": record["candidate_sha256"],
            "verifier_receipt": receipt_identity,
            "result": "PROMOTED",
        }
        transition_path = controller / "promotions" / f"{transition_id}.json"
        _write_immutable(transition_path, _canonical_json_bytes(transition))
        _atomic_write(state_path, updated_bytes)
        _update_sample_status(root, controller, sample_id, "PROMOTED", receipt_identity)
        history = {
            "event": "FRONTIER_PROMOTED",
            "promotion_id": transition_id,
            "sample_id": sample_id,
            "candidate_sha256": record["candidate_sha256"],
            "receipt_id": receipt_id,
            "from_frontier_sha256": transition["from_frontier_sha256"],
            "to_frontier_sha256": transition["to_frontier_sha256"],
            "promotion_path": _relative_to_root(root, transition_path),
        }
        _append_jsonl_once(
            controller / "history" / "promotions.jsonl",
            "promotion_id",
            transition_id,
            history,
        )
    return updated


def validate_search_decision(
    root: Path, decision: dict[str, Any], state: dict[str, Any]
) -> None:
    _require_fields(
        decision,
        (
            "schema_version",
            "decision_id",
            "current_frontier",
            "semantic_task",
            "active_lesson_contract",
            "cleared_dimensions",
            "unresolved_defects",
            "strongest_known_generative_failure_pattern",
            "next_search_target",
            "decision_maker",
        ),
        "search decision",
    )
    if decision["schema_version"] != SCHEMA_VERSION:
        raise ControllerError("search decision schema_version must be 1")
    _validate_id(decision["decision_id"], "decision_id")
    if _validate_frontier_binding(decision["current_frontier"]) != _frontier_binding(state):
        raise ControllerError("search decision is bound to a stale or different frontier")
    if decision["semantic_task"] != state["semantic_task"]:
        raise ControllerError("search decision semantic_task identity differs")
    if decision["active_lesson_contract"] != state["active_lesson_contract"]:
        raise ControllerError("search decision lesson-contract identity differs")
    _validate_authority_identity(root, decision["semantic_task"], "decision.semantic_task")
    _validate_authority_identity(
        root, decision["active_lesson_contract"], "decision.active_lesson_contract"
    )
    cleared = set(_validate_dimension_list(decision["cleared_dimensions"], "cleared_dimensions"))
    if not set(state["cleared_dimensions"]).issubset(cleared):
        raise ControllerError("search decision may not silently remove a cleared dimension")
    _validate_defects(decision["unresolved_defects"])
    if not _nonblank(decision["strongest_known_generative_failure_pattern"]):
        raise ControllerError("strongest_known_generative_failure_pattern must be nonblank")
    _validate_search_target(decision["next_search_target"])
    maker = decision["decision_maker"]
    if not isinstance(maker, dict):
        raise ControllerError("decision_maker must be an object")
    _require_fields(maker, ("identity", "context_id"), "decision_maker")
    if not _nonblank(maker["identity"]) or not _nonblank(maker["context_id"]):
        raise ControllerError("decision_maker identity/context_id must be nonblank")
    source_receipt = decision.get("source_verifier_receipt")
    if source_receipt is not None:
        if not isinstance(source_receipt, dict):
            raise ControllerError("source_verifier_receipt must be an object or null")
        _require_fields(source_receipt, ("receipt_id", "sha256"), "source_verifier_receipt")
        _validate_id(source_receipt["receipt_id"], "source_verifier_receipt.receipt_id")
        _validate_sha(source_receipt["sha256"], "source_verifier_receipt.sha256")


def apply_search_decision(
    root: Path,
    decision_path: Path,
    *,
    controller_dir: Path = DEFAULT_CONTROLLER_DIR,
) -> dict[str, Any]:
    root = root.resolve()
    controller = _repo_path(root, controller_dir)
    state_path = controller / "frontier.json"
    decision = _read_json(decision_path)
    decision_id = _validate_id(decision.get("decision_id"), "decision_id")
    with _controller_lock(controller):
        state_bytes = state_path.read_bytes()
        state = load_frontier(root, controller_dir)
        validate_search_decision(root, decision, state)
        source = decision.get("source_verifier_receipt")
        if source is not None:
            receipt, identity = _load_receipt(root, controller, source["receipt_id"])
            del receipt
            if source != {"receipt_id": identity["receipt_id"], "sha256": identity["sha256"]}:
                raise ControllerError("source_verifier_receipt identity/hash mismatch")
        canonical = _canonical_json_bytes(decision)
        target = controller / "decisions" / f"{decision_id}.json"
        transition_path = controller / "decisions" / f"{decision_id}.transition.json"
        current_state_sha = _sha256_bytes(state_bytes)

        if transition_path.exists():
            _write_immutable(target, canonical)
            transition = _read_json(transition_path)
            if transition.get("decision_sha256") != _sha256_bytes(canonical):
                raise ControllerError("search-decision transition is bound to different bytes")
            if current_state_sha == transition.get("to_frontier_sha256"):
                history = {
                    "event": "SEARCH_DECISION_APPLIED",
                    "decision_id": decision_id,
                    "decision_sha256": transition["decision_sha256"],
                    "decision_path": _relative_to_root(root, target),
                    "source_verifier_receipt": source,
                }
                _append_jsonl_once(
                    controller / "history" / "controller-decisions.jsonl",
                    "decision_id",
                    decision_id,
                    history,
                )
                return state
            if current_state_sha != transition.get("from_frontier_sha256"):
                raise ControllerError("search-decision replay is stale or conflicts with current state")

        updated = copy.deepcopy(state)
        updated["cleared_dimensions"] = decision["cleared_dimensions"]
        updated["unresolved_defects"] = decision["unresolved_defects"]
        updated["strongest_known_generative_failure_pattern"] = decision[
            "strongest_known_generative_failure_pattern"
        ]
        updated["next_search_target"] = decision["next_search_target"]
        updated["revision"] = state["revision"] + 1
        validate_frontier(root, updated)
        updated_bytes = _canonical_json_bytes(updated)
        transition = {
            "schema_version": SCHEMA_VERSION,
            "decision_id": decision_id,
            "decision_sha256": _sha256_bytes(canonical),
            "from_frontier_sha256": current_state_sha,
            "to_frontier_sha256": _sha256_bytes(updated_bytes),
        }
        _write_immutable(target, canonical)
        _write_immutable(transition_path, _canonical_json_bytes(transition))
        _atomic_write(state_path, updated_bytes)
        history = {
            "event": "SEARCH_DECISION_APPLIED",
            "decision_id": decision_id,
            "decision_sha256": transition["decision_sha256"],
            "decision_path": _relative_to_root(root, target),
            "source_verifier_receipt": source,
        }
        _append_jsonl_once(
            controller / "history" / "controller-decisions.jsonl",
            "decision_id",
            decision_id,
            history,
        )
    return updated


SOURCE_INTEGRITY_PROHIBITIONS = [
    "Do not include rejected candidate prose or prior verifier rationales.",
    "Do not use unrelated Joel prose, Pangram-Human donor text, or external human prose.",
    "Do not invent autobiography, chronology, symptoms, evidence, mechanisms, examples, authorities, quotations, terminology, certainty, or fake human texture.",
    "Do not treat a raw generation, recency, filename, detector result, or model confidence as promotion authority.",
]


def build_writer_packet(
    root: Path, controller_dir: Path = DEFAULT_CONTROLLER_DIR
) -> dict[str, Any]:
    root = root.resolve()
    state = load_frontier(root, controller_dir)
    target = _validate_search_target(state["next_search_target"], allow_review=True)
    if target["kind"] != "GENERATION":
        raise ControllerError(
            "writer packet blocked: reasoning Chat must review the controller and supply a GENERATION search target"
        )
    semantic_path = _repo_path(root, state["semantic_task"]["path"])
    current = state["best_promoted_owner_facing_candidate"]
    return {
        "schema_version": SCHEMA_VERSION,
        "packet_type": "SOMATIC_INTRO_WRITER",
        "article_id": state["article_id"],
        "scope": state["scope"],
        "semantic_authority": {
            **state["semantic_task"],
            "content": semantic_path.read_text(encoding="utf-8"),
        },
        "externally_preserved_frontier": None
        if current is None
        else {"sample_id": current["sample_id"], "sha256": current["sha256"]},
        "cleared_dimensions_as_constraints": state["cleared_dimensions"],
        "unresolved_defects": state["unresolved_defects"],
        "strongest_known_generative_failure_pattern": state[
            "strongest_known_generative_failure_pattern"
        ],
        "next_search_target": target,
        "source_integrity_prohibitions": SOURCE_INTEGRITY_PROHIBITIONS,
        "candidate_prose_policy": "NO_PRIOR_CANDIDATE_PROSE_INCLUDED",
    }


def _receipt_schema_template(state: dict[str, Any], sample: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "receipt_id": "<unique-receipt-id>",
        "candidate": {
            "sample_id": sample["sample_id"],
            "sha256": sample["candidate_sha256"],
        },
        "current_frontier": _frontier_binding(state),
        "semantic_task": state["semantic_task"],
        "active_lesson_contract": state["active_lesson_contract"],
        "hard_constraints": "PASS|FAIL",
        "regressions": ["<dimension-id>"],
        "improvements": [
            {"dimension_id": "<dimension-id>", "description": "<comparative judgment>"}
        ],
        "cleared_dimensions_after": ["<dimension-id>"],
        "unresolved_defects": [
            {"rank": 1, "dimension_id": "<dimension-id>", "description": "<defect>"}
        ],
        "strongest_blocking_defect": "<one concrete diagnosis or explicit none>",
        "strongest_known_generative_failure_pattern_after": "<externally judged pattern>",
        "frontier_comparison": "DOMINATES|NONDOMINATED|REGRESSES|INCOMPARABLE",
        "next_search_target": {
            "id": "<target-id>",
            "kind": "GENERATION",
            "description": "<one bounded changed search operation>",
        },
        "promotion": "ALLOW|BLOCK",
        "verifier": {"identity": "<verifier-id>", "context_id": "<verifier-context-id>"},
    }


def build_verifier_packet(
    root: Path,
    sample_id: str,
    controller_dir: Path = DEFAULT_CONTROLLER_DIR,
) -> dict[str, Any]:
    root = root.resolve()
    sample_id = _validate_id(sample_id, "sample_id")
    controller = _repo_path(root, controller_dir)
    state = load_frontier(root, controller_dir)
    sample, _, content = _load_sample(root, controller, sample_id)
    semantic_path = _repo_path(root, state["semantic_task"]["path"])
    lesson_path = _repo_path(root, state["active_lesson_contract"]["path"])
    current = state["best_promoted_owner_facing_candidate"]
    current_packet: dict[str, Any] | None = None
    if current is not None:
        current_record, _, current_content = _load_sample(root, controller, current["sample_id"])
        if current_record["candidate_sha256"] != current["sha256"]:
            raise ControllerError("current promoted frontier sample identity/hash mismatch")
        current_packet = {
            "sample_id": current["sample_id"],
            "sha256": current["sha256"],
            "content": current_content.decode("utf-8"),
        }
    try:
        candidate_text = content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ControllerError("candidate sample must be UTF-8 for verifier packet") from exc
    return {
        "schema_version": SCHEMA_VERSION,
        "packet_type": "SOMATIC_INTRO_COMPARATIVE_VERIFIER",
        "article_id": state["article_id"],
        "scope": state["scope"],
        "candidate": {
            "sample_id": sample_id,
            "sha256": sample["candidate_sha256"],
            "content": candidate_text,
        },
        "current_promoted_frontier": current_packet,
        "semantic_authority": {
            **state["semantic_task"],
            "content": semantic_path.read_text(encoding="utf-8"),
        },
        "active_lesson_contract": {
            **state["active_lesson_contract"],
            "content": lesson_path.read_text(encoding="utf-8"),
        },
        "required_receipt": _receipt_schema_template(state, sample),
        "verifier_role_boundary": (
            "Supply comparative semantic judgments. The Codex controller only validates and stores them."
        ),
    }


def emit_owner_facing_candidate(
    root: Path, controller_dir: Path = DEFAULT_CONTROLLER_DIR
) -> bytes:
    root = root.resolve()
    controller = _repo_path(root, controller_dir)
    state = load_frontier(root, controller_dir)
    current = state["best_promoted_owner_facing_candidate"]
    if current is None:
        raise ControllerError("no verified promoted owner-facing frontier exists")
    record, status, content = _load_sample(root, controller, current["sample_id"])
    if record["candidate_sha256"] != current["sha256"] or status["current_status"] != "PROMOTED":
        raise ControllerError("promoted frontier/sample status binding is invalid")
    if state["semantic_provenance_hard_constraint_status"] != "PASS":
        raise ControllerError("promoted frontier hard-constraint state is not PASS")
    return content


def _write_or_print_json(value: dict[str, Any], output: Path | None) -> None:
    content = _canonical_json_bytes(value)
    if output is None:
        sys.stdout.buffer.write(content)
    else:
        _atomic_write(output, content)


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--controller-dir", type=Path, default=DEFAULT_CONTROLLER_DIR)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("init", help="Initialize/read the fail-closed frontier state.")

    register = subparsers.add_parser("register-sample", help="Quarantine an immutable raw sample.")
    register.add_argument("--sample-id", required=True)
    register.add_argument("--candidate", type=Path, required=True)
    register.add_argument("--created-at", required=True)
    register.add_argument("--writer-identity")
    register.add_argument("--writer-context")

    writer = subparsers.add_parser("emit-writer-packet")
    writer.add_argument("--output", type=Path)

    verifier = subparsers.add_parser("emit-verifier-packet")
    verifier.add_argument("--sample-id", required=True)
    verifier.add_argument("--output", type=Path)

    record = subparsers.add_parser("record-verifier-receipt")
    record.add_argument("--receipt", type=Path, required=True)

    promote = subparsers.add_parser("attempt-promotion")
    promote.add_argument("--receipt-id", required=True)

    decision = subparsers.add_parser(
        "apply-search-decision",
        help="Apply a hash-bound reasoning-Chat search-state decision without changing the candidate frontier.",
    )
    decision.add_argument("--decision", type=Path, required=True)

    subparsers.add_parser("show", help="Show the current frontier state without candidate prose.")

    owner = subparsers.add_parser(
        "emit-owner-facing-candidate",
        help="Emit only the exact currently promoted candidate; fail when none exists.",
    )
    owner.add_argument("--output", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "init":
            result = initialize_controller(root, args.controller_dir)
            _write_or_print_json(result, None)
        elif args.command == "register-sample":
            result = register_sample(
                root,
                args.candidate,
                args.sample_id,
                controller_dir=args.controller_dir,
                writer_identity=args.writer_identity,
                writer_context=args.writer_context,
                created_at=args.created_at,
            )
            _write_or_print_json(result, None)
        elif args.command == "emit-writer-packet":
            _write_or_print_json(build_writer_packet(root, args.controller_dir), args.output)
        elif args.command == "emit-verifier-packet":
            _write_or_print_json(
                build_verifier_packet(root, args.sample_id, args.controller_dir), args.output
            )
        elif args.command == "record-verifier-receipt":
            _write_or_print_json(
                record_verifier_receipt(
                    root, args.receipt, controller_dir=args.controller_dir
                ),
                None,
            )
        elif args.command == "attempt-promotion":
            _write_or_print_json(
                attempt_promotion(
                    root, args.receipt_id, controller_dir=args.controller_dir
                ),
                None,
            )
        elif args.command == "apply-search-decision":
            _write_or_print_json(
                apply_search_decision(root, args.decision, controller_dir=args.controller_dir),
                None,
            )
        elif args.command == "show":
            _write_or_print_json(load_frontier(root, args.controller_dir), None)
        elif args.command == "emit-owner-facing-candidate":
            content = emit_owner_facing_candidate(root, args.controller_dir)
            if args.output is None:
                sys.stdout.buffer.write(content)
            else:
                _atomic_write(args.output, content)
        else:  # pragma: no cover - argparse makes this unreachable.
            raise ControllerError(f"unknown command: {args.command}")
    except (ControllerError, FileNotFoundError, OSError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
