"""Turn 78: the moved article as plain text for free Substack checks, split at h1 boundaries into parts of at most
LIMIT words (Joel, 2026-10-21 00:49 UTC: "the free substack post workaround for a large section (up to 9999 words i think)").
Text as the lane's Pangram tools see it (tools/humanization/paragraphs_alone.reader_blocks and ptext.plain): no notes,
no image or embed stand-ins, links as their words, no emphasis marks. Writes part-N.txt and PARTS.json next to itself."""
import hashlib, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 9000
here = pathlib.Path(__file__).resolve().parent
md = (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')
md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
seq = reader_blocks(md)
assert seq[0][1].startswith('# Inner Child Therapy — humanized article so far') and seq[1][1].startswith('> **Working review assembly only.**')
seq = seq[2:]
chapters = []
for kind, b in seq:
    if b.strip() == '---':
        continue
    t = plain('\n'.join(re.sub(r'^>\s?', '', l) for l in b.split('\n')))
    if kind == 'h' and b.startswith('# '):
        chapters.append({'h1': t, 'blocks': []})
    if not chapters:
        chapters.append({'h1': '(opening, before the first h1)', 'blocks': []})
    chapters[-1]['blocks'].append(t)
for c in chapters:
    c['words'] = sum(len(x.split()) for x in c['blocks'])
parts, cur = [], []
for c in chapters:
    if cur and sum(x['words'] for x in cur) + c['words'] > LIMIT:
        parts.append(cur); cur = []
    cur.append(c)
parts.append(cur)
out = []
for n, p in enumerate(parts, 1):
    text = '\n\n'.join(b for c in p for b in c['blocks']) + '\n'
    (here / f'part-{n}.txt').write_text(text, encoding='utf-8')
    out.append({'part': n, 'file': f'part-{n}.txt', 'words': len(text.split()), 'sha256': hashlib.sha256(text.encode()).hexdigest(),
                'first_h1': p[0]['h1'], 'last_h1': p[-1]['h1'], 'h1s': [c['h1'] for c in p]})
(here / 'PARTS.json').write_text(json.dumps({'limit': LIMIT, 'article_words': sum(c['words'] for c in chapters), 'parts': out}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for o in out:
    print(o['part'], o['words'], 'words |', o['first_h1'], '...', o['last_h1'])
