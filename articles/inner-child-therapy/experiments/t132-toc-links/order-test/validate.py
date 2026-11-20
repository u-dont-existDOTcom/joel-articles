#!/usr/bin/env python3
"""Check an outline answer: every id N001..N148 exactly once, valid fields. Prints OK or the problems."""
import json, sys
p = sys.argv[1]
try:
    d = json.load(open(p))
except Exception as e:
    print('JSON does not parse:', e); sys.exit(1)
out = d.get('outline')
if not isinstance(out, list):
    print('no "outline" list'); sys.exit(1)
seen, prob = {}, []
want = {f"N{i:03d}" for i in range(1, 149)}
for k, e in enumerate(out):
    if not isinstance(e, dict):
        prob.append(f'entry {k} is not an object'); continue
    if 'new' in e:
        if not isinstance(e.get('level'), int) or not 1 <= e['level'] <= 5:
            prob.append(f'entry {k}: new heading needs level 1-5')
        continue
    i = e.get('id')
    if i not in want:
        prob.append(f'entry {k}: unknown id {i!r}'); continue
    seen[i] = seen.get(i, 0) + 1
    if 'merge_into' in e:
        if e['merge_into'] not in want or e['merge_into'] == i: prob.append(f'{i}: bad merge_into')
    elif e.get('drop'):
        pass
    elif not isinstance(e.get('level'), int) or not 1 <= e['level'] <= 5:
        prob.append(f'{i}: needs level 1-5')
miss = sorted(want - set(seen)); dup = sorted(i for i, c in seen.items() if c > 1)
if miss: prob.append('missing ids: ' + ' '.join(miss))
if dup: prob.append('ids more than once: ' + ' '.join(dup))
print('OK' if not prob else '\n'.join(prob))
sys.exit(0 if not prob else 1)
