"""Batch 327g (2026-10-17): screens (E175) of section 15 draft v6's variants (../make_v6.py, ../v6-variants.json: H1-P4 a and
c, H3-P2 plain and l, from Emulate round d). Each variant alone and inside its subsection; the whole section twice (a with
plain, c with l). Marches: review-r6 for the variants (two readings); the rest as in 326g (../b326/make_batch.py).
Run from candidate/: python3 s15/b327/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S15 = C / 's15'
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


def labels(rnd):
    return [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
             (S15 / rnd / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']


MARCH = {}
def take(rnd, mapping):
    L = labels(rnd)
    for p, n in mapping.items():
        MARCH[p] = [m[n] for m in L]
take('review-r2d', {'H1-P2': 2, 'H1-P3': 3})
take('review-r2', {'H2-P5': 10, 'H3-P6': 18})
take('review-r3', {'H2-P6': 6})
take('review-r4b', {'H2-P1': 2})
take('review-r5', {p: n for n, p in enumerate(json.loads((S15 / 'review-r5' / 'march-ids.json').read_text()), start=1)})
r6 = json.loads((S15 / 'review-r6' / 'march-ids.json').read_text())
L6 = labels('review-r6')
M6 = {p: [m[n] for m in L6] for n, p in enumerate(r6, start=1)}
VAR = json.loads((S15 / 'v6-variants.json').read_text(encoding='utf-8'))


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
def add(key, parts, T, M):
    drafts[key] = '\n\n'.join(plain(T[p].lstrip('#').strip()) if p in ('H1', 'H2', 'H3') else plain(T[p]) for p in parts)
    ps = [p for p in parts if p in M]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in M[p]], 'march_note': 'variants review-r6; the rest as in 326g',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])


combos = {'S15v6': ('a', 'plain'), 'S15v6x': ('c', 'l')}
base_reader, base = blocks('v5')
for v in ('a', 'c'):
    T = dict(base, **{'H1-P4': VAR['H1-P4'][v]})
    M = dict(MARCH, **{'H1-P4': M6['H1-P4' + v]})
    add('S15v6-H1-P4' + v, ['H1-P4'], T, M)
    add('S15v6%s-H1' % v, [p for p in IDS if p == 'H1' or p.startswith('H1-')], T, M)
for v in ('plain', 'l'):
    T = dict(base, **{'H3-P2': VAR['H3-P2'][v]})
    M = dict(MARCH, **{'H3-P2': M6['H3-P2' + v]})
    add('S15v6-H3-P2' + v, ['H3-P2'], T, M)
    add('S15v6%s-H3' % v, [p for p in IDS if p == 'H3' or p.startswith('H3-')], T, M)
for key, (v4, v2) in combos.items():
    subprocess.run([sys.executable, str(S15 / 'make_v6.py'), v4, v2], check=True, capture_output=True)
    reader, T = blocks('v6')
    M = dict(MARCH, **{'H1-P4': M6['H1-P4' + v4], 'H3-P2': M6['H3-P2' + v2]})
    drafts[key] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b)) for b in reader)
    gate[key] = {'kind': 'screen', 'march': [x for p in PARAS for x in M[p]], 'march_note': 'every paragraph',
                 'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))), 'words': len(drafts[key].split())}
subprocess.run([sys.executable, str(S15 / 'make_v6.py'), 'a', 'plain'], check=True, capture_output=True)
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b327.js'), '--name', 'B327'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b327-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
