"""tools/humanization/tell_panel.py: the tell panel's summary (E253 and E256 (Inner Child))."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import tell_panel as T  # noqa: E402

TEXT = 'We all have days like that. 🤗 Fear is the first guess, but maybe you didn\'t know how.'


class TellPanelTest(unittest.TestCase):
    def test_an_emoji_quote_is_found_in_its_sentence(self):
        joined = T.norm(' '.join(T.sentences(TEXT)))
        bounds, at = [], 0
        for s in T.sentences(TEXT):
            n = len(T.norm(s))
            bounds.append((at, at + n))
            at += n + 1
        spans, sents = T.locate('🤗', joined, bounds)
        self.assertEqual(sents, [1])

    def test_a_short_word_is_not_matched(self):
        joined = T.norm(TEXT)
        spans, sents = T.locate('how', joined, [(0, len(joined))])
        self.assertEqual(sents, [])

    def test_an_emoji_point_is_not_read_as_a_note_on_the_whole_paragraph(self):
        reply = 'AI:\n1. "🤗" - an emoji.\n\nWHOLE:\nThe rhythm is even.\n\nHUMAN:\nnone\n'
        self.assertEqual(T.whole_points(reply), ['The rhythm is even.'])

    def test_a_long_point_is_shown_whole_up_to_the_cap(self):
        long = 'x' * 900
        self.assertEqual(T.clip(long), long)
        self.assertTrue(T.clip('y' * 2000).endswith('[cut]'))


if __name__ == '__main__':
    unittest.main()
