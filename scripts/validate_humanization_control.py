#!/usr/bin/env python3
"""Validate a fail-closed humanization control record.

The validator proves artifact identity, role/input separation, recorded gate
completion, and detector ordering. It does not write prose or make semantic,
editorial, attribution, or structural-novelty judgments; those belong to the
separate Chat roles recorded by the control.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9-]*$")
ALLOWED_STATES = {"prewrite_ready", "candidate_validated", "detector_recorded"}
ALLOWED_PROVENANCE = {"OWNER_LOCK", "AI_TARGET", "UNKNOWN"}
GATE_NAMES = {
    "provenance_lock",
    "semantic_only_writer_input",
    "rejected_strategy_isolation",
    "preservation",
    "attribution",
    "structural_recurrence",
    "separate_adversarial_validation",
}
PREWRITE_PASS = {
    "provenance_lock",
    "semantic_only_writer_input",
    "rejected_strategy_isolation",
}
MANDATORY_STRUCTURAL_CHECKS = {
    "conceptual_card_count_and_order",
    "balanced_alternatives",
    "triads",
    "setup_qualification_summary",
    "significance_staging",
    "explanatory_aftercare",
    "mirrored_clauses",
    "generic_transitions",
}
MANDATORY_INVALID_JUSTIFICATIONS = {
    "sounds more conversational",
    "uses contractions",
    "simpler wording",
    "more first-person",
    "better flow",
    "shorter sentences",
    "more human",
}
BANNED_WRITER_KEYS = {
    "source_text",
    "source_prose",
    "original_text",
    "original_prose",
    "candidate_text",
    "rejected_candidate",
    "rejected_candidates",
    "rejected_strategy",
    "rejected_strategies",
    "rejected_strategy_ledger",
}
ATTRIBUTION_FALSE_FIELDS = {
    "general_claim_became_autobiography",
    "observation_became_interpretation",
    "certainty_shifted",
    "owner_language_counted_as_new_repair",
}


def _finding(code: str, message: str) -> dict[str, str]:
    return {"code": code, "message": message}


def _nonblank(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _resolve(root: Path, value: object) -> Path | None:
    if not _nonblank(value):
        return None
    raw = Path(str(value))
    if raw.is_absolute() or ".." in raw.parts:
        return None
    candidate = (root / raw).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def _load_bound_json(
    root: Path,
    record: object,
    prefix: str,
    findings: list[dict[str, str]],
) -> tuple[Path | None, object | None]:
    if not isinstance(record, dict):
        findings.append(_finding(f"{prefix}.record", f"{prefix} must be an object."))
        return None, None
    path = _resolve(root, record.get("path"))
    expected = record.get("sha256")
    if path is None:
        findings.append(_finding(f"{prefix}.path", f"{prefix}.path must be a safe relative path."))
        return None, None
    if not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
        findings.append(_finding(f"{prefix}.sha256", f"{prefix}.sha256 must be lowercase SHA-256."))
        return path, None
    try:
        payload = path.read_bytes()
    except OSError as exc:
        findings.append(_finding(f"{prefix}.read", f"Could not read {path}: {exc}"))
        return path, None
    if _sha256(payload) != expected:
        findings.append(_finding(f"{prefix}.hash", f"{prefix} hash does not match its bound artifact."))
        return path, None
    try:
        return path, json.loads(payload)
    except (UnicodeError, json.JSONDecodeError) as exc:
        findings.append(_finding(f"{prefix}.json", f"{prefix} must be valid UTF-8 JSON: {exc}"))
        return path, None


def _walk(value: object, trail: tuple[str, ...] = ()) -> Iterable[tuple[tuple[str, ...], object]]:
    yield trail, value
    if isinstance(value, dict):
        for key, item in value.items():
            yield from _walk(item, (*trail, str(key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk(item, (*trail, str(index)))


def _tokens(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", value.lower())


def _ngrams(tokens: list[str], width: int = 8) -> set[tuple[str, ...]]:
    if len(tokens) < width:
        return set()
    return {tuple(tokens[index : index + width]) for index in range(len(tokens) - width + 1)}


def _validate_source_and_provenance(
    data: dict[str, Any], root: Path, findings: list[dict[str, str]]
) -> tuple[bytes, set[str]]:
    source = data.get("source")
    if not isinstance(source, dict):
        findings.append(_finding("control.source", "source must be an object."))
        return b"", set()
    source_path = _resolve(root, source.get("path"))
    if source_path is None:
        findings.append(_finding("control.source.path", "source.path must be a safe relative path."))
        return b"", set()
    try:
        source_bytes = source_path.read_bytes()
    except OSError as exc:
        findings.append(_finding("control.source.read", f"Could not read source: {exc}"))
        return b"", set()
    expected_hash = source.get("sha256")
    if not isinstance(expected_hash, str) or not SHA256_RE.fullmatch(expected_hash):
        findings.append(_finding("control.source.sha256", "source.sha256 must be lowercase SHA-256."))
    elif _sha256(source_bytes) != expected_hash:
        findings.append(_finding("control.source.hash", "Source hash does not match the frozen artifact."))
    if not _nonblank(source.get("revision")) or not _nonblank(source.get("changed_scope")):
        findings.append(_finding("control.source.identity", "source revision and changed_scope must be nonblank."))

    lines = source_bytes.splitlines(keepends=True)
    if source.get("line_count") != len(lines):
        findings.append(_finding("control.source.lines", "source.line_count does not match the artifact."))

    spans = data.get("provenance_spans")
    if not isinstance(spans, list) or not spans:
        findings.append(_finding("control.provenance", "provenance_spans must be a non-empty array."))
        return source_bytes, set()
    next_line = 1
    seen: set[str] = set()
    ai_ids: set[str] = set()
    for index, span in enumerate(spans):
        prefix = f"provenance_spans[{index}]"
        if not isinstance(span, dict):
            findings.append(_finding("control.provenance.span", f"{prefix} must be an object."))
            continue
        span_id = span.get("span_id")
        if not isinstance(span_id, str) or not ID_RE.fullmatch(span_id) or span_id in seen:
            findings.append(_finding("control.provenance.id", f"{prefix}.span_id must be a unique ID."))
        else:
            seen.add(span_id)
        classification = span.get("classification")
        if classification not in ALLOWED_PROVENANCE:
            findings.append(_finding("control.provenance.classification", f"{prefix} has an unsupported classification."))
        start, end = span.get("line_start"), span.get("line_end")
        if not isinstance(start, int) or not isinstance(end, int) or start != next_line or end < start or end > len(lines):
            findings.append(_finding("control.provenance.coverage", f"{prefix} does not continue exact, ordered source coverage."))
        else:
            actual = _sha256(b"".join(lines[start - 1 : end]))
            if span.get("sha256") != actual:
                findings.append(_finding("control.provenance.hash", f"{prefix} hash does not match its exact source lines."))
            next_line = end + 1
        if classification in {"OWNER_LOCK", "UNKNOWN"}:
            if span.get("frozen") is not True or span.get("writer_access") != "none":
                findings.append(_finding("control.provenance.freeze", f"{prefix} must be frozen and withheld from the writer."))
        if classification == "AI_TARGET":
            if span.get("frozen") is not False or span.get("writer_access") != "semantics-only":
                findings.append(_finding("control.provenance.target", f"{prefix} must expose semantics only and remain the sole mutable class."))
            if isinstance(span_id, str):
                ai_ids.add(span_id)
        if not _nonblank(span.get("authority_note")):
            findings.append(_finding("control.provenance.authority", f"{prefix}.authority_note must be nonblank."))
    if next_line != len(lines) + 1:
        findings.append(_finding("control.provenance.coverage", "Provenance spans must cover every source line exactly once."))
    if not ai_ids:
        findings.append(_finding("control.provenance.no-target", "At least one AI_TARGET span is required."))
    return source_bytes, ai_ids


def _validate_writer_packet(
    packet: object,
    ai_ids: set[str],
    source_bytes: bytes,
    data: dict[str, Any],
    findings: list[dict[str, str]],
) -> None:
    if not isinstance(packet, dict):
        findings.append(_finding("writer.invalid", "Writer packet must be a JSON object."))
        return
    if packet.get("schema_version") != 1:
        findings.append(_finding("writer.schema", "Writer packet schema_version must be 1."))
    if packet.get("writer_role") != "chat_reasoning" or packet.get("executor_role") != "mechanical_only":
        findings.append(_finding("writer.roles", "Writer packet must assign reasoning to Chat and mechanical execution to Codex."))
    if set(packet.get("target_span_ids", [])) != ai_ids:
        findings.append(_finding("writer.targets", "Writer packet target_span_ids must equal the AI_TARGET provenance spans."))
    units = packet.get("semantic_units")
    if not isinstance(units, list) or not units:
        findings.append(_finding("writer.units", "Writer packet must contain semantic_units."))
        units = []
    seen: set[str] = set()
    for index, unit in enumerate(units):
        prefix = f"semantic_units[{index}]"
        if not isinstance(unit, dict):
            findings.append(_finding("writer.unit", f"{prefix} must be an object."))
            continue
        unit_id = unit.get("unit_id")
        if not isinstance(unit_id, str) or not ID_RE.fullmatch(unit_id) or unit_id in seen:
            findings.append(_finding("writer.unit.id", f"{prefix}.unit_id must be unique."))
        else:
            seen.add(unit_id)
        for field in ("proposition", "function", "provenance_plane", "certainty", "attribution_constraint"):
            if not _nonblank(unit.get(field)):
                findings.append(_finding(f"writer.unit.{field}", f"{prefix}.{field} must be nonblank."))
    if not isinstance(packet.get("hard_constraints"), list) or not packet["hard_constraints"]:
        findings.append(_finding("writer.constraints", "Writer packet must contain hard_constraints."))

    span_by_id = {
        span.get("span_id"): span
        for span in data.get("provenance_spans", [])
        if isinstance(span, dict) and isinstance(span.get("span_id"), str)
    }
    source_lines = source_bytes.splitlines(keepends=True)
    authorized_exact = packet.get("authorized_exact_owner_language")
    if not isinstance(authorized_exact, list):
        findings.append(_finding("writer.owner-language", "authorized_exact_owner_language must be an array."))
        authorized_exact = []
    for index, record in enumerate(authorized_exact):
        prefix = f"authorized_exact_owner_language[{index}]"
        if not isinstance(record, dict) or not _nonblank(record.get("text")):
            findings.append(_finding("writer.owner-language.record", f"{prefix} must contain exact text."))
            continue
        text_bytes = record["text"].encode("utf-8")
        if record.get("sha256") != _sha256(text_bytes):
            findings.append(_finding("writer.owner-language.hash", f"{prefix}.sha256 must bind the exact text."))
        span = span_by_id.get(record.get("source_span_id"))
        if not isinstance(span, dict) or span.get("classification") != "OWNER_LOCK":
            findings.append(_finding("writer.owner-language.source", f"{prefix} must reference an OWNER_LOCK span."))
        else:
            span_bytes = b"".join(source_lines[span["line_start"] - 1 : span["line_end"]])
            if text_bytes not in span_bytes:
                findings.append(_finding("writer.owner-language.membership", f"{prefix} text is not present byte-for-byte in its OWNER_LOCK span."))

    for trail, value in _walk(packet):
        if trail and trail[-1].lower() in BANNED_WRITER_KEYS:
            findings.append(_finding("writer.forbidden-key", f"Writer packet contains forbidden field {'.'.join(trail)}."))

    target_text = ""
    for span in data.get("provenance_spans", []):
        if isinstance(span, dict) and span.get("classification") == "AI_TARGET":
            target_text += b"".join(source_lines[span["line_start"] - 1 : span["line_end"]]).decode("utf-8", errors="ignore")
    target_ngrams = _ngrams(_tokens(target_text))
    exact_owner_paths = {("authorized_exact_owner_language", str(index), "text") for index, _ in enumerate(packet.get("authorized_exact_owner_language", []))}
    for trail, value in _walk(packet):
        if not isinstance(value, str) or trail in exact_owner_paths:
            continue
        if target_ngrams & _ngrams(_tokens(value)):
            findings.append(_finding("writer.source-prose-leak", f"Writer packet field {'.'.join(trail)} shares an eight-word source sequence."))
            break


def _validate_ledger(ledger: object, findings: list[dict[str, str]]) -> tuple[set[str], set[str]]:
    if not isinstance(ledger, dict):
        findings.append(_finding("ledger.invalid", "Rejected-strategy ledger must be a JSON object."))
        return set(), set()
    if ledger.get("schema_version") != 1 or ledger.get("validator_role") != "separate_chat_adversarial_validator" or ledger.get("writer_access") != "withheld":
        findings.append(_finding("ledger.roles", "Ledger must be withheld from the writer and assigned to a separate Chat validator."))
    families = ledger.get("strategy_families")
    if not isinstance(families, list) or not families:
        findings.append(_finding("ledger.families", "Ledger must contain rejected strategy families."))
        families = []
    family_ids: set[str] = set()
    for index, family in enumerate(families):
        prefix = f"strategy_families[{index}]"
        if not isinstance(family, dict):
            findings.append(_finding("ledger.family", f"{prefix} must be an object."))
            continue
        family_id = family.get("family_id")
        if not isinstance(family_id, str) or not ID_RE.fullmatch(family_id) or family_id in family_ids:
            findings.append(_finding("ledger.family.id", f"{prefix}.family_id must be unique."))
        else:
            family_ids.add(family_id)
        for field in ("structural_signature", "automatic_reject_if"):
            if not _nonblank(family.get(field)):
                findings.append(_finding(f"ledger.family.{field}", f"{prefix}.{field} must be nonblank."))
        for field in ("evidence_refs", "surface_changes_do_not_cure"):
            if not isinstance(family.get(field), list) or not family[field]:
                findings.append(_finding(f"ledger.family.{field}", f"{prefix}.{field} must be non-empty."))
    checks = set(ledger.get("mandatory_structural_checks", []))
    if not MANDATORY_STRUCTURAL_CHECKS <= checks:
        findings.append(_finding("ledger.structural-checks", "Ledger omits mandatory structural recurrence checks."))
    invalid = {str(item).strip().lower() for item in ledger.get("invalid_change_justifications", [])}
    if not MANDATORY_INVALID_JUSTIFICATIONS <= invalid:
        findings.append(_finding("ledger.invalid-justifications", "Ledger omits invalid surface-change justifications."))
    return family_ids, checks


def _validate_candidate_stage(
    data: dict[str, Any], root: Path, family_ids: set[str], structural_checks: set[str], findings: list[dict[str, str]]
) -> str | None:
    candidate = data.get("candidate")
    if not isinstance(candidate, dict):
        findings.append(_finding("candidate.missing", "Validated stages require a candidate object."))
        return None
    path = _resolve(root, candidate.get("path"))
    expected = candidate.get("sha256")
    if path is None or not isinstance(expected, str) or not SHA256_RE.fullmatch(expected):
        findings.append(_finding("candidate.identity", "Candidate needs a safe path and lowercase SHA-256."))
        return None
    try:
        actual = _sha256(path.read_bytes())
    except OSError as exc:
        findings.append(_finding("candidate.read", f"Could not read candidate: {exc}"))
        return None
    if actual != expected:
        findings.append(_finding("candidate.hash", "Candidate hash does not match."))

    receipt = data.get("validation_receipt")
    if not isinstance(receipt, dict):
        findings.append(_finding("receipt.missing", "Validated stages require validation_receipt."))
        return expected
    justifications = receipt.get("change_justifications")
    if not isinstance(justifications, dict) or justifications.get("sentence_coverage_complete") is not True:
        findings.append(_finding("receipt.justification-coverage", "Every candidate sentence must have a recorded change justification."))
    else:
        records = justifications.get("records")
        if not isinstance(records, list) or not records:
            findings.append(_finding("receipt.justifications", "Change justification records must be non-empty."))
        else:
            invalid = MANDATORY_INVALID_JUSTIFICATIONS
            for record in records:
                if not isinstance(record, dict) or not _nonblank(record.get("sentence_ref")) or not _nonblank(record.get("defect_eliminated")):
                    findings.append(_finding("receipt.justification-record", "Each sentence justification needs sentence_ref and defect_eliminated."))
                    continue
                if str(record.get("defect_eliminated", "")).strip().lower() in invalid:
                    findings.append(_finding("receipt.superficial-justification", "Surface conversational changes are not valid defect eliminations."))

    attribution = receipt.get("attribution")
    if not isinstance(attribution, dict) or attribution.get("verdict") != "pass" or attribution.get("findings") != []:
        findings.append(_finding("receipt.attribution", "Attribution review must pass with no findings."))
    elif any(attribution.get(field) is not False for field in ATTRIBUTION_FALSE_FIELDS):
        findings.append(_finding("receipt.attribution-drift", "Attribution review records a forbidden provenance or certainty shift."))

    structural = receipt.get("structural_recurrence")
    if not isinstance(structural, dict) or structural.get("verdict") != "pass" or structural.get("recurrences") != []:
        findings.append(_finding("receipt.structural", "Structural recurrence review must pass with no recurrences."))
    else:
        if set(structural.get("compared_strategy_ids", [])) != family_ids:
            findings.append(_finding("receipt.structural-coverage", "Structural review must compare every rejected strategy family."))
        checks = structural.get("checks")
        if not isinstance(checks, dict) or set(checks) != structural_checks or any(value != "pass" for value in checks.values()):
            findings.append(_finding("receipt.structural-checks", "Every mandatory structural recurrence check must pass."))

    adversarial = receipt.get("adversarial_validation")
    writer_context = data.get("role_boundary", {}).get("writer_context_id") if isinstance(data.get("role_boundary"), dict) else None
    if not isinstance(adversarial, dict):
        findings.append(_finding("receipt.adversarial", "Separate adversarial validation is required."))
    elif (
        adversarial.get("validator_role") != "chat_reasoning"
        or not _nonblank(adversarial.get("validator_context_id"))
        or adversarial.get("validator_context_id") == writer_context
        or adversarial.get("saw_rejected_strategy_ledger") is not True
        or adversarial.get("did_not_edit_candidate") is not True
        or adversarial.get("verdict") != "pass"
        or adversarial.get("findings") != []
    ):
        findings.append(_finding("receipt.adversarial-independence", "Adversarial validation must be a separate, non-editing Chat context with a clean pass."))

    preservation = receipt.get("preservation")
    if not isinstance(preservation, dict) or preservation.get("verdict") != "pass" or preservation.get("unexplained_deltas") != []:
        findings.append(_finding("receipt.preservation", "Preservation must pass with zero unexplained deltas."))
    locked = receipt.get("locked_span_checks")
    expected_locked = {
        span.get("span_id"): span.get("sha256")
        for span in data.get("provenance_spans", [])
        if isinstance(span, dict) and span.get("classification") in {"OWNER_LOCK", "UNKNOWN"}
    }
    if not isinstance(locked, list):
        findings.append(_finding("receipt.locks", "Every frozen/owner-locked span must have a passing byte-preservation check."))
    else:
        actual_locked = {
            item.get("span_id"): item
            for item in locked
            if isinstance(item, dict) and isinstance(item.get("span_id"), str)
        }
        if set(actual_locked) != set(expected_locked):
            findings.append(_finding("receipt.lock-coverage", "Locked-span checks must cover every OWNER_LOCK and UNKNOWN span exactly once."))
        for span_id, expected_hash in expected_locked.items():
            item = actual_locked.get(span_id, {})
            if (
                item.get("verdict") != "pass"
                or item.get("source_sha256") != expected_hash
                or item.get("candidate_sha256") != expected_hash
            ):
                findings.append(_finding("receipt.lock-hash", f"Locked span {span_id!r} is not byte-identical in the candidate."))
    return expected


def validate_control(data: object, root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if not isinstance(data, dict):
        return [_finding("control.invalid-root", "Control root must be a JSON object.")]
    if data.get("schema_version") != 1:
        findings.append(_finding("control.schema", "schema_version must be 1."))
    if not _nonblank(data.get("control_id")):
        findings.append(_finding("control.id", "control_id must be nonblank."))
    state = data.get("workflow_state")
    if state not in ALLOWED_STATES:
        findings.append(_finding("control.state", "workflow_state is unsupported."))

    roles = data.get("role_boundary")
    if not isinstance(roles, dict) or roles.get("reasoning_owner") != "Chat" or roles.get("mechanical_executor") != "Codex" or not _nonblank(roles.get("rule")):
        findings.append(_finding("control.roles", "The role boundary must assign reasoning to Chat and mechanical execution to Codex."))

    source_bytes, ai_ids = _validate_source_and_provenance(data, root, findings)
    _, writer = _load_bound_json(root, data.get("writer_packet"), "writer_packet", findings)
    writer_record = data.get("writer_packet")
    if not isinstance(writer_record, dict) or any(writer_record.get(field) is not True for field in ("source_prose_withheld", "rejected_strategy_ledger_withheld", "semantic_units_frozen")):
        findings.append(_finding("writer.isolation", "Writer isolation declarations must all be true."))
    _validate_writer_packet(writer, ai_ids, source_bytes, data, findings)

    _, ledger = _load_bound_json(root, data.get("rejected_strategy_ledger"), "rejected_strategy_ledger", findings)
    ledger_record = data.get("rejected_strategy_ledger")
    if not isinstance(ledger_record, dict) or ledger_record.get("writer_withheld") is not True or ledger_record.get("adversarial_validator_only") is not True:
        findings.append(_finding("ledger.isolation", "Rejected-strategy ledger must be withheld from the writer and reserved for the validator."))
    family_ids, structural_checks = _validate_ledger(ledger, findings)

    gates = data.get("gates")
    if not isinstance(gates, dict) or set(gates) != GATE_NAMES:
        findings.append(_finding("control.gates", "gates must contain exactly the required gate names."))
        gates = {}
    release = data.get("release")
    detector = data.get("detector")
    if not isinstance(detector, dict) or detector.get("policy") != "detector-last":
        findings.append(_finding("detector.policy", "Detector policy must be detector-last."))
        detector = {}

    if state == "prewrite_ready":
        for gate in GATE_NAMES:
            expected = "pass" if gate in PREWRITE_PASS else "pending"
            if gates.get(gate) != expected:
                findings.append(_finding("control.prewrite-gates", f"Prewrite gate {gate} must be {expected}."))
        if data.get("candidate") is not None or data.get("validation_receipt") is not None:
            findings.append(_finding("control.prewrite-candidate", "Prewrite state cannot contain a candidate or validation receipt."))
        if not isinstance(release, dict) or release.get("candidate_visibility") != "blocked" or release.get("detector_eligibility") != "blocked" or not release.get("blockers"):
            findings.append(_finding("control.fail-closed", "Prewrite state must block candidate visibility and detector eligibility with reasons."))
        if detector.get("status") != "not-run" or detector.get("submitted_candidate_sha256") is not None or detector.get("result") is not None:
            findings.append(_finding("detector.early", "Detector must not run in prewrite state."))
    elif state in {"candidate_validated", "detector_recorded"}:
        if any(gates.get(gate) != "pass" for gate in GATE_NAMES):
            findings.append(_finding("control.validated-gates", "Every gate must pass before candidate release or detector use."))
        candidate_hash = _validate_candidate_stage(data, root, family_ids, structural_checks, findings)
        if not isinstance(release, dict) or release.get("candidate_visibility") != "eligible" or release.get("detector_eligibility") != "eligible" or release.get("blockers") != []:
            findings.append(_finding("control.release", "Validated state must record an unblocked candidate and detector eligibility."))
        if state == "candidate_validated":
            if detector.get("status") != "not-run" or detector.get("submitted_candidate_sha256") is not None or detector.get("result") is not None:
                findings.append(_finding("detector.order", "Detector can run only after candidate_validated state is recorded."))
        else:
            checkpoint_record = detector.get("validated_control_checkpoint")
            _, checkpoint = _load_bound_json(root, checkpoint_record, "detector.validated-checkpoint", findings)
            checkpoint_valid = (
                isinstance(checkpoint, dict)
                and checkpoint.get("control_id") == data.get("control_id")
                and checkpoint.get("workflow_state") == "candidate_validated"
                and isinstance(checkpoint.get("candidate"), dict)
                and checkpoint["candidate"].get("sha256") == candidate_hash
                and isinstance(checkpoint.get("detector"), dict)
                and checkpoint["detector"].get("status") == "not-run"
                and isinstance(checkpoint.get("gates"), dict)
                and all(checkpoint["gates"].get(gate) == "pass" for gate in GATE_NAMES)
            )
            if not checkpoint_valid:
                findings.append(_finding("detector.checkpoint", "Detector use requires an exact prior candidate_validated control checkpoint with detector not run."))
            if detector.get("status") != "recorded" or detector.get("submitted_candidate_sha256") != candidate_hash or not isinstance(detector.get("result"), dict):
                findings.append(_finding("detector.binding", "Recorded detector result must bind to the validated candidate hash."))
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("control", type=Path, help="Path to humanization-control JSON")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.control.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"FAIL: could not read control: {exc}", file=sys.stderr)
        return 2
    findings = validate_control(data, args.root.resolve())
    status = "PASS" if not findings else "FAIL"
    print(json.dumps({"status": status, "workflow_state": data.get("workflow_state"), "findings": findings}, indent=2, ensure_ascii=False))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
