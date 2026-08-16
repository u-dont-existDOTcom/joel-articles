from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_article_architecture_maps import validate_architecture_maps


class ArticleArchitectureMapValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_index(self, articles: list[dict[str, object]], *, status: str) -> None:
        self.write(
            "articles/INDEX.json",
            json.dumps(
                {
                    "schema_version": 1,
                    "repository_status": status,
                    "authority_note": "Only registered, hash-bound files are article authority.",
                    "articles": articles,
                }
            )
            + "\n",
        )

    @staticmethod
    def codes(findings: list[dict[str, str]]) -> set[str]:
        return {finding["code"] for finding in findings}

    @staticmethod
    def incomplete_article(*, artifacts: list[dict[str, object]] | None = None) -> dict[str, object]:
        return {
            "id": "example",
            "title": "Example",
            "status": "working",
            "authority": {},
            "review": {},
            "publication_exports": [],
            "additional_artifacts": artifacts or [],
        }

    def test_repository_requires_article_meta_map(self) -> None:
        self.write_index([], status="governance_incubator")
        self.assertIn("index.meta-map.missing", self.codes(validate_architecture_maps(self.root)))

    def test_meta_map_requires_plain_mermaid_fence(self) -> None:
        self.write_index([], status="governance_incubator")
        self.write("articles/ARTICLE-META-MAP.md", "# Article meta-map\n\nNo graph yet.\n")
        self.assertIn("index.meta-map.invalid", self.codes(validate_architecture_maps(self.root)))

    def test_meta_map_must_be_physical_reserved_file(self) -> None:
        self.write_index([], status="governance_incubator")
        self.write(
            "detached-meta.md",
            '# Article meta-map\n\n```mermaid\nflowchart LR\n    empty["No registered articles yet"]\n```\n',
        )
        (self.root / "articles/ARTICLE-META-MAP.md").symlink_to("../detached-meta.md")
        self.assertIn("index.reserved-symlink", self.codes(validate_architecture_maps(self.root)))

    def test_registered_article_requires_architecture_map_artifact(self) -> None:
        self.write_index([self.incomplete_article()], status="active")
        self.write(
            "articles/ARTICLE-META-MAP.md",
            '# Article meta-map\n\n<!-- article-id: example -->\n\n```mermaid\nflowchart LR\n    example["Example"]\n```\n',
        )
        self.assertIn("article.architecture.missing", self.codes(validate_architecture_maps(self.root)))

    def test_architecture_map_must_use_canonical_path(self) -> None:
        self.write("articles/example/map.md", '# Map\n\n<!-- article-id: example -->\n\n```mermaid\nflowchart TD\n    a["A"]\n```\n')
        article = self.incomplete_article(
            artifacts=[
                {
                    "role": "architecture_map",
                    "path": "articles/example/map.md",
                    "sha256": "0" * 64,
                }
            ]
        )
        self.write_index([article], status="active")
        self.write(
            "articles/ARTICLE-META-MAP.md",
            '# Article meta-map\n\n<!-- article-id: example -->\n\n```mermaid\nflowchart LR\n    example["Example"]\n```\n',
        )
        self.assertIn("article.architecture.path", self.codes(validate_architecture_maps(self.root)))

    def test_architecture_map_requires_matching_marker_and_plain_mermaid_fence(self) -> None:
        content = "# Example architecture\n\nNo marker and no graph.\n"
        self.write("articles/example/ARCHITECTURE.md", content)
        article = self.incomplete_article(
            artifacts=[
                {
                    "role": "architecture_map",
                    "path": "articles/example/ARCHITECTURE.md",
                    "sha256": "0" * 64,
                }
            ]
        )
        self.write_index([article], status="active")
        self.write(
            "articles/ARTICLE-META-MAP.md",
            '# Article meta-map\n\n<!-- article-id: example -->\n\n```mermaid\nflowchart LR\n    example["Example"]\n```\n',
        )
        codes = self.codes(validate_architecture_maps(self.root))
        self.assertIn("article.architecture.marker", codes)
        self.assertIn("article.architecture.mermaid", codes)

    def test_meta_map_must_include_every_registered_article(self) -> None:
        self.write_index([self.incomplete_article()], status="active")
        self.write(
            "articles/ARTICLE-META-MAP.md",
            '# Article meta-map\n\n```mermaid\nflowchart LR\n    empty["No registered articles yet"]\n```\n',
        )
        self.assertIn("index.meta-map.article-missing", self.codes(validate_architecture_maps(self.root)))


if __name__ == "__main__":
    unittest.main()
