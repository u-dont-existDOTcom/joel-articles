#!/usr/bin/env python3
"""Write what each fresh reader sees: one contents (numbered lines, indented by level, cut off where Substack's sidebar
cuts it) and the 68 situations in one mixed order (the 38 from turn 130 and the 30 held-out ones, unmarked).

  python3 make_reader_files.py OUTDIR      # OUTDIR/<contents>/CONTENTS.txt + SITUATIONS.txt; writes CONTENTS-*.txt, SITUATIONS-MIXED.json here
"""
import json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts
T130 = os.path.join(HERE, '..', 't130-toc')
CONTENTS = {'NOW': os.path.join(T130, 'LIVE-TOC.json'), 'OPUS': os.path.join(T130, 'PROPOSAL-PICK.json'),
            'GPT': os.path.join(T130, 'PROPOSAL-C.json'), 'FABLE': os.path.join(HERE, 'PROPOSAL-FABLE.json'),
            'FABLE2': os.path.join(HERE, 'PROPOSAL-FABLE2.json'), 'FABLE3': os.path.join(HERE, 'PROPOSAL-FABLE3.json')}

def lines(path):
    E = [e for e in json.load(open(path)) if not e.get('drop')]
    # an added heading (FABLE2's S048b) counts as the section it sits in
    return [(i + 1, e.get('part_of', e['id']), e['level'], ts.shown(e['heading'], e['level'])[1]) for i, e in enumerate(E)]

def situations():
    old = []
    for l in open(os.path.join(T130, 'SITUATIONS.md'), encoding='utf-8'):
        m = re.match(r'^(\d+)\.\s+(.*)$', l.strip())
        if m:
            old.append(('A' + m.group(1), m.group(2)))
    held = [('B' + str(h['n']), h['situation']) for h in json.load(open(os.path.join(HERE, 'SITUATIONS-HELDOUT.json')))['situations']]
    allv = old + held
    random.Random(131).shuffle(allv)
    return [{'n': i + 1, 'key': k, 'situation': s} for i, (k, s) in enumerate(allv)]

if __name__ == '__main__':
    out = sys.argv[1]
    S = situations()
    json.dump(S, open(os.path.join(HERE, 'SITUATIONS-MIXED.json'), 'w'), ensure_ascii=False, indent=1)
    sit_txt = '\n'.join(f"{s['n']}. {s['situation']}" for s in S) + '\n'
    for name, path in CONTENTS.items():
        txt = '\n'.join(f"{n:>3}  {'    ' * (lvl - 1)}{shown}" for n, _, lvl, shown in lines(path)) + '\n'
        open(os.path.join(HERE, f'CONTENTS-{name}.txt'), 'w', encoding='utf-8').write(txt)
        d = os.path.join(out, name)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'CONTENTS.txt'), 'w', encoding='utf-8').write(txt)
        open(os.path.join(d, 'SITUATIONS.txt'), 'w', encoding='utf-8').write(sit_txt)
    print(len(S), 'situations;', ', '.join(CONTENTS))
