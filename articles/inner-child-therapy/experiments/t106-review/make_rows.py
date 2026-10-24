#!/usr/bin/env python3
"""Turn 106's review page rows: each paragraph my installs of his picks changed (his cuts, his merged sentence, d3 and the
paragraph break), beside what it was. His own five sections are his text and aren't repeated here.
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
old_md = re.sub(r'<!--.*?-->', '', subprocess.run(['git', 'show', 'cd4f8402:articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'],
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
    ('Reparenting means consciously evolving', 'Reparenting means consciously evolving', 'Your nutshell without its last sentence (h2)'),
    ('I think most people who chase spiritual freedom', 'I think most people who chase spiritual freedom', 'My Journey without "It doesn\'t mean you\'re stupid or crazy." (h3; question 103)'),
    ('Maybe just imagining a caring grown-up', 'Maybe just imagining a caring grown-up', 'If the Love Isn\'t Coming Yet: "It\'s scaffolding." (h7)'),
    ("Intentional, meaning you pick one", "Intentional, meaning you pick one", 'Under the new heading Make It Intentional, without "Some of them are only one step anyway." (e9, h12)'),
    ('After the day, look at what actually happened.', 'After the day, look at what actually happened.', 'd3 in place of your paragraph (your "98.2a")'),
    ('Whichever age it picks on, saving everybody', 'Whichever age it picks on, saving everybody', 'Instead of Blame without "Hindsight being 20/20 doesn\'t change that." (e10)'),
    ('Pema Chödrön calls the tightening', 'Pema Chödrön calls the tightening', 'Catch the Hook without "You can figure that out later." (h14)'),
    ('Count recognition as progress', 'Count recognition as progress', 'Your One Intention without the repeat of the repair (e13)'),
    ('While you look, notice what your body does', 'While you look, notice what your body does', 'Your photos paragraph without ", which is also completely OK" (h17)'),
    ("We don't need to ask it leading questions", "We don't need to ask it leading questions", 'Your photos paragraph without ", so we gotta be careful about that" (h18)'),
    ('Any of those reactions, from mania to paranoia', 'Any of those reactions, from mania to paranoia', 'When Escape Leaves Reality Behind: the disclaimer out, "These are just" (h22)'),
    ('Be careful what you mix, too', 'Be careful what you mix, too', 'Your merged acacia sentence (h23; question 103)'),
    ('With that under you, belonging with people', 'With that under you, belonging with people', 'You Belong Everywhere and Nowhere without "Not all at once, though." (h31)'),
    ('Most of us need enough Nurturer and Protector first.', 'Timing is different for everyone, but most of us', 'Timing Is Individual without "Timing is different for everyone, but" (h32)'),
    ('Where it really differs is spirituality.', 'Where it really differs is spirituality.', 'How This Relates to Schema Therapy: the Jeffrey Young parenthetical, "(no belief in God required)" and the last line out (h38, h39)'),
    ('Then again, maybe what', 'You might barely have spontaneous words', 'Your Inner Monologue P2, split before "Then again" (e5): both versions read Human'),
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
out = {'title': 'Inner Child Therapy, turn 106: what changed',
       'meta': '2026-10-24, his answers of 2026-10-24 22:55 UTC; the article at branch handoff/claude-dangerous-adult-20260924-1631',
       'intro': ["Each paragraph my installs of your picks changed, beside what it was: your cuts, your merged sentence, d3 and the "
                 "paragraph break you said I could try. Your own five sections are in word for word and aren't repeated here, and the "
                 "25 new headings change no paragraph. Every check is on experiments/t106-api/API-CHECKS.md."],
       'blocks': blocks}
(HERE / 'ROWS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(rows), 'rows in', len(blocks), 'blocks')
