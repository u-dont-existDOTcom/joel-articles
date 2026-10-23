"""Tests for tools/humanization/pangram_ledger.py: the shared prediction ledger, its budget counter and the scorecards
(2026-10-20, Joel at 17:38 UTC: every humanization lane on one scorecard and improvement loop, with its own scorecard)."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import pangram_ledger as L  # noqa: E402


class Ledger(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.d.name)
        self.ledger = str(self.dir / 'pangram-ledger.jsonl')
        self.n = 0

    def tearDown(self):
        self.d.cleanup()

    def text(self, body):
        self.n += 1
        p = self.dir / ('t%d.txt' % self.n)
        p.write_text(body, encoding='utf-8')
        return str(p)

    def predict(self, body, lineage='P1', scope='paragraph', call='Human', diagnosis=None, tells=('a list of three',), key=None):
        argv = ['predict', self.ledger, '--lineage', lineage, '--scope', scope, '--text', self.text(body), '--call', call,
                '--chance', '0.6' if call == 'Human' else '0.4'] + (['--key', key] if key else [])
        for t in tells:
            argv += ['--tells', t]
        if diagnosis:
            argv += ['--diagnosis', diagnosis]
        return L.main(argv)

    def result(self, body, verdict):
        return L.main(['result', self.ledger, '--sha', L.sha256(body), '--verdict', verdict,
                       '--link', 'https://www.pangram.com/history/x%d' % self.n])

    def test_a_prediction_needs_evidence(self):
        self.assertEqual(self.predict('one', tells=()), 2)
        self.assertEqual(L.read(self.ledger), [])

    def test_the_chance_is_of_a_human_result(self):
        """An AI call at 0.9 recorded the confidence in the call; the ledger's chance is of a 100% Human result (2026-10-22)."""
        argv = lambda ch: ['predict', self.ledger, '--lineage', 'C', '--scope', 'paragraph', '--text', self.text('c' + ch),
                           '--call', 'AI', '--chance', ch, '--tells', 'a tidy closer']
        self.assertEqual(L.main(argv('0.9')), 2)
        self.assertEqual(L.read(self.ledger), [])
        self.assertEqual(L.main(argv('0.1')), 0)

    def test_a_paragraph_lineage_stops_at_six_tries(self):
        for i in range(6):
            self.assertEqual(self.predict('v%d' % i, diagnosis='try %d fixes the list' % i), 0)
            self.result('v%d' % i, 'AI')
            L.main(['explain', self.ledger, '--sha', L.sha256('v%d' % i), '--cause', 'list', '--note', 'the list read AI'])
        self.assertEqual(self.predict('v6', diagnosis='a seventh idea'), 2)

    def test_a_section_gets_one_retest(self):
        self.assertEqual(self.predict('s1', lineage='S13', scope='section'), 0)
        self.result('s1', 'Mixed')
        self.assertEqual(self.predict('s2', lineage='S13', scope='section', diagnosis='the seam of P3 and P4 rewritten'), 0)
        self.result('s2', 'AI')
        self.assertEqual(self.predict('s3', lineage='S13', scope='section', diagnosis='another'), 2)

    def test_a_substack_article_check_goes_past_two_when_it_decides_something(self):
        """Joel, 2026-10-21 17:56 UTC, question 7 b: Substack checks of a whole article may go past two, each predicted
        first and run only when its result decides something. A pangram.com article check keeps the cap of two."""
        def sub(body, decides=None, diagnosis='the fixes since the last check'):
            argv = ['predict', self.ledger, '--lineage', 'W', '--scope', 'article', '--text', self.text(body), '--call', 'AI',
                    '--chance', '0.1', '--tells', 'as-published sections', '--diagnosis', diagnosis,
                    '--detector', "pangram 4.1, Pangram's check of the Substack draft (free)"]
            return L.main(argv + (['--decides', decides] if decides else []))
        for i in range(3):
            self.assertEqual(sub('w%d' % i, decides='whether the fixes hold'), 0)
            self.result('w%d' % i, 'Mixed')
        self.assertEqual(sub('w3'), 2)   # past two, and no --decides
        self.assertEqual(self.predict('a1', lineage='A', scope='article'), 0)
        self.result('a1', 'Mixed')
        self.assertEqual(self.predict('a2', lineage='A', scope='article', diagnosis='fixed'), 0)
        self.result('a2', 'Mixed')
        self.assertEqual(self.predict('a3', lineage='A', scope='article', diagnosis='fixed again'), 2)

    def test_a_retry_after_a_failure_needs_a_diagnosis(self):
        self.predict('v1')
        self.result('v1', 'AI')
        self.assertEqual(self.predict('v2'), 2)
        self.assertEqual(self.predict('v2', diagnosis='the closing quip read AI; v2 ends on the fact'), 0)

    def test_two_unexplained_misses_stop_the_lineage(self):
        self.predict('v1')
        self.result('v1', 'AI')
        self.predict('v2', diagnosis='d2')
        self.result('v2', 'AI')
        self.assertEqual(self.predict('v3', diagnosis='d3'), 2)
        L.main(['explain', self.ledger, '--sha', L.sha256('v2'), '--cause', 'context', '--note', 'the window spans P3'])
        self.assertEqual(self.predict('v3', diagnosis='d3'), 0)

    def test_the_same_text_is_not_paid_for_twice(self):
        self.predict('same')
        self.result('same', 'Human')
        self.assertEqual(self.predict('same', diagnosis='again'), 2)

    def test_a_submission_without_a_result_holds_its_slot(self):
        self.predict('v1')
        self.assertEqual(self.predict('v2', diagnosis='d'), 2)
        L.main(['void', self.ledger, '--sha', L.sha256('v1'), '--reason', 'never sent: the page was signed out'])
        self.assertEqual(self.predict('v2', diagnosis='d'), 0)

    def test_a_result_is_scored_against_its_prediction(self):
        self.predict('v1', call='AI')
        self.result('v1', 'Mixed')
        res = [r for r in L.read(self.ledger) if r['type'] == 'result'][0]
        self.assertTrue(res['right'])
        with self.assertRaises(SystemExit):
            L.main(['result', self.ledger, '--sha', L.sha256('nothing'), '--verdict', 'Human', '--link', 'x'])

    def test_a_typed_verdict_must_agree_with_its_headline(self):
        self.predict('m1', call='AI')
        with self.assertRaises(SystemExit):
            L.main(['result', self.ledger, '--sha', L.sha256('m1'), '--verdict', 'Human', '--link', 'x',
                    '--headline', 'Mostly Human Written', '--ai-fraction', '0.0138'])
        L.main(['result', self.ledger, '--sha', L.sha256('m1'), '--verdict', 'Mixed', '--link', 'x',
                '--headline', 'Mostly Human Written', '--ai-fraction', '0.0138'])
        self.assertTrue([r for r in L.read(self.ledger) if r['type'] == 'result'][0]['right'])
        # without a fraction, "AI Detected" can be Mixed: that verdict stands, and only Human is refused
        self.predict('m2', call='AI', lineage='P2')
        with self.assertRaises(SystemExit):
            L.main(['result', self.ledger, '--sha', L.sha256('m2'), '--verdict', 'Human', '--link', 'x',
                    '--headline', 'AI Detected'])
        L.main(['result', self.ledger, '--sha', L.sha256('m2'), '--verdict', 'Mixed', '--link', 'x',
                '--headline', 'AI Detected'])

    def test_results_from_the_page_reader(self):
        self.predict('k1 text', key='K1')
        res = self.dir / 'res.json'
        res.write_text(json.dumps({'K1': {'headline': 'Mostly Human Written', 'fraction_ai': 0.12,
                                          'link': 'https://www.pangram.com/history/abc'}}), encoding='utf-8')
        L.main(['results', self.ledger, str(res)])
        r = [x for x in L.read(self.ledger) if x['type'] == 'result'][0]
        self.assertEqual(r['verdict'], 'Mixed')
        self.assertFalse(r['right'])

    def test_one_rule_scores_every_lane(self):
        table = self.dir / 'PREDICTIONS.md'
        table.write_text('| date | text | prediction | result | hit |\n|---|---|---|---|---|\n'
                         '| d | P1 alone | Human, low | Mostly Human Written (0.15; 1245), 2 windows | hit |\n'
                         '| d | P2 alone | Human, low | Human Written (0.03; 300) | hit |\n'
                         '| d | P3 alone | AI | 100% AI | hit |\n'
                         '| d | P4 alone | Human | not scanned again: the same text | hit |\n', encoding='utf-8')
        rows = L.legacy_rows({'kind': 'table', 'path': str(table)}, 'lane')
        self.assertEqual([r['right'] for r in rows], [False, True, True])
        self.assertEqual(rows[0]['marked'], True)

    def test_build_writes_each_lane_and_the_universal_page(self):
        self.predict('v1', call='AI')
        self.result('v1', 'Human')
        lanes = self.dir / 'lanes.json'
        lanes.write_text(json.dumps({'lanes': [{'lane': 'test lane', 'ledger': self.ledger}]}), encoding='utf-8')
        out = self.dir / 'U.md'
        L.main(['build', '--lanes', str(lanes), '--universal', str(out)])
        page = (self.dir / 'SCORECARD.md').read_text(encoding='utf-8')
        self.assertIn('Misses since the ledger (1)', page)
        self.assertIn('**not explained yet**', page)
        self.assertIn('| test lane | 1 | 0 (0%)', out.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
