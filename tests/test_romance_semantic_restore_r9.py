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
SOURCE = WORK / "materialized-semantic-r8"
SCRIPT = WORK / "apply_semantic_restore_r9.py"
SOURCE_P1_SHA = "35dea0c3fc5e1723a3d8d1f0c8192447525758dfb953910e1e0d353ae3dcf4d9"
REQUIRED = "When a strong woman surrenders, she is choosing to, which is sexy."


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomanceSemanticRestoreR9Tests(unittest.TestCase):
    def test_restores_final_erotic_value_without_changing_part1(self) -> None:
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
            self.assertTrue(manifest["candidate"]["master"]["semantic_invariant_audit"]["passed"])
            self.assertEqual(sha256(out / "candidate-part-1.txt"), SOURCE_P1_SHA)
            self.assertEqual(manifest["traceability"]["registered_lost_units_corrected_total"], 10)
            self.assertEqual(manifest["traceability"]["remaining_known_unsuperseded_lost_units"], 0)
            self.assertIn(REQUIRED, (out / "candidate-master.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
