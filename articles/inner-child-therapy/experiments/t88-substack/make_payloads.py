"""Turn 88 (copied from turn 87, from turn 79): the article as Substack paste payloads for the free Pangram check, split at h1 boundaries so each post's
text stays under LIMIT characters (Substack's check reads at most 99,999 per post; the hypnosis lane's finding).
Headings become <h1>..<h4>, every other block a <p>; text as the lane's Pangram tools see it (paragraphs_alone.reader_blocks,
ptext.plain): no notes, image or embed stand-ins, links as their words, no emphasis marks. Writes PAYLOAD-<X>.html,
TEXT-<X>.txt (the text the payload holds) and PAYLOADS.json (characters, words, SHA-256 of each payload file)."""
import hashlib, html, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 95000
here = pathlib.Path(__file__).resolve().parent
md = (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')
md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
seq = reader_blocks(md)
assert seq[0][1].startswith('# Inner Child Therapy — humanized article so far') and seq[1][1].startswith('> **Working review assembly only.**')
chapters = []
for kind, b in seq[2:]:
    if b.strip() == '---':
        continue
    lvl = len(b.split(' ')[0]) if kind == 'h' else 0
    t = plain('\n'.join(re.sub(r'^>\s?', '', l) for l in b.split('\n')))
    if kind == 'h' and lvl == 1 or not chapters:
        chapters.append([])
    chapters[-1].append((lvl, t))
parts, cur = [], []
size = lambda ch: sum(len(t) + 2 for _, t in ch)
for ch in chapters:
    if cur and sum(size(c) for c in cur) + size(ch) > LIMIT:
        parts.append(cur); cur = []
    cur.append(ch)
parts.append(cur)
out = []
for n, p in enumerate(parts):
    x = 'AB CD'.replace(' ', '')[n]
    blocks = [b for ch in p for b in ch]
    text = '\n\n'.join(t for _, t in blocks) + '\n'
    body = ''.join(('<h%d>%s</h%d>' % (l, html.escape(t), l)) if l else '<p>%s</p>' % html.escape(t).replace('\n', '<br>') for l, t in blocks)
    (here / f'PAYLOAD-{x}.html').write_text(body, encoding='utf-8')
    (here / f'TEXT-{x}.txt').write_text(text, encoding='utf-8')
    out.append({'part': x, 'payload': f'PAYLOAD-{x}.html', 'text': f'TEXT-{x}.txt', 'chars': len(text), 'words': len(text.split()),
                'payload_sha256': hashlib.sha256(body.encode('utf-8')).hexdigest(), 'first': blocks[0][1][:60], 'last_h1': [t for l, t in blocks if l == 1][-1]})
(here / 'PAYLOADS.json').write_text(json.dumps({'limit_chars': LIMIT, 'parts': out}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for o in out:
    print(o['part'], o['chars'], 'chars', o['words'], 'words |', o['first'][:40], '... last h1:', o['last_h1'])
