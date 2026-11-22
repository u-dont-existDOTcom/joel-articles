#!/usr/bin/env python3
"""score.py - each reader's picks against the key (SITUATIONS.json's expected sections, by section id, so a renamed heading
still counts): first pick right, guesses, right by the second pick.

  python3 score.py      reads reads/READ-<CONTENTS>-<n>.txt ("situation | line | sure|guess | next line" per line)
"""
import glob, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
S = {s['n']: s for s in json.load(open(os.path.join(HERE, 'SITUATIONS.json'), encoding='utf-8'))['situations']}
# the second reader's additions to the key (gate inner-child-2026-11-17b): a section that answers the situation just as
# directly counts as right too
if os.path.exists(os.path.join(HERE, 'KEY-CHECK.json')):
    for a in json.load(open(os.path.join(HERE, 'KEY-CHECK.json'), encoding='utf-8')).get('add', []):
        if a.get('n') in S:
            S[a['n']]['expected'] = list(S[a['n']]['expected']) + [i for i in a.get('ids', []) if i not in S[a['n']]['expected']]
rows, per = [], {}
for f in sorted(glob.glob(os.path.join(HERE, 'reads', 'READ-*.txt'))):
    name, k = re.match(r'READ-([A-Z0-9]+)-(\d+)\.txt$', os.path.basename(f)).groups()
    ids = {e['n']: e['id'] for e in json.load(open(os.path.join(HERE, 'LINES-%s.json' % name)))}
    first = guess = second = 0
    for line in open(f, encoding='utf-8'):
        m = re.match(r'\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(sure|guess)\s*(?:\|\s*(\d+))?', line, re.I)
        if not m:
            continue
        n, a, how, b = int(m.group(1)), int(m.group(2)), m.group(3).lower(), m.group(4)
        exp = S[n]['expected'] if n in S else []
        ok1 = ids.get(a) in exp
        ok2 = ok1 or (b is not None and ids.get(int(b)) in exp)
        first += ok1; guess += how == 'guess'; second += ok2
        per.setdefault(n, {})['%s-%s' % (name, k)] = (ids.get(a), how, ok1)
    rows.append({'reader': '%s-%s' % (name, k), 'first_right': first, 'guesses': guess, 'right_by_second': second})
json.dump({'rows': rows, 'per_situation': per}, open(os.path.join(HERE, 'SCORES.json'), 'w'), indent=1)
for r in rows:
    print('%-10s first right %2d   guesses %2d   right by the 2nd %2d   (of %d)' % (r['reader'], r['first_right'], r['guesses'], r['right_by_second'], len(S)))
