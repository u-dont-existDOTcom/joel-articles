#!/usr/bin/env python3
"""The partly real junk passages that still stand in the fixed version (r30/junk/VETTED.md, PARTLY), each in its section
check as r38/sections.py cut it, with the flagged sentence marked and whose words it is (the last layer that wrote its
paragraph: his answer, my tested change, or the live post). Writes PARAS.md (for the writer) and ITEMS.json.
Left out: B22, whose sentence his own fix of section 05 kept (his check read it High), and B155, whose flagged words a
later fix already changed; B87, B210, B331, B363, B414, B435 and B482's flagged words are gone from the fixed version."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
V = (FIX / 'r30' / 'junk' / 'VETTED.md').read_text(encoding='utf-8')
SECTIONS = json.loads((FIX / 'r38' / 'SECTIONS.json').read_text(encoding='utf-8'))
CMAP = json.loads((FIX / 'whole' / 'CHANGE-MAP.json').read_text(encoding='utf-8'))
SPLIT = re.compile(r'(?<=[.!?…”"])\s+(?=[A-Z“"(])')
ANCHOR = {'B47': 'The full conversation', 'B50': 'People don’t only trigger each other', 'B54': 'It depends what each of you',
          'B123': 'wisdom window', 'B128': 'Jealousy, abandonment, possessiveness', 'B148': 'right when both people most need',
          'B170': 'It’s great if the ground underneath', 'B173': 'Going in, it helps to recognize your pattern',
          'B178': 'If something severe is happening', 'B217': 'contains the seed of its own destruction',
          'B230': 'or make them primary meditation targets', 'B232': 'Nobody has to be completely healed',
          'B234': 'I already said before dating that', 'B255': 'show me where I was missing people',
          'B330': 'In the previous section', 'B391': 'Every couple has to work out for themselves',
          'B459': 'with the goal of helping the conflict', 'B465': 'Even the curiosity itself',
          'B476': 'A relationship like this is rare', 'B477': 'which might be why we see ourselves',
          'B478': 'Also reminiscent of Somé'}
EXTRA = {'B217': ['It is wonderful to have their love and support'], 'B330': ['since, each contains the seed of the other'],
         'B459': ['But do it fairly']}
prob = {}
for line in V.splitlines():
    m = re.match(r'\|\s*(B[\d\-]+)\s*\|\s*(\w+)\s*\|\s*(\w+)\s*\|\s*(.*)\|\s*$', line)
    if m:
        prob[m.group(1)] = (m.group(2), m.group(3), m.group(4).strip())


def whose(par):
    last = None
    for c in CMAP:
        if any(par == n for n in c.get('new', [])):
            last = c['check']
    if last is None:
        return 'MODEL (the live post as it was)'
    return ('HIS (%s)' % last) if last.startswith('his answer') else ('MODEL (%s)' % last)


items = []
for bid, anchor in ANCHOR.items():
    hits = []
    for s in SECTIONS:
        t = (FIX / 'r38' / 'checks' / ('CHECK-%s.txt' % s['key'])).read_text(encoding='utf-8')
        if anchor in t:
            hits.append((s, t))
    assert len(hits) == 1, (bid, [h[0]['key'] for h in hits])
    s, t = hits[0]
    par = next(p for p in t.split('\n\n') if anchor in p)
    marks = [x for x in SPLIT.split(par) if anchor in x or any(e in x for e in EXTRA.get(bid, []))]
    assert marks, bid
    # whose: the fixed version's paragraph with its links, found by its plain words
    items.append({'id': bid, 'key': s['key'], 'heading': s['heading'], 'paragraph': par, 'marks': marks,
                  'problem': prob[bid][2], 'reader_voice': prob[bid][1], 'whose': whose(par) if True else ''})
by_key = {}
for it in items:
    by_key.setdefault(it['key'], []).append(it)
out = ['# The passages to fix, each in its section', '',
       'Each item is a section of the essay. The sentences a reader flagged as not making sense or not following are marked',
       '[[FLAG (whose): the sentence || the problem]]. Everything else is context: keep it word for word.', '']
n = 0
for key, its in by_key.items():
    n += 1
    t = (FIX / 'r38' / 'checks' / ('CHECK-%s.txt' % key)).read_text(encoding='utf-8')
    for it in its:
        w = 'HIS' if it['whose'].startswith('HIS') else 'MODEL'
        for m in it['marks']:
            assert t.count(m) == 1, (it['id'], m[:50])
            t = t.replace(m, '[[FLAG %s (%s): %s || the problem: %s]]' % (it['id'], w, m, it['problem']))
    out += ['## Item %d (%s)' % (n, key), '', 'Section: %s' % its[0]['heading'], '', t, '']
(HERE / 'PARAS.md').write_text('\n'.join(out), encoding='utf-8')
(HERE / 'ITEMS.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(items), 'passages in', len(by_key), 'sections')
for it in items:
    print(it['id'], it['key'][:40], '|', it['whose'][:70])
