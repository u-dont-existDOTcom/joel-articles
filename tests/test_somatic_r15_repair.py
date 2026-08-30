from __future__ import annotations

import importlib.util
import subprocess
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_somatic_r15_repair.py"
SPEC = importlib.util.spec_from_file_location("check_somatic_r15_repair", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SomaticR15RepairTest(unittest.TestCase):
    def test_bounded_repair_invariants(self) -> None:
        result = MODULE.audit()
        self.assertEqual(result["failures"], [])
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["ordinaryLinks"], 16)
        self.assertEqual(result["nativePlaceholders"], 7)
        self.assertEqual(
            set(result["microChangedSections"]), MODULE.MICRO_AUTHORIZED_HEADINGS
        )

    def test_shallow_clone_uses_exact_section_manifest(self) -> None:
        unavailable = subprocess.CalledProcessError(128, ["git", "cat-file"])
        with mock.patch.object(MODULE, "git_blob_text", side_effect=unavailable):
            result = MODULE.audit()
        self.assertEqual(result["failures"], [])
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["preMicroIdentitySource"], "manifest")
        self.assertEqual(
            set(result["microChangedSections"]), MODULE.MICRO_AUTHORIZED_HEADINGS
        )


if __name__ == "__main__":
    unittest.main()
