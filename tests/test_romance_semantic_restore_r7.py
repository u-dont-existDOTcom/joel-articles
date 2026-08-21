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
SOURCE = WORK / "materialized-part1-semantic-r6"
SCRIPT = WORK / "apply_semantic_restore_r7.py"
SOURCE_P1_SHA = "3f33b066869e16fd75885c4a69564d772da33670486147ba8289613991ca5ffe"

REQUIRED = (
    "Many people are not even aware of how incredible sex can be when the polarity, trust, love & safety are all where they should be.",
    "That laboratory evidence establishes the uniqueness of the phenomenon.",
    "She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine.",
    "she can overcorrect into needing nobody and make receiving care or letting a man lead feel like weakness.",
    "Letting a man help, lead, or give her pleasure doesn’t make a strong woman helpless.",
    "A man receiving care doesn’t make him a child either.",
    "Even the curiosity itself can be therapeutic for you.",
)

OWNER = (
    "What attracts me is the feminine intuitive leap, because it's hard for me to understand, seems often absurd, yet many times more accurate than what I could have figured.",
    "Sexclusivity started gaining sway around the time we started planting carrots and peas, and owning land.",
    "When did you two last dance? And not the “we dance around our problems” joke (LOL)..",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class RomanceSemanticRestoreR7Tests(unittest.TestCase):
    def test_restores_all_known_lost_units_without_changing_part1(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            cp = subprocess.run([
                sys.executable, str(SCRIPT),
                "--source-master", str(SOURCE / "candidate-master.md"),
                "--source-part1", str(SOURCE / "candidate-part-1.txt"),
                "--source-part2", str(SOURCE / "candidate-part-2.txt"),
                "--output-dir", str(out),
            ], cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(cp.returncode, 0, msg=f"stdout:\n{cp.stdout}\nstderr:\n{cp.stderr}")
            manifest = json.loads((out / "candidate-manifest.json").read_text(encoding="utf-8"))
            self.assertTrue(manifest["candidate"]["master"]["semantic_invariant_audit"]["passed"])
            self.assertEqual(sha256(out / "candidate-part-1.txt"), SOURCE_P1_SHA)
            self.assertEqual(manifest["traceability"]["remaining_known_unsuperseded_lost_units"], 0)
            text = (out / "candidate-master.md").read_text(encoding="utf-8")
            for anchor in REQUIRED + OWNER:
                self.assertIn(anchor, text)


if __name__ == "__main__":
    unittest.main()
