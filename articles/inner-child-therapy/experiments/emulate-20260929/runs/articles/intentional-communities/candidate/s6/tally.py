"""Count my predictions against Pangram's verdicts in PREDICTIONS-s6.md (tables with mine and Pangram columns).
A prediction is right when its first word (Human, AI, Mixed) matches the verdict's first word; "Human overall, n% AI" counts as Mixed
(a window read AI), and rows with no verdict are skipped."""
import re, sys
rows = right = 0
per = {}
batch = None
for line in open('PREDICTIONS-s6.md', encoding='utf-8'):
    m = re.match(r'^(?:API )?batch (\d+)', line.strip(), re.I)
    if m: batch = int(m.group(1))
    if not line.startswith('| ') or line.startswith('| text') or line.startswith('|---'): continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells) < 4 or not cells[3] or cells[3].startswith('not '): continue
    mine, got = cells[1].replace('*', ''), cells[3].replace('*', '')
    g = 'Mixed' if got.startswith('Human overall') else got.split()[0].rstrip(':')
    m0 = mine.split()[0].rstrip(',:;') if mine else ''
    ok = m0 == g
    rows += 1; right += ok
    b = per.setdefault(batch, [0, 0]); b[0] += 1; b[1] += ok
print('rows', rows, 'right', right)
for b in sorted(k for k in per if k is not None): print(b, per[b])
