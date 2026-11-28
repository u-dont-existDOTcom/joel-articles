"""pangram_api.py warns on a text bigger than six paragraphs or 1,200 words and refuses, before anything is sent, only half an
article or more (rules audit 2026-11-28, card C07, approved; Joel, 2026-10-23, E218:
"not more than like 5-6 paras at a time in general (not half an  article)"; 2026-11-02 20:38 UTC, after four halves of
the hypnosis guide went through the API: "that should be done the free way to not waste my pangram credits", E325)."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import pangram_api as pa  # noqa: E402

PARA = 'This is a paragraph of more than eight words, as a test needs it to be.'


class SizeGuard(unittest.TestCase):
    def test_six_paragraphs_go_seven_warn(self):
        self.assertIsNone(pa.size_warning('\n\n'.join([PARA] * 6)))
        self.assertIsNone(pa.too_big('\n\n'.join([PARA] * 7)))        # a warning, no longer a refusal
        self.assertIn('7 paragraphs', pa.size_warning('\n\n'.join([PARA] * 7)))

    def test_headings_and_list_numbers_are_not_paragraphs(self):
        self.assertIsNone(pa.size_warning('\n\n'.join(['A heading', PARA, '4.', PARA, PARA, PARA, PARA, PARA])))

    def test_more_than_1200_words_warns(self):
        self.assertIsNotNone(pa.size_warning(' '.join(['word'] * 1201)))
        self.assertIsNone(pa.too_big(' '.join(['word'] * 1201)))

    def test_half_an_article_is_refused_when_its_length_is_known(self):
        text = '\n\n'.join([PARA] * 40)                              # 40 paragraphs, 560 words
        words = len(text.split())
        self.assertIn('Substack', pa.too_big(text, article_words=words * 2))      # exactly half
        self.assertIn('Substack', pa.too_big(text, article_words=words))          # the whole of it
        self.assertIsNone(pa.too_big(text, article_words=words * 4))              # a quarter
        self.assertIsNone(pa.too_big(PARA, article_words=10))                     # small texts only warn

    def test_without_the_articles_length_only_above_3000_words_is_refused(self):
        self.assertIsNone(pa.too_big(' '.join(['word'] * 3000)))
        self.assertIn('Substack', pa.too_big(' '.join(['word'] * 3001)))

    def test_check_refuses_before_sending_anything(self):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'TEXTS.json'
            f.write_text(json.dumps({'half': '\n\n'.join([PARA] * 400)}), encoding='utf-8')   # over 3,000 words
            with self.assertRaises(SystemExit) as e:
                pa.check(str(f), str(pathlib.Path(d) / 'out'))
            self.assertIn('REFUSED, nothing sent', str(e.exception))
            self.assertFalse((pathlib.Path(d) / 'out').exists())

    def test_check_warns_and_goes_on_for_seven_paragraphs(self):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'TEXTS.json'
            f.write_text(json.dumps({'seven': '\n\n'.join([PARA] * 7)}), encoding='utf-8')
            sent = []
            orig = pa.request
            pa.request = lambda *a, **k: (sent.append(a) or (500, {}))   # stops after the first POST
            try:
                with self.assertRaises(SystemExit) as e:
                    pa.check(str(f), str(pathlib.Path(d) / 'out'))
            finally:
                pa.request = orig
            self.assertNotIn('REFUSED', str(e.exception))
            self.assertEqual(len(sent), 1)                                 # it got as far as the POST


if __name__ == '__main__':
    unittest.main()
