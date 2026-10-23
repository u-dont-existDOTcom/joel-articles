"""tools/humanization/clarity_read.py: the whole-article clarity read (Joel, 2026-10-23 16:55 UTC: "let's make sure this
kind of check is standard for articles as we write them and as we finalize before publishing in future")."""
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402

ARTICLE_HTML = ('<div class="body markup"><h1>One</h1><p>First paragraph about “unification” here.</p>'
                '<div class="captioned-image-container"><figure><img src="x.png"><figcaption>A caption</figcaption></figure></div>'
                '<p>https://example.substack.com/p/a-card</p><h2>Two</h2><p>' + 'Second section text. ' * 30 + '</p>'
                '<ul><li><p>An item.</p></li></ul><h2>Three</h2><p>' + 'Third section text. ' * 30 + '</p></div>')

READER = '''## 1
QUOTE: First paragraph about “unification” here.
HARD: "unification" is never explained.
SCORE: 3
PLAIN: First paragraph about "unification" (gathering the mind into one) here.

## 2
QUOTE: A sentence the reader made up.
HARD: something
SCORE: 2
PLAIN: something plainer
'''


class ClarityReadTests(unittest.TestCase):
    def test_reading_text_keeps_headings_and_paragraphs_and_skips_images_and_cards(self):
        t = C.reading_text(ARTICLE_HTML, 'html')
        lines = t.split('\n')
        self.assertEqual(lines[0], '## One')
        self.assertIn('First paragraph about “unification” here.', lines)
        self.assertNotIn('A caption', t)
        self.assertNotIn('https://example.substack.com', t)
        self.assertIn('- An item.', lines)

    def test_parts_start_at_headings_and_cover_everything(self):
        t = C.reading_text(ARTICLE_HTML, 'html')
        ps = C.split_parts(t, 3)
        self.assertEqual('\n'.join(ps), t)
        for p in ps[1:]:
            self.assertTrue(p.startswith('## '), p[:30])

    def test_make_collect_and_page(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            art = d / 'a.html'
            art.write_text(ARTICLE_HTML, encoding='utf-8')
            out = d / 'clarity'
            C.make(art, out, parts=2, about='a test article', question='Is anything unclear?')
            brief = (out / 'BRIEF-1.txt').read_text(encoding='utf-8')
            self.assertIn('part 1 of 2 of a test article', brief)
            self.assertIn('Compression.', brief)  # Joel's examples are in every brief
            self.assertIn('no summing-up line', brief)
            (out / 'READER-1.md').write_text(READER, encoding='utf-8')
            (out / 'READER-2.md').write_text('NOTHING\n', encoding='utf-8')
            items = C.collect(out)
            self.assertEqual(len(items), 2)
            self.assertTrue(items[0]['found'])
            self.assertEqual(items[0]['heading'], 'One')
            self.assertFalse(items[1]['found'])
            # the worker's whole-article check is kept when the readers' reports are collected again
            items[1]['status'] = 'drop'
            items[1]['note'] = 'not in the article'
            (out / 'ITEMS.json').write_text(json.dumps(items), encoding='utf-8')
            items = C.collect(out)
            self.assertEqual(items[1]['status'], 'drop')
            md, n = C.page(out, title='T')
            self.assertEqual(n, 1)
            self.assertIn('### 1. One', md)
            self.assertIn('## Flagged but not counted', md)

    def test_a_quote_is_found_when_only_its_quote_marks_differ(self):
        self.assertEqual(C.locate('## H\nHe said "yes" there.', 'He said “yes” there.'), (2, 'H'))
        self.assertIsNone(C.locate('## H\nx\nx', 'x'))


if __name__ == '__main__':
    unittest.main()
