#!/usr/bin/env python3
"""Turn 105's review page rows: his 101.1 (GPT's 97.8, in) beside what it was, and the two paragraphs of question 102.1
and 102.2, each beside the draft that goes with its options.
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
old_md = re.sub(r'<!--.*?-->', '', subprocess.run(['git', 'show', '6fb51604:articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'],
                                                  cwd=ROOT, capture_output=True, text=True, check=True).stdout, flags=re.S)
old = [b for t, b in reader_blocks(old_md) if t == 'p']
DRAFTS = HERE.parent / 't105-tries' / 'drafts'
DRAFTS_104 = HERE.parent / 't104-tries' / 'drafts'


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
i = at('Say you keep coming back from trips confused or spaced out.')
rows.append((i, {'label': "101.1: GPT's 97.8, in, word for word (Human, 0.0000% AI in its stretch)", 'start': start_of(seq[i][1]),
                 'beside': {'label': 'Before', 'text': old_para('Milder reactions afterward count as caution signs too')}}))
i = at('Sometimes the session itself goes really well.')
rows.append((i, {'label': '102.1: 98.7 as it is (my pick, A, cuts it), beside d5 (option B: 100% Human alone, 34% AI in its section)',
                 'start': start_of(seq[i][1]),
                 'beside': {'label': 'Draft d5', 'text': (DRAFTS_104 / '98_7-d5.txt').read_text(encoding='utf-8').strip()}}))
i = at('After the day, look at what actually happened.')
rows.append((i, {'label': '102.2: your 98.2 as it is, beside d3 (my pick, A: Human alone and in its h2; not in)', 'start': start_of(seq[i][1]),
                 'beside': {'label': 'Draft d3', 'text': (DRAFTS / '98_2-d3.txt').read_text(encoding='utf-8').strip()}}))
rows.sort(key=lambda r: r[0])
blocks = []
for i, row in rows:
    hs = heads_at(i)
    if blocks and blocks[-1]['headings'] == hs:
        blocks[-1]['rows'].append(row)
    else:
        blocks.append({'headings': hs, 'rows': [row]})
out = {'title': 'Inner Child Therapy, turn 105: what changed',
       'meta': '2026-10-24, his answers of 2026-10-24 18:40 UTC; the article at branch handoff/claude-dangerous-adult-20260924-1631',
       'intro': ["Your 101.1, in, beside what it was before. Then the two paragraphs of question 102.1 and 102.2 as they are, each "
                 "beside the draft that goes with its options, which is not in. Every check is on experiments/t105-api/API-CHECKS.md, "
                 "and the panels' records are in experiments/t105-panel/."],
       'blocks': blocks}
(HERE / 'ROWS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(rows), 'rows in', len(blocks), 'blocks')
