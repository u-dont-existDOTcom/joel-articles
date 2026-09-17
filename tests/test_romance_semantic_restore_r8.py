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
SOURCE = WORK / "materialized-semantic-r7"
SCRIPT = WORK / "apply_semantic_restore_r8.py"
SOURCE_P1_SHA = "35dea0c3fc5e1723a3d8d1f0c8192447525758dfb953910e1e0d353ae3dcf4d9"

REQUIRED = (
    "Then I have to defend the identity every time I hesitate, cry, need help, or get something wrong.",
    "Surrender means so much more when she could take control but prefers not to at that moment.",
)

OWNER = (
    "What attracts me is the feminine intuitive leap, because it's hard for me to understand, seems often absurd, yet many times more accurate than what I could have figured.",
    "Sexclusivity started gaining sway around the time we started planting carrots and peas, and owning land.",
    "When did you two last dance? And not the “we dance around our problems” joke (LOL)..",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomanceSemanticRestoreR8Tests(unittest.TestCase):
    def test_restores_final_known_units_without_changing_part1(self) -> None:
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
            self.assertEqual(manifest["traceability"]["remaining_known_unsuperseded_lost_units"], 0)
            self.assertEqual(manifest["traceability"]["registered_lost_units_corrected_total"], 9)
            text = (out / "candidate-master.md").read_text(encoding="utf-8")
            for anchor in REQUIRED + OWNER:
                self.assertIn(anchor, text)


if __name__ == "__main__":
    unittest.main()
