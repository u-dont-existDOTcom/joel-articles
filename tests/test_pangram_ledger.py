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

    def predict(self, body, lineage='P1', scope='paragraph', call='Human', diagnosis=None, tells=('a list of three',), key=None,
                narrowed=None, panel=None):
        argv = ['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', lineage, '--scope', scope, '--text', self.text(body), '--call', call,
                '--chance', '0.6' if call == 'Human' else '0.4'] + (['--key', key] if key else []) + \
            (['--narrowed', narrowed] if narrowed else []) + (['--panel', panel] if panel else [])
        for t in tells:
            argv += ['--tells', t]
        if diagnosis:
            argv += ['--diagnosis', diagnosis]
        return L.main(argv)

    def result(self, body, verdict):
        return L.main(['result', self.ledger, '--sha', L.sha256(body), '--verdict', verdict,
                       '--link', 'https://www.pangram.com/history/x%d' % self.n])

    def test_compact_results_keep_their_windows(self):
        """The web app reader's compact form gives the windows as one string; read character by character, every result
        was Mixed (2026-11-01, batch s1101). A correction run records the right verdict after the wrong one."""
        self.assertEqual(self.predict('all human', key='k1'), 0)
        res = self.dir / 'res.json'
        res.write_text(json.dumps({'k1': ['Human Written', 0, 2, 'Human, High, 2', '20:00:00', '/u1', []]}), encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        p = L.find(L.read(self.ledger), key='k1')
        self.assertEqual(p['result']['verdict'], 'Human')
        res.write_text(json.dumps({'k1': ['Mostly Human Written', 0.05, 2, 'Human, High, 1; AI-Generated, Low, 1', '20:00:00',
                                          '/u1', []]}), encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res), '--correct', 'test']), 0)
        p = L.find(L.read(self.ledger), key='k1')
        self.assertEqual(p['result']['verdict'], 'Mixed')
        self.assertIn('corrects', p['result']['note'])

    def test_a_prediction_needs_evidence(self):
        self.assertEqual(self.predict('one', tells=()), 2)
        self.assertEqual(L.read(self.ledger), [])

    def test_the_chance_is_of_a_human_result(self):
        """An AI call at 0.9 recorded the confidence in the call; the ledger's chance is of a 100% Human result (2026-10-22)."""
        argv = lambda ch: ['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', 'C', '--scope', 'paragraph', '--text', self.text('c' + ch),
                           '--call', 'AI', '--chance', ch, '--tells', 'a tidy closer']
        self.assertEqual(L.main(argv('0.9')), 2)
        self.assertEqual(L.read(self.ledger), [])
        self.assertEqual(L.main(argv('0.1')), 0)

    def panel(self):
        p = self.dir / 'PANEL.md'
        p.write_text('# Tell panel\n', encoding='utf-8')
        return str(p)

    def test_a_paragraph_lineage_stops_at_six_tries(self):
        for i in range(6):
            self.assertEqual(self.predict('v%d' % i, diagnosis='try %d fixes the list' % i,
                                          panel=self.panel() if i >= 2 else None), 0)
            self.result('v%d' % i, 'AI')
            L.main(['explain', self.ledger, '--sha', L.sha256('v%d' % i), '--cause', 'list', '--note', 'the list read AI'])
        self.assertEqual(self.predict('v6', diagnosis='a seventh idea'), 2)

    def test_a_paragraph_that_read_ai_twice_goes_to_the_tell_panel_first(self):
        """E346 (2026-11-04): the neuro de-armoring lane's two uridine paragraphs took four tries each before the tell panel
        ran; with it, one read Human at its fifth try, and the other at its sixth, in another family's rewrite."""
        for i in range(2):
            self.assertEqual(self.predict('w%d' % i, lineage='Q', call='AI', diagnosis='try %d' % i), 0)
            self.result('w%d' % i, 'AI' if i == 0 else 'Mixed')
        self.assertEqual(self.predict('w2', lineage='Q', call='AI', diagnosis='a third wording'), 2)
        self.assertEqual(self.predict('w2', lineage='Q', call='AI', diagnosis='a third wording',
                                      panel=str(self.dir / 'NONE.md')), 2)
        self.assertEqual(self.predict('w2', lineage='Q', call='AI', diagnosis='the agreed tells fixed', panel=self.panel()), 0)
        # one AI read needs no panel
        self.assertEqual(self.predict('x0', lineage='R', call='AI', diagnosis='first'), 0)
        self.result('x0', 'AI')
        self.assertEqual(self.predict('x1', lineage='R', call='AI', diagnosis='second'), 0)

    def test_a_section_gets_one_retest(self):
        self.assertEqual(self.predict('s1', lineage='S13', scope='section'), 0)
        self.result('s1', 'Mixed')
        # since 2026-11-04 (E343), a section that read AI or Mixed is narrowed to its paragraphs before it is tried again
        self.assertEqual(self.predict('s2', lineage='S13', scope='section', diagnosis='the seam of P3 and P4 rewritten'), 2)
        self.assertEqual(self.predict('s2', lineage='S13', scope='section', diagnosis='the seam of P3 and P4 rewritten',
                                      narrowed='P3 and P4 by themselves'), 0)
        self.result('s2', 'AI')
        self.assertEqual(self.predict('s3', lineage='S13', scope='section', diagnosis='another'), 2)

    def test_a_half_does_not_go_through_the_paid_api(self):
        """Joel, 2026-11-02 20:38 UTC: "that should be done the free way to not waste my pangram credits" (E218, E325)."""
        half = ' '.join(['word'] * 1500)
        argv = ['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', 'W2', '--scope', 'stretch', '--text', self.text(half), '--call', 'AI',
                '--chance', '0.4', '--tells', 'x', '--detector', "pangram 4.1, the API (Joel's key, run on his laptop; E218)"]
        self.assertEqual(L.main(argv), 2)
        sub = list(argv); sub[-1] = "pangram 4.1, Pangram's check of the Substack draft (free)"
        self.assertEqual(L.main(sub + ['--decides', 'what the whole reads now']), 0)

    def test_a_fixed_section_gets_one_more_check_after_each_fix(self):
        """Joel, 2026-11-02 19:11 UTC, his answer 28a: one more check of the whole section after each fix, each with my
        prediction written first. Past its two tries a section takes a check only with --after-fix, and never of a text it
        has already sent."""
        def fixed(body, after_fix=None):
            argv = ['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', 'S9', '--scope', 'section', '--text', self.text(body), '--call', 'Human',
                    '--chance', '0.6', '--tells', 'a closer', '--diagnosis', 'the closer cut']
            return L.main(argv + (['--after-fix', after_fix] if after_fix else []))
        self.assertEqual(self.predict('a1', lineage='S9', scope='section', call='AI'), 0)
        self.result('a1', 'Mixed')
        self.assertEqual(self.predict('a2', lineage='S9', scope='section', call='AI', diagnosis='the seam rewritten',
                                      narrowed='P2 and P3 by themselves'), 0)
        self.result('a2', 'Mixed')
        self.assertEqual(fixed('a3'), 2)
        self.assertEqual(fixed('a3', 'the closer of P2 cut'), 0)
        self.result('a3', 'Human')
        self.assertEqual(fixed('a3', 'the same text again'), 2)
        self.assertEqual(L.main(['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', 'P9', '--scope', 'paragraph', '--text', self.text('p'),
                                 '--call', 'Human', '--chance', '0.6', '--tells', 'x', '--after-fix', 'not a section']), 0)

    def test_a_substack_article_check_goes_past_two_when_it_decides_something(self):
        """Joel, 2026-10-21 17:56 UTC, question 7 b: Substack checks of a whole article may go past two, each predicted
        first and run only when its result decides something. A pangram.com article check keeps the cap of two."""
        def sub(body, decides=None, diagnosis='the fixes since the last check'):
            argv = ['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', 'W', '--scope', 'article', '--text', self.text(body), '--call', 'AI',
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

    def test_a_stretch_that_read_ai_is_narrowed_to_its_paragraphs_first(self):
        """Joel, 2026-11-04 10:01 UTC: "you could go for a whole section if you feel confident, but then you'd still need
        to narrow it down to para level if it doesn't work" (the neuro lane's round 2 tried its stretches twice, E343)."""
        self.assertEqual(self.predict('s1', lineage='S', scope='stretch', call='AI'), 0)
        self.result('s1', 'AI')
        self.assertEqual(self.predict('s2', lineage='S', scope='stretch', call='AI', diagnosis='re-said'), 2)
        self.assertEqual(L.main(['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', 'S', '--scope', 'stretch', '--text', self.text('s2'),
                                 '--call', 'AI', '--chance', '0.4', '--tells', 'a list', '--diagnosis', 're-said',
                                 '--narrowed', 'P016, P017 and P085 by themselves']), 0)
        # a paragraph's retry needs only its diagnosis, and a stretch that read Human may be tried again
        self.assertEqual(self.predict('h1', lineage='H', scope='stretch'), 0)
        self.result('h1', 'Human')
        self.assertEqual(self.predict('h2', lineage='H', scope='stretch', diagnosis='its heading changed'), 0)

    def test_an_article_check_waits_for_the_windows_a_section_check_showed(self):
        """Joel, 2026-11-04 14:41 UTC: "no the whole article doesn't decide, we need to first fix any windows we can see
        before we check the article" (the gut lane checked the article after its stacks section read AI alone, E354)."""
        sec = 'I don\'t think there\'s one stack for everyone. Start with low doses of prebiotics and probiotics, then build up.'
        self.assertEqual(self.predict(sec, lineage='S', scope='section', call='AI', key='sec'), 0)
        res = self.dir / 'res.json'
        res.write_text(json.dumps({'sec': {'sha256': L.sha256(sec), 'words': 19, 'prediction_short': 'AI',
                                           'fraction_human': 0.05, 'version': '4.1',
                                           'link': 'https://www.pangram.com/history/s1', 'windows': [
                                               {'label': 'Human Written', 'confidence': 'High', 'words': 7,
                                                'text': "I don't think there's one stack for everyone."},
                                               {'label': 'AI-Generated', 'confidence': 'Medium', 'words': 12,
                                                'text': ' Start with low doses of prebiotics and probiotics, then build up.'}]}}),
                       encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        article = 'Intro words here.\n' + sec.replace("'", '’') + '\nMore words.'
        sub = "pangram 4.1, Pangram's check of the Substack draft (free)"
        base = ['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', 'A', '--scope', 'article', '--call',
                'Human', '--chance', '0.6',
                '--tells', 'the stacks paragraph', '--detector', sub, '--decides', 'whether the article is done']
        # the AI window is still in the article (curly quotes and all): refused
        self.assertEqual(L.main(base + ['--text', self.text(article)]), 2)
        # an article check without its text can't be compared, so it is refused too
        with self.assertRaises(SystemExit):
            L.main(base + ['--sha', L.sha256(article)])
        # fixed: the window's words are gone, so it may go
        fixed = article.replace('Start with low doses of prebiotics and probiotics, then build up.',
                                'Go slow with prebiotics at first; they make most people gassy.')
        self.assertEqual(L.main(base + ['--text', self.text(fixed)]), 0)
        # or named, with why it stays
        self.assertEqual(L.main(base[:5] + ['B'] + base[6:] + ['--text', self.text(article + ' x'),
                                                                 '--windows-ok', 'his words; sent to him as a help request']), 0)
        # a later check that reads the same words Human (Medium or High) clears the window
        para = 'Start with low doses of prebiotics and probiotics, then build up.'
        self.assertEqual(self.predict(para, lineage='P', key='para'), 0)
        res.write_text(json.dumps({'para': {'sha256': L.sha256(para), 'words': 12, 'prediction_short': 'Human',
                                            'fraction_human': 1.0, 'version': '4.1', 'link': 'https://www.pangram.com/history/p1',
                                            'windows': [{'label': 'Human Written', 'confidence': 'High', 'words': 12,
                                                         'text': para}]}}), encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        self.assertEqual(L.open_windows(L.read(self.ledger), article), [])

    def test_web_app_results_keep_their_ai_windows_for_the_article_rule(self):
        """The web app reader's flagged windows were dropped (2026-11-04), so E354 couldn't see a web-app check's AI
        windows, and its links came out with a double slash."""
        sec = 'Start any kit at a low dose and build up as your gut gets used to it. Everything else here is fine.'
        self.assertEqual(self.predict(sec, lineage='S', scope='section', call='AI', key='w1'), 0)
        res = self.dir / 'res.json'
        res.write_text(json.dumps({'w1': ['AI Detected', 0.2, 20, 'AI-Generated, Low, 15; Human, High, 5', '16:10:41', '/abc',
                                          ['AI-Generated (15 words): Start any kit at a low dose and build up as your gut gets used to it.']]}),
                       encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        r = L.find(L.read(self.ledger), key='w1')['result']
        self.assertEqual(r['link'], 'https://www.pangram.com/history/abc')
        self.assertEqual(r['windows'][0]['text'], 'Start any kit at a low dose and build up as your gut gets used to it.')
        self.assertEqual(r['verdict'], 'Mixed')
        seen = L.open_windows(L.read(self.ledger), 'Intro.\n' + sec)
        self.assertEqual([(l, c) for l, _, c, _ in seen], [('S', 'Low')])

    def test_a_later_check_kept_without_window_text_is_named_and_its_text_clears_the_window(self):
        """Gate gut-2026-11-06c (the gut lane, 2026-11-06): E354 named three AI Low windows that later checks (#137, #139) had read
        Human, High, because the ledger kept only those results' labels; I rewrote words that already read High, and
        both rewrites read worse. The refusal now names the later checks kept without window text, and a correction
        line with their text clears the window."""
        sec = 'Start any kit at a low dose and build up as your gut gets used to it. Everything else here is fine.'
        self.assertEqual(self.predict(sec, lineage='S', scope='section', call='AI', key='w1'), 0)
        res = self.dir / 'res.json'
        res.write_text(json.dumps({'w1': ['AI Detected', 0.2, 20, 'AI-Generated, Low, 15; Human, High, 5', '16:10:41', '/abc',
                                          ['AI-Generated (15 words): Start any kit at a low dose and build up as your gut gets used to it.']]}),
                       encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        whole = 'Intro.\n' + sec + '\nMore.'
        self.assertEqual(self.predict(whole, lineage='W', scope='section', key='w2'), 0)
        res.write_text(json.dumps({'w2': ['Human Written', 0.0, 22, 'Human, High, 22', '16:20:00', '/def', []]}),
                       encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        recs = L.read(self.ledger)
        self.assertEqual(len(L.open_windows(recs, whole)), 1)
        later = L.textless_after(recs, {'S'})
        self.assertEqual(later, [L.find(recs, key='w2')['id']])
        r = dict(L.state(recs)[later[0]]['result'])
        r['windows'] = [{'label': 'Human', 'confidence': 'High', 'words': 22, 'text': whole}]
        r['corrected'] = 'the same result, with its window text from Pangram\'s history'
        L.append(self.ledger, r)
        recs = L.read(self.ledger)
        self.assertEqual(L.open_windows(recs, whole), [])
        self.assertEqual(L.textless_after(recs, {'S'}), [])

    def test_two_unexplained_misses_stop_the_lineage(self):
        self.predict('v1')
        self.result('v1', 'AI')
        self.predict('v2', diagnosis='d2')
        self.result('v2', 'AI')
        self.assertEqual(self.predict('v3', diagnosis='d3'), 2)
        L.main(['explain', self.ledger, '--sha', L.sha256('v2'), '--cause', 'context', '--note', 'the window spans P3'])
        self.assertEqual(self.predict('v3', diagnosis='d3', panel=self.panel()), 0)

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

    def test_a_human_headline_with_ai_windows_is_mixed(self):
        # Nibbāna's second recheck, 2026-10-23: "Human Written" at 0.27% AI, two AI windows
        self.assertEqual(L.verdict_of('Human Written', None, 0.0027), 'Mixed')
        self.assertEqual(L.verdict_of('Human Written', None, 4.2e-22), 'Human')
        self.assertEqual(L.verdict_of('Human Written', ['H,H,0,10', 'A,L,10,20']), 'Mixed')
        self.assertEqual(L.verdict_of('Human Written', ['H,H,0,10']), 'Human')
        # window records, as RESULTS files hold them: gut r03 butyrate try 3 (2026-11-04), one AI-Assisted window,
        # fraction_ai 5e-12 with the rest "assisted", had been recorded as Human
        self.assertEqual(L.verdict_of(None, [{'label': 'AI-Assisted', 'confidence': 'Medium'}], 5.2e-12), 'AI')
        self.assertEqual(L.verdict_of(None, [{'label': 'Human Written'}, {'label': 'AI-Generated'}], 0.6), 'Mixed')
        self.assertEqual(L.verdict_of(None, [{'label': 'Human Written'}], 1e-20), 'Human')
        self.predict('h1', call='AI')
        with self.assertRaises(SystemExit):
            L.main(['result', self.ledger, '--sha', L.sha256('h1'), '--verdict', 'Human', '--link', 'x',
                    '--headline', 'Human Written', '--ai-fraction', '0.0027'])
        L.main(['result', self.ledger, '--sha', L.sha256('h1'), '--verdict', 'Mixed', '--link', 'x',
                '--headline', 'Human Written', '--ai-fraction', '0.0027'])
        self.assertTrue([r for r in L.read(self.ledger) if r['type'] == 'result'][0]['right'])

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



class SenseGate(unittest.TestCase):
    """Gates E365 (enforcing E362) and E361 (Joel, 2026-11-05 15:14 UTC: "fix the way you work because i'm not telling you the same stuff
    over and over"): a text of mine reaches Pangram only with a making-sense receipt that passes, and a retry changes at
    most 40% of the words of the try before it unless --big-change says why."""

    def setUp(self):
        self.d = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.d.name)
        self.ledger = str(self.dir / 'pangram-ledger.jsonl')
        self.n = 0
        import sense_receipt
        self.S = sense_receipt

    def tearDown(self):
        self.d.cleanup()

    def files(self, body, fill=True):
        self.n += 1
        t = self.dir / ('t%d.txt' % self.n)
        t.write_text(body + '\n', encoding='utf-8')
        r = self.S.make(body, 'Active Seizure', 'someone with a person having a seizure from MDMA or a psychedelic '
                        'overdose, which is generalized')
        if fill:
            for x in r['sentences']:
                x['payoff'] = 'tells the helper what to do next'
                x['follows'] = 'continues the step before'
                if 'link' in x:
                    x['link'] = 'none: each step is the next one the helper expects'
            r['placement'] = 'after the first-aid paragraph, which it continues'
            r['opens']['why_reading'] = 'the helper learns what to do in the first minute of the seizure'
            r['same_point'] = 'none: read the Active Seizure section from its heading to the next for these steps'
            r['questions'] = {q: 'PASS: said in the sentence itself' for q in self.S.QUESTIONS}
        rp = self.dir / ('r%d.json' % self.n)
        rp.write_text(json.dumps(r), encoding='utf-8')
        return str(t), str(rp)

    def predict(self, text, receipt=None, extra=()):
        argv = ['predict', self.ledger, '--lineage', 'G', '--scope', 'paragraph', '--text', text, '--call', 'AI',
                '--chance', '0.4', '--tells', 'a list'] + (['--receipt', receipt] if receipt else []) + list(extra)
        return L.main(argv)

    def read_ai(self, t):
        L.main(['result', self.ledger, '--sha', L.sha256(pathlib.Path(t).read_text(encoding='utf-8').rstrip('\n')), '--verdict', 'AI',
                '--link', 'https://www.pangram.com/history/x%d' % self.n])

    def test_the_text_is_hashed_as_pangram_reads_it_without_the_final_newline(self):
        t, r = self.files('Time the seizure. Keep them on their side.')
        self.assertEqual(self.predict(t, r), 0)
        self.assertEqual(L.read(self.ledger)[-1]['sha256'], L.sha256('Time the seizure. Keep them on their side.'))

    def test_a_text_of_mine_needs_its_receipt(self):
        t, r = self.files('Time the seizure. Keep them on their side.')
        self.assertEqual(self.predict(t), 2)
        self.assertEqual(L.read(self.ledger), [])
        self.assertEqual(self.predict(t, r), 0)

    def test_an_unfilled_receipt_is_refused(self):
        t, r = self.files('Time the seizure. Keep them on their side.', fill=False)
        self.assertEqual(self.predict(t, r), 2)

    def test_a_point_that_lost_its_reason_is_cut(self):
        t, r = self.files('Time the seizure. Keep them on their side.')
        rec = json.loads(pathlib.Path(r).read_text())
        rec['checked'] = [{'point': '7-OH-CBD is more active', 'found': 'about as active as CBD in mice',
                           'still_needed': 'no: nothing is missed through the skin', 'fate': 'changed'}]
        pathlib.Path(r).write_text(json.dumps(rec))
        self.assertEqual(self.predict(t, r), 2)
        rec['checked'][0]['fate'] = 'cut'
        pathlib.Path(r).write_text(json.dumps(rec))
        self.assertEqual(self.predict(t, r), 0)

    def test_a_receipt_for_another_text_is_refused(self):
        t, r = self.files('Time the seizure. Keep them on their side.')
        t2, _ = self.files('Time it. Keep them on their side.')
        self.assertEqual(self.predict(t2, r), 2)

    def test_his_own_text_needs_no_receipt(self):
        t, _ = self.files('Anything that could let someone hurt themselves takes priority.')
        self.assertEqual(self.predict(t, extra=('--his', 'his own: the line he wrote into the guide, 2026-11-04')), 0)

    def test_his_version_of_a_models_text_is_not_his_own(self):
        """Gate E373, Joel 2026-11-06 17:30 UTC: "'my words' for an AI article, are not my words, unless those were human
        before we started humanizing ... otherwise it's AI words that i humanized"."""
        t, _ = self.files('If they are thirsty, offer water, and suggest they sip it rather than chug.')
        self.assertEqual(self.predict(t, extra=('--his', 'his round-8 version')), 2)
        self.assertEqual(self.predict(t, extra=('--unchanged', 'his round-8 version as he sent it on ROOM-YOURS')), 0)
        recs = [json.loads(x) for x in open(self.ledger, encoding='utf-8')]
        self.assertEqual(recs[-1]['unchanged'], 'his round-8 version as he sent it on ROOM-YOURS')

    def test_a_retry_takes_small_steps(self):
        """His movement fix: two words and a move. My tries rewrote nearly every word (gate E361)."""
        t1, r1 = self.files('Letting them move around is fine. If they want to leave, someone goes with them.')
        self.assertEqual(self.predict(t1, r1), 0)
        self.read_ai(t1)
        t2, r2 = self.files('If they want to leave, have someone go with them. Letting them move around is fine.')
        self.assertLess(L.changed_share(pathlib.Path(t1).read_text(), pathlib.Path(t2).read_text()), 0.4)
        t3, r3 = self.files('Pacing is fine, so let them walk laps of the yard. Walk with them if they insist on going.')
        self.assertGreater(L.changed_share(pathlib.Path(t1).read_text(), pathlib.Path(t3).read_text()), 0.4)
        self.assertEqual(self.predict(t3, r3, ('--diagnosis', 'acts on things')), 2)
        self.assertEqual(self.predict(t3, r3, ('--diagnosis', 'acts on things', '--big-change',
                                               'every small fix of the windows was tried')), 0)
        self.read_ai(t3)

    def test_a_small_retry_goes_through(self):
        t1, r1 = self.files('Letting them move around is fine. If they want to leave, someone goes with them.')
        self.assertEqual(self.predict(t1, r1), 0)
        self.read_ai(t1)
        t2, r2 = self.files('If they want to leave, have someone go with them. Letting them move around is fine.')
        self.assertEqual(self.predict(t2, r2, ('--diagnosis', 'the leaving line made practical, moved')), 0)


class FirstFix(SenseGate):
    """Gate E368 (Joel, 2026-11-05 18:43 UTC, on the fuels stretch he fixed by joining sentences, putting back "converted
    into" and moving the payoffs up: "why did you not check the same issue i always fix?"): a text of mine that reworks a
    sentence which read below High goes to Pangram only with --first-fix saying what his usual fix did there first."""

    OLD = ('Inside the mitochondria, it gets turned straight into alpha-ketoglutarate, or α-KG. The α-KG goes into the '
           'citric acid cycle, which is how the mitochondria make their energy.')
    NEW = ('Inside the mitochondria, it gets converted into alpha-ketoglutarate, or α-KG, which then goes into the citric '
           'acid cycle, which is how the mitochondria make their energy.')
    FIX = ('payoff: the energy point now lands in the same sentence as the conversion; join: the α-KG sentence joined to '
           'the one before; plain: "turned straight into" back to "converted into"')

    def window(self, label, conf, text):
        res = self.dir / 'res.json'
        res.write_text(json.dumps({'old': {'headline': 'Mostly Human Written', 'fraction_ai': 0.2, 'words': 40,
                                           'windows': [{'label': label, 'confidence': conf, 'words': 30, 'text': text}],
                                           'link': 'https://www.pangram.com/history/old'}}), encoding='utf-8')
        L.main(['predict', self.ledger, '--unchanged', 'his post as published', '--lineage', 'OLD', '--scope', 'paragraph', '--text',
                self.files(text)[0], '--call', 'Human', '--chance', '0.6', '--human-tells', 'his voice', '--key', 'old'])
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)

    def test_a_rework_of_a_window_below_high_says_what_his_fix_did_first(self):
        self.window('AI-Generated', 'Medium', self.OLD)
        t, r = self.files(self.NEW)
        self.assertEqual(self.predict(t, r), 2)
        self.assertEqual(self.predict(t, r, ('--first-fix', 'payoff: moved up')), 2)   # join and plain unsaid
        self.assertEqual(self.predict(t, r, ('--first-fix', self.FIX)), 0)
        self.assertEqual(L.read(self.ledger)[-1]['first_fix'], self.FIX)

    def test_human_at_medium_is_below_high_too(self):
        self.window('Human', 'Medium', self.OLD)
        t, r = self.files(self.NEW)
        self.assertEqual(self.predict(t, r), 2)

    def test_a_window_read_human_high_or_text_left_alone_needs_nothing(self):
        self.window('Human', 'High', self.OLD)
        t, r = self.files(self.NEW)
        self.assertEqual(self.predict(t, r), 0)

    def test_unchanged_sentences_and_his_own_fix_need_nothing(self):
        self.window('AI-Generated', 'Low', self.OLD)
        t, r = self.files(self.OLD + ' Glutamine also provides nitrogen to help build new cells.')
        self.assertEqual(self.predict(t, r), 0)
        t2, _ = self.files(self.NEW)
        self.assertEqual(L.main(['predict', self.ledger, '--lineage', 'H', '--scope', 'paragraph', '--text', t2,
                                 '--call', 'Human', '--chance', '0.7', '--human-tells', 'his joins',
                                 '--unchanged', 'his F9-1 version as he sent it']), 0)



if __name__ == '__main__':
    unittest.main()