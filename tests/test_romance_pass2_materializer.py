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
PASS1 = WORK / "materialized"
SCRIPT = WORK / "apply_pass2.py"
REGISTERED_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePass2MaterializerTests(unittest.TestCase):
    def test_materializes_and_restores_part1_exactly(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--pass1-master",
                    str(PASS1 / "candidate-master.md"),
                    "--pass1-part1",
                    str(PASS1 / "candidate-part-1.txt"),
                    "--pass1-part2",
                    str(PASS1 / "candidate-part-2.txt"),
                    "--output-dir",
                    str(out),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(sha256(out / "candidate-part-1.txt"), REGISTERED_P1_SHA)
            self.assertTrue(manifest["candidate"]["part1"]["reuses_registered_detector_result"])
            self.assertEqual(manifest["detector_plan"]["part1"], "no_new_call_exact_registered_hash_restored")
            self.assertEqual(manifest["detector_plan"]["part2"], "one_new_pangram4_measurement_only")
            self.assertTrue(manifest["candidate"]["master"]["invariant_audit"]["passed"])

            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            part2 = (out / "candidate-part-2.txt").read_text(encoding="utf-8")
            for text in (master, part2):
                self.assertIn("rather than one-dimensionalizing them", text)
                self.assertNotIn("Don't flatten them into one character", text)
                self.assertNotIn("Staying curious about what happened can be therapeutic in itself.", text)


if __name__ == "__main__":
    unittest.main()
