from __future__ import annotations

import unittest

from scripts.build_section_diff_manifest import manifest


class SectionDiffManifestTests(unittest.TestCase):
    def test_reports_only_changed_aligned_sections(self) -> None:
        source = "preamble\n\n# One\nalpha\n\n## Two\nbeta\n\n# Three\ngamma\n"
        candidate = "preamble\n\n# One\nalpha\n\n## Two\nbeta changed\n\n# Three\ngamma\n"
        data = manifest(source, candidate)
        self.assertEqual(data["heading_count"], 3)
        self.assertEqual(data["changed_section_count"], 1)
        row = data["changed_sections"][0]
        self.assertEqual(row["heading"], "Two")
        self.assertEqual(row["level"], 2)
        self.assertEqual(row["ordinal"], 1)
        self.assertNotEqual(row["source_sha256"], row["candidate_sha256"])

    def test_fails_closed_when_heading_sequence_differs(self) -> None:
        with self.assertRaises(RuntimeError):
            manifest("# One\na\n", "# Renamed\na\n")


if __name__ == "__main__":
    unittest.main()
