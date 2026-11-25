"""depends.py: the registry of shared passages (articles/DEPENDS.json) and the check that names what to re-read when
one of them changes. Joel, 2026-11-25 11:18 UTC: "make sure we have a common reference point for the things that are
common, in our github version control system for the articles rigth, or some way to know when one thing changes that
another thing is dependent on in same article or diff article." Every test builds a small repository of its own in a
temporary folder; the last one reads the real registry for its shape only."""
import contextlib
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import depends as D  # noqa: E402

SOURCE_HTML = ('<h1>Understanding</h1><p>Welcome.</p>'
               '<h2>Borrowed <em>Adulthood</em></h2>'
               '<p>Maybe you copy one small thing you&rsquo;ve seen them do, and try <strong>one piece</strong> '
               'yourself.&nbsp;That&rsquo;s what I mean by &ldquo;borrowed adulthood&rdquo;.</p>'
               '<h2>Ask What They Need</h2><p>Ask what they need. Ask what they need.</p>'
               '<p>See my <a href="https://example.org/p/somatic">somatic guide</a>.</p>')
GUIDE_MD = ('# The Guide\n\n'
            'Put on the **adult hat** for a while, then give it back.\n\n'
            'The longer version is in my [Inner Child Guide](https://example.org/p/inner-child).\n\n'
            '## Breathe\n\n'
            '- Try breathing *less*.\n'
            '- Stop if you feel dizzy.\n')
HOME_QUOTE = "Maybe you copy one small thing you've seen them do, and try one piece yourself."
USE_QUOTE = 'Put on the adult hat for a while, then give it back.'


def registry():
    return {'about': 'test', 'his_words': [{'when': '2026-11-25 11:18 UTC', 'words': 'a common reference point'}],
            'texts': {},
            'points': [
                {'id': 'H01', 'what': 'the hat exercise', 'kind': 'passage',
                 'home': {'article': 'source', 'section': 'Borrowed Adulthood', 'quote': HOME_QUOTE},
                 'uses': [{'article': 'guide', 'section': 'The Guide', 'quote': USE_QUOTE, 'relation': 'own words',
                           'state': 'in line', 'as_of': '2026-11-25', 'note': ''}],
                 'from': 'a test'},
                {'id': 'L01', 'what': 'the link to Borrowed Adulthood', 'kind': 'link',
                 'home': {'article': 'source', 'heading': 'Borrowed Adulthood', 'anchor': 'borrowed-adulthood'},
                 'uses': [{'article': 'guide', 'section': 'The Guide',
                           'href': 'https://example.org/i/1/borrowed-adulthood', 'words': 'Inner Child Guide'}],
                 'from': 'a test'}]}


class Fixture(unittest.TestCase):
    """A repository with two articles: source (master.html) and guide (master.md), and a registry."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self._tmp.name)
        for name in ('source', 'guide'):
            (self.root / 'articles' / name).mkdir(parents=True)
        self.write('articles/source/master.html', SOURCE_HTML)
        self.write('articles/guide/master.md', GUIDE_MD)
        self.write('articles/INDEX.json', json.dumps({'articles': [
            {'id': 'source', 'title': 'The Source Guide', 'authority': {'master': {'path': 'articles/source/master.html'}}},
            {'id': 'guide', 'title': 'The Built-On Guide', 'authority': {'master': {'path': 'articles/guide/master.md'}}}]}))
        self.save(registry())

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        (self.root / rel).write_text(text, encoding='utf-8')

    def save(self, reg):
        self.write(D.REGISTRY, json.dumps(reg, ensure_ascii=False))

    def reg(self):
        return D.load(self.root)

    def run_main(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = D.main(['--root', str(self.root)] + list(args))
        return code, out.getvalue(), err.getvalue()


class PlainText(unittest.TestCase):
    def test_html_tags_entities_and_paragraphs(self):
        t = D.parse(SOURCE_HTML, 'master.html')
        self.assertIn("you've seen them do, and try one piece yourself. That's what I mean by \"borrowed adulthood\".", t.text)
        self.assertIn('Welcome. Borrowed Adulthood Maybe', t.text)          # a block tag is a space, an inline tag is not
        self.assertEqual(t.headings, ['Understanding', 'Borrowed Adulthood', 'Ask What They Need'])
        self.assertNotIn('<', t.text)
        self.assertNotIn('example.org', t.text)

    def test_markdown_emphasis_links_and_bullets(self):
        t = D.parse(GUIDE_MD, 'master.md')
        self.assertIn('Put on the adult hat for a while', t.text)
        self.assertIn('The longer version is in my Inner Child Guide. Breathe Try breathing less. Stop if', t.text)
        self.assertEqual(t.headings, ['The Guide', 'Breathe'])
        self.assertEqual(D.parse('a snake_case_name and 2 * 3 * 4 and \\*kept\\*', 'x.md').text,
                         'a snake_case_name and 2 * 3 * 4 and *kept*')

    def test_quotes_apostrophes_and_whitespace(self):
        self.assertEqual(D.plain('“It’s  fine,”\n\tshe said'), D.plain('"It\'s fine," she said'))
        self.assertEqual(D.plain('see my somatic guide .'), D.plain('see my somatic guide.'))
        self.assertNotEqual(D.plain('together'), D.plain('to get her'))
        t = D.parse(SOURCE_HTML, 'master.html')
        for q in ('That’s what I mean by “borrowed adulthood”.', "That's   what I mean\nby \"borrowed adulthood\".",
                  'See my somatic guide .', 'try **one piece** yourself', 'try <strong>one piece</strong> yourself'):
            self.assertEqual(D.count(q, t.text), 1, q)
        self.assertEqual(D.count('Ask what they need.', t.text), 2)
        self.assertEqual(D.count('ask what they need', t.text), 0)           # the words, as written

    def test_sections_json_and_txt(self):
        sections = json.dumps([{'id': 'S000', 'level': 0, 'heading': '(before the first heading)', 'text': 'Subscribe now'},
                               {'id': 'S001', 'level': 1, 'heading': 'Borrowed Adulthood',
                                'paragraphs': ['One piece yourself.', 'See my somatic guide .']},
                               {'id': 'S002', 'level': 2, 'heading': 'Breathe', 'text': 'Try less.\n\nStop if dizzy.'}])
        t = D.parse(sections, 'SECTIONS.json')
        self.assertEqual(t.headings, ['Borrowed Adulthood', 'Breathe'])
        self.assertEqual(D.count('One piece yourself. See my somatic guide.', t.text), 1)
        self.assertEqual(D.count('Try less. Stop if dizzy.', t.text), 1)
        with self.assertRaises(ValueError):
            D.parse('{"headings": []}', 'CATALOG.json')
        t = D.parse('A first paragraph.\n\nWho Gets Reborn?\n\nStream entry and so on.\n', 'WHOLE.txt')
        self.assertIn('Who Gets Reborn?', t.headings)
        self.assertEqual(D.count('Stream entry and so on.', t.text), 1)


class Check(Fixture):
    def test_everything_found(self):
        findings, unread, places = D.check(self.reg(), D.Texts(self.reg(), self.root))
        self.assertEqual((findings, unread, places), ([], [], 3))
        code, out, _ = self.run_main('check')
        self.assertEqual(code, 0)
        self.assertIn('2 points (1 passage, 1 link), 3 places read: 0 changed, 0 not read', out)

    def test_changed_home_names_its_dependents(self):
        self.write('articles/source/master.html', SOURCE_HTML.replace('one small thing', 'one little thing'))
        findings, _, _ = D.check(self.reg(), D.Texts(self.reg(), self.root))
        self.assertEqual([(f['id'], f['side']) for f in findings], [('H01', 'home')])
        self.assertEqual(findings[0]['partners'][0]['article'], 'guide')
        code, out, _ = self.run_main('check')
        self.assertEqual(code, 1)
        self.assertIn('CHANGED  H01  the hat exercise', out)
        self.assertIn('source, "Borrowed Adulthood": "Maybe you copy one small thing you\'ve seen…"', out)
        self.assertIn('these depend on it, to re-read:', out)
        self.assertIn('guide, "The Guide": "Put on the adult hat for a while,…" (own words; in line; 2026-11-25)', out)
        self.assertIn('1 changed', out)

    def test_changed_use_names_its_home(self):
        self.write('articles/guide/master.md', GUIDE_MD.replace('adult hat', 'grown-up hat'))
        code, out, _ = self.run_main('check')
        self.assertEqual(code, 1)
        self.assertIn('guide, "The Guide": "Put on the adult hat', out)
        self.assertIn('it depends on, to re-read:', out)
        self.assertIn('source, "Borrowed Adulthood": "Maybe you copy', out)

    def test_markup_changes_are_not_changes(self):
        self.write('articles/guide/master.md', GUIDE_MD.replace('**adult hat**', '_adult_   hat'))
        self.write('articles/source/master.html', SOURCE_HTML.replace('you&rsquo;ve seen', "<em>you've</em> seen"))
        self.assertEqual(self.run_main('check')[0], 0)

    def test_text_comes_from_the_flag_then_the_registry_then_the_master(self):
        reg = self.reg()
        self.assertEqual(D.text_source(reg, self.root, 'guide'), ('articles/guide/master.md', 'its registered master'))
        self.write('articles/guide/LIVE.json', json.dumps([{'heading': 'The Guide', 'paragraphs': ['Nothing of it.']}]))
        reg['texts'] = {'guide': 'articles/guide/LIVE.json'}
        self.save(reg)
        code, out, _ = self.run_main('check')
        self.assertEqual(code, 1)                                    # the live copy has not got the use's words
        self.assertIn('no longer found in articles/guide/LIVE.json', out)
        self.write('articles/guide/OTHER.txt', 'Put on the adult hat for a while, then give it back.')
        self.assertEqual(self.run_main('check', '--text', 'guide=articles/guide/OTHER.txt')[0], 0)

    def test_an_article_without_a_text_is_not_read_and_a_missing_file_fails(self):
        reg = self.reg()
        reg['points'][0]['uses'].append({'article': 'hearthwork', 'section': 'Hats', 'quote': 'a hat', 'relation': 'own words',
                                         'state': 'behind', 'as_of': '2026-11-25', 'note': ''})
        self.save(reg)
        code, out, _ = self.run_main('check')
        self.assertEqual(code, 0)
        self.assertIn('NOT READ  hearthwork', out)
        self.assertIn('0 changed, 1 not read', out)
        reg['texts'] = {'guide': 'articles/guide/GONE.html'}
        self.save(reg)
        code, out, _ = self.run_main('check')
        self.assertEqual(code, 1)
        self.assertIn('articles/guide/GONE.html', out)

    def test_article_filter(self):
        reg = self.reg()
        reg['points'].append({'id': 'S01', 'what': 'inside the source', 'kind': 'passage',
                              'home': {'article': 'source', 'section': 'Understanding', 'quote': 'Welcome.'},
                              'uses': [{'article': 'source', 'section': 'Ask What They Need', 'quote': 'See my somatic guide.',
                                        'relation': 'pointer', 'state': 'in line', 'as_of': '2026-11-25', 'note': ''}],
                              'from': 'a test'})
        self.save(reg)
        self.assertIn('0 points (0 passages, 0 links), 0 places read', self.run_main('check', '--article', 'nobody')[1])
        self.assertIn('3 points (2 passages, 1 link), 5 places read', self.run_main('check', '--article', 'source')[1])
        self.assertIn('2 points (1 passage, 1 link), 3 places read', self.run_main('check', '--article', 'guide')[1])


class Links(Fixture):
    def catalog(self, headings):
        self.write('articles/source/SECTION-LINKS.json', json.dumps({
            'post': {'base': 'https://example.org', 'id': '1'}, 'headings': headings, 'links': []}))

    def test_heading_renamed_in_the_text(self):
        self.write('articles/source/master.html', SOURCE_HTML.replace('Borrowed <em>Adulthood</em>', 'Borrow an Adult'))
        findings, _, _ = D.check(self.reg(), D.Texts(self.reg(), self.root))
        self.assertEqual([(f['id'], f['side']) for f in findings], [('L01', 'home')])
        code, out, _ = self.run_main('check')
        self.assertEqual(code, 1)
        self.assertIn('"Borrowed Adulthood" is not a heading in articles/source/master.html', out)
        self.assertIn('these link to it, to re-read:', out)
        self.assertIn('guide, "The Guide": "Inner Child Guide" https://example.org/i/1/borrowed-adulthood', out)

    def test_the_words_alone_are_not_a_heading(self):
        self.write('articles/source/master.html', SOURCE_HTML.replace('<h2>Borrowed <em>Adulthood</em></h2>',
                                                                      '<p>Borrowed Adulthood</p>'))
        self.assertEqual([f['id'] for f in D.check(self.reg(), D.Texts(self.reg(), self.root))[0]], ['L01'])

    def test_anchor_gone_from_the_catalog(self):
        self.catalog([{'id': 'S002', 'level': 2, 'text': 'Borrowed Adulthood', 'anchor': 'borrowed-adulthood'}])
        self.assertEqual(self.run_main('check')[0], 0)
        self.catalog([{'id': 'S002', 'level': 2, 'text': 'Borrow an Adult', 'anchor': 'borrow-an-adult'}])
        code, out, _ = self.run_main('check')
        self.assertEqual(code, 1)
        self.assertIn('no heading in articles/source/SECTION-LINKS.json has the anchor "borrowed-adulthood"', out)

    def test_a_link_that_ends_in_another_anchor(self):
        reg = self.reg()
        reg['points'][1]['uses'][0]['href'] = 'https://example.org/p/post?open=false#%C2%A7borrowed-adulthood'
        self.assertEqual(D.check(reg, D.Texts(reg, self.root))[0], [])
        reg['points'][1]['uses'][0]['href'] = 'https://example.org/i/1/borrow-an-adult'
        findings, _, _ = D.check(reg, D.Texts(reg, self.root))
        self.assertEqual([(f['id'], f['side']) for f in findings], [('L01', 'use')])


class Add(Fixture):
    def add(self, *more):
        return self.run_main('add', '--id', 'N01', '--what', 'ask what they need', *more)

    def test_refuses_a_quote_that_is_not_there(self):
        before = (self.root / D.REGISTRY).read_text(encoding='utf-8')
        code, _, err = self.add('--home', 'source:Understanding', '--home-quote', 'Welcome, everyone.',
                                '--use', 'guide:Breathe', '--use-quote', 'Stop if you feel dizzy.')
        self.assertEqual(code, 1)
        self.assertIn('--home-quote: these words are not in source', err)
        self.assertEqual((self.root / D.REGISTRY).read_text(encoding='utf-8'), before)

    def test_refuses_a_quote_that_stands_twice(self):
        code, _, err = self.add('--home', 'source:Ask What They Need', '--home-quote', 'Ask what they need.',
                                '--use', 'guide:Breathe', '--use-quote', 'Stop if you feel dizzy.')
        self.assertEqual(code, 1)
        self.assertIn('stand 2 times in source', err)
        code, _, err = self.add('--home', 'guide:Breathe', '--home-quote', 'Stop if you feel dizzy.',
                                '--use', 'source:Ask What They Need', '--use-quote', 'Ask what they need.')
        self.assertEqual(code, 1)
        self.assertIn('--use-quote: these words stand 2 times in source', err)

    def test_adds_a_point_and_then_a_use_to_it(self):
        code, out, _ = self.add('--home', 'source:Understanding', '--home-quote', 'Welcome.',
                                '--use', 'guide:Breathe', '--use-quote', 'Stop if you feel dizzy.',
                                '--state', 'behind', '--note', 'n', '--from', 'a read of both')
        self.assertEqual(code, 0, out)
        point = self.reg()['points'][-1]
        self.assertEqual((point['id'], point['kind'], point['what'], point['from']),
                         ('N01', 'passage', 'ask what they need', 'a read of both'))
        self.assertEqual(point['home'], {'article': 'source', 'section': 'Understanding', 'quote': 'Welcome.'})
        use = point['uses'][0]
        self.assertEqual((use['article'], use['section'], use['relation'], use['state'], use['note']),
                         ('guide', 'Breathe', 'own words', 'behind', 'n'))
        self.assertRegex(use['as_of'], r'^\d{4}-\d\d-\d\d$')
        code, _, _ = self.run_main('add', '--id', 'N01', '--use', 'guide:Breathe', '--use-quote', 'Try breathing less.',
                                   '--relation', 'pointer')
        self.assertEqual(code, 0)
        self.assertEqual([u['quote'] for u in self.reg()['points'][-1]['uses']],
                         ['Stop if you feel dizzy.', 'Try breathing less.'])
        self.assertEqual(self.run_main('check')[0], 0)
        code, _, err = self.run_main('add', '--id', 'N01', '--use', 'guide:Breathe', '--use-quote', 'Try breathing less.')
        self.assertEqual(code, 1)
        self.assertIn('already has this use', err)
        code, _, err = self.run_main('add', '--id', 'N01', '--home', 'guide:Breathe', '--home-quote', 'Welcome.',
                                     '--use', 'guide:The Guide', '--use-quote', USE_QUOTE)
        self.assertEqual(code, 1)
        self.assertIn('already has another home', err)

    def test_same_words_and_the_same_place(self):
        self.write('articles/guide/master.md', GUIDE_MD + '\nWelcome.\n')
        point = D.add(self.reg(), D.Texts(self.reg(), self.root), 'N02', 'guide:Breathe', 'Welcome.',
                      home='source:Understanding', home_quote='Welcome.', what='the welcome')
        self.assertEqual(point['uses'][0]['relation'], 'same words')
        with self.assertRaises(ValueError) as e:
            D.add(self.reg(), D.Texts(self.reg(), self.root), 'N03', 'guide:Breathe', 'Try breathing less.',
                  home='guide:Breathe', home_quote='Try breathing less. Stop if you feel dizzy.', what='x')
        self.assertIn('the same place', str(e.exception))
        with self.assertRaises(ValueError):
            D.add(self.reg(), D.Texts(self.reg(), self.root), 'N04', 'guide', 'Welcome.', home='source:Understanding',
                  home_quote='Welcome.', what='no section named')


class Changed(Fixture):
    def texts(self, source=SOURCE_HTML, guide=GUIDE_MD):
        return {'source': D.parse(source, 'master.html'), 'guide': D.parse(guide, 'master.md')}

    def test_two_versions_of_a_text(self):
        reg, old = self.reg(), self.texts()
        self.assertEqual(D.changed_between(reg, old, self.texts()), [])
        new = self.texts(source=SOURCE_HTML.replace('one small thing', 'one little thing'))
        findings = D.changed_between(reg, old, new)
        self.assertEqual([(f['id'], f['side'], f['tie']) for f in findings], [('H01', 'home', 'depend on it')])
        self.assertEqual(findings[0]['partners'][0]['quote'], USE_QUOTE)
        lines = D.finding_lines(findings[0], since='origin/main')
        self.assertTrue(lines[0].startswith('you changed this since origin/main (point H01 of articles/DEPENDS.json'))
        self.assertIn('    guide, "The Guide": "Put on the adult hat for a while,…" (own words; in line; 2026-11-25)', lines)
        self.assertEqual(D.changed_between(reg, new, new), [])           # not there before: not this change
        self.assertEqual(D.changed_between(reg, old, new, article='guide'), [])
        self.assertEqual(len(D.changed_between(reg, old, new, article='source')), 1)

    def test_a_changed_use_and_a_renamed_heading(self):
        reg, old = self.reg(), self.texts()
        new = self.texts(source=SOURCE_HTML.replace('Borrowed <em>Adulthood</em>', 'Borrow an Adult'),
                         guide=GUIDE_MD.replace('adult hat', 'grown-up hat'))
        got = {(f['id'], f['side'], f['tie']) for f in D.changed_between(reg, old, new)}
        self.assertEqual(got, {('H01', 'use', 'it depends on'), ('L01', 'home', 'link to it')})

    def test_new_words_in_the_registry_do_not_hide_the_change(self):
        base_reg, old = self.reg(), self.texts()
        new_quote = HOME_QUOTE.replace('one small thing', 'one little thing')
        new = self.texts(source=SOURCE_HTML.replace('one small thing', 'one little thing'))
        reg = self.reg()
        reg['points'][0]['home']['quote'] = new_quote
        self.assertEqual(D.changed_between(reg, old, new), [])
        findings = D.changed_between(reg, old, new, base_reg=base_reg)
        self.assertEqual([(f['id'], f['side']) for f in findings], [('H01', 'home')])
        self.assertEqual(findings[0]['place']['quote'], HOME_QUOTE)

    def test_notice_is_quiet_when_it_cannot_compare(self):
        self.assertEqual(D.notice_lines(base='no-such-ref', root=self.root), [])
        self.assertEqual(self.run_main('changed', '--base', 'no-such-ref')[0], 0)

    @unittest.skipUnless(shutil.which('git'), 'git is not installed')
    def test_through_git(self):
        # A repository of its own in the temporary folder. Every GIT_* variable is taken out first: inside a git hook
        # GIT_DIR names the real repository, and these commands must never reach it.
        env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM='1')
        patch = mock.patch.dict(os.environ, env, clear=True)
        patch.start()
        self.addCleanup(patch.stop)

        def git(*args):
            return subprocess.run(['git', '-c', 'user.name=t', '-c', 'user.email=t@example.invalid',
                                   '-c', 'commit.gpgsign=false', '-c', 'core.hooksPath=' + os.devnull] + list(args),
                                  cwd=str(self.root), capture_output=True)
        if git('init', '-q').returncode or git('add', '-A').returncode or git('commit', '-q', '-m', 'first').returncode:
            self.skipTest('git cannot make a repository here')
        top = git('rev-parse', '--show-toplevel').stdout.decode().strip()
        self.assertEqual(pathlib.Path(top).resolve(), self.root.resolve())
        self.assertEqual(D.notice_lines(base='HEAD', root=self.root), [])
        self.write('articles/source/master.html', SOURCE_HTML.replace('one small thing', 'one little thing'))
        lines = D.notice_lines(article='source', base='HEAD', root=self.root)
        self.assertTrue(lines and lines[0].startswith('you changed this since HEAD (point H01'), lines)
        self.assertTrue(any('guide, "The Guide"' in line for line in lines))
        self.assertEqual(D.notice_lines(article='guide', base='HEAD', root=self.root), [])
        code, out, _ = self.run_main('changed', '--base', 'HEAD')
        self.assertEqual(code, 0)                                         # a notice, never a failure
        self.assertIn('1 registered passage or heading changed since HEAD', out)


class Page(Fixture):
    def test_list(self):
        code, out, _ = self.run_main('list')
        self.assertEqual(code, 0)
        self.assertIn('tools/humanization/depends.py', out.split('\n')[2])
        self.assertIn('articles/DEPENDS.json', out.split('\n')[2])
        self.assertIn('## The Source Guide (source)', out)
        self.assertIn('### What other posts take from this one (2)', out)
        self.assertIn('## The Built-On Guide (guide)', out)
        self.assertIn('### What this one takes from others (2)', out)
        self.assertIn('| **H01** the hat exercise | “Borrowed Adulthood”: “Maybe you copy one small thing you\'ve seen…” | '
                      'guide, “The Guide”: “Put on the adult hat for a while,…” | own words | in line | 2026-11-25 |', out)
        self.assertIn('[Inner Child Guide](https://example.org/i/1/borrowed-adulthood) | link |', out)
        only = self.run_main('list', '--article', 'guide')[1]
        self.assertNotIn('## The Source Guide', only)
        self.assertIn('### What this one takes from others (2)', only)

    def test_write(self):
        code, _, _ = self.run_main('list', '--write')
        self.assertEqual(code, 0)
        self.assertEqual((self.root / D.PAGE).read_text(encoding='utf-8'), D.page(self.reg(), root=self.root))
        self.assertEqual(self.run_main('list', '--write', '--article', 'guide')[0], 1)

    def test_a_pair_inside_one_post_and_a_path_in_a_note(self):
        reg = self.reg()
        reg['points'].append({'id': 'S01', 'what': 'inside the source', 'kind': 'passage',
                              'home': {'article': 'source', 'section': 'Understanding', 'quote': 'Welcome.'},
                              'uses': [{'article': 'source', 'section': 'Ask What They Need', 'quote': 'See my somatic guide.',
                                        'relation': 'pointer', 'state': 'in line', 'as_of': '2026-11-25', 'note': ''}],
                              'from': 'a test'})
        reg['points'][1]['uses'][0]['note'] = 'to go in (articles/guide/master.md, and NOT-THERE/x.md)'
        out = D.page(reg, root=self.root)
        self.assertIn('### Inside this post (1)', out)
        self.assertIn('to go in ([articles/guide/master.md](%sarticles/guide/master.md), and NOT-THERE/x.md)' % D.GIT, out)


class TheRegistry(unittest.TestCase):
    """The shape of articles/DEPENDS.json (not whether its quotes still stand: that is `depends.py check`)."""

    def test_shape(self):
        path = REPO / D.REGISTRY
        if not path.exists():
            self.skipTest('no registry in this checkout')
        reg = json.loads(path.read_text(encoding='utf-8'))
        self.assertTrue(reg['about'] and reg['his_words'][0]['when'] and reg['his_words'][0]['words'])
        ids = [p['id'] for p in reg['points']]
        self.assertEqual(len(ids), len(set(ids)), 'a point id is used twice')
        for p in reg['points']:
            self.assertTrue(p['what'] and p['uses'], p['id'])
            self.assertIn(p['kind'], ('passage', 'link'), p['id'])
            if p['kind'] == 'link':
                self.assertTrue(p['home']['article'] and p['home']['heading'] and p['home']['anchor'], p['id'])
                continue
            self.assertTrue(p['home']['article'] and p['home']['section'] and p['home']['quote'], p['id'])
            for u in p['uses']:
                self.assertTrue(u['article'] and u['section'] and u['quote'], p['id'])
                self.assertIn(u['relation'], D.RELATIONS, p['id'])
                self.assertIn(u['state'], D.STATES, p['id'])
                self.assertRegex(u['as_of'], r'^\d{4}-\d\d-\d\d$', p['id'])


if __name__ == '__main__':
    unittest.main()
