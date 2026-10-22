"""The rebuild of the text a Substack post's Pangram check reads (tools/humanization/substack_check_text.py).

The rules below were found on the Nibbana post's check of 2026-10-20, rebuilt from Joel's editor HTML of 2026-10-22:
an embedded Substack note keeps its straight quotes, trailing spaces go, and so do the emoji joiners and presentation
selectors.
"""
import importlib.util
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import substack_check_text as S  # noqa: E402


@unittest.skipUnless(importlib.util.find_spec('bs4'), 'needs BeautifulSoup (CI installs nothing)')
class CheckedText(unittest.TestCase):
    def test_paragraphs_are_curled_but_a_note_keeps_straight_quotes(self):
        html = ('<div class="body"><p>He said "yes" and it\'s done.</p>'
                '<div class="FeedProseMirror"><p>A note says "no" and it\'s fine.</p></div></div>')
        self.assertEqual(S.checked_text(html),
                         'He said “yes” and it’s done.\nA note says "no" and it\'s fine.')

    def test_trailing_spaces_and_emoji_joiners_go(self):
        html = '<div class="body"><p>Love ❤️  </p><p>Fog \U0001f636‍\U0001f32b️</p></div>'
        self.assertEqual(S.checked_text(html), 'Love ❤\nFog \U0001f636\U0001f32b')

    def test_a_bare_link_becomes_its_embed_lines_curled(self):
        html = '<div class="body"><p>Before</p><p>https://example.com/x</p><p>After</p></div>'
        self.assertEqual(S.checked_text(html, embeds={'https://example.com/x': ['An "embed" line']}),
                         'Before\nAn “embed” line\nAfter')

    def test_list_items_and_skipped_images(self):
        html = ('<div class="body"><ul><li>One "a"</li><li><p>Two</p></li></ul>'
                '<div class="captioned-image-container"><p>caption</p></div><p>End</p></div>')
        self.assertEqual(S.checked_text(html), 'One “a”\nTwo\nEnd')


if __name__ == '__main__':
    unittest.main()
