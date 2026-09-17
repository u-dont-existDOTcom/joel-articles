from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "work" / "romance-detector-repair-20260820" / "run_pass3_gui_fallback.sh"


class RomancePass3GuiRunnerTests(unittest.TestCase):
    def test_shell_syntax_and_part2_only_detector_invocation(self) -> None:
        subprocess.run(["bash", "-n", str(SCRIPT)], check=True, cwd=ROOT)
        text = SCRIPT.read_text(encoding="utf-8")
        self.assertEqual(text.count("pangram-local run"), 1)
        self.assertIn('P2="$JOEL/work/romance-detector-repair-20260820/materialized-pass3/candidate-part-2.txt"', text)
        self.assertIn('--input "$P2"', text)
        self.assertNotIn("candidate-part-1.txt", text)
        self.assertIn("Pangram GUI authentication is not ready; no detector submission was made", text)
        self.assertIn("No automatic repeat will be attempted.", text)


if __name__ == "__main__":
    unittest.main()
