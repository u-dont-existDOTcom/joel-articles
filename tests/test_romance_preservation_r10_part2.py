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
SCRIPT = WORK / "apply_preservation_r10_part2.py"
SOURCE_P1_SHA = "35dea0c3fc5e1723a3d8d1f0c8192447525758dfb953910e1e0d353ae3dcf4d9"
REQUIRED = (
    "every time I hesitate, cry, need help, or get something wrong, I have to defend the role all over again",
    "She shouldn't have to keep acting soft, helpless, or cute so I know she's feminine.",
    "When a strong woman does that, I find it sexy.",
    "A man receiving care doesn’t make him a child either.",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePreservationR10Part2Tests(unittest.TestCase):
    def test_materializes_only_primal_section(self) -> None:
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
            self.assertTrue(manifest["candidate"]["master"]["invariant_audit"]["passed"])
            self.assertEqual(manifest["preservation_proof"]["unexplained_deltas"], 0)
            self.assertEqual(sha256(out / "candidate-part-1.txt"), SOURCE_P1_SHA)
            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            for anchor in REQUIRED:
                self.assertIn(anchor, master)

    def test_source_hashes_are_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            bad = temp / "part2.txt"
            bad.write_text((SOURCE / "candidate-part-2.txt").read_text(encoding="utf-8") + "\nmutant\n", encoding="utf-8")
            cp = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--source-master", str(SOURCE / "candidate-master.md"),
                    "--source-part1", str(SOURCE / "candidate-part-1.txt"),
                    "--source-part2", str(bad),
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
