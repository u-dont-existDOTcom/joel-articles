from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "romance-detector-repair-20260820"
SOURCE = WORK / "materialized-part1-repair-r2"
SCRIPT = WORK / "apply_part1_repair_r3.py"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePart1FinalResidualMaterializerTests(unittest.TestCase):
    def test_materializes_final_residuals_and_preserves_part2(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = subprocess.run([
                sys.executable, str(SCRIPT),
                "--source-master", str(SOURCE / "candidate-master.md"),
                "--source-part1", str(SOURCE / "candidate-part-1.txt"),
                "--source-part2", str(SOURCE / "candidate-part-2.txt"),
                "--output-dir", str(out),
            ], cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(cp.returncode, 0, msg=f"stdout:\n{cp.stdout}\nstderr:\n{cp.stderr}")
            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            self.assertTrue(manifest["candidate"]["master"]["invariant_audit"]["passed"])
            self.assertEqual(sha256(out / "candidate-part-2.txt"), SOURCE_P2_SHA)
            self.assertEqual(len(manifest["candidate"]["part1"]["operations"]), 4)
            p1 = (out / "candidate-part-1.txt").read_text(encoding="utf-8")
            self.assertIn("Your body wasn't part of the agreement", p1)
            self.assertIn("Okay, that's honest as far as it goes.", p1)
            self.assertIn("then I want to see a boring day", p1)
            self.assertIn("Mostly I have to build my own brakes before I'm alone with her", p1)
            self.assertIn("That's where Gandarussa matters to me.", p1)
            self.assertNotIn("Ten profound conversations in one weekend may tell me we can have profound conversations.", p1)


if __name__ == "__main__":
    unittest.main()
