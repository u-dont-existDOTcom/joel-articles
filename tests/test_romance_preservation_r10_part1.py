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
SOURCE = WORK / "materialized-semantic-r9"
SCRIPT = WORK / "apply_preservation_r10_part1.py"
SOURCE_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"
FALSE = "My dad gave me one piece of advice about sex: before you do it, ask each other whether you would want to raise children together and whether you're ready."
READINESS = "would we like to raise children together? Are we ready?"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePreservationR10Part1Tests(unittest.TestCase):
    def test_materializes_only_authorized_part1_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--source-master", str(SOURCE / "candidate-master.md"),
                    "--source-part1", str(SOURCE / "candidate-part-1.txt"),
                    "--source-part2", str(SOURCE / "candidate-part-2.txt"),
                    "--output-dir", str(out),
                ],
                cwd=WORK,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(cp.returncode, 0, msg=f"stdout:\n{cp.stdout}\nstderr:\n{cp.stderr}")
            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            checks = manifest["candidate"]["master"]["invariant_audit"]
            self.assertTrue(checks["passed"])
            self.assertTrue(checks["casual_section_byte_identical"])
            self.assertEqual(manifest["preservation_proof"]["unexplained_deltas"], 0)
            self.assertEqual(sha256(out / "candidate-part-2.txt"), SOURCE_P2_SHA)

            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            p1 = (out / "candidate-part-1.txt").read_text(encoding="utf-8")
            for text in (master, p1):
                self.assertNotIn(FALSE, text)
                self.assertIn(READINESS, text)
                self.assertIn("Sex drives are independently alive and always changing.", text)
                self.assertIn("This will naturally prevent sex from happening too soon", text)
                self.assertIn("Not because couples need another homework assignment.", text)
                self.assertIn("keeping some sexual life in me is partly my responsibility.", text)

    def test_source_hashes_are_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            bad_p1 = temp / "part1.txt"
            bad_p1.write_text((SOURCE / "candidate-part-1.txt").read_text(encoding="utf-8") + "\nmutant\n", encoding="utf-8")
            cp = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--source-master", str(SOURCE / "candidate-master.md"),
                    "--source-part1", str(bad_p1),
                    "--source-part2", str(SOURCE / "candidate-part-2.txt"),
                    "--output-dir", str(temp / "out"),
                ],
                cwd=WORK,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(cp.returncode, 0)
            self.assertIn("source hash mismatch", cp.stderr)


if __name__ == "__main__":
    unittest.main()
