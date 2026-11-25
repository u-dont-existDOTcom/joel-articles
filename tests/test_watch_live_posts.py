"""watch_live_posts.py: the daily look at the live posts for a registered passage that changed, and the issues it
opens. Joel, 2026-11-25 11:18 UTC: "some way to know when one thing changes that another thing is dependent on in same
article or diff article"; 16:14 UTC: "for the registry, yes you can add the github job".

Every test builds a small repository of its own in a temporary folder, with two posts and a registry, and gives the
watcher its own fetch and its own `gh`: nothing here touches the network or GitHub."""
import contextlib
import copy
import hashlib
import io
import json
import pathlib
import re
import sys
import tempfile
import unittest
from unittest import mock

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(REPO / 'scripts'))
import depends as D  # noqa: E402
import live_sections as LS  # noqa: E402
import section_links as SL  # noqa: E402
import watch_live_posts as W  # noqa: E402

BASE = 'https://example.substack.com'
SOURCE = ('<p>Welcome, lovey bunnies!</p>'
          '<h1>Understanding</h1><p>Here is the idea behind it.</p>'
          '<h2>Borrowed Adulthood</h2>'
          '<p>Maybe you copy one small thing you’ve seen them do, and try <strong>one piece</strong> yourself. '
          'That’s what I mean by borrowed adulthood.</p>'
          '<p>A second paragraph that nothing depends on.</p>'
          '<h2>Ask What They Need</h2><p>Ask what they need, every time you sit down with them.</p>'
          '<h1>Sources</h1>'
          '<h2>Books</h2><p>One book, and another book.</p>')
GUIDE = ('<h1>The Guide</h1>'
         '<p>Put on the adult hat for a while, then give it back.</p>'
         '<p>There is more on borrowed adulthood in my <a href="%s/i/111/borrowed-adulthood">Inner Child Guide</a>.</p>'
         '<h2>Breathe</h2><ul><li><p>Try breathing less.</p></li><li><p>Stop if you feel dizzy.</p></li></ul>' % BASE)
HOME_QUOTE = 'Maybe you copy one small thing you’ve seen them do, and try one piece yourself.'
USE_QUOTE = 'Put on the adult hat for a while, then give it back.'
POINTER = 'There is more on borrowed adulthood in my Inner Child Guide.'


def post(post_id, slug, title, body, updated='2026-11-25T12:00:00.000Z'):
    return {'id': post_id, 'title': title, 'subtitle': 'A subtitle', 'slug': slug,
            'canonical_url': '%s/p/%s' % (BASE, slug), 'post_date': '2026-03-03T13:32:42.671Z', 'updated_at': updated,
            'wordcount': len(body.split()), 'audience': 'everyone', 'body_html': body}


def registry():
    return {'about': 'test', 'his_words': [], 'texts': {'source': 'articles/source/LIVE-SECTIONS.json',
                                                         'guide': 'articles/guide/LIVE-SECTIONS.json'},
            'points': [
                {'id': 'H01', 'what': 'the hat exercise', 'kind': 'passage',
                 'home': {'article': 'source', 'section': 'Borrowed Adulthood', 'quote': HOME_QUOTE},
                 'uses': [{'article': 'guide', 'section': 'The Guide', 'quote': USE_QUOTE, 'relation': 'own words',
                           'state': 'in line', 'as_of': '2026-11-25', 'note': ''}], 'from': 'a test'},
                {'id': 'P02', 'what': 'the pointer to borrowed adulthood', 'kind': 'passage',
                 'home': {'article': 'source', 'section': 'Borrowed Adulthood',
                          'quote': 'That’s what I mean by borrowed adulthood.'},
                 'uses': [{'article': 'guide', 'section': 'The Guide', 'quote': POINTER, 'relation': 'pointer',
                           'state': 'in line', 'as_of': '2026-11-25', 'note': ''}], 'from': 'a test'},
                {'id': 'L01', 'what': 'the link to Borrowed Adulthood', 'kind': 'link',
                 'home': {'article': 'source', 'heading': 'Borrowed Adulthood', 'anchor': 'borrowed-adulthood'},
                 'uses': [{'article': 'guide', 'section': 'The Guide', 'href': BASE + '/i/111/borrowed-adulthood',
                           'words': 'Inner Child Guide', 'as_of': '2026-11-25',
                           'note': 'in the post (articles/guide/LIVE-SECTIONS.json)'}], 'from': 'a test'}]}


class Fixture(unittest.TestCase):
    """Two posts as they were saved (source, post 111, with a section-link catalog; guide, post 222) and as they are
    now on Substack (self.live, which a test edits)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = pathlib.Path(self._tmp.name)
        self.live = {111: post(111, 'source-guide', 'The Source Guide', SOURCE),
                     222: post(222, 'built-on-guide', 'The Built-On Guide', GUIDE)}
        for name, post_id in (('source', 111), ('guide', 222)):
            (self.root / 'articles' / name).mkdir(parents=True)
            self.write('articles/%s/LIVE-SECTIONS.json' % name,
                       LS.dumps(LS.build(self.live[post_id], fetched='2026-11-25', source='saved for a test')))
        self.write('articles/source/SECTION-LINKS.json',
                   json.dumps(SL.build(SOURCE, BASE, 111, 'a test'), ensure_ascii=False, indent=1) + '\n')
        self.write('articles/INDEX.json', json.dumps({'articles': [{'id': 'source', 'title': 'The Source Guide'},
                                                                     {'id': 'guide', 'title': 'The Built-On Guide'}]}))
        self.save(registry())
        self.asked = []
        guard = mock.patch('urllib.request.urlopen', side_effect=AssertionError('a test touched the network'))
        guard.start()
        self.addCleanup(guard.stop)

    def write(self, rel, text):
        (self.root / rel).write_text(text, encoding='utf-8')

    def save(self, reg):
        self.write(D.REGISTRY, json.dumps(reg, ensure_ascii=False))

    def edit(self, post_id, old, new, updated='2026-11-26T08:09:10.000Z'):
        body = self.live[post_id]['body_html']
        self.assertEqual(body.count(old), 1, old)
        self.live[post_id] = dict(self.live[post_id], body_html=body.replace(old, new), updated_at=updated)

    def fetch(self, post_id, saved_post):
        self.asked.append(post_id)
        answer = self.live[post_id]
        if isinstance(answer, Exception):
            raise answer
        return copy.deepcopy(answer)

    def watch(self, today='2026-11-26'):
        return W.watch(self.root, fetch=self.fetch, today=today)

    def files(self):
        return {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(self.root.rglob('*')) if p.is_file()}

    def run_main(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(LS, 'fetch_post', side_effect=lambda post_id, base, timeout=None: self.fetch(post_id, None)):
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = W.main(['--root', str(self.root)] + list(args))
        return code, out.getvalue(), err.getvalue()


class NothingChanged(Fixture):
    def test_exit_0_and_nothing_written(self):
        before = self.files()
        r = self.watch()
        self.assertEqual((r['exit'], r['affected'], r['already'], r['fetch_failures']), (0, [], [], []))
        self.assertEqual((r['points'], r['places'], r['watched']), (3, 5, 2))
        self.assertEqual(self.asked, [111, 222])
        self.assertIn('Nothing registered changed: every passage and heading of the registry that was looked for '
                      '(3 points, 5 places) still stands in the 2 live posts.', r['report'])
        self.assertEqual(r['report'].count('- No change: [the post]('), 2)
        self.assertNotIn('To re-read', r['report'])
        self.assertEqual([(a['article'], a['html_changed'], a['words_changed']) for a in r['articles']],
                         [('source', False, False), ('guide', False, False)])
        self.assertEqual(self.files(), before)                       # nothing written, under articles/ or anywhere
        json.dumps(r)                                                # the whole result goes to JSON

    def test_a_change_no_point_rests_on(self):
        self.edit(111, 'A second paragraph that nothing depends on.', 'A second paragraph, said another way now.')
        self.edit(111, '<h1>Sources</h1>', '<h2>A New Section</h2><p>New words.</p><p>More.</p><h1>Sources</h1>')
        self.edit(222, '<h2>Breathe</h2><ul><li><p>Try breathing less.</p></li><li><p>Stop if you feel dizzy.</p></li></ul>', '')
        r = self.watch()
        self.assertEqual((r['exit'], r['affected']), (0, []))
        source, guide = r['articles']
        self.assertTrue(source['html_changed'] and source['words_changed'])
        self.assertEqual([s['heading'] for s in source['sections']['changed']], ['Borrowed Adulthood'])
        self.assertEqual(source['sections']['changed'][0]['points'], ['H01', 'P02', 'L01'])
        self.assertEqual(source['sections']['changed'][0]['text']['changed'], 1)
        self.assertEqual([(s['heading'], s['paragraphs']) for s in source['sections']['added']], [('A New Section', 2)])
        self.assertEqual([s['heading'] for s in guide['sections']['removed']], ['Breathe'])
        self.assertIn('Nothing registered changed', r['report'])
        self.assertIn('- **Changed** since [the saved copy of 2026-11-25](%sarticles/source/LIVE-SECTIONS.json): '
                      '[the post](%s/p/source-guide). Substack last updated it 2026-11-26T08:09:10.000Z (the saved '
                      'copy has 2026-11-25T12:00:00.000Z).' % (D.GIT, BASE), r['report'])
        self.assertIn('  - “Borrowed Adulthood”: 1 paragraph changed. Registered here: H01, P02, L01.', r['report'])
        self.assertIn('    - was: “A second paragraph that nothing depends on.”\n'
                      '      now: “A second paragraph, said another way now.”', r['report'])
        self.assertIn('- New sections (1): “A New Section” (2 paragraphs).', r['report'])
        self.assertIn('- Sections that are gone (1):\n  - “Breathe” (1 paragraph).', r['report'])

    def test_only_the_html_changed(self):
        self.edit(222, '/i/111/borrowed-adulthood">Inner Child Guide</a>', '/i/111/borrowed-adulthood" rel="x">Inner Child Guide</a>')
        r = self.watch()
        self.assertEqual(r['exit'], 0)
        self.assertEqual((r['articles'][1]['html_changed'], r['articles'][1]['words_changed']), (True, False))
        self.assertIn('- No words changed in [the post](%s/p/built-on-guide) since' % BASE, r['report'])
        self.assertIn('its HTML did (links, pictures or formatting).', r['report'])

    def test_markup_and_quote_marks_alone_do_not_change_a_registered_passage(self):
        self.edit(111, 'you’ve seen them do, and try <strong>one piece</strong> yourself.',
                  'you\'ve seen them do, and try <em>one piece</em>&nbsp;yourself.')
        r = self.watch()
        self.assertEqual((r['exit'], r['affected']), (0, []))
        self.assertEqual([s['heading'] for s in r['articles'][0]['sections']['changed']], ['Borrowed Adulthood'])

    def test_a_title_or_subtitle_that_changed(self):
        self.live[111] = dict(self.live[111], subtitle='Updated: Nov 26, 2026', updated_at='2026-11-26T08:00:00.000Z')
        r = self.watch()
        self.assertEqual(r['exit'], 0)
        self.assertIn('- Its subtitle changed: “Updated: Nov 26, 2026”, was “A subtitle”.', r['report'])
        self.assertIn('- No change: [the post](%s/p/source-guide) is the same as in' % BASE, r['report'])
        self.assertIn('Substack last updated it 2026-11-26T08:00:00.000Z', r['report'])


class RegisteredPassageChanged(Fixture):
    def test_a_changed_home_names_every_place_that_depends_on_it(self):
        self.edit(111, 'and try <strong>one piece</strong> yourself.', 'and then do <strong>one part</strong> alone.')
        r = self.watch()
        self.assertEqual(r['exit'], 1)
        self.assertEqual([(f['id'], f['side'], f['place']['article'], f['tie']) for f in r['affected']],
                         [('H01', 'home', 'source', 'depend on it')])
        self.assertEqual(r['affected'][0]['partners'][0]['article'], 'guide')
        self.assertEqual(r['title'], 'Live post changed: 1 registered passage to re-read (2026-11-26)')
        report = r['report']
        self.assertIn('**1 registered passage changed in a live post.**', report)
        self.assertIn('### To re-read (1)', report)
        self.assertIn('**H01** the hat exercise', report)
        self.assertIn('- Changed: source, [Borrowed Adulthood](%s/i/111/borrowed-adulthood): “Maybe you copy one small '
                      'thing you’ve seen…”' % BASE, report)
        self.assertIn('  - no longer found in the live post (%s/p/source-guide)' % BASE, report)
        self.assertIn('- These depend on it, to re-read:\n  - guide, “The Guide”: “Put on the adult hat for a while,…” '
                      '(own words; in line; 2026-11-25)', report)
        self.assertIn('    - was: “…thing you’ve seen them do, and try one piece yourself. That’s what I mean by borrowed…”\n'
                      '      now: “…thing you’ve seen them do, and then do one part alone. That’s what I mean by borrowed…”',
                      report)
        self.assertLess(report.index('### To re-read'), report.index('## The posts'))

    def test_a_changed_use_names_its_home(self):
        self.edit(222, 'Put on the adult hat for a while', 'Wear the adult hat for a bit')
        r = self.watch()
        self.assertEqual(r['exit'], 1)
        self.assertEqual([(f['id'], f['side'], f['tie']) for f in r['affected']], [('H01', 'use', 'it depends on')])
        self.assertIn('- Changed: guide, “The Guide”: “Put on the adult hat for a while,…”', r['report'])
        self.assertIn('- It depends on this, to re-read:\n  - source, [Borrowed Adulthood](%s/i/111/borrowed-adulthood): '
                      '“Maybe you copy one small thing you’ve seen…”' % BASE, r['report'])

    def test_two_passages_in_two_posts(self):
        self.edit(111, 'That’s what I mean by borrowed adulthood.', 'That is the thing I call borrowed adulthood.')
        self.edit(222, 'Put on the adult hat for a while', 'Wear the adult hat for a bit')
        r = self.watch()
        self.assertEqual(r['exit'], 1)
        self.assertEqual(sorted((f['id'], f['side']) for f in r['affected']), [('H01', 'use'), ('P02', 'home')])
        self.assertEqual(r['title'], 'Live post changed: 2 registered passages to re-read (2026-11-26)')
        self.assertIn('**2 registered passages changed in a live post.**', r['report'])
        self.assertIn('  - guide, “The Guide”: “There is more on borrowed adulthood in my…” (pointer; in line; 2026-11-25)',
                      r['report'])

    def test_a_heading_renamed(self):
        self.edit(111, '<h2>Borrowed Adulthood</h2>', '<h2>Borrowing an Adult</h2>')
        r = self.watch()
        self.assertEqual(r['exit'], 1)
        self.assertEqual([(f['id'], f['kind'], f['side'], f['tie']) for f in r['affected']],
                         [('L01', 'link', 'home', 'link to it')])
        report = r['report']
        self.assertIn('**L01** the link to Borrowed Adulthood', report)
        self.assertIn('- Changed: source, “Borrowed Adulthood” (the section)', report)
        self.assertIn('"Borrowed Adulthood" is not a heading in the live post (%s/p/source-guide); no heading in the '
                      'live post (%s/p/source-guide) has the anchor "borrowed-adulthood"' % (BASE, BASE), report)
        self.assertIn('- These link to it, to re-read:\n  - guide, “The Guide”: [Inner Child Guide]'
                      '(%s/i/111/borrowed-adulthood) (in the post ([articles/guide/LIVE-SECTIONS.json]'
                      '(%sarticles/guide/LIVE-SECTIONS.json)); 2026-11-25)' % (BASE, D.GIT), report)
        self.assertIn('- Headings renamed (1):\n  - “Borrowed Adulthood” is now “Borrowing an Adult”. '
                      'Registered here: H01, P02, L01.', report)
        self.assertEqual(r['articles'][0]['sections']['added'] + r['articles'][0]['sections']['removed'], [])

    def test_a_heading_with_no_words_of_its_own_renamed(self):
        self.edit(111, '<h1>Sources</h1>', '<h1>Sources and Thanks</h1>')
        r = self.watch()
        self.assertEqual(r['exit'], 0)
        self.assertEqual([(s['was'], s['now'], s['text']) for s in r['articles'][0]['sections']['renamed']],
                         [('Sources', 'Sources and Thanks', None)])

    def test_what_was_already_missing_from_the_saved_copy_is_not_a_change_on_substack(self):
        reg = registry()
        reg['points'][0]['uses'][0]['quote'] = 'Words the guide never had.'
        self.save(reg)
        r = self.watch()
        self.assertEqual((r['exit'], r['affected']), (0, []))
        self.assertEqual([(f['id'], f['side']) for f in r['already']], [('H01', 'use')])
        self.assertIn('### Already missing from the saved copy (1)', r['report'])
        self.assertIn('No registered passage changed on Substack: the 2 live posts say what the saved copies say. '
                      '1 registered passage was already missing from a saved copy and is listed below.', r['report'])
        self.assertNotIn('Nothing registered changed', r['report'])
        self.assertIn('they are not a change on Substack', r['report'])
        self.edit(111, 'That’s what I mean by borrowed adulthood.', 'That is the thing I call borrowed adulthood.')
        r = self.watch()
        self.assertEqual((r['exit'], [f['id'] for f in r['affected']], [f['id'] for f in r['already']]),
                         (1, ['P02'], ['H01']))

    def test_the_same_change_reads_the_same_the_next_day(self):
        self.edit(111, 'and try <strong>one piece</strong> yourself.', 'and then do <strong>one part</strong> alone.')
        first, second = self.watch('2026-11-26'), self.watch('2026-11-27')
        self.assertEqual((first['report'], first['fingerprint']), (second['report'], second['fingerprint']))
        self.assertNotIn('2026-11-27', second['report'])
        self.edit(222, 'Put on the adult hat for a while', 'Wear the adult hat for a bit')
        self.assertNotEqual(self.watch('2026-11-27')['fingerprint'], first['fingerprint'])
        # another edit that no point rests on is not another list of changed passages
        self.live[222] = post(222, 'built-on-guide', 'The Built-On Guide', GUIDE)
        self.edit(222, 'Try breathing less.', 'Try breathing a little less.')
        self.assertEqual(self.watch('2026-11-28')['fingerprint'], first['fingerprint'])


class FetchFailed(Fixture):
    def test_exit_2_says_which_post_and_the_status(self):
        self.live[222] = LS.FetchError('HTTP 403 Forbidden', 403, BASE + '/api/v1/posts/by-id/222')
        before = self.files()
        r = self.watch()
        self.assertEqual(r['exit'], 2)
        self.assertEqual(r['fetch_failures'], [{'article': 'guide', 'post_id': 222, 'api': BASE + '/api/v1/posts/by-id/222',
                                                'status': 403, 'reason': 'HTTP 403 Forbidden',
                                                'points_not_checked': ['H01', 'P02']}])
        self.assertEqual([(a['article'], a['fetched']) for a in r['articles']], [('source', True), ('guide', False)])
        report = r['report']
        self.assertIn('**1 of the 2 live posts could not be fetched**, so the passages in it were not checked.', report)
        self.assertIn('- **guide** (post 222): HTTP 403 Forbidden. %s/api/v1/posts/by-id/222 Not checked: 2 points '
                      '(H01, P02).' % BASE, report)
        self.assertIn('No registered passage changed in the posts that could be fetched.', report)
        self.assertIn('- Could not be fetched: HTTP 403 Forbidden.', report)
        self.assertEqual(self.files(), before)

    def test_what_could_be_fetched_is_still_checked(self):
        self.live[222] = LS.FetchError('no answer (timed out)', None, BASE + '/api/v1/posts/by-id/222')
        self.edit(111, '<h2>Borrowed Adulthood</h2>', '<h2>Borrowing an Adult</h2>')
        r = self.watch()
        self.assertEqual(r['exit'], 2)                               # the job has to fail, and the change is still told
        self.assertEqual([f['id'] for f in r['affected']], ['L01'])
        self.assertIn('**1 registered passage changed in a live post.**', r['report'])
        self.assertIn('no answer (timed out)', r['report'])

    def test_an_answer_for_another_post_or_without_a_body(self):
        self.live[111] = dict(self.live[111], id=999)
        self.live[222] = {'id': 222, 'title': 'paywalled', 'body_html': None}
        r = self.watch()
        self.assertEqual(r['exit'], 2)
        self.assertEqual([(f['article'], f['status'], f['reason']) for f in r['fetch_failures']],
                         [('source', None, 'the answer is post 999, not post 111'),
                          ('guide', None, 'the answer has no body_html')])

    def test_a_text_that_is_no_saved_live_post(self):
        reg = registry()
        reg['texts']['guide'] = 'articles/guide/master.html'
        self.save(reg)
        self.write('articles/guide/master.html', GUIDE)
        r = self.watch()
        self.assertEqual((r['exit'], self.asked), (2, [111]))
        self.assertIn('no post id', r['fetch_failures'][0]['reason'])


class Sections(unittest.TestCase):
    def sec(self, *rows):
        return [{'id': 'S%03d' % i, 'level': level, 'heading': heading, 'paragraphs': list(paras)}
                for i, (level, heading, paras) in enumerate(rows)]

    def test_changed_added_removed_renamed_and_level(self):
        old = self.sec((0, LS.BEFORE, []), (1, 'A', ['a one', 'a two']), (2, 'B', ['b one b two b three b four']),
                       (2, 'C', ['c']), (1, 'D', []), (2, 'E', ['e']))
        new = self.sec((0, LS.BEFORE, ['Subscribe']), (1, 'A', ['a one', 'a 2', 'a three']),
                       (2, 'B renamed', ['b one b two b three b five']), (1, 'D now', []), (3, 'E', ['e']), (2, 'F', ['f']))
        d = W.diff_sections(old, new)
        self.assertEqual([(s['heading'], s['text']['changed'], s['text']['added'], s['text']['removed'])
                          for s in d['changed']], [(LS.BEFORE, 0, 1, 0), ('A', 1, 1, 0)])
        self.assertEqual([(s['was'], s['now'], bool(s['text'])) for s in d['renamed']],
                         [('B', 'B renamed', True), ('D', 'D now', False)])
        self.assertEqual([s['heading'] for s in d['removed']], ['C'])
        self.assertEqual([s['heading'] for s in d['added']], ['F'])
        self.assertEqual(d['level'], [{'heading': 'E', 'was': 2, 'now': 3}])
        self.assertEqual(W.diff_sections(old, old), {'changed': [], 'renamed': [], 'added': [], 'removed': [], 'level': []})

    def test_two_sections_with_one_heading_and_a_section_that_moved(self):
        old = self.sec((1, 'Forgiving Yourself', ['first']), (1, 'X', ['x']), (1, 'Forgiving Yourself', ['second']))
        new = self.sec((1, 'Forgiving Yourself', ['second']), (1, 'X', ['x']), (1, 'Forgiving Yourself', ['first']))
        self.assertEqual(W.diff_sections(old, new), {'changed': [], 'renamed': [], 'added': [], 'removed': [], 'level': []})
        old = self.sec((1, 'A', ['the same words here']), (1, 'B', ['b']), (1, 'C', ['c']))
        new = self.sec((1, 'B', ['b']), (1, 'C', ['c']), (1, 'A moved and renamed', ['the same words here']))
        d = W.diff_sections(old, new)
        self.assertEqual([(s['was'], s['now']) for s in d['renamed']], [('A', 'A moved and renamed')])
        self.assertEqual(d['added'] + d['removed'], [])

    def test_the_stretch_where_two_paragraphs_differ(self):
        long = ' '.join('w%d' % i for i in range(60))
        was, now = W._differs(long, long.replace('w30', 'CHANGED'))
        self.assertEqual(was, '…w24 w25 w26 w27 w28 w29 w30 w31 w32 w33 w34 w35 w36…')
        self.assertEqual(now, was.replace('w30', 'CHANGED'))
        text = W.paragraph_changes(['a', 'b', 'c', 'd', 'e'], ['a', 'B', 'C', 'D', 'E', 'f'])
        self.assertEqual((text['changed'], text['added'], text['removed'], len(text['examples']), text['more']),
                         (4, 1, 0, 3, 2))


class Command(Fixture):
    def test_the_report_on_the_screen_and_in_a_file(self):
        self.edit(111, 'and try <strong>one piece</strong> yourself.', 'and then do <strong>one part</strong> alone.')
        target = self.root / 'report.md'
        code, out, err = self.run_main('--report', str(target))
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith('## Live posts and the shared passages\n'))
        self.assertEqual(target.read_text(encoding='utf-8'), out)
        self.assertEqual(err, '')

    def test_json(self):
        target = self.root / 'report.md'
        code, out, _ = self.run_main('--json', '--report', str(target))
        result = json.loads(out)
        self.assertEqual((code, result['exit'], result['affected']), (0, 0, []))
        self.assertEqual(result['report'], target.read_text(encoding='utf-8'))
        for key in ('checked', 'title', 'fingerprint', 'fetch_failures', 'articles', 'points', 'places', 'watched'):
            self.assertIn(key, result)

    def test_exit_2_names_the_post_on_stderr(self):
        self.live[111] = LS.FetchError('HTTP 429 Too Many Requests', 429, BASE + '/api/v1/posts/by-id/111')
        code, out, err = self.run_main()
        self.assertEqual(code, 2)
        self.assertIn('not fetched: source (post 111): HTTP 429 Too Many Requests', err)
        self.assertIn('HTTP 429 Too Many Requests', out)

    def test_it_does_not_write_under_articles(self):
        before = self.files()
        code, out, err = self.run_main('--report', str(self.root / 'articles' / 'source' / 'WATCH.md'))
        self.assertEqual((code, out), (3, ''))
        self.assertIn('cannot go under articles/', err)
        self.assertEqual((self.files(), self.asked), (before, []))

    def test_a_failure_of_the_script_is_3_never_1_or_2(self):
        self.write(D.REGISTRY, '{not json')
        code, _, err = self.run_main()
        self.assertEqual(code, 3)
        self.assertIn('watch_live_posts.py failed', err)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as e:
            W.main(['--no-such-flag'])
        self.assertEqual(e.exception.code, 3)

    def test_issues_from_a_saved_result(self):
        self.edit(111, 'and try <strong>one piece</strong> yourself.', 'and then do <strong>one part</strong> alone.')
        code, out, _ = self.run_main('--json')
        saved = self.root / 'result.json'
        saved.write_text(out, encoding='utf-8')
        gh = Gh()
        with mock.patch.object(W, 'run_gh', gh), contextlib.redirect_stdout(io.StringIO()) as said:
            code = W.main(['--issues-from', str(saved), '--run-url', 'https://github.test/runs/7'])
        self.assertEqual((code, self.asked), (0, [111, 222]))        # the second step fetches nothing
        self.assertIn('opened an issue: Live post changed: 1 registered passage to re-read', said.getvalue())
        self.assertIn('[this run](https://github.test/runs/7)', gh.issues[1]['body'])


class Gh:
    """Stands in for the GitHub CLI: labels and issues in memory, and every call kept."""

    def __init__(self, labels=()):
        self.labels, self.issues, self.calls = list(labels), {}, []

    def __call__(self, args, text=None):
        self.calls.append(' '.join(args[:2]))
        verb, flags = args[:2], args[2:]

        def flag(name):
            return flags[flags.index(name) + 1]

        if verb == ['label', 'list']:
            return json.dumps([{'name': n} for n in self.labels if flag('--search') in n])
        if verb == ['label', 'create']:
            assert flags[0] not in self.labels, 'the label is there already'
            self.labels.append(flags[0])
            return ''
        if verb == ['issue', 'list']:
            assert flag('--state') == 'open'
            return json.dumps([{'number': n, 'title': i['title'], 'url': 'https://github.test/issues/%d' % n}
                               for n, i in self.issues.items() if i['open'] and flag('--label') in i['labels']])
        if verb == ['issue', 'create']:
            assert flag('--label') in self.labels and flag('--body-file') == '-' and len(text) < 65536
            n = len(self.issues) + 1
            self.issues[n] = {'title': flag('--title'), 'labels': [flag('--label')], 'body': text, 'comments': [],
                              'open': True}
            return 'https://github.test/issues/%d\n' % n
        issue = self.issues[int(flags[0])]
        if verb == ['issue', 'view']:
            return json.dumps({'body': issue['body'], 'comments': [{'body': c} for c in issue['comments']]})
        if verb == ['issue', 'comment']:
            assert flag('--body-file') == '-' and len(text) < 65536
            issue['comments'].append(text)
            return ''
        if verb == ['issue', 'edit']:
            assert flag('--body-file') == '-'
            issue['body'] = text
            return ''
        if verb == ['issue', 'close']:
            issue['open'] = False
            issue['comments'].append(flag('--comment'))
            return ''
        raise AssertionError('gh %s' % ' '.join(args))

    def open(self, label):
        return [n for n, i in self.issues.items() if i['open'] and label in i['labels']]


class Issues(Fixture):
    def day(self, gh, today):
        result = self.watch(today)
        return result, W.file_issues(json.loads(json.dumps(result)), gh=gh, run_url='https://github.test/runs/1')

    def test_nothing_changed_posts_nothing(self):
        gh = Gh()
        _, done = self.day(gh, '2026-11-26')
        self.assertEqual((done, gh.issues, gh.labels, gh.calls), (['nothing to post'], {}, [], ['label list']))

    def test_one_issue_then_a_comment_only_when_the_list_is_another_one(self):
        gh = Gh()
        self.edit(111, 'and try <strong>one piece</strong> yourself.', 'and then do <strong>one part</strong> alone.')
        result, done = self.day(gh, '2026-11-26')
        self.assertEqual(gh.labels, ['depends-watch'])
        self.assertEqual(list(gh.issues), [1])
        issue = gh.issues[1]
        self.assertEqual(issue['title'], 'Live post changed: 1 registered passage to re-read (2026-11-26)')
        self.assertEqual(issue['labels'], ['depends-watch'])
        self.assertIn(result['report'], issue['body'])
        self.assertIn('- These depend on it, to re-read:\n  - guide, “The Guide”', issue['body'])
        self.assertIn('<!-- depends-watch report %s -->' % result['fingerprint'], issue['body'])
        self.assertIn('[articles/DEPENDS.md](%sarticles/DEPENDS.md)' % D.GIT, issue['body'])
        self.assertIn('opened an issue', done[0])

        _, done = self.day(gh, '2026-11-27')                          # the same change, the next day
        self.assertEqual((list(gh.issues), issue['comments']), ([1], []))
        self.assertIn('nothing posted', done[0])

        self.edit(222, 'Put on the adult hat for a while', 'Wear the adult hat for a bit')
        result, done = self.day(gh, '2026-11-28')                     # one more passage changed
        self.assertEqual((list(gh.issues), len(issue['comments'])), ([1], 1))
        self.assertIn('**2026-11-28: 2 registered passages to re-read now.**', issue['comments'][0])
        self.assertIn(result['report'], issue['comments'][0])
        self.assertIn('<!-- depends-watch report %s -->' % result['fingerprint'], issue['comments'][0])
        _, done = self.day(gh, '2026-11-29')
        self.assertEqual(len(issue['comments']), 1)

        self.live[222] = post(222, 'built-on-guide', 'The Built-On Guide', GUIDE)
        self.day(gh, '2026-11-30')                                    # back to the first list: the last posted counts
        self.assertEqual((list(gh.issues), len(issue['comments'])), ([1], 2))

        issue['open'] = False                                         # he closed it; the change is still there
        self.day(gh, '2026-12-01')
        self.assertEqual((sorted(gh.issues), gh.open('depends-watch')), ([1, 2], [2]))

    def test_a_post_that_cannot_be_fetched_has_one_issue_until_it_can(self):
        gh = Gh()
        self.live[222] = LS.FetchError('HTTP 403 Forbidden', 403, BASE + '/api/v1/posts/by-id/222')
        _, done = self.day(gh, '2026-11-26')
        self.assertEqual((gh.labels, list(gh.issues)), (['depends-watch-fetch'], [1]))
        issue = gh.issues[1]
        self.assertEqual(issue['title'], 'Live post could not be fetched since 2026-11-26')
        self.assertIn('- **guide** (post 222): HTTP 403 Forbidden, since 2026-11-26.', issue['body'])
        self.assertIn('Last tried: 2026-11-26.', issue['body'])

        self.day(gh, '2026-11-27')
        self.day(gh, '2026-11-28')
        self.assertEqual((list(gh.issues), issue['comments']), ([1], []))                 # no issue a day, no comment a day
        self.assertIn('- **guide** (post 222): HTTP 403 Forbidden, since 2026-11-26.', issue['body'])
        self.assertIn('Last tried: 2026-11-28.', issue['body'])

        self.live[111] = LS.FetchError('HTTP 429 Too Many Requests', 429, BASE + '/api/v1/posts/by-id/111')
        self.day(gh, '2026-11-29')                                    # another post fails too: said once
        self.assertEqual((list(gh.issues), len(issue['comments'])), ([1], 1))
        self.assertIn('- **source** (post 111): HTTP 429 Too Many Requests, since 2026-11-29.', issue['body'])
        self.assertIn('- **guide** (post 222): HTTP 403 Forbidden, since 2026-11-26.', issue['body'])
        self.day(gh, '2026-11-30')
        self.assertEqual(len(issue['comments']), 1)

        self.live = {111: post(111, 'source-guide', 'The Source Guide', SOURCE),
                     222: post(222, 'built-on-guide', 'The Built-On Guide', GUIDE)}
        _, done = self.day(gh, '2026-12-01')
        self.assertFalse(issue['open'])
        self.assertEqual(issue['comments'][-1], 'Fetching works again: on 2026-12-01 the job read all 2 live posts.')
        self.assertIn('closed issue #1', done[0])
        _, done = self.day(gh, '2026-12-02')
        self.assertEqual((done, list(gh.issues)), (['nothing to post'], [1]))

    def test_a_changed_passage_and_a_failed_fetch_on_one_day(self):
        gh = Gh()
        self.live[222] = LS.FetchError('HTTP 403 Forbidden', 403, BASE + '/api/v1/posts/by-id/222')
        self.edit(111, '<h2>Borrowed Adulthood</h2>', '<h2>Borrowing an Adult</h2>')
        result, _ = self.day(gh, '2026-11-26')
        self.assertEqual(result['exit'], 2)
        self.assertEqual((gh.open('depends-watch'), gh.open('depends-watch-fetch')), ([1], [2]))
        self.assertIn('**L01** the link to Borrowed Adulthood', gh.issues[1]['body'])
        self.live[222] = post(222, 'built-on-guide', 'The Built-On Guide', GUIDE)
        self.day(gh, '2026-11-27')                                    # fetching works again; the change stands
        self.assertEqual((gh.open('depends-watch'), gh.open('depends-watch-fetch')), ([1], []))
        self.assertEqual(gh.issues[1]['comments'], [])

    def test_a_report_longer_than_an_issue_holds(self):
        self.edit(111, 'and try <strong>one piece</strong> yourself.', 'and then do <strong>one part</strong> alone.')
        result = self.watch()
        result['report'] += 'x' * 50 + '\n' + ('a line of the report\n' * 4000)
        gh = Gh()
        W.file_issues(result, gh=gh)
        body = gh.issues[1]['body']
        self.assertLess(len(body), 65536)
        self.assertIn('The report is longer than an issue can hold.', body)
        self.assertIn('<!-- depends-watch report %s -->' % result['fingerprint'], body)


class DependsHook(Fixture):
    """What depends.py got for the watcher: texts and catalogs that are already in hand, a finding as Markdown, and
    the page's paragraph on the daily job."""

    def test_given_texts_are_checked_and_the_rest_is_read_from_its_file(self):
        reg = D.load(self.root)
        changed = LS.build(dict(self.live[111], body_html=SOURCE.replace('one piece', 'one part')))
        text = D.parse(json.dumps(changed), 'live.json')._replace(path='the live post')
        texts = D.Texts(reg, self.root, given={'source': text})
        self.assertEqual(texts.source('source'), ('the live post', 'given'))
        self.assertEqual(texts.source('guide'), ('articles/guide/LIVE-SECTIONS.json', '"texts" in the registry'))
        findings, unread, places = D.check(reg, texts)
        self.assertEqual([(f['id'], f['problem']) for f in findings], [('H01', 'no longer found in the live post')])
        self.assertEqual((unread, places), ([], 5))
        self.assertEqual(D.check(reg, D.Texts(reg, self.root))[0], [])            # as before without them

    def test_a_given_catalog_is_named_by_its_text_and_a_missing_text_by_its_reason(self):
        reg = D.load(self.root)
        body = SOURCE.replace('<h2>Borrowed Adulthood</h2>', '<h2>Borrowed Adulthood!</h2>')
        text = D.parse(json.dumps(LS.build(dict(self.live[111], body_html=body))), 'live.json')._replace(path='the live post')
        catalog = SL.build(body, BASE, 111)
        texts = D.Texts(reg, self.root, given={'source': text, 'guide': None}, catalogs={'source': catalog},
                        why={'guide': 'its live post could not be fetched (HTTP 403 Forbidden)'})
        findings, unread, _ = D.check(reg, texts)
        self.assertEqual([f['problem'] for f in findings if f['id'] == 'L01'], [
            '"Borrowed Adulthood" is not a heading in the live post; the live post has the anchor "borrowed-adulthood" '
            'under the heading "Borrowed Adulthood!"'])
        self.assertEqual(sorted(set(unread)), [
            ('H01', 'guide', 'its live post could not be fetched (HTTP 403 Forbidden)'),
            ('P02', 'guide', 'its live post could not be fetched (HTTP 403 Forbidden)')])
        self.assertIsNone(D.Texts(reg, self.root).catalog_name('source'))

    def test_the_page_says_a_job_looks_every_day_once_the_job_is_there(self):
        reg = D.load(self.root)
        self.assertNotIn('Checked every day', D.page(reg, root=self.root))
        (self.root / '.github' / 'workflows').mkdir(parents=True)
        self.write(D.WATCH, 'name: x\n')
        page = D.page(reg, root=self.root)
        self.assertIn('**Checked every day.** Once a day a job on GitHub ([the daily check](%s%s)) reads the 2 live '
                      'posts on Substack and looks for every passage on this page.' % (D.GIT, D.WATCH), page)
        self.assertIn('it opens [an issue on GitHub](https://github.com/u-dont-existDOTcom/joel-articles/issues?q=label'
                      '%3Adepends-watch) (a note in this repository\'s Issues list) that names the passage and every '
                      'other place that depends on it', page)
        self.assertLess(page.index('3 points:'), page.index('**Checked every day.**'))
        self.assertLess(page.index('**Checked every day.**'), page.index('## '))

    def test_the_real_page_says_it(self):
        if not ((REPO / D.WATCH).exists() and (REPO / D.PAGE).exists()):
            self.skipTest('no daily job or no page in this checkout')
        self.assertTrue(D.watch_note(D.load(REPO)) in (REPO / D.PAGE).read_text(encoding='utf-8'),
                        'articles/DEPENDS.md has no "Checked every day" paragraph: make the page again '
                        '(python3 tools/humanization/depends.py list --write)')


class Workflow(unittest.TestCase):
    """.github/workflows/depends-watch.yml: daily and by hand, the two permissions it needs, the repository's pin."""

    def setUp(self):
        self.path = REPO / D.WATCH
        if not self.path.exists():
            self.skipTest('no daily job in this checkout')
        self.text = self.path.read_text(encoding='utf-8')

    def block(self, key):
        lines = self.text.splitlines()
        start = lines.index(key + ':')
        rows = []
        for line in lines[start + 1:]:
            if line and not line.startswith((' ', '\t')):
                break
            rows.append(line)
        return [r.strip() for r in rows if r.strip()]

    def test_daily_and_by_hand_only(self):
        on = self.block('on')
        self.assertEqual([r for r in on if not r.startswith('- cron')], ['schedule:', 'workflow_dispatch:'])
        crons = [r for r in on if r.startswith('- cron')]
        self.assertEqual(len(crons), 1)
        minute, hour, day, month, weekday = re.fullmatch(r'- cron: "([^"]+)"', crons[0]).group(1).split()
        self.assertEqual((day, month, weekday), ('*', '*', '*'))      # every day
        self.assertTrue(minute.isdigit() and hour.isdigit() and 0 < int(minute) < 60 and int(minute) != 30)

    def test_least_permissions_and_the_pinned_checkout(self):
        self.assertEqual(self.block('permissions'), ['contents: read', 'issues: write'])
        uses = re.findall(r'^\s*(?:- )?uses:\s*(\S+)', self.text, flags=re.M)
        self.assertEqual(len(uses), 1)
        self.assertRegex(uses[0], r'^actions/checkout@[0-9a-f]{40}$')
        other = (REPO / '.github' / 'workflows' / 'content-integrity.yml').read_text(encoding='utf-8')
        self.assertIn(uses[0], other)                                 # the commit the other workflows pin
        self.assertIn('persist-credentials: false', self.text)
        self.assertNotIn('pull_request', self.text.replace('a pull request', ''))
        self.assertNotIn('pip install', self.text)                    # CI installs nothing

    def test_it_runs_the_watcher_then_the_issues_and_fails_on_a_post_not_fetched(self):
        self.assertIn('python scripts/watch_live_posts.py --root . --report "$RUNNER_TEMP/depends-watch.md" --json',
                      self.text)
        self.assertIn('python scripts/watch_live_posts.py --issues-from "$RUNNER_TEMP/depends-watch.json"', self.text)
        self.assertIn('GH_TOKEN: ${{ github.token }}', self.text)
        self.assertIn("if: steps.watch.outputs.code == '2'", self.text)
        self.assertLess(self.text.index('--issues-from'), self.text.index("steps.watch.outputs.code == '2'"))
        scripts, inside = [], None                                    # what each "run:" runs
        for line in self.text.splitlines():
            indent = len(line) - len(line.lstrip(' '))
            if inside is not None and (not line.strip() or indent > inside):
                scripts[-1] += line + '\n'
                continue
            inside = None
            m = re.match(r'\s*run:\s*(.*)$', line)
            if m:
                scripts.append(m.group(1) + '\n')
                inside = indent if m.group(1).strip() == '|' else None
        self.assertEqual(len(scripts), 3)
        self.assertNotIn('${{', ''.join(scripts))                     # a script reads its values from env, never from ${{ }}

    def test_the_repository_audit_finds_nothing_in_it(self):
        import audit_codex_github as audit
        findings = []
        audit._audit_workflows(REPO, [self.path], findings)
        self.assertEqual(findings, [])


if __name__ == '__main__':
    unittest.main()
