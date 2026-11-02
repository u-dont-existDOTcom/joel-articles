"""pangram_api.py refuses a text bigger than six paragraphs or 1,200 words before anything is sent (Joel, 2026-10-23, E218:
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
    def test_six_paragraphs_go_seven_do_not(self):
        self.assertIsNone(pa.too_big('\n\n'.join([PARA] * 6)))
        self.assertIn('Substack', pa.too_big('\n\n'.join([PARA] * 7)))

    def test_headings_and_list_numbers_are_not_paragraphs(self):
        self.assertIsNone(pa.too_big('\n\n'.join(['A heading', PARA, '4.', PARA, PARA, PARA, PARA, PARA])))

    def test_more_than_1200_words_is_refused(self):
        self.assertIsNotNone(pa.too_big(' '.join(['word'] * 1201)))

    def test_check_refuses_before_sending_anything(self):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / 'TEXTS.json'
            f.write_text(json.dumps({'half': '\n\n'.join([PARA] * 40)}), encoding='utf-8')
            with self.assertRaises(SystemExit) as e:
                pa.check(str(f), str(pathlib.Path(d) / 'out'))
            self.assertIn('REFUSED, nothing sent', str(e.exception))
            self.assertFalse((pathlib.Path(d) / 'out').exists())


if __name__ == '__main__':
    unittest.main()
