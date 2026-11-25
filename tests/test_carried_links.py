"""carried_links.py: a sentence brought from one of his posts into another comes with its links (lesson toc-2026-11-25f)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools', 'humanization'))
import carried_links as cl  # noqa: E402

SOURCE = (
    '<h2>Dip Your Toes In First</h2>'
    '<p>If being alone was a big part of what hurt during your childhood, I’d call somebody now, mess and all, since '
    'reaching toward people is part of taking care of your little one too. Even if you don’t have someone you know who '
    'wants to listen, there are <a href="https://www.warmline.org/">warmlines</a> for this (not hotlines unless it’s an '
    'emergency).</p>'
    '<p>For more, see my <a href="https://example.org/page">breathwork page</a>. By simply pursing your lips together on '
    'exhale, you can slow down your exhale.</p>'
    '<ul><li><p>Some massage therapies are super aggressive, like <a href="https://example.org/r"><em>Rolfing</em></a>, '
    'some are quite gentle. But they can know things you don’t and still be wrong for you.</p></li></ul>')


class CarriedLinks(unittest.TestCase):
    def test_the_link_inside_a_carried_sentence_is_found(self):
        r = cl.find(SOURCE, "Even if you don't have someone you know who wants to listen, there are warmlines for this "
                            "(not hotlines unless it's an emergency).")
        self.assertEqual(r['found'], 1.0)
        self.assertEqual([(l['words'], l['href']) for l in r['links']], [('warmlines', 'https://www.warmline.org/')])

    def test_a_link_elsewhere_in_the_paragraph_is_not_carried(self):
        r = cl.find(SOURCE, 'By simply pursing your lips together on exhale, you can slow down your exhale.')
        self.assertEqual((r['found'], r['links']), (1.0, []))

    def test_a_link_inside_a_list_item_and_emphasis(self):
        r = cl.find(SOURCE, 'Some massage therapies are super aggressive, like Rolfing, some are quite gentle.')
        self.assertEqual([(l['words'], l['href']) for l in r['links']], [('Rolfing', 'https://example.org/r')])

    def test_a_sentence_with_a_word_changed_is_found_in_part(self):
        # the carried sentence dropped his opening "But"
        r = cl.find(SOURCE, 'They can know things you don’t and still be wrong for you.')
        self.assertGreater(r['found'], 0.8)
        self.assertLess(r['found'], 1.0)

    def test_a_sentence_that_is_not_there(self):
        self.assertEqual(cl.find(SOURCE, 'Nothing like this sentence is anywhere in the source post at all.')['found'], 0.0)


if __name__ == '__main__':
    unittest.main()
