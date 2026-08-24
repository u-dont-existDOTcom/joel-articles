import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "project-sources" / "CONFIRMED-SUBSTACK-HELPER.json"
GATE = ROOT / "docs" / "SUBSTACK-HELPER-DELIVERY-GATE.md"
GENERATOR = ROOT / "project-sources" / "substack_transfer_helper.py.txt"


class SubstackHelperDeliveryGateTests(unittest.TestCase):
    def test_profile_requires_canonical_generator_and_fail_closed_fallback(self):
        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        contract = profile.get("generation_contract", {})

        self.assertEqual(
            contract.get("protocol"),
            "docs/SUBSTACK-HELPER-DELIVERY-GATE.md",
        )
        self.assertEqual(
            contract.get("canonical_generator"),
            "project-sources/substack_transfer_helper.py.txt",
        )
        self.assertEqual(
            contract.get("canonical_native_object_parser"),
            "project-sources/html_islands.py.txt",
        )
        self.assertTrue(contract.get("raw_editor_html_required_for_native_object_authority"))
        self.assertEqual(contract.get("canonical_build_sequence"), ["init", "build", "verify"])
        self.assertEqual(contract.get("delivery_requires_embedded_manifest"), "hva-transfer-manifest")
        self.assertEqual(contract.get("delivery_requires_current_helper_format"), "joel-substack-transfer-helper-v4")
        self.assertFalse(contract.get("improvised_helper_allowed"))
        self.assertEqual(contract.get("fallback_if_generator_unavailable"), "fail_closed_report_blocker")

        forbidden = "\n".join(contract.get("forbidden_fallbacks", [])).lower()
        self.assertIn("hand-built", forbidden)
        self.assertIn("markdown-to-html", forbidden)
        self.assertIn("memory", forbidden)

    def test_locked_invariants_forbid_improvised_delivery(self):
        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        invariants = "\n".join(profile.get("locked_invariants", [])).lower()
        self.assertIn("hand-built helper implementations are forbidden", invariants)
        self.assertIn("fail closed", invariants)
        self.assertIn("raw substack editor html", invariants)

    def test_delivery_gate_is_explicit(self):
        text = GATE.read_text(encoding="utf-8").lower()
        self.assertIn("active / blocking", text)
        self.assertIn("do not hand-build a fallback helper", text)
        self.assertIn("init`, `build`, and `verify", text)
        self.assertIn("hva-transfer-manifest", text)
        self.assertIn("not verified for delivery", text)

    def test_generator_format_matches_delivery_contract(self):
        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        required_format = profile["generation_contract"]["delivery_requires_current_helper_format"]
        generator = GENERATOR.read_text(encoding="utf-8")
        self.assertIn(f'HELPER_FORMAT = "{required_format}"', generator)
        self.assertIn("def verify_helper_static_features", generator)
        self.assertIn("Helper lacks transfer manifest", generator)


if __name__ == "__main__":
    unittest.main()
