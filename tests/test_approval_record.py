"""Gate bad-trips-2026-11-07a: ask Joel only where the meaning might change or there's a downside, and learn from what he
approves, revises and rejects (Joel, 2026-11-07 12:08 UTC: "you're asking me to approve things that are clearly good / you
should be learning what you actually need to ask my opinion on, like if meaning might have changed or there's a downside to
consider ... make sure you're continuously learning from what i approve vs what i revise or reject")."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import approval_record as A  # noqa: E402
import suggestion_review as R  # noqa: E402


def answers(rid, when, items):
    return {'format': A.FORMAT, 'review_id': rid, 'exported_at': when, 'items': items}


def item(cid, typ, status, comment='', version=''):
    return {'id': cid, 'type': typ, 'title': cid + ' title', 'status': status, 'comment': comment, 'your_version': version}


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        d = self.root / 'articles' / 'demo' / 'review' / 'r1'
        d.mkdir(parents=True)
        first = [item('P%d' % i, 'plain', 'approved') for i in range(5)] + [
            item('S1', 'structure', 'pending'), item('C1', 'cut', 'approved'), item('C2', 'cut', 'revise', 'keep the joke',
                                                                                      'his own line')]
        later = [item('S1', 'structure', 'rejected', 'the order carries the point'), item('P0', 'plain', 'pending'),
                 item('C1', 'cut', 'approved', "didn't need to ask me for this")]
        (d / 'ANSWERS-R1-a.json').write_text(json.dumps(answers('demo-r1', '2026-11-07T10:00:00Z', first)), encoding='utf-8')
        (d / 'ANSWERS-R1-b.json').write_text(json.dumps(answers('demo-r1', '2026-11-07T11:00:00Z', later)), encoding='utf-8')
        (d / 'ANSWERS-other.json').write_text('{"format": "something else", "items": []}', encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_each_card_counts_once_with_its_latest_answer(self):
        rec = A.record(self.root)['demo']
        self.assertEqual((rec['plain']['approved'], rec['plain']['pending']), (5, 0))   # a later pending export loses
        self.assertEqual((rec['structure']['rejected'], rec['structure']['pending']), (1, 0))   # a later answer wins
        self.assertEqual((rec['cut']['approved'], rec['cut']['revise']), (1, 1))

    def test_what_he_wrote_is_kept(self):
        rec = A.record(self.root)['demo']
        self.assertEqual(rec['cut']['pushback'][0]['comment'], 'keep the joke')
        self.assertEqual(rec['cut']['pushback'][0]['your_version'], 'his own line')
        self.assertEqual(rec['cut']['notes'][0]['comment'], "didn't need to ask me for this")
        self.assertEqual(rec['structure']['pushback'][0]['status'], 'rejected')

    def test_answers_read_from_a_published_page_take_type_and_title_from_its_review(self):
        d = self.root / 'articles' / 'demo' / 'review' / 'r2'
        d.mkdir(parents=True)
        (d / 'REVIEW-R2.json').write_text(json.dumps({'review_id': 'demo-r2', 'suggestions': [
            {'id': 'Q1', 'type': 'safety', 'title': 'A warning said once'}]}), encoding='utf-8')
        saved = {'format': A.FORMAT + " (read from the published page's saved decisions)", 'review_id': 'demo-r2',
                 'items': [{'id': 'Q1', 'status': 'approved', 'history': [{'to': 'approved', 'at': '2026-11-07T12:04Z'}]}]}
        (d / 'ANSWERS-R2-db.json').write_text(json.dumps(saved), encoding='utf-8')
        got = A.latest(self.root)[('demo', 'demo-r2', 'Q1')]
        self.assertEqual((got['type'], got['title'], got['when']), ('safety', 'A warning said once', '2026-11-07T12:04Z'))

    def test_a_type_he_approves_every_time_is_marked(self):
        rec = A.record(self.root)['demo']
        self.assertTrue(A.always_approved(rec['plain']))
        self.assertFalse(A.always_approved(rec['cut']))
        self.assertIn('all 5 approved', A.type_line('plain', rec['plain']))
        self.assertEqual(len(A.summary(rec, {'plain', 'cut'})), 2)


class AskTests(unittest.TestCase):
    def card(self, **kw):
        s = {'id': 'X-1', 'type': 'plain', 'title': 'A rewording', 'advice': 'approve'}
        s.update(kw)
        return s

    def rv(self, cards, built='2026-11-07', **kw):
        r = {'built': built, 'article': {'file': 'x.md'}, 'suggestions': cards}
        r.update(kw)
        return r

    def test_a_card_says_why_it_goes_to_him(self):
        self.assertTrue(R.ask_problems(self.rv([self.card()])))
        self.assertTrue(R.ask_problems(self.rv([self.card(ask_because='downside: x')])))   # a reason, not a word
        self.assertTrue(R.ask_problems(self.rv([self.card(ask_because='it reads better now')])))
        for why in ('meaning: "may help" becomes "helps", a stronger claim',
                    'downside: a reader who skips to this section loses the warning',
                    'his own: his line in the round-6 export, Sorrow P4'):
            self.assertEqual(R.ask_problems(self.rv([self.card(ask_because=why)])), [], why)

    def test_questions_older_pages_and_fine_grained_pages_need_no_reason(self):
        self.assertEqual(R.ask_problems(self.rv([self.card(advice='ask'), self.card(advice='edit')])), [])
        self.assertEqual(R.ask_problems(self.rv([self.card()], built='2026-11-06')), [])
        self.assertEqual(R.ask_problems(self.rv([self.card()], built='now')), [])
        fine = 'Joel, 2026-11-08 09:00 UTC: "show me every change this time"'
        self.assertEqual(R.ask_problems(self.rv([self.card()], fine_grained=fine)), [])

    def test_the_problem_names_his_record(self):
        rec = {'plain': {'approved': 7, 'revise': 0, 'rejected': 0, 'pending': 0, 'pushback': [], 'notes': []}}
        p = R.ask_problems(self.rv([self.card()]), rec)
        self.assertEqual(len(p), 1)
        self.assertIn('7 approved, 0 revised, 0 rejected', p[0])
        self.assertIn('all 7 approved', p[0])

    def test_a_stretch_he_rewrites_says_what_a_fresh_reader_found(self):
        asked = {'id': 'T-1', 'type': 'teach', 'advice': 'edit', 'whose': 'he asked: Joel, 2026-11-07: "give me the top paragraphs"'}
        rv = lambda cards, built='2026-11-07': {'built': built, 'suggestions': cards}
        self.assertTrue(R.sense_problems(rv([dict(asked)])))
        self.assertTrue(R.sense_problems(rv([dict(asked, sense='fine')])))
        found = 'a fresh reader asked what "content" means here; my tries say "a post about it" instead'
        self.assertEqual(R.sense_problems(rv([dict(asked, sense=found)])), [])
        self.assertEqual(R.sense_problems(rv([dict(asked)], built='2026-11-06')), [])
        own = dict(asked, whose='his own: his paragraph in the 2026-10-03 post')
        self.assertEqual(R.sense_problems(rv([own])), [])

    def test_a_stretch_on_a_list_covers_every_item(self):
        # gate bad-trips-2026-11-07k: round 23's steps card covered the first of four numbered steps
        md = '### Steps\n\n1. **First:** sleep.\n\n2. **Then:** write it down.\n\n3. **Last:** small changes.\n\nAfter.\n'
        bl = R.blocks(md)
        self.assertEqual([b['kind'] for b in bl], ['h3', 'oli', 'oli', 'oli', 'p'])
        sp = lambda i: {'block': i, 'start': 0, 'end': len(bl[i]['text'])}
        rv = lambda cards, built='2026-11-07': {'built': built, 'suggestions': cards}
        card = {'id': 'T-2', 'type': 'teach', 'advice': 'edit', 'spans': [sp(1)]}
        p = R.list_problems(rv([card]), bl)
        self.assertEqual(len(p), 1)
        self.assertIn('covers 1 of the 3 items', p[0])
        self.assertEqual(R.list_problems(rv([dict(card, spans=[sp(1), sp(2), sp(3)])]), bl), [])
        self.assertEqual(R.list_problems(rv([dict(card, list_part='only the second step names a dose')]), bl), [])
        self.assertEqual(R.list_problems(rv([dict(card, advice='approve')]), bl), [])   # an edit card's job
        self.assertEqual(R.list_problems(rv([card], built='2026-11-06'), bl), [])
        self.assertEqual(R.list_problems(rv([dict(card, spans=[sp(4)])]), bl), [])   # not a list

    def test_the_card_shows_why_im_asking(self):
        md = '# A heading\n\nThis is the first paragraph. It says a thing.\n'
        bl = R.blocks(md)
        para = bl[1]
        s = {'id': 'CV-1.1', 'type': 'caveat', 'title': 'A claim', 'advice': 'approve',
             'spans': [{'block': 1, 'start': 0, 'end': len(para['text'])}],
             'edits': [{'block': 1, 'before': para['text'], 'after': 'This is the first paragraph. It says another thing.'}],
             'inserts': [], 'moves': [], 'what': 'Changes the claim.', 'why': 'The source says so.', 'stays': 'The rest.',
             'deciding': 'Approve changes it.', 'ask_because': 'meaning: the claim changes from a thing to another thing'}
        rv = {'format': R.FORMAT, 'review_id': 't', 'title': 'T', 'intro': ['Hi.'], 'article': {'file': 'x.md', 'sha256': 'f' * 64},
              'built': 'now', 'types': {'caveat': {'label': 'Caveats', 'about': 'a'}}, 'suggestions': [s]}
        self.assertEqual(R.check(rv, bl), [])
        page = R.page(rv, md, bl)
        self.assertIn('Why I&#x27;m asking', page)
        self.assertIn('Meaning: the claim changes', page)


if __name__ == '__main__':
    unittest.main()
