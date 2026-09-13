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
SOURCE = WORK / "materialized-part1-repair-r5"
SCRIPT = WORK / "apply_part1_semantic_restore_r6.py"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"

REQUIRED = (
    "ask each other whether you would want to raise children together and whether you're ready",
    "Talk before you’re naked.",
    "anything kinky you need to be able to say out loud",
    "Sex drives are independently alive and always changing.",
    "For me both things matter",
    "It shouldn't become relationship homework.",
    "whatever exhausted scraps of time happen to be left after everything else",
    "The person getting more of what they want may think the arrangement is fulfilling.",
    "any children have a village",
    "enough moments become a pattern",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePart1SemanticRestoreTests(unittest.TestCase):
    def test_restores_unsuperseded_functions_and_preserves_part2(self) -> None:
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
            self.assertEqual(sha256(out / "candidate-part-2.txt"), SOURCE_P2_SHA)
            p1 = (out / "candidate-part-1.txt").read_text(encoding="utf-8")
            for anchor in REQUIRED:
                self.assertIn(anchor, p1)
            self.assertEqual(manifest["traceability"]["method"], "requirements-traceability plus atomic-content-unit adaptation")
            self.assertTrue(manifest["source_detector_result"]["rejected_for_semantic_loss"])
            self.assertEqual(manifest["detector_plan"]["status"], "do not dispatch aggregate yet")


if __name__ == "__main__":
    unittest.main()
