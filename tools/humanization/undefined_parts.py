#!/usr/bin/env python3
"""List the parts and roles a guide doesn't define in its own words: ask its author about these before any sort.

A heading with sections under it and little or no text of its own leaves its job to be guessed, and a model asked what
it is for reads the answer off what sits under it now, which carries the old order into any reorganization (lesson
inner-child-2026-11-20r). On 4 November the inner child guide's Nurturer had no text of its own. The frame written for
the contents sorts said its work included "borrowing love from other people or from a spiritual source" and "widening
the sense of what happiness is possible", which were the headings under it, and no sort moved the spiritual sections to
the Guide, where Joel had put them.

Code counts the words; whether a short text says what its part is for is a reader's call, so its first words are shown.

  python3 tools/humanization/undefined_parts.py GUIDE.md [--min-words 40]
  python3 tools/humanization/undefined_parts.py master.html
"""
import argparse
import html.parser
import re
import sys

MD_HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*#*\s*$')
FENCE = re.compile(r'^\s*(```|~~~)')
HTML_HEADING = re.compile(r'h[1-6]')
BLOCK_END = {'p', 'li', 'div', 'blockquote', 'figure', 'figcaption', 'pre', 'table', 'tr'}


def from_markdown(text):
    """[{'level', 'heading', 'own'}] in order; 'own' is the text between a heading and the next heading of any level."""
    out, fenced = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            fenced = not fenced
        m = None if fenced else MD_HEADING.match(line)
        if m:
            out.append({'level': len(m.group(1)), 'heading': m.group(2), 'own': ''})
        elif out:
            out[-1]['own'] += line + '\n'
    return out


class _HTML(html.parser.HTMLParser):
    SKIP = {'script', 'style'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.in_heading, self.skip = [], False, 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif HTML_HEADING.fullmatch(tag):
            self.in_heading = True
            self.out.append({'level': int(tag[1]), 'heading': '', 'own': ''})
        elif tag == 'br' and self.out:
            self.out[-1]['own'] += '\n'

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        elif HTML_HEADING.fullmatch(tag):
            self.in_heading = False
        elif tag in BLOCK_END and self.out:
            self.out[-1]['own'] += '\n'

    def handle_data(self, data):
        if self.skip or not self.out:
            return
        self.out[-1]['heading' if self.in_heading else 'own'] += data


def from_html(text):
    p = _HTML()
    p.feed(text)
    p.close()
    for s in p.out:
        s['heading'] = ' '.join(s['heading'].split())
    return p.out


def words(text):
    return len(text.split())


def undefined(sections, min_words=40):
    """Headings with sections under them and fewer than min_words words of their own, with the count and first words."""
    found = []
    for i, s in enumerate(sections):
        nxt = sections[i + 1] if i + 1 < len(sections) else None
        if nxt is None or nxt['level'] <= s['level']:
            continue
        n = words(s['own'])
        if n < min_words:
            found.append({'level': s['level'], 'heading': s['heading'], 'words': n,
                          'start': ' '.join(s['own'].split()[:15])})
    return found


def report(found, total, min_words):
    lines = ['%d headings; %d have sections under them and fewer than %d words of their own:' % (total, len(found), min_words)]
    for f in found:
        if f['words']:
            own = '%d words: "%s%s"' % (f['words'], f['start'], '...' if f['words'] > 15 else '')
        else:
            own = 'no text of its own'
        lines.append('- %s "%s": %s' % ('#' * f['level'], f['heading'], own))
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('path', help='the guide, as Markdown or HTML (by its extension, or --html)')
    ap.add_argument('--min-words', type=int, default=40)
    ap.add_argument('--html', action='store_true')
    a = ap.parse_args(argv)
    text = open(a.path, encoding='utf-8').read()
    secs = from_html(text) if (a.html or a.path.lower().endswith(('.html', '.htm'))) else from_markdown(text)
    print('\n'.join(report(undefined(secs, a.min_words), len(secs), a.min_words)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
