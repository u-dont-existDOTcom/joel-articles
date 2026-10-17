"""Batch 332g (2026-10-17): screens (E175) of section 15 draft v10 (../make_v10.py: H1-P4 in three shapes from Emulate round e,
q, u and v, each with the published "often"; ../make_v9.py: H3-P2 with the published "any" and "long-term" back). H1-P4 alone
and inside H1, once for each shape; H3-P2 alone and inside H3; the whole section with each shape. Marches: s16/review-r8 (two
readings) for H1-P4 q, u and v and H3-P2; the rest as in 330g (../b330/make_batch.py).
Run from candidate/: python3 s15/b332/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S15 = C / 's15'
S16 = C / 's16'
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video)')
IDS = ['H1'] + ['H1-P%d' % i for i in range(1, 6)] + ['H2'] + ['H2-P%d' % i for i in range(1, 8)] + ['H3'] + ['H3-P%d' % i for i in range(1, 9)]
PARAS = [i for i in IDS if '-' in i]


def blocks(name):
    bl = [b.strip() for b in re.split(r'\n\s*\n', (S15 / (name + '.md')).read_text(encoding='utf-8')) if b.strip()]
    reader = [b for b in bl if not SKIP.match(b)]
    prose = [b for b in reader if not b.startswith('[caption]')]
    assert len(prose) == len(IDS)
    return reader, dict(zip(IDS, prose))


def labels(folder):
    return [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
             (folder / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']


MARCH = {}
def take(folder, mapping):
    L = labels(folder)
    for p, n in mapping.items():
        MARCH[p] = [m[n] for m in L]
take(S15 / 'review-r2d', {'H1-P2': 2, 'H1-P3': 3})
take(S15 / 'review-r2', {'H2-P5': 10, 'H3-P6': 18})
take(S15 / 'review-r3', {'H2-P6': 6})
take(S15 / 'review-r4b', {'H2-P1': 2})
take(S15 / 'review-r5', {p: n for n, p in enumerate(json.loads((S15 / 'review-r5' / 'march-ids.json').read_text()), start=1)})
for rnd in ('review-r5', 'review-r6', 'review-r8'):
    ids = json.loads((S16 / rnd / 'march-ids.json').read_text())
    take(S16 / rnd, {p[4:]: n for n, p in enumerate(ids, start=1) if p.startswith('s15-')})
VAR = json.loads((S15 / 'v10-variants.json').read_text(encoding='utf-8'))['H1-P4']


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
def add(key, parts, T, M):
    drafts[key] = '\n\n'.join(plain(T[p].lstrip('#').strip()) if p in ('H1', 'H2', 'H3') else plain(T[p]) for p in parts)
    ps = [p for p in parts if p in M]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in M[p]], 'march_note': 's16/review-r8; the rest as in 330g',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])


SUB = {h: [h] + [p for p in PARAS if p.startswith(h + '-')] for h in ('H1', 'H2', 'H3')}
for v in ('q', 'u', 'v'):
    subprocess.run([sys.executable, str(S15 / 'make_v10.py'), v], check=True, capture_output=True)
    reader, T = blocks('v10')
    M = dict(MARCH, **{'H1-P4': MARCH['H1-P4' + v]})
    assert T['H1-P4'] == VAR[v]
    add('S15v10-H1-P4' + v, ['H1-P4'], T, M)
    add('S15v10%s-H1' % v, SUB['H1'], T, M)
    if v == 'q':
        add('S15v10-H3-P2', ['H3-P2'], T, M)
        add('S15v10-H3', SUB['H3'], T, M)
    key = 'S15v10' + v
    drafts[key] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b)) for b in reader)
    gate[key] = {'kind': 'screen', 'march': [x for p in PARAS for x in M[p]], 'march_note': 'every paragraph',
                 'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))), 'words': len(drafts[key].split())}
subprocess.run([sys.executable, str(S15 / 'make_v10.py'), 'q'], check=True, capture_output=True)
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b332.js'), '--name', 'B332'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b332-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
