#!/usr/bin/env python3
"""section_links.py - the link a section mention carries in a Substack post, and each heading's anchor.

Lesson inner-child-2026-11-20c. Joel, 2026-11-20 16:39 UTC: "also curious why you never made links so that whenever i
reference a section it would link to it. that's easy to do in substack so make that part of joel-articles, sections
mentioned are always linked to." Turn 132 linked 22 mentions in his inner child post; every anchor was opened on the
rendered page. A section's link is https://<publication>.substack.com/i/<post id>/<slug>.

The slug, as Substack makes it from the heading's words (37 anchors from two of his posts agree: 22 in the inner child
guide, 15 in the bad trips guide): lower case; every character that is not a letter a to z, a digit, a space or a hyphen
is dropped, so "Alone at 3 a.m." gives alone-at-3-am, "Therapy or Escapism?" therapy-or-escapism, and an emoji nothing;
spaces become hyphens, a run of hyphens becomes one, and none is left at either end.

Checked on a rendered page so far: ? : , . + straight and curly double quotes, emoji, hyphens and digits. Not checked yet:
apostrophes, accented letters, "&", brackets, "!" and two headings with the same words. A heading with any of those is
marked UNCHECKED: open the post, read that heading's anchor (its link in the contents sidebar), and add it to
tests/test_section_links.py when it is known.

Finding the mentions is tools/humanization/section_refs.py's job (every place a paragraph names a section). A mention
left unlinked on purpose is recorded with its reason in the article's CURRENT-STATE.md, so the next pass doesn't link it.

The catalog (lesson inner-child-2026-11-20g; Joel, 2026-11-20 21:49 UTC: "every time a heading changes, we have to fix the
anchor links. make sure that's part of the protocol in joel-articles. so the anchor links should all be catalogued so this
is automatic and easy"). Each post with section links keeps SECTION-LINKS.json beside its article: the post, every heading
with its anchor, every section link (where it sits, its words, the section it points to, its href), and the mentions left
unlinked on purpose with the reason. A heading changes only through `rename`, which gives the heading its new anchor and
lists every link to change in the post (old href, new href), and `links` says whether every catalogued link still lands
on a heading. `build` makes a catalog from the post's HTML (its body as Substack's API or editor gives it).

  python3 tools/humanization/section_links.py slug "Therapy or Escapism?"
  python3 tools/humanization/section_links.py url https://ibogaqueen.substack.com 189761959 "Therapy or Escapism?"
  python3 tools/humanization/section_links.py check ARTICLE.md      # each heading's slug; exit 1 if one is UNCHECKED or repeated
  python3 tools/humanization/section_links.py links CATALOG          # exit 1 if a link no longer lands on a heading
  python3 tools/humanization/section_links.py rename CATALOG S095 "Prepare for Altered States Now" [--write]
  python3 tools/humanization/section_links.py build --html BODY.html --base URL --post ID [--source TEXT] > CATALOG
"""
import argparse
import html.parser
import json
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from section_refs import plain  # noqa: E402

CHECKED_DROPPED = set('?:,.+"“”!’')
# Read 2026-11-21 from all 149 anchored headings of the inner child guide as rendered
# (articles/inner-child-therapy/experiments/t140-moves/live_anchors.txt): "&" reads "and", an accented letter keeps
# its plain letter ("Céline" -> "celine"), and "!" and "’" go like the other punctuation.
HEAD = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')


def _kept(ch):
    return ('a' <= ch <= 'z') or ('0' <= ch <= '9') or ch in ' -'


def _emoji(ch):
    return unicodedata.category(ch) in ('So', 'Sk') or 0xFE00 <= ord(ch) <= 0xFE0F or ord(ch) == 0x200D


def _plain_letter(ch):
    """An accented letter's plain letter ("é" -> "e"), or None."""
    base = ''.join(c for c in unicodedata.normalize('NFKD', ch) if not unicodedata.combining(c))
    return base if base != ch and len(base) == 1 and _kept(base) else None


def slug(heading):
    """The anchor Substack gives a heading with these words."""
    s = re.sub(r'\s+', ' ', heading).lower().replace('&', ' and ')
    s = ''.join(_plain_letter(ch) or ch for ch in s)
    s = ''.join(ch for ch in s if _kept(ch))
    s = re.sub(r' ', '-', s)
    return re.sub(r'-+', '-', s).strip('-')


def unchecked(heading):
    """The characters in a heading whose handling hasn't been seen on a rendered page yet."""
    out = []
    for ch in re.sub(r'\s+', ' ', heading).lower():
        if _kept(ch) or ch in CHECKED_DROPPED or _emoji(ch) or ch == '&' or _plain_letter(ch):
            continue
        if ch not in out:
            out.append(ch)
    return out


def url(base, post_id, heading):
    return '%s/i/%s/%s' % (base.rstrip('/'), post_id, slug(heading))


def check(md):
    """[(level, heading, slug, problems)] for every heading of a Markdown article."""
    rows, seen = [], {}
    for line in md.splitlines():
        m = HEAD.match(line)
        if not m:
            continue
        text = plain(m.group(2))
        s = slug(text)
        probs = []
        odd = unchecked(text)
        if odd:
            probs.append('UNCHECKED characters: ' + ' '.join(odd))
        if not s:
            probs.append('no slug')
        if s in seen:
            probs.append('same slug as "%s" (UNCHECKED: how Substack tells them apart)' % seen[s])
        seen.setdefault(s, text)
        rows.append((len(m.group(1)), text, s, probs))
    return rows


def anchor_of(href):
    return href.rstrip('/').rsplit('/', 1)[-1].split('#')[0].split('?')[0]


def _heading(cat, key):
    """A catalog heading by its id, or by its words."""
    for h in cat['headings']:
        if key in (h.get('id'), h['text']):
            return h
    raise SystemExit('no heading %r in the catalog' % key)


def links_check(cat):
    """[(link, problem)] for every catalogued link that no longer lands where it should."""
    anchors = {h['anchor']: h for h in cat['headings']}
    by_id = {h['id']: h for h in cat['headings'] if h.get('id')}
    out = []
    for ln in cat['links']:
        a = anchor_of(ln['href'])
        tgt = by_id.get(ln.get('target'))
        if tgt is not None and tgt['anchor'] != a:
            out.append((ln, 'points to #%s, but "%s" is now #%s' % (a, tgt['text'], tgt['anchor'])))
        elif a not in anchors:
            out.append((ln, 'no heading has the anchor #%s' % a))
    return out


def rename(cat, key, new_text):
    """Give a heading new words and its new anchor; return [(link, old_href, new_href)] for every link to change."""
    h = _heading(cat, key)
    old = h['anchor']
    h['text'], h['anchor'] = new_text, slug(new_text)
    changes = []
    for ln in cat['links']:
        if ln.get('target') and h.get('id'):
            points_here = ln['target'] == h['id']
        else:
            points_here = anchor_of(ln['href']) == old
        if not points_here:
            continue
        new_href = url(cat['post']['base'], cat['post']['id'], new_text)
        if new_href != ln['href']:
            changes.append((ln, ln['href'], new_href))
            ln['href'] = new_href
    return changes


class _PostHTML(html.parser.HTMLParser):
    def __init__(self, post_id):
        super().__init__(convert_charrefs=True)
        self.needle, self.headings, self.links = '/i/%s/' % post_id, [], []
        self._h = self._a = None
        self._text = ''

    def handle_starttag(self, tag, attrs):
        if re.fullmatch(r'h[1-4]', tag):
            self._h, self._text = int(tag[1]), ''
        elif tag == 'a' and self.needle in (dict(attrs).get('href') or ''):
            self._a, self._atext = dict(attrs)['href'], ''

    def handle_endtag(self, tag):
        if self._h and tag == 'h%d' % self._h:
            text = re.sub(r'\s+', ' ', self._text).strip()
            if text:
                self.headings.append({'level': self._h, 'text': text, 'anchor': slug(text)})
            self._h = None
        elif tag == 'a' and self._a:
            where = self.headings[-1]['text'] if self.headings else ''
            self.links.append({'in': where, 'text': re.sub(r'\s+', ' ', self._atext).strip(), 'href': self._a})
            self._a = None

    def handle_data(self, data):
        if self._h:
            self._text += data
        if self._a:
            self._atext += data


def build(html_text, base, post_id, source=''):
    p = _PostHTML(post_id)
    p.feed(html_text)
    return {'post': {'base': base.rstrip('/'), 'id': str(post_id)}, 'source': source, 'headings': p.headings,
            'links': p.links, 'unlinked_on_purpose': []}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('slug'); a.add_argument('heading')
    b = sub.add_parser('url'); b.add_argument('base'); b.add_argument('post_id'); b.add_argument('heading')
    c = sub.add_parser('check'); c.add_argument('article')
    d = sub.add_parser('links'); d.add_argument('catalog')
    e = sub.add_parser('rename'); e.add_argument('catalog'); e.add_argument('key'); e.add_argument('new_heading')
    e.add_argument('--write', action='store_true')
    f = sub.add_parser('build'); f.add_argument('--html', required=True); f.add_argument('--base', required=True)
    f.add_argument('--post', required=True); f.add_argument('--source', default='')
    args = ap.parse_args(argv)
    if args.cmd == 'links':
        cat = json.loads(pathlib.Path(args.catalog).read_text(encoding='utf-8'))
        probs = links_check(cat)
        for ln, why in probs:
            print('%s: "%s" -> %s' % (ln.get('in', ''), ln['text'], why))
        print('%d of %d links to fix' % (len(probs), len(cat['links'])) if probs else 'all %d links land on a heading' % len(cat['links']))
        return 1 if probs else 0
    if args.cmd == 'rename':
        path = pathlib.Path(args.catalog)
        cat = json.loads(path.read_text(encoding='utf-8'))
        changes = rename(cat, args.key, args.new_heading)
        for ln, old, new in changes:
            print('in %s, "%s": %s -> %s' % (ln.get('in', ''), ln['text'], old, new))
        odd = unchecked(args.new_heading)
        print('%d link(s) to change in the post%s' % (len(changes), ('; UNCHECKED characters in the new heading: ' + ' '.join(odd)) if odd else ''))
        if args.write:
            path.write_text(json.dumps(cat, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        return 0
    if args.cmd == 'build':
        cat = build(pathlib.Path(args.html).read_text(encoding='utf-8'), args.base, args.post, args.source)
        print(json.dumps(cat, ensure_ascii=False, indent=1))
        return 0
    if args.cmd in ('slug', 'url'):
        out = slug(args.heading) if args.cmd == 'slug' else url(args.base, args.post_id, args.heading)
        odd = unchecked(args.heading)
        print(out + ('    UNCHECKED characters: ' + ' '.join(odd) if odd else ''))
        return 1 if odd else 0
    bad = 0
    for level, text, s, probs in check(pathlib.Path(args.article).read_text(encoding='utf-8')):
        print('%s %s -> %s%s' % ('#' * level, text, s, ('    ' + '; '.join(probs)) if probs else ''))
        bad += bool(probs)
    print('%d heading(s) to check on the rendered page' % bad if bad else 'every heading uses checked characters only')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
