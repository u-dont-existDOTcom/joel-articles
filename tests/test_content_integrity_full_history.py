import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/content-integrity.yml"


class ContentIntegrityFullHistoryTests(unittest.TestCase):
    def test_checkout_fetches_history_needed_for_blob_provenance(self):
        text = WORKFLOW.read_text(encoding="utf-8")
        pattern = re.compile(
            r"- name: Check out repository\n"
            r"\s+uses: actions/checkout@[^\n]+\n"
            r"\s+with:\n"
            r"\s+fetch-depth:\s*0(?:\n|$)"
        )
        self.assertRegex(text, pattern)


if __name__ == "__main__":
    unittest.main()
