import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import contradictions as C  # noqa: E402

EXTRACT = '''# EXTRACT

## 1. Doses and timings

### 1.1 Not a contradiction item
- line 3: "Take one at night."

## 2. Disagreements

### 2.1 Dose of the thing
- line 3: "Take one at night."
- line 9: "Take two at night."
- What differs: One says one, the other says two.
- Explained in the text: no

### 2.2 Showers
- line 12: "Hot showers calm you."
- line 20: "No hot showers."
- What differs: One uses hot showers, the other bars them.
- Explained in the text: yes, line 19, "In week three, stop the hot showers."
'''


class TestContradictions(unittest.TestCase):
    def test_parse_keeps_only_items_with_what_differs(self):
        items = C.parse(EXTRACT)
        self.assertEqual([it['id'] for it in items], ['2.1', '2.2'])
        self.assertEqual(items[0]['quotes'], [(3, 'Take one at night.'), (9, 'Take two at night.')])
        self.assertTrue(items[1]['explained'].startswith('yes'))

    def test_missing_fate_fails(self):
        ok, lines = C.check(EXTRACT, {'items': {'2.1': {'fate': 'question', 'ref': 'question 4'}}})
        self.assertFalse(ok)
        self.assertTrue(any('2.2' in l and 'no fate' in l for l in lines))

    def test_all_fates_pass_but_done_fails_while_one_is_open(self):
        fates = {'items': {'2.1': {'fate': 'question', 'ref': 'question 4'},
                           '2.2': {'fate': 'explained', 'ref': 'line 19'}}}
        self.assertTrue(C.check(EXTRACT, fates)[0])
        ok, lines = C.check(EXTRACT, fates, done=True)
        self.assertFalse(ok)
        self.assertTrue(any('still question' in l for l in lines))
        fates['items']['2.1'] = {'fate': 'answered', 'ref': 'APPLIED.json'}
        self.assertTrue(C.check(EXTRACT, fates, done=True)[0])

    def test_unknown_fate_empty_fate_and_stray_fate_fail(self):
        for f in ({'fate': 'fixed', 'ref': 'x'}, {'fate': 'answered'}):
            ok, _ = C.check(EXTRACT, {'items': {'2.1': f, '2.2': {'fate': 'explained', 'ref': 'line 19'}}})
            self.assertFalse(ok)
        ok, lines = C.check(EXTRACT, {'items': {'2.1': {'fate': 'answered', 'ref': 'a'},
                                                '2.2': {'fate': 'explained', 'ref': 'b'},
                                                '2.9': {'fate': 'answered', 'ref': 'c'}}})
        self.assertFalse(ok)

    def test_article_lists_changed_quotes(self):
        fates = {'items': {'2.1': {'fate': 'answered', 'ref': 'a'}, '2.2': {'fate': 'explained', 'ref': 'b'}}}
        art = 'Take one at night.\nHot showers calm you.\nNo hot showers.'
        ok, lines = C.check(EXTRACT, fates, art)
        self.assertTrue(ok)
        self.assertTrue(any(l.startswith('2.1:') and 'no longer in the article' in l for l in lines))

    def test_brief_numbers_every_line(self):
        with tempfile.TemporaryDirectory() as d:
            p = pathlib.Path(d) / 'a.md'
            p.write_text('# Title\n\nTake one at night.\n', encoding='utf-8')
            b = C.brief(p, 'a test article')
            self.assertIn('3: Take one at night.', b)
            self.assertIn('a test article', b)
            self.assertNotIn('__TEXT__', b)
            self.assertEqual(C.main(['brief', str(p), str(pathlib.Path(d) / 'out')]), 0)
            self.assertTrue((pathlib.Path(d) / 'out' / 'BRIEF.txt').exists())


if __name__ == '__main__':
    unittest.main()
