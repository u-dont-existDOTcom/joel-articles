#!/usr/bin/env python3
"""Validate Joel Articles authority, integrity, privacy, and recovery metadata.

This gate validates repository truth. An empty governance incubator may pass while
content import remains explicitly blocked; passing never invents article authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
ARTICLE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ARTICLE_STATUSES = {"working", "owner_final", "published", "blocked"}
REPOSITORY_STATUSES = {"governance_incubator", "active", "archived"}
REVIEW_STATUSES = {
    "citations": {"pending", "verified", "blocked", "not_applicable"},
    "detector": {"not_run", "recorded", "blocked", "not_applicable"},
    "editorial": {"pending", "passed", "blocked"},
}
AUTHORITY_FIELDS = {
    "master",
    "owner_locks",
    "source_evidence",
    "unincorporated_ideas",
    "current_state",
}
REVIEW_FIELDS = {"citations", "detector", "editorial"}
FORBIDDEN_DIRECTORY_NAMES = {
    "incoming-private",
    "private",
    "secrets",
}
DETACHED_CONTENT_ROOTS = {"sources", "evidence", "experiments", "publish"}
ARTICLE_STATE_HEADINGS = {
    "goal",
    "authority / baseline",
    "completed",
    "current checkpoint",
    "remaining",
    "blockers / unresolved",
    "evidence / artifacts",
    "next safe action",
}


def _finding(code: str, path: str, message: str) -> dict[str, str]:
    return {"code": code, "path": path, "message": message}


def _sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _safe_relative_path(value: object) -> str | None:
    if not isinstance(value, str) or not value or "\\" in value:
        return None
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path.as_posix()


def _first_symlink_component(root: Path, relative: str) -> str | None:
    probe = root
    for part in PurePosixPath(relative).parts:
        probe = probe / part
        if probe.is_symlink():
            return probe.relative_to(root).as_posix()
    return None


def _load_json(path: Path) -> tuple[Any | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return None, str(exc)


def _tracked_or_present_files(root: Path) -> list[Path]:
    if (root / ".git").exists():
        result = subprocess.run(
            [
                "git",
                "-C",
                str(root),
                "ls-files",
                "--cached",
                "--others",
                "--exclude-standard",
                "-z",
            ],
            check=False,
            capture_output=True,
        )
        if result.returncode == 0:
            return [root / raw.decode("utf-8") for raw in result.stdout.split(b"\0") if raw]
    return [
        path
        for path in root.rglob("*")
        if path.is_file()
        and ".git" not in path.relative_to(root).parts
        and "__pycache__" not in path.relative_to(root).parts
    ]


def _validate_privacy(root: Path) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in _tracked_or_present_files(root):
        relative = path.relative_to(root)
        if (
            relative.name == ".env"
            or relative.name.startswith(".env.")
            or any(part.lower() in FORBIDDEN_DIRECTORY_NAMES for part in relative.parts[:-1])
        ):
            findings.append(
                _finding(
                    "privacy.forbidden-path",
                    relative.as_posix(),
                    "Private staging, environment, and secret material must not be tracked in this public repository.",
                )
            )
    return findings


def _validate_reference(
    root: Path,
    article_id: str,
    label: str,
    reference: object,
) -> tuple[list[dict[str, str]], Path | None]:
    findings: list[dict[str, str]] = []
    index_path = "articles/INDEX.json"
    if not isinstance(reference, dict):
        return [
            _finding(
                "article.field.invalid",
                index_path,
                f"Article {article_id!r} reference {label!r} must be an object with path and sha256.",
            )
        ], None

    relative = _safe_relative_path(reference.get("path"))
    expected_sha = reference.get("sha256")
    if relative is None or not isinstance(expected_sha, str) or not SHA256_RE.fullmatch(expected_sha):
        return [
            _finding(
                "article.field.invalid",
                index_path,
                f"Article {article_id!r} reference {label!r} needs a safe relative path and lowercase SHA-256.",
            )
        ], None

    prefix = f"articles/{article_id}/"
    if not relative.startswith(prefix):
        findings.append(
            _finding(
                "article.path.outside-boundary",
                relative,
                f"Article {article_id!r} references must remain inside {prefix!r}.",
            )
        )

    path = root / relative
    symlink_component = _first_symlink_component(root, relative)
    if symlink_component is not None:
        findings.append(
            _finding(
                "article.path.symlink",
                relative,
                f"Article {article_id!r} reference {label!r} crosses a symlink at {symlink_component!r}; article authority must be physically self-contained.",
            )
        )
        return findings, None
    if not path.is_file():
        findings.append(
            _finding(
                "article.path.missing",
                relative,
                f"Article {article_id!r} reference {label!r} does not exist.",
            )
        )
        return findings, None

    actual_sha = _sha256_bytes(path.read_bytes())
    if actual_sha != expected_sha:
        findings.append(
            _finding(
                "article.hash.mismatch",
                relative,
                f"Article {article_id!r} reference {label!r} expected {expected_sha} but found {actual_sha}.",
            )
        )
    return findings, path


def _validate_owner_locks(
    article_id: str,
    article_status: object,
    master_path: Path | None,
    locks_path: Path | None,
) -> list[dict[str, str]]:
    if master_path is None or locks_path is None:
        return []
    findings: list[dict[str, str]] = []
    lock_data, error = _load_json(locks_path)
    lock_relative = locks_path.as_posix()
    if error or not isinstance(lock_data, dict):
        return [
            _finding(
                "article.owner-lock.invalid",
                lock_relative,
                f"Owner-lock manifest is not valid JSON: {error or 'root must be an object'}.",
            )
        ]
    if lock_data.get("schema_version") != 1 or lock_data.get("article_id") != article_id:
        findings.append(
            _finding(
                "article.owner-lock.invalid",
                lock_relative,
                "Owner-lock manifest must use schema_version 1 and match the article id.",
            )
        )
    passages = lock_data.get("locked_passages")
    functions = lock_data.get("protected_functions")
    owner_review = lock_data.get("owner_review")
    if not isinstance(passages, list) or not isinstance(functions, list) or not isinstance(owner_review, dict):
        findings.append(
            _finding(
                "article.owner-lock.invalid",
                lock_relative,
                "Owner-lock manifest requires locked_passages and protected_functions arrays plus an owner_review object.",
            )
        )
        return findings

    review_status = owner_review.get("status")
    review_evidence = owner_review.get("evidence")
    if review_status not in {"pending", "confirmed", "blocked"} or not isinstance(review_evidence, str) or not review_evidence.strip():
        findings.append(
            _finding(
                "article.owner-lock.invalid",
                lock_relative,
                "owner_review needs a supported status and nonblank durable evidence reference.",
            )
        )
    if article_status in {"owner_final", "published"} and review_status != "confirmed":
        findings.append(
            _finding(
                "article.owner-lock.unconfirmed",
                lock_relative,
                f"Article {article_id!r} cannot be {article_status!r} until owner-lock review is confirmed.",
            )
        )

    master = master_path.read_text(encoding="utf-8")
    seen: set[str] = set()
    for position, item in enumerate(passages):
        if not isinstance(item, dict):
            findings.append(
                _finding(
                    "article.owner-lock.invalid",
                    lock_relative,
                    f"locked_passages[{position}] must be an object.",
                )
            )
            continue
        lock_id = item.get("id")
        text = item.get("text")
        expected_sha = item.get("sha256")
        if (
            not isinstance(lock_id, str)
            or not lock_id
            or lock_id in seen
            or not isinstance(text, str)
            or not text
            or not isinstance(expected_sha, str)
            or not SHA256_RE.fullmatch(expected_sha)
        ):
            findings.append(
                _finding(
                    "article.owner-lock.invalid",
                    lock_relative,
                    f"locked_passages[{position}] needs a unique id, exact text, and lowercase SHA-256.",
                )
            )
            continue
        seen.add(lock_id)
        actual_sha = _sha256_bytes(text.encode("utf-8"))
        if actual_sha != expected_sha:
            findings.append(
                _finding(
                    "article.owner-lock.hash-mismatch",
                    lock_relative,
                    f"Owner lock {lock_id!r} hashes to {actual_sha}, not {expected_sha}.",
                )
            )
        if text not in master:
            findings.append(
                _finding(
                    "article.owner-lock.missing",
                    master_path.as_posix(),
                    f"Owner-locked passage {lock_id!r} is absent from the registered master.",
                )
            )
    function_ids: set[str] = set()
    for position, item in enumerate(functions):
        function_id = item.get("id") if isinstance(item, dict) else None
        description = item.get("description") if isinstance(item, dict) else None
        if (
            not isinstance(function_id, str)
            or not function_id
            or function_id in function_ids
            or not isinstance(description, str)
            or not description.strip()
        ):
            findings.append(
                _finding(
                    "article.owner-lock.invalid",
                    lock_relative,
                    f"protected_functions[{position}] needs a unique id and nonblank description.",
                )
            )
            continue
        function_ids.add(function_id)
    return findings


def _validate_source_evidence(article_id: str, path: Path | None) -> list[dict[str, str]]:
    if path is None:
        return []
    data, error = _load_json(path)
    if (
        error
        or not isinstance(data, dict)
        or data.get("schema_version") != 1
        or data.get("article_id") != article_id
        or not isinstance(data.get("claims"), list)
    ):
        return [
            _finding(
                "article.evidence.invalid",
                path.as_posix(),
                "Source-evidence index must be schema_version 1, match the article id, and contain a claims array.",
            )
        ]
    return []


def _validate_review_file(
    article_id: str,
    label: str,
    expected_status: object,
    path: Path | None,
) -> list[dict[str, str]]:
    if path is None:
        return []
    data, error = _load_json(path)
    collection_key = {"citations": "claims", "detector": "runs", "editorial": "checks"}[label]
    if (
        error
        or not isinstance(data, dict)
        or data.get("schema_version") != 1
        or data.get("article_id") != article_id
        or not isinstance(data.get(collection_key), list)
    ):
        return [
            _finding(
                "article.review.invalid",
                path.as_posix(),
                f"{label!r} record must be schema_version 1, match the article id, and contain a {collection_key} array.",
            )
        ]
    if data.get("status") != expected_status:
        return [
            _finding(
                "article.review.mismatch",
                path.as_posix(),
                f"{label!r} file status {data.get('status')!r} does not match registry status {expected_status!r}.",
            )
        ]
    return []


def _validate_article_state(article_id: str, state_path: Path | None) -> list[dict[str, str]]:
    if state_path is None:
        return []
    headings = {
        line[3:].strip().lower()
        for line in state_path.read_text(encoding="utf-8").splitlines()
        if line.startswith("## ")
    }
    missing = sorted(ARTICLE_STATE_HEADINGS - headings)
    if not missing:
        return []
    return [
        _finding(
            "article.state.incomplete",
            state_path.as_posix(),
            f"Article {article_id!r} current state is missing headings: {', '.join(missing)}.",
        )
    ]


def _validate_article(root: Path, article: object, position: int) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    index_path = "articles/INDEX.json"
    if not isinstance(article, dict):
        return [
            _finding(
                "article.invalid",
                index_path,
                f"articles[{position}] must be an object.",
            )
        ]

    article_id = article.get("id")
    title = article.get("title")
    status = article.get("status")
    if not isinstance(article_id, str) or not ARTICLE_ID_RE.fullmatch(article_id):
        return [
            _finding(
                "article.id.invalid",
                index_path,
                f"articles[{position}].id must be a lowercase kebab-case identifier.",
            )
        ]
    if not isinstance(title, str) or not title.strip() or status not in ARTICLE_STATUSES:
        findings.append(
            _finding(
                "article.field.invalid",
                index_path,
                f"Article {article_id!r} needs a nonblank title and a supported status.",
            )
        )

    authority = article.get("authority")
    review = article.get("review")
    if not isinstance(authority, dict) or not AUTHORITY_FIELDS.issubset(authority):
        missing = sorted(AUTHORITY_FIELDS - set(authority or {}) if isinstance(authority, dict) else AUTHORITY_FIELDS)
        findings.append(
            _finding(
                "article.field.missing",
                index_path,
                f"Article {article_id!r} authority is missing: {', '.join(missing)}.",
            )
        )
    if not isinstance(review, dict) or not REVIEW_FIELDS.issubset(review):
        missing = sorted(REVIEW_FIELDS - set(review or {}) if isinstance(review, dict) else REVIEW_FIELDS)
        findings.append(
            _finding(
                "article.field.missing",
                index_path,
                f"Article {article_id!r} review is missing: {', '.join(missing)}.",
            )
        )

    resolved: dict[str, Path | None] = {}
    if isinstance(authority, dict):
        for label in sorted(AUTHORITY_FIELDS & set(authority)):
            reference_findings, resolved[label] = _validate_reference(
                root, article_id, label, authority[label]
            )
            findings.extend(reference_findings)

    if isinstance(review, dict):
        for label in sorted(REVIEW_FIELDS & set(review)):
            record = review[label]
            reference_findings, resolved[label] = _validate_reference(
                root, article_id, label, record
            )
            findings.extend(reference_findings)
            actual_status = record.get("status") if isinstance(record, dict) else None
            if actual_status not in REVIEW_STATUSES[label]:
                findings.append(
                    _finding(
                        "article.review.invalid",
                        index_path,
                        f"Article {article_id!r} review {label!r} has unsupported status {actual_status!r}.",
                    )
                )

        if status in {"owner_final", "published"}:
            citation_status = review.get("citations", {}).get("status") if isinstance(review.get("citations"), dict) else None
            editorial_status = review.get("editorial", {}).get("status") if isinstance(review.get("editorial"), dict) else None
            if citation_status not in {"verified", "not_applicable"} or editorial_status != "passed":
                findings.append(
                    _finding(
                        "article.review.incomplete",
                        index_path,
                        f"Article {article_id!r} cannot be {status!r} without completed citation disposition and editorial pass.",
                    )
                )

    findings.extend(
        _validate_owner_locks(
            article_id,
            status,
            resolved.get("master"),
            resolved.get("owner_locks"),
        )
    )
    findings.extend(_validate_source_evidence(article_id, resolved.get("source_evidence")))
    if isinstance(review, dict):
        for label in sorted(REVIEW_FIELDS & set(review)):
            record = review[label]
            expected_status = record.get("status") if isinstance(record, dict) else None
            findings.extend(
                _validate_review_file(
                    article_id,
                    label,
                    expected_status,
                    resolved.get(label),
                )
            )
    findings.extend(_validate_article_state(article_id, resolved.get("current_state")))

    exports = article.get("publication_exports")
    if not isinstance(exports, list):
        findings.append(
            _finding(
                "article.field.missing",
                index_path,
                f"Article {article_id!r} requires a publication_exports array.",
            )
        )
        exports = []
    published_exports = 0
    for export_position, export in enumerate(exports):
        required = {"path", "sha256", "destination", "source_authority", "status"}
        if not isinstance(export, dict) or not required.issubset(export):
            findings.append(
                _finding(
                    "article.export.invalid",
                    index_path,
                    f"Article {article_id!r} export {export_position} must record path, sha256, destination, source_authority, and status.",
                )
            )
            continue
        reference_findings, _ = _validate_reference(
            root,
            article_id,
            f"publication_exports[{export_position}]",
            export,
        )
        findings.extend(reference_findings)
        if export.get("status") not in {"draft", "published", "superseded"}:
            findings.append(
                _finding(
                    "article.export.invalid",
                    index_path,
                    f"Article {article_id!r} export {export_position} has an unsupported status.",
                )
            )
        if not isinstance(export.get("destination"), str) or not export.get("destination") or not isinstance(export.get("source_authority"), str) or not export.get("source_authority"):
            findings.append(
                _finding(
                    "article.export.invalid",
                    index_path,
                    f"Article {article_id!r} export {export_position} needs nonblank destination and source_authority provenance.",
                )
            )
        if export.get("status") == "published":
            published_exports += 1
    if status == "published" and published_exports == 0:
        findings.append(
            _finding(
                "article.export.invalid",
                index_path,
                f"Article {article_id!r} is marked published without a published export record.",
            )
        )

    additional = article.get("additional_artifacts")
    if not isinstance(additional, list):
        findings.append(
            _finding(
                "article.field.missing",
                index_path,
                f"Article {article_id!r} requires an additional_artifacts array, even when empty.",
            )
        )
        additional = []
    for artifact_position, artifact in enumerate(additional):
        role = artifact.get("role") if isinstance(artifact, dict) else None
        if not isinstance(role, str) or not role.strip():
            findings.append(
                _finding(
                    "article.artifact.invalid",
                    index_path,
                    f"Article {article_id!r} additional artifact {artifact_position} needs a nonblank role.",
                )
            )
        reference_findings, _ = _validate_reference(
            root,
            article_id,
            f"additional_artifacts[{artifact_position}]",
            artifact,
        )
        findings.extend(reference_findings)
    return findings


def _registered_article_paths(article: object) -> set[str]:
    if not isinstance(article, dict):
        return set()
    references: list[object] = []
    for container_name in ("authority", "review"):
        container = article.get(container_name)
        if isinstance(container, dict):
            references.extend(container.values())
    for list_name in ("publication_exports", "additional_artifacts"):
        container = article.get(list_name)
        if isinstance(container, list):
            references.extend(container)
    paths: set[str] = set()
    for reference in references:
        if isinstance(reference, dict):
            relative = _safe_relative_path(reference.get("path"))
            if relative is not None:
                paths.add(relative)
    return paths


def _validate_content_inventory(
    root: Path,
    repository_status: object,
    articles: list[object],
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    registered_ids = {
        article["id"]
        for article in articles
        if isinstance(article, dict)
        and isinstance(article.get("id"), str)
        and ARTICLE_ID_RE.fullmatch(article["id"])
    }
    registered_paths: dict[str, set[str]] = {
        article_id: set() for article_id in registered_ids
    }
    for article in articles:
        if isinstance(article, dict) and article.get("id") in registered_paths:
            registered_paths[article["id"]].update(_registered_article_paths(article))

    reserved_article_files = {"articles/INDEX.json", "articles/AGENTS.md"}
    article_files: list[str] = []
    for path in _tracked_or_present_files(root):
        relative = path.relative_to(root).as_posix()
        parts = PurePosixPath(relative).parts
        symlink_component = (
            _first_symlink_component(root, relative)
            if relative in reserved_article_files
            else None
        )
        if symlink_component is not None:
            findings.append(
                _finding(
                    "index.reserved-symlink",
                    relative,
                    f"Reserved article registry/policy files must be physical repository files; symlink component found at {symlink_component!r}.",
                )
            )
        if parts and parts[0] in DETACHED_CONTENT_ROOTS:
            findings.append(
                _finding(
                    "index.detached-content",
                    relative,
                    "Article sources, evidence, experiments, and exports must be registered inside one article family, not a detached top-level content root.",
                )
            )
        if len(parts) >= 2 and parts[0] == "articles" and relative not in reserved_article_files:
            article_files.append(relative)

    if repository_status == "governance_incubator":
        if articles:
            findings.append(
                _finding(
                    "index.status.mismatch",
                    "articles/INDEX.json",
                    "A governance_incubator must have an empty article registry; switch to active only with a complete registered family.",
                )
            )
        for relative in article_files:
            findings.append(
                _finding(
                    "index.unregistered-content",
                    relative,
                    "A governance_incubator cannot contain article-family content outside its empty registry.",
                )
            )
        return findings

    for relative in article_files:
        parts = PurePosixPath(relative).parts
        article_id = parts[1]
        if article_id not in registered_ids:
            findings.append(
                _finding(
                    "index.unregistered-content",
                    relative,
                    f"Article-family path belongs to unregistered article id {article_id!r}.",
                )
            )
        elif relative not in registered_paths[article_id]:
            findings.append(
                _finding(
                    "article.file.unregistered",
                    relative,
                    f"File is inside article {article_id!r} but is absent from its authority, review, export, and additional-artifact inventory.",
                )
            )
    return findings


def validate_repository(root: Path) -> list[dict[str, str]]:
    root = root.resolve()
    findings = _validate_privacy(root)
    index_path = root / "articles/INDEX.json"
    index_symlink = _first_symlink_component(root, "articles/INDEX.json")
    if index_symlink is not None:
        findings.append(
            _finding(
                "index.symlink",
                "articles/INDEX.json",
                f"The canonical article registry must be a physical repository file; symlink component found at {index_symlink!r}.",
            )
        )
        return sorted(findings, key=lambda item: (item["path"], item["code"], item["message"]))
    if not index_path.is_file():
        findings.append(
            _finding(
                "index.missing",
                "articles/INDEX.json",
                "The canonical article registry is missing.",
            )
        )
        return sorted(findings, key=lambda item: (item["path"], item["code"], item["message"]))

    index, error = _load_json(index_path)
    if error or not isinstance(index, dict):
        findings.append(
            _finding(
                "index.invalid",
                "articles/INDEX.json",
                f"The article registry is not valid JSON: {error or 'root must be an object'}.",
            )
        )
        return sorted(findings, key=lambda item: (item["path"], item["code"], item["message"]))

    if index.get("schema_version") != 1:
        findings.append(_finding("index.invalid", "articles/INDEX.json", "schema_version must be 1."))
    repository_status = index.get("repository_status")
    if repository_status not in REPOSITORY_STATUSES:
        findings.append(
            _finding(
                "index.invalid",
                "articles/INDEX.json",
                f"repository_status must be one of {sorted(REPOSITORY_STATUSES)}.",
            )
        )
    authority_note = index.get("authority_note")
    if not isinstance(authority_note, str) or not authority_note.strip():
        findings.append(
            _finding("index.invalid", "articles/INDEX.json", "authority_note must be nonblank.")
        )

    articles = index.get("articles")
    if not isinstance(articles, list):
        findings.append(_finding("index.invalid", "articles/INDEX.json", "articles must be an array."))
        articles = []
    if repository_status != "governance_incubator" and not articles:
        findings.append(
            _finding(
                "index.articles.empty",
                "articles/INDEX.json",
                "Only a governance_incubator may have no registered articles.",
            )
        )

    seen_ids: set[str] = set()
    for position, article in enumerate(articles):
        if isinstance(article, dict) and isinstance(article.get("id"), str):
            article_id = article["id"]
            if article_id in seen_ids:
                findings.append(
                    _finding(
                        "article.id.duplicate",
                        "articles/INDEX.json",
                        f"Article id {article_id!r} appears more than once.",
                    )
                )
            seen_ids.add(article_id)
        findings.extend(_validate_article(root, article, position))

    findings.extend(_validate_content_inventory(root, repository_status, articles))

    return sorted(findings, key=lambda item: (item["path"], item["code"], item["message"]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repository root (default: .)")
    args = parser.parse_args(argv)
    findings = validate_repository(args.root)
    for finding in findings:
        print(f"ERROR [{finding['code']}] {finding['path']}: {finding['message']}")
    if findings:
        print(f"Content repository validation failed with {len(findings)} finding(s).")
        return 1

    index = json.loads((args.root / "articles/INDEX.json").read_text(encoding="utf-8"))
    count = len(index["articles"])
    if index["repository_status"] == "governance_incubator":
        print(
            "Content repository structure passed: governance_incubator with "
            f"{count} registered article(s). Canonical content import remains BLOCKED."
        )
    else:
        print(f"Content repository structure passed: {count} registered article(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
