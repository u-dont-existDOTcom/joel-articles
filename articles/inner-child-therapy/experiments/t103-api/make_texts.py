#!/usr/bin/env python3
"""Turn 103, first round: every paragraph his 97 and 98 answers changed (the 26 cuts of experiments/t102-safety/), alone,
where it has 50 words or more after the cut. His 96.1 paragraph passed his own check, so it goes in its stretch in round 2
with the rest. Writes TEXTS.json and texts/, and NAMES.json for the results page."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
seq = reader_blocks(md)
CUTS = json.loads((HERE.parent / 't102-safety' / 'CUTS.json').read_text(encoding='utf-8'))
AFTER = json.loads((HERE.parent / 't102-safety' / 'CUTS-AFTER.json').read_text(encoding='utf-8'))


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


def find_after(after_text):
    hits = [i for i, (k, b) in enumerate(seq) if k == 'p' and b == after_text]
    assert len(hits) == 1, (after_text[:60], hits)
    return hits[0]


ITEMS = [it for g in CUTS['groups'] for it in g['items']]
TEXTS, NAMES, INDEX = {}, {}, {}
for it in ITEMS:
    i = find_after(AFTER[it['id']]['after'])
    INDEX[it['id']] = i
    t = line(*seq[i])
    if len(t.split()) >= 50:
        n = 't103_' + it['id'].replace('.', '_')
        TEXTS[n] = t
        NAMES[n] = '%s (%s), the paragraph after the cut, alone' % (it['id'], it['title'].strip('"'))

if __name__ == '__main__':
    (HERE / 'TEXTS.json').write_text(json.dumps(TEXTS, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / 'INDEX.json').write_text(json.dumps(INDEX, indent=1) + '\n', encoding='utf-8')
    names = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8')) if (HERE / 'NAMES.json').exists() else {}
    names.update(NAMES)
    (HERE / 'NAMES.json').write_text(json.dumps(names, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for n, t in TEXTS.items():
        (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
    short = [it['id'] for it in ITEMS if 't103_' + it['id'].replace('.', '_') not in TEXTS]
    print(len(TEXTS), 'alone texts;', 'under 50 words (section only):', ', '.join(short))
    for n, t in TEXTS.items():
        print('%-12s %4d | %s' % (n, len(t.split()), t[:70]))
