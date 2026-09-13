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
SCRIPT = WORK / "apply_preservation_r14_affection_maturity_split.py"
CANONICAL = ROOT / "articles" / "romance" / "master.md"
OLD_P2_SHA = "9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85"
CANONICAL_AFF_READER_SHA = "c307f3ae443c05eee135a459c01fba42a981bf1094bdb0fc83039dd3bc75dcc0"
SLOW_SHA = "2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4"
MATURITY = "When you and your partner are at different levels of maturity\n"
PRIMAL = "Primal attraction: channeling the Divine Masculine & Feminine\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class RomancePreservationR14Tests(unittest.TestCase):
    def run_materializer(self, out: Path, source_part1: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--source-master", str(SOURCE / "candidate-master.md"),
                "--source-part1", str(source_part1 or (SOURCE / "candidate-part-1.txt")),
                "--source-part2", str(SOURCE / "candidate-part-2.txt"),
                "--canonical-master", str(CANONICAL),
                "--output-dir", str(out),
            ],
            cwd=WORK,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_restores_canonical_affection_and_moves_only_detector_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = self.run_materializer(out)
            self.assertEqual(cp.returncode, 0, msg=f"stdout:\n{cp.stdout}\nstderr:\n{cp.stderr}")

            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            checks = manifest["invariant_audit"]
            self.assertTrue(checks["passed"])
            self.assertEqual(manifest["preservation"]["unexplained_deltas"], 0)
            self.assertTrue(checks["headings_identical"])
            self.assertTrue(checks["native_markers_identical"])
            self.assertTrue(checks["markdown_link_destinations_identical"])
            self.assertTrue(checks["affection_master_exact_canonical"])
            self.assertTrue(checks["affection_reader_exact_canonical"])
            self.assertTrue(checks["talk_reader_byte_identical"])
            self.assertTrue(checks["casual_reader_byte_identical"])
            self.assertTrue(checks["slow_exact_known_human_match"])
            self.assertTrue(checks["new_part1_excludes_maturity_section"])
            self.assertTrue(checks["new_part2_starts_at_complete_maturity_section"])
            self.assertTrue(checks["new_part2_contains_old_part2_byte_for_byte"])

            p1 = (out / "candidate-part-1.txt").read_text(encoding="utf-8")
            p2 = (out / "candidate-part-2.txt").read_text(encoding="utf-8")
            source_p2 = (SOURCE / "candidate-part-2.txt").read_text(encoding="utf-8")
            self.assertNotIn(MATURITY, p1)
            self.assertTrue(p2.startswith(MATURITY))
            self.assertIn(PRIMAL, p2)
            self.assertIn(source_p2, p2)
            self.assertEqual(sha256_text(source_p2), OLD_P2_SHA)

            aff = p1[p1.index("Affection and the simmer\n"):p1.index("Can Casual Sex or a Situationship Actually Be Honest?\n")]
            self.assertEqual(sha256_text(aff), CANONICAL_AFF_READER_SHA)
            self.assertIn("The opposite failure is letting the erotic current disappear", aff)
            self.assertIn("Affection has to be safe from escalation, and the erotic current has to stay alive.", aff)
            self.assertIn("If the sex changes, ask what else changed", aff)
            self.assertIn("she shouldn’t have to manufacture all my desire for me.", aff)

            self.assertIn("would we like to raise children together? Are we ready?", p1)
            self.assertIn("This will naturally prevent sex from happening too soon", p1)
            self.assertIn("The STI part is easy: say what you know, or say you don’t know.", p1)
            self.assertNotIn("But the first night isn’t necessarily the final ceiling either.", p1)

    def test_source_hashes_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            bad = temp / "part1.txt"
            bad.write_text((SOURCE / "candidate-part-1.txt").read_text(encoding="utf-8") + "mutant", encoding="utf-8")
            cp = self.run_materializer(temp / "out", source_part1=bad)
            self.assertNotEqual(cp.returncode, 0)
            self.assertIn("source hash mismatch", cp.stderr)


if __name__ == "__main__":
    unittest.main()
