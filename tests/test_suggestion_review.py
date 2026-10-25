"""tools/humanization/suggestion_review.py: the whole article with every suggestion marked where it applies (Joel,
2026-10-25 14:40 UTC: "why don't you give me the full HTML guide with highlighting where you notice x,y,z type of problems
(color-coded) and your suggestion for that and then my comment box on your suggestion with approve reject reivse buttons")."""
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import clarity_read  # noqa: E402
import suggestion_review as R  # noqa: E402

MD = '''# A heading

[image 1](https://example.com/a.png)

[Subscribe now](%%checkout_url%%)

This is the first paragraph. It has a [link here](https://example.com/x) and “curly quotes”. As I said, it repeats.

## A subheading

- A list item.

Double click to interact with video

The last paragraph says something, then it says it again.
'''


def review(suggestions):
    return {'format': R.FORMAT, 'review_id': 'test-review', 'title': 'Test Review', 'intro': ['Hello.'],
            'article': {'file': 'x.md', 'sha256': 'f' * 64}, 'built': 'now',
            'types': {'caveat': {'label': 'Caveats', 'about': 'a'}, 'structure': {'label': 'Headings', 'about': 'b'}},
            'suggestions': suggestions}


class SuggestionReviewTests(unittest.TestCase):
    def setUp(self):
        self.bl = R.blocks(MD)

    def test_blocks_number_paragraphs_and_mark_native_objects(self):
        kinds = [(b['kind'], b['native'], b['pn']) for b in self.bl]
        self.assertEqual(kinds[0], ('h1', None, None))
        self.assertEqual(kinds[1][1], 'image 1')
        self.assertEqual(kinds[2][1], 'subscribe button')
        para = self.bl[3]
        self.assertEqual(para['pn'], 'P3')
        self.assertIn('link here', para['text'])
        self.assertNotIn('](', para['text'])
        self.assertEqual(self.bl[6]['native'], 'video')
        self.assertEqual(self.bl[7]['section'], 'A subheading')

    def test_a_quote_is_found_with_other_quote_marks_and_spacing(self):
        i, s, e = R.find_quote(self.bl, 'and "curly quotes".')
        self.assertEqual(self.bl[i]['text'][s:e], 'and “curly quotes”.')
        with self.assertRaises(ValueError):
            R.find_quote(self.bl, 'words that are not there')

    def test_a_cut_is_tidied_only_where_it_joins(self):
        line = 'Keep this , untouched. Cut me here. And the rest!'
        s = line.index('Cut me here.')
        self.assertEqual(R.cut_text(line, s, s + len('Cut me here.')), 'Keep this , untouched. And the rest!')
        line2 = 'One thing (a parenthetical) or it may be nothing!'
        s2 = line2.index(' or it may be nothing!')
        self.assertEqual(R.cut_text(line2, s2, len(line2)), 'One thing (a parenthetical)!')

    def test_check_finds_a_before_text_that_is_not_the_articles(self):
        para = self.bl[3]
        good = {'id': 'CV-1.1', 'type': 'caveat', 'title': 'A cut', 'advice': 'approve',
                'spans': [{'block': 3, 'start': para['text'].index('As I said'), 'end': len(para['text'])}],
                'edits': [{'block': 3, 'before': para['text'], 'after': para['text'].replace(' As I said, it repeats.', '')}],
                'inserts': [], 'moves': [], 'what': 'Cuts it.', 'why': 'Said already.', 'stays': 'The rest.',
                'deciding': 'Approve cuts it.'}
        self.assertEqual(R.check(review([good]), self.bl), [])
        bad = dict(good, id='CV-1.2', edits=[{'block': 3, 'before': 'not the text', 'after': 'x'}])
        self.assertTrue(any('before-text' in p for p in R.check(review([bad]), self.bl)))
        vague = dict(good, id='CV-1.3', what='')
        self.assertTrue(any('no what' in p for p in R.check(review([vague]), self.bl)))

    def test_the_page_marks_the_words_and_carries_the_cards_and_the_form_controls(self):
        para = self.bl[3]
        s = {'id': 'CV-1.1', 'type': 'caveat', 'title': 'A cut', 'advice': 'approve',
             'spans': [{'block': 3, 'start': para['text'].index('As I said'), 'end': len(para['text'])}],
             'edits': [{'block': 3, 'before': para['text'], 'after': para['text'].replace(' As I said, it repeats.', '')}],
             'inserts': [], 'moves': [], 'what': 'Cuts it.', 'why': 'Said already.', 'stays': 'The rest.',
             'deciding': 'Approve cuts it.', 'approve_label': 'cut it'}
        h = {'id': 'ST-1.1', 'type': 'structure', 'title': 'A heading', 'advice': 'leave', 'spans': [], 'edits': [],
             'inserts': [{'before': 7, 'kind': 'h2', 'text': 'A new heading', 'seq': 0}], 'moves': [],
             'what': 'Adds a heading.', 'why': 'Why.', 'stays': 'All.', 'deciding': 'Approve adds it.'}
        page = R.page(review([s, h]), MD, self.bl)
        self.assertIn('<mark class="hl t-caveat" data-s="CV-1.1">As I said, it repeats.</mark>', page)
        self.assertIn('<del>', page)
        self.assertIn('id="c-CV-1.1"', page)
        self.assertIn('Approve: cut it', page)
        self.assertIn('Approve: make this change anyway', page)   # a leave card says what approving it does
        self.assertIn('class="card t-structure leave"', page)
        self.assertIn('A new heading', page)
        self.assertIn('review-form-controls-v1', page)
        self.assertIn((ROOT / 'project-sources' / 'review-form-controls.css').read_text(encoding='utf-8'), page)
        self.assertIn('<a href="https://example.com/x"', page)
        self.assertIn('[video]', page)
        self.assertNotIn('Double click to interact', page)
        data = json.loads(re.search(r'<script id="review-data" type="application/json">(.*?)</script>', page, re.S).group(1))
        self.assertEqual([x['id'] for x in data['suggestions']], ['CV-1.1', 'ST-1.1'])
        self.assertNotIn('https://fonts', page)
        self.assertIn('claude:viewport-fit-sides', page)
        self.assertIn('prefers-color-scheme: dark', page)

    def test_the_hypnosis_review_builds_and_checks(self):
        """The 2026-10-25 page: every suggestion's before-text is the guide's, so the page can't show another version."""
        rj = ROOT / 'articles/inner-signal/humanize/fix-20261025/review/REVIEW.json'
        rv = json.loads(rj.read_text(encoding='utf-8'))
        md = (ROOT / rv['article']['file']).read_text(encoding='utf-8')
        bl = R.blocks(md)
        import hashlib
        if hashlib.sha256(md.encode('utf-8')).hexdigest() != rv['article']['sha256']:
            self.skipTest('the guide changed after this review was built')
        self.assertEqual(R.check(rv, bl), [])
        ids = [s['id'] for s in rv['suggestions']]
        self.assertEqual(len(ids), len(set(ids)))
        decided = [s for s in rv['suggestions'] if s.get('decided')]
        self.assertEqual([s['id'] for s in decided], ['RR-1.1'])   # his own fix of 14:40


class ReaderBriefTests(unittest.TestCase):
    def test_the_brief_says_a_referent_right_before_is_clear(self):
        """E264: the reader flagged "do that" right after "remove anything from laws of nature"; Joel, 14:40: ""do that" is
        clearly referring to "remove anything from the laws of nature" directly before it"."""
        self.assertIn('whose meaning is in the words right before it', clarity_read.BRIEF)
        self.assertIn('read the sentence before it', clarity_read.BRIEF)

    def test_the_brief_keeps_plain_versions_his_own_words(self):
        """E264: the plain version added two brackets; Joel: "it's actually harder to read now with these 2 parentheticals"."""
        self.assertIn('How to write PLAIN', clarity_read.BRIEF)
        self.assertIn('at most one per passage', clarity_read.BRIEF)
        ex = json.loads((ROOT / 'tools/humanization/clarity_examples.json').read_text(encoding='utf-8'))
        last = ex[-1] if isinstance(ex, list) else ex['examples'][-1]
        self.assertIn('redirecting the thought stream with your conscious, higher intention', json.dumps(last, ensure_ascii=False))


if __name__ == '__main__':
    unittest.main()
