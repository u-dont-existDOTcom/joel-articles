"""tools/humanization/revised_stretches.py: a card he revised with his own version has its stretch replaced, wherever his
version goes in (gate bad-trips-2026-11-09d; Joel, 2026-11-09 17:22 UTC: "i thought i already merged it and cut that
section in the last turn")."""
import contextlib
import io
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import revised_stretches as R  # noqa: E402
import suggestion_review as sr  # noqa: E402

PAGE = '''# Guide

## First Minutes

Stay with them and keep the room calm and quiet for a while.

## The Loop

A common loop is fear trying to solve fear, over and over again.

Name it and wait for the wave to pass before you decide anything.
'''


def review_for(page):
    bl = sr.blocks(page)
    i = [b['i'] for b in bl if b['text'].startswith('A common loop')][0]
    j = [b['i'] for b in bl if b['text'].startswith('Name it')][0]
    return {'suggestions': [{'id': 'TEACH-LOOP', 'advice': 'edit', 'spans': [{'block': i, 'start': 0, 'end': len(bl[i]['text'])},
                                                           {'block': j, 'start': 0, 'end': len(bl[j]['text'])}]}]}


class RevisedStretchesTest(unittest.TestCase):
    def setUp(self):
        self.review = review_for(PAGE)
        stretch = ('A common loop is fear trying to solve fear, over and over again.\n\n'
                   'Name it and wait for the wave to pass before you decide anything.')
        self.answers = {'items': [{'id': 'TEACH-LOOP', 'status': 'revise', 'before': stretch,
                                   'your_version': stretch,     # the page's prefill, left unchanged
                                   'comment': 'putting my version back: Sometimes people get stuck in a panic loop, and '
                                              'feelings just need to be felt.'}]}

    def test_kept_section_is_flagged(self):
        # his version went into the first minutes, the old section stayed: the round-27 miss
        article = PAGE.replace('Stay with them', 'Sometimes people get stuck in a panic loop. Stay with them')
        left = R.stale(self.answers, self.review, PAGE, article)
        self.assertEqual([c for c, _ in left], ['TEACH-LOOP', 'TEACH-LOOP'])

    def test_cut_section_passes(self):
        article = '# Guide\n\n## First Minutes\n\nSometimes people get stuck in a panic loop. Stay with them.\n'
        self.assertEqual(R.stale(self.answers, self.review, PAGE, article), [])

    def test_sentence_he_kept_is_not_flagged(self):
        self.answers['items'][0]['comment'] += ' Name it and wait for the wave to pass before you decide anything.'
        article = PAGE.replace('A common loop is fear trying to solve fear, over and over again.', '')
        self.assertEqual(R.stale(self.answers, self.review, PAGE, article), [])

    def test_insert_card_marks_a_place_only(self):
        # an approve card that inserts a paragraph spans the block before it; his version replaces the insert, not that block
        self.review['suggestions'][0]['advice'] = 'approve'
        self.review['suggestions'][0]['inserts'] = [{'before': 0, 'kind': 'p', 'text': 'new'}]
        self.assertEqual(R.stale(self.answers, self.review, PAGE, PAGE), [])

    def test_revised_edit_card_checks_its_before(self):
        self.review['suggestions'][0]['advice'] = 'approve'
        self.review['suggestions'][0]['edits'] = [{'block': 0, 'before': 'Stay with them and keep the room calm and quiet for a while.', 'after': 'x'}]
        self.assertEqual([c for c, _ in R.stale(self.answers, self.review, PAGE, PAGE)], ['TEACH-LOOP'])

    def test_approved_card_is_not_checked(self):
        self.answers['items'][0]['status'] = 'approved'
        self.assertEqual(R.stale(self.answers, self.review, PAGE, PAGE), [])

    def test_cli_exit_and_kept(self):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            (d / 'a.json').write_text(json.dumps(self.answers))
            (d / 'r.json').write_text(json.dumps(self.review))
            (d / 'p.md').write_text(PAGE)
            (d / 'g.md').write_text(PAGE)
            args = ['--answers', d / 'a.json', '--review', d / 'r.json', '--page', d / 'p.md', '--article', d / 'g.md']
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(R.main([str(x) for x in args]), 1)
                self.assertEqual(R.main([str(x) for x in args] + ['--kept', 'TEACH-LOOP', 'he said to keep it']), 0)


if __name__ == '__main__':
    unittest.main()
