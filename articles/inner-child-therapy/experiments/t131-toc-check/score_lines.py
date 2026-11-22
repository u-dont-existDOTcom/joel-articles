#!/usr/bin/env python3
"""Score the turn-131 readers. Each read (reads/READ-<CONTENTS>-<n>.txt) is the reader's reply as it came back:
rows "situation number | first line number | sure or guess | next line number" over the mixed list of 68 situations.

  python3 score_lines.py        # writes SCORES.json and SUMMARY.json, prints the table

A line number is turned into the section id of that contents (make_reader_files.py numbers the lines), so a renamed
section counts by its id. A first pick is "right" when its section is one of the situation's right or also sections,
"near" when it is a heading those sections sit under, "wrong" otherwise. "Mo' Money, Mo' Problems" (S051) is an h5, which the sidebar
doesn't list, so its listed parent (S050, Ask God for a Loan) stands in for it.

Three keys: the 38 turn-130 situations under the frozen turn-130 key (old-frozen) and under that key plus the checker's
additions (old-reviewed), and the 30 held-out situations (held).
"""
import glob, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
import make_reader_files as mk

UNLISTED_PARENT = {'S051': 'S050'}
MIXED = {s['n']: s['key'] for s in json.load(open(os.path.join(HERE, 'SITUATIONS-MIXED.json')))}
FROZEN = json.load(open(os.path.join(HERE, '..', 't130-toc', 'EXPECTED.json')))['situations']
REVIEWED = json.load(open(os.path.join(HERE, 'EXPECTED-REVIEWED.json')))['situations']
HELD = {str(h['n']): h for h in json.load(open(os.path.join(HERE, 'SITUATIONS-HELDOUT.json')))['situations']}

def ok_sets(key):
    """key 'A12' or 'B7' -> {keyname: set of right ids}"""
    k = key[1:]
    if key[0] == 'A':
        fr = {i for i, _ in FROZEN[k]['right']} | {i for i, _ in FROZEN[k]['also']}
        rv = set(REVIEWED[k]['right']) | set(REVIEWED[k]['also']) | {a['id'] for a in REVIEWED[k]['added']}
        out = {'old-frozen': fr, 'old-reviewed': rv}
    else:
        out = {'held': set(HELD[k]['right']) | set(HELD[k]['also'])}
    return {name: ids | {UNLISTED_PARENT[i] for i in ids if i in UNLISTED_PARENT} for name, ids in out.items()}

def contents(name):
    rows = mk.lines(mk.CONTENTS[name])
    byline = {n: sid for n, sid, _, _ in rows}
    anc, stack = {}, []
    for n, sid, lvl, _ in rows:
        while stack and stack[-1][1] >= lvl:
            stack.pop()
        anc[sid] = [s for s, _ in stack]
        stack.append((sid, lvl))
    return byline, anc

def parse(path):
    out, notes = {}, []
    for line in open(path, encoding='utf-8'):
        line = line.strip().strip('`')
        if line.upper().startswith('NOTE'):
            notes.append(line)
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) >= 3 and cells[0].isdigit():
            first = re.match(r'\d+', cells[1])
            nxt = re.match(r'\d+', cells[3]) if len(cells) > 3 else None
            out[int(cells[0])] = {'first': int(first.group()) if first else None, 'sure': cells[2].lower().startswith('sure'),
                                  'next': int(nxt.group()) if nxt else None}
    return out, notes

def judge(sid, ok, anc):
    if sid is None:
        return 'none'
    if sid in ok:
        return 'right'
    if any(sid in anc.get(i, []) for i in ok):
        return 'near'
    return 'wrong'

def score(path):
    name = os.path.basename(path)[5:-4]
    variant = re.sub(r'-\d+$', '', name)
    byline, anc = contents(variant)
    R, notes = parse(path)
    per, tot = {}, {}
    for n, key in sorted(MIXED.items()):
        r = R.get(n, {'first': None, 'sure': False, 'next': None})
        f, x = byline.get(r['first']), byline.get(r['next'])
        for kname, ok in ok_sets(key).items():
            jf, jx = judge(f, ok, anc), judge(x, ok, anc)
            t = tot.setdefault(kname, {'situations': 0, 'right': 0, 'near': 0, 'wrong': 0, 'none': 0, 'guesses': 0, 'found_by_2nd': 0, 'sure_but_not_right': 0})
            t['situations'] += 1
            t[jf] += 1
            t['guesses'] += (not r['sure'])
            t['found_by_2nd'] += (jf == 'right' or jx == 'right')
            t['sure_but_not_right'] += (r['sure'] and jf != 'right')
            per.setdefault(key, {'mixed_n': n, 'first_line': r['first'], 'first_id': f, 'sure': r['sure'], 'next_line': r['next'], 'next_id': x})[kname] = {'first_is': jf, 'next_is': jx}
    return name, variant, tot, per, notes, len(R)

if __name__ == '__main__':
    out = {}
    for p in sorted(glob.glob(os.path.join(HERE, 'reads', 'READ-*.txt'))):
        name, variant, tot, per, notes, rows = score(p)
        out[name] = {'contents': variant, 'rows': rows, 'totals': tot, 'situations': per, 'notes': notes}
    json.dump(out, open(os.path.join(HERE, 'SCORES.json'), 'w'), ensure_ascii=False, indent=1)
    summary = {}
    for name, v in out.items():
        s = summary.setdefault(v['contents'], {'readers': 0})
        s['readers'] += 1
        for kname, t in v['totals'].items():
            for m in ('right', 'near', 'guesses', 'found_by_2nd', 'sure_but_not_right'):
                s.setdefault(kname, {}).setdefault(m, []).append(t[m])
            s[kname]['of'] = t['situations']
    json.dump(summary, open(os.path.join(HERE, 'SUMMARY.json'), 'w'), ensure_ascii=False, indent=1)
    for c, s in summary.items():
        print(f"{c:6} readers {s['readers']}")
        for kname in ('old-frozen', 'old-reviewed', 'held'):
            if kname in s:
                t = s[kname]
                print(f"   {kname:13} right {t['right']} of {t['of']}   by 2nd {t['found_by_2nd']}   guesses {t['guesses']}   sure-but-not-right {t['sure_but_not_right']}")
