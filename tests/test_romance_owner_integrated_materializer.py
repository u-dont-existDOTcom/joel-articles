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
PASS6 = WORK / "materialized-pass6"
SCRIPT = WORK / "apply_owner_integrated.py"
REGISTERED_P1_SHA = "ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8"
PASS6_MASTER_SHA = "e09cb2309653d3ba9fc14526e7a49b1bef6f27a7494783489895a9c32fba93c5"
PASS6_P2_SHA = "6166fb2c17022e978de1019210067429f749071e53581bbe184adb721dbe8215"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomanceOwnerIntegratedMaterializerTests(unittest.TestCase):
    def test_materializes_exact_owner_integrated_candidate_from_pass6(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--pass6-master",
                    str(PASS6 / "candidate-master.md"),
                    "--pass6-part1",
                    str(PASS6 / "candidate-part-1.txt"),
                    "--pass6-part2",
                    str(PASS6 / "candidate-part-2.txt"),
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
            self.assertEqual(manifest["status"], "owner_integrated_candidate_not_owner_final_article")
            self.assertEqual(manifest["source_pass6"]["master"], PASS6_MASTER_SHA)
            self.assertEqual(manifest["source_pass6"]["part2"], PASS6_P2_SHA)
            self.assertEqual(sha256(out / "candidate-part-1.txt"), REGISTERED_P1_SHA)
            self.assertTrue(manifest["candidate"]["part1"]["reuses_registered_detector_result"])
            self.assertEqual(len(manifest["candidate"]["master"]["operations"]), 4)
            self.assertEqual(len(manifest["candidate"]["part2"]["operations"]), 4)
            self.assertTrue(manifest["candidate"]["master"]["invariant_audit"]["passed"])
            self.assertIn("cap_exhausted_6_of_6", manifest["detector_plan"]["part2"])

            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            part2 = (out / "candidate-part-2.txt").read_text(encoding="utf-8")

            for text in (master, part2):
                self.assertIn("I'm referring more to feminine vs masculine archetypes.", text)
                self.assertIn("seems often absurd, yet many times more accurate than what I could have figured", text)
                self.assertIn("Listening doesn't mean I'm gonna be a doormat tho.", text)
                self.assertIn("My house, my rules", text)
                self.assertIn("She may know much more than I do about some particular field", text)
                self.assertIn("I don't think equality means dividing every role 50/50.", text)
                self.assertIn("When a woman appreciates that masculine side of me, it tends to come out by itself.", text)
                self.assertIn("It's hard to find sexually monogamous animals, have you ever looked?", text)
                self.assertIn("Sexclusivity started gaining sway", text)
                self.assertIn("planting carrots and peas", text)
                self.assertIn("we're just like bonobos", text)
                self.assertIn("I can't fully commit to you if I’m still attracted to other women", text)
                self.assertIn("When did you two last dance?", text)
                self.assertIn("unconscious resentment begins to snowball", text)
                self.assertIn("old Romeo & Juliette might get wandering eye syndrome", text)
                self.assertIn("Outside help can sometimes break the loop fast", text)
                self.assertIn("Gandarussa", text)

                self.assertNotIn("Of course, this isn’t literally women=poetry and men=prose.", text)
                self.assertNotIn("Pushing me out of the way isn’t.", text)
                self.assertNotIn("At one point I tried a more literal solution: stop being attracted to anyone else.", text)
                self.assertNotIn("Start with the pinkest elephants in the room:", text)
                self.assertNotIn("See whether the other person will stay in the conversation.", text)

            self.assertIn("## Not A Performance", master)
            self.assertIn("Not A Performance", part2)
            self.assertNotIn("## Not A Performance", part2)
            self.assertIn("as they grow", master)
            self.assertNotIn("as the grow", master)
            self.assertNotIn("she see sees", master)

    def test_source_hash_gate_rejects_wrong_pass6_input(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)
            bad_master = temp_dir / "bad-master.md"
            bad_master.write_text(
                (PASS6 / "candidate-master.md").read_text(encoding="utf-8") + "\nmutation\n",
                encoding="utf-8",
            )
            cp = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--pass6-master",
                    str(bad_master),
                    "--pass6-part1",
                    str(PASS6 / "candidate-part-1.txt"),
                    "--pass6-part2",
                    str(PASS6 / "candidate-part-2.txt"),
                    "--output-dir",
                    str(temp_dir / "out"),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(cp.returncode, 0)
            self.assertIn("pass-6 source hash mismatch", cp.stderr + cp.stdout)


if __name__ == "__main__":
    unittest.main()
