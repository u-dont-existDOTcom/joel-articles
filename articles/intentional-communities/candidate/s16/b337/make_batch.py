"""Batch 337g (2026-10-17): screens (E175) of section 16 draft v6 (../make_v6.py: H1-P2 numbered inline, H2-P5 from round b's
call B, H3-P4 from call A, H3-P5 opening with a question). Each changed paragraph with each neighbor in its subsection (H2-P5
alone too: 50 words or more), each subsection with its heading, and the whole section. Marches: review-r11 (two readings) for
the changed paragraphs, the rest as in 333g. Run from candidate/: python3 s16/b337/make_batch.py"""
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
            'review-r10', 'review-r11'):
    L = labels(S16 / rnd)
    for n, p in enumerate(json.loads((S16 / rnd / 'march-ids.json').read_text()), start=1):
        if p.startswith('s15-'):
            continue
        MARCH[p[4:] if p.startswith('s16-') else p] = [m[n] for m in L]
MARCH['H1-P1'] = MARCH['H1-P1a']
MARCH['H2-P3'] = MARCH['H2-P3a']
subprocess.run([sys.executable, str(S16 / 'make_v6.py')], check=True, capture_output=True)
bl = [b.strip() for b in re.split(r'\n\s*\n', (S16 / 'v6.md').read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in bl if not SKIP.match(b)]
prose = [b for b in reader if not b.startswith('[caption]')]
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
def add(key, parts):
    drafts[key] = '\n\n'.join(plain(T[p].lstrip('#').strip()) if p in ('H1', 'H2', 'H3') else plain(T[p]) for p in parts)
    ps = [p for p in parts if p in MARCH]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in MARCH[p]], 'march_note': 's16/review-r11; the rest as in 333g',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])


SUB = {h: [h] + [p for p in PARAS if p.startswith(h + '-')] for h in ('H1', 'H2', 'H3')}
add('S16v6-H1-P1+P2', ['H1-P1', 'H1-P2'])
add('S16v6-H1-P2+P3', ['H1-P2', 'H1-P3'])
add('S16v6-H1', SUB['H1'])
add('S16v6-H2-P4+P5', ['H2-P4', 'H2-P5'])
add('S16v6-H2-P5', ['H2-P5'])
add('S16v6-H2-P5+P6', ['H2-P5', 'H2-P6'])
add('S16v6-H2', SUB['H2'])
add('S16v6-H3-P3+P4', ['H3-P3', 'H3-P4'])
add('S16v6-H3-P4+P5', ['H3-P4', 'H3-P5'])
add('S16v6-H3-P5+P6', ['H3-P5', 'H3-P6'])
add('S16v6-H3', SUB['H3'])
drafts['S16v6'] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b).lstrip('#').strip()) for b in reader)
gate['S16v6'] = {'kind': 'screen', 'march': [x for p in PARAS for x in MARCH[p]], 'march_note': 'every paragraph',
                 'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))), 'words': len(drafts['S16v6'].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b337.js'), '--name', 'B337'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b337-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
