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
SOURCE = WORK / "materialized-part1-repair-r1"
SCRIPT = WORK / "apply_part1_repair_r2.py"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePart1ResidualMaterializerTests(unittest.TestCase):
    def test_materializes_residual_repair_and_preserves_part2(self) -> None:
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
            self.assertEqual(len(manifest["candidate"]["part1"]["operations"]), 3)
            p1 = (out / "candidate-part-1.txt").read_text(encoding="utf-8")
            self.assertIn("I’m not going to assume our problem magically begins at bedtime", p1)
            self.assertIn("Attachment is less cooperative.", p1)
            self.assertIn("I usually had some idea, so of course I answered.", p1)
            self.assertNotIn("The STI part is easy: say what you know, or say you don’t know. Feelings aren’t.", p1)
            self.assertNotIn("But enough moments become a pattern.", p1)


if __name__ == "__main__":
    unittest.main()
