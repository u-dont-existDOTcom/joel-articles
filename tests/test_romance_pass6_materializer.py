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
PASS5 = WORK / "materialized-pass5"
SCRIPT = WORK / "apply_pass6_exact.py"
REGISTERED_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePass6MaterializerTests(unittest.TestCase):
    def test_materializes_from_exact_pass5_and_preserves_part1(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--pass5-master",
                    str(PASS5 / "candidate-master.md"),
                    "--pass5-part1",
                    str(PASS5 / "candidate-part-1.txt"),
                    "--pass5-part2",
                    str(PASS5 / "candidate-part-2.txt"),
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
            self.assertEqual(manifest["detector_plan"]["part2"], "final_paid_pangram4_measurement_slot_6_via_private_selfhost")
            self.assertTrue(manifest["candidate"]["master"]["invariant_audit"]["passed"])
            self.assertEqual(len(manifest["candidate"]["part2"]["operations"]), 4)

            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            part2 = (out / "candidate-part-2.txt").read_text(encoding="utf-8")
            for text in (master, part2):
                self.assertIn("that’s the Crucible safety problem I already talked about.", text)
                self.assertIn("Her earning more than me is fine.", text)
                self.assertIn("effeminate me in the relationship", text)
                self.assertIn("successful woman to shrink so I feel masculine", text)
                self.assertIn("This is where I want to go. This is what I think we should do. Are you game?", text)
                self.assertIn("She can improve the plan or say no.", text)
                self.assertIn("Mandar obedeciendo", text)
                self.assertIn("Community isn't magic either", text)
                self.assertIn("That's not abstract to me: I'm sure B. and I would still be together", text)
                self.assertIn("agriculture, property, and inheritance", text)
                self.assertIn("Industrial Revolution", text)
                self.assertIn("social monogamy", text)
                self.assertIn("promise that this feeling will last forever", text)
                self.assertNotIn("Mutual friends can notice patterns neither person sees.", text)
                self.assertNotIn("can be a kind of gentle leadership", text)

            self.assertIn("## Not A Performance", master)
            self.assertIn("Not A Performance", part2)


if __name__ == "__main__":
    unittest.main()
