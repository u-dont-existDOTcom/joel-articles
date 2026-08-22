#!/usr/bin/env python3
"""Validate a humanization preservation-proof receipt.

This validator checks that the *recorded* preservation proof is complete and
fail-closed. It does not decide semantic equivalence or discover missing source
obligations automatically; those remain editorial judgments performed before
this structural gate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
UNIT_ID_RE = re.compile(r"^[A-Z][A-Z0-9-]*$")
CHANGE_ID_RE = re.compile(r"^[A-Z][A-Z0-9-]*$")
DELTA_ID_RE = re.compile(r"^[A-Z][A-Z0-9-]*$")

UNIT_TYPES = {
    "claim",
    "certainty",
    "attribution",
    "agency",
    "chronology",
    "causality",
    "memory",
    "quotation",
    "example",
    "judgment",
    "function",
    "object",
    "context",
    "recurrence",
}
UNIT_STATUSES = {
    "preserved",
    "moved",
    "owner-superseded",
    "owner-deleted",
    "consolidated",
}
DISPOSITION_EXACT = {
    "must-remain-here",
    "may-reword-semantically",
    "must-remain-exact",
}
DISPOSITION_PREFIXES = {
    "may-move:",
    "owner-superseded:",
    "owner-deleted:",
    "duplicate-function-consolidation:",
}
FORBIDDEN_DISPOSITION_WORDS = {
    "omit",
    "inferable",
    "redundant",
    "smoother",
    "not needed",
    "better for pangram",
}
DELTA_CLASSIFICATIONS = {
    "added-proposition",
    "deleted-proposition",
    "certainty-scope-change",
    "attribution-provenance-change",
    "agency-change",
    "chronology-causality-change",
    "movement",
    "consolidation",
    "new-explanation",
    "bridge-metaphor-moral",
    "recurrence-placement-change",
    "link-media-object-change",
    "authorized-rewording",
    "other-substantive-change",
}


def _finding(code: str, message: str) -> dict[str, str]:
    return {"code": code, "message": message}


def _nonblank(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_disposition(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    normalized = value.strip().lower()
    if normalized in FORBIDDEN_DISPOSITION_WORDS:
        return False
    if value in DISPOSITION_EXACT:
        return True
    return any(value.startswith(prefix) and value[len(prefix) :].strip() for prefix in DISPOSITION_PREFIXES)


def validate_proof(data: object) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(data, dict):
        return [_finding("proof.invalid-root", "Preservation proof root must be a JSON object.")]

    if data.get("schema_version") != 1:
        findings.append(_finding("proof.schema", "schema_version must be 1."))

    source = data.get("source")
    if not isinstance(source, dict):
        findings.append(_finding("proof.source", "source must be an object."))
    else:
        if not _nonblank(source.get("path")):
            findings.append(_finding("proof.source.path", "source.path must be nonblank."))
        if not isinstance(source.get("sha256"), str) or not SHA256_RE.fullmatch(source["sha256"]):
            findings.append(_finding("proof.source.sha256", "source.sha256 must be lowercase SHA-256."))
        if not _nonblank(source.get("revision")):
            findings.append(_finding("proof.source.revision", "source.revision must be nonblank."))

    for field in ("changed_scope", "mode", "edit_dose"):
        if not _nonblank(data.get(field)):
            findings.append(_finding(f"proof.{field}", f"{field} must be nonblank."))

    units = data.get("preservation_units")
    if not isinstance(units, list) or not units:
        findings.append(_finding("proof.units", "preservation_units must be a non-empty array."))
        units = []

    seen_units: set[str] = set()
    for index, unit in enumerate(units):
        prefix = f"preservation_units[{index}]"
        if not isinstance(unit, dict):
            findings.append(_finding("proof.unit.invalid", f"{prefix} must be an object."))
            continue
        unit_id = unit.get("unit_id")
        if not isinstance(unit_id, str) or not UNIT_ID_RE.fullmatch(unit_id) or unit_id in seen_units:
            findings.append(_finding("proof.unit.id", f"{prefix}.unit_id must be unique uppercase/kebab-style ID."))
        else:
            seen_units.add(unit_id)
        if not _nonblank(unit.get("source_ref")):
            findings.append(_finding("proof.unit.source", f"{prefix}.source_ref must be nonblank."))
        if not _nonblank(unit.get("authority")):
            findings.append(_finding("proof.unit.authority", f"{prefix}.authority must be nonblank."))
        if unit.get("type") not in UNIT_TYPES:
            findings.append(_finding("proof.unit.type", f"{prefix}.type is unsupported."))
        if not _nonblank(unit.get("meaning")):
            findings.append(_finding("proof.unit.meaning", f"{prefix}.meaning must be nonblank."))
        if not _valid_disposition(unit.get("allowed_disposition")):
            findings.append(_finding("proof.unit.disposition", f"{prefix}.allowed_disposition is missing or forbidden."))

        status = unit.get("status")
        if status not in UNIT_STATUSES:
            findings.append(_finding("proof.unit.status", f"{prefix}.status must be a terminal preservation status."))
            continue

        candidate_mapping = unit.get("candidate_mapping")
        authority_ref = unit.get("authority_ref")
        if status in {"preserved", "moved", "consolidated"} and not _nonblank(candidate_mapping):
            findings.append(_finding("proof.unit.mapping", f"{prefix} status {status!r} requires candidate_mapping."))
        if status in {"owner-superseded", "owner-deleted"} and not _nonblank(authority_ref):
            findings.append(_finding("proof.unit.owner-authority", f"{prefix} status {status!r} requires authority_ref."))

    whitelist = data.get("change_whitelist")
    if not isinstance(whitelist, list):
        findings.append(_finding("proof.whitelist", "change_whitelist must be an array."))
        whitelist = []
    seen_changes: set[str] = set()
    for index, change in enumerate(whitelist):
        prefix = f"change_whitelist[{index}]"
        if not isinstance(change, dict):
            findings.append(_finding("proof.change.invalid", f"{prefix} must be an object."))
            continue
        change_id = change.get("change_id")
        if not isinstance(change_id, str) or not CHANGE_ID_RE.fullmatch(change_id) or change_id in seen_changes:
            findings.append(_finding("proof.change.id", f"{prefix}.change_id must be unique uppercase/kebab-style ID."))
        else:
            seen_changes.add(change_id)
        if not _nonblank(change.get("description")):
            findings.append(_finding("proof.change.description", f"{prefix}.description must be nonblank."))

    deltas = data.get("candidate_deltas")
    if not isinstance(deltas, list):
        findings.append(_finding("proof.deltas", "candidate_deltas must be an array."))
        deltas = []
    seen_deltas: set[str] = set()
    for index, delta in enumerate(deltas):
        prefix = f"candidate_deltas[{index}]"
        if not isinstance(delta, dict):
            findings.append(_finding("proof.delta.invalid", f"{prefix} must be an object."))
            continue
        delta_id = delta.get("delta_id")
        if not isinstance(delta_id, str) or not DELTA_ID_RE.fullmatch(delta_id) or delta_id in seen_deltas:
            findings.append(_finding("proof.delta.id", f"{prefix}.delta_id must be unique uppercase/kebab-style ID."))
        else:
            seen_deltas.add(delta_id)
        if delta.get("classification") not in DELTA_CLASSIFICATIONS:
            findings.append(_finding("proof.delta.classification", f"{prefix}.classification is unsupported."))
        if not _nonblank(delta.get("description")):
            findings.append(_finding("proof.delta.description", f"{prefix}.description must be nonblank."))
        authority_ref = delta.get("authority_ref")
        if not _nonblank(authority_ref):
            findings.append(_finding("proof.delta.authority", f"{prefix}.authority_ref must be nonblank."))
        elif isinstance(authority_ref, str) and authority_ref.startswith("CH-") and authority_ref not in seen_changes:
            findings.append(_finding("proof.delta.unknown-change", f"{prefix}.authority_ref {authority_ref!r} is not in change_whitelist."))
        if delta.get("status") != "authorized":
            findings.append(_finding("proof.delta.status", f"{prefix}.status must be 'authorized'."))

    unexplained = data.get("unexplained_deltas")
    if not isinstance(unexplained, list):
        findings.append(_finding("proof.unexplained", "unexplained_deltas must be an array."))
    elif unexplained:
        findings.append(_finding("proof.unexplained.nonzero", "unexplained_deltas must be empty before detector eligibility."))

    if data.get("forward_traceability") != "pass":
        findings.append(_finding("proof.forward", "forward_traceability must be 'pass'."))
    if data.get("reverse_traceability") != "pass":
        findings.append(_finding("proof.reverse", "reverse_traceability must be 'pass'."))
    if data.get("owner_provenance_separation") != "pass":
        findings.append(_finding("proof.provenance", "owner_provenance_separation must be 'pass'."))
    if data.get("architecture_dependency_gate") != "pass":
        findings.append(_finding("proof.architecture", "architecture_dependency_gate must be 'pass'."))
    if data.get("detector_eligibility") != "eligible":
        findings.append(_finding("proof.detector-eligibility", "detector_eligibility must be 'eligible'."))

    return findings


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("proof", type=Path, help="Path to preservation-proof JSON receipt")
    args = parser.parse_args(argv)
    try:
        data = _load(args.proof)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"FAIL: could not read preservation proof: {exc}", file=sys.stderr)
        return 2

    findings = validate_proof(data)
    if findings:
        print(json.dumps({"status": "FAIL", "findings": findings}, indent=2, ensure_ascii=False))
        return 1
    print(json.dumps({"status": "PASS", "findings": []}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
