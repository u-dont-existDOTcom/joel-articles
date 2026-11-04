import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
from typography_swap import swap_html, swap_text  # noqa: E402


class TypographySwap(unittest.TestCase):
    """Gate E337 (gut) (Joel, 2026-11-03 22:02 UTC: "yes make that swapping standard"), and E353 (Inner Child) for the
    dashes (2026-11-04 16:30 UTC: his two hyphens, "--", with no spaces, in every article)."""

    def test_curly_marks_become_straight(self):
        self.assertEqual(swap_text('It’s “fine”, she said ‘ok’.')[0], 'It\'s "fine", she said \'ok\'.')

    def test_em_dash_becomes_his_two_hyphens(self):
        for before in ('the house—and the garden', 'the house — and the garden', 'the house —and the garden'):
            with self.subTest(before=before):
                self.assertEqual(swap_text(before), ('the house--and the garden', 1))

    def test_a_spaced_en_dash_becomes_his_two_hyphens_too(self):
        # what the swap made until 2026-11-04, and his own " – "s ("bigger – perhaps much bigger – than")
        self.assertEqual(swap_text('bigger – perhaps much bigger – than'), ('bigger--perhaps much bigger--than', 2))
        self.assertEqual(swap_text('On ne change pas – "we don\'t change."')[0], 'On ne change pas--"we don\'t change."')

    def test_his_own_two_hyphens_and_straight_marks_are_untouched(self):
        text = "I don't know--maybe \"later\", as in handling--we see."
        self.assertEqual(swap_text(text), (text, 0))

    def test_a_range_stays_a_range(self):
        self.assertEqual(swap_text('pages 10—20')[0], 'pages 10–20')
        for text in ('1990–2000', 'NAC: 1.8g – 2.4g (divided doses).', '10 – 20 minutes'):
            with self.subTest(text=text):
                self.assertEqual(swap_text(text), (text, 0))

    def test_a_dash_at_a_line_edge_keeps_a_space_toward_its_words(self):
        self.assertEqual(swap_text('— Rumi')[0], '-- Rumi')
        self.assertEqual(swap_text('a line ending —\nnext')[0], 'a line ending --\nnext')

    def test_html_attributes_and_scripts_are_left_alone(self):
        html = '<a href="x’y" title="“q”">it’s—here</a><script>var s = "—";</script>'
        out, n = swap_html(html)
        self.assertEqual(out, '<a href="x’y" title="“q”">it\'s--here</a><script>var s = "—";</script>')
        self.assertEqual(n, 2)


if __name__ == '__main__':
    unittest.main()
