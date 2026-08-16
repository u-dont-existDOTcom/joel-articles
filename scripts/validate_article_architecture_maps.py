#!/usr/bin/env python3
"""Validate per-article Mermaid architecture maps and the repository article meta-map."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ARTICLE_META_MAP_PATH = "articles/ARTICLE-META-MAP.md"
ARCHITECTURE_ROLE = "architecture_map"
PLAIN_MERMAID_FENCE = "```mermaid\n"


def _finding(code: str, path: str, message: str) -> dict[str, str]:
    return {"code": code, "path": path, "message": message}


def _load_index(root: Path) -> tuple[dict[str, Any] | None, list[dict[str, str]]]:
    path = root / "articles/INDEX.json"
    if not path.is_file():
        return None, [
            _finding(
                "index.missing",
                "articles/INDEX.json",
                "The canonical article registry is missing.",
            )
        ]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return None, [
            _finding(
                "index.invalid",
                "articles/INDEX.json",
                f"The article registry is not valid JSON: {exc}.",
            )
        ]
    if not isinstance(data, dict):
        return None, [
            _finding(
                "index.invalid",
                "articles/INDEX.json",
                "The article registry root must be an object.",
            )
        ]
    return data, []


def _has_plain_mermaid_fence(text: str) -> bool:
    return PLAIN_MERMAID_FENCE in text


def _validate_meta_map(root: Path, articles: list[object]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    path = root / ARTICLE_META_MAP_PATH

    if path.is_symlink():
        findings.append(
            _finding(
                "index.reserved-symlink",
                ARTICLE_META_MAP_PATH,
                "The repository article meta-map must be a physical repository file, not a symlink.",
            )
        )
        return findings

    if not path.is_file():
        findings.append(
            _finding(
                "index.meta-map.missing",
                ARTICLE_META_MAP_PATH,
                "The repository-wide article meta-map is required.",
            )
        )
        return findings

    text = path.read_text(encoding="utf-8")
    if not _has_plain_mermaid_fence(text):
        findings.append(
            _finding(
                "index.meta-map.invalid",
                ARTICLE_META_MAP_PATH,
                "The article meta-map must contain a plain GitHub-compatible ```mermaid fence.",
            )
        )

    for article in articles:
        if not isinstance(article, dict):
            continue
        article_id = article.get("id")
        if not isinstance(article_id, str) or not article_id:
            continue
        marker = f"<!-- article-id: {article_id} -->"
        count = text.count(marker)
        if count != 1:
            findings.append(
                _finding(
                    "index.meta-map.article-missing",
                    ARTICLE_META_MAP_PATH,
                    f"Registered article {article_id!r} must appear exactly once as {marker!r}; found {count}.",
                )
            )
    return findings


def _architecture_artifacts(article: dict[str, object]) -> list[dict[str, object]]:
    artifacts = article.get("additional_artifacts")
    if not isinstance(artifacts, list):
        return []
    return [
        artifact
        for artifact in artifacts
        if isinstance(artifact, dict) and artifact.get("role") == ARCHITECTURE_ROLE
    ]


def _validate_article_map(root: Path, article: object) -> list[dict[str, str]]:
    if not isinstance(article, dict):
        return []
    article_id = article.get("id")
    if not isinstance(article_id, str) or not article_id:
        return []

    findings: list[dict[str, str]] = []
    artifacts = _architecture_artifacts(article)
    if not artifacts:
        return [
            _finding(
                "article.architecture.missing",
                "articles/INDEX.json",
                f"Article {article_id!r} requires one additional_artifact with role {ARCHITECTURE_ROLE!r}.",
            )
        ]
    if len(artifacts) != 1:
        return [
            _finding(
                "article.architecture.count",
                "articles/INDEX.json",
                f"Article {article_id!r} must register exactly one architecture map; found {len(artifacts)}.",
            )
        ]

    artifact = artifacts[0]
    expected_path = f"articles/{article_id}/ARCHITECTURE.md"
    relative = artifact.get("path")
    if relative != expected_path:
        findings.append(
            _finding(
                "article.architecture.path",
                "articles/INDEX.json",
                f"Article {article_id!r} architecture_map path must be {expected_path!r}, not {relative!r}.",
            )
        )
        return findings

    path = root / expected_path
    if path.is_symlink():
        findings.append(
            _finding(
                "article.architecture.symlink",
                expected_path,
                "Article architecture maps must be physical article-family files, not symlinks.",
            )
        )
        return findings
    if not path.is_file():
        findings.append(
            _finding(
                "article.architecture.file-missing",
                expected_path,
                "The registered article architecture map does not exist.",
            )
        )
        return findings

    text = path.read_text(encoding="utf-8")
    marker = f"<!-- article-id: {article_id} -->"
    if text.count(marker) != 1:
        findings.append(
            _finding(
                "article.architecture.marker",
                expected_path,
                f"The article architecture map must contain exactly one marker {marker!r}.",
            )
        )
    if not _has_plain_mermaid_fence(text):
        findings.append(
            _finding(
                "article.architecture.mermaid",
                expected_path,
                "The article architecture map must contain a plain GitHub-compatible ```mermaid fence.",
            )
        )
    return findings


def validate_architecture_maps(root: Path) -> list[dict[str, str]]:
    root = root.resolve()
    index, findings = _load_index(root)
    if index is None:
        return findings

    articles = index.get("articles")
    if not isinstance(articles, list):
        articles = []

    findings.extend(_validate_meta_map(root, articles))
    for article in articles:
        findings.extend(_validate_article_map(root, article))
    return sorted(findings, key=lambda item: (item["path"], item["code"], item["message"]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repository root (default: .)")
    args = parser.parse_args(argv)
    findings = validate_architecture_maps(args.root)
    for finding in findings:
        print(f"ERROR [{finding['code']}] {finding['path']}: {finding['message']}")
    if findings:
        print(f"Article architecture map validation failed with {len(findings)} finding(s).")
        return 1
    print("Article architecture maps passed structural validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
