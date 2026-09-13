from __future__ import annotations

import contextlib
import copy
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "somatic_intro_progress_controller",
    ROOT / "scripts" / "somatic_intro_progress_controller.py",
)
assert SPEC and SPEC.loader
CONTROLLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CONTROLLER)


class SomaticIntroProgressControllerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="somatic-progress-controller-")
        self.root = Path(self.temp.name)
        self.controller_dir = Path("controller")
        self.semantic_task = Path("authority/semantic-task.md")
        self.lesson_contract = Path("authority/active-lessons.md")
        (self.root / "authority").mkdir(parents=True)
        (self.root / self.semantic_task).write_text(
            "SYNTHETIC SEMANTIC AUTHORITY\n", encoding="utf-8"
        )
        (self.root / self.lesson_contract).write_text(
            "SYNTHETIC ACTIVE LESSON CONTRACT\n", encoding="utf-8"
        )
        CONTROLLER.initialize_controller(
            self.root,
            self.controller_dir,
            semantic_task=self.semantic_task,
            lesson_contract=self.lesson_contract,
            next_search_target={
                "id": "synthetic-search-1",
                "kind": "GENERATION",
                "description": "Produce one disposable synthetic sample.",
            },
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    @property
    def controller(self) -> Path:
        return self.root / self.controller_dir

    def register(self, sample_id: str, text: str) -> dict[str, object]:
        input_path = self.root / f"{sample_id}.txt"
        input_path.write_text(text, encoding="utf-8")
        return CONTROLLER.register_sample(
            self.root,
            input_path,
            sample_id,
            controller_dir=self.controller_dir,
            writer_identity=f"writer-{sample_id}",
            writer_context=f"writer-context-{sample_id}",
            created_at="2026-08-31T12:00:00Z",
        )

    def receipt(
        self,
        sample_id: str,
        *,
        receipt_id: str | None = None,
        hard_constraints: str = "PASS",
        comparison: str = "DOMINATES",
        promotion: str = "ALLOW",
        regressions: list[str] | None = None,
        improvements: list[dict[str, str]] | None = None,
        cleared_after: list[str] | None = None,
    ) -> dict[str, object]:
        state = CONTROLLER.load_frontier(self.root, self.controller_dir)
        record = json.loads(
            (self.controller / "samples" / sample_id / "record.json").read_text(
                encoding="utf-8"
            )
        )
        default_improvement = f"improved-{sample_id}"
        if improvements is None:
            improvements = [
                {
                    "dimension_id": default_improvement,
                    "description": f"Synthetic improvement for {sample_id}.",
                }
            ]
        if cleared_after is None:
            cleared_after = list(state["cleared_dimensions"])
            cleared_after.extend(
                item["dimension_id"]
                for item in improvements
                if item["dimension_id"] not in cleared_after
            )
        return {
            "schema_version": 1,
            "receipt_id": receipt_id or f"receipt-{sample_id}",
            "candidate": {
                "sample_id": sample_id,
                "sha256": record["candidate_sha256"],
            },
            "current_frontier": CONTROLLER._frontier_binding(state),
            "semantic_task": state["semantic_task"],
            "active_lesson_contract": state["active_lesson_contract"],
            "hard_constraints": hard_constraints,
            "regressions": regressions or [],
            "improvements": improvements,
            "cleared_dimensions_after": cleared_after,
            "unresolved_defects": [
                {
                    "rank": 1,
                    "dimension_id": f"unresolved-{sample_id}",
                    "description": f"Synthetic unresolved defect for {sample_id}.",
                }
            ],
            "strongest_blocking_defect": "No blocking defect in this synthetic fixture.",
            "strongest_known_generative_failure_pattern_after": (
                f"Synthetic failure pattern after {sample_id}."
            ),
            "frontier_comparison": comparison,
            "next_search_target": {
                "id": f"search-after-{sample_id}",
                "kind": "GENERATION",
                "description": f"Run one changed synthetic search after {sample_id}.",
            },
            "promotion": promotion,
            "verifier": {
                "identity": f"verifier-{sample_id}",
                "context_id": f"verifier-context-{sample_id}",
            },
        }

    def record_receipt(self, receipt: dict[str, object]) -> dict[str, str]:
        path = self.root / f"{receipt.get('receipt_id', 'invalid')}.json"
        path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        return CONTROLLER.record_verifier_receipt(
            self.root, path, controller_dir=self.controller_dir
        )

    def promote_first(self, sample_id: str = "alpha") -> dict[str, object]:
        self.register(sample_id, f"SYNTHETIC PROMOTABLE SAMPLE {sample_id}\n")
        receipt = self.receipt(sample_id)
        self.record_receipt(receipt)
        return CONTROLLER.attempt_promotion(
            self.root, receipt["receipt_id"], controller_dir=self.controller_dir
        )

    def frontier_bytes(self) -> bytes:
        return (self.controller / "frontier.json").read_bytes()

    def test_newer_rejected_sample_cannot_replace_frontier(self) -> None:
        promoted = self.promote_first()
        self.register("beta", "SYNTHETIC REJECTED SAMPLE BETA\n")
        receipt = self.receipt(
            "beta",
            hard_constraints="FAIL",
            comparison="REGRESSES",
            promotion="BLOCK",
            regressions=[promoted["cleared_dimensions"][0]],
            cleared_after=[],
        )
        self.record_receipt(receipt)
        before = self.frontier_bytes()
        with self.assertRaises(CONTROLLER.ControllerError):
            CONTROLLER.attempt_promotion(
                self.root, receipt["receipt_id"], controller_dir=self.controller_dir
            )
        self.assertEqual(self.frontier_bytes(), before)
        current = CONTROLLER.load_frontier(self.root, self.controller_dir)
        self.assertEqual(current["best_promoted_owner_facing_candidate"]["sample_id"], "alpha")
        status = json.loads(
            (self.controller / "samples/beta/status.json").read_text(encoding="utf-8")
        )
        self.assertEqual(status["current_status"], "REJECTED")

    def test_sample_without_verifier_receipt_cannot_promote(self) -> None:
        self.register("alpha", "SYNTHETIC UNVERIFIED SAMPLE\n")
        before = self.frontier_bytes()
        with self.assertRaises(CONTROLLER.ControllerError):
            CONTROLLER.attempt_promotion(
                self.root, "missing-receipt", controller_dir=self.controller_dir
            )
        self.assertEqual(self.frontier_bytes(), before)

    def test_candidate_hash_mismatch_blocks_promotion(self) -> None:
        self.register("alpha", "SYNTHETIC HASH-BOUND SAMPLE\n")
        receipt = self.receipt("alpha")
        self.record_receipt(receipt)
        (self.controller / "samples/alpha/candidate.txt").write_text(
            "SYNTHETIC TAMPERED SAMPLE\n", encoding="utf-8"
        )
        before = self.frontier_bytes()
        with self.assertRaises(CONTROLLER.ControllerError):
            CONTROLLER.attempt_promotion(
                self.root, receipt["receipt_id"], controller_dir=self.controller_dir
            )
        self.assertEqual(self.frontier_bytes(), before)

    def test_stale_task_or_lesson_contract_blocks_promotion(self) -> None:
        for changed_path in (self.semantic_task, self.lesson_contract):
            with self.subTest(changed_path=changed_path):
                with self.temp_fixture_clone() as cloned:
                    cloned.register("alpha", "SYNTHETIC STALE-AUTHORITY SAMPLE\n")
                    receipt = cloned.receipt("alpha")
                    cloned.record_receipt(receipt)
                    before = cloned.frontier_bytes()
                    (cloned.root / changed_path).write_text("CHANGED AUTHORITY\n", encoding="utf-8")
                    with self.assertRaises(CONTROLLER.ControllerError):
                        CONTROLLER.attempt_promotion(
                            cloned.root,
                            receipt["receipt_id"],
                            controller_dir=cloned.controller_dir,
                        )
                    self.assertEqual(cloned.frontier_bytes(), before)

    @contextlib.contextmanager
    def temp_fixture_clone(self):
        clone = SomaticIntroProgressControllerTests(methodName="runTest")
        clone.setUp()
        try:
            yield clone
        finally:
            clone.tearDown()

    def test_allow_still_blocks_regression_of_cleared_dimension(self) -> None:
        promoted = self.promote_first()
        cleared = promoted["cleared_dimensions"][0]
        self.register("beta", "SYNTHETIC REGRESSIVE SAMPLE\n")
        receipt = self.receipt(
            "beta",
            comparison="DOMINATES",
            promotion="ALLOW",
            regressions=[cleared],
            cleared_after=[],
        )
        self.record_receipt(receipt)
        before = self.frontier_bytes()
        with self.assertRaises(CONTROLLER.ControllerError):
            CONTROLLER.attempt_promotion(
                self.root, receipt["receipt_id"], controller_dir=self.controller_dir
            )
        self.assertEqual(self.frontier_bytes(), before)

    def test_nonadvancing_comparisons_never_replace_existing_frontier(self) -> None:
        self.promote_first()
        for comparison in ("REGRESSES", "INCOMPARABLE", "NONDOMINATED"):
            with self.subTest(comparison=comparison):
                sample_id = comparison.lower()
                self.register(sample_id, f"SYNTHETIC {comparison} SAMPLE\n")
                regressions = ["unresolved-comparison"] if comparison == "REGRESSES" else []
                receipt = self.receipt(
                    sample_id,
                    comparison=comparison,
                    promotion="ALLOW",
                    regressions=regressions,
                )
                self.record_receipt(receipt)
                before = self.frontier_bytes()
                with self.assertRaises(CONTROLLER.ControllerError):
                    CONTROLLER.attempt_promotion(
                        self.root,
                        receipt["receipt_id"],
                        controller_dir=self.controller_dir,
                    )
                self.assertEqual(self.frontier_bytes(), before)
                self.assertEqual(
                    CONTROLLER.load_frontier(self.root, self.controller_dir)[
                        "best_promoted_owner_facing_candidate"
                    ]["sample_id"],
                    "alpha",
                )

    def test_valid_dominates_receipt_promotes_atomically(self) -> None:
        first = self.promote_first()
        self.register("beta", "SYNTHETIC DOMINATING SAMPLE BETA\n")
        receipt = self.receipt("beta")
        self.record_receipt(receipt)
        before = self.frontier_bytes()
        updated = CONTROLLER.attempt_promotion(
            self.root, receipt["receipt_id"], controller_dir=self.controller_dir
        )
        self.assertNotEqual(self.frontier_bytes(), before)
        self.assertEqual(updated["best_promoted_owner_facing_candidate"]["sample_id"], "beta")
        self.assertGreater(updated["revision"], first["revision"])
        self.assertEqual(
            CONTROLLER.emit_owner_facing_candidate(self.root, self.controller_dir),
            b"SYNTHETIC DOMINATING SAMPLE BETA\n",
        )

    def test_failed_promotion_preserves_frontier_bytes(self) -> None:
        self.promote_first()
        self.register("beta", "SYNTHETIC NONDOMINATED SAMPLE\n")
        receipt = self.receipt("beta", comparison="NONDOMINATED")
        self.record_receipt(receipt)
        before = self.frontier_bytes()
        with self.assertRaises(CONTROLLER.ControllerError):
            CONTROLLER.attempt_promotion(
                self.root, receipt["receipt_id"], controller_dir=self.controller_dir
            )
        self.assertEqual(self.frontier_bytes(), before)

    def test_writer_packet_excludes_rejected_candidate_and_rationale(self) -> None:
        self.register("rejected", "REJECTED-CANDIDATE-SENTINEL\n")
        receipt = self.receipt(
            "rejected",
            hard_constraints="FAIL",
            comparison="REGRESSES",
            promotion="BLOCK",
            regressions=["synthetic-regression"],
            cleared_after=[],
        )
        receipt["strongest_blocking_defect"] = "REJECTED-RATIONALE-SENTINEL"
        self.record_receipt(receipt)
        packet_text = json.dumps(
            CONTROLLER.build_writer_packet(self.root, self.controller_dir), sort_keys=True
        )
        self.assertNotIn("REJECTED-CANDIDATE-SENTINEL", packet_text)
        self.assertNotIn("REJECTED-RATIONALE-SENTINEL", packet_text)
        self.assertEqual(
            CONTROLLER.build_writer_packet(self.root, self.controller_dir)[
                "candidate_prose_policy"
            ],
            "NO_PRIOR_CANDIDATE_PROSE_INCLUDED",
        )

    def test_verifier_packet_contains_exact_candidate_and_frontier_identities(self) -> None:
        promoted = self.promote_first()
        self.register("beta", "SYNTHETIC NEW CANDIDATE BETA\n")
        packet = CONTROLLER.build_verifier_packet(
            self.root, "beta", self.controller_dir
        )
        self.assertEqual(packet["candidate"]["content"], "SYNTHETIC NEW CANDIDATE BETA\n")
        self.assertEqual(
            packet["current_promoted_frontier"]["sample_id"],
            promoted["best_promoted_owner_facing_candidate"]["sample_id"],
        )
        self.assertEqual(
            packet["required_receipt"]["current_frontier"],
            CONTROLLER._frontier_binding(promoted),
        )

    def test_missing_required_receipt_field_fails_closed(self) -> None:
        self.register("alpha", "SYNTHETIC INCOMPLETE-RECEIPT SAMPLE\n")
        receipt = self.receipt("alpha")
        del receipt["hard_constraints"]
        with self.assertRaises(CONTROLLER.ControllerError):
            self.record_receipt(receipt)
        self.assertIsNone(
            CONTROLLER.load_frontier(self.root, self.controller_dir)[
                "best_promoted_owner_facing_candidate"
            ]
        )

    def test_writer_and_verifier_context_must_be_distinguishable(self) -> None:
        self.register("alpha", "SYNTHETIC SAME-CONTEXT SAMPLE\n")
        receipt = self.receipt("alpha")
        receipt["verifier"] = {
            "identity": "different-label-does-not-matter",
            "context_id": "writer-context-alpha",
        }
        with self.assertRaises(CONTROLLER.ControllerError):
            self.record_receipt(receipt)

    def test_repeated_registration_receipt_and_promotion_are_idempotent(self) -> None:
        first_record = self.register("alpha", "SYNTHETIC IDEMPOTENT SAMPLE\n")
        second_record = self.register("alpha", "SYNTHETIC IDEMPOTENT SAMPLE\n")
        self.assertEqual(first_record, second_record)
        receipt = self.receipt("alpha")
        first_identity = self.record_receipt(receipt)
        second_identity = self.record_receipt(copy.deepcopy(receipt))
        self.assertEqual(first_identity, second_identity)
        first_state = CONTROLLER.attempt_promotion(
            self.root, receipt["receipt_id"], controller_dir=self.controller_dir
        )
        state_bytes = self.frontier_bytes()
        second_state = CONTROLLER.attempt_promotion(
            self.root, receipt["receipt_id"], controller_dir=self.controller_dir
        )
        self.assertEqual(first_state, second_state)
        self.assertEqual(self.frontier_bytes(), state_bytes)
        sample_lines = (self.controller / "history/samples.jsonl").read_text(
            encoding="utf-8"
        ).splitlines()
        receipt_lines = (self.controller / "history/adjudications.jsonl").read_text(
            encoding="utf-8"
        ).splitlines()
        promotion_lines = (self.controller / "history/promotions.jsonl").read_text(
            encoding="utf-8"
        ).splitlines()
        self.assertEqual(len(sample_lines), 1)
        self.assertEqual(len(receipt_lines), 1)
        self.assertEqual(len(promotion_lines), 1)

    def test_conflicting_sample_replay_is_rejected(self) -> None:
        self.register("alpha", "SYNTHETIC ORIGINAL SAMPLE\n")
        with self.assertRaises(CONTROLLER.ControllerError):
            self.register("alpha", "SYNTHETIC CONFLICTING SAMPLE\n")

    def test_initial_review_target_blocks_writer_packet(self) -> None:
        separate = tempfile.TemporaryDirectory(prefix="somatic-controller-review-")
        try:
            root = Path(separate.name)
            (root / "authority").mkdir()
            (root / self.semantic_task).write_text("TASK\n", encoding="utf-8")
            (root / self.lesson_contract).write_text("LESSONS\n", encoding="utf-8")
            CONTROLLER.initialize_controller(
                root,
                Path("controller"),
                semantic_task=self.semantic_task,
                lesson_contract=self.lesson_contract,
            )
            with self.assertRaises(CONTROLLER.ControllerError):
                CONTROLLER.build_writer_packet(root, Path("controller"))
        finally:
            separate.cleanup()

    def test_search_decision_changes_search_state_but_not_candidate_frontier(self) -> None:
        promoted = self.promote_first()
        state = CONTROLLER.load_frontier(self.root, self.controller_dir)
        decision = {
            "schema_version": 1,
            "decision_id": "synthetic-search-decision",
            "current_frontier": CONTROLLER._frontier_binding(state),
            "semantic_task": state["semantic_task"],
            "active_lesson_contract": state["active_lesson_contract"],
            "cleared_dimensions": state["cleared_dimensions"],
            "unresolved_defects": [
                {
                    "rank": 1,
                    "dimension_id": "new-search-defect",
                    "description": "Synthetic externally supplied search defect.",
                }
            ],
            "strongest_known_generative_failure_pattern": "Synthetic external pattern.",
            "next_search_target": {
                "id": "changed-search-target",
                "kind": "GENERATION",
                "description": "Run one different synthetic search operation.",
            },
            "decision_maker": {
                "identity": "reasoning-chat",
                "context_id": "reasoning-chat-context",
            },
            "source_verifier_receipt": None,
        }
        decision_path = self.root / "search-decision.json"
        decision_path.write_text(json.dumps(decision), encoding="utf-8")
        updated = CONTROLLER.apply_search_decision(
            self.root, decision_path, controller_dir=self.controller_dir
        )
        self.assertEqual(
            updated["best_promoted_owner_facing_candidate"],
            promoted["best_promoted_owner_facing_candidate"],
        )
        self.assertEqual(updated["next_search_target"]["id"], "changed-search-target")
        packet = CONTROLLER.build_writer_packet(self.root, self.controller_dir)
        self.assertEqual(packet["next_search_target"]["id"], "changed-search-target")
        state_bytes = self.frontier_bytes()
        replayed = CONTROLLER.apply_search_decision(
            self.root, decision_path, controller_dir=self.controller_dir
        )
        self.assertEqual(replayed, updated)
        self.assertEqual(self.frontier_bytes(), state_bytes)
        self.assertEqual(
            len(
                (self.controller / "history/controller-decisions.jsonl")
                .read_text(encoding="utf-8")
                .splitlines()
            ),
            1,
        )

    def test_completed_promotion_replay_repairs_status_and_history_projection(self) -> None:
        state = self.promote_first()
        receipt_id = state["last_promotion_receipt"]["receipt_id"]
        status_path = self.controller / "samples/alpha/status.json"
        status = json.loads(status_path.read_text(encoding="utf-8"))
        status["current_status"] = "ADJUDICATED"
        status_path.write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
        history_path = self.controller / "history/promotions.jsonl"
        history_path.unlink()
        replayed = CONTROLLER.attempt_promotion(
            self.root, receipt_id, controller_dir=self.controller_dir
        )
        self.assertEqual(replayed, state)
        repaired_status = json.loads(status_path.read_text(encoding="utf-8"))
        self.assertEqual(repaired_status["current_status"], "PROMOTED")
        self.assertEqual(len(history_path.read_text(encoding="utf-8").splitlines()), 1)

    def test_cli_composition_executes_register_verify_promote_and_emit(self) -> None:
        script = ROOT / "scripts/somatic_intro_progress_controller.py"
        common = [
            "python",
            str(script),
            "--root",
            str(self.root),
            "--controller-dir",
            str(self.controller_dir),
        ]
        candidate = self.root / "cli-candidate.txt"
        candidate.write_text("SYNTHETIC CLI CANDIDATE\n", encoding="utf-8")
        registered = subprocess.run(
            common
            + [
                "register-sample",
                "--sample-id",
                "cli-sample",
                "--candidate",
                str(candidate),
                "--created-at",
                "2026-08-31T12:00:00Z",
                "--writer-identity",
                "cli-writer",
                "--writer-context",
                "cli-writer-context",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(registered.returncode, 0, registered.stderr)
        receipt = self.receipt("cli-sample", receipt_id="cli-receipt")
        receipt_path = self.root / "cli-receipt-input.json"
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        recorded = subprocess.run(
            common + ["record-verifier-receipt", "--receipt", str(receipt_path)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(recorded.returncode, 0, recorded.stderr)
        promoted = subprocess.run(
            common + ["attempt-promotion", "--receipt-id", "cli-receipt"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(promoted.returncode, 0, promoted.stderr)
        owner_output = self.root / "owner-facing.txt"
        emitted = subprocess.run(
            common
            + [
                "emit-owner-facing-candidate",
                "--output",
                str(owner_output),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(emitted.returncode, 0, emitted.stderr)
        self.assertEqual(owner_output.read_text(encoding="utf-8"), "SYNTHETIC CLI CANDIDATE\n")


if __name__ == "__main__":
    unittest.main()
