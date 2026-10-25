#!/usr/bin/env python3
"""Fail-closed owner-facing humanization delivery gate.

This does NOT certify authorship or cryptographically prove reviewer independence.
It verifies the exact draft/context/source/inventory identities, executes the
existing mechanical linter, and requires separately saved, source-bound review
evidence before exporting model-written Joel-byline prose.

Usage:
  python3 tools/humanization/owner_delivery_gate.py init \
      --draft DRAFT.txt --context SECTION.txt --source SOURCE.txt --manifest RECEIPT.json
  python3 tools/humanization/owner_delivery_gate.py check \
      --draft DRAFT.txt --context SECTION.txt --source SOURCE.txt --manifest RECEIPT.json
  python3 tools/humanization/owner_delivery_gate.py deliver \
      --draft DRAFT.txt --context SECTION.txt --source SOURCE.txt --manifest RECEIPT.json \
      --out OWNER_REVIEW.txt --proof OWNER_REVIEW.proof.json

Generate a draft INTERNALLY before init. The init receipt is intentionally
PENDING and cannot be used as approval; populate all ledger entries and point
its review_files to external, independently produced review JSON files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[2]
INVENTORY = ROOT / "docs" / "HUMANIZATION-TELL-INVENTORY.md"
LINTER = pathlib.Path(__file__).with_name("tells_lint.py")
SCHEMA = "JOEL_OWNER_DELIVERY_GATE_V1"
REVIEW_SCHEMA = "JOEL_COLD_REVIEW_V1"
ROLES = ("preservation", "cold_read_1", "cold_read_2")
TELL_ID = re.compile(r"^\*\*((?:T|C)\d{2})\s+—", re.M)
VERDICT = re.compile(r"^verdict:\s*(CLEAR|REVIEW|FAIL)\s*$", re.M)
FLAG = re.compile(r"^-- (.+) \((\d+)\)$")


class GateError(Exception):
    """One or more delivery gates could not be verified."""


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: pathlib.Path) -> bytes:
    return path.read_bytes()


def json_file(path: pathlib.Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise GateError(f"{path}: expected JSON object")
    return value


def inventory_ids(data: bytes) -> list[str]:
    ids = TELL_ID.findall(data.decode("utf-8"))
    if len(ids) != len(set(ids)) or not ids:
        raise GateError("tell inventory must have unique T/C identifiers")
    return ids


def flags(output: str) -> list[dict]:
    found = []
    current = None
    for line in output.splitlines():
        match = FLAG.match(line)
        if match:
            current = {"label": match.group(1), "examples": []}
            found.append(current)
        elif line.startswith("   * ") and current is not None:
            current["examples"].append(line[5:].strip())
    return found


def lint(draft: pathlib.Path, source: pathlib.Path) -> dict:
    run = subprocess.run(
        [sys.executable, str(LINTER), str(draft), '--source', str(source)],
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
        env=None,
    )
    match = VERDICT.search(run.stdout)
    if match is None or run.returncode not in (0, 1, 2):
        raise GateError(
            f"tells_lint.py did not produce a trustworthy verdict; exit={run.returncode}; "
            f"stderr={run.stderr[-500:]}"
        )
    status = match.group(1)
    if run.returncode != {"CLEAR": 0, "REVIEW": 1, "FAIL": 2}[status]:
        raise GateError(f"tells_lint.py exit code contradicts verdict {status}")
    return {
        "verdict": status,
        "stdout_sha256": sha(run.stdout.encode("utf-8")),
        "linter_sha256": sha(load(LINTER)),
        "findings": flags(run.stdout),
        "output": run.stdout,
    }


def source_values(args: argparse.Namespace) -> dict:
    draft = args.draft.read_bytes()
    context = args.context.read_bytes()
    source = args.source.read_bytes()
    if not draft.strip() or not context.strip() or not source.strip():
        raise GateError("draft, context and source must all be nonempty")
    # The literal target must occur once in the actual reading boundary.
    if context.count(draft) != 1:
        raise GateError("context must contain the exact draft bytes exactly once")
    inv = load(INVENTORY)
    return {
        "candidate_sha256": sha(draft),
        "context_sha256": sha(context),
        "source_sha256": sha(source),
        "inventory_sha256": sha(inv),
        "inventory_ids": inventory_ids(inv),
    }


def template(args: argparse.Namespace) -> dict:
    values = source_values(args)
    result = lint(args.draft, args.source)
    return {
        "schema": SCHEMA,
        "status": "PENDING",
        **{k: v for k, v in values.items() if k != "inventory_ids"},
        "writer": {
            "name": "",
            "context_id": "",
        },
        "lint": {
            "verdict_at_init": result["verdict"],
            "linter_sha256": result["linter_sha256"],
            "stdout_sha256": result["stdout_sha256"],
            "findings": [
                {**finding, "disposition": "PENDING", "reason": ""}
                for finding in result["findings"]
            ],
        },
        "tell_ledger": [
            {"id": ident, "status": "UNCERTAIN", "evidence": "", "resolution": ""}
            for ident in values["inventory_ids"]
        ],
        "review_files": {role: "" for role in ROLES},
    }


def check_review(
    role: str, path: pathlib.Path, values: dict, writer: dict
) -> tuple[dict, str]:
    review = json_file(path)
    errors = []
    if review.get("schema") != REVIEW_SCHEMA or review.get("role") != role:
        errors.append("schema/role mismatch")
    for k in ("candidate_sha256", "context_sha256", "source_sha256"):
        if review.get(k) != values[k]:
            errors.append(f"{k} mismatch")
    if review.get("verdict") != "PASS" or review.get("unresolved"):
        errors.append("review is not a resolved PASS")
    # A claimed 'fresh' label is insufficient on its own. Keep independently
    # produced, exact-bound artifacts and reported context IDs auditable.
    rv = review.get("reviewer")
    if not isinstance(rv, dict):
        rv = {}
    for k in ("name", "context_id", "origin"):
        if not isinstance(rv.get(k), str) or not rv[k].strip():
            errors.append(f"missing reviewer.{k}")
    if rv.get("context_id") == writer.get("context_id"):
        errors.append("writer and reviewer contexts are identical")
    note = review.get("evidence")
    if not isinstance(note, str) or len(note.strip()) < 30:
        errors.append("review needs substantive, source-specific evidence")
    if errors:
        raise GateError(f"{role} review {path}: " + "; ".join(errors))
    return review, sha(load(path))


def validate(args: argparse.Namespace) -> dict:
    values = source_values(args)
    manifest = json_file(args.manifest)
    errors = []
    if manifest.get("schema") != SCHEMA:
        errors.append("invalid manifest schema")
    if manifest.get("status") != "READY_FOR_CHECK":
        errors.append("manifest status must be READY_FOR_CHECK after completed reviews")
    for key in ("candidate_sha256", "context_sha256", "source_sha256", "inventory_sha256"):
        if manifest.get(key) != values[key]:
            errors.append(f"stale or incorrect {key}")
    writer = manifest.get("writer")
    if not isinstance(writer, dict):
        writer = {}
    for k in ("name", "context_id"):
        if not isinstance(writer.get(k), str) or not writer[k].strip():
            errors.append(f"writer.{k} is missing")
    # Lint runs afresh at admission time. A recorded linter answer alone
    # cannot clear a candidate; FAIL is always blocking for model prose.
    current = lint(args.draft, args.source)
    old_lint = manifest.get("lint")
    if not isinstance(old_lint, dict):
        old_lint = {}
    for key, value in (
        ("verdict_at_init", current["verdict"]),
        ("linter_sha256", current["linter_sha256"]),
        ("stdout_sha256", current["stdout_sha256"]),
    ):
        if old_lint.get(key) != value:
            errors.append(f"linter changed since init: {key}")
    if current["verdict"] == "FAIL":
        errors.append("mechanical tells_lint verdict FAIL (rewrite before delivery)")
    actual_flags = {f["label"]: f["examples"] for f in current["findings"]}
    recorded = old_lint.get("findings", [])
    if not isinstance(recorded, list):
        recorded = []
    recorded_flags = {}
    for flag in recorded:
        if not isinstance(flag, dict) or not isinstance(flag.get("label"), str):
            errors.append("malformed linter finding")
            continue
        if flag["label"] in recorded_flags:
            errors.append(f"duplicate lint disposition {flag['label']}")
        recorded_flags[flag["label"]] = flag
    if set(actual_flags) != set(recorded_flags):
        errors.append("lint findings do not match current literal candidate")
    for label, examples in actual_flags.items():
        record = recorded_flags.get(label, {})
        if record.get("examples") != examples:
            errors.append(f"changed lint examples for {label}")
        if record.get("disposition") != "JUSTIFIED_KEEP":
            errors.append(f"lint finding unresolved: {label}")
        if len(str(record.get("reason") or "").strip()) < 24:
            errors.append(f"missing specific lint reasoning: {label}")
    ledger = manifest.get("tell_ledger", [])
    if not isinstance(ledger, list):
        ledger = []
    found = {}
    for row in ledger:
        if not isinstance(row, dict):
            errors.append("non-object tell entry")
            continue
        ident = row.get("id")
        if ident in found:
            errors.append(f"duplicate tell entry {ident}")
        found[ident] = row
    if set(found) != set(values["inventory_ids"]):
        absent = sorted(set(values["inventory_ids"]) - set(found))
        extra = sorted(set(found) - set(values["inventory_ids"]))
        errors.append(f"tell inventory incomplete or stale: missing={absent}, extra={extra}")
    justified = []
    for ident in values["inventory_ids"]:
        row = found.get(ident)
        if row is None:
            continue
        status = row.get("status")
        evidence = row.get("evidence")
        if status not in ("ABSENT", "PRESENT"):
            errors.append(f"{ident}: UNCERTAIN or invalid status is blocking")
        if not isinstance(evidence, str) or len(evidence.strip()) < 12:
            errors.append(f"{ident}: missing literal-text evidence")
        if status == "PRESENT":
            if row.get("resolution") != "JUSTIFIED_KEEP":
                errors.append(f"{ident}: PRESENT without explicit accepted resolution")
            elif len(str(row.get("reason") or "").strip()) < 24:
                errors.append(f"{ident}: missing particular justification")
            else:
                justified.append(ident)
    reports = manifest.get("review_files")
    if not isinstance(reports, dict):
        reports = {}
    proof_reviews = {}
    contexts = []
    for role in ROLES:
        rel = reports.get(role)
        if not isinstance(rel, str) or not rel.strip():
            errors.append(f"{role}: missing separate reviewer report file")
            continue
        path = (args.manifest.parent / rel).resolve()
        if not path.is_file():
            errors.append(f"{role}: review artifact not found: {rel}")
            continue
        try:
            review, review_sha = check_review(role, path, values, writer)
            rv = review["reviewer"]
            contexts.append(rv["context_id"])
            proof_reviews[role] = {
                "path": rel,
                "sha256": review_sha,
                "reviewer": rv,
            }
            if justified and not set(justified).issubset(
                set(review.get("resolved_tell_ids", []))
            ):
                errors.append(
                    f"{role} did not explicitly review justified tells {justified}"
                )
        except (GateError, ValueError, OSError) as exc:
            errors.append(str(exc))
    if len(contexts) != len(set(contexts)):
        errors.append("reviewers shared a context; separate cold reads not verified")
    if errors:
        # The full evidence is in the manifest and lint stdout. Present an
        # actionable summary rather than 33 near-identical UNCERTAIN rows.
        raise GateError("\n- " + "\n- ".join(errors[:14]) +
                        (f"\n- ... and {len(errors) - 14} additional unresolved gate items"
                         if len(errors) > 14 else ""))
    return {
        "schema": "JOEL_OWNER_DELIVERY_ADMITTED_V1",
        "candidate_sha256": values["candidate_sha256"],
        "context_sha256": values["context_sha256"],
        "source_sha256": values["source_sha256"],
        "inventory_sha256": values["inventory_sha256"],
        "lint_verdict": current["verdict"],
        "linter_sha256": current["linter_sha256"],
        "lint_stdout_sha256": current["stdout_sha256"],
        "lint_findings": [
            {"label": f["label"], "examples": f["examples"],
             "disposition": recorded_flags.get(f["label"], {}).get("disposition")}
            for f in current["findings"]
        ],
        "tell_ledger_counts": {
            "ABSENT": sum(row.get("status") == "ABSENT" for row in found.values()),
            "PRESENT_JUSTIFIED": len(justified),
            "UNCERTAIN": 0,
            "total": len(values["inventory_ids"]),
        },
        "justified_tells": justified,
        "reviews": proof_reviews,
        "manifest_sha256": sha(load(args.manifest)),
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def save_file(path: pathlib.Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Don't silently overwrite someone else's candidate or review packet.
    if path.exists() and path.read_bytes() != data:
        raise GateError(f"refusing to overwrite non-identical file: {path}")
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".gate-", delete=False) as f:
        f.write(data)
        temp = pathlib.Path(f.name)
    temp.replace(path)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="action", required=True)
    for name in ("init", "check", "deliver"):
        p = sub.add_parser(name)
        p.add_argument("--draft", type=pathlib.Path, required=True)
        p.add_argument("--context", type=pathlib.Path, required=True)
        p.add_argument("--source", type=pathlib.Path, required=True)
        p.add_argument("--manifest", type=pathlib.Path, required=True)
        if name == "deliver":
            p.add_argument("--out", type=pathlib.Path, required=True)
            p.add_argument("--proof", type=pathlib.Path, required=True)
    args = ap.parse_args(argv)
    try:
        if args.action == "init":
            data = template(args)
            save_file(
                args.manifest,
                (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
            )
            print(
                f"PENDING: {args.manifest} candidate={data['candidate_sha256']} "
                f"tell_rows={len(data['tell_ledger'])} lint={data['lint']['verdict_at_init']}"
            )
            return 0
        report = validate(args)
        if args.action == "check":
            print(
                f"ADMITTED candidate={report['candidate_sha256']} "
                f"reviews={','.join(report['reviews'])}"
            )
            return 0
        payload = load(args.draft)
        receipt = (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        sources = {args.draft.resolve(), args.context.resolve(), args.source.resolve(),
                   args.manifest.resolve(), INVENTORY.resolve(), LINTER.resolve()}
        if args.out.resolve() in sources or args.proof.resolve() in sources:
            raise GateError("delivery cannot overwrite draft/source/context/manifest")
        if args.out.resolve() == args.proof.resolve():
            raise GateError("delivered text and proof paths must differ")
        # Preflight both destinations BEFORE writing either.
        for path, data in ((args.out, payload), (args.proof, receipt)):
            if path.exists() and path.read_bytes() != data:
                raise GateError(f"refusing to replace existing artifact: {path}")
        save_file(args.out, payload)
        save_file(args.proof, receipt)
        print(f"DELIVERED {args.out} proof={args.proof} sha256={report['candidate_sha256']}")
        return 0
    except (GateError, ValueError, OSError, subprocess.TimeoutExpired) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
