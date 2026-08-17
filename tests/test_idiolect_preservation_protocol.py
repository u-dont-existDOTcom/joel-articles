from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "project-sources" / "IDIOLECT-PRESERVATION-PROTOCOL.md"


class IdiolectPreservationProtocolTests(unittest.TestCase):
    def test_protocol_encodes_minimum_dose_and_three_axes(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertIn("minimum necessary edit dose", text.lower())
        for dose in ("`D0`", "`D1`", "`D2`", "`D3`", "`D4`"):
            self.assertIn(dose, text)
        self.assertIn("Semantic/editorial fidelity", text)
        self.assertIn("Detector status", text)
        self.assertIn("Authorship-signal retention", text)

    def test_protocol_does_not_mislabel_single_author_proxy_as_ier(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertIn("single-author retention proxy", text)
        self.assertIn("not IER", text)
        self.assertIn("No universal pass threshold", text)
        self.assertIn("baseline accuracy minus rewrite accuracy", text)

    def test_protocol_routes_to_lab_commands_and_protects_authority(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertIn("u-dont-existDOTcom/pangram-humanization-lab", text)
        self.assertIn("pangram-lab idiolect-retention", text)
        self.assertIn("pangram-lab idiolect-ier", text)
        self.assertIn("Never manufacture errors", text)
        self.assertIn("Neither repository may use a metric to silently soften", text)

    def test_canonical_loaders_route_to_protocol(self):
        for relative in (
            "SKILL.md",
            "CANONICAL-REPO-MAP.md",
            "docs/INDEX.md",
            "docs/HUMANIZATION-ARCHITECTURE-GATE.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn(
                "IDIOLECT-PRESERVATION-PROTOCOL.md",
                text,
                msg=f"missing idiolect protocol route in {relative}",
            )


if __name__ == "__main__":
    unittest.main()
