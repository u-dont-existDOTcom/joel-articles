"""The Inner Child questions page refuses an open question that says a stretch reads AI without linking the check (E214).

Joel, 2026-10-22 23:54 UTC: "can you please always give me the links to the checks you want me to copy and fix? i thought
that was a rule already."
"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'articles' / 'inner-child-therapy' / 'tools'))
import questions_page as Q  # noqa: E402

HEAD = '# Questions\n\n## Open questions\n\n'
TAIL = '\n## Decided\n\n### 🟢 Old\n\nThat paragraph still reads AI, long ago.\n'


class LinkedChecks(unittest.TestCase):
    def test_an_ai_reading_without_a_link_is_refused(self):
        md = HEAD + '### 🟣 88. What still reads AI\n\nP4\'s questions read High.\n' + TAIL
        self.assertEqual(Q.unlinked_ai_asks(md), ['### 🟣 88. What still reads AI'])

    def test_a_feed_or_history_link_or_a_results_or_checks_page_passes(self):
        for link in ('https://www.pangram.com/feed/f0a788bc-07a4-411d-bd1b-292c7370c630',
                     'https://www.pangram.com/history/ac67756a-4621-44c6-8d06-84ce60f24a64',
                     'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/x/t97-results/API-RESULTS.md',
                     'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/x/t97-api/API-CHECKS.md#t97b_parent'):
            md = HEAD + '### 🟣 88. What still reads AI\n\nP4 read High (part 5 of 9): %s\n' % link + TAIL
            self.assertEqual(Q.unlinked_ai_asks(md), [], link)

    def test_a_pricing_link_is_not_a_check(self):
        md = HEAD + ('### 🟣 88. Credit\n\nThis read AI; the price is on '
                     'https://www.pangram.com/knowledge-hub/what-is-pangrams-developers-plan\n') + TAIL
        self.assertEqual(Q.unlinked_ai_asks(md), ['### 🟣 88. Credit'])

    def test_only_open_questions_are_checked(self):
        md = HEAD + '### 🟣 88. A choice\n\nA or B?\n' + TAIL
        self.assertEqual(Q.unlinked_ai_asks(md), [])


if __name__ == '__main__':
    unittest.main()
