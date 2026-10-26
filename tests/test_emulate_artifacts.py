"""The strict Emulate check (tools/humanization/emulate_artifacts.py): each check on a small case, and the fixes keep
links and italics. Joel, 2026-10-25 19:42 UTC: "make those emulate checks more strict pls for future also"."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import emulate_artifacts as ea  # noqa: E402


class Case:
    def __init__(self, article, source, allowed=None, article_name='article.md', source_name='his.md'):
        self.dir = tempfile.TemporaryDirectory()
        d = pathlib.Path(self.dir.name)
        self.article = d / article_name
        self.article.write_text(article, encoding='utf-8')
        self.source = d / source_name
        self.source.write_text(source, encoding='utf-8')
        self.allowed = []
        if allowed:
            a = d / 'allowed.txt'
            a.write_text(allowed, encoding='utf-8')
            self.allowed = [a]
        self.out = d / 'out'
        self.record = ea.audit(self.article, [self.source], self.allowed, self.out, parts=2)

    def kinds(self, kind):
        return [f for f in self.record['findings'] if f['kind'] == kind]

    def fixed(self, kinds=None):
        out = pathlib.Path(self.dir.name) / ('fixed' + self.article.suffix)
        ea.fix(self.article, self.out / 'AUDIT.json', out, kinds)
        return out.read_text(encoding='utf-8')


HIS = ('# Learning\n\nRead the book first, then practice for a few minutes every day.\n\n'
       'Let it take its time, and come back when you are ready.\n\n'
       'Work with the inner child here, gently and without force.\n\n'
       'Maggie Phillips and Claire Frederick, *Healing the Divided Self* (1995), especially pp.24–27, covers this.\n\n'
       '[Twin Oaks](https://twinoaks.org/) and other communities receive visitors in the summer.\n')


class TestEmulateArtifacts(unittest.TestCase):
    def test_his_paragraphs_are_skipped(self):
        c = Case(HIS, HIS)
        self.assertEqual(c.record['checked'], 0)
        self.assertEqual(c.record['findings'], [])

    def test_space_before_punctuation_is_found_and_fixed(self):
        c = Case('# Learning\n\nRead the book first , then practice for a few minutes every day .\n', HIS)
        sp = c.kinds('space-before-punct')
        self.assertEqual(len(sp), 2)
        self.assertTrue(all(f['auto'] for f in sp))
        self.assertIn('Read the book first, then practice for a few minutes every day.', c.fixed())

    def test_a_space_his_own_text_has_is_left_alone(self):
        c = Case('# Learning\n\nThis is mine , really mine and nobody else.\n', HIS + '\nThis is mine , truly.\n')
        self.assertEqual(c.kinds('space-before-punct'), [])

    def test_ellipsis_then_full_stop(self):
        c = Case('# Learning\n\nStop the induction and do something else… . Whatever you do, come back.\n', HIS)
        self.assertIn('do something else… Whatever you do', c.fixed())

    def test_confusable_where_his_line_has_the_other_word(self):
        c = Case("# Learning\n\nLet it take it's time, and come back when you are ready.\n", HIS)
        conf = c.kinds('confusable')
        self.assertEqual(len(conf), 1)
        self.assertEqual(conf[0]['strength'], 'likely')
        self.assertIn('its', conf[0]['note'])

    def test_scare_quotes_his_line_does_not_have(self):
        c = Case('# Learning\n\nWork with the "inner child" here, gently and without any force.\n', HIS)
        q = c.kinds('quote-marks')
        self.assertEqual(len(q), 1)
        self.assertEqual(q[0]['strength'], 'likely')
        self.assertIn('"inner child"', c.fixed())   # not a mechanical fix: it waits for a decision
        self.assertIn('Work with the inner child here, gently', c.fixed(['quote-marks']))

    def test_citation_that_lost_its_italics_and_pages(self):
        c = Case('# Learning\n\nHealing the Divided Self , Maggie Phillips and Claire Frederick, (1995) pp 24-27 covers it.\n',
                 HIS)
        cit = c.kinds('citation')
        self.assertEqual(len(cit), 1)
        self.assertIn('italics', cit[0]['note'])
        self.assertIn('punctuation', cit[0]['note'])

    def test_a_reference_none_of_his_texts_has(self):
        c = Case('# Learning\n\nA 2019 study by Brooke and Smith found that this works for most people.\n', HIS)
        cit = c.kinds('citation')
        self.assertEqual(len(cit), 1)
        self.assertIn('none of his texts', cit[0]['note'])

    def test_a_link_his_paragraph_had(self):
        c = Case('# Learning\n\nTwin Oaks and other communities receive visitors in the summer months.\n', HIS)
        links = c.kinds('link')
        self.assertTrue(any('twinoaks.org' in f['note'] for f in links))

    def test_numbers_and_new_sentences(self):
        c = Case('# Learning\n\nRead the book first, then practice for 5 minutes every day.\n\n'
                 'My friend Brooke bought $500 boots for the retreat last year.\n', HIS)
        self.assertEqual(len(c.kinds('number')), 1)
        self.assertTrue(any('Brooke' in f['text'] for f in c.kinds('new-sentence')))

    def test_allowed_words_are_not_reported(self):
        c = Case('# Learning\n\nMy friend Brooke bought $500 boots for the retreat last year.\n', HIS,
                 allowed='My friend Brooke bought $500 boots for the retreat last year.')
        self.assertEqual(c.record['checked'], 0)

    def test_html_fix_keeps_links_and_italics(self):
        art = ('<h2>Learning</h2><p><a href="https://example.org/book"><em>Healing the Divided Self</em></a> , '
               'Phillips and Frederick, covers it all here .</p>')
        c = Case(art, HIS, article_name='article.html')
        out = c.fixed()
        self.assertIn('<a href="https://example.org/book"><em>Healing the Divided Self</em></a>, Phillips', out)
        self.assertIn('covers it all here.</p>', out)

    def test_pairs_give_his_paragraph(self):
        c = Case('# Learning\n\nFirst read the book, and then every day practice for a few minutes.\n', HIS)
        pairs = json.loads((c.out / 'PAIRS.json').read_text(encoding='utf-8'))
        self.assertEqual(len(pairs), 1)
        self.assertIn('Read the book first', pairs[0]['his'][0]['text'])
        self.assertTrue((c.out / 'PAIRS-1.txt').exists())

    def test_align_blocks_keeps_order_and_finds_a_move(self):
        src = [{'text': t} for t in ('apples oranges pears', 'cats dogs horses', 'rivers lakes oceans', 'red green blue')]
        art = [{'text': t} for t in ('apples oranges plums', 'rivers lakes seas', 'cats dogs cows', 'red green yellow')]
        m = ea.align_blocks(art, src)
        self.assertEqual(m[0], [0])
        self.assertEqual(m[3], [3])
        self.assertIn(m[1], ([2], [1, 2], [2, 3]))
        self.assertTrue(m[2])


if __name__ == '__main__':
    unittest.main()
