#!/usr/bin/env python3
"""make_reader_files.py - what each fresh reader of the contents sees (the method of the inner child lane's turn 131,
../../../../inner-child-therapy/experiments/t131-toc-check/make_reader_files.py): one contents, numbered lines indented
by level and cut off where Substack's sidebar cuts them (tools/humanization/toc_sidebar.py), and the situations.

  python3 make_reader_files.py NOW FABLE      writes CONTENTS-<name>.txt and SITUATIONS.txt here
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

FILES = {'NOW': 'NOW.json', 'FABLE': 'PROPOSAL-FABLE.json', 'PICK': 'PROPOSAL-PICK.json', 'WHOLE': 'NOW.json'}


def lines(name):
    E = json.load(open(os.path.join(HERE, FILES[name]), encoding='utf-8'))
    out = []
    for i, e in enumerate(E):
        text = e['heading'] if name == 'WHOLE' else ts.shown(e['heading'], e['level'])[1]
        out.append((i + 1, e['id'], e['level'], text))
    return out


def write(name):
    L = lines(name)
    with open(os.path.join(HERE, 'CONTENTS-%s.txt' % name), 'w', encoding='utf-8') as f:
        for n, _id, level, text in L:
            f.write('%d  %s%s\n' % (n, '    ' * (level - 1), text))
    json.dump([{'n': n, 'id': i} for n, i, _, _ in L], open(os.path.join(HERE, 'LINES-%s.json' % name), 'w'), indent=1)


if __name__ == '__main__':
    for name in sys.argv[1:]:
        write(name)
    S = json.load(open(os.path.join(HERE, 'SITUATIONS.json'), encoding='utf-8'))['situations']
    with open(os.path.join(HERE, 'SITUATIONS.txt'), 'w', encoding='utf-8') as f:
        for s in S:
            f.write('%d. %s\n' % (s['n'], s['situation']))
    print('written:', ', '.join(sys.argv[1:]), '+ SITUATIONS.txt (%d)' % len(S))
