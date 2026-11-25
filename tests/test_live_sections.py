"""live_sections.py: a live Substack post as the sections of articles/<id>/LIVE-SECTIONS.json, which the registry of
shared passages reads (tools/humanization/depends.py) and the daily job compares with (scripts/watch_live_posts.py;
Joel, 2026-11-25 16:14 UTC: "for the registry, yes you can add the github job").

The ground truth is the saved inner-signal copy and the body it was made from. Nothing here touches the network:
every fetch gets a stand-in for urlopen."""
import contextlib
import hashlib
import importlib.util
import io
import json
import pathlib
import re
import sys
import tempfile
import unittest
import urllib.error
from unittest import mock

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import depends as D  # noqa: E402
import live_sections as LS  # noqa: E402

SAVED = REPO / 'articles' / 'inner-signal' / 'LIVE-SECTIONS.json'
BODIES = REPO / 'articles' / 'inner-signal' / 'experiments' / 'toc-20261123'          # its LIVE-BODY-*.html

POST_HTML = (
    'words outside any element'
    '<p>This guide has an <a href="http://example.org/">app coming soon</a>! Working hard!</p>'
    '<p><br></p>'
    '<p class="button-wrapper" data-attrs="{&quot;text&quot;:&quot;Subscribe now&quot;}">'
    '<a class="button primary" href="https://example.org/subscribe?"><span>Subscribe now</span></a></p>'
    '<h1>How to Use This <em>Huge</em> Guide</h1>'
    '<p>Begin with the <a href="#§quick">Quick start section</a>, then see my <a href="https://example.org/p/s">'
    'somatic guide</a>.</p>'
    '<div class="digest-post-embed" data-attrs="{&quot;title&quot;:&quot;Not text&quot;}"></div>'
    '<div class="captioned-image-container"><figure><a class="image-link" href="https://example.org/i.png">'
    '<div class="image2-inset"><picture><source type="image/webp" srcset="a.webp 424w"><img src="i.png" alt="alt">'
    '</picture></div></a><figcaption class="image-caption">A caption</figcaption></figure></div>'
    '<h2>Awareness<strong>es</strong> &amp;  You</h2>'
    '<ul><li><p>First   thing.</p></li><li><p>Second&nbsp;thing, it&#8217;s <strong>bold</strong>.</p></li></ul>'
    '<blockquote><p>Tell me what feels unsafe.</p><p>I&rsquo;m listening.</p></blockquote>'
    '<hr>'
    '<!-- a comment --><p>one<!-- inside -->two</p>'
    '<h3></h3>'
    '<p>Under a heading with no words.\n  Next line.</p>'
    '<div><h2>Not a section: it is inside a block</h2><script>var x = "not text";</script><p>Inside.</p></div>'
    '<style>p { color: red }</style>'
    '<h4>Last</h4>'
    '<p>Unclosed <b>bold</p><p>stray </span>end tag</p>')
POST_SECTIONS = [
    {'id': 'S000', 'level': 0, 'heading': '(before the first heading)',
     'paragraphs': ['This guide has an app coming soon ! Working hard!', 'Subscribe now']},
    {'id': 'S001', 'level': 1, 'heading': 'How to Use This Huge Guide',
     'paragraphs': ['Begin with the Quick start section , then see my somatic guide .', 'A caption']},
    {'id': 'S002', 'level': 2, 'heading': 'Awarenesses & You',
     'paragraphs': ['First thing. Second thing, it’s bold .', 'Tell me what feels unsafe. I’m listening.', 'one two']},
    {'id': 'S003', 'level': 3, 'heading': '', 'paragraphs': [
        'Under a heading with no words. Next line.', 'Not a section: it is inside a block Inside.']},
    {'id': 'S004', 'level': 4, 'heading': 'Last', 'paragraphs': ['Unclosed bold', 'stray end tag']}]


def answer(body=POST_HTML, **more):
    post = {'id': 4242, 'title': 'A Guide', 'subtitle': 'Its subtitle', 'slug': 'a-guide',
            'canonical_url': 'https://example.substack.com/p/a-guide', 'post_date': '2026-06-24T14:39:28.546Z',
            'updated_at': '2026-11-25T12:00:39.424Z', 'wordcount': 123, 'audience': 'everyone', 'body_html': body,
            'reactions': {'❤': 3}}
    post.update(more)
    return post


class Response:
    def __init__(self, raw, status=200):
        self.raw, self.status = raw, status

    def read(self):
        return self.raw

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def http_error(code, reason):
    return urllib.error.HTTPError('https://example.substack.com/x', code, reason, {}, io.BytesIO(b''))


class Opener:
    """Stands in for urllib.request.urlopen: gives each answer in turn (an exception is raised)."""

    def __init__(self, *answers):
        self.answers, self.requests, self.timeouts = list(answers), [], []

    def __call__(self, request, timeout=None):
        self.requests.append(request)
        self.timeouts.append(timeout)
        a = self.answers.pop(0)
        if isinstance(a, Exception):
            raise a
        return a


class GroundTruth(unittest.TestCase):
    """A saved copy and the body it was made from: this tool has to make the same sections from the same body.

    The saved inner-signal copy of 2026-11-25 12:00 UTC was made by hand (BeautifulSoup) from
    LIVE-BODY-20261125-after.html, and this tool gave the same 160 sections and the same file. The lane saves the post
    again after each edit, with the new body beside the old ones, so the body is never named here: it is the
    LIVE-BODY-*.html whose sha256 is the one the saved copy records ("post.body_sha256")."""

    def body_of(self, folder, post):
        for path in sorted(folder.rglob('LIVE-BODY-*.html')):
            body = path.read_bytes().decode('utf-8')
            if LS.body_sha256(body) == post.get('body_sha256'):
                return body
        return None

    def same(self, saved_path, body):
        saved_text = saved_path.read_bytes().decode('utf-8')
        saved = json.loads(saved_text)
        made = LS.sections(body)
        self.assertEqual(len(made), len(saved['sections']))
        for mine, theirs in zip(made, saved['sections']):
            self.assertEqual(mine, theirs, theirs['id'])
        doc = LS.build(dict(saved['post'], body_html=body), fetched=saved['post']['fetched'],
                       source=saved['post']['source'])
        self.assertEqual(doc, saved)
        self.assertEqual(LS.dumps(doc), saved_text)                 # the file itself, to the last character

    def test_inner_signal_and_the_body_it_was_made_from(self):
        if not SAVED.exists():
            self.skipTest('the saved inner-signal copy is not in this checkout')
        body = self.body_of(BODIES, json.loads(SAVED.read_text(encoding='utf-8'))['post'])
        if body is None:
            self.skipTest('no LIVE-BODY-*.html in %s has the sha256 the saved copy records' % BODIES.name)
        self.same(SAVED, body)

    def test_every_saved_copy_whose_body_is_in_the_repository(self):
        if not (REPO / D.REGISTRY).exists():
            self.skipTest('no registry in this checkout')
        checked = []
        for article, row in LS.posts(REPO).items():
            body = self.body_of(REPO / 'articles' / article, row['post'])
            if body is not None:
                self.same(REPO / row['path'], body)
                checked.append(article)
        if not checked:
            self.skipTest('no saved copy has its body (LIVE-BODY-*.html with the recorded sha256) in this checkout')

    def test_the_saved_copies_have_the_shape_this_tool_writes(self):
        if not (REPO / D.REGISTRY).exists():
            self.skipTest('no registry in this checkout')
        for article, row in LS.posts(REPO).items():
            if not (REPO / row['path']).exists():
                continue
            text = (REPO / row['path']).read_bytes().decode('utf-8')
            saved = json.loads(text)
            self.assertEqual(LS.dumps(saved), text, row['path'])
            self.assertEqual(list(saved['post']), list(LS.META) + ['source', 'fetched', 'body_sha256'], row['path'])
            self.assertTrue(row['id'], row['path'])
            self.assertEqual([s['id'] for s in saved['sections']],
                             ['S%03d' % i for i in range(len(saved['sections']))], row['path'])
            self.assertEqual((saved['sections'][0]['level'], saved['sections'][0]['heading']), (0, LS.BEFORE))
            for s in saved['sections']:
                self.assertEqual(list(s), ['id', 'level', 'heading', 'paragraphs'], row['path'])
                self.assertTrue(all(p and p == re.sub(r'\s+', ' ', p).strip() for p in s['paragraphs']), s['id'])


class Rules(unittest.TestCase):
    def test_a_post_with_every_kind_of_block(self):
        self.assertEqual(LS.sections(POST_HTML), POST_SECTIONS)

    def test_no_headings_and_nothing_at_all(self):
        self.assertEqual(LS.sections('<p>Only this.</p>'), [
            {'id': 'S000', 'level': 0, 'heading': LS.BEFORE, 'paragraphs': ['Only this.']}])
        self.assertEqual(LS.sections(''), [{'id': 'S000', 'level': 0, 'heading': LS.BEFORE, 'paragraphs': []}])
        self.assertEqual(LS.sections(None), LS.sections(''))

    def test_headings_are_numbered_in_order_whatever_their_level(self):
        made = LS.sections('<h3>C</h3><p>c</p><h1>A</h1><h6>F</h6><p>f</p><h2>B</h2>')
        self.assertEqual([(s['id'], s['level'], s['heading'], s['paragraphs']) for s in made], [
            ('S000', 0, LS.BEFORE, []), ('S001', 3, 'C', ['c']), ('S002', 1, 'A', []), ('S003', 6, 'F', ['f']),
            ('S004', 2, 'B', [])])

    def test_a_link_leaves_a_space_and_emphasis_inside_a_heading_does_not(self):
        made = LS.sections('<h2>Don\'t <em>Rush</em> the Repair<strong>s</strong></h2>'
                           '<p>See <a href="x">my <em>somatic</em> guide</a>.</p>')
        self.assertEqual(made[1]['heading'], "Don't Rush the Repairs")
        self.assertEqual(made[1]['paragraphs'], ['See my somatic guide .'])
        # the registry's comparison takes that space out again, so a quote written without it is found
        text = D.parse(json.dumps({'sections': made}), 'x.json')
        self.assertEqual(D.count('See my somatic guide.', text.text), 1)
        self.assertEqual(text.headings, ["Don't Rush the Repairs"])

    def test_whitespace_and_character_references(self):
        made = LS.sections('<p>\n  a&nbsp;b \t c&amp;d &lt;e&gt; &#233; &#x2019; &quot;q&quot; AT&T &copy 2026 ​z</p>'
                           '<p> \n </p><p>&nbsp;</p>')
        self.assertEqual(made[0]['paragraphs'], ['a b c&d <e> é ’ "q" AT&T © 2026 ​z'])

    def test_what_is_not_text(self):
        made = LS.sections('<script>top()</script><style>a{}</style><template><p>t</p></template>'
                           '<p>kept<script>nested()</script><style>b{}</style></p><!-- c --><!DOCTYPE html>'
                           '<div data-attrs="{&quot;caption&quot;:&quot;Not text&quot;}"><iframe src="v"></iframe></div>'
                           '<p><img src="x" alt="not text" title="nor this"></p><svg><title>t</title></svg>')
        self.assertEqual(made[0]['paragraphs'], ['kept', 't'])       # an svg's <title> is text, as it was in the files

    def test_tags_that_are_not_closed_or_not_opened(self):
        self.assertEqual(LS.sections('<p>a<p>b</p>')[0]['paragraphs'], ['a b'])              # the second is inside the first
        self.assertEqual(LS.sections('<p>a</div>b</p><p>c</p>')[0]['paragraphs'], ['a b', 'c'])
        self.assertEqual(LS.sections('<div><p>a<span>b</div><p>c</p>')[0]['paragraphs'], ['a b', 'c'])
        self.assertEqual(LS.sections('<p>a<br>b<br/>c</br>d</p><hr><hr/><p>e</p>')[0]['paragraphs'], ['a b cd', 'e'])
        self.assertEqual(LS.sections('<p>never closed <b>at all')[0]['paragraphs'], ['never closed at all'])

    @unittest.skipUnless(importlib.util.find_spec('bs4'), 'needs BeautifulSoup (CI installs nothing)')
    def test_the_same_as_the_method_that_made_the_saved_files(self):
        """make_files.py in articles/inner-signal/experiments/toc-20261123 read the body with BeautifulSoup."""
        from bs4 import BeautifulSoup, Tag

        def with_bs4(html):
            out = [{'id': 'S000', 'level': 0, 'heading': LS.BEFORE, 'paragraphs': []}]
            for b in BeautifulSoup(html, 'html.parser').children:
                if not isinstance(b, Tag) or b.name in ('script', 'style', 'template'):
                    continue
                if re.fullmatch(r'h[1-6]', b.name or ''):
                    out.append({'id': 'S%03d' % len(out), 'level': int(b.name[1]),
                                'heading': re.sub(r'\s+', ' ', b.get_text('')).strip(), 'paragraphs': []})
                    continue
                t = re.sub(r'\s+', ' ', b.get_text(' ', strip=True)).strip()
                if t:
                    out[-1]['paragraphs'].append(t)
            return out

        bodies = [POST_HTML] + [p.read_bytes().decode('utf-8')
                                for p in sorted((REPO / 'articles').rglob('LIVE-BODY-*.html'))]
        for body in bodies:
            self.assertEqual(LS.sections(body), with_bs4(body))


class Build(unittest.TestCase):
    def test_the_document(self):
        doc = LS.build(answer(), fetched='2026-11-26')
        self.assertEqual(list(doc), ['post', 'sections'])
        self.assertEqual(doc['post'], {
            'id': 4242, 'title': 'A Guide', 'subtitle': 'Its subtitle', 'slug': 'a-guide',
            'canonical_url': 'https://example.substack.com/p/a-guide', 'post_date': '2026-06-24T14:39:28.546Z',
            'updated_at': '2026-11-25T12:00:39.424Z', 'wordcount': 123,
            'source': 'https://example.substack.com/api/v1/posts/by-id/4242, fetched by '
                      'tools/humanization/live_sections.py (public post API)',
            'fetched': '2026-11-26', 'body_sha256': LS.body_sha256(POST_HTML)})
        self.assertEqual(doc['sections'], POST_SECTIONS)
        self.assertRegex(LS.build(answer())['post']['fetched'], r'^\d{4}-\d\d-\d\d$')
        self.assertEqual(LS.build(answer(), source='read by hand')['post']['source'], 'read by hand')

    def test_the_post_under_post_and_an_answer_without_a_body(self):
        self.assertEqual(LS.build({'post': answer()}, fetched='2026-11-26'), LS.build(answer(), fetched='2026-11-26'))
        for bad in ({}, {'post': {'id': 1}}, {'id': 1, 'body_html': None}, [], None):
            with self.assertRaises(LS.FetchError) as e:
                LS.build(bad)
            self.assertIn('no body_html', str(e.exception))

    def test_the_file_is_written_like_the_saved_copies(self):
        text = LS.dumps(LS.build(answer('<h1>A</h1><p>b “c”</p>'), fetched='2026-11-26'))
        self.assertTrue(text.startswith('{\n"post": {\n"id": 4242,\n"title": "A Guide",'))
        self.assertTrue(text.endswith('"paragraphs": [\n"b “c”"\n]\n}\n]\n}'))
        self.assertEqual(json.loads(text)['sections'][1]['heading'], 'A')

    def test_the_sha_is_of_the_body_as_given(self):
        self.assertEqual(LS.body_sha256('<p>é</p>'), hashlib.sha256('<p>é</p>'.encode('utf-8')).hexdigest())
        self.assertNotEqual(LS.body_sha256('<p>a</p>'), LS.body_sha256('<p>a</p>\n'))


class Fetch(unittest.TestCase):
    def raw(self, obj):
        return json.dumps(obj).encode('utf-8')

    def test_a_post_at_the_top_or_under_post(self):
        for shape in (answer(), {'post': answer()}):
            opener = Opener(Response(self.raw(shape)))
            post = LS.fetch_post(4242, 'https://example.substack.com', timeout=7, urlopen=opener)
            self.assertEqual(post['body_html'], POST_HTML)
            request = opener.requests[0]
            self.assertEqual(request.full_url, 'https://example.substack.com/api/v1/posts/by-id/4242')
            self.assertIn('Mozilla/5.0', request.get_header('User-agent'))
            self.assertNotIn('python', request.get_header('User-agent').lower())
            self.assertEqual(opener.timeouts, [7])

    def test_his_publication_by_default(self):
        opener = Opener(Response(self.raw(answer())))
        LS.fetch_post(202810155, urlopen=opener)
        self.assertEqual(opener.requests[0].full_url, 'https://ibogaqueen.substack.com/api/v1/posts/by-id/202810155')

    def test_a_refusal_is_final_and_keeps_its_status(self):
        opener, naps = Opener(http_error(403, 'Forbidden')), []
        with self.assertRaises(LS.FetchError) as e:
            LS.fetch_post(4242, urlopen=opener, sleep=naps.append)
        self.assertEqual((e.exception.status, str(e.exception)), (403, 'HTTP 403 Forbidden'))
        self.assertEqual(e.exception.url, 'https://ibogaqueen.substack.com/api/v1/posts/by-id/4242')
        self.assertEqual((len(opener.requests), naps), (1, []))

    def test_a_busy_server_and_a_dropped_line_are_tried_again(self):
        opener, naps = Opener(http_error(503, 'Service Unavailable'), urllib.error.URLError('timed out'),
                              Response(self.raw(answer()))), []
        post = LS.fetch_post(4242, urlopen=opener, sleep=naps.append, pause=5)
        self.assertEqual((post['id'], len(opener.requests), naps), (4242, 3, [5, 10]))
        opener = Opener(http_error(429, 'Too Many Requests'), http_error(429, 'Too Many Requests'),
                        http_error(429, 'Too Many Requests'))
        with self.assertRaises(LS.FetchError) as e:
            LS.fetch_post(4242, urlopen=opener, sleep=naps.append)
        self.assertEqual((e.exception.status, len(opener.requests)), (429, 3))
        opener = Opener(TimeoutError('timed out'), OSError('reset'))
        with self.assertRaises(LS.FetchError) as e:
            LS.fetch_post(4242, tries=2, urlopen=opener, sleep=naps.append)
        self.assertEqual((e.exception.status, str(e.exception)), (None, 'no answer (reset)'))

    def test_an_answer_that_is_not_a_post(self):
        with self.assertRaises(LS.FetchError) as e:
            LS.fetch_post(4242, urlopen=Opener(Response(b'<!DOCTYPE html><title>Just a moment...</title>')))
        self.assertEqual(e.exception.status, 200)
        self.assertIn('HTTP 200, but the answer is not JSON (it starts: <!DOCTYPE html><title>Just a moment', str(e.exception))
        with self.assertRaises(LS.FetchError) as e:
            LS.fetch_post(4242, urlopen=Opener(Response(self.raw({'error': 'not found'}))))
        self.assertEqual(str(e.exception), 'HTTP 200, but the answer has no body_html')


class Repo(unittest.TestCase):
    """A small repository: a registry whose "texts" names one saved live post, one master and one missing file."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self._tmp.name)
        (self.root / 'articles' / 'guide').mkdir(parents=True)
        (self.root / 'articles' / 'guide' / 'LIVE-SECTIONS.json').write_text(
            LS.dumps(LS.build(answer(), fetched='2026-11-25')), encoding='utf-8')
        (self.root / 'articles' / 'guide' / 'master.html').write_text('<h1>A</h1>', encoding='utf-8')
        (self.root / D.REGISTRY).write_text(json.dumps({'texts': {
            'guide': 'articles/guide/LIVE-SECTIONS.json', 'old': 'articles/guide/master.html',
            'gone': 'articles/gone/LIVE-SECTIONS.json'}, 'points': []}), encoding='utf-8')
        guard = mock.patch('urllib.request.urlopen', side_effect=AssertionError('a test touched the network'))
        guard.start()
        self.addCleanup(guard.stop)
        self.addCleanup(self._tmp.cleanup)

    def run_main(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = LS.main(['--root', str(self.root)] + list(args))
        return code, out.getvalue(), err.getvalue()

    def test_posts(self):
        known = LS.posts(self.root)
        self.assertEqual(list(known), ['guide', 'old', 'gone'])
        self.assertEqual((known['guide']['id'], known['guide']['url']),
                         (4242, 'https://example.substack.com/api/v1/posts/by-id/4242'))
        self.assertIsNone(known['old']['id'])
        self.assertIn('cannot be read', known['old']['why'] + known['gone']['why'])
        code, out, _ = self.run_main('posts')
        self.assertEqual(code, 0)
        self.assertIn('guide  4242  https://example.substack.com/api/v1/posts/by-id/4242', out)

    def test_build_fetches_and_prints_or_writes(self):
        newer = answer(POST_HTML + '<p>One more.</p>', updated_at='2026-11-26T08:00:00.000Z')
        with mock.patch.object(LS, 'fetch_post', return_value=newer) as fetch:
            code, out, _ = self.run_main('build', '--article', 'guide')
            self.assertEqual(code, 0)
            self.assertEqual(fetch.call_args[0], (4242, 'https://example.substack.com'))
            doc = json.loads(out)
            self.assertEqual(doc['sections'][-1]['paragraphs'][-1], 'One more.')
            self.assertEqual(doc['post']['updated_at'], '2026-11-26T08:00:00.000Z')
            target = self.root / 'out.json'
            code, out, err = self.run_main('build', '--article', 'guide', '--out', str(target))
            self.assertEqual((code, out), (0, ''))
            self.assertIn('written:', err)
            self.assertEqual(json.loads(target.read_text(encoding='utf-8'))['sections'], doc['sections'])
            self.assertFalse(target.read_text(encoding='utf-8').endswith('\n'))

    def test_build_from_a_saved_answer(self):
        saved = self.root / 'POST.json'
        saved.write_text(json.dumps({'post': answer()}), encoding='utf-8')
        code, out, _ = self.run_main('build', '--article', 'guide', '--from', str(saved))
        self.assertEqual(code, 0)
        doc = json.loads(out)
        self.assertEqual(doc['sections'], POST_SECTIONS)
        self.assertIn('read from POST.json', doc['post']['source'])
        code, out, _ = self.run_main('build', '--article', 'guide', '--from', str(saved), '--fetched', '2026-11-25',
                                     '--source', LS.build(answer())['post']['source'])
        self.assertEqual((code, out.rstrip('\n')),                    # the saved copy again, to the last character
                         (0, (self.root / 'articles' / 'guide' / 'LIVE-SECTIONS.json').read_text(encoding='utf-8')))
        saved.write_text(json.dumps(answer(id=999)), encoding='utf-8')
        code, _, err = self.run_main('build', '--article', 'guide', '--from', str(saved))
        self.assertEqual(code, 1)
        self.assertIn('the answer is post 999, and the saved copy is post 4242', err)

    def test_build_says_what_it_could_not_do(self):
        code, _, err = self.run_main('build', '--article', 'nobody')
        self.assertEqual(code, 1)
        self.assertIn('no saved live post', err)
        code, _, err = self.run_main('build', '--article', 'old')
        self.assertEqual(code, 1)
        with mock.patch.object(LS, 'fetch_post', side_effect=LS.FetchError('HTTP 403 Forbidden', 403, 'https://x/api')):
            code, out, err = self.run_main('build', '--article', 'guide')
        self.assertEqual((code, out), (2, ''))
        self.assertIn('guide: post 4242 could not be had: HTTP 403 Forbidden (https://x/api)', err)


if __name__ == '__main__':
    unittest.main()
