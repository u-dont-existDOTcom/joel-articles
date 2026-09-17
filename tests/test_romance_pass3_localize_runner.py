from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "work" / "romance-detector-repair-20260820" / "run_pass3_localize.sh"


class RomancePass3LocalizeRunnerTests(unittest.TestCase):
    def test_runner_is_read_only_and_shell_valid(self) -> None:
        subprocess.run(["bash", "-n", str(RUNNER)], check=True)
        text = RUNNER.read_text(encoding="utf-8")

        self.assertIn("pangram-local localize", text)
        self.assertIn("--report-url", text)
        self.assertIn("Detector submission path: NONE", text)
        self.assertIn('echo "No detector call was made."', text)
        self.assertNotIn("pangram-local run", text)
        self.assertNotIn('="necho', text)
        self.assertNotIn('==============="necho', text)


if __name__ == "__main__":
    unittest.main()
