#!/usr/bin/env python3
"""carried_links.py - the links inside sentences brought from one of his posts into another.

Joel, 2026-11-25 16:00 UTC, on a card that brought two sentences of his inner child guide into the Self-Hypnosis guide:
"i had warmlines linked in the inner child guide tho make sure it's still linked right? always carry the links"
(lesson toc-2026-11-25f). The texts this repository keeps of his live posts are words only, so a sentence copied from
them arrives without its links. This reads the source post's HTML and says which words of each carried sentence are
linked there, and to where, so the link goes in with the sentence.

  python3 tools/humanization/carried_links.py SOURCE.html "sentence one" "sentence two" ...
  python3 tools/humanization/carried_links.py SOURCE.html --json CARRIED.json     # {"id": "text", ...}

SOURCE.html is the post's body_html (https://<publication>/api/v1/posts/by-id/<id>). A sentence is found by its words
(quotes and dashes of either kind, and runs of spaces, are the same); one that isn't found whole is looked for by its
longest run of words that is, and the result says how much of it was found, because a carried sentence is often his
sentence with a word or two changed. Exit 1 if a sentence could not be found at all: check that one by eye.
"""
import argparse
import html.parser
import json
import re
import sys

BLOCKS = {'p', 'li', 'blockquote', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'td', 'figcaption'}
_SAME = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '–': '-', '—': '-', '\xa0': ' '})


def norm(s):
    return re.sub(r'\s+', ' ', s.translate(_SAME)).strip()


class _Blocks(html.parser.HTMLParser):
    """Each text block of the post as (text, [(start, end, href), ...])."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.depth, self.text, self.links, self.href, self.start = [], 0, '', [], None, 0

    def handle_starttag(self, tag, attrs):
        if tag in BLOCKS:
            if self.depth == 0:
                self.text, self.links = '', []
            self.depth += 1
        elif tag == 'a' and self.depth:
            self.href, self.start = dict(attrs).get('href'), len(self.text)
        elif tag == 'br' and self.depth:
            self.text += ' '

    def handle_endtag(self, tag):
        if tag == 'a' and self.depth and self.href is not None:
            if len(self.text) > self.start:
                self.links.append((self.start, len(self.text), self.href))
            self.href = None
        elif tag in BLOCKS and self.depth:
            self.depth -= 1
            if self.depth == 0 and self.text.strip():
                self.out.append((self.text, self.links))

    def handle_data(self, data):
        if self.depth:
            self.text += data


def blocks(source_html):
    p = _Blocks()
    p.feed(source_html)
    return p.out


def _normalized(text, links):
    """The block's text as norm() gives it, with each link's span moved to match."""
    t = text.translate(_SAME)
    out, where = [], []
    for i, ch in enumerate(t):
        if ch.isspace():
            if out and out[-1] == ' ':
                continue
            ch = ' '
        out.append(ch)
        where.append(i)
    s = ''.join(out)
    lead = len(s) - len(s.lstrip())
    s = s.strip()
    where = where[lead:lead + len(s)]
    spans = []
    for a, b, href in links:
        ks = [k for k, i in enumerate(where) if a <= i < b]
        if ks:
            spans.append((ks[0], ks[-1] + 1, href))
    return s, spans


def find(source_html, sentence, min_words=5):
    """{'found': share of the sentence's words found, 'links': [{'words', 'href'}], 'in': the start of its block}."""
    want = norm(sentence)
    words = want.split(' ')
    best = None
    for text, links in blocks(source_html):
        s, spans = _normalized(text, links)
        if want in s:
            at, n = s.index(want), len(want)
            best = (1.0, s, spans, at, at + n)
            break
        # the longest run of the sentence's words that this block has
        for size in range(len(words) - 1, min_words - 1, -1):
            if best and best[0] >= size / len(words):
                break
            for k in range(len(words) - size + 1):
                run = ' '.join(words[k:k + size])
                if run in s:
                    at = s.index(run)
                    best = (size / len(words), s, spans, at, at + len(run))
                    break
            else:
                continue
            break
    if not best:
        return {'found': 0.0, 'links': [], 'in': None}
    share, s, spans, a, b = best
    inside = [{'words': s[max(x, a):min(y, b)], 'href': href, 'whole': x >= a and y <= b}
              for x, y, href in spans if x < b and y > a]
    return {'found': round(share, 2), 'links': inside, 'in': s[:60]}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('source')
    ap.add_argument('sentences', nargs='*')
    ap.add_argument('--json', help='a file of {"id": "carried text", ...}')
    a = ap.parse_args(argv)
    src = open(a.source, encoding='utf-8').read()
    items = dict(json.load(open(a.json, encoding='utf-8'))) if a.json else {}
    items.update({'#%d' % (k + 1): s for k, s in enumerate(a.sentences)})
    missing = 0
    for key, text in items.items():
        # a carried text of several sentences: each sentence by itself, so a changed word in one doesn't hide the rest
        for sent in [x for x in re.split(r'(?<=[.!?])\s+', norm(text)) if len(x.split()) >= 3]:
            r = find(src, sent)
            if not r['found']:
                missing += 1
                print('%s: NOT FOUND in the source: "%s"' % (key, sent[:80]))
            for ln in r['links']:
                print('%s: "%s" is linked to %s%s' % (key, ln['words'], ln['href'],
                                                      '' if r['found'] == 1.0 else ' (sentence found in part: %d%%)' % (r['found'] * 100)))
    if not missing:
        print('%d carried texts read; every sentence found in the source' % len(items))
    return 1 if missing else 0


if __name__ == '__main__':
    sys.exit(main())
