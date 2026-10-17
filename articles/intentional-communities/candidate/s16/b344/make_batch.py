"""Batch 344g (2026-10-17): screens (E175) of section 16 draft v10 (../make_v10.py: H1 rebuilt from Emulate round d's call D,
with H1-P2 from call D or call B; shapes dd, db and ed, the last with v8's H1-P1 e; H3 as v9's shape a). For each shape: H1-P1
with H1-P2, H1-P2 with H1-P3 (dd and db), H1 and the whole section; H1-P3 alone, once. Marches: review-r18 (two readings) for
the new paragraphs, the rest as in 342g. Run from candidate/: python3 s16/b344/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S16 = C / 's16'
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

SKIP = re.compile(r'^\[image \d+\]')
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
PARAS = [i for i in IDS if '-' in i]


def labels(folder):
    return [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
             (folder / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']


MARCH = {}
L = labels(S16 / 'review-r2')
for n, p in enumerate(json.loads((S16 / 'review-r2' / 'march-ids.json').read_text()), start=1):
    MARCH[p] = [m[n] for m in L]
for rnd in ('review-r3', 'review-r3b', 'review-r3c', 'review-r3d', 'review-r5', 'review-r6', 'review-r8', 'review-r9',
            'review-r10', 'review-r11', 'review-r12', 'review-r14', 'review-r15', 'review-r16', 'review-r17', 'review-r18'):
    L = labels(S16 / rnd)
    for n, p in enumerate(json.loads((S16 / rnd / 'march-ids.json').read_text()), start=1):
        if p.startswith('s15-'):
            continue
        if rnd == 'review-r11' and p == 's16-H1-P2':
            p = 's16-H1-P2num'  # v6's numbered H1-P2, not the plain one shape e keeps
        MARCH[p[4:] if p.startswith('s16-') else p] = [m[n] for m in L]
MARCH['H2-P3'] = MARCH['H2-P3a']
MARCH['H2-P5'] = MARCH['H2-P5d']  # trace r13 T1's fix in the shape the linter passes (../make_v8.py), review-r16
MARCH['H3-P4'] = MARCH['H3-P4x']
SHAPE = {'H1-P1': MARCH['H1-P1e'], 'H1-P2': MARCH['H1-P2']}


def blocks(shape):
    subprocess.run([sys.executable, str(S16 / 'make_v10.py'), shape], check=True, capture_output=True)
    bl = [b.strip() for b in re.split(r'\n\s*\n', (S16 / 'v10.md').read_text(encoding='utf-8')) if b.strip()]
    reader = [b for b in bl if not SKIP.match(b)]
    prose = [b for b in reader if not b.startswith('[caption]')]
    assert len(prose) == len(IDS)
    return reader, dict(zip(IDS, prose))


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
def add(key, parts, T, M):
    drafts[key] = '\n\n'.join(plain(T[p].lstrip('#').strip()) if p in ('H1', 'H2', 'H3') else plain(T[p]) for p in parts)
    ps = [p for p in parts if p in M]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in M[p]], 'march_note': 's16/review-r18; the rest as in 342g',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])


SUB = {h: [h] + [p for p in PARAS if p.startswith(h + '-')] for h in ('H1', 'H2', 'H3')}
SH = {'dd': ('H1-P1D', 'H1-P2D', 'H1-P3D'), 'db': ('H1-P1D', 'H1-P2B', 'H1-P3D'), 'ed': ('H1-P1e', 'H1-P2D', 'H1-P3D')}
for shape in ('dd', 'db', 'ed'):
    reader, T = blocks(shape)
    M = dict(MARCH)
    M['H1-P1'], M['H1-P2'], M['H1-P3'] = (MARCH[x] for x in SH[shape])
    M['H3-P6'] = MARCH['H3-P6a']
    add('S16v10%s-H1-P1+P2' % shape, ['H1-P1', 'H1-P2'], T, M)
    if shape != 'ed':
        add('S16v10%s-H1-P2+P3' % shape, ['H1-P2', 'H1-P3'], T, M)
    if shape == 'dd':
        add('S16v10-H1-P3', ['H1-P3'], T, M)
    add('S16v10%s-H1' % shape, SUB['H1'], T, M)
    key = 'S16v10' + shape
    drafts[key] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b).lstrip('#').strip()) for b in reader)
    gate[key] = {'kind': 'screen', 'march': [x for p in PARAS for x in M[p]], 'march_note': 'every paragraph',
                 'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))),
                 'words': len(drafts[key].split())}
subprocess.run([sys.executable, str(S16 / 'make_v10.py'), 'dd'], check=True, capture_output=True)
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b344.js'), '--name', 'B344'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b344-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
