"""Batch 308g (2026-10-16): screens of section 13 draft v28 (E175). v28 (../make_v28.py) is v27 with the sentences I had
rebuilt from the published wording taken back to Emulate round j's, and only the lost meaning put in (b307/PREDICTIONS.md: the
pair H5-P3 with H5-P4 read 0.99 AI, and the section's AI windows ended on rebuilt sentences).

Screens: the whole section first, and the groups 307g read AI or that v28 changed most. Marches: review-r19's third read
(MARCH-labels-3a/3b: the first, second and last subsections of v28, read in their subsections) and b304's records for the land
and visitor subsections, unchanged since v26. Run from candidate/: python3 s13/b308/make_batch.py"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
S13 = C / 's13'
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
HEADS = {0: 'H1', 5: 'H2', 11: 'H3', 17: 'H4', 27: 'H5'}
bl = [b.strip() for b in re.split(r'\n\s*\n', (S13 / 'v28.md').read_text(encoding='utf-8')) if b.strip()]
assert len(bl) == len(IDS)
TEXT = {(p or HEADS[i]): b for i, (p, b) in enumerate(zip(IDS, bl))}


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


R19_3 = [labels(S13 / 'review-r19' / ('MARCH-labels-3%s.txt' % x)) for x in 'ab']
R19_ORDER = ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
for r in R19_3:
    assert sorted(r) == list(range(1, len(R19_ORDER) + 1)), sorted(r)
MARCH = {p: [r[n] for r in R19_3] for n, p in enumerate(R19_ORDER, start=1)}
g304 = json.loads((S13 / 'b304' / 'GATE.json').read_text(encoding='utf-8'))
for key, sub in (('S13v26-H3', ['H3-P%d' % i for i in range(1, 6)]), ('S13v26-H4', ['H4-P%d' % i for i in range(1, 10)])):
    m = g304[key]['march']
    assert len(m) == 2 * len(sub)
    for i, p in enumerate(sub):
        MARCH[p] = m[2 * i:2 * i + 2]
for p in MARCH:
    assert p in TEXT
SUB = {'H1': ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], 'H2': ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       'H5': ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']}
ITEMS = {
 'S13v28': [(p or HEADS[i]) for i, p in enumerate(IDS)],
 'S13v28-H1': ['H1'] + SUB['H1'],
 'S13v28-J1': ['H1-P3', 'H1-P4', 'H2'] + SUB['H2'],
 'S13v28-H2': ['H2'] + SUB['H2'],
 'S13v28-5P3P4': ['H5-P3', 'H5-P4'],
 'S13v28-H5': ['H5'] + SUB['H5'],
}


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
for key, parts in ITEMS.items():
    md = [TEXT[p] for p in parts]
    drafts[key] = '\n\n'.join(plain(x) for x in md)
    ps = [p for p in parts if p in MARCH]
    gate[key] = {'kind': 'screen', 'march': [m for p in ps for m in MARCH[p]],
                 'march_note': '; '.join('%s: %s %s' % (p, 'r19 (third read)' if p in R19_ORDER else 'b304', MARCH[p]) for p in ps),
                 'lint': lint('\n\n'.join(x for x in md if not x.startswith('#'))),
                 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, key
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b308.js'), '--name', 'B308'] + list(ITEMS), capture_output=True, text=True)
print(r.stdout[-3000:], r.stderr[-1500:])
for k, g in gate.items():
    print('%-16s %4d words  lint %-6s  march %s' % (k, g['words'], g['lint'], ' | '.join(g['march'][:4]) + (' ...' if len(g['march']) > 4 else '')))
