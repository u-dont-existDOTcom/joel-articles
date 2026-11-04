#!/usr/bin/env python3
"""Turn 119: round 9, his reorganized guide as it is now (HUMANIZED-ARTICLE-SO-FAR.md after turns 117 and 118), as the paste
payloads for the two temporary Substack drafts, for the free check through his Pangram extension (E200; Joel, 2026-11-04
00:51 UTC: "go ahead").

Adapted from turn 114's make_payloads.py (round 8): split at h1 boundaries so each draft's text stays under LIMIT
characters of the 99,999 the check reads; the notes (pictures, videos, the pull-quote note) are comments and go, since
the check reads neither images nor embeds. Two changes for his guide: it has no title block to skip, and his lists go in
as real lists (<ul>/<ol>, an item a line) as his post will have them, where round 8 had no lists. Headings are <h1> to
<h5>; a paragraph's line breaks are <br>; text as the lane's tools see it (ptext.plain: links and bold as plain text), with
the quote marks curled as the post shows them (curl(): the master keeps the standard swap's straight marks).
Writes PAYLOAD-<X>.html, TEXT-<X>.txt (every block's text, headings included, which the paste's word check hashes) and
PAYLOADS.json."""
import hashlib
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import plain  # noqa: E402  (ptext.plain)

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 95000
OPENERS = set('([{—–-/')


def curl(s):
    """The quote marks curled as the post should show them. Substack's editor curls every straight mark on paste, and
    after an opening bracket it curls a double one the wrong way: the first paste of round 9 showed "(”What would Jesus
    do?”", "(”You hated that coat”)" and "(”Once upon a time…”", three of the typos he approved fixing in turn 117. So the
    payload carries them curled already: an opening mark at the start, after a space or one of ( [ { — – - /, and a
    closing mark or apostrophe elsewhere (a single opening mark only before a letter or digit)."""
    out = []
    for i, c in enumerate(s):
        prev = s[i - 1] if i else ' '
        nxt = s[i + 1] if i + 1 < len(s) else ' '
        if c == '"':
            out.append('“' if prev.isspace() or prev in OPENERS else '”')
        elif c == "'":
            out.append('‘' if (prev.isspace() or prev in OPENERS or prev in '"“') and nxt.isalnum() else '’')
        else:
            out.append(c)
    return ''.join(out)
SRC = ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'
ITEM = re.compile(r'^(?:[-*+]|\d+\.)\s+')


def blocks(md):
    """[(kind, level, text or items)]: ('h', 1..6, text), ('ul' or 'ol', 0, [item]), ('p', 0, text)."""
    md = curl(re.sub(r'<!--.*?-->', '', md, flags=re.S))
    out = []
    for b in re.split(r'\n\s*\n', md):
        b = b.strip('\n')
        if not b.strip():
            continue
        if b.startswith('#'):
            out.append(('h', len(b.split(' ')[0]), plain(b)))
            continue
        lines = b.split('\n')
        if ITEM.match(lines[0]):
            items = []
            for l in lines:
                if ITEM.match(l):
                    items.append(ITEM.sub('', l).rstrip())
                else:
                    items[-1] += '\n' + l.strip()
            kind = 'ol' if re.match(r'^\d+\.', lines[0]) else 'ul'
            out.append((kind, 0, [plain(x).replace(' \n', '\n') for x in items]))
            continue
        out.append(('p', 0, plain(b).replace(' \n', '\n')))
    return out


def text_of(b):
    k, _, t = b
    return '\n'.join(t) if k in ('ul', 'ol') else t


def html_of(b):
    k, lvl, t = b
    if k == 'h':
        return '<h%d>%s</h%d>' % (lvl, html.escape(t), lvl)
    if k in ('ul', 'ol'):
        return '<%s>%s</%s>' % (k, ''.join('<li><p>%s</p></li>' % html.escape(x).replace('\n', '<br>') for x in t), k)
    return '<p>%s</p>' % html.escape(t).replace('\n', '<br>')


def main():
    seq = blocks(SRC.read_text(encoding='utf-8'))
    chapters = []
    for b in seq:
        if (b[0] == 'h' and b[1] == 1) or not chapters:
            chapters.append([])
        chapters[-1].append(b)
    size = lambda ch: sum(len(text_of(b)) + 2 for b in ch)
    parts, cur = [], []
    for ch in chapters:
        if cur and sum(size(c) for c in cur) + size(ch) > LIMIT:
            parts.append(cur)
            cur = []
        cur.append(ch)
    parts.append(cur)
    out = []
    for n, p in enumerate(parts):
        x = 'ABCD'[n]
        bl = [b for ch in p for b in ch]
        text = '\n\n'.join(text_of(b) for b in bl) + '\n'
        body = ''.join(html_of(b) for b in bl)
        (HERE / ('PAYLOAD-%s.html' % x)).write_text(body, encoding='utf-8')
        (HERE / ('TEXT-%s.txt' % x)).write_text(text, encoding='utf-8')
        words = ' '.join(text.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'})).split())
        out.append({'part': x, 'payload': 'PAYLOAD-%s.html' % x, 'text': 'TEXT-%s.txt' % x, 'chars': len(text), 'words': len(text.split()),
                    'payload_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest(),
                    'words_sha256': hashlib.sha256(words.encode('utf-8')).hexdigest(),
                    'first': text_of(bl[0])[:60], 'h1s': [b[2] for b in bl if b[0] == 'h' and b[1] == 1]})
    (HERE / 'PAYLOADS.json').write_text(json.dumps({'source_sha256': hashlib.sha256(SRC.read_bytes()).hexdigest(), 'limit_chars': LIMIT,
                                                    'parts': out}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for o in out:
        print(o['part'], o['chars'], 'chars', o['words'], 'words |', o['first'][:40], '| h1s:', ' / '.join(o['h1s']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
