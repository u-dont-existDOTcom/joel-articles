"""Tests for the hypnosis guide's 4.1 edits list (articles/inner-signal/humanize/fix-20261020/apply_edits41.py): an edit is
applied once, whatever its shape (2026-10-21: an edit that adds a sentence after an installed one keeps the old text inside
the new, and the list would have applied it again on the next run)."""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'apply_edits41', ROOT / 'articles' / 'inner-signal' / 'humanize' / 'fix-20261020' / 'apply_edits41.py')
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)


def edit(key, old, new):
    return {'key': key, 'old': old, 'new': new}


class Apply(unittest.TestCase):
    def test_an_addition_after_an_installed_sentence_goes_in_once(self):
        md = 'One.\n\nIf it stops, do the above.\n\nThree.'
        e = edit('add', 'If it stops, do the above.', 'If it stops, do the above. Press your feet into a surface as well.')
        md1, applied, done = A.apply(md, [e])
        self.assertEqual(applied, ['add'])
        md2, applied2, done2 = A.apply(md1, [e])
        self.assertEqual((md2, applied2, done2), (md1, [], ['add']))
        self.assertEqual(md2.count('Press your feet'), 1)

    def test_a_cut_is_done_only_when_the_old_text_is_gone(self):
        md = 'Keep this. Cut this.'
        e = edit('cut', 'Keep this. Cut this.', 'Keep this.')
        md1, applied, _ = A.apply(md, [e])
        self.assertEqual((md1, applied), ('Keep this.', ['cut']))
        self.assertEqual(A.apply(md1, [e])[1:], ([], ['cut']))

    def test_a_replacement_and_a_changed_working_copy(self):
        e = edit('rep', 'a Protector', 'a protector part')
        md1, applied, _ = A.apply('it could be a Protector, or', [e])
        self.assertEqual((md1, applied), ('it could be a protector part, or', ['rep']))
        with self.assertRaises(SystemExit):
            A.apply('nothing of either here', [e])


if __name__ == '__main__':
    unittest.main()
