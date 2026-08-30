import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_somatic_r15_task.py"
SPEC = importlib.util.spec_from_file_location("check_somatic_r15_task", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class SomaticOwnerOutcomeAcceptanceTests(unittest.TestCase):
    def test_review_ready_at_13_82_percent_cannot_close_root_task(self):
        lock = {
            "status": "ready_for_owner_review",
            "objectiveReconciliation": {"typedCompletionClaim": "READY_FOR_OWNER_REVIEW"},
            "finalOutcome": {
                "candidateSha256": "candidate",
                "pangram": {
                    "fractionHuman": 0.1381948739,
                    "candidateSha256": "candidate",
                    "exactBoundarySha256": "boundary",
                },
                "gates": {},
            },
        }
        reconciliation = {
            "completionClaim": {"type": "READY_FOR_OWNER_REVIEW"},
            "terminalComparator": {
                "rootTerminalizationAllowed": True,
                "unmetOutcomeIds": [],
            },
        }

        findings = MODULE.outcome_acceptance_failures(lock, reconciliation)

        self.assertIn("OWNER_OUTCOME_NOT_ACHIEVED", findings)
        self.assertIn("COMPLETION_CLAIM_NOT_OWNER_OUTCOME_ACHIEVED", findings)
        self.assertIn("PANGRAM_100_PERCENT_HUMAN_MISSING", findings)

    def test_exact_100_percent_candidate_with_all_gates_and_delivery_passes(self):
        pass_gates = {
            "sourceIntegrity": "PASS",
            "forwardTraceability": "PASS",
            "reverseTraceability": "PASS",
            "semanticSanity": "PASS",
            "architectureMultiscale": "PASS",
            "coldAudit": "PASS",
            "independentFinalReader": "PASS",
            "linksAndNativeObjects": "PASS",
            "failedBranchContamination": "PASS",
        }
        lock = {
            "status": "owner_outcome_achieved",
            "objectiveReconciliation": {"typedCompletionClaim": "OWNER_OUTCOME_ACHIEVED"},
            "finalOutcome": {
                "candidateSha256": "candidate",
                "unexplainedSubstantiveDeltas": 0,
                "pangram": {
                    "fractionHuman": 1.0,
                    "candidateSha256": "candidate",
                    "exactBoundarySha256": "boundary",
                },
                "gates": pass_gates,
                "chatDelivery": {
                    "conversationUrl": "https://chatgpt.com/c/example",
                    "finalDraftSha256": "draft",
                    "commentableDiffSha256": "diff",
                },
            },
        }
        reconciliation = {
            "completionClaim": {"type": "OWNER_OUTCOME_ACHIEVED"},
            "terminalComparator": {
                "rootTerminalizationAllowed": True,
                "unmetOutcomeIds": [],
            },
        }

        self.assertEqual(MODULE.outcome_acceptance_failures(lock, reconciliation), [])


if __name__ == "__main__":
    unittest.main()
