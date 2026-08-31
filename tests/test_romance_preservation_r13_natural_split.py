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
SOURCE = WORK / "materialized-preservation-r12-part1"
SCRIPT = WORK / "apply_preservation_r13_natural_split.py"
SOURCE_MASTER_SHA = "43d98cdb0df5fc9437f89ba56187e3a5586951375ccbf69e6e6a82e82569925f"
PRIMAL = "Primal attraction: channeling the Divine Masculine & Feminine\n"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePreservationR13NaturalSplitTests(unittest.TestCase):
    def run_materializer(self, out: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
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

    def test_moves_only_detector_half_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = self.run_materializer(out)
            self.assertEqual(cp.returncode, 0, msg=f"stdout:\n{cp.stdout}\nstderr:\n{cp.stderr}")
            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            self.assertTrue(manifest["invariant_audit"]["passed"])
            self.assertFalse(manifest["operation"]["article_prose_changed"])
            self.assertFalse(manifest["operation"]["full_reader_visible_bytes_changed"])
            self.assertEqual(sha256(out / "candidate-master.md"), SOURCE_MASTER_SHA)

            source_full = (SOURCE / "candidate-part-1.txt").read_text(encoding="utf-8") + "\n" + (SOURCE / "candidate-part-2.txt").read_text(encoding="utf-8")
            candidate_full = (out / "candidate-part-1.txt").read_text(encoding="utf-8") + (out / "candidate-part-2.txt").read_text(encoding="utf-8")
            self.assertEqual(candidate_full, source_full)
            self.assertTrue((out / "candidate-part-2.txt").read_text(encoding="utf-8").startswith(PRIMAL))
            self.assertIn('Key at first asked me innocently, "Can you be my guru?"', (out / "candidate-part-1.txt").read_text(encoding="utf-8"))

    def test_source_hashes_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            bad = temp / "part1.txt"
            bad.write_text((SOURCE / "candidate-part-1.txt").read_text(encoding="utf-8") + "mutant", encoding="utf-8")
            cp = subprocess.run(
                [sys.executable, str(SCRIPT), "--source-master", str(SOURCE / "candidate-master.md"), "--source-part1", str(bad), "--source-part2", str(SOURCE / "candidate-part-2.txt"), "--output-dir", str(temp / "out")],
                cwd=WORK,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(cp.returncode, 0)
            self.assertIn("source hash mismatch", cp.stderr)


if __name__ == "__main__":
    unittest.main()
