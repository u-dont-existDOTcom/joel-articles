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
PASS4 = WORK / "materialized-pass4"
SCRIPT = WORK / "apply_pass5.py"
REGISTERED_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePass5MaterializerTests(unittest.TestCase):
    def test_materializes_from_exact_pass4_and_preserves_part1(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--pass4-master",
                    str(PASS4 / "candidate-master.md"),
                    "--pass4-part1",
                    str(PASS4 / "candidate-part-1.txt"),
                    "--pass4-part2",
                    str(PASS4 / "candidate-part-2.txt"),
                    "--output-dir",
                    str(out),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(cp.returncode, 0, msg=f"stdout:\n{cp.stdout}\nstderr:\n{cp.stderr}")
            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(sha256(out / "candidate-part-1.txt"), REGISTERED_P1_SHA)
            self.assertTrue(manifest["candidate"]["part1"]["reuses_registered_detector_result"])
            self.assertEqual(manifest["detector_plan"]["part1"], "no_new_call_exact_registered_hash_unchanged")
            self.assertEqual(manifest["detector_plan"]["part2"], "one_new_pangram4_measurement_via_private_selfhost")
            self.assertTrue(manifest["candidate"]["master"]["invariant_audit"]["passed"])
            self.assertEqual(len(manifest["candidate"]["part2"]["operations"]), 5)

            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            part2 = (out / "candidate-part-2.txt").read_text(encoding="utf-8")
            for text in (master, part2):
                self.assertIn("Her jade-egg practice is basically the solo version", text)
                self.assertIn("That’s the Crucible safety problem I already talked about.", text)
                self.assertIn("effeminate me in the relationship", text)
                self.assertIn("Mandar obedeciendo", text)
                self.assertIn("Bee once called me her “wife.”", text)
                self.assertIn("Anami emphasizes learning to receive.", text)
                self.assertIn("When a strong woman surrenders, she is choosing to.", text)
                self.assertIn("same words for two different futures", text)
                self.assertIn("Industrial Revolution", text)
                self.assertIn("social monogamy", text)
                self.assertIn("guarantee a permanent romantic feeling", text)
                self.assertNotIn("The point is not to tally every act and force the totals to match.", text)
                self.assertNotIn("Those origins still matter.", text)


if __name__ == "__main__":
    unittest.main()
