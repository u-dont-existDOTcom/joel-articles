#!/usr/bin/env python3
"""Score the fresh readers' answers against EXPECTED.json, by section id.

  python3 score_reads.py            # reads reads/READ-*.md, writes SCORES.json, prints the table

Each read names the contents it saw (its file name: READ-NOW-SIDEBAR-1.md, READ-B-2.md, ...); its part 1 table gives,
per situation, the first heading and the next one. A heading is matched to its section in that contents (as the
sidebar showed it, cut-off "…" included), so a renamed or moved section counts by its id. A first pick is "right"
when its section is one of the situation's right or also sections, "near" when it is the part or parent heading they
sit in, and "wrong" otherwise; "found" counts a right first or next pick.
"""
import difflib, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

CONTENTS = {'NOW-SIDEBAR': ('LIVE-TOC.json', True), 'NOW-FULL': ('LIVE-TOC.json', False),
            'B': ('PROPOSAL-B.json', True), 'B2': ('PROPOSAL-B2.json', True), 'C': ('PROPOSAL-C.json', True)}
EXP = json.load(open(os.path.join(HERE, 'EXPECTED.json')))['situations']
_EMO = re.compile('[☀-➿\U0001F000-\U0001FAFF️‍\U0001F3FB-\U0001F3FF]')

def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = _EMO.sub('', s)
    s = re.sub(r'[`*#]', '', s).strip()
    s = re.sub(r'(…|\.\.\.)\s*$', '', s)
    s = s.strip(' "\'').lower()
    return re.sub(r'\s+', ' ', s).strip()

def load(name):
    f, sidebar = CONTENTS[name]
    E = [e for e in json.load(open(os.path.join(HERE, f))) if not e.get('drop')]
    for i, e in enumerate(E):
        e['shown_n'] = norm(ts.shown(e['heading'], e['level'])[1] if sidebar else e['heading'])
        e['full_n'] = norm(e['heading'])
        anc, stack = [], []
        for p in E[:i]:
            pass
    # ancestors
    stack = []
    for e in E:
        while stack and stack[-1]['level'] >= e['level']:
            stack.pop()
        e['ancestors'] = [p['id'] for p in stack]
        stack.append(e)
    return E

def match(text, E):
    t = norm(text)
    if not t or t in ('-', '—'):
        return None
    for key in ('shown_n', 'full_n'):
        hits = [e for e in E if e[key] == t]
        if len(hits) == 1:
            return hits[0]
    if len(t) >= 8:
        hits = [e for e in E if e['full_n'].startswith(t) or (len(e['shown_n']) >= 8 and t.startswith(e['shown_n']))]
        if len(hits) == 1:
            return hits[0]
    best = max(E, key=lambda e: max(difflib.SequenceMatcher(a=t, b=e['shown_n']).ratio(), difflib.SequenceMatcher(a=t, b=e['full_n']).ratio()))
    r = max(difflib.SequenceMatcher(a=t, b=best['shown_n']).ratio(), difflib.SequenceMatcher(a=t, b=best['full_n']).ratio())
    return best if r >= 0.6 else None

def rows(path):
    out = {}
    for line in open(path, encoding='utf-8'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) >= 3 and cells[0].isdigit():
            out[int(cells[0])] = {'first': cells[1], 'sure': cells[2].lower(), 'next': cells[3] if len(cells) > 3 else ''}
    return out

def judge(e, sit, E):
    if e is None:
        return 'unmatched'
    ok = {i for i, _ in EXP[sit]['right']} | {i for i, _ in EXP[sit]['also']}
    if e['id'] in ok:
        return 'right'
    byid = {x['id']: x for x in E}
    if any(e['id'] in byid[i]['ancestors'] for i in ok if i in byid):
        return 'near'
    return 'wrong'

def score(path):
    name = os.path.basename(path)[5:-3]
    variant = re.sub(r'-\d+$', '', name)
    E = load(variant)
    R = rows(path)
    per = {}
    for k in sorted(EXP, key=int):
        r = R.get(int(k), {'first': '', 'sure': '', 'next': ''})
        f, n = match(r['first'], E), match(r['next'], E)
        jf, jn = judge(f, k, E), judge(n, k, E) if r['next'] else None
        per[k] = {'first': r['first'], 'first_id': f and f['id'], 'first_is': jf, 'sure': 'sure' in r['sure'],
                  'next': r['next'], 'next_id': n and n['id'], 'next_is': jn}
    v = per.values()
    tot = {'right': sum(x['first_is'] == 'right' for x in v), 'near': sum(x['first_is'] == 'near' for x in v),
           'wrong': sum(x['first_is'] in ('wrong', 'unmatched') for x in v), 'guesses': sum(not x['sure'] for x in v),
           'sure_but_wrong': sum(x['sure'] and x['first_is'] != 'right' for x in v),
           'found': sum(x['first_is'] == 'right' or x['next_is'] == 'right' for x in v),
           'unmatched': sum(x['first_is'] == 'unmatched' for x in v), 'situations': len(per)}
    return name, variant, tot, per

if __name__ == '__main__':
    out = {}
    for p in sorted(glob.glob(os.path.join(HERE, 'reads', 'READ-*.md'))):
        name, variant, tot, per = score(p)
        out[name] = {'contents': variant, 'totals': tot, 'situations': per}
        print(f"{name:18} right {tot['right']:2}  near {tot['near']:2}  wrong {tot['wrong']:2}  guesses {tot['guesses']:2}  sure-but-not-right {tot['sure_but_wrong']:2}  found by 2nd pick {tot['found']:2}/{tot['situations']}  unmatched {tot['unmatched']}")
    json.dump(out, open(os.path.join(HERE, 'SCORES.json'), 'w'), ensure_ascii=False, indent=1)
