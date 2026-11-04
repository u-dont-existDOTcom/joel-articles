import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
from typography_swap import swap_html, swap_text  # noqa: E402


class TypographySwap(unittest.TestCase):
    """Gate E337 (gut) (Joel, 2026-11-03 22:02 UTC: "yes make that swapping standard")."""

    def test_curly_marks_become_straight(self):
        self.assertEqual(swap_text('It’s “fine”, she said ‘ok’.')[0], 'It\'s "fine", she said \'ok\'.')

    def test_em_dash_becomes_his_spaced_en_dash(self):
        for before in ('the house—and the garden', 'the house — and the garden', 'the house —and the garden'):
            with self.subTest(before=before):
                self.assertEqual(swap_text(before)[0], 'the house – and the garden')

    def test_a_range_stays_a_range(self):
        self.assertEqual(swap_text('pages 10—20')[0], 'pages 10–20')

    def test_his_own_straight_marks_and_en_dashes_are_untouched(self):
        text = "I don't know – maybe \"later\"."
        self.assertEqual(swap_text(text), (text, 0))

    def test_html_attributes_and_scripts_are_left_alone(self):
        html = '<a href="x’y" title="“q”">it’s—here</a><script>var s = "—";</script>'
        out, n = swap_html(html)
        self.assertEqual(out, '<a href="x’y" title="“q”">it\'s – here</a><script>var s = "—";</script>')
        self.assertEqual(n, 2)


if __name__ == '__main__':
    unittest.main()
