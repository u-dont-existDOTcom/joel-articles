import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORE = ROOT / ".gitleaksignore"

EXPECTED_FINGERPRINTS = {
    "9b85154309c90bef820923b43d44ea1222b4a91d:.github/workflows/update-inner-signal-infographics.yml:generic-api-key:67",
    "9b85154309c90bef820923b43d44ea1222b4a91d:.github/workflows/update-inner-signal-infographics.yml:generic-api-key:73",
    "defc51d43fa291dcb00c93468e111c967094164a:articles/inner-signal/INFOGRAPHIC-UPDATE-RECEIPT.json:generic-api-key:10",
    "defc51d43fa291dcb00c93468e111c967094164a:articles/inner-signal/INFOGRAPHIC-UPDATE-RECEIPT.json:generic-api-key:19",
    "4229009b35f9cdff71d835d2a6c7df398fa15206:state/CODEX-CURRENT-STATE.md:generic-api-key:31",
    "0ff49c99fdfe275b596bda72c1338f80fec14941:state/CODEX-CURRENT-STATE.md:generic-api-key:31",
    "hosted/actions/run-34550531021.log:generic-api-key:330",
    "hosted/actions/run-34550531021.log:generic-api-key:336",
}


class GitleaksAdjudicationTests(unittest.TestCase):
    def test_ignore_file_contains_only_approved_exact_fingerprints(self) -> None:
        lines = {
            line.strip()
            for line in IGNORE.read_text(encoding="utf-8").splitlines()
            if line.strip()
        }
        self.assertEqual(lines, EXPECTED_FINGERPRINTS)

    def test_fingerprints_are_finding_specific(self) -> None:
        pattern = re.compile(
            r"^(?:[0-9a-f]{40}:[^:*?\[\]]+|hosted/actions/run-[0-9]+\.log)"
            r":generic-api-key:[1-9][0-9]*$"
        )
        for fingerprint in EXPECTED_FINGERPRINTS:
            with self.subTest(fingerprint=fingerprint):
                self.assertRegex(fingerprint, pattern)


if __name__ == "__main__":
    unittest.main()
