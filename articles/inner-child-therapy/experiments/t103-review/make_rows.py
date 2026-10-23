#!/usr/bin/env python3
"""Turn 103's review page rows: his 96.1 paragraph, the 26 cuts of 97 and 98 (each beside its paragraph before the cut),
and The Inner Guide's three headings, in article order. Writes ROWS.json for tools/humanization/review_rows.py."""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402

md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
seq = reader_blocks(md)
CUTS = json.loads((HERE.parent / 't102-safety' / 'CUTS.json').read_text(encoding='utf-8'))
AFTER = json.loads((HERE.parent / 't102-safety' / 'CUTS-AFTER.json').read_text(encoding='utf-8'))
old_md = subprocess.run(['git', 'show', '614524e7:articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'], cwd=ROOT,
                        capture_output=True, text=True, check=True).stdout
old_961 = [l for l in old_md.split('\n') if l.startswith('Differentiation is slow, and it goes on your whole life.')][0]


def start_of(text):
    """A row's start: the paragraph's first words, stopping before a link, which the rendered page shows as its text only."""
    s = text[:60]
    return s.split('[')[0].rstrip() if '[' in s else s


def heads_at(i):
    heads, level = [], 9
    for k in range(i, -1, -1):
        t, b = seq[k]
        if t == 'h':
            n = len(b) - len(b.lstrip('#'))
            if n < level:
                heads.append(b)
                level = n
            if n == 1:
                break
    return list(reversed(heads))


rows = []
titles = {it['id']: it['title'] for g in CUTS['groups'] for it in g['items']}
for iid, v in AFTER.items():
    i = [k for k, (t, b) in enumerate(seq) if t == 'p' and b == v['after']][0]
    rows.append((i, {'label': '%s A: cut %s' % (iid, titles[iid]), 'start': start_of(v['after']),
                     'beside': {'label': 'Before the cut', 'text': v['before']}}))
i = [k for k, (t, b) in enumerate(seq) if t == 'p' and b.startswith('Differentiation is slow, and it goes on your whole life.')][0]
rows.append((i, {'label': '96.1 B: your paragraph, word for word', 'start': 'Differentiation is slow, and it goes on your whole life.', 'beside': {'label': 'Before', 'text': old_961}}))
for h in ('## Between Spoiling and Clamping Down', '## A Healthy Mind Is Not a Perfect Mind', '## A Belonging Deeper Than Any Group'):
    i = [k for k, (t, b) in enumerate(seq) if b == h][0]
    rows.append((i + 1, {'label': '99 A: under the new heading %s (no word changes)' % h.lstrip('# '), 'start': start_of(seq[i + 1][1])}))
rows.sort(key=lambda r: r[0])
blocks = []
for i, row in rows:
    hs = heads_at(i)
    if blocks and blocks[-1]['headings'] == hs:
        blocks[-1]['rows'].append(row)
    else:
        blocks.append({'headings': hs, 'rows': [row]})
out = {'title': 'Inner Child Therapy, turn 103: what changed',
       'meta': '2026-10-23, his answers of 21:52 UTC; the article at branch handoff/claude-dangerous-adult-20260924-1631',
       'intro': ['Your 96.1 paragraph, the 26 cuts you took in 97 and 98, and The Inner Guide\'s three headings (99 A). Beside each paragraph: what it was before. Every check is on experiments/t103-api/API-CHECKS.md, and what still reads AI is question 100.'],
       'blocks': blocks}
(HERE / 'ROWS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(rows), 'rows in', len(blocks), 'blocks')
