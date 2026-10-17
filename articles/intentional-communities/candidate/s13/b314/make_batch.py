"""Batch 314g (2026-10-17): screens (E175) of section 13 draft v32 (section 14 v6 went in 313g), from Joel's message of
2026-10-16 23:38 UTC. Section 13 v32 (../make_v32.py): his "if the community uses them" back, the short visit's punchline
fixed (the one paragraph that read AI alone in 312g), the book line pointing to the book for its nuts and bolts instead of
its order, and the dedup. Section 14 v6 (../../s14/make_v6.py): the dedup. Every changed paragraph alone (under 50 words by
spaces, with a neighbor), the subsections holding them, and both sections whole. Marches: review-r21 (s13) and review-r6
(s14), two readings each, every paragraph read in its section. Run from candidate/: python3 s13/b314/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
HEADS = {0: 'H1', 5: 'H2', 11: 'H3', 17: 'H4', 27: 'H5'}
bl = [b.strip() for b in re.split(r'\n\s*\n', (C / 's13' / 'v32.md').read_text(encoding='utf-8')) if b.strip()]
assert len(bl) == len(IDS)
T13 = {(p or HEADS[i]): b for i, (p, b) in enumerate(zip(IDS, bl))}
PARAS13 = [p for p in IDS if p]


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


M13 = [labels(C / 's13' / 'review-r21' / ('MARCH-labels-2%s.txt' % x)) for x in 'ab']
for m in M13:
    assert sorted(m) == list(range(1, len(PARAS13) + 1)), sorted(m)
MARCH = {p: [m[n] for m in M13] for n, p in enumerate(PARAS13, start=1)}
s14 = [b.strip() for b in re.split(r'\n\s*\n', (C / 's14' / 'v6.md').read_text(encoding='utf-8')) if b.strip()]
s14 = [b for b in s14 if not b.startswith('[image')]
assert s14[0] == '# Dissolution and Exit' and len(s14) == 7
K14 = ['S14H', 'S14-P1', 'S14-P2', 'S14-P3', 'S14-P4', 'S14-P5', 'S14-P6']
T = dict(T13, **dict(zip(K14, s14)))
M14 = [labels(C / 's14' / 'review-r6' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
for m in M14:
    assert sorted(m) == list(range(1, 7)), sorted(m)
MARCH.update({K14[n]: [m[n] for m in M14] for n in range(1, 7)})
SUB = {'H1': ['H1', 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'],
       'H3': ['H3', 'H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'],
       'H4': ['H4'] + ['H4-P%d' % i for i in range(1, 10)]}
ITEMS = {
    'S13v32-H1-P4': ['H1-P4'], 'S13v32-H3-P3': ['H3-P3'], 'S13v32-H3-P4': ['H3-P4'], 'S13v32-H3-P4+P5': ['H3-P4', 'H3-P5'],
    'S13v32-H4-P1': ['H4-P1'], 'S13v32-H4-P2+P3': ['H4-P2', 'H4-P3'], 'S13v32-H4-P3+P4': ['H4-P3', 'H4-P4'],
    'S13v32-H4-P4': ['H4-P4'], 'S13v32-H1': SUB['H1'], 'S13v32-H3': SUB['H3'], 'S13v32-H4': SUB['H4'],
    'S13v32': [(p or HEADS[i]) for i, p in enumerate(IDS)],
}


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
for key, parts in ITEMS.items():
    drafts[key] = '\n\n'.join(plain(T[p]) for p in parts)
    ps = [p for p in parts if p in MARCH]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in MARCH[p]],
                 'march_note': ('s13/review-r21' if key.startswith('S13') else 's14/review-r6') + '/MARCH-labels-a.txt, -b.txt (s14); s13: review-r21/MARCH-labels-2a.txt, -2b.txt',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b314.js'), '--name', 'B314'] + list(ITEMS), capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b314-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), {k: g['words'] for k, g in gate.items()})
