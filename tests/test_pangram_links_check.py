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


class HelpRequests(unittest.TestCase):
    # E253 (Inner Child): a help request with tells links the tell panel's record (Joel, 2026-10-23 23:21 UTC:
    # "so why don't you fix your process before asking for help")
    def test_help_request_without_panel_is_flagged(self):
        ask = "I can't find any more AI tells here. Can you help show me the tells I'm missing?"
        self.assertEqual(len(P.unpaneled_help(ask)), 1)

    def test_help_request_with_panel_passes(self):
        url = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/x/articles/inner-child-therapy/experiments/'
               't104-panel/97_8-d3/PANEL.md')
        ask = "Three readers' tells are [here](%s). Can you help show me the tells I'm missing?" % url
        self.assertEqual(P.unpaneled_help(ask), [])

    def test_other_text_is_not_a_help_request(self):
        self.assertEqual(P.unpaneled_help('The linter flags tells in my sentences, and a list of three reads AI.'), [])


if __name__ == '__main__':
    unittest.main()
