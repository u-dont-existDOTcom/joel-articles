import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_somatic_r15_articlewide.py"
SPEC = importlib.util.spec_from_file_location("check_somatic_r15_articlewide", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class SomaticArticleWideChecks(unittest.TestCase):
    def test_current_candidate_passes(self):
        self.assertEqual(MODULE.audit()["failures"], [])

    def test_lost_native_object_fails(self):
        source = MODULE.CANDIDATE.read_text(encoding="utf-8")
        source = source.replace(
            "**[EXISTING SKY HYPNOSIS NATIVE EMBED — exact object retained in HTML promotion]**",
            "",
        )
        with tempfile.TemporaryDirectory() as tmp:
            candidate = Path(tmp) / "candidate.md"
            candidate.write_text(source, encoding="utf-8")
            self.assertIn(
                "NATIVE_PLACEHOLDER_IDENTITY_ORDER_CHANGED",
                MODULE.audit(candidate)["failures"],
            )

    def test_lost_owner_constraint_fails(self):
        source = MODULE.CANDIDATE.read_text(encoding="utf-8").replace(
            "blissful tingles", "pleasant sensation"
        )
        with tempfile.TemporaryDirectory() as tmp:
            candidate = Path(tmp) / "candidate.md"
            candidate.write_text(source, encoding="utf-8")
            self.assertIn(
                "PRESERVATION_MARKER_MISSING:blissful-tingles",
                MODULE.audit(candidate)["failures"],
            )


if __name__ == "__main__":
    unittest.main()
