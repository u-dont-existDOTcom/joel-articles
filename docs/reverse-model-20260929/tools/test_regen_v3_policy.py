import unittest
from regen_v3_policy import copy_guard, parse_chinese_notes, qualified_keep


class RegenerationV3PolicyTest(unittest.TestCase):
    def test_chinese_notes_have_separate_form_keep_and_content(self):
        parsed, issue = parse_chinese_notes('FORM: first-person letter\nKEEP:\n- Rochester\nNOTES:\n1. 我写信解释两个朋友之间发生的事情以及为什么我对此感到非常担心。')
        self.assertIsNone(issue)
        self.assertEqual(parsed['form'], 'first-person letter')
        self.assertEqual(parsed['keep'], ['Rochester'])
        self.assertNotIn('KEEP:', parsed['notes'])

    def test_protected_title_does_not_rescue_copied_prose(self):
        source = ('A critic discussed Memento Mori, The Prime of Miss Jean Brodie and A Far Cry From Kensington. '
                  'The critic then explained that the wording of the review should not be copied into another text without changing it.')
        title = 'Memento Mori, The Prime of Miss Jean Brodie'
        clean = copy_guard(source, '这个评论主要讨论了作品的名称以及读者如何理解它。 '+title,
                           'The review discusses '+title+' and its readers.', [title])
        self.assertTrue(clean['passed'])
        copied = copy_guard(source, '这个评论讨论作品。 '+title,
                            'The critic then explained that the wording of the review should not be copied into another text without changing it.', [title])
        self.assertFalse(copied['passed'])
        self.assertGreater(copied['draft_longest_run'], 10)

    def test_exempt_share_and_list_guard(self):
        source = 'Paris London Berlin Madrid Rome Lisbon Oslo Athens Vienna Prague Warsaw Dublin Helsinki Stockholm'
        chosen, share, rejected = qualified_keep(source, ['Paris London Berlin Madrid Rome Lisbon Oslo Athens'])
        self.assertEqual(chosen, [])
        self.assertEqual(share, 0)
        self.assertEqual(rejected[0]['reason'], 'combined_share_exceeded')
        checked = copy_guard('An artist wrote about Paris and her trip.', '旅程与巴黎的画家有关而且内容值得解释。 Paris',
                             '- The artist went to Paris.', ['Paris'])
        self.assertFalse(checked['passed'])
        self.assertTrue(checked['draft_has_list_markers'])


if __name__ == '__main__':
    unittest.main()
