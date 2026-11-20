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

  python3 tools/humanization/section_links.py slug "Therapy or Escapism?"
  python3 tools/humanization/section_links.py url https://ibogaqueen.substack.com 189761959 "Therapy or Escapism?"
  python3 tools/humanization/section_links.py check ARTICLE.md      # each heading's slug; exit 1 if one is UNCHECKED or repeated
"""
import argparse
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from section_refs import plain  # noqa: E402

CHECKED_DROPPED = set('?:,.+"“”')
HEAD = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')


def _kept(ch):
    return ('a' <= ch <= 'z') or ('0' <= ch <= '9') or ch in ' -'


def _emoji(ch):
    return unicodedata.category(ch) in ('So', 'Sk') or 0xFE00 <= ord(ch) <= 0xFE0F or ord(ch) == 0x200D


def slug(heading):
    """The anchor Substack gives a heading with these words."""
    s = re.sub(r'\s+', ' ', heading).lower()
    s = ''.join(ch for ch in s if _kept(ch))
    s = re.sub(r' ', '-', s)
    return re.sub(r'-+', '-', s).strip('-')


def unchecked(heading):
    """The characters in a heading whose handling hasn't been seen on a rendered page yet."""
    out = []
    for ch in re.sub(r'\s+', ' ', heading).lower():
        if _kept(ch) or ch in CHECKED_DROPPED or _emoji(ch):
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('slug'); a.add_argument('heading')
    b = sub.add_parser('url'); b.add_argument('base'); b.add_argument('post_id'); b.add_argument('heading')
    c = sub.add_parser('check'); c.add_argument('article')
    args = ap.parse_args(argv)
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
