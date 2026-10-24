"""tools/humanization/html_text_edit.py: a paragraph's words change and its links and italics stay on their words (the
method of Nibbāna's batch n8, Joel's GPT edit of 2026-10-24, used again for the community article's 64 cuts)."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import html_text_edit as T  # noqa: E402


class SetTextTests(unittest.TestCase):
    def test_a_cut_before_a_link_keeps_the_link_on_its_words(self):
        inner = 'Community’s not a panacea, but it can help. See <a href="https://x.org/a">the advisory</a> &amp; more.'
        out, dropped, moved = T.set_text(inner, 'Community can help. See the advisory & more.')
        self.assertEqual(out, 'Community can help. See <a href="https://x.org/a">the advisory</a> &amp; more.')
        self.assertEqual((dropped, moved), ([], []))

    def test_italics_inside_a_changed_stretch_follow_their_words_or_are_dropped(self):
        out, dropped, _ = T.set_text('The later philosopher <em>Milindapañha</em> compared it.',
                                     'The later text Milindapañha compared it.')
        self.assertEqual(out, 'The later text <em>Milindapañha</em> compared it.')
        out, dropped, _ = T.set_text('He said it <em>jokingly</em> once.', 'He said it once.')
        self.assertEqual(out, 'He said it once.')
        self.assertEqual(dropped, ['<em>jokingly</em>'])

    def test_a_tag_that_crosses_a_change_grows_with_it_and_is_reported(self):
        out, _, moved = T.set_text('A <em>big red</em> barn', 'A big greenhouse')
        self.assertEqual(out, 'A <em>big greenhouse</em>')
        self.assertEqual(len(moved), 1)
        # words put in front of a tag go outside it (Nibbāna's n8 moved one back by hand, for its meaning)
        out, _, moved = T.set_text('<em>nibbāna is the fruition</em> of practice', 'When nibbāna is the fruition of practice')
        self.assertEqual(out, 'When <em>nibbāna is the fruition</em> of practice')

    def test_nesting_and_trailing_breaks_are_kept(self):
        out, _, _ = T.set_text('Read <em><a href="u">this</a></em> now.<br>', 'Please read this now.')
        self.assertEqual(out, 'Please read <em><a href="u">this</a></em> now.<br>')
        out, _, _ = T.set_text('Read <a href="u"><em>this</em></a> now.', 'Read this now.')
        self.assertEqual(out, 'Read <a href="u"><em>this</em></a> now.')

    def test_a_break_inside_a_paragraph_is_refused(self):
        with self.assertRaises(ValueError):
            T.set_text('one<br>two', 'one two')

    def test_paragraphs_lists_plain_text(self):
        doc = '<h2>H</h2><p>A <a href="u">link</a> &amp; text.</p><p>Two.</p>'
        self.assertEqual([p[4] for p in T.paragraphs(doc)], ['A link & text.', 'Two.'])


if __name__ == '__main__':
    unittest.main()
