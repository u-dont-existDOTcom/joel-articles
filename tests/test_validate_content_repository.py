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
                "owner_review": {
                    "status": "confirmed",
                    "evidence": "Owner-reviewed import decision.",
                },
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
            "additional_artifacts": [],
        }

    @staticmethod
    def codes(findings: list[dict[str, str]]) -> set[str]:
        return {finding["code"] for finding in findings}

    def test_truthful_empty_incubator_is_valid(self) -> None:
        self.write_index([])
        self.assertEqual([], validate_repository(self.root))

    def test_article_registry_must_not_be_a_symlink(self) -> None:
        content = json.dumps(
            {
                "schema_version": 1,
                "repository_status": "governance_incubator",
                "authority_note": "Detached registry.",
                "articles": [],
            }
        ) + "\n"
        self.write("detached-index.json", content)
        articles = self.root / "articles"
        articles.mkdir(parents=True, exist_ok=True)
        (articles / "INDEX.json").symlink_to("../detached-index.json")
        self.assertIn("index.symlink", self.codes(validate_repository(self.root)))

    def test_article_registry_parent_must_not_be_a_symlink(self) -> None:
        content = json.dumps(
            {
                "schema_version": 1,
                "repository_status": "governance_incubator",
                "authority_note": "Registry behind a symlinked authority root.",
                "articles": [],
            }
        ) + "\n"
        self.write("some-articles/INDEX.json", content)
        (self.root / "articles").symlink_to("some-articles", target_is_directory=True)
        self.assertIn("index.symlink", self.codes(validate_repository(self.root)))

    def test_reserved_article_policy_must_not_be_a_symlink(self) -> None:
        self.write_index([])
        self.write("detached-agents.md", "# Detached policy\n")
        (self.root / "articles/AGENTS.md").symlink_to("../detached-agents.md")
        self.assertIn("index.reserved-symlink", self.codes(validate_repository(self.root)))

    def test_non_incubator_cannot_have_an_empty_article_registry(self) -> None:
        self.write_index([], status="active")
        self.assertIn("index.articles.empty", self.codes(validate_repository(self.root)))

    def test_incubator_rejects_unregistered_article_content(self) -> None:
        self.write_index([])
        self.write("articles/example/master.md", "# Detached candidate\n")
        self.assertIn("index.unregistered-content", self.codes(validate_repository(self.root)))

    def test_incubator_cannot_contain_a_registered_article(self) -> None:
        article = self.valid_article()
        self.write_index([article])
        self.assertIn("index.status.mismatch", self.codes(validate_repository(self.root)))

    def test_active_article_rejects_an_unregistered_family_file(self) -> None:
        article = self.valid_article()
        self.write("articles/example/detached-notes.md", "not registered\n")
        self.write_index([article], status="active")
        self.assertIn("article.file.unregistered", self.codes(validate_repository(self.root)))

    def test_additional_artifact_registers_an_extra_family_file(self) -> None:
        article = self.valid_article()
        content = "approved supporting artifact\n"
        self.write("articles/example/supporting-note.md", content)
        article["additional_artifacts"] = [
            {
                "role": "supporting_note",
                "path": "articles/example/supporting-note.md",
                "sha256": self.sha256(content),
            }
        ]
        self.write_index([article], status="active")
        self.assertEqual([], validate_repository(self.root))

    def test_detached_top_level_source_family_is_rejected(self) -> None:
        self.write_index([])
        self.write("sources/private-interview.md", "detached source\n")
        self.assertIn("index.detached-content", self.codes(validate_repository(self.root)))

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

    def test_referenced_file_must_not_cross_boundary_through_symlink(self) -> None:
        article = self.valid_article()
        outside = "# Shared mutable file\n"
        self.write("README.md", outside)
        master_path = self.root / "articles/example/master.md"
        master_path.unlink()
        master_path.symlink_to("../../README.md")
        article["authority"]["master"]["sha256"] = self.sha256(outside)  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.path.symlink", self.codes(validate_repository(self.root)))

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

    def test_owner_final_article_requires_confirmed_owner_lock_review(self) -> None:
        article = self.valid_article()
        locks_path = self.root / "articles/example/OWNER-LOCKS.json"
        locks = json.loads(locks_path.read_text(encoding="utf-8"))
        locks["owner_review"] = {"status": "pending", "evidence": "Awaiting owner."}
        updated = json.dumps(locks, indent=2) + "\n"
        self.write("articles/example/OWNER-LOCKS.json", updated)
        article["authority"]["owner_locks"]["sha256"] = self.sha256(updated)  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.owner-lock.unconfirmed", self.codes(validate_repository(self.root)))

    def test_source_evidence_must_match_article_and_schema(self) -> None:
        article = self.valid_article()
        evidence = '{"schema_version": 1, "article_id": "other", "claims": []}\n'
        self.write("articles/example/SOURCE-EVIDENCE.json", evidence)
        article["authority"]["source_evidence"]["sha256"] = self.sha256(evidence)  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.evidence.invalid", self.codes(validate_repository(self.root)))

    def test_review_file_status_must_match_registry_status(self) -> None:
        article = self.valid_article()
        citations = '{"schema_version": 1, "article_id": "example", "status": "pending", "claims": []}\n'
        self.write("articles/example/CITATIONS.json", citations)
        article["review"]["citations"]["sha256"] = self.sha256(citations)  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.review.mismatch", self.codes(validate_repository(self.root)))

    def test_protected_function_requires_unique_id_and_description(self) -> None:
        article = self.valid_article()
        locks_path = self.root / "articles/example/OWNER-LOCKS.json"
        locks = json.loads(locks_path.read_text(encoding="utf-8"))
        locks["protected_functions"] = [{"id": "function-1", "description": ""}]
        updated = json.dumps(locks, indent=2) + "\n"
        self.write("articles/example/OWNER-LOCKS.json", updated)
        article["authority"]["owner_locks"]["sha256"] = self.sha256(updated)  # type: ignore[index]
        self.write_index([article], status="active")
        self.assertIn("article.owner-lock.invalid", self.codes(validate_repository(self.root)))

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
