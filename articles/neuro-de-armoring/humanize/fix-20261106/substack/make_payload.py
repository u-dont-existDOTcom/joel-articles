#!/usr/bin/env python3
"""The whole article as it stands (HUMANIZED-SO-FAR.md), as the paste payload for one temporary Substack draft, for the free
check through Joel's Pangram extension (E325, E200; Joel, 2026-11-04 20:19 UTC: "so then are we done can we publish it?").

Adapted from the Inner Child lane's experiments/t119-substack/make_payloads.py (copied, not changed there). The check reads
at most 99,999 characters, and this article is about 38,000, so it is one draft. The pictures go ("[image N](...)" lines),
since the check reads no images. Headings are <h1> to <h6>; every other block is a <p> (the article has no lists in
Markdown). Text as the lane's tools see it (ptext.plain: links, bold and italics as plain text), with the quote marks
curled as the post shows them (curl(), the Inner Child lane's: Substack's editor curls every straight mark on paste, and
after an opening bracket it curls a double one the wrong way, so the payload carries them curled already).
Writes PAYLOAD-A.html, TEXT-A.txt (every block's text, headings included, which the paste's word check hashes) and
PAYLOADS.json."""
import hashlib
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import plain  # noqa: E402  (ptext.plain)

SRC = ROOT / 'articles/neuro-de-armoring/humanize/HUMANIZED-SO-FAR.md'
TITLE = 'Neuro de-armoring, draft A (temp, delete after)'
OPENERS = set('([{—–-/')
IMAGE = re.compile(r'^\[image \d+\]\(\S+\)$')


def curl(s):
    """The Inner Child lane's curl(): an opening mark at the start, after a space or one of ( [ { — – - /, and a closing
    mark or apostrophe elsewhere (a single opening mark only before a letter or digit)."""
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


def blocks(md):
    out = []
    for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)):
        b = b.strip()
        if not b or IMAGE.match(b):
            continue
        if b.startswith('#'):
            out.append(('h', len(b.split(' ')[0]), curl(plain(b))))
        else:
            out.append(('p', 0, curl(plain(b))))
    return out


def html_of(b):
    k, lvl, t = b
    if k == 'h':
        return '<h%d>%s</h%d>' % (lvl, html.escape(t, quote=False), lvl)
    return '<p>%s</p>' % html.escape(t, quote=False)


def main():
    seq = blocks(SRC.read_text(encoding='utf-8'))
    text = '\n\n'.join(t for _, _, t in seq) + '\n'
    body = ''.join(html_of(b) for b in seq)
    (HERE / 'PAYLOAD-A.html').write_text(body, encoding='utf-8')
    (HERE / 'TEXT-A.txt').write_text(text, encoding='utf-8')
    words = ' '.join(text.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'})).split())
    part = {'part': 'A', 'title': TITLE, 'payload': 'PAYLOAD-A.html', 'text': 'TEXT-A.txt', 'chars': len(text),
            'words': len(text.split()), 'blocks': len(seq), 'headings': sum(1 for b in seq if b[0] == 'h'),
            'payload_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest(),
            'words_sha256': hashlib.sha256(words.encode('utf-8')).hexdigest()}
    (HERE / 'PAYLOADS.json').write_text(json.dumps({'source': str(SRC.relative_to(ROOT)),
                                                    'source_sha256': hashlib.sha256(SRC.read_bytes()).hexdigest(),
                                                    'parts': [part]}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(part, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
