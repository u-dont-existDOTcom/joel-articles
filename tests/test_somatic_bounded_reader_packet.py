from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/materialize_somatic_bounded_reader_packet.py"
CANDIDATE = ROOT / "articles/somatic-therapies/experiments/R15-CLEAN-REPAIR-CANDIDATE-20260830.md"
SPEC = importlib.util.spec_from_file_location("materialize_somatic_bounded_reader_packet", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SomaticBoundedReaderPacketTest(unittest.TestCase):
    def test_exact_bounded_material(self) -> None:
        material = MODULE.material_from_source(CANDIDATE.read_text(encoding="utf-8"))
        self.assertTrue(material.startswith(MODULE.FIRST_START))
        self.assertIn(MODULE.SECOND_START, material)
        self.assertIn(MODULE.SKY_REPLACEMENT, material)
        self.assertNotIn(MODULE.SKY_PLACEHOLDER, material)
        self.assertNotIn("# Introduction", material)
        self.assertNotIn("# When the Body Knows More Than the Story", material)
        for withheld in ("Pangram", "detector", "R15", "R16", "R65", "preservation"):
            self.assertNotIn(withheld, material)


if __name__ == "__main__":
    unittest.main()
