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
PASS3 = WORK / "materialized-pass3"
SCRIPT = WORK / "apply_pass4.py"
REGISTERED_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePass4MaterializerTests(unittest.TestCase):
    def test_materializes_from_exact_pass3_and_preserves_part1(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--pass3-master",
                    str(PASS3 / "candidate-master.md"),
                    "--pass3-part1",
                    str(PASS3 / "candidate-part-1.txt"),
                    "--pass3-part2",
                    str(PASS3 / "candidate-part-2.txt"),
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
            self.assertEqual(manifest["detector_plan"]["part1"], "no_new_call_exact_registered_hash_unchanged")
            self.assertEqual(manifest["detector_plan"]["part2"], "one_new_pangram4_measurement_via_private_selfhost")
            self.assertTrue(manifest["candidate"]["master"]["invariant_audit"]["passed"])
            self.assertEqual(len(manifest["candidate"]["part2"]["operations"]), 3)

            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            part2 = (out / "candidate-part-2.txt").read_text(encoding="utf-8")
            for text in (master, part2):
                self.assertNotIn("Micromanaging everything is totally different and not attractive.", text)
                self.assertIn("A woman earning more than me isn’t the problem", text)
                self.assertIn("She doesn't have to pretend I'm always right either.", text)
                self.assertIn("At one point I tried a more literal solution: stop being attracted to anyone else.", text)
                self.assertNotIn("I haven't done any of this perfectly. At one point I tried a more radical answer: changing attraction itself.", text)


if __name__ == "__main__":
    unittest.main()
