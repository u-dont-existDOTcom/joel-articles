#!/usr/bin/env python3
"""Turn 107's review page rows: each paragraph of his My Journey and Not Every Hero Wears A Cape whose words changed, beside
what it was (so he can see the links and the two italic words back on the same words, and each of his lines its own
paragraph), and the typo fix. Writes ROWS.json for tools/humanization/review_rows.py."""
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
old_md = re.sub(r'<!--.*?-->', '', subprocess.run(['git', 'show', 'bf7ac9f5:articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'],
                                                  cwd=ROOT, capture_output=True, text=True, check=True).stdout, flags=re.S)
old = [b for t, b in reader_blocks(old_md) if t == 'p']



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


ROWS = [  # (start of the paragraph now, start of the paragraph before, label)
    ('I used to preach', 'I used to preach', 'Your first paragraph (103.1)'),
    ("From what I've seen, most people (like me)", 'I think most people who chase spiritual freedom', 'Your bypassing paragraph, now second (103.1)'),
    ('The way I think this works is simple.', 'The way I picture it is almost stupidly simple.', 'Your food bank paragraph (103.1)'),
    ('I was well-loved as a child', 'I was well-loved as a child', 'Your metta paragraph (103.1)'),
    ('I also found more love in the rest of the', 'I found more love in', 'Your teachings paragraph, without "Metta gave all that love somewhere to land." (103.1)'),
    ('But it didn’t reach everything.', "But it didn't reach everything.", 'Your clarification as an article sentence of yours (one of the "too verbatim" ones)'),
    ('At one pivotal point,', 'I used San Pedro cactus', 'Your San Pedro sentence (103.1)'),
    ('Years later, I found a warm, intuitive', 'I found the therapist, Daja,', 'Your Daja paragraph (one of the "too verbatim" ones)'),
    ('It also showed me that I really do need', 'It also showed me that I really do need', 'Your last paragraph before the map, without "in general and map it out completely" (one of the "too verbatim" ones)'),
    ('You can protect your little one from yourself too', 'You can protect your little one from yourself too', 'Your Not Every Hero P2 (103.2)'),
    ('How many tries would I give it?', 'How many tries would I give it?', 'The typo in your When to Change the Strategy (103.4 A)'),
]
rows = []
for now, before, label in ROWS:
    i = at(now)
    was = old_para(before)
    k = 0
    while k < min(len(seq[i][1]), len(was)) and seq[i][1][k] == was[k]:
        k += 1
    common = seq[i][1][:k].rsplit(' ', 1)[0]
    # the page marks the words that changed, so a start that runs into a change isn't on it; use the unchanged prefix
    start = start_of(seq[i][1]) if k >= 60 or len(common) < 20 else common
    rows.append((i, {'label': label, 'start': start, 'beside': {'label': 'Before', 'text': was}}))
rows.sort(key=lambda r: r[0])
blocks = []
for i, row in rows:
    hs = heads_at(i)
    if blocks and blocks[-1]['headings'] == hs:
        blocks[-1]['rows'].append(row)
    else:
        blocks.append({'headings': hs, 'rows': [row]})
out = {'title': 'Inner Child Therapy, turn 107: what changed',
       'meta': '2026-10-25, his answers of 2026-10-25 00:24 UTC; the article at branch handoff/claude-dangerous-adult-20260924-1631',
       'intro': ["Your My Journey and your first three paragraphs of Not Every Hero Wears A Cape are in word for word. Each paragraph "
                 "whose words changed is here beside what it was, so you can see that the links and the two italic words are back on "
                 "the same words (your paste was plain text) and that each of your lines is its own paragraph. Your acacia sentence "
                 "stays (103.3 A), and the typo is fixed (103.4 A). Nothing here was checked again, since you checked both sections."],
       'blocks': blocks}
(HERE / 'ROWS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(rows), 'rows in', len(blocks), 'blocks')
