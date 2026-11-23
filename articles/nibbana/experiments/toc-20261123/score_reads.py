#!/usr/bin/env python3
"""Score the fresh readers' answers against the answer key, by section id (the method of
../../../inner-child-therapy/experiments/t130-toc/score_reads.py).

  python3 score_reads.py [KEY.json]      # reads reads/READ-<NAME>-<k>.md, writes SCORES.json, prints the table

A read's name says which contents it saw: NOW-SIDEBAR, NOW-FULL (CONTENTS-NOW.json) or a proposal (PROPOSAL-<NAME>.json,
sidebar view). Its part-1 table gives, per situation, the first heading and, for a guess, the next. A heading is matched to
its section in that contents as the reader saw it ("…" included), so a renamed section counts by its id. A first pick is
"right" when its section is one of the situation's right or also sections, "near" when it is the parent of one of them, and
"wrong" otherwise; "found" counts a right first or next pick.
"""
import difflib, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

_EMO = re.compile('[☀-➿\U0001F000-\U0001FAFF️‍\U0001F3FB-\U0001F3FF]')


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-')
    s = _EMO.sub('', s)
    s = re.sub(r'[`*#]', '', s).strip()
    s = re.sub(r'\s*\(\d+ words\)\s*$', '', s)
    s = re.sub(r'(…|\.\.\.)\s*$', '', s)
    s = s.strip(' "\'').lower()
    return re.sub(r'\s+', ' ', s).strip()


def contents(name):
    if name.startswith('NOW'):
        E = json.load(open(os.path.join(HERE, 'CONTENTS-NOW.json'), encoding='utf-8'))
        sidebar = name != 'NOW-FULL'
    else:
        E = json.load(open(os.path.join(HERE, 'PROPOSAL-%s.json' % name), encoding='utf-8'))
        sidebar = True
    out = []
    for e in E:
        shown = ts.shown(e['heading'], e['level'])[1] if sidebar else e['heading']
        out.append({'id': e['id'], 'level': e['level'], 'label': norm(shown), 'full': norm(e['heading'])})
    return out


def parents(C):
    up, stack = {}, []
    for e in C:
        while stack and stack[-1]['level'] >= e['level']:
            stack.pop()
        up[e['id']] = stack[-1]['id'] if stack else None
        stack.append(e)
    return up


def match(text, C):
    t = norm(text)
    if not t or t in ('n/a', 'na', '-', 'none'):
        return None
    for key in ('label', 'full'):
        for e in C:
            if e[key] == t:
                return e['id']
    for e in C:   # a reader who typed the start of a cut-off label
        if e['label'].startswith(t) or t.startswith(e['label']):
            return e['id']
    best = difflib.get_close_matches(t, [e['label'] for e in C], n=1, cutoff=0.6)
    return next((e['id'] for e in C if best and e['label'] == best[0]), None)


def rows(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) >= 3 and re.fullmatch(r'\d+', cells[0]):
            out[cells[0]] = {'first': cells[1], 'sure': cells[2].lower().startswith('sure'), 'next': cells[3] if len(cells) > 3 else ''}
    return out


def main(key='EXPECTED-REVIEWED.json'):
    if not os.path.exists(os.path.join(HERE, key)):
        key = 'EXPECTED.json'
    X = json.load(open(os.path.join(HERE, key), encoding='utf-8'))['situations']
    scores = {'key': key, 'reads': {}}
    for path in sorted(glob.glob(os.path.join(HERE, 'reads', 'READ-*.md'))):
        name = re.match(r'READ-(.+)-(\d+)\.md$', os.path.basename(path))
        C = contents(name.group(1))
        up = parents(C)
        R = rows(path)
        tally = {'right': 0, 'near': 0, 'wrong': 0, 'missing': 0, 'guess': 0, 'found': 0, 'unmatched': []}
        per = {}
        for n, want in X.items():
            ok = set(want['right']) | set(want.get('also', []))
            r = R.get(n)
            if not r:
                tally['missing'] += 1
                per[n] = 'missing'
                continue
            first = match(r['first'], C)
            nxt = match(r['next'], C)
            if first is None:
                tally['unmatched'].append(r['first'])
            kind = 'right' if first in ok else 'near' if first and any(up.get(i) == first for i in ok) else 'wrong'
            tally[kind] += 1
            tally['guess'] += 0 if r['sure'] else 1
            tally['found'] += 1 if kind == 'right' or nxt in ok else 0
            per[n] = {'first': first, 'next': nxt, 'kind': kind, 'sure': r['sure']}
        scores['reads'][os.path.basename(path)] = {'tally': tally, 'per': per}
    json.dump(scores, open(os.path.join(HERE, 'SCORES.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('key: %s, %d situations' % (key, len(X)))
    print('%-28s %6s %5s %6s %6s %6s' % ('read', 'right', 'near', 'wrong', 'guess', 'found'))
    for f, s in scores['reads'].items():
        t = s['tally']
        print('%-28s %6d %5d %6d %6d %6d%s' % (f, t['right'], t['near'], t['wrong'], t['guess'], t['found'],
                                                '  unmatched: %s' % t['unmatched'] if t['unmatched'] else ''))


if __name__ == '__main__':
    main(*sys.argv[1:])
