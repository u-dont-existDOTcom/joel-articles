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
SOURCE = WORK / "materialized-owner-integrated-r2"
SCRIPT = WORK / "apply_part1_repair_r1.py"
SOURCE_P2_SHA = "20301b1bfb0052de694657411f231f82d9a45ae62ff9c4839015befce5c57dc2"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomancePart1RepairMaterializerTests(unittest.TestCase):
    def test_materializes_part1_repair_and_preserves_part2(self) -> None:
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
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(cp.returncode, 0, msg=f"stdout:\n{cp.stdout}\nstderr:\n{cp.stderr}")
            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["status"], "part1_repair_candidate_not_owner_final_article")
            self.assertTrue(manifest["candidate"]["master"]["invariant_audit"]["passed"])
            self.assertEqual(sha256(out / "candidate-part-2.txt"), SOURCE_P2_SHA)
            self.assertTrue(manifest["candidate"]["part2"]["unchanged"])
            self.assertEqual(len(manifest["candidate"]["part1"]["operations"]), 5)

            master = (out / "candidate-master.md").read_text(encoding="utf-8")
            part1 = (out / "candidate-part-1.txt").read_text(encoding="utf-8")
            for text in (master, part1):
                self.assertIn("whether you would want to raise children together and whether you're ready", text)
                self.assertIn("This will naturally prevent sex from happening too soon", text)
                self.assertIn("touch his wife without an agenda", text)
                self.assertIn("the sexual current between encounters", text)
                self.assertIn("If anybody was supposed to be winning that arrangement, it was him.", text)
                self.assertIn("one person terrorizing or controlling the other", text)
                self.assertIn("scared to say no or tell the truth", text)
                self.assertIn("get other people involved and think about safety first", text)
                self.assertIn("Outside a loving poly community or tribe, I think honest casual sex is almost impossible.", text)
                self.assertNotIn("If you want something closer to “casual love-making” without quite so many ways to damage each other", text)
                self.assertNotIn("Sex drives are independently alive and always changing.", text)

            self.assertIn("[*50 Things I Learned from 50 Years of Marriage*](https://dougtoft.substack.com/p/50-things-i-learned-from-50-years)", master)
            self.assertIn("[“the simmer”](https://kimanami.com/meet-another-well-fked-man/)", master)
            self.assertNotIn("https://", part1)

    def test_wrong_source_hash_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)
            bad = temp_dir / "bad-p1.txt"
            bad.write_text((SOURCE / "candidate-part-1.txt").read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
            cp = subprocess.run(
                [
                    sys.executable, str(SCRIPT),
                    "--source-master", str(SOURCE / "candidate-master.md"),
                    "--source-part1", str(bad),
                    "--source-part2", str(SOURCE / "candidate-part-2.txt"),
                    "--output-dir", str(temp_dir / "out"),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(cp.returncode, 0)
            self.assertIn("source hash mismatch", cp.stderr + cp.stdout)


if __name__ == "__main__":
    unittest.main()
