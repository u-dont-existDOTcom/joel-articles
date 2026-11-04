#!/usr/bin/env python3
"""typography_swap.py - the standard typographic swap (gate E337 (gut), and E353 (Inner Child) for the dashes): curly quote
marks become straight ones, and each em dash, and each en dash with a space beside it, becomes his two hyphens, "--", with
no spaces around them. Nothing else changes.

Joel, 2026-11-03 22:02 UTC: "yes make that swapping standard". The evidence: pangram-humanization-lab PR #195
(state/experiments/quote-style-41-20261103/) and PR #196 (state/experiments/dash-style-41-20261103/). Straightening
improved 40 of 113 borderline paragraphs of his articles on Pangram 4.1 and hurt 4. The dash swap improved 9 of 47 AI or
borderline ones and hurt none. Paragraphs already at 100% Human, High barely moved either way. His own straight marks
stay as he typed them (curling them only hurt).

Until 2026-11-04 the swap made each em dash a spaced en dash (" – "). On the Inner Child guide's sense-read marking page
he turned down making his two "--" into that dash: "no everything should be the 2 dashes not em-dash, em-dash is ai";
asked whether that meant all the guide's dashes, with no spaces like his "handling--we", and the swap for every article,
he answered (2026-11-04 16:30 UTC): "yes to both, we've already established before that pangram prefers the 2 dashes, but
it won't matter anyway in high conf human sections. it could flip low conf ones ai". A range stays a range: an em dash
between two digits becomes an unspaced en dash ("10–20"), and an unspaced en dash is left as it is.

  python3 tools/humanization/typography_swap.py FILE [--html] [--write]   # prints what changes; --write saves it
  python3 tools/humanization/typography_swap.py --check FILE [--html]     # exit 1 if anything would change

With --html, only the text between tags changes (attributes, URLs and scripts are left alone). No third-party packages,
so CI's bare Python can run it.
"""
import argparse
import pathlib
import re
import sys

QUOTES = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'})
EM = '—'
EN = '–'


# a dash in running text: any em dash, with its spaces, or an en dash with a space on either side ("a – b", "a –b")
DASH = re.compile('[ \u00a0]*' + EM + '[ \u00a0]*|[ \u00a0]+' + EN + '[ \u00a0]*|' + EN + '[ \u00a0]+')
RANGE = re.compile(r'(?<=\d)' + EM + r'(?=\d)')
NUMBER_BEFORE = re.compile(r'\d[A-Za-z%\u00b0]{0,3}$')
NUMBER_AFTER = re.compile(r'\d')


def swap_text(text):
    """The swapped text and the number of characters changed. An em dash between two digits (a range) becomes an
    unspaced en dash, and an unspaced en dash (a range or a compound) stays; every other em dash, and every en dash with
    a space beside it, becomes "--" with no spaces, except at a line's edge, where it keeps one space toward its words."""
    out = text.translate(QUOTES)
    changed = sum(1 for c in text if c in '‘’“”') + len(RANGE.findall(out))
    out = RANGE.sub(EN, out)
    src, n = out, [0]

    def hyphens(m):
        if EN in m.group(0) and NUMBER_BEFORE.search(src, 0, m.start()) and NUMBER_AFTER.match(src, m.end()):
            return m.group(0)   # a spaced range between two amounts ("1.8g – 2.4g") stays as it is
        n[0] += 1
        before = src[m.start() - 1] if m.start() else '\n'
        after = src[m.end()] if m.end() < len(src) else '\n'
        return '-- ' if before == '\n' else ' --' if after == '\n' else '--'
    out = DASH.sub(hyphens, src)
    return out, changed + n[0]


TAG = re.compile(r'(<script\b.*?</script>|<style\b.*?</style>|<[^>]*>)', re.S | re.I)


def swap_html(html):
    """The same swap on the text between tags only."""
    parts, n = [], 0
    for i, piece in enumerate(TAG.split(html)):
        if i % 2:          # a tag, a script or a style block: untouched
            parts.append(piece)
        else:
            t, c = swap_text(piece)
            parts.append(t)
            n += c
    return ''.join(parts), n


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('file')
    ap.add_argument('--html', action='store_true')
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    p = pathlib.Path(a.file)
    src = p.read_text(encoding='utf-8')
    new, n = (swap_html if a.html else swap_text)(src)
    if a.check:
        print('%s: %d character(s) to swap' % (p, n))
        return 1 if new != src else 0
    if a.write and new != src:
        p.write_text(new, encoding='utf-8')
    print('%s: %d character(s) %s' % (p, n, 'swapped' if a.write else 'would be swapped'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
