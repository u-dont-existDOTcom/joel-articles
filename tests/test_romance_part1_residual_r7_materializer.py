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
SOURCE = WORK / "materialized-part1-repair-r6"
SCRIPT = WORK / "apply_part1_repair_r7.py"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePart1ResidualR7Tests(unittest.TestCase):
    def test_materializes_two_measured_residual_repairs_and_preserves_part2(self) -> None:
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
            self.assertEqual(len(manifest["candidate"]["part1"]["operations"]), 2)
            p1 = (out / "candidate-part-1.txt").read_text(encoding="utf-8")
            self.assertNotIn("Spiritual depth also doesn't tell me how dependable somebody is.", p1)
            self.assertIn("I’ve been through the wringer so much with idealization", p1)
            self.assertIn("I could know a woman for twenty years and still get into bed with her", p1)
            self.assertNotIn("Going slowly can show you how somebody’s moods move over time", p1)
            self.assertEqual(manifest["local_detector_evidence"]["part1-conversation-flaws"]["fraction_human"], 1.0)
            self.assertEqual(manifest["local_detector_evidence"]["part1-slow-steady"]["fraction_human"], 1.0)


if __name__ == "__main__":
    unittest.main()
