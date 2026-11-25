#!/usr/bin/env python3
"""live_sections.py - a live Substack post as the list of its sections: the file articles/<id>/LIVE-SECTIONS.json.

The registry of shared passages (articles/DEPENDS.json, tools/humanization/depends.py) reads each article's words in
articles/<id>/LIVE-SECTIONS.json, the text of its live post by section. Until 2026-11-25 those files were made by hand
from a body fetched on his laptop. This tool makes one from the post as Substack's public API gives it, so the daily
job (scripts/watch_live_posts.py; Joel, 2026-11-25 16:14 UTC: "for the registry, yes you can add the github job") and
a lane refreshing its saved copy both get the same sections from the same HTML.

The shape: {"post": {id, title, subtitle, slug, canonical_url, post_date, updated_at, wordcount, source, fetched,
body_sha256}, "sections": [{"id": "S000", "level": 0, "heading": "(before the first heading)", "paragraphs": [...]},
{"id": "S001", "level": 1, "heading": ..., "paragraphs": [...]}, ...]}. body_sha256 is the sha256 of the post's
body_html as the API gave it.

The rules, read from the four saved files and from the method that made them (make_files.py in
articles/inner-signal/experiments/toc-20261123, which uses BeautifulSoup; CI installs nothing, so this file does the
same with the standard library, and tests/test_live_sections.py holds it to the saved inner-signal copy):

  - Only the elements at the top of the body count as blocks. Words outside any element are left out.
  - A top-level h1 to h6 starts a section. Sections are numbered in order, S001 for the first heading; S000 is the
    stretch before it and is always there, even when empty. The level is the heading's number. A heading with no
    words still starts a section (its heading is "").
  - A heading's words are joined as they stand (Awareness<strong>es</strong> is "Awarenesses"), then runs of
    whitespace become one space.
  - Every other top-level element with words is one paragraph: a <p>, a whole list (its items in one paragraph), a
    whole quote, a button (its label, "Subscribe now"), an embed or a picture (whatever words it shows, often none).
    Its pieces of text, cut wherever a tag starts or ends, are each trimmed and joined with one space, so a link
    leaves a space around its words ("my somatic guide ." where the link ends before the full stop). Runs of
    whitespace become one space, a non-breaking space included. An element with no words is no paragraph.
  - Tags leave nothing else: no link address, no attribute, no comment, and nothing from script, style or template.

  python3 tools/humanization/live_sections.py posts                       # each article and its post's id
  python3 tools/humanization/live_sections.py build --article inner-signal            # fetch, print the file
  python3 tools/humanization/live_sections.py build --article inner-signal --out FILE # ... or write it
        # (the lane that owns the post writes articles/inner-signal/LIVE-SECTIONS.json; the file is written as the
        # saved copies are, so an unchanged post gives the same "sections" and "body_sha256", character for character)
  python3 tools/humanization/live_sections.py build --article inner-signal --from POST.json [--out FILE]
        # POST.json is the API's answer saved where Substack can be reached (the cloud shell's proxy refuses it):
        #   curl -A "Mozilla/5.0" https://ibogaqueen.substack.com/api/v1/posts/by-id/202810155 > POST.json
        # --source "..." sets the note in "source" and --fetched YYYY-MM-DD the day in "fetched" (default: today, UTC)
"""
import argparse
import datetime
import hashlib
import html.entities
import html.parser
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import depends as D  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[2]
PUBLICATION = 'https://ibogaqueen.substack.com'
API = '%s/api/v1/posts/by-id/%s'
# Substack answers a script's default User-Agent with 403, so the request names a browser. Nothing else is sent.
USER_AGENT = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 '
              'Safari/537.36')
BEFORE = '(before the first heading)'
META = ('id', 'title', 'subtitle', 'slug', 'canonical_url', 'post_date', 'updated_at', 'wordcount')

# ---------------------------------------------------------------- the body's blocks

_VOID = frozenset('area base basefont bgsound br col command embed frame hr image img input isindex keygen link '
                  'menuitem meta nextid param source spacer track wbr'.split())
_SILENT = frozenset(('script', 'style', 'template', 'rt', 'rp'))
_NAMES = {}
for _name, _char in sorted(html.entities.html5.items()):
    _NAMES.setdefault(_name.rstrip(';'), _char)


def _charref(number):
    if number == 0 or number > 0x10FFFF or 0xD800 <= number <= 0xDFFF:
        return '\ufffd'
    if 0x80 <= number <= 0x9F:                       # written as Windows-1252, as browsers read it
        try:
            return bytes([number]).decode('cp1252')
        except UnicodeDecodeError:
            pass
    return chr(number)


class _Blocks(html.parser.HTMLParser):
    """The top-level elements of a body, each with its pieces of text: [(tag, [text, ...]), ...].

    A piece of text ends wherever a tag, a comment or a declaration stands. An end tag closes every element opened
    since the tag it names; an end tag that names no open element closes nothing; nothing closes by itself except an
    element that can have no content (br, hr, img, ...). This is how BeautifulSoup's "html.parser" reads a body, which
    the saved files were made with."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.blocks, self._stack, self._data, self._strings, self._closed = [], [], [], None, []

    def _flush(self):
        text, self._data = ''.join(self._data), []
        if text and self._strings is not None and not _SILENT.intersection(self._stack):
            self._strings.append(text)

    def _open(self, tag):
        self._flush()
        if not self._stack:
            self._strings = []
            self.blocks.append((tag, self._strings))
        self._stack.append(tag)

    def _close(self, tag):
        self._flush()
        if tag in self._stack:
            while self._stack.pop() != tag:
                pass
        if not self._stack:
            self._strings = None

    def handle_starttag(self, tag, attrs):
        self._open(tag)
        if tag in _VOID:
            self._close(tag)
            self._closed.append(tag)

    def handle_startendtag(self, tag, attrs):
        self._open(tag)
        self._close(tag)

    def handle_endtag(self, tag):
        if tag in self._closed:                      # </br> after <br>: already closed
            self._closed.remove(tag)
        else:
            self._close(tag)

    def handle_data(self, data):
        self._data.append(data)

    def handle_entityref(self, name):
        self._data.append(_NAMES.get(name, '&' + name))

    def handle_charref(self, name):
        sixteen = name[:1] in ('x', 'X')
        m = re.match(r'([0-9a-fA-F]+)(.*)' if sixteen else r'([0-9]+)(.*)', name[1:] if sixteen else name, re.S)
        self._data.append(_charref(int(m.group(1), 16 if sixteen else 10)) + m.group(2) if m else name)

    def handle_comment(self, data):
        self._flush()

    def handle_decl(self, decl):
        self._flush()

    def handle_pi(self, data):
        self._flush()

    def unknown_decl(self, data):
        self._flush()
        if data.upper().startswith('CDATA['):
            self._data.append(data[6:])
            self._flush()

    def close(self):
        super().close()
        self._flush()
        self._stack, self._strings = [], None


def blocks(body_html):
    """[(tag, [piece of text, ...]), ...] for each top-level element of a post's body."""
    p = _Blocks()
    p.feed(body_html or '')
    p.close()
    return p.blocks


def _one_space(text):
    return re.sub(r'\s+', ' ', text).strip()


def sections(body_html):
    """The sections of a post's body, in the shape of LIVE-SECTIONS.json's "sections"."""
    out = [{'id': 'S000', 'level': 0, 'heading': BEFORE, 'paragraphs': []}]
    for tag, strings in blocks(body_html):
        if re.fullmatch(r'h[1-6]', tag):
            out.append({'id': 'S%03d' % len(out), 'level': int(tag[1]), 'heading': _one_space(''.join(strings)),
                        'paragraphs': []})
            continue
        text = _one_space(' '.join(s.strip() for s in strings if s.strip()))
        if text:
            out[-1]['paragraphs'].append(text)
    return out


# ---------------------------------------------------------------- the post, as the API gives it

class FetchError(Exception):
    """A post that could not be had. status is the HTTP status when Substack answered, else None."""

    def __init__(self, reason, status=None, url=None):
        super().__init__(reason)
        self.reason, self.status, self.url = reason, status, url

    def __str__(self):
        return self.reason


def api_url(post_id, base=PUBLICATION):
    return API % (base.rstrip('/'), post_id)


def publication(post):
    """The publication's address, from a saved or fetched post's canonical_url (else his Substack)."""
    parts = urllib.parse.urlsplit((post or {}).get('canonical_url') or '')
    if parts.scheme in ('http', 'https') and parts.netloc:
        return '%s://%s' % (parts.scheme, parts.netloc)
    return PUBLICATION


def post_of(answer, url=None):
    """The post in the API's answer (at the top, or under "post"), or FetchError when it has no body_html."""
    post = None
    if isinstance(answer, dict):
        post = answer if 'body_html' in answer else answer.get('post')
    if not isinstance(post, dict) or not isinstance(post.get('body_html'), str):
        raise FetchError('the answer has no body_html', None, url)
    return post


# Where else the same post API answers. On 2026-11-25 the daily job's first run on GitHub got HTTP 403 for all four posts
# from the publication's own address (Substack refuses GitHub's servers there). Substack's own address serves the same
# API with the same body_html (read from his laptop the same day: both addresses, two posts, equal sha256).
ELSEWHERE = ('https://substack.com',)


def fetch_post(post_id, base=PUBLICATION, timeout=30, tries=3, pause=5, urlopen=None, sleep=time.sleep,
               elsewhere=ELSEWHERE):
    """The post from the publication's address; when that address refuses (HTTP 403), from each address in
    `elsewhere` in turn. The first refusal is the one raised when none answers, with what the others said added."""
    try:
        return _fetch_post(post_id, base, timeout, tries, pause, urlopen, sleep)
    except FetchError as first:
        if first.status != 403:
            raise
        said = []
        for other in elsewhere or ():
            if other.rstrip('/') == base.rstrip('/'):
                continue
            try:
                return _fetch_post(post_id, other, timeout, tries, pause, urlopen, sleep)
            except FetchError as e:
                said.append('%s: %s' % (other, e.reason))
        if said:
            first.reason = '%s (also tried %s)' % (first.reason, '; '.join(said))
        raise first


def _fetch_post(post_id, base=PUBLICATION, timeout=30, tries=3, pause=5, urlopen=None, sleep=time.sleep):
    """The post as the public API gives it (a dict with body_html), or FetchError.

    A network error, a 429 and a 5xx are tried again (tries in all, pause seconds apart, then twice that); any other
    refusal is final. urlopen and sleep are there for the tests, which never touch the network."""
    url = api_url(post_id, base)
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'application/json'})
    error = FetchError('not tried', None, url)
    for attempt in range(1, max(1, tries) + 1):
        try:
            with (urlopen or urllib.request.urlopen)(request, timeout=timeout) as response:
                status = getattr(response, 'status', None) or 200
                raw = response.read()
        except urllib.error.HTTPError as e:
            error = FetchError('HTTP %s %s' % (e.code, e.reason or ''), e.code, url)
            if e.code != 429 and e.code < 500:
                break
        except (urllib.error.URLError, OSError, ValueError) as e:
            error = FetchError('no answer (%s)' % (getattr(e, 'reason', None) or e), None, url)
        else:
            try:
                return post_of(json.loads(raw.decode('utf-8')), url)
            except FetchError as e:
                error = FetchError('HTTP %s, but %s' % (status, e.reason), status, url)
            except (ValueError, UnicodeError):
                start = _one_space(raw[:80].decode('utf-8', 'replace'))
                error = FetchError('HTTP %s, but the answer is not JSON (it starts: %s)' % (status, start), status, url)
            break
        if attempt < tries:
            sleep(pause * attempt)
    error.reason = error.reason.strip()
    raise error


def body_sha256(body_html):
    return hashlib.sha256(body_html.encode('utf-8')).hexdigest()


def build(post, fetched=None, source=None):
    """The LIVE-SECTIONS.json document for a post (the API's answer, or a dict with the same keys and body_html)."""
    post = post_of(post)
    url = api_url(post.get('id'), publication(post))
    meta = {k: post.get(k) for k in META}
    meta['source'] = source or '%s, fetched by tools/humanization/live_sections.py (public post API)' % url
    meta['fetched'] = fetched or datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    meta['body_sha256'] = body_sha256(post['body_html'])
    return {'post': meta, 'sections': sections(post['body_html'])}


def dumps(doc):
    """The file's text, as the saved copies are written (one value a line, no indent, no last newline)."""
    return json.dumps(doc, ensure_ascii=False, indent=0)


# ---------------------------------------------------------------- which article is which post

def posts(root=REPO, reg=None):
    """{article: {"id", "path", "url", "post"}} for every article the registry's "texts" names: the post's id is read
    from the saved file's "post". "id" is None, with "why", when the file is not a saved live post."""
    root = pathlib.Path(root)
    reg = reg or D.load(root)
    out = {}
    for article, path in (reg.get('texts') or {}).items():
        row = {'id': None, 'path': path, 'url': None, 'post': {}}
        try:
            saved = json.loads((root / path).read_text(encoding='utf-8'))
            row['post'] = saved['post'] if isinstance(saved, dict) and isinstance(saved.get('post'), dict) else {}
            row['id'] = row['post'].get('id')
            if not row['id']:
                row['why'] = '%s has no "post" with an "id"' % path
        except (OSError, ValueError) as e:
            row['why'] = '%s cannot be read: %s' % (path, e)
        if row['id']:
            row['url'] = api_url(row['id'], publication(row['post']))
        out[article] = row
    return out


# ---------------------------------------------------------------- the commands

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--root', default=str(REPO), help='the repository (default: this one)')
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('posts', help='each article the registry reads in a saved live post, and the post\'s id')
    b = sub.add_parser('build', help='fetch an article\'s live post and print (or write) its LIVE-SECTIONS.json')
    b.add_argument('--article', required=True)
    b.add_argument('--out', metavar='FILE', help='write the file here (default: print it)')
    b.add_argument('--from', dest='answer', metavar='POST.json', help='the API\'s answer saved in a file: no fetch')
    b.add_argument('--source', help='the note for "source" (default: the API address and how it was read)')
    b.add_argument('--fetched', metavar='YYYY-MM-DD', help='the day for "fetched" (default: today, UTC)')
    b.add_argument('--timeout', type=float, default=30)
    args = ap.parse_args(argv)
    known = posts(args.root)

    if args.cmd == 'posts':
        for article, row in known.items():
            print('%s  %s  %s' % (article, row['id'] or '-', row['url'] or row.get('why')))
        return 0

    row = known.get(args.article)
    if row is None or not row['id']:
        print('%s: %s' % (args.article, row['why'] if row else 'the registry\'s "texts" has no saved live post for '
                                                               'it (articles/DEPENDS.json)'), file=sys.stderr)
        return 1
    try:
        if args.answer:
            name = pathlib.Path(args.answer).name
            post = post_of(json.loads(pathlib.Path(args.answer).read_text(encoding='utf-8')), row['url'])
            source = args.source or '%s, read from %s (public post API)' % (row['url'], name)
        else:
            post = fetch_post(row['id'], publication(row['post']), timeout=args.timeout)
            source = args.source
    except FetchError as e:
        print('%s: post %s could not be had: %s (%s)' % (args.article, row['id'], e, e.url), file=sys.stderr)
        return 2
    if str(post.get('id')) != str(row['id']):
        print('%s: the answer is post %s, and the saved copy is post %s' % (args.article, post.get('id'), row['id']),
              file=sys.stderr)
        return 1
    text = dumps(build(post, fetched=args.fetched, source=source))
    if args.out:
        pathlib.Path(args.out).write_text(text, encoding='utf-8')
        print('written: %s (%d sections, updated on Substack %s)'
              % (args.out, text.count('"id": "S'), post.get('updated_at')), file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
