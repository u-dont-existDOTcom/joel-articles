import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_somatic_r15_direct_owner.py"
SPEC = importlib.util.spec_from_file_location("check_somatic_r15_direct_owner", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class SomaticDirectOwnerChecks(unittest.TestCase):
    def test_current_candidate_passes(self):
        self.assertEqual(MODULE.audit()["failures"], [])

    def test_lost_owner_wording_fails(self):
        source = MODULE.CANDIDATE.read_text(encoding="utf-8").replace(
            "big fuckity whoopty doo", "what does that prove"
        )
        with tempfile.TemporaryDirectory() as tmp:
            candidate = Path(tmp) / "candidate.md"
            candidate.write_text(source, encoding="utf-8")
            self.assertIn(
                "PRESERVATION_MARKER_MISSING:owner-credibility-line",
                MODULE.audit(candidate)["failures"],
            )

    def test_lost_link_fails(self):
        source = MODULE.CANDIDATE.read_text(encoding="utf-8").replace(
            "http://loveyhuasca.info", "https://example.invalid", 1
        )
        with tempfile.TemporaryDirectory() as tmp:
            candidate = Path(tmp) / "candidate.md"
            candidate.write_text(source, encoding="utf-8")
            self.assertIn("LINK_MULTISET_CHANGED", MODULE.audit(candidate)["failures"])


if __name__ == "__main__":
    unittest.main()
