"""Tests for the owner-page checks of 2026-10-21 (Joel, 17:56 UTC): the file references he can't open
(tools/humanization/owner_refs_check.py) and the inner-figure sweep's prompt (tools/humanization/conflation_sweep_prompt.py)."""
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import conflation_sweep_prompt as C  # noqa: E402
import owner_refs_check as O  # noqa: E402


class OwnerRefs(unittest.TestCase):
    def test_a_backticked_repo_path_on_a_page_is_not_openable(self):
        """The questions page said the repeats lists were in `fix-20261020/b467/REPEATS.md`; Joel: "you didn't give links
        to click"."""
        page = 'The full lists are in `fix-20261020/b467/REPEATS.md` (16) and `fix-20261020/b467/part2/REPEATS.md` (14).'
        self.assertEqual(O.unresolved(page, []), ['fix-20261020/b467/REPEATS.md', 'fix-20261020/b467/part2/REPEATS.md'])

    def test_a_linked_path_and_a_fenced_command_pass(self):
        page = ('The full list: [the repeats, part A](https://github.com/o/r/blob/b/fix-20261020/b467/REPEATS.md), or '
                '[fix-20261020/b467/REPEATS.md](https://github.com/o/r/blob/b/fix-20261020/b467/REPEATS.md).\n\n'
                '```\npython3 tools/humanization/pangram_ledger.py status\n```\n')
        self.assertEqual(O.unresolved(page, []), [])

    def test_a_sent_file_counts_as_openable(self):
        self.assertEqual(O.unresolved('See report.md for the table.', ['/tmp/x/report.md']), [])
        self.assertEqual(O.unresolved('See report.md for the table.', []), ['report.md'])

    def test_the_command_line_fails_a_page_with_a_path(self):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'OWNER-QUESTIONS.md'
            f.write_text('Read `fix/VERIFY.md` first.\n', encoding='utf-8')
            self.assertEqual(O.main([str(f)]), 1)
            f.write_text('Read the [meaning check](https://github.com/o/r/blob/b/fix/VERIFY.md) first.\n', encoding='utf-8')
            self.assertEqual(O.main([str(f)]), 0)


class ConflationSweep(unittest.TestCase):
    def test_the_prompt_carries_the_map_the_example_and_every_kind(self):
        p = C.build('/a/ARTICLE.md', 'B3: "your Nurturer, your Protector"', '/a/SWEEP.md')
        for want in ('/a/ARTICLE.md', 'B3: "your Nurturer, your Protector"', 'The more consciously sculpted adult in you',
                     '(a)', '(b)', '(c)', '(d)', '(e)', '/a/SWEEP.md', 'either reading fits the map'):
            self.assertIn(want, p)

    def test_an_empty_map_is_refused(self):
        with self.assertRaises(ValueError):
            C.build('/a/ARTICLE.md', '  \n', '/a/SWEEP.md')

    def test_the_command_line_writes_the_prompt(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'A.md').write_text('# T\n\nThe adult in you can answer.\n', encoding='utf-8')
            (d / 'MAP.txt').write_text('B1: "the inherited parent"\n', encoding='utf-8')
            self.assertEqual(C.main(['--article', str(d / 'A.md'), '--map', str(d / 'MAP.txt'), '--report',
                                     str(d / 'R.md'), '--out', str(d / 'P.txt')]), 0)
            self.assertIn('the inherited parent', (d / 'P.txt').read_text(encoding='utf-8'))
            self.assertEqual(C.main(['--article', str(d / 'missing.md'), '--map', str(d / 'MAP.txt'), '--report',
                                     str(d / 'R.md'), '--out', str(d / 'P.txt')]), 2)


if __name__ == '__main__':
    unittest.main()
