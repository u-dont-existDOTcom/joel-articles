from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_humanization_control",
    ROOT / "scripts" / "validate_humanization_control.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
validate_control = MODULE.validate_control


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


class ControlFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        source = b"frozen before\nold generated realization with enough distinct words to detect a verbatim source prose leak now\nfrozen after\n"
        (root / "source.md").write_bytes(source)
        self.writer = {
            "schema_version": 1,
            "packet_id": "writer-1",
            "writer_role": "chat_reasoning",
            "executor_role": "mechanical_only",
            "source_sha256": digest(source),
            "target_span_ids": ["AI-1"],
            "authorized_exact_owner_language": [],
            "semantic_units": [
                {
                    "unit_id": "SEM-1",
                    "proposition": "A prior hazard can remain active in bodily response.",
                    "function": "Preserve the core claim.",
                    "provenance_plane": "general claim",
                    "certainty": "may",
                    "attribution_constraint": "Do not invent autobiography.",
                }
            ],
            "hard_constraints": ["Write from semantics only."],
        }
        self.ledger = {
            "schema_version": 1,
            "ledger_id": "ledger-1",
            "validator_role": "separate_chat_adversarial_validator",
            "writer_access": "withheld",
            "strategy_families": [
                {
                    "family_id": "RS-1",
                    "structural_signature": "Old conceptual order under new words.",
                    "evidence_refs": ["source paragraph"],
                    "automatic_reject_if": "The old structure recurs.",
                    "surface_changes_do_not_cure": ["contractions"],
                }
            ],
            "mandatory_structural_checks": sorted(MODULE.MANDATORY_STRUCTURAL_CHECKS),
            "invalid_change_justifications": sorted(MODULE.MANDATORY_INVALID_JUSTIFICATIONS),
        }
        self._write_packets()
        self.control = {
            "schema_version": 1,
            "control_id": "control-1",
            "workflow_state": "prewrite_ready",
            "role_boundary": {
                "reasoning_owner": "Chat",
                "mechanical_executor": "Codex",
                "writer_context_id": None,
                "rule": "Chat reasons and Codex executes mechanically.",
            },
            "source": {
                "path": "source.md",
                "revision": "abc123",
                "sha256": digest(source),
                "line_count": 3,
                "changed_scope": "line 2",
            },
            "provenance_spans": [
                {
                    "span_id": "UNKNOWN-1",
                    "classification": "UNKNOWN",
                    "line_start": 1,
                    "line_end": 1,
                    "sha256": digest(b"frozen before\n"),
                    "frozen": True,
                    "writer_access": "none",
                    "authority_note": "Outside scope.",
                },
                {
                    "span_id": "AI-1",
                    "classification": "AI_TARGET",
                    "line_start": 2,
                    "line_end": 2,
                    "sha256": digest(b"old generated realization with enough distinct words to detect a verbatim source prose leak now\n"),
                    "frozen": False,
                    "writer_access": "semantics-only",
                    "authority_note": "Diagnosed target.",
                },
                {
                    "span_id": "LOCK-1",
                    "classification": "OWNER_LOCK",
                    "line_start": 3,
                    "line_end": 3,
                    "sha256": digest(b"frozen after\n"),
                    "frozen": True,
                    "writer_access": "none",
                    "authority_note": "Exact owner lock.",
                },
            ],
            "writer_packet": self._record("writer.json"),
            "rejected_strategy_ledger": self._record("ledger.json"),
            "candidate": None,
            "validation_receipt": None,
            "gates": {
                "provenance_lock": "pass",
                "semantic_only_writer_input": "pass",
                "rejected_strategy_isolation": "pass",
                "preservation": "pending",
                "attribution": "pending",
                "structural_recurrence": "pending",
                "separate_adversarial_validation": "pending",
            },
            "release": {
                "candidate_visibility": "blocked",
                "detector_eligibility": "blocked",
                "blockers": ["Candidate and independent validations are pending."],
            },
            "detector": {
                "policy": "detector-last",
                "status": "not-run",
                "submitted_candidate_sha256": None,
                "result": None,
            },
        }

    def _write_packets(self) -> None:
        (self.root / "writer.json").write_text(json.dumps(self.writer), encoding="utf-8")
        (self.root / "ledger.json").write_text(json.dumps(self.ledger), encoding="utf-8")

    def _record(self, name: str) -> dict[str, object]:
        record: dict[str, object] = {
            "path": name,
            "sha256": digest((self.root / name).read_bytes()),
        }
        if name == "writer.json":
            record.update(
                source_prose_withheld=True,
                rejected_strategy_ledger_withheld=True,
                semantic_units_frozen=True,
            )
        else:
            record.update(writer_withheld=True, adversarial_validator_only=True)
        return record

    def bind_packets(self) -> None:
        self._write_packets()
        self.control["writer_packet"] = self._record("writer.json")
        self.control["rejected_strategy_ledger"] = self._record("ledger.json")

    def await_reasoning_packet(self) -> None:
        for name in ("builder.md", "strategy.md", "transport.md"):
            (self.root / name).write_text(f"frozen {name}\n", encoding="utf-8")
        source = (self.root / "source.md").read_bytes()
        self.control["workflow_state"] = "awaiting_reasoning_packet"
        self.control["provenance_spans"] = [
            {
                "span_id": "UNKNOWN-ALL",
                "classification": "UNKNOWN",
                "line_start": 1,
                "line_end": 3,
                "sha256": digest(source),
                "frozen": True,
                "writer_access": "none",
                "authority_note": "Awaiting Chat provenance review.",
            }
        ]
        self.control["reasoning_packet_request"] = {
            "packet_builder_prompt": self._record("builder.md"),
            "adversarial_strategy_evidence": self._record("strategy.md"),
            "mechanical_transport_directive": self._record("transport.md"),
        }
        self.control["writer_packet"] = None
        self.control["rejected_strategy_ledger"] = None
        self.control["gates"] = {name: "pending" for name in MODULE.GATE_NAMES}
        self.control["release"]["blockers"] = ["Chat reasoning packet is pending."]

    def advance_to_candidate(self) -> None:
        candidate = b"Fresh candidate sentence.\n"
        (self.root / "candidate.md").write_bytes(candidate)
        self.control["workflow_state"] = "candidate_validated"
        self.control["role_boundary"]["writer_context_id"] = "chat-writer-1"
        self.control["candidate"] = {"path": "candidate.md", "sha256": digest(candidate)}
        self.control["gates"] = {name: "pass" for name in MODULE.GATE_NAMES}
        self.control["release"] = {
            "candidate_visibility": "eligible",
            "detector_eligibility": "eligible",
            "blockers": [],
        }
        self.control["validation_receipt"] = {
            "change_justifications": {
                "sentence_coverage_complete": True,
                "records": [
                    {
                        "sentence_ref": "candidate sentence 1",
                        "defect_eliminated": "Breaks the inherited conceptual order while realizing SEM-1.",
                    }
                ],
            },
            "attribution": {
                "verdict": "pass",
                "findings": [],
                "general_claim_became_autobiography": False,
                "observation_became_interpretation": False,
                "certainty_shifted": False,
                "owner_language_counted_as_new_repair": False,
            },
            "structural_recurrence": {
                "verdict": "pass",
                "recurrences": [],
                "compared_strategy_ids": ["RS-1"],
                "checks": {name: "pass" for name in self.ledger["mandatory_structural_checks"]},
            },
            "adversarial_validation": {
                "validator_role": "chat_reasoning",
                "validator_context_id": "chat-validator-2",
                "saw_rejected_strategy_ledger": True,
                "did_not_edit_candidate": True,
                "verdict": "pass",
                "findings": [],
            },
            "preservation": {"verdict": "pass", "unexplained_deltas": []},
            "locked_span_checks": [
                {
                    "span_id": "UNKNOWN-1",
                    "source_sha256": digest(b"frozen before\n"),
                    "candidate_sha256": digest(b"frozen before\n"),
                    "verdict": "pass",
                },
                {
                    "span_id": "LOCK-1",
                    "source_sha256": digest(b"frozen after\n"),
                    "candidate_sha256": digest(b"frozen after\n"),
                    "verdict": "pass",
                },
            ],
        }


class HumanizationControlTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.fixture = ControlFixture(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def codes(self) -> set[str]:
        return {item["code"] for item in validate_control(self.fixture.control, self.root)}

    def test_valid_prewrite_control_passes_while_release_stays_blocked(self) -> None:
        self.assertEqual(validate_control(self.fixture.control, self.root), [])

    def test_current_activation_control_passes_separate_recovery_schema(self) -> None:
        control_path = (
            ROOT
            / "tasks"
            / "somatic-r15-clean-continuation-20260830"
            / "HUMANIZATION-CONTROL-STATE-20260831.json"
        )
        control = json.loads(control_path.read_text(encoding="utf-8"))
        self.assertEqual(validate_control(control, ROOT), [])

    def test_current_activation_control_rejects_pangram_or_master_mutation(self) -> None:
        control_path = (
            ROOT
            / "tasks"
            / "somatic-r15-clean-continuation-20260830"
            / "HUMANIZATION-CONTROL-STATE-20260831.json"
        )
        control = json.loads(control_path.read_text(encoding="utf-8"))
        control["activation_steering_result"]["pangram_run"] = True
        codes = {item["code"] for item in validate_control(control, ROOT)}
        self.assertIn("activation.result-state", codes)

    def test_current_parallel_control_rejects_teaching_lane_mutation(self) -> None:
        control_path = (
            ROOT
            / "tasks"
            / "somatic-r15-clean-continuation-20260830"
            / "HUMANIZATION-CONTROL-STATE-20260831.json"
        )
        control = json.loads(control_path.read_text(encoding="utf-8"))
        control["strategy"]["owner_teaching_trajectory"]["status"] = "AUTOMATED"
        codes = {item["code"] for item in validate_control(control, ROOT)}
        self.assertIn("recovery.teaching-state", codes)

    def test_valid_pending_reasoning_state_freezes_every_source_byte(self) -> None:
        self.fixture.await_reasoning_packet()
        self.assertEqual(validate_control(self.fixture.control, self.root), [])

    def test_pending_reasoning_state_rejects_executor_preclassification(self) -> None:
        self.fixture.await_reasoning_packet()
        self.fixture.control["provenance_spans"][0].update(
            classification="AI_TARGET",
            frozen=False,
            writer_access="semantics-only",
        )
        self.assertIn("control.pending-provenance", self.codes())

    def test_pending_reasoning_state_rejects_unreviewed_writer_input(self) -> None:
        self.fixture.await_reasoning_packet()
        self.fixture.control["writer_packet"] = self.fixture._record("writer.json")
        self.assertIn("control.pending-inputs", self.codes())

    def test_pending_reasoning_state_binds_request_artifacts(self) -> None:
        self.fixture.await_reasoning_packet()
        (self.root / "builder.md").write_text("drift\n", encoding="utf-8")
        self.assertIn("reasoning_packet_request.packet_builder_prompt.hash", self.codes())

    def test_source_hash_mutation_fails(self) -> None:
        self.fixture.control["source"]["sha256"] = "0" * 64
        self.assertIn("control.source.hash", self.codes())

    def test_provenance_coverage_gap_fails(self) -> None:
        self.fixture.control["provenance_spans"][1]["line_start"] = 3
        self.assertIn("control.provenance.coverage", self.codes())

    def test_owner_or_unknown_span_must_be_frozen(self) -> None:
        self.fixture.control["provenance_spans"][0]["frozen"] = False
        self.assertIn("control.provenance.freeze", self.codes())

    def test_writer_source_prose_leak_fails(self) -> None:
        self.fixture.writer["hard_constraints"].append(
            "old generated realization with enough distinct words to detect a verbatim source prose leak now"
        )
        self.fixture.bind_packets()
        self.assertIn("writer.source-prose-leak", self.codes())

    def test_rejected_strategy_field_in_writer_packet_fails(self) -> None:
        self.fixture.writer["rejected_strategies"] = ["old pattern"]
        self.fixture.bind_packets()
        self.assertIn("writer.forbidden-key", self.codes())

    def test_missing_structural_check_fails(self) -> None:
        self.fixture.ledger["mandatory_structural_checks"].remove("triads")
        self.fixture.bind_packets()
        self.assertIn("ledger.structural-checks", self.codes())

    def test_prewrite_detector_run_fails_closed(self) -> None:
        self.fixture.control["detector"]["status"] = "recorded"
        self.assertIn("detector.early", self.codes())

    def test_valid_candidate_stage_passes(self) -> None:
        self.fixture.advance_to_candidate()
        self.assertEqual(validate_control(self.fixture.control, self.root), [])

    def test_superficial_sentence_justification_fails(self) -> None:
        self.fixture.advance_to_candidate()
        self.fixture.control["validation_receipt"]["change_justifications"]["records"][0]["defect_eliminated"] = "better flow"
        self.assertIn("receipt.superficial-justification", self.codes())

    def test_attribution_laundering_fails(self) -> None:
        self.fixture.advance_to_candidate()
        self.fixture.control["validation_receipt"]["attribution"]["general_claim_became_autobiography"] = True
        self.assertIn("receipt.attribution-drift", self.codes())

    def test_structural_recurrence_fails(self) -> None:
        self.fixture.advance_to_candidate()
        self.fixture.control["validation_receipt"]["structural_recurrence"]["recurrences"] = ["RS-1"]
        self.assertIn("receipt.structural", self.codes())

    def test_same_context_adversarial_review_fails(self) -> None:
        self.fixture.advance_to_candidate()
        self.fixture.control["validation_receipt"]["adversarial_validation"]["validator_context_id"] = "chat-writer-1"
        self.assertIn("receipt.adversarial-independence", self.codes())

    def test_locked_span_hash_drift_fails(self) -> None:
        self.fixture.advance_to_candidate()
        self.fixture.control["validation_receipt"]["locked_span_checks"][0]["candidate_sha256"] = "0" * 64
        self.assertIn("receipt.lock-hash", self.codes())

    def test_detector_must_wait_for_validated_checkpoint(self) -> None:
        self.fixture.advance_to_candidate()
        self.fixture.control["detector"] = {
            "policy": "detector-last",
            "status": "recorded",
            "submitted_candidate_sha256": self.fixture.control["candidate"]["sha256"],
            "result": {"human": 1.0},
        }
        self.assertIn("detector.order", self.codes())

    def test_detector_result_binds_exact_validated_candidate(self) -> None:
        self.fixture.advance_to_candidate()
        self.fixture.control["workflow_state"] = "detector_recorded"
        self.fixture.control["detector"] = {
            "policy": "detector-last",
            "status": "recorded",
            "submitted_candidate_sha256": "0" * 64,
            "result": {"human": 1.0},
        }
        self.assertIn("detector.binding", self.codes())

    def test_detector_record_requires_prior_validated_checkpoint(self) -> None:
        self.fixture.advance_to_candidate()
        candidate_validated = copy.deepcopy(self.fixture.control)
        checkpoint = self.root / "candidate-validated-control.json"
        checkpoint.write_text(json.dumps(candidate_validated), encoding="utf-8")
        self.fixture.control["workflow_state"] = "detector_recorded"
        self.fixture.control["detector"] = {
            "policy": "detector-last",
            "status": "recorded",
            "submitted_candidate_sha256": self.fixture.control["candidate"]["sha256"],
            "validated_control_checkpoint": {
                "path": checkpoint.name,
                "sha256": digest(checkpoint.read_bytes()),
            },
            "result": {"human": 1.0},
        }
        self.assertEqual(validate_control(self.fixture.control, self.root), [])


if __name__ == "__main__":
    unittest.main()
