"""Tests for tools/humanization/pangram_links_check.py: an AI result needs its check's link in the same paragraph."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import pangram_links_check as P  # noqa: E402


class Missing(unittest.TestCase):
    def test_ai_result_without_link_is_flagged(self):
        self.assertEqual(len(P.missing('The pair read AI on Pangram, 80% AI.')), 1)

    def test_pangram_page_link_passes(self):
        self.assertEqual(P.missing('It read AI Detected ([the check](https://www.pangram.com/feed/abc)).'), [])

    def test_api_check_heading_link_passes(self):
        # an API check has no Pangram page; its heading on the batch's API-CHECKS.md page is its link
        url = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/'
               'humanize/fix-20261023/n1/API-CHECKS.md#n1_science_t2')
        self.assertEqual(P.missing('The fix read AI on Pangram, 100%% AI ([the check](%s)).' % url), [])

    def test_other_github_page_does_not_pass(self):
        url = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/README.md'
        self.assertEqual(len(P.missing('It read AI on Pangram, 51%% AI ([notes](%s)).' % url)), 1)


if __name__ == '__main__':
    unittest.main()
