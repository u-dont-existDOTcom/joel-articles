#!/usr/bin/env python3
"""build.py - turn 51's texts for Pangram, made the way h57's build_baseline.py makes them.

- s01: Dealing With Shadow Thoughts as the guide now has it, his round-44 section with one word read his way ("we
  re-identify" for "we re-identifying"), so the correction is checked in place before the turn ends.
- The AI sections the handoff names, each paragraph by itself as the guide has it (lesson 19b: the near miss a try
  starts from, or Human High by itself and done). A paragraph under 50 words (the web app's minimum) goes with the ones
  after it in its section until the unit has 50; one left short at a section's end joins the unit before it. Only
  sections whose newest checks (../h57-20261119/STATUS.md) still show windows below High; headings left out.

  python3 build.py h59a      writes TEST-KEY.txt and ITEMS-h59a.json ([[key, text, sha256], ...]) and UNITS.json
"""
import collections, hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / 'h57-20261119'))
import build_baseline as BB  # noqa: E402

BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
BY = {b['id']: b for b in BLOCKS}
SKIP = ('h1', 'h2', 'h3', 'hr', 'image', 'youtube')
SECTIONS = [  # (heading it starts with, short name for keys)
    ('Who to Contact', 'contact'), ('Alone at 3 a.m.', 'alone'), ('For the Person Helping', 'helper'),
    ('When What They Say Turns Toward Harm', 'harm'), ('No Rash Actions', 'rash'), ('When the Trip Feels Amazing', 'euph'),
    ('Spiritual', 'spirit'), ('Dealing With Sorrow', 'sorrow'), ('Hand on Heart', 'heart'),
    ('Touch, Consent, and Compassion', 'touch'), ('Demons, Jinn, Entities, and Shadow Forces', 'demons'),
    ('Abuse Memories, Recovered Memories, and Certainty', 'abuse'), ('After the Storm', 'storm'),
]
STATUS = json.loads((HERE.parent / 'h57-20261119' / 'STATUS.json').read_text(encoding='utf-8'))
BELOW = collections.defaultdict(list)
for r in STATUS:
    if r['status'] != 'Human High':
        BELOW[r['block']].append(r)


def words(i):
    return len(BB.plain(BY[i]['md']).split())


def section_blocks():
    head, out = None, collections.OrderedDict()
    for b in BLOCKS:
        if b['kind'] in ('h1', 'h2', 'h3'):
            head = b['md'].lstrip('#').strip()
            continue
        if b['kind'] in SKIP or not head:
            continue
        for start, name in SECTIONS:
            if head.startswith(start):
                out.setdefault(name, (head, []))[1].append(b['id'])
    return out


def units():
    U = collections.OrderedDict()
    U['s01-shadow-section'] = (['B410', 'B411', 'B412', 'B414', 'R43-SHADOW-LIGHT', 'R43-SHADOW-PRESSURE', 'B415', 'B413'],
                               'section', "Dealing With Shadow Thoughts as the guide has it after his round-44 version")
    for name, (head, ids) in section_blocks().items():
        if not any(i in BELOW for i in ids):
            continue
        groups, cur = [], []
        for i in ids:
            cur.append(i)
            if sum(words(j) for j in cur) >= 50:
                groups.append(cur)
                cur = []
        if cur:
            if groups:
                groups[-1] += cur
            else:
                groups.append(cur)
        groups = [g for g in groups if any(i in BELOW for i in g)]   # a unit already Human High by itself is done
        for n, g in enumerate(groups, 1):
            scope = 'paragraph' if len(g) == 1 else ('pair' if len(g) == 2 else 'stretch')
            U['a%02d-%s-%d' % (len(U), name, n)] = (g, scope, '%s: %s (%s), by itself as the guide has it' % (
                head, ', '.join(g), '%d words' % sum(words(j) for j in g)))
    return U


UNITS = units()


def text(ids):
    return '\n\n'.join(BB.plain(BY[i]['md']) for i in ids).strip() + '\n'


def main(batch):
    items = []
    for key, (ids, scope, what) in UNITS.items():
        t = text(ids)
        (HERE / ('TEST-%s.txt' % key)).write_text(t, encoding='utf-8')
        s = t.strip()
        items.append([key, s, hashlib.sha256(s.encode('utf-8')).hexdigest()])
        print(key, scope, len(s.split()), ids)
    (HERE / ('ITEMS-%s.json' % batch)).write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'UNITS.json').write_text(json.dumps(UNITS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1])
