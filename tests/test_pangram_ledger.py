"""Tests for tools/humanization/pangram_ledger.py: the shared prediction ledger, its budget counter and the scorecards
(2026-10-20, Joel at 17:38 UTC: every humanization lane on one scorecard and improvement loop, with its own scorecard)."""
import contextlib
import io
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import pangram_ledger as L  # noqa: E402

NOTE = 'NOTE (a note, not a refusal): '


def run(argv):
    """L.main(ARGV) and what it printed: (exit code, stdout, where the notes go, stderr, where refusals go)."""
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = L.main(argv)
    return code, out.getvalue(), err.getvalue()


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
                narrowed=None, panel=None, paid_ok=None, trail=None):
        argv = ['predict', self.ledger, '--his', 'his own: a test text of Joel\'s', '--lineage', lineage, '--scope', scope, '--text', self.text(body), '--call', call,
                '--chance', '0.6' if call == 'Human' else '0.4'] + (['--key', key] if key else []) + \
            (['--narrowed', narrowed] if narrowed else []) + (['--panel', panel] if panel else []) + \
            (['--paid-ok', paid_ok] if paid_ok else []) + (['--trail', trail] if trail else [])
        for t in tells:
            argv += ['--tells', t]
        if diagnosis:
            argv += ['--diagnosis', diagnosis]
        code, self.out, self.err = run(argv)
        return code

    def result(self, body, verdict):
        return run(['result', self.ledger, '--sha', L.sha256(body), '--verdict', verdict,
                    '--link', 'https://www.pangram.com/history/x%d' % self.n])[0]

    def test_a_human_tell_says_what_a_model_would_write_instead(self):
        # Lesson neuro-2026-11-27g (Joel, 2026-11-27: "\"it's the same kind of thing\" isn't a human tell, ai can write
        # that also ... post-ashwa is a human tell bc ai doesn't tend to reduce the full name").
        rec = {'tells': ['a list of three'], 'scope': 'paragraph', 'call': 'Human', 'chance': 0.6, 'lineage': 'P1'}
        bad = L.refusals([], dict(rec, human_tells=['his "it\'s the same kind of thing"']))
        self.assertTrue(any('what a model would write' in r for r in bad))
        good = L.refusals([], dict(rec, human_tells=['his clipped "Post-ashwa" (a model writes "post-ashwagandha syndrome")',
                                                    'his writing: his card version of the herbs warning']))
        self.assertFalse(any('what a model would write' in r for r in good))

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

    def test_a_paragraph_lineage_has_ten_tries_and_more_only_on_a_trail(self):
        """Rules audit 2026-11-28, cards C05 and C07 (approved, merged): up to ten tries per paragraph, each past the first
        with a named reason; past ten a try goes on when it says why more checks help (his note on C05: "if you're hot on
        the trail and just need more budget then the budget should be flexible"), and is refused without it."""
        self.assertEqual([L.cap_for(s) for s in ('sentence', 'heading', 'paragraph', 'pair')], [10] * 4)
        for i in range(10):
            self.assertEqual(self.predict('v%d' % i, diagnosis='try %d fixes the list' % i), 0, self.err)
            self.result('v%d' % i, 'AI')
            run(['explain', self.ledger, '--sha', L.sha256('v%d' % i), '--cause', 'list', '--note', 'the list read AI'])
        self.assertEqual(self.predict('v10', diagnosis='an eleventh idea'), 2)
        self.assertIn('has used its 10 tries', self.err)
        self.assertIn('--trail', self.err)
        self.assertTrue(any('--trail' in b for b in L.blocks(L.read(self.ledger), 'P1', 'paragraph')))   # status says so
        self.assertEqual(self.predict('v10', diagnosis='an eleventh idea', trail='still on it'), 2)   # under 20 characters
        self.assertIn('the one given has 11', self.err)
        trail = 'the minimal pair: "it" against "this med", one word apart'
        self.assertEqual(self.predict('v10', trail=trail), 2)   # a try past the first still needs its diagnosis
        self.assertEqual(self.predict('v10', diagnosis='"this med" for "it"', trail=trail), 0, self.err)
        self.assertEqual(L.read(self.ledger)[-1]['trail'], trail)
        self.assertIn('try 11 of 10 (past them on its trail', self.out.splitlines()[-1])
        self.result('v10', 'AI')
        self.assertEqual(self.predict('v11', diagnosis='the next word'), 2)   # each try past ten says its trail
        self.assertEqual(self.predict('v11', diagnosis='the next word', trail=trail), 0, self.err)

    def compact(self, body, key, likelihood, windows):
        """Record a result in the web app reader's compact form, with its likelihood and windows."""
        res = self.dir / ('res-%s.json' % key)
        head = 'Human Written' if likelihood == 0 else 'AI Detected'
        res.write_text(json.dumps({key: [head, likelihood, 50, windows, '20:00:00', '/u-%s' % key, []]}), encoding='utf-8')
        return run(['results', self.ledger, str(res)])[0]

    def test_a_worse_reading_does_not_stop_a_lineage_before_ten(self):
        """Cards C05 and C07: the score comparison no longer decides the cap (his words, 2026-11-21: "pangram can be fickle
        so when you're not fully fixed yet you might go back and forth on pangram results"). This lineage's sixth check
        read worse than its fourth, so right_track says no; before the audit its seventh try was refused as a blind test
        (lesson bad-trips-2026-11-20g)."""
        for i, lk in enumerate((0.9, 0.8, 0.6, 0.5, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95)):
            body = 'ot%d' % i
            self.assertEqual(self.predict(body, lineage='OT', call='AI', key=body, diagnosis='try %d' % i), 0, self.err)
            self.assertEqual(self.compact(body, body, lk, 'Human, Low, 20; AI-Generated, Low, 30'), 0)
            if i == 5:
                self.assertFalse(L.right_track(L.lineage_view(L.state(L.read(self.ledger)), 'OT')))
        self.assertEqual(self.predict('ot10', lineage='OT', call='AI', diagnosis='an eleventh idea'), 2)

    def test_a_trail_does_not_lift_a_sections_cap(self):
        """The section rules stay (cards C05 and C07 keep --after-fix and narrowing): --trail is for a paragraph-sized
        lineage."""
        self.assertEqual(self.predict('s1', lineage='S', scope='section'), 0)
        self.result('s1', 'Human')
        self.assertEqual(self.predict('s2', lineage='S', scope='section', diagnosis='its heading changed'), 0)
        self.result('s2', 'Human')
        self.assertEqual(self.predict('s3', lineage='S', scope='section', diagnosis='its closer changed',
                                      trail='the trail: its closer, one word at a time'), 2)
        self.assertIn('--after-fix', self.err)

    def test_a_third_try_after_two_ai_reads_needs_no_tell_panel(self):
        """Rules audit 2026-11-28, card C20 (approved): after an AI read the next obvious fix goes, whatever the count (his
        words, E361: "I do what i know works, and if it doesn't fix it, I just try to find the next obvious thing that
        shoudl work"). --panel is optional now, and recorded when given; one naming no file gets a note."""
        for i in range(2):
            self.assertEqual(self.predict('w%d' % i, lineage='Q', call='AI', diagnosis='try %d' % i), 0)
            self.result('w%d' % i, 'AI' if i == 0 else 'Mixed')
        self.assertEqual(self.predict('w2', lineage='Q', call='AI', diagnosis='the next obvious fix'), 0, self.err)
        self.assertNotIn('panel', L.read(self.ledger)[-1])
        self.assertNotIn(NOTE, self.out)
        self.result('w2', 'AI')
        self.assertEqual(self.predict('w3', lineage='Q', call='AI', diagnosis='the agreed tells fixed', panel=self.panel()),
                         0, self.err)
        self.assertEqual(L.read(self.ledger)[-1]['panel'], self.panel())
        self.result('w3', 'AI')
        none = str(self.dir / 'NONE.md')
        self.assertEqual(self.predict('w4', lineage='Q', call='AI', diagnosis='another fix', panel=none), 0, self.err)
        self.assertIn(NOTE + '--panel %s: no such file' % none, self.out)
        self.assertEqual(L.read(self.ledger)[-1]['panel'], none)

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
        # a pangram.com article check only goes with his words (toc-2026-11-23d), and then keeps the cap of two
        ok = 'his words allowing it'
        self.assertEqual(self.predict('a1', lineage='A', scope='article', paid_ok=ok), 0)
        self.result('a1', 'Mixed')
        self.assertEqual(self.predict('a2', lineage='A', scope='article', diagnosis='fixed', paid_ok=ok), 0)
        self.result('a2', 'Mixed')
        self.assertEqual(self.predict('a3', lineage='A', scope='article', diagnosis='fixed again', paid_ok=ok), 2)

    def test_a_whole_article_never_goes_through_the_web_app(self):
        """Joel, 2026-11-03 22:02 UTC: "we don't do whole article checks with pangram GUI ... i have a free route for those.
        you can do a section check in the GUI tho, like 5-6 paragraphs or so". On 2026-11-23 the contents lane checked the
        whole Nirvana post in the web app six times, since only the API was refused (toc-2026-11-23d)."""
        self.assertEqual(self.predict('the whole post', lineage='W', scope='article'), 2)   # the default detector is the web app
        long_section = ' '.join(['word'] * 1300)
        self.assertEqual(self.predict(long_section, lineage='S', scope='section'), 2)
        self.assertEqual(self.predict(' '.join(['word'] * 600), lineage='S2', scope='section'), 0)   # 5 or 6 paragraphs
        free = ['predict', self.ledger, '--his', "his own: a test text of Joel's", '--lineage', 'W2', '--scope', 'article',
                '--text', self.text('the whole post, live'), '--call', 'Human', '--chance', '0.6', '--tells', 'x',
                '--decides', 'whether the heading keeps its body High',
                '--detector', 'Pangram 4.1, his extension (Brave) on the live Substack post (free)']
        self.assertEqual(L.main(free), 0)

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
        # an AI window can't be named away with --windows-ok (gate gut-2026-11-07a): refused
        self.assertEqual(L.main(base[:5] + ['B'] + base[6:] + ['--text', self.text(article + ' x'),
                                                                 '--windows-ok', 'his words; sent to him as a help request']), 2)
        # a later check that reads the same words Human (Medium or High) clears the window
        para = 'Start with low doses of prebiotics and probiotics, then build up.'
        self.assertEqual(self.predict(para, lineage='P', key='para'), 0)
        res.write_text(json.dumps({'para': {'sha256': L.sha256(para), 'words': 12, 'prediction_short': 'Human',
                                            'fraction_human': 1.0, 'version': '4.1', 'link': 'https://www.pangram.com/history/p1',
                                            'windows': [{'label': 'Human Written', 'confidence': 'High', 'words': 12,
                                                         'text': para}]}}), encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        self.assertEqual(L.open_windows(L.read(self.ledger), article), [])

    def test_a_section_that_read_ai_is_fixed_before_the_article_and_the_article_does_not_clear_it(self):
        """Gate gut-2026-11-07a (Joel, 2026-11-06 23:59 UTC: "make sure you're fixing any paras or sections that test ai
        before you ask for whole articel checks"): the gut lane checked the whole article twice with --windows-ok saying a
        cut's AI windows read Human in the whole article. An AI window a smaller check showed now blocks the article check
        whatever --windows-ok says; a whole-article check reading the same words Human doesn't clear it, a later section
        check does; a Low window can still be named with why it stays."""
        sec = 'Start by re-seeding with the yogurt. Then feed the new bacteria with plants, thirty kinds a week.'
        self.assertEqual(self.predict(sec, lineage='S', scope='section', call='AI', key='sec'), 0)
        res = self.dir / 'res.json'
        res.write_text(json.dumps({'sec': {'sha256': L.sha256(sec), 'words': 17, 'prediction_short': 'AI',
                                           'fraction_human': 0.4, 'version': '4.1', 'link': 'https://www.pangram.com/history/s1',
                                           'windows': [
                                               {'label': 'Human Written', 'confidence': 'Low', 'words': 6,
                                                'text': 'Start by re-seeding with the yogurt.'},
                                               {'label': 'AI-Generated', 'confidence': 'High', 'words': 11,
                                                'text': 'Then feed the new bacteria with plants, thirty kinds a week.'}]}}),
                       encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        article = 'Intro words here.\n' + sec + '\nMore words.'
        sub = "pangram 4.1, his Pangram extension on a temporary Substack draft (free)"
        base = ['predict', self.ledger, '--unchanged', 'the article as it stands', '--scope', 'article', '--call', 'Human',
                '--chance', '0.6', '--tells', 'the steps', '--detector', sub, '--decides', 'whether the article is done',
                '--windows-ok', 'the cut read them AI, the whole article reads them Human']
        self.assertEqual(L.main(base + ['--lineage', 'A', '--text', self.text(article)]), 2)
        # a whole-article check that reads the words Human doesn't fix the section that read them AI
        art = 'Intro words here.\n' + sec + '\nOther words.'
        self.assertEqual(L.main(['predict', self.ledger, '--unchanged', 'the article as it stands', '--scope', 'article',
                                 '--call', 'Human', '--chance', '0.6', '--detector', sub, '--decides', 'a test',
                                 '--lineage', 'B', '--key', 'art', '--text', self.text(art), '--windows-ok', 'a test',
                                 '--paid-ok', 'a test']), 2)
        recs = L.read(self.ledger)
        p = {'type': 'prediction', 'id': 'B#90', 'key': 'art', 'lineage': 'B', 'scope': 'article', 'call': 'Human',
             'sha256': L.sha256(art), 'at': '2026-11-07T00:00:00Z'}
        L.append(self.ledger, p)
        res.write_text(json.dumps({'art': {'sha256': L.sha256(art), 'words': 21, 'prediction_short': 'Human',
                                           'fraction_human': 1.0, 'version': '4.1', 'link': 'https://www.pangram.com/feed/a1',
                                           'windows': [{'label': 'Human Written', 'confidence': 'High', 'words': 21,
                                                        'text': art}]}}), encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        self.assertEqual([(l, lab) for l, lab, c, t in L.open_windows(L.read(self.ledger), article)
                          if lab.startswith('AI')], [('S', 'AI-Generated')])
        # a later section check that reads them Human clears the AI window; the Low one may then be named
        self.assertEqual(self.predict(sec, lineage='S2', scope='section', key='sec2', diagnosis='fixed'), 0)
        res.write_text(json.dumps({'sec2': {'sha256': L.sha256(sec), 'words': 17, 'prediction_short': 'Human',
                                            'fraction_human': 1.0, 'version': '4.1', 'link': 'https://www.pangram.com/history/s2',
                                            'windows': [{'label': 'Human Written', 'confidence': 'Low', 'words': 6,
                                                         'text': 'Start by re-seeding with the yogurt.'},
                                                        {'label': 'Human Written', 'confidence': 'High', 'words': 11,
                                                         'text': 'Then feed the new bacteria with plants, thirty kinds a week.'}]}}),
                       encoding='utf-8')
        self.assertEqual(L.main(['results', self.ledger, str(res)]), 0)
        seen = L.open_windows(L.read(self.ledger), article)
        self.assertTrue(seen and all(c == 'Low' and not lab.startswith('AI') for l, lab, c, t in seen), seen)
        self.assertEqual(L.main(base + ['--lineage', 'C', '--text', self.text(article + ' y')]), 0)

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
        self.assertEqual(self.predict('v3', diagnosis='d3'), 0)   # no tell panel needed since card C20

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
    over and over"), as the rules audit of 2026-11-28 left them: the making-sense read comes before every try of a text of
    mine, and its receipt's problems, a missing receipt and a retry that changes more than 40% of the words of the try
    before it are notes, not refusals (cards C01 and C02)."""

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
            r['needed'] = {'reader': 'a fresh reader given needed_read_brief.md', 'unneeded': [], 'kept': {}}
            r['his_fixes'] = {'reader': 'a fresh reader given his_fixes_brief.md', 'marked': [], 'kept': {}}
            r['fit'] = {'reader': 'a fresh reader given fit_read_brief.md', 'marked': [], 'kept': {}}
            r['questions'] = {q: 'PASS: said in the sentence itself' for q in self.S.QUESTIONS}
        rp = self.dir / ('r%d.json' % self.n)
        rp.write_text(json.dumps(r), encoding='utf-8')
        return str(t), str(rp)

    HUMANIZED = ('--humanized', 'payoffs moved to lead each sentence, two short sentences joined')

    def predict(self, text, receipt=None, extra=(), humanized=True):
        own = not any(x in ('--his', '--unchanged') for x in extra)
        argv = ['predict', self.ledger, '--lineage', 'G', '--scope', 'paragraph', '--text', text, '--call', 'AI',
                '--chance', '0.4', '--tells', 'a list'] + (['--receipt', receipt] if receipt else []) + list(extra) + \
            (list(self.HUMANIZED) if humanized and own else [])
        code, self.out, self.err = run(argv)
        return code

    def receipt_notes(self, text_path, receipt_path):
        """What the receipt's check finds, as predict prints it (worded by sense_receipt.py, whatever it finds)."""
        text = pathlib.Path(text_path).read_text(encoding='utf-8').rstrip('\n')
        rec = json.loads(pathlib.Path(receipt_path).read_text(encoding='utf-8'))
        return [NOTE + 'making-sense receipt: ' + p for p in self.S.check(text, rec)]

    def test_a_draft_not_written_to_read_human_is_not_checked(self):
        """Gate neuro-2026-11-07c: a science correction drafted for its content alone reads AI; it goes to Pangram
        only after a pass meant to make it read human, which --humanized names."""
        t, r = self.files('Time the seizure. Keep them on their side.')
        self.assertEqual(self.predict(t, r, humanized=False), 2)
        self.assertEqual(self.predict(t, r, ('--humanized', 'none: a science correction'), humanized=False), 2)
        self.assertEqual(self.predict(t, r, ('--humanized', 'short'), humanized=False), 2)
        self.assertEqual(L.read(self.ledger), [])
        self.assertEqual(self.predict(t, r), 0)
        self.assertEqual(L.read(self.ledger)[-1]['humanized'], self.HUMANIZED[1])

    def test_his_text_and_a_text_as_it_stands_need_no_humanizing_pass(self):
        t, _ = self.files('Time the seizure. Keep them on their side.')
        self.assertEqual(self.predict(t, extra=('--his', 'his own: the line he wrote into the guide, 2026-11-04'),
                                      humanized=False), 0)

    def read_ai(self, t):
        run(['result', self.ledger, '--sha', L.sha256(pathlib.Path(t).read_text(encoding='utf-8').rstrip('\n')), '--verdict', 'AI',
             '--link', 'https://www.pangram.com/history/x%d' % self.n])

    def test_the_text_is_hashed_as_pangram_reads_it_without_the_final_newline(self):
        t, r = self.files('Time the seizure. Keep them on their side.')
        self.assertEqual(self.predict(t, r), 0)
        self.assertEqual(L.read(self.ledger)[-1]['sha256'], L.sha256('Time the seizure. Keep them on their side.'))

    def test_a_text_of_mine_without_a_receipt_gets_a_note(self):
        """Rules audit 2026-11-28, card C02 (approved): the making-sense read comes before every try, and no text is
        refused for lacking its receipt (his note: "something like this already exists maybe merge")."""
        t, r = self.files('Time the seizure. Keep them on their side.')
        self.assertEqual(self.predict(t), 0, self.err)
        self.assertIn(NOTE + 'the making-sense read comes before every try', self.out)
        self.assertTrue(self.out.splitlines()[-1].startswith('G#1: try 1 of 10'))   # the prediction's line stays last
        self.assertNotIn('receipt', L.read(self.ledger)[-1])
        run(['void', self.ledger, '--sha', L.sha256('Time the seizure. Keep them on their side.'), '--reason', 'a test'])
        self.assertEqual(self.predict(t, r), 0, self.err)
        self.assertNotIn('the making-sense read comes before every try', self.out)
        self.assertEqual(L.read(self.ledger)[-1]['receipt'], r)

    def test_an_unfilled_receipt_is_a_note_not_a_refusal(self):
        """Card C02: a receipt given and failing its check: its problems are printed as notes, not refusals."""
        t, r = self.files('Time the seizure. Keep them on their side.', fill=False)
        notes = self.receipt_notes(t, r)
        self.assertEqual(self.predict(t, r), 0, self.err)
        for n in notes:
            self.assertIn(n, self.out)
        # a question answered FAIL is still a problem of the receipt's (sense_receipt.py), and a note here
        self.read_ai(t)
        t2, r2 = self.files('Keep them on their side. Time the seizure.')
        rec = json.loads(pathlib.Path(r2).read_text(encoding='utf-8'))
        rec['questions']['Q5'] = 'FAIL: nothing ties the second step to the first'
        pathlib.Path(r2).write_text(json.dumps(rec), encoding='utf-8')
        notes = self.receipt_notes(t2, r2)
        self.assertTrue(notes)
        self.assertEqual(self.predict(t2, r2, ('--diagnosis', 'the steps in the order a helper takes them')), 0, self.err)
        for n in notes:
            self.assertIn(n, self.out)

    def test_a_point_that_lost_its_reason_is_a_note(self):
        t, r = self.files('Time the seizure. Keep them on their side.')
        rec = json.loads(pathlib.Path(r).read_text())
        rec['checked'] = [{'point': '7-OH-CBD is more active', 'found': 'about as active as CBD in mice',
                           'still_needed': 'no: nothing is missed through the skin', 'fate': 'changed'}]
        pathlib.Path(r).write_text(json.dumps(rec))
        notes = self.receipt_notes(t, r)
        self.assertEqual(self.predict(t, r), 0, self.err)
        for n in notes:
            self.assertIn(n, self.out)

    def test_a_receipt_for_another_text_is_a_note(self):
        t, r = self.files('Time the seizure. Keep them on their side.')
        t2, _ = self.files('Time it. Keep them on their side.')
        notes = self.receipt_notes(t2, r)
        self.assertTrue(notes)
        self.assertEqual(self.predict(t2, r), 0, self.err)
        for n in notes:
            self.assertIn(n, self.out)
        # a check by --sha takes its text from a receipt for that text, and only notes one for another text
        code, out, err = run(['predict', self.ledger, '--lineage', 'S', '--scope', 'paragraph', '--sha', L.sha256('other'),
                              '--call', 'AI', '--chance', '0.4', '--tells', 'a list', '--receipt', r] + list(self.HUMANIZED))
        self.assertEqual(code, 0, err)
        self.assertIn(NOTE + 'making-sense receipt: the receipt is for another text', out)

    def test_a_receipt_that_cannot_be_read_is_a_note(self):
        t, _ = self.files('Time the seizure. Keep them on their side.')
        self.assertEqual(self.predict(t, str(self.dir / 'NO-RECEIPT.json')), 0, self.err)
        self.assertIn(NOTE + '--receipt %s can\'t be read' % (self.dir / 'NO-RECEIPT.json'), self.out)

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

    def test_a_big_retry_is_a_note_not_a_refusal(self):
        """Rules audit 2026-11-28, card C01 (approved): "you do whatever you need to do get it to read well" (2026-11-04).
        A retry that changes more than 40% of the words of the try before it without --big-change was refused (gate E361,
        after his movement fix: two words and a move); it gets a note, and --big-change is recorded when given."""
        t1, r1 = self.files('Letting them move around is fine. If they want to leave, someone goes with them.')
        self.assertEqual(self.predict(t1, r1), 0)
        self.read_ai(t1)
        t2, r2 = self.files('If they want to leave, have someone go with them. Letting them move around is fine.')
        self.assertLess(L.changed_share(pathlib.Path(t1).read_text(), pathlib.Path(t2).read_text()), 0.4)
        t3, r3 = self.files('Pacing is fine, so let them walk laps of the yard. Walk with them if they insist on going.')
        self.assertGreater(L.changed_share(pathlib.Path(t1).read_text(), pathlib.Path(t3).read_text()), 0.4)
        self.assertEqual(self.predict(t3, r3, ('--diagnosis', 'acts on things')), 0, self.err)
        self.assertIn(NOTE + 'this try changes', self.out)
        self.assertIn('of the words of the try before it in the lineage (G#1)', self.out)
        self.read_ai(t3)
        t4, r4 = self.files('Someone stays close if they head out the door, and moving about the room is fine.')
        self.assertGreater(L.changed_share(pathlib.Path(t3).read_text(), pathlib.Path(t4).read_text()), 0.4)
        why = 'every small fix of the windows was tried'
        self.assertEqual(self.predict(t4, r4, ('--diagnosis', 'said in the order a helper meets it', '--big-change', why)),
                         0, self.err)
        self.assertNotIn('of the words of the try before it', self.out)
        self.assertEqual(L.read(self.ledger)[-1]['big_change'], why)

    def test_a_near_miss_is_where_the_next_try_starts(self):
        """Rules audit 2026-11-28, card C01 (approved): after a try with a Human window, the next starts from it and fixes
        what is unclear in it, however many words that takes. Lesson bad-trips-2026-11-19b refused a try that changed more
        than 20% of its words, whatever --big-change said; it is a note now (his note on the card: "usually it makes sense
        to focus on the most AI sentences first")."""
        t1, r1 = self.files('Letting them move around is fine. If they want to leave, someone goes with them.')
        self.assertEqual(self.predict(t1, r1), 0)
        pid = L.read(self.ledger)[-1]['id']
        with open(self.ledger, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'type': 'result', 'prediction': pid, 'at': 'x', 'sha256': L.read(self.ledger)[-1]['sha256'],
                                'verdict': 'Mixed', 'link': 'https://www.pangram.com/history/near', 'right': False,
                                'likelihood': 0.79, 'windows': [{'label': 'Human', 'confidence': 'Low', 'words': 8},
                                                                {'label': 'AI-Generated', 'confidence': 'Medium', 'words': 9}]}) + '\n')
        t3, r3 = self.files('Pacing is fine, so let them walk laps of the yard. Walk with them if they insist on going.')
        self.assertEqual(self.predict(t3, r3, ('--diagnosis', 'acts on things', '--big-change',
                                               'every small fix of the windows was tried')), 0, self.err)
        self.assertIn(NOTE + 'the best try of this lineage, %s, read with a Human window: start from it' % pid, self.out)
        self.assertIn('however many words that takes', self.out)
        self.read_ai(t3)
        t2, r2 = self.files('Letting them move around is fine. If they want to leave, someone should go with them.')
        self.assertEqual(self.predict(t2, r2, ('--diagnosis', 'what someone does said as what they should do')), 0, self.err)
        self.assertNotIn('the best try of this lineage', self.out)   # a try from the near miss

    def test_the_near_miss_is_the_try_with_fewer_words_below_high_when_likelihoods_tie(self):
        """Turn 50 (2026-11-20): Pangram rounds a Human text's likelihood to 0, so niacin's side effects as the guide had them
        (a Medium window) tied my fix of them (Human High in every window), and the near-miss rule measured the next try
        from the older text."""
        def human(windows):
            last = L.read(self.ledger)[-1]
            with open(self.ledger, 'a', encoding='utf-8') as f:
                f.write(json.dumps({'type': 'result', 'prediction': last['id'], 'at': 'x', 'sha256': last['sha256'],
                                    'verdict': 'Human', 'link': 'https://www.pangram.com/history/h%d' % self.n,
                                    'right': True, 'likelihood': 0, 'windows': windows}) + '\n')
        t1, r1 = self.files('Higher or repeated doses can create real risk, especially with liver problems, alcohol, '
                            'medications, or sensitive physiology.')
        self.assertEqual(self.predict(t1, r1), 0)
        human([{'label': 'Human', 'confidence': 'High', 'words': 6}, {'label': 'Human', 'confidence': 'Medium', 'words': 11}])
        t2, r2 = self.files('Higher or repeated doses can create a real risk, especially with liver problems, alcohol, '
                            'medications, or sensitive physiology.')
        self.assertEqual(self.predict(t2, r2, ('--diagnosis', 'the risk said as one')), 0)
        human([{'label': 'Human', 'confidence': 'High', 'words': 17}])
        best = L.best_near_miss(L.lineage_view(L.state(L.read(self.ledger)), 'G'))
        self.assertEqual(best['text'], pathlib.Path(t2).read_text(encoding='utf-8').rstrip('\n'))

    def test_the_near_miss_ranks_likelihoods_as_the_web_app_shows_them(self):
        """Lesson bad-trips-2026-11-27i: through the API a Human text's likelihood comes unrounded, so a try with a Medium
        window (2.6e-31) ranked above one that read High in every window (7e-29); rounded to whole percent they tie, and
        the words below High decide."""
        def human(windows, lk):
            last = L.read(self.ledger)[-1]
            with open(self.ledger, 'a', encoding='utf-8') as f:
                f.write(json.dumps({'type': 'result', 'prediction': last['id'], 'at': 'x', 'sha256': last['sha256'],
                                    'verdict': 'Human', 'link': 'https://www.pangram.com/history/u%d' % self.n,
                                    'right': True, 'likelihood': lk, 'windows': windows}) + '\n')
        t1, r1 = self.files('A whole leaf can easily end the trip and may keep you from tripping for days afterward.')
        self.assertEqual(self.predict(t1, r1), 0)
        human([{'label': 'Human Written', 'confidence': 'High', 'words': 17}], 7.08e-29)
        t2, r2 = self.files('Eating a whole leaf can easily end the trip and may keep you from tripping for days afterward.')
        self.assertEqual(self.predict(t2, r2, ('--diagnosis', 'how the leaf is taken')), 0)
        human([{'label': 'Human Written', 'confidence': 'High', 'words': 10},
               {'label': 'Human Written', 'confidence': 'Medium', 'words': 8}], 2.63e-31)
        best = L.best_near_miss(L.lineage_view(L.state(L.read(self.ledger)), 'G'))
        self.assertEqual(best['text'], pathlib.Path(t1).read_text(encoding='utf-8').rstrip('\n'))
        self.assertEqual(L.shown_likelihood(2.63e-31), 0.0)
        self.assertEqual(L.shown_likelihood(None), 1.0)

    def test_a_try_that_adds_an_overused_word_gets_a_note(self):
        """Lesson bad-trips-2026-11-20e: my try added "ordinary"; he took it out and the paragraph read Human High.
        Card C11 (2026-11-28): an overused word is read, not banned, so the try gets a note, not a refusal."""
        t1, r1 = self.files('Samsara offers no shortage of difficult experiences to process.')
        self.assertEqual(self.predict(t1, r1), 0)
        self.read_ai(t1)
        t2, r2 = self.files('Samsara, the cycle of ordinary existence, offers no shortage of difficult experiences to process.')
        self.assertEqual(self.predict(t2, r2, ('--diagnosis', 'the term explained')), 0)
        self.assertIn(NOTE + 'this try adds "ordinary", which AI overuses', self.out)
        self.read_ai(t2)
        t3, r3 = self.files('Samsara, the cycle of existence, offers no shortage of difficult experiences to process.')
        self.assertEqual(self.predict(t3, r3, ('--diagnosis', 'the term explained')), 0)
        self.assertNotIn('which AI overuses', self.out)

    def test_a_small_retry_goes_through(self):
        t1, r1 = self.files('Letting them move around is fine. If they want to leave, someone goes with them.')
        self.assertEqual(self.predict(t1, r1), 0)
        self.read_ai(t1)
        t2, r2 = self.files('If they want to leave, have someone go with them. Letting them move around is fine.')
        self.assertEqual(self.predict(t2, r2, ('--diagnosis', 'the leaving line made practical, moved')), 0)


class FirstFix(SenseGate):
    """Gate E368 (Joel, 2026-11-05 18:43 UTC, on the fuels stretch he fixed by joining sentences, putting back "converted
    into" and moving the payoffs up: "why did you not check the same issue i always fix?"), as the rules audit of
    2026-11-28 left it (card C14, approved): a text of mine that reworks a sentence which read below High gets a note with
    what his fixes did first; no --first-fix declaration is required, and one given is recorded."""

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
        run(['predict', self.ledger, '--unchanged', 'his post as published', '--lineage', 'OLD', '--scope', 'paragraph', '--text',
             self.files(text)[0], '--call', 'Human', '--chance', '0.6', '--human-tells', 'his voice', '--key', 'old'])
        self.assertEqual(run(['results', self.ledger, str(res)])[0], 0)

    REWORKS = NOTE + 'this text reworks sentences that read below High before'

    def test_a_rework_of_a_window_below_high_gets_a_note_not_a_refusal(self):
        self.window('AI-Generated', 'Medium', self.OLD)
        t, r = self.files(self.NEW)
        self.assertEqual(self.predict(t, r), 0, self.err)
        self.assertIn(self.REWORKS, self.out)
        self.assertIn('payoff lands and move it up', self.out)
        self.assertNotIn('first_fix', L.read(self.ledger)[-1])
        run(['void', self.ledger, '--sha', L.sha256(self.NEW), '--reason', 'a test: predicted again with --first-fix'])
        self.assertEqual(self.predict(t, r, ('--first-fix', 'payoff: moved up')), 0, self.err)   # join and plain unsaid
        self.assertNotIn(self.REWORKS, self.out)
        self.assertEqual(L.read(self.ledger)[-1]['first_fix'], 'payoff: moved up')

    def test_a_payoff_that_moved_nothing_is_recorded_not_refused(self):
        """Lesson bad-trips-2026-11-20c refused "payoff: none moved" that didn't say how each sentence already leads; with
        the declaration gone (card C14), whatever --first-fix says is recorded."""
        self.window('AI-Generated', 'Medium', self.OLD)
        t, r = self.files(self.NEW)
        said = ('payoff: none moved; join: the α-KG sentence joined to the one before; plain: "turned straight into" back '
                'to "converted into"')
        self.assertEqual(self.predict(t, r, ('--first-fix', said)), 0, self.err)
        self.assertEqual(L.read(self.ledger)[-1]['first_fix'], said)

    def test_human_at_medium_is_below_high_too(self):
        self.window('Human', 'Medium', self.OLD)
        t, r = self.files(self.NEW)
        self.assertEqual(self.predict(t, r), 0, self.err)
        self.assertIn(self.REWORKS, self.out)

    def test_a_window_read_human_high_or_text_left_alone_needs_nothing(self):
        self.window('Human', 'High', self.OLD)
        t, r = self.files(self.NEW)
        self.assertEqual(self.predict(t, r), 0)
        self.assertNotIn(self.REWORKS, self.out)

    def test_unchanged_sentences_and_his_own_fix_need_nothing(self):
        self.window('AI-Generated', 'Low', self.OLD)
        t, r = self.files(self.OLD + ' Glutamine also provides nitrogen to help build new cells.')
        self.assertEqual(self.predict(t, r), 0)
        self.assertNotIn(self.REWORKS, self.out)
        t2, _ = self.files(self.NEW)
        code, out, err = run(['predict', self.ledger, '--lineage', 'H', '--scope', 'paragraph', '--text', t2,
                              '--call', 'Human', '--chance', '0.7', '--human-tells', 'his joins',
                              '--unchanged', 'his F9-1 version as he sent it'])
        self.assertEqual(code, 0, err)
        self.assertNotIn(NOTE, out)



class Flags(unittest.TestCase):
    """Rules audit 2026-11-28: every flag stays accepted (other lanes' scripts pass them), and one that no longer gates
    anything says in its help that it is optional now."""

    def test_the_flags_that_gate_nothing_say_they_are_optional(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), self.assertRaises(SystemExit):
            L.main(['predict', '-h'])
        helps = {}
        for chunk in out.getvalue().split('\n  -')[1:]:
            helps[chunk.split()[0].strip('-,')] = ' '.join(chunk.split())
        for flag in ('receipt', 'big-change', 'first-fix', 'panel'):
            self.assertIn('optional now', helps[flag], flag)
        self.assertIn('trail', helps)


class LanesCoverEveryLedger(unittest.TestCase):
    """Gate neuro-2026-11-07g: every lane's ledger is listed in tools/humanization/pangram_lanes.json, so no lane's
    checks go uncounted. The neuro de-armoring lane had 153 rows on no scorecard for four days, because nothing
    listed the lanes but that file and nothing checked it."""

    def test_every_ledger_in_the_repository_is_a_lane(self):
        root = pathlib.Path(__file__).resolve().parents[1]
        lanes = json.loads((root / 'tools/humanization/pangram_lanes.json').read_text(encoding='utf-8'))
        listed = {l['ledger'] for l in lanes['lanes']}
        for led in sorted(root.glob('articles/*/humanize/pangram-ledger.jsonl')):
            rel = led.relative_to(root).as_posix()
            self.assertIn(rel, listed,
                          '%s is not a lane in tools/humanization/pangram_lanes.json, so its checks are on no '
                          'scorecard (gate neuro-2026-11-07g)' % rel)


if __name__ == '__main__':
    unittest.main()