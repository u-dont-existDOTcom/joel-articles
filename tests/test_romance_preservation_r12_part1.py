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
SOURCE = WORK / "materialized-preservation-r11-part1"
SCRIPT = WORK / "apply_preservation_r12_part1.py"
SOURCE_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"
SLOW_SHA = "2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4"
R11_PATIENT = "All three women eventually told me they felt like my patient, and I could see why."
R10_PATIENT = "All three women told me at some point that they felt like my patient. Which is true"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePreservationR12Part1Tests(unittest.TestCase):
    def run_materializer(self, out: Path, part1: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--source-master", str(SOURCE / "candidate-master.md"),
                "--source-part1", str(part1 or (SOURCE / "candidate-part-1.txt")),
                "--source-part2", str(SOURCE / "candidate-part-2.txt"),
                "--output-dir", str(out),
            ],
            cwd=WORK,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_rejects_noncompositional_patient_rollback_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = self.run_materializer(out)
            self.assertEqual(cp.returncode, 0, msg=f"stdout:\n{cp.stdout}\nstderr:\n{cp.stderr}")
            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            checks = manifest["candidate"]["master"]["invariant_audit"]
            self.assertTrue(checks["passed"])
            self.assertEqual(manifest["preservation_proof"]["unexplained_deltas"], 0)
            self.assertTrue(checks["talk_section_byte_identical"])
            self.assertTrue(checks["affection_section_byte_identical"])
            self.assertTrue(checks["casual_section_byte_identical"])
            self.assertEqual(checks["slow_local_sha256"], SLOW_SHA)
            self.assertTrue(checks["slow_exact_known_human_match"])
            self.assertEqual(sha256(out / "candidate-part-2.txt"), SOURCE_P2_SHA)

            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            p1 = (out / "candidate-part-1.txt").read_text(encoding="utf-8")
            for text in (master, p1):
                self.assertNotIn(R11_PATIENT, text)
                self.assertIn(R10_PATIENT, text)
                self.assertNotIn("But the first night isn’t necessarily the final ceiling either.", text)
                self.assertIn("Something that developed between us had changed what her body could do with me.", text)

            ops = [op["label"] for op in manifest["candidate"]["part1"]["operations"]]
            self.assertEqual(ops, ["reject-noncompositional-patient-local-green-rollback"])

    def test_source_hashes_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            bad_p1 = temp / "part1.txt"
            bad_p1.write_text((SOURCE / "candidate-part-1.txt").read_text(encoding="utf-8") + "\nmutant\n", encoding="utf-8")
            cp = self.run_materializer(temp / "out", part1=bad_p1)
            self.assertNotEqual(cp.returncode, 0)
            self.assertIn("source hash mismatch", cp.stderr)


if __name__ == "__main__":
    unittest.main()
