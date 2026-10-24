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


class SelfContainedQuestions(unittest.TestCase):
    """E257 (Inner Child; Joel, 2026-10-24 22:55 UTC: "i hope you know i have no idea at this point what my 100.6 was")."""
    PAGE = ('# Questions\n\n## Open questions\n\n### 🟣 102. Two things (turn 105)\n\n%s\n\n'
            '## For you to do (no decision needed)\n\n### 🔵 Round 6 (turn 101)\n\n%s\n\n'
            '## Decided\n\n### 🟢 101, 2026-10-24 18:40 UTC\n\nAnswered, with 100.6 in it.\n\n'
            '### 🟢 96 to 99, 2026-10-23 21:52 UTC\n\nOld.\n\n### 🟢 78.2, 84 and 85, 2026-10-22 21:35 UTC\n\nOld.\n')

    def test_an_old_number_alone_is_refused(self):
        for line in ('- **102.3 Four sections (your 100.6, still open).** A or B?', '- **102.1** the way 97.8 went.',
                     '- see question 85 for that.', '- **102.2 98.2, your P5.**'):
            self.assertTrue(Q.old_number_refs(self.PAGE % (line, 'It waits.')), line)

    def test_its_own_items_quotes_links_and_decided_text_pass(self):
        for line in ('- **102.1 When to Change the Strategy\'s last paragraph.** "your 100.6" was his phrase. 102.2 is next.',
                     '- the [check](https://github.com/x/t97-api/API-CHECKS.md#t98_7) reads Human at 0.0000% AI, Pangram 4.1.',
                     '- sections 12.2 and 13.1 of the book.'):
            self.assertEqual(Q.old_number_refs(self.PAGE % (line, 'It waits.')), [], line)

    def test_the_to_do_list_is_checked_too(self):
        self.assertTrue(Q.old_number_refs(self.PAGE % ('- A or B?', 'It waits for your answer to question 99.')))


if __name__ == '__main__':
    unittest.main()
