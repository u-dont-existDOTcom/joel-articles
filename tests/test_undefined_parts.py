"""undefined_parts.py: the parts and roles a guide doesn't define in its own words, which go to the author before any
sort (lesson inner-child-2026-11-20r)."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import undefined_parts as U  # noqa: E402

GUIDE = """# Building Your Inner Adult
## The Nurturer
### Ask God for a Loan
The dog kind of love is real love.
## The Inner Guide
As the Guide, you choose what your little one learns and what it gets to experience.
### Borrow Hindsight
Text.
```
# not a heading
```
"""


class UndefinedParts(unittest.TestCase):
    def test_a_part_or_role_with_no_text_of_its_own(self):
        found = U.undefined(U.from_markdown(GUIDE), min_words=1)
        self.assertEqual([f['heading'] for f in found], ['Building Your Inner Adult', 'The Nurturer'])
        self.assertEqual(found[1]['words'], 0)

    def test_a_short_text_counts_below_the_minimum(self):
        found = U.undefined(U.from_markdown(GUIDE), min_words=40)
        self.assertEqual([f['heading'] for f in found], ['Building Your Inner Adult', 'The Nurturer', 'The Inner Guide'])
        self.assertEqual(found[2]['words'], 16)
        self.assertTrue(found[2]['start'].startswith('As the Guide, you choose'))

    def test_a_heading_with_nothing_under_it_is_not_listed(self):
        self.assertEqual(U.undefined(U.from_markdown('# A\n## B\n## C\n'), 1),
                         [{'level': 1, 'heading': 'A', 'words': 0, 'start': ''}])

    def test_a_hash_inside_a_code_fence_is_not_a_heading(self):
        self.assertNotIn('not a heading', [s['heading'] for s in U.from_markdown(GUIDE)])

    def test_html(self):
        page = ('<h2>The Nurturer</h2><h3>Borrow <em>Love</em></h3><p>Some text.</p>'
                '<h2>The Guide</h2><p>As the Guide, you choose.</p><h3>Borrow Hindsight</h3><p>x</p>')
        secs = U.from_html(page)
        self.assertEqual(secs[1]['heading'], 'Borrow Love')
        self.assertEqual([f['heading'] for f in U.undefined(secs, min_words=1)], ['The Nurturer'])

    def test_captions_buttons_and_widgets_are_not_a_parts_own_text(self):
        page = ('<h1>Healing Old Patterns</h1>'
                '<div class="captioned-image-container"><figure><img src="x.png"><figcaption>My dad and me in '
                'Moscow</figcaption></figure></div>'
                '<div class="pullquote"><p>A line he repeats from the text below</p></div>'
                '<div class="subscription-widget-wrap"><p>Thanks for reading! Subscribe for free</p>'
                '<button>Subscribe</button></div>'
                '<h2>Re-do Trauma Memories</h2><p>Once you have your cast of characters, go back.</p>')
        found = U.undefined(U.from_html(page), min_words=1)
        self.assertEqual([(f['heading'], f['words']) for f in found], [('Healing Old Patterns', 0)])

    def test_substack_json(self):
        import json
        import tempfile
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump({'body_html': '<h2>The Nurturer</h2><h3>Borrow Love</h3><p>x</p>'}, f)
        import contextlib
        import io
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            U.main([f.name, '--substack-json', '--min-words', '1'])
        self.assertIn('- ## "The Nurturer": no text of its own', out.getvalue())

    def test_report(self):
        lines = U.report(U.undefined(U.from_markdown(GUIDE), 40), 5, 40)
        self.assertEqual(lines[2], '- ## "The Nurturer": no text of its own')
        self.assertEqual(lines[3], '- ## "The Inner Guide": 16 words: "As the Guide, you choose what your little one '
                                   'learns and what it gets to..."')


if __name__ == '__main__':
    unittest.main()
