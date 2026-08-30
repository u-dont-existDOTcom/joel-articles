from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
