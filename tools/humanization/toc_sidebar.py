#!/usr/bin/env python3
"""How Substack's contents sidebar shows each heading: whole, or cut off with "…".

Joel, 2026-11-16 02:19 UTC: "we should be optimizing substack posts specifrically for their very narrow toc sidebar so we
might need to rethink some headings". Measured that day in the post's own contents menu (his laptop, the Claude desktop
app's browser): the labels are 15px system-ui (Inter there; SF Pro on a Mac and Segoe UI on Windows are a little
narrower), one line each, cut with an ellipsis, and the width left for the text is 217px for an h1, 205 for an h2, 193 for
an h3 and 181 for an h4 (each level is indented 12px more). An h5 or deeper isn't listed. Brave on the same laptop showed
about one character less (its scrollbar takes room), so a heading is "tight" when it fits by less than --margin (12px,
about two letters) and may be cut for some readers.

Widths come from HarfBuzz shaping with Inter Regular 4.001 (fonts/, under the SIL Open Font License: fonts/Inter-LICENSE.txt; exactly the browser's numbers, checked on all 147 labels), or,
without uharfbuzz, from a per-character table of the same font (within about 1px). An emoji counts 18.75px, as measured.

Usage:
  toc_sidebar.py TOC.md            # one line per heading: status, width/room, and what the sidebar shows
  toc_sidebar.py TOC.md --json     # the same as JSON
  toc_sidebar.py --text "My Heading" --level 2
TOC.md lines are Markdown headings (#, ##, ### or ####, indented or not); anything after two spaces and "(" (a word count) is ignored,
and so is a leading "[S012] " section id.
"""
from __future__ import annotations
import argparse, json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, 'fonts', 'Inter-Regular.ttf')
TABLE = os.path.join(HERE, 'fonts', 'inter-regular-15px-advances.json')
PX = 15.0
ROOM = {1: 217.0, 2: 205.0, 3: 193.0, 4: 181.0}
EMOJI_PX = 18.75
ELLIPSIS = '…'
_EMOJI = re.compile('(?:[☀-➿\U0001F000-\U0001FAFF][️\U0001F3FB-\U0001F3FF‍♀♂☀-➿\U0001F000-\U0001FAFF]*)')

_hb = None
def _shaper():
    global _hb
    if _hb is None:
        try:
            import uharfbuzz as hb
            face = hb.Face(hb.Blob.from_file_path(FONT))
            _hb = (hb, hb.Font(face), face.upem)
        except Exception:
            _hb = False
    return _hb

_table = None
def _advances():
    global _table
    if _table is None:
        with open(TABLE, encoding='utf-8') as f:
            _table = json.load(f)
    return _table

def _plain_width(text: str) -> float:
    if not text:
        return 0.0
    s = _shaper()
    if s:
        hb, font, upem = s
        buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
        hb.shape(font, buf, {'kern': True, 'liga': True})
        return sum(p.x_advance for p in buf.glyph_positions) * PX / upem
    t = _advances()
    adv, kern = t['advances'], t['kern']
    total = sum(adv.get(ch, adv['?']) for ch in text)
    return total + sum(kern.get(text[i:i + 2], 0.0) for i in range(len(text) - 1))

def width(text: str) -> float:
    """Width in px at 15px, emoji counted as EMOJI_PX each."""
    total, last = 0.0, 0
    for m in _EMOJI.finditer(text):
        total += _plain_width(text[last:m.start()]) + EMOJI_PX
        last = m.end()
    return total + _plain_width(text[last:])

def shown(text: str, level: int) -> tuple[bool, str, float, float]:
    """(fits, what the sidebar shows, width, room) for a heading at level 1-4."""
    room = ROOM[level]
    w = width(text)
    if w <= room + 0.01:
        return True, text, w, room
    ell = width(ELLIPSIS)
    lo, hi = 0, len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if width(text[:mid]) + ell <= room:
            lo = mid
        else:
            hi = mid - 1
    return False, text[:lo] + ELLIPSIS, w, room

def status(text: str, level: int, margin: float = 12.0) -> str:
    fits, _, w, room = shown(text, level)
    if not fits:
        return 'cut'
    return 'tight' if room - w < margin else 'fits'

_LINE = re.compile(r'^\s*(#{1,6})\s+(?:\[(S\d+)\]\s+)?(.*?)(?:\s{2,}\(.*\))?\s*$')
def parse_toc(path: str):
    out = []
    for line in open(path, encoding='utf-8'):
        m = _LINE.match(line.rstrip('\n'))
        if m:
            out.append({'level': len(m.group(1)), 'id': m.group(2), 'heading': m.group(3)})
    return out

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('toc', nargs='?')
    ap.add_argument('--text'); ap.add_argument('--level', type=int, default=2)
    ap.add_argument('--margin', type=float, default=12.0)
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    rows = [{'level': a.level, 'id': None, 'heading': a.text}] if a.text else parse_toc(a.toc)
    res = []
    for r in rows:
        if r['level'] > 4:
            res.append({**r, 'status': 'not listed', 'shown': '', 'width': round(width(r['heading']), 1), 'room': None}); continue
        fits, sh, w, room = shown(r['heading'], r['level'])
        res.append({**r, 'status': status(r['heading'], r['level'], a.margin), 'shown': sh, 'width': round(w, 1), 'room': room})
    if a.json:
        json.dump(res, sys.stdout, ensure_ascii=False, indent=1); print()
    else:
        for r in res:
            ind = '  ' * (r['level'] - 1)
            room = '' if r['room'] is None else f"/{r['room']:.0f}"
            print(f"{r['status']:10} {r['width']:6.1f}{room:5} {ind}{r['shown'] or r['heading']}")
        n = {s: sum(1 for r in res if r['status'] == s) for s in ('fits', 'tight', 'cut')}
        print(f"\n{len(res)} headings: {n['fits']} fit, {n['tight']} tight (fit by less than {a.margin:g}px), {n['cut']} cut off")
    return 0

if __name__ == '__main__':
    sys.exit(main())
