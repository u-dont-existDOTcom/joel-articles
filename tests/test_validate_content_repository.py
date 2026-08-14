from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_content_repository import validate_repository


class ContentRepositoryValidationTests(unittest.TestCase):
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

    @staticmethod
    def sha256(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def write_index(self, articles: list[dict[str, object]], *, status: str = "governance_incubator") -> None:
        self.write(
            "articles/INDEX.json",
            json.dumps(
                {
                    "schema_version": 1,
                    "repository_status": status,
                    "authority_note": "Only registered, hash-bound files are article authority.",
                    "articles": articles,
                },
                indent=2,
            )
            + "\n",
        )

    def valid_article(self) -> dict[str, object]:
        master = "# Example\n\nOwner-locked sentence.\n"
        locks = json.dumps(
            {
                "schema_version": 1,
                "article_id": "example",
                "locked_passages": [
                    {
                        "id": "lock-1",
                        "text": "Owner-locked sentence.",
                        "sha256": self.sha256("Owner-locked sentence."),
                    }
                ],
                "protected_functions": [
                    {"id": "function-1", "description": "Preserve the owner's conclusion."}
                ],
            },
            indent=2,
        ) + "\n"
        evidence = '{"schema_version": 1, "article_id": "example", "claims": []}\n'
        ideas = "# Unincorporated ideas\n\nNone recorded.\n"
        state = "# Article current state\n\n## Goal\n\n## Authority / baseline\n\n## Completed\n\n## Current checkpoint\n\n## Remaining\n\n## Blockers / unresolved\n\n## Evidence / artifacts\n\n## Next safe action\n"
        citations = '{"schema_version": 1, "article_id": "example", "status": "verified", "claims": []}\n'
        detector = '{"schema_version": 1, "article_id": "example", "status": "not_run", "runs": []}\n'
        editorial = '{"schema_version": 1, "article_id": "example", "status": "passed", "checks": []}\n'

        files = {
            "master": ("articles/example/master.md", master),
            "owner_locks": ("articles/example/OWNER-LOCKS.json", locks),
            "source_evidence": ("articles/example/SOURCE-EVIDENCE.json", evidence),
            "unincorporated_ideas": ("articles/example/UNINCORPORATED-IDEAS.md", ideas),
            "current_state": ("articles/example/CURRENT-STATE.md", state),
            "citations": ("articles/example/CITATIONS.json", citations),
            "detector": ("articles/example/DETECTOR-EVIDENCE.json", detector),
            "editorial": ("articles/example/EDITORIAL-STATUS.json", editorial),
        }
        refs: dict[str, dict[str, str]] = {}
        for key, (path, content) in files.items():
            self.write(path, content)
            refs[key] = {"path": path, "sha256": self.sha256(content)}

        return {
            "id": "example",
            "title": "Example",
            "status": "owner_final",
            "authority": {
                key: refs[key]
                for key in (
                    "master",
                    "owner_locks",
                    "source_evidence",
                    "unincorporated_ideas",
                    "current_state",
                )
            },
            "review": {
                "citations": {**refs["citations"], "status": "verified"},
                "detector": {**refs["detector"], "status": "not_run"},
                "editorial": {**refs["editorial"], "status": "passed"},
            },
            "publication_exports": [],
        }

    @staticmethod
    def codes(findings: list[dict[str, str]]) -> set[str]:
        return {finding["code"] for finding in findings}

    def test_truthful_empty_incubator_is_valid(self) -> None:
        self.write_index([])
        self.assertEqual([], validate_repository(self.root))

    def test_non_incubator_cannot_have_an_empty_article_registry(self) -> None:
        self.write_index([], status="active")
        self.assertIn("index.articles.empty", self.codes(validate_repository(self.root)))

    def test_article_requires_every_authority_and_review_record(self) -> None:
        article = self.valid_article()
        del article["authority"]["owner_locks"]  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.field.missing", self.codes(validate_repository(self.root)))

    def test_referenced_file_must_exist(self) -> None:
        article = self.valid_article()
        Path(self.root / "articles/example/master.md").unlink()
        self.write_index([article], status="active")
        self.assertIn("article.path.missing", self.codes(validate_repository(self.root)))

    def test_referenced_file_hash_must_match(self) -> None:
        article = self.valid_article()
        self.write("articles/example/master.md", "# Quiet substitution\n")
        self.write_index([article], status="active")
        self.assertIn("article.hash.mismatch", self.codes(validate_repository(self.root)))

    def test_owner_locked_passage_must_remain_in_master(self) -> None:
        article = self.valid_article()
        replacement = "# Example\n\nSentence removed.\n"
        self.write("articles/example/master.md", replacement)
        article["authority"]["master"]["sha256"] = self.sha256(replacement)  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.owner-lock.missing", self.codes(validate_repository(self.root)))

    def test_owner_lock_hash_must_match_exact_text(self) -> None:
        article = self.valid_article()
        locks_path = self.root / "articles/example/OWNER-LOCKS.json"
        locks = json.loads(locks_path.read_text(encoding="utf-8"))
        locks["locked_passages"][0]["sha256"] = "0" * 64
        updated = json.dumps(locks, indent=2) + "\n"
        self.write("articles/example/OWNER-LOCKS.json", updated)
        article["authority"]["owner_locks"]["sha256"] = self.sha256(updated)  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.owner-lock.hash-mismatch", self.codes(validate_repository(self.root)))

    def test_owner_final_article_requires_editorial_pass(self) -> None:
        article = self.valid_article()
        article["review"]["editorial"]["status"] = "pending"  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.review.incomplete", self.codes(validate_repository(self.root)))

    def test_publication_export_requires_destination_and_source_authority(self) -> None:
        article = self.valid_article()
        article["status"] = "published"
        article["publication_exports"] = [{"path": "articles/example/master.md"}]
        self.write_index([article], status="active")
        self.assertIn("article.export.invalid", self.codes(validate_repository(self.root)))

    def test_private_staging_paths_are_forbidden(self) -> None:
        self.write_index([])
        self.write("incoming-private/notes.txt", "must not be committed\n")
        self.assertIn("privacy.forbidden-path", self.codes(validate_repository(self.root)))


if __name__ == "__main__":
    unittest.main()
