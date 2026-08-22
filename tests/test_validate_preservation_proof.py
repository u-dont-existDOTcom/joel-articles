from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_preservation_proof",
    ROOT / "scripts" / "validate_preservation_proof.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
validate_proof = MODULE.validate_proof


def valid_proof() -> dict[str, object]:
    return {
        "schema_version": 1,
        "source": {
            "path": "articles/romance/master.md",
            "revision": "deadbeef",
            "sha256": "a" * 64,
        },
        "changed_scope": "Talk about making love before you do it",
        "mode": "P2S",
        "edit_dose": "D3",
        "preservation_units": [
            {
                "unit_id": "PU-TALK-01",
                "source_ref": "heading:Talk about making love before you do it / paragraph 1",
                "authority": "registered source",
                "type": "claim",
                "meaning": "Talk about sex before becoming sexually exposed.",
                "required_context": "local section",
                "allowed_disposition": "may-reword-semantically",
                "candidate_mapping": "candidate paragraph 1",
                "status": "preserved",
            },
            {
                "unit_id": "PU-TALK-02",
                "source_ref": "owner correction 2026-08-21",
                "authority": "direct owner correction",
                "type": "attribution",
                "meaning": "Later readiness/co-parenting interpretation is not a quotation from the father.",
                "required_context": "opening father quotation remains a separate provenance object",
                "allowed_disposition": "must-remain-here",
                "candidate_mapping": "candidate paragraph 2",
                "status": "preserved",
            },
        ],
        "change_whitelist": [
            {
                "change_id": "CH-TALK-01",
                "description": "Correct false father attribution without deleting the later readiness/co-parenting question.",
            }
        ],
        "candidate_deltas": [
            {
                "delta_id": "DELTA-TALK-01",
                "classification": "attribution-provenance-change",
                "description": "Remove false father attribution and state the later interpretation as Joel's own.",
                "authority_ref": "CH-TALK-01",
                "status": "authorized",
            }
        ],
        "unexplained_deltas": [],
        "forward_traceability": "pass",
        "reverse_traceability": "pass",
        "owner_provenance_separation": "pass",
        "architecture_dependency_gate": "pass",
        "detector_eligibility": "eligible",
    }


class PreservationProofValidatorTests(unittest.TestCase):
    def assert_fails_with(self, proof: dict[str, object], code: str) -> None:
        findings = validate_proof(proof)
        self.assertIn(code, {item["code"] for item in findings}, findings)

    def test_valid_receipt_passes(self) -> None:
        self.assertEqual(validate_proof(valid_proof()), [])

    def test_deleted_unique_claim_cannot_be_left_pending(self) -> None:
        proof = valid_proof()
        unit = proof["preservation_units"][0]
        assert isinstance(unit, dict)
        unit["status"] = "pending"
        unit["candidate_mapping"] = ""
        self.assert_fails_with(proof, "proof.unit.status")

    def test_generic_redundant_disposition_is_forbidden(self) -> None:
        proof = valid_proof()
        unit = proof["preservation_units"][0]
        assert isinstance(unit, dict)
        unit["allowed_disposition"] = "redundant"
        self.assert_fails_with(proof, "proof.unit.disposition")

    def test_provenance_mutant_fails_when_separation_gate_fails(self) -> None:
        proof = valid_proof()
        proof["owner_provenance_separation"] = "fail"
        self.assert_fails_with(proof, "proof.provenance")

    def test_actor_or_causal_change_requires_authority(self) -> None:
        proof = valid_proof()
        deltas = proof["candidate_deltas"]
        assert isinstance(deltas, list)
        deltas.append(
            {
                "delta_id": "DELTA-TALK-02",
                "classification": "agency-change",
                "description": "Swap who gives the advice.",
                "authority_ref": "",
                "status": "authorized",
            }
        )
        self.assert_fails_with(proof, "proof.delta.authority")

    def test_unknown_whitelist_reference_fails(self) -> None:
        proof = valid_proof()
        delta = proof["candidate_deltas"][0]
        assert isinstance(delta, dict)
        delta["authority_ref"] = "CH-MISSING-99"
        self.assert_fails_with(proof, "proof.delta.unknown-change")

    def test_unexplained_addition_blocks_detector_eligibility(self) -> None:
        proof = valid_proof()
        proof["unexplained_deltas"] = [
            {
                "delta_id": "DELTA-EXTRA-01",
                "description": "New explanatory bridge not authorized by source or whitelist.",
            }
        ]
        self.assert_fails_with(proof, "proof.unexplained.nonzero")

    def test_moved_unit_requires_candidate_destination(self) -> None:
        proof = valid_proof()
        unit = proof["preservation_units"][0]
        assert isinstance(unit, dict)
        unit["allowed_disposition"] = "may-move:next section"
        unit["status"] = "moved"
        unit["candidate_mapping"] = ""
        self.assert_fails_with(proof, "proof.unit.mapping")

    def test_owner_deleted_unit_requires_authority_reference(self) -> None:
        proof = valid_proof()
        unit = proof["preservation_units"][0]
        assert isinstance(unit, dict)
        unit["allowed_disposition"] = "owner-deleted:owner comment"
        unit["status"] = "owner-deleted"
        unit["candidate_mapping"] = ""
        unit["authority_ref"] = ""
        self.assert_fails_with(proof, "proof.unit.owner-authority")

    def test_detector_cannot_be_eligible_when_reverse_traceability_fails(self) -> None:
        proof = valid_proof()
        proof["reverse_traceability"] = "fail"
        self.assert_fails_with(proof, "proof.reverse")

    def test_duplicate_unit_ids_fail(self) -> None:
        proof = valid_proof()
        units = proof["preservation_units"]
        assert isinstance(units, list)
        duplicate = copy.deepcopy(units[0])
        units.append(duplicate)
        self.assert_fails_with(proof, "proof.unit.id")


if __name__ == "__main__":
    unittest.main()
