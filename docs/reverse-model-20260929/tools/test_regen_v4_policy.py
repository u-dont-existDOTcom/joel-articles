import unittest
from regen_v4_policy import chinese_fraction, roundtrip_guard, source_latin_runs


class RoundTripPolicyTest(unittest.TestCase):
    def test_chinese_fraction_removes_only_source_matching_runs(self):
        source = 'The author discussed Paris and then left.'
        check = chinese_fraction(source, '作者谈到 Paris，随后离开。')
        self.assertEqual(check['removed_source_latin_runs'], ['Paris'])
        self.assertTrue(check['passed'])
        self.assertFalse(chinese_fraction(source, 'The author discussed Paris and then left.')['passed'])
        self.assertFalse(chinese_fraction(source, '作者说 unmentioned English words and more.')['passed'])

    def test_source_strings_protected_but_copied_prose_rejected(self):
        source = ('A reviewer said Memento Mori was challenging. The reviewer then explained in many words '
                  'why this lengthy sentence must be rewritten rather than copied straight into another text.')
        translation = '评论家认为 Memento Mori 很有挑战性。'
        self.assertIn('Memento Mori', [r for _, _, r in source_latin_runs(source, translation)])
        clean = roundtrip_guard(source, translation, 'The reviewer found Memento Mori challenging.')
        self.assertTrue(clean['passed'])
        copied = roundtrip_guard(source, translation,
            'The reviewer then explained in many words why this lengthy sentence must be rewritten rather than copied straight into another text.')
        self.assertFalse(copied['passed'])
        self.assertGreater(copied['draft_longest_run'], 10)


if __name__ == '__main__':
    unittest.main()
