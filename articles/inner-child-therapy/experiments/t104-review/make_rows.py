#!/usr/bin/env python3
"""Turn 104's review page rows: his 100.1 A (the naming aside after P1, his heading, P9 and P10) and 100.2 A (P2), each
beside what it was, and the three paragraphs of question 101, each beside the draft the tell panel and Pangram read.
Writes ROWS.json for tools/humanization/review_rows.py."""
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
old_md = re.sub(r'<!--.*?-->', '', subprocess.run(['git', 'show', '64becc8f:articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'],
                                                  cwd=ROOT, capture_output=True, text=True, check=True).stdout, flags=re.S)
old = [b for t, b in reader_blocks(old_md) if t == 'p']
DRAFTS = HERE.parent / 't104-tries' / 'drafts'


def old_para(start):
    hits = [b for b in old if b.startswith(start)]
    assert len(hits) == 1, start
    return hits[0]


def start_of(text):
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


def at(start):
    hits = [k for k, (t, b) in enumerate(seq) if t == 'p' and b.startswith(start)]
    assert len(hits) == 1, start
    return hits[0]


rows = []
i = at('By the way, this job doesn')
rows.append((i, {'label': '100.1 A: the naming aside, moved here from the end of P10 (GPT\'s move)', 'start': start_of(seq[i][1]),
                 'beside': {'label': 'Before: P10 ended with it', 'text': old_para('With that under you, belonging with people')}}))
i = at("Maybe you've let a small child win at Go Fish")
rows.append((i, {'label': '100.2 A: treats and pampering at set times', 'start': start_of(seq[i][1]),
                 'beside': {'label': 'Before', 'text': old_para("Maybe you've let a small child win at Go Fish")}}))
i = at('The Guide also points beyond itself')
rows.append((i, {'label': '100.1 A: your heading and P9, word for word', 'start': 'The Guide also points beyond itself, toward',
                 'beside': {'label': 'Before (under "A Belonging Deeper Than Any Group")', 'text': old_para('The Guide also points beyond itself')}}))
i = at('With that under you, belonging with people')
rows.append((i, {'label': '100.1 A: your P10, word for word', 'start': start_of(seq[i][1])}))
for start, name, label in (('Milder reactions afterward count as caution signs too', '97_8-d4', '101.1: 97.8 as it is, beside draft d4 (100% AI; not in)'),
                           ('Sometimes the session itself goes really well.', '98_7-d5', '101.2: 98.7 as it is, beside draft d5 (100% Human alone, 34% AI in its section; not in)'),
                           ('After the day, look at what actually happened.', '98_2-c1', '101.3: your 98.2 as it is, beside candidate c1 (35% AI; not in)')):
    i = at(start)
    rows.append((i, {'label': label, 'start': start_of(seq[i][1]),
                     'beside': {'label': 'Draft ' + name.split('-')[1], 'text': (DRAFTS / (name + '.txt')).read_text(encoding='utf-8').strip()}}))
rows.sort(key=lambda r: r[0])
blocks = []
for i, row in rows:
    hs = heads_at(i)
    if blocks and blocks[-1]['headings'] == hs:
        blocks[-1]['rows'].append(row)
    else:
        blocks.append({'headings': hs, 'rows': [row]})
out = {'title': 'Inner Child Therapy, turn 104: what changed',
       'meta': '2026-10-24, his answers of 2026-10-23 23:21 UTC; the article at branch handoff/claude-dangerous-adult-20260924-1631',
       'intro': ['Your 100.1 A and 100.2 A, in, each beside what it was before. Then the three paragraphs of question 101 as they '
                 'are, each beside the draft the tell panel and Pangram read, which is not in. Every check is on '
                 'experiments/t104-api/API-CHECKS.md, and each panel\'s record is in experiments/t104-panel/.'],
       'blocks': blocks}
(HERE / 'ROWS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(rows), 'rows in', len(blocks), 'blocks')
