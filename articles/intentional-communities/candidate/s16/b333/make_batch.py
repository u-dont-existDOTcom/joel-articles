"""Batch 333g (2026-10-17): screens (E175) of section 16 draft v5 (../make_v5.py: the paragraphs that read AI in 328g rebuilt
from Emulate round b with the published meaning put back; H1-P1 and H2-P3 in two shapes each; H2-P3 b had no break in the first march reading, so only a goes). Each changed paragraph with
its neighbor in its subsection (each is under 50 words), once for each shape; each subsection with its heading; the whole
section with the a shapes and with the b shapes. Marches: review-r8 (two readings) for the changed paragraphs, the rest as in
328g. Run from candidate/: python3 s16/b333/make_batch.py"""
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
for rnd in ('review-r3', 'review-r3b', 'review-r3c', 'review-r3d', 'review-r5', 'review-r6', 'review-r8', 'review-r9', 'review-r10'):
    L = labels(S16 / rnd)
    for n, p in enumerate(json.loads((S16 / rnd / 'march-ids.json').read_text()), start=1):
        if p.startswith('s15-'):
            continue
        MARCH[p[4:] if p.startswith('s16-') else p] = [m[n] for m in L]


def blocks(c1, c3):
    subprocess.run([sys.executable, str(S16 / 'make_v5.py'), c1, c3], check=True, capture_output=True)
    bl = [b.strip() for b in re.split(r'\n\s*\n', (S16 / 'v5.md').read_text(encoding='utf-8')) if b.strip()]
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
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in M[p]], 'march_note': 's16/review-r8; the rest as in 328g',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])


SUB = {h: [h] + [p for p in PARAS if p.startswith(h + '-')] for h in ('H1', 'H2', 'H3')}
for v in ('a', 'b'):
    # H2-P3 b had no break in review-r8's first reading, so only a goes (with each H1-P1)
    reader, T = blocks(v, 'a')
    M = dict(MARCH, **{'H1-P1': MARCH['H1-P1' + v], 'H2-P3': MARCH['H2-P3a']})
    add('S16v5-H1-P1%s+P2' % v, ['H1-P1', 'H1-P2'], T, M)
    add('S16v5%s-H1' % v, SUB['H1'], T, M)
    if v == 'a':
        add('S16v5-H2-P2+P3a', ['H2-P2', 'H2-P3'], T, M)
        add('S16v5-H2-P3a+P4', ['H2-P3', 'H2-P4'], T, M)
        add('S16v5a-H2', SUB['H2'], T, M)
        add('S16v5-H2-P5+P6', ['H2-P5', 'H2-P6'], T, M)
        add('S16v5-H3-P3+P4', ['H3-P3', 'H3-P4'], T, M)
        add('S16v5-H3-P4+P5', ['H3-P4', 'H3-P5'], T, M)
        add('S16v5-H3-P5+P6', ['H3-P5', 'H3-P6'], T, M)
        add('S16v5-H3-P6+P7', ['H3-P6', 'H3-P7'], T, M)
        add('S16v5-H3', SUB['H3'], T, M)
    key = 'S16v5' + v
    drafts[key] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b).lstrip('#').strip()) for b in reader)
    gate[key] = {'kind': 'screen', 'march': [x for p in PARAS for x in M[p]], 'march_note': 'every paragraph',
                 'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))), 'words': len(drafts[key].split())}
subprocess.run([sys.executable, str(S16 / 'make_v5.py'), 'a', 'a'], check=True, capture_output=True)
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b333.js'), '--name', 'B333'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b333-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
