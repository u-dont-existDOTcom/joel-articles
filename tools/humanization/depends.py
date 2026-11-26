#!/usr/bin/env python3
"""depends.py - which passages of his guides are the same point, and what to re-read when one of them changes.

Joel, 2026-11-25 11:18 UTC: "make sure we have a common reference point for the things that are common, in our github
version control system for the articles rigth, or some way to know when one thing changes that another thing is
dependent on in same article or diff article."

Several of his guides share passages: one guide was built on another, repeats a practice, a caution, an instruction or
a term from it, or links to one of its sections. articles/BUILT-ON.json records that at the level of sections (which
sections of one post are built on another post). This tool keeps the level below it, in the registry
articles/DEPENDS.json: a list of points. A point is one passage (its home: article, section, the exact words) and the
passages that take from it (its uses), each with its own exact words, how it relates to the home ("same words", "own
words", "pointer", "differs"), and where it stands ("in line", "behind", "his to settle", "left as it is") on which
day. A point of kind "link" is a section of a post (its heading and anchor) and the links to it from other places. A
use may sit in the same article as its home.

The words are looked for in each article's current text: the file given with --text, else the one the registry's
"texts" names for that article, else the article's registered master (articles/INDEX.json). A text is .html, .md,
.txt, or a .json list of sections ({"heading", "paragraphs": [...]} or {"heading", "text"}, as the contents lanes
save a live post). The comparison is on plain text: HTML tags and Markdown emphasis and link markup are dropped, runs
of whitespace count as one space, curly and straight quotes and apostrophes are the same, and so are a non-breaking
space and a space. A space before a full stop, comma or other closing mark is ignored too, because the section files
put one where a link ends ("my somatic guide ."). In a .txt file a heading is a line of its own.

A quote that is no longer found has changed. The tool does not judge the new wording: it names the passages that
depend on the changed one, or that it depends on, so an editor re-reads them, brings them in line or puts them to Joel,
and then writes the new words and the state into the registry file (docs/FIXING-AN-ARTICLE.md, section 1, item 6, has
the steps for a built-on post). For a link point, the home's heading has to be a heading of its article's text, its
anchor has to be one of the anchors in the article's catalog when it has one (articles/<id>/SECTION-LINKS.json, kept by
tools/humanization/section_links.py), and each link's address has to end in that anchor.

`changed` is the notice for a push: it reads each text as it was at a git ref (`git show REF:path`) and lists the
registered quotes and headings that stood there and do not stand in the working copy, each with its partners. It
reads the registry as it was at the ref too, so a passage is listed even when its new words went into the registry in
the same change. It reads the same files as `check`, so an article whose "texts" entry names a saved copy of the live
post is compared in that copy, not in its master.

What Joel changes on Substack himself never reaches those saved copies, so a job on GitHub looks once a day
(.github/workflows/depends-watch.yml, scripts/watch_live_posts.py; Joel, 2026-11-25 16:14 UTC: "for the registry, yes
you can add the github job"). It fetches each post "texts" names, makes its sections in memory
(tools/humanization/live_sections.py) and runs `check` on them through `Texts(given=...)`; a registered passage that
is no longer in a live post goes into an issue with every place that depends on it. `list` says so on the page.

  python3 tools/humanization/depends.py check                          # every point; exit 1 if anything changed
  python3 tools/humanization/depends.py check --article inner-signal   # only the points that touch one article
  python3 tools/humanization/depends.py check --text inner-signal=work/LIVE-BODY.html
  python3 tools/humanization/depends.py changed --base origin/main [--article inner-child-therapy]
        # what this branch changed since REF that something depends on: "you changed this; these depend on it"
        # (always exit 0: it is a notice; notice_lines() returns the same lines, for a push to print)
  python3 tools/humanization/depends.py add --id H01 --what "the hat exercise" \\
        --home inner-child-therapy:"Borrowed Adulthood" --home-quote "exact words there" \\
        --use inner-signal:"No Adult Yet? Borrow One" --use-quote "exact words here" \\
        [--relation "own words"] [--state "in line"] [--note "..."] [--from "where the pair was found"]
        # refuses a quote that is not found exactly once in its article's text; with an --id the registry already
        # has, it adds the use to that point (--home and --what are not needed then)
  python3 tools/humanization/depends.py list [--article inner-signal]   # the page for Joel, on the screen
  python3 tools/humanization/depends.py list --write                    # ... written to articles/DEPENDS.md
"""
import argparse
import collections
import datetime
import html.parser
import json
import pathlib
import re
import subprocess
import sys
import urllib.parse

REPO = pathlib.Path(__file__).resolve().parents[2]
REGISTRY = 'articles/DEPENDS.json'
PAGE = 'articles/DEPENDS.md'
GIT = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
WATCH = '.github/workflows/depends-watch.yml'     # the daily job that runs scripts/watch_live_posts.py
WATCH_LABEL = 'depends-watch'                     # the label of the issues it opens
RELATIONS = ('same words', 'own words', 'pointer', 'differs')
STATES = ('in line', 'behind', 'his to settle', 'left as it is')

Text = collections.namedtuple('Text', 'text headings path')   # both in the comparison form (plain())


# ---------------------------------------------------------------- plain text

_DOUBLE = '“”„‟«»″'
_SINGLE = '‘’‚‛′`´'
_SPACES = '     '
_GONE = '​⁠﻿️­'      # zero-width characters, the emoji variation mark, the soft hyphen
_CHARS = {ord(c): '"' for c in _DOUBLE}
_CHARS.update({ord(c): "'" for c in _SINGLE})
_CHARS.update({ord(c): ' ' for c in _SPACES})
_CHARS.update({ord(c): None for c in _GONE})


def plain(words):
    """The form two texts are compared in: one kind of quote mark and apostrophe, one space for every run of
    whitespace (a non-breaking space included), and no space before a closing mark or after an opening bracket."""
    s = re.sub(r'\s+', ' ', (words or '').translate(_CHARS)).strip()
    s = re.sub(r' (?=[.,;:!?)\]}…])', '', s)
    return re.sub(r'(?<=[(\[{]) ', '', s)


_INLINE = frozenset('a abbr b bdi bdo cite code del dfn em font i ins kbd mark q s samp small span strike strong sub '
                    'sup u var wbr'.split())


class _Html(html.parser.HTMLParser):
    """The words of an HTML text, and its headings. A tag inside a line of text (a link, emphasis) leaves nothing;
    any other tag leaves a space, so two paragraphs don't run together."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.headings, self._h, self._skip = [], [], None, 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self._skip += 1
        if tag not in _INLINE:
            self.out.append(' ')
            if self._h is not None:
                self._h.append(' ')
        if re.fullmatch(r'h[1-6]', tag):
            self._h = []

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self._skip = max(0, self._skip - 1)
        if re.fullmatch(r'h[1-6]', tag) and self._h is not None:
            self.headings.append(''.join(self._h))
            self._h = None
        if tag not in _INLINE:
            self.out.append(' ')

    def handle_data(self, data):
        if self._skip:
            return
        self.out.append(data)
        if self._h is not None:
            self._h.append(data)


def _html(raw):
    p = _Html()
    p.feed(raw)
    p.close()
    return ''.join(p.out), p.headings


_ESCAPED = re.compile(r'\\([\\`*_{}\[\]()#+\-.!|>~])')
_NO_BREAK = r'((?:(?!\n[ \t]*\n).)+?)'          # words inside one paragraph


def _md_inline(s):
    s = _ESCAPED.sub(lambda m: chr(0xE000 + ord(m.group(1))), s)                   # "\*" is a star, not emphasis
    s = re.sub(r'!\[([^\]]*)\]\((?:[^()\s]|\([^()]*\))*(?:\s+"[^"]*")?\)', r'\1', s)   # a picture: its words
    s = re.sub(r'\[([^\]]*)\]\((?:[^()\s]|\([^()]*\))*(?:\s+"[^"]*")?\)', r'\1', s)    # a link: its words
    s = re.sub(r'\[([^\]]+)\]\[[^\]]*\]', r'\1', s)
    s = re.sub(r'<(https?://[^>\s]+)>', r'\1', s)
    s = re.sub(r'</?([A-Za-z][A-Za-z0-9]*)\b[^>]*>', lambda m: '' if m.group(1).lower() in _INLINE else ' ', s)
    s = re.sub(r'`+([^`\n]*)`+', r'\1', s)
    s = re.sub(r'~~' + _NO_BREAK + r'~~', r'\1', s, flags=re.S)
    for _ in range(4):                                                              # emphasis inside emphasis
        t = re.sub(r'(\*{1,3})(?=\S)' + _NO_BREAK + r'(?<=\S)\1', r'\2', s, flags=re.S)
        t = re.sub(r'(?<!\w)(_{1,3})(?=\S)' + _NO_BREAK + r'(?<=\S)\1(?!\w)', r'\2', t, flags=re.S)
        if t == s:
            break
        s = t
    return ''.join(chr(ord(c) - 0xE000) if 0xE000 <= ord(c) < 0xE080 else c for c in s)


def _md(raw):
    lines, headings = [], []
    for line in raw.replace('\r\n', '\n').split('\n'):
        m = re.match(r'^ {0,3}#{1,6}[ \t]+(.*?)[ \t]*#*[ \t]*$', line)
        if m and m.group(1):
            headings.append(_md_inline(m.group(1)))
            lines += ['', m.group(1), '']
            continue
        if re.match(r'^ {0,3}([-*_])([ \t]*\1){2,}[ \t]*$', line):      # a rule
            lines.append('')
            continue
        line = re.sub(r'^[ \t]*(?:>[ \t]?)+', '', line)                 # a quoted block's mark
        lines.append(re.sub(r'^[ \t]*[-*+][ \t]+', '', line))           # a bullet
    return _md_inline('\n'.join(lines)), headings


def _sections(raw):
    data = json.loads(raw)
    if isinstance(data, dict):
        data = data.get('sections')
    rows = [s for s in data or [] if isinstance(s, dict) and 'heading' in s]
    if not rows:
        raise ValueError('not a list of sections ({"heading", "paragraphs": [...]})')
    parts, headings = [], []
    for s in rows:
        if s.get('heading') and s.get('level', 1):       # level 0 is the stretch before the first heading
            headings.append(s['heading'])
            parts.append(s['heading'])
        paras = s.get('paragraphs') or s.get('text') or []
        parts += [paras] if isinstance(paras, str) else [p for p in paras if isinstance(p, str)]
    return '\n\n'.join(parts), headings


def parse(raw, name):
    """A Text from a file's contents; its kind is read from the name (.html, .md, .json, anything else is .txt)."""
    suffix = pathlib.PurePath(str(name)).suffix.lower()
    if suffix in ('.html', '.htm'):
        words, headings = _html(raw)
    elif suffix in ('.md', '.markdown'):
        words, headings = _md(raw)
    elif suffix == '.json':
        words, headings = _sections(raw)
    else:
        words, headings = raw, [line for line in raw.splitlines() if line.strip()]
    return Text(plain(words), [plain(h) for h in headings if plain(h)], str(name))


def count(quote, text):
    """How many times these words stand in a text (a Text's .text). The quote may carry Markdown or HTML markup."""
    forms = [plain(quote)]
    for other in (plain(_md(quote or '')[0]), plain(_html(quote or '')[0])):
        if other not in forms:
            forms.append(other)
    return max([text.count(f) for f in forms if f] or [0])


def first_words(quote, n=8):
    words = re.sub(r'\s+', ' ', quote or '').strip().split(' ')
    return ' '.join(words[:n]) + ('…' if len(words) > n else '')


# ---------------------------------------------------------------- the registry and the texts

def load(root=REPO, path=None):
    p = pathlib.Path(path) if path else pathlib.Path(root) / REGISTRY
    if not p.exists():
        return {'about': '', 'his_words': [], 'texts': {}, 'points': []}
    reg = json.loads(p.read_text(encoding='utf-8'))
    reg.setdefault('texts', {})
    reg.setdefault('points', [])
    return reg


def save(reg, root=REPO, path=None):
    p = pathlib.Path(path) if path else pathlib.Path(root) / REGISTRY
    p.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return p


def _index(root):
    try:
        index = (pathlib.Path(root) / 'articles' / 'INDEX.json').read_text(encoding='utf-8')
        return json.loads(index).get('articles', [])
    except (OSError, ValueError, AttributeError):
        return []


def text_source(reg, root, article, overrides=None):
    """(path, what named it) of the text an article's words are looked for in, or (None, why there is none)."""
    if overrides and article in overrides:
        return overrides[article], '--text'
    if article in (reg.get('texts') or {}):
        return reg['texts'][article], '"texts" in the registry'
    for a in _index(root):
        if a.get('id') == article:
            master = ((a.get('authority') or {}).get('master') or {}).get('path')
            if master:
                return master, 'its registered master'
    return None, 'no text for it: none given with --text, none in the registry\'s "texts", no registered master'


def _git_show(root, ref, path):
    p = pathlib.Path(path)
    if p.is_absolute():
        p = p.relative_to(pathlib.Path(root).resolve())
    r = subprocess.run(['git', 'show', '%s:./%s' % (ref, p.as_posix())], cwd=str(root), capture_output=True,
                       timeout=120)
    if r.returncode:
        raise OSError((r.stderr.decode('utf-8', 'replace').strip().splitlines() or ['git show failed'])[-1])
    return r.stdout.decode('utf-8')


class Texts:
    """Each article's text, read once: from the working copy, or as it was at a git ref.

    given holds texts that are already in hand, {article: Text}, and catalogs their section-link catalogs,
    {article: catalog or None}; an article in neither is read from its file as before. scripts/watch_live_posts.py
    gives each live post as it has just fetched it, so `check` looks in the post and not in the saved copy. A given
    text of None is an article that could not be had; why says so ({article: reason})."""

    def __init__(self, reg, root=REPO, overrides=None, ref=None, given=None, catalogs=None, why=None):
        self.reg, self.root, self.overrides, self.ref = reg, pathlib.Path(root), overrides or {}, ref
        self.why, self.broken = dict(why or {}), set()
        self._texts, self._catalogs = dict(given or {}), dict(catalogs or {})
        self._given, self._given_catalogs = set(self._texts), set(self._catalogs)

    def source(self, article):
        if article in self._given:
            text = self._texts[article]
            return (text.path, 'given') if text is not None else (None, self.why.get(article, 'no text for it'))
        return text_source(self.reg, self.root, article, self.overrides)

    def _raw(self, path):
        if self.ref:
            return _git_show(self.root, self.ref, path)
        return (self.root / path).read_text(encoding='utf-8')

    def get(self, article):
        """The article's Text, or None (self.why[article] then says why)."""
        if article not in self._texts:
            path, named = self.source(article)
            text = None
            if path is None:
                self.why[article] = named
            else:
                try:
                    text = parse(self._raw(path), path)
                except (OSError, ValueError, subprocess.SubprocessError) as e:
                    self.why[article] = '%s (%s) cannot be read%s: %s' % (
                        path, named, ' at ' + self.ref if self.ref else '', e)
                    self.broken.add(article)
            self._texts[article] = text
        return self._texts[article]

    def catalog(self, article):
        """The article's section-link catalog (tools/humanization/section_links.py), or None."""
        if article not in self._catalogs:
            try:
                self._catalogs[article] = json.loads(self._raw('articles/%s/SECTION-LINKS.json' % article))
            except (OSError, ValueError, subprocess.SubprocessError):
                self._catalogs[article] = None
        return self._catalogs[article]

    def catalog_name(self, article):
        """What a given catalog is called in a finding (the text it was made from), or None for the article's file."""
        text = self._texts.get(article) if article in self._given_catalogs else None
        return text.path if text is not None else None


def _catalog(texts, article):
    get = getattr(texts, 'catalog', None)
    return get(article) if get else None


def _catalog_name(texts, article):
    name = getattr(texts, 'catalog_name', None)
    return name(article) if name else None


def _why(texts, article):
    return getattr(texts, 'why', {}).get(article, 'no text for it')


def _is_link(point):
    return point.get('kind', 'passage') == 'link'


def _is_read(points, article):
    """Does a check of these points read this article's text? (The use of a link is not looked for in its article.)"""
    return any(article == p['home'].get('article')
               or (not _is_link(p) and article in [u.get('article') for u in p.get('uses', [])]) for p in points)


def _touches(point, article):
    return article in [point['home'].get('article')] + [u.get('article') for u in point.get('uses', [])]


def anchor_of(href):
    """The section a link lands on: the last part of an /i/<post>/<anchor> address, or what follows "#§"."""
    h = urllib.parse.unquote(href or '')
    if '#§' in h:
        return h.split('#§', 1)[1]
    return h.rstrip('/').rsplit('/', 1)[-1].split('#')[0].split('?')[0]


# ---------------------------------------------------------------- check and changed

def _finding(point, side, place, problem, partners, tie):
    return {'id': point.get('id', '?'), 'what': point.get('what', ''), 'kind': point.get('kind', 'passage'),
            'side': side, 'place': place, 'problem': problem, 'partners': partners, 'tie': tie}


def check(reg, texts, article=None):
    """Look for every registered quote and heading in the current texts.

    Returns (findings, unread, places): a finding is one quote or heading that is no longer where the registry says,
    with the passages to re-read; unread lists (point id, article, why) for what could not be looked for; places is
    how many quotes and headings were looked for."""
    findings, unread, places = [], [], 0
    for p in reg.get('points', []):
        if article and not _touches(p, article):
            continue
        home, uses = p['home'], p.get('uses', [])
        if _is_link(p):
            t, cat = texts.get(home['article']), _catalog(texts, home['article'])
            given = _catalog_name(texts, home['article'])        # a catalog made from the text itself, not the file
            anchors = {h.get('anchor'): h.get('text') for h in (cat or {}).get('headings', [])}
            problems = []
            if t is None:
                unread.append((p.get('id'), home['article'], _why(texts, home['article'])))
            else:
                places += 1
                if plain(home['heading']) not in t.headings:
                    problems.append('"%s" is not a heading in %s%s' % (
                        home['heading'], t.path,
                        ' (the catalog still has it, so this text may be behind the post)'
                        if home.get('anchor') in anchors and not given else ''))
            if cat is not None and home.get('anchor') not in anchors:
                problems.append('no heading in %s has the anchor "%s"'
                                % (given or 'articles/%s/SECTION-LINKS.json' % home['article'], home.get('anchor')))
            elif cat is not None and plain(anchors[home['anchor']] or '') != plain(home['heading']):
                problems.append('%s has the anchor "%s" under the heading "%s"'
                                % (given or 'the catalog', home['anchor'], anchors[home['anchor']]))
            if problems:
                findings.append(_finding(p, 'home', home, '; '.join(problems), uses, 'link to it'))
            for u in uses:
                if u.get('href') and home.get('anchor') and anchor_of(u['href']) != home['anchor']:
                    findings.append(_finding(p, 'use', u, 'its link ends in "%s", and the section\'s anchor is "%s"'
                                             % (anchor_of(u['href']), home['anchor']), [home], 'it links to'))
            continue
        for side, place in [('home', home)] + [('use', u) for u in uses]:
            t = texts.get(place['article'])
            if t is None:
                unread.append((p.get('id'), place['article'], _why(texts, place['article'])))
                continue
            places += 1
            if not count(place.get('quote'), t.text):
                findings.append(_finding(p, side, place, 'no longer found in %s' % t.path,
                                         uses if side == 'home' else [home],
                                         'depend on it' if side == 'home' else 'it depends on'))
    return findings, unread, places


def changed_between(reg, old, new, article=None, base_reg=None):
    """The registered quotes and headings that stood in the old texts and do not stand in the new ones, each with its
    partners. old and new give an article's Text with .get(article) (a dict will do). With --article, only what
    changed in that article. base_reg is the registry as it was with the old texts: a quote it had counts too, so a
    change shows even when the registry was given the new words in the same change."""
    now = {p.get('id'): p for p in reg.get('points', [])}
    findings, seen = [], set()
    for source in ([base_reg] if base_reg else []) + [reg]:
        for p in source.get('points', []):
            cur = now.get(p.get('id'), p)
            link = _is_link(p)
            for side, place in [('home', p['home'])] + ([] if link else [('use', u) for u in p.get('uses', [])]):
                if article and place.get('article') != article:
                    continue
                words = place.get('heading') if link else place.get('quote')
                key = (p.get('id'), side, place.get('article'), plain(words))
                if key in seen:
                    continue
                seen.add(key)
                a, b = old.get(place['article']), new.get(place['article'])
                if link:
                    ca, cb = _catalog(old, place['article']), _catalog(new, place['article'])
                    was = (a is not None and plain(words) in a.headings,
                           ca is not None and place.get('anchor') in [h.get('anchor') for h in ca.get('headings', [])])
                    is_ = (b is not None and plain(words) in b.headings,
                           cb is not None and place.get('anchor') in [h.get('anchor') for h in cb.get('headings', [])])
                    gone = (was[0] and b is not None and not is_[0]) or (was[1] and cb is not None and not is_[1])
                else:
                    gone = a is not None and b is not None and count(words, a.text) and not count(words, b.text)
                if not gone:
                    continue
                if side == 'home':
                    findings.append(_finding(cur, side, place, 'changed', cur.get('uses', []),
                                             'link to it' if link else 'depend on it'))
                else:
                    findings.append(_finding(cur, side, place, 'changed', [cur['home']], 'it depends on'))
    return findings


def _where(place, link):
    """One place in words: article, section, and its first words (or, for a link, where it leads)."""
    if 'heading' in place and 'quote' not in place:                    # the home of a link
        return '%s, the section "%s" (anchor %s)' % (place.get('article'), place.get('heading'), place.get('anchor'))
    if link:                                                           # a link to it
        tail = ' '.join(x for x in ('"%s"' % place['words'] if place.get('words') else '', place.get('href')) if x)
        note = ' [%s]' % place['note'] if place.get('note') else ''
        return '%s, "%s": %s%s' % (place.get('article'), place.get('section'), tail or 'link', note)
    state = '; '.join(x for x in (place.get('relation'), place.get('state'), place.get('as_of')) if x)
    return '%s, "%s": "%s"%s' % (place.get('article'), place.get('section'), first_words(place.get('quote')),
                                 ' (%s)' % state if state else '')


def finding_lines(f, since=None):
    """A finding as printed: what changed, then what to re-read. With since (a git ref) it is worded as the notice."""
    link = f['kind'] == 'link'
    out = ['you changed this since %s (point %s of %s: %s):' % (since, f['id'], REGISTRY, f['what']) if since
           else 'CHANGED  %s  %s' % (f['id'], f['what'])]
    out.append('  %s' % _where(f['place'], link and f['side'] == 'use'))
    if f['problem'] != 'changed':
        out.append('  %s' % f['problem'])
    out.append('  %s, to re-read:' % {'depend on it': 'these depend on it', 'it depends on': 'it depends on',
                                      'link to it': 'these link to it', 'it links to': 'it links to'}[f['tie']])
    out += ['    %s' % _where(x, link and f['side'] == 'home') for x in f['partners']] or ['    (none registered)']
    return out


def finding_md(f, texts):
    """A finding as Markdown lines, for an issue or a page Joel reads: the point, the place that changed, and each
    place to re-read. A section is a link to the post where its article's catalog knows the heading."""
    link, root = f['kind'] == 'link', getattr(texts, 'root', REPO)
    out = ['**%s** %s' % (f['id'], f['what']), '',
           '- Changed: %s' % _side_md(texts, f['place'], link and f['side'] == 'use', f['place'].get('article'))]
    if f['problem'] != 'changed':
        out.append('  - %s' % _linked(root, f['problem']))
    out.append('- %s, to re-read:' % {'depend on it': 'These depend on it', 'it depends on': 'It depends on this',
                                      'link to it': 'These link to it', 'it links to': 'It links to this'}[f['tie']])
    for x in f['partners']:
        state = '; '.join(v for v in (x.get('relation'), x.get('state') or _linked(root, x.get('note')),
                                      x.get('as_of')) if v)
        out.append('  - %s%s' % (_side_md(texts, x, link and f['side'] == 'home', x.get('article')),
                                 ' (%s)' % state if state else ''))
    return out + ([] if f['partners'] else ['  - (none registered)'])


def changed(reg, root=REPO, base='origin/main', article=None, registry_path=None):
    """(findings, notes): what the working copy changed since the git ref base, among the registered words."""
    root = pathlib.Path(root)
    old, new = Texts(reg, root, ref=base), Texts(reg, root)
    base_reg = None
    try:
        rel = pathlib.Path(registry_path).resolve().relative_to(root.resolve()) if registry_path else REGISTRY
        base_reg = json.loads(_git_show(root, base, rel))
    except (OSError, ValueError, subprocess.SubprocessError):
        pass
    findings = changed_between(reg, old, new, article, base_reg)
    notes = list(dict.fromkeys('%s: %s' % (a, why) for t in (old, new) for a, why in sorted(t.why.items())))
    return findings, notes


def notice_lines(article=None, base='origin/main', root=REPO):
    """The lines a push prints: every registered passage or section heading this branch changed since base, with what
    depends on it ("you changed this; these depend on it"). No lines when nothing registered changed, or when the
    registry or the ref can't be read: it is a notice and never stops a push."""
    try:
        findings, _ = changed(load(root), root, base, article)
    except Exception:                                    # noqa: BLE001 - a notice must not break the push
        return []
    return [line for f in findings for line in finding_lines(f, since=base)]


# ---------------------------------------------------------------- add

def _split(arg, name):
    article, sep, section = (arg or '').partition(':')
    if not (article.strip() and sep and section.strip()):
        raise ValueError('%s takes ARTICLE:SECTION, e.g. inner-signal:"The Guide"' % name)
    return article.strip(), section.strip()


def _once(texts, article, quote, name):
    t = texts.get(article)
    if t is None:
        raise ValueError('%s: %s: %s' % (name, article, _why(texts, article)))
    n = count(quote, t.text)
    if n == 0:
        raise ValueError('%s: these words are not in %s (%s): "%s"' % (name, article, t.path, first_words(quote, 12)))
    if n > 1:
        raise ValueError('%s: these words stand %d times in %s (%s); give more of them, so they name one place: "%s"'
                         % (name, n, article, t.path, first_words(quote, 12)))


def add(reg, texts, pid, use, use_quote, home=None, home_quote=None, what=None, relation=None, state='in line',
        note='', found='', as_of=None):
    """Add a point, or a use to the point that already has this id, once each new quote is found exactly once in its
    article's text. Returns the point; raises ValueError with the reason when it refuses."""
    point = next((p for p in reg.setdefault('points', []) if p.get('id') == pid), None)
    use_article, use_section = _split(use, '--use')
    if point is not None and _is_link(point):
        raise ValueError('%s is a link point; add its links in the registry file' % pid)
    if point is None:
        if not (what and home and home_quote):
            raise ValueError('a new point needs --what, --home and --home-quote')
        home_article, home_section = _split(home, '--home')
        _once(texts, home_article, home_quote, '--home-quote')
        new_home = {'article': home_article, 'section': home_section, 'quote': home_quote}
    else:
        new_home = point['home']
        if home or home_quote:
            given = _split(home, '--home')[0] if home else new_home['article']
            if given != new_home['article'] or (home_quote and plain(home_quote) != plain(new_home['quote'])):
                raise ValueError('%s already has another home: %s' % (pid, _where(new_home, False)))
    if relation and relation not in RELATIONS:
        raise ValueError('--relation is one of: %s' % ', '.join(RELATIONS))
    if state not in STATES:
        raise ValueError('--state is one of: %s' % ', '.join(STATES))
    _once(texts, use_article, use_quote, '--use-quote')
    h, u = plain(new_home['quote']), plain(use_quote)
    if use_article == new_home['article'] and (h in u or u in h):
        raise ValueError('--use-quote and the home quote are the same place in %s; a use is another passage'
                         % use_article)
    if point is not None and any(x.get('article') == use_article and plain(x.get('quote')) == u
                                 for x in point.get('uses', [])):
        raise ValueError('%s already has this use' % pid)
    entry = {'article': use_article, 'section': use_section, 'quote': use_quote,
             'relation': relation or ('same words' if h == u else 'own words'), 'state': state,
             'as_of': as_of or datetime.datetime.now(datetime.timezone.utc).date().isoformat(), 'note': note or ''}
    if point is None:
        point = {'id': pid, 'what': what, 'kind': 'passage', 'home': new_home, 'uses': [], 'from': found or ''}
        reg['points'].append(point)
    point.setdefault('uses', []).append(entry)
    return point


# ---------------------------------------------------------------- the page for Joel

def _n(n, word):
    return '%d %s%s' % (n, word, '' if n == 1 else 's')


def _cell(s):
    return re.sub(r'\s+', ' ', str(s or '')).replace('|', '\\|').strip() or '—'


_PATH = re.compile(r'(?<![\w/\[.-])(?<!\]\()((?:[\w@+-][\w.@+-]*/)+[\w@+-][\w.@+-]*'
                   r'\.(?:md|json|jsonl|py|txt|html|js))(?![\w/-])')


def _linked(root, s):
    """A note for the page: each file of the repository it names becomes a link Joel can click, not a path."""
    return _PATH.sub(lambda m: '[%s](%s%s)' % (m.group(1), GIT, m.group(1))
                     if (pathlib.Path(root) / m.group(1)).exists() else m.group(1), s or '')


def _section_md(texts, article, section):
    """A section's name, linked to its anchor on the live post when the article has a catalog that knows it."""
    cat = _catalog(texts, article) or {}
    post = cat.get('post') or {}
    for h in cat.get('headings', []):
        if plain(h.get('text')) == plain(section) and post.get('base') and post.get('id') and h.get('anchor'):
            return '[%s](%s/i/%s/%s)' % (section, post['base'].rstrip('/'), post['id'], h['anchor'])
    return '“%s”' % section


def _side_md(texts, place, link, with_article=None):
    """One side of a pair for the page: the section and its first words (or the link)."""
    if 'heading' in place and 'quote' not in place:
        s = '%s (the section)' % _section_md(texts, place['article'], place['heading'])
    elif link:
        words = place.get('words') or 'the link'
        s = '%s: %s' % (_section_md(texts, place['article'], place.get('section', '')),
                        '[%s](%s)' % (words, place['href']) if place.get('href') else words)
    else:
        s = '%s: “%s”' % (_section_md(texts, place['article'], place.get('section', '')),
                          first_words(place.get('quote')))
    return ('%s, %s' % (with_article, s)) if with_article else s


def watch_is_daily(root=REPO):
    """Whether the job's file has a schedule that is not commented out (it was switched off on 2026-11-25, when
    Substack refused GitHub's servers)."""
    f = pathlib.Path(root) / WATCH
    return f.exists() and re.search(r'^\s*schedule:\s*$', f.read_text(encoding='utf-8'), flags=re.M) is not None


def watch_note(reg, root=REPO):
    """The page's paragraph on the daily job (Joel, 2026-11-25 16:14 UTC: "for the registry, yes you can add the
    github job"). The page carries it only where the job's file is in the repository, and says "every day" only while
    the job has a schedule."""
    n = len(reg.get('texts') or {})
    where = (reg.get('watch') or {})
    if where.get('runs') == 'laptop':
        return ('**Checked every day, from Joel\'s laptop.** Once a day, at about %s, a timer on his laptop runs the '
                'check ([the script](%s%s), installed by %s since %s) on %s: it looks for every passage on this page and, '
                'when one has changed, for instance because he edited a post on Substack himself, it opens [an issue '
                'on GitHub](%s/issues?q=label%%3A%s) that names the passage and every other place that depends on it, so '
                'those can be read again, and shows a notice on his screen. A day the laptop is off, it runs at the next '
                'start. It runs there because Substack refuses GitHub\'s servers ([the job on GitHub](%s%s) runs only '
                'by hand).'
                % (where.get('at', '08:23'), GIT, where.get('script', 'scripts/laptop/depends-watch-run.sh'),
                   where.get('install', 'scripts/laptop/install-depends-watch.sh'), where.get('since', '?'),
                   'the %s' % _n(n, 'live post') if n else 'the live posts', GIT.split('/blob/')[0], WATCH_LABEL,
                   GIT, WATCH))
    if not watch_is_daily(root):
        return ('**Not checked by itself yet.** A job on GitHub ([the check](%s%s)) can read %s on Substack and look '
                'for every passage on this page, and open [an issue on GitHub](%s/issues?q=label%%3A%s) that names a '
                'changed passage and every other place that depends on it. But Substack refuses GitHub\'s servers '
                '(tried on 2026-11-25), so the job does not run by itself. The same check runs from a computer '
                'Substack answers: `python3 scripts/watch_live_posts.py`. Until it has such a place to run every '
                'day, a lane runs it before it edits a post.'
                % (GIT, WATCH, 'the %s' % _n(n, 'live post') if n else 'the live posts', GIT.split('/blob/')[0],
                   WATCH_LABEL))
    return ('**Checked every day.** Once a day a job on GitHub ([the daily check](%s%s)) reads %s on Substack and '
            'looks for every passage on this page. When one has changed, for instance because you edited a post on '
            'Substack yourself, it opens [an issue on GitHub](%s/issues?q=label%%3A%s) (a note in this repository\'s '
            'Issues list) that names the passage and every other place that depends on it, so those can be read '
            'again. While the same change stands it does not write again. If it cannot read a post, it says so in '
            'an issue of its own.'
            % (GIT, WATCH, 'the %s' % _n(n, 'live post') if n else 'the live posts', GIT.split('/blob/')[0],
               WATCH_LABEL))


def page(reg, article=None, root=REPO):
    """The Markdown page for Joel: for each article, what other posts take from it and what it takes from others."""
    texts = Texts(reg, root)
    titles = {a.get('id'): a.get('title') for a in _index(root)}
    points = reg.get('points', [])

    def name(a):
        return '%s (%s)' % (titles[a], a) if titles.get(a) else a

    def note(u):
        return _linked(root, u.get('state') or u.get('note'))

    pairs = [(p, u) for p in points for u in p.get('uses', [])]
    states = collections.Counter(u.get('state') or 'no state' for p, u in pairs if not _is_link(p))
    n_links = sum(1 for p in points if _is_link(p))
    out = ['# Shared passages: what depends on what', '',
           'Made by [tools/humanization/depends.py](%stools/humanization/depends.py) (`depends.py list --write`) from '
           'the registry [%s](%s%s). To change this page, change the registry and make the page again.'
           % (GIT, REGISTRY, GIT, REGISTRY), '']
    for w in reg.get('his_words', []):
        out += ['Joel, %s: "%s"' % (w.get('when', ''), w.get('words', '')), '']
    tally = ', '.join('%d %s' % (states[s], s) for s in list(STATES) + ['no state'] if states.get(s))
    out += ['Each row is one pair: a passage where a point has its home, and a passage in another place that takes '
            'from it. When the words on either side change, `depends.py check` names the other side to re-read. In '
            'each table "Here" is the side in the post named above the table and "There" is the other side, with its '
            'post\'s short name (the one in brackets in the headings).', '',
            '- **Relation.** *same words*: the passage repeats the home\'s words. *own words*: it says the same in '
            'other words. *pointer*: it sends the reader to the home. *differs*: it says something else. *link*: a '
            'link to that section.',
            '- **State.** *in line*: nothing to do. *behind*: the home says something this passage has not taken in '
            'yet. *his to settle*: the two differ and only Joel can say which stands. *left as it is*: the passage '
            'stays, with at most a link to the home. For a link, the note on where the link stands.', '',
            '%s: %s%s, and %s.' % (_n(len(points), 'point'), _n(sum(states.values()), 'passage pair'),
                                   ' (%s)' % tally if tally else '', _n(n_links, 'section link')), '']
    if (pathlib.Path(root) / WATCH).exists():
        out += [watch_note(reg, root), '']
    order = []
    for p, u in pairs:
        for a in (p['home']['article'], u['article']):
            if a not in order:
                order.append(a)
    head = '| Point | Here | There | Relation | State | Date |\n|---|---|---|---|---|---|'

    def row(p, u, here_is_home, other):
        link = _is_link(p)
        here, there = (p['home'], u) if here_is_home else (u, p['home'])
        return '| %s | %s | %s | %s | %s | %s |' % (
            _cell('**%s** %s' % (p.get('id'), p.get('what', ''))),
            _cell(_side_md(texts, here, link and not here_is_home)),
            _cell(_side_md(texts, there, link and here_is_home, other)),
            'link' if link else _cell(u.get('relation')), _cell(note(u)), _cell(u.get('as_of')))

    for a in ([article] if article else order):
        gives = [(p, u) for p, u in pairs if p['home']['article'] == a and u['article'] != a]
        takes = [(p, u) for p, u in pairs if u['article'] == a and p['home']['article'] != a]
        inside = [(p, u) for p, u in pairs if u['article'] == a and p['home']['article'] == a]
        out += ['## %s' % name(a), '']
        if not (gives or takes or inside):
            out += ['Nothing registered for it yet.', '']
        if gives:
            out += ['### What other posts take from this one (%d)' % len(gives), '', head]
            out += [row(p, u, True, u['article']) for p, u in gives] + ['']
        if takes:
            out += ['### What this one takes from others (%d)' % len(takes), '', head]
            out += [row(p, u, False, p['home']['article']) for p, u in takes] + ['']
        if inside:
            out += ['### Inside this post (%d)' % len(inside), '',
                    'Here is the passage that takes; There is the home, in the same post.', '', head]
            out += [row(p, u, False, None) for p, u in inside] + ['']
    return '\n'.join(out).rstrip('\n') + '\n'


# ---------------------------------------------------------------- the commands

def _overrides(pairs):
    out = {}
    for item in pairs or []:
        article, sep, path = item.partition('=')
        if not (article and sep and path):
            raise SystemExit('--text takes ARTICLE=PATH, e.g. --text inner-signal=work/LIVE-BODY.html')
        out[article] = path
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--root', default=str(REPO), help='the repository (default: this one)')
    ap.add_argument('--registry', help='the registry file (default: %s under the root)' % REGISTRY)
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('check', help='look for every registered quote and heading; exit 1 if one changed')
    c.add_argument('--article')
    c.add_argument('--text', action='append', metavar='ARTICLE=PATH')
    d = sub.add_parser('changed', help='what changed since a git ref that something depends on (a notice, exit 0)')
    d.add_argument('--base', required=True, metavar='REF')
    d.add_argument('--article')
    a = sub.add_parser('add', help='add a point, or a use to a point, after finding each quote exactly once')
    a.add_argument('--id', required=True)
    a.add_argument('--what')
    a.add_argument('--home', metavar='ARTICLE:SECTION')
    a.add_argument('--home-quote')
    a.add_argument('--use', required=True, metavar='ARTICLE:SECTION')
    a.add_argument('--use-quote', required=True)
    a.add_argument('--relation', choices=RELATIONS)
    a.add_argument('--state', choices=STATES, default='in line')
    a.add_argument('--note', default='')
    a.add_argument('--from', dest='found', default='')
    a.add_argument('--text', action='append', metavar='ARTICLE=PATH')
    ls = sub.add_parser('list', help='the page for Joel: what each article gives and takes')
    ls.add_argument('--article')
    ls.add_argument('--write', action='store_true', help='write %s' % PAGE)
    args = ap.parse_args(argv)
    root = pathlib.Path(args.root)
    reg = load(root, args.registry)

    if args.cmd == 'check':
        texts = Texts(reg, root, _overrides(args.text))
        findings, unread, places = check(reg, texts, args.article)
        points = [p for p in reg['points'] if not args.article or _touches(p, args.article)]
        for art in dict.fromkeys(x.get('article') for p in points for x in [p['home']] + p.get('uses', [])):
            path, named = texts.source(art)
            if _is_read(points, art):
                print('%s is read in %s (%s)' % (art, path, named) if path else '%s: %s' % (art, named))
        for f in findings:
            print('\n'.join(finding_lines(f)))
        for why in sorted({'%s: %s' % (art, why) for _, art, why in unread}):
            print('NOT READ  %s' % why)
        links = sum(1 for p in points if _is_link(p))
        print('%s (%s, %s), %s read: %d changed, %d not read'
              % (_n(len(points), 'point'), _n(len(points) - links, 'passage'), _n(links, 'link'), _n(places, 'place'),
                 len(findings), len(unread)))
        return 1 if findings or texts.broken else 0

    if args.cmd == 'changed':
        findings, notes = changed(reg, root, args.base, args.article, args.registry)
        for f in findings:
            print('\n'.join(finding_lines(f, since=args.base)))
        for n in notes:
            print('not compared  %s' % n)
        print('%d registered %s changed since %s' % (len(findings), 'passage or heading' if len(findings) == 1
                                                     else 'passages or headings', args.base))
        return 0

    if args.cmd == 'add':
        try:
            point = add(reg, Texts(reg, root, _overrides(args.text)), args.id, args.use, args.use_quote, args.home,
                        args.home_quote, args.what, args.relation, args.state, args.note, args.found)
        except ValueError as e:
            print('not added: %s' % e, file=sys.stderr)
            return 1
        path = save(reg, root, args.registry)
        print('%s: %s; %s; written to %s' % (point['id'], point['what'], _n(len(point['uses']), 'use'), path))
        return 0

    text = page(reg, args.article, root)
    if args.write:
        if args.article:
            print('--write makes the whole page; leave --article out', file=sys.stderr)
            return 1
        (root / PAGE).write_text(text, encoding='utf-8')
        print('written: %s (%s)' % (root / PAGE, _n(len(reg['points']), 'point')))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
