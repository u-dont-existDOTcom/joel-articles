#!/usr/bin/env python3
"""Score outlines of the 4 November guide (N001..N148) against Joel's own reorganization (HIS-OUTLINE.json).

  python3 score_order.py OUT1.json [OUT2.json ...]

For each unit: its parent is the nearest unit above it with a lower level, new headings skipped (so a grouping heading a
model adds doesn't count against it); a merged unit's parent is the unit it joined. Measures, against his version:
  re-parented: of the units he gave a new parent, how many the outline gives the same new parent (and how many it put
               somewhere else); extra: units the outline re-parents that he left with their 4 November parent;
  levels:      of the units whose level he changed, how many get his level; extra level changes;
  order:       Kendall's tau between the outline's order and his, over units placed in both;
  same place:  units with his parent and his preceding unit."""
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
N = json.load(open(os.path.join(HERE, 'NOV4-SECTIONS.json')))
BASE = {'outline': [{'id': f"N{s['n']:03d}", 'level': s['level']} for s in N[1:]]}
HIS = json.load(open(os.path.join(HERE, 'HIS-OUTLINE.json')))

def parse(d):
    seq, lev, par, prev, merged, dropped = [], {}, {}, {}, {}, set()
    stack = []          # (level, id) of existing units
    last = None
    for e in d['outline']:
        if 'new' in e:
            continue
        i = e['id']
        if 'merge_into' in e:
            merged[i] = e['merge_into']; continue
        if e.get('drop'):
            dropped.add(i); continue
        L = e['level']
        while stack and stack[-1][0] >= L:
            stack.pop()
        par[i] = stack[-1][1] if stack else None
        prev[i] = last; last = i
        stack.append((L, i)); lev[i] = L; seq.append(i)
    for i, j in merged.items():
        par[i] = j
    return {'seq': seq, 'lev': lev, 'par': par, 'prev': prev, 'merged': merged, 'dropped': dropped}

def tau(a, b):
    common = [x for x in a if x in set(b)]
    pos = {x: k for k, x in enumerate(b)}
    r = [pos[x] for x in common]
    n = len(r); conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            if r[i] < r[j]: conc += 1
            else: disc += 1
    return (conc - disc) / max(1, conc + disc)

def score(d, base=BASE, his=HIS):
    B, H, M = parse(base), parse(his), parse(d)
    units = [f"N{k:03d}" for k in range(1, 149)]
    R = [u for u in units if u in H['par'] and H['par'].get(u) != B['par'].get(u)]
    got = [u for u in R if M['par'].get(u) == H['par'].get(u)]
    moved_elsewhere = [u for u in R if M['par'].get(u) not in (H['par'].get(u), B['par'].get(u))]
    extra = [u for u in units if u not in R and u in M['par'] and M['par'].get(u) != B['par'].get(u) and M['par'].get(u) != H['par'].get(u)]
    Lc = [u for u in units if u in H['lev'] and u in B['lev'] and H['lev'][u] != B['lev'][u]]
    lgot = [u for u in Lc if M['lev'].get(u) == H['lev'][u]]
    lextra = [u for u in units if u not in Lc and u in M['lev'] and u in B['lev'] and M['lev'][u] != B['lev'][u]]
    same = [u for u in units if u in H['par'] and M['par'].get(u) == H['par'].get(u) and M['prev'].get(u) == H['prev'].get(u)]
    return {'reparented_his': len(R), 'reparented_same': len(got), 'reparented_elsewhere': len(moved_elsewhere),
            'reparented_extra': len(extra), 'levels_his': len(Lc), 'levels_same': len(lgot), 'levels_extra': len(lextra),
            'tau_vs_his': round(tau(M['seq'], H['seq']), 3), 'same_place': len(same), 'units': len(H['par']),
            'got': got, 'extra': extra, 'merges': M['merged']}

if __name__ == '__main__':
    print('baseline (4 November, unchanged):', {k: v for k, v in score(BASE).items() if k not in ('got', 'extra', 'merges')})
    for p in sys.argv[1:]:
        s = score(json.load(open(p)))
        print(os.path.basename(p), {k: v for k, v in s.items() if k not in ('got', 'extra')})
