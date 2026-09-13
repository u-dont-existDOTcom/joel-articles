from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "work" / "romance-detector-repair-20260820" / "run_pass2_api.sh"


class RomancePass2ApiRunnerTests(unittest.TestCase):
    def test_shell_syntax_and_detector_route(self) -> None:
        subprocess.run(["bash", "-n", str(SCRIPT)], check=True)
        text = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("pangram-lab detect-file", text)
        self.assertIn("--allow-public-cache", text)
        self.assertIn("romance-detector-repair-20260820.part2.pass2", text)
        self.assertIn("ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8", text)
        self.assertIn("Part 1 Pangram call:     NONE", text)
        self.assertNotIn("pangram-local run", text)
        self.assertNotIn("candidate-part-1.txt\" \\\n  --expect-sha", text)


if __name__ == "__main__":
    unittest.main()
