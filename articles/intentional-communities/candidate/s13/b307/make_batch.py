"""Batch 307g (2026-10-16): screens of section 13 draft v27 (E175: a screen goes to Pangram after the lint and the march, before
the meaning reviews). v27 (../make_v27.py) is v26 with the two stretches that read AI inside the whole section in 304g stage 2
rewritten from Emulate round j, each sent whole (Joel, 21:05 UTC: "34a and learn from how emulate fixes it"), and the meaning put
back inside Emulate's sentences (v27-fixes.json).

Screens: each new pair, each changed subsection whole, the first stretch as Emulate got it (H1-P3 through the values
subsection), the run from H4-P9 into the last subsection, and the whole section. Marches: review-r19 (the first, second and last
subsections, read in their subsections) and, for the land and visitor subsections, unchanged since v26, b304's records.
Run from candidate/: python3 s13/b307/make_batch.py"""
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
bl = [b.strip() for b in re.split(r'\n\s*\n', (S13 / 'v27.md').read_text(encoding='utf-8')) if b.strip()]
assert len(bl) == len(IDS)
TEXT = {(p or HEADS[i]): b for i, (p, b) in enumerate(zip(IDS, bl))}


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


# review-r19's first read (MARCH-labels-a/b) had all three changed subsections; it found no break in H1-P4 (both readings)
# and in H5-P3 (reading b), which v27 then fixed, so the first and last subsections were read again (MARCH-labels-2a/2b).
R19 = [labels(S13 / 'review-r19' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
R19_ORDER = ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
R19_2 = [labels(S13 / 'review-r19' / ('MARCH-labels-2%s.txt' % x)) for x in 'ab']
R19_2_ORDER = ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
for r, order in [(r, R19_ORDER) for r in R19] + [(r, R19_2_ORDER) for r in R19_2]:
    assert sorted(r) == list(range(1, len(order) + 1)), sorted(r)
MARCH = {p: [r[n] for r in R19] for n, p in enumerate(R19_ORDER, start=1) if p.startswith('H2')}
MARCH.update({p: [r[n] for r in R19_2] for n, p in enumerate(R19_2_ORDER, start=1)})
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
 'S13v27-1P3P4': ['H1-P3', 'H1-P4'],
 'S13v27-H1': ['H1'] + SUB['H1'],
 'S13v27-2P2P3': ['H2-P2', 'H2-P3'],
 'S13v27-2P3bP4': ['H2-P3b', 'H2-P4'],
 'S13v27-H2': ['H2'] + SUB['H2'],
 'S13v27-J1': ['H1-P3', 'H1-P4', 'H2'] + SUB['H2'],
 'S13v27-5P1P2': ['H5-P1', 'H5-P2'],
 'S13v27-5P3P4': ['H5-P3', 'H5-P4'],
 'S13v27-H5': ['H5'] + SUB['H5'],
 'S13v27-4P9h5P2': ['H4-P9', 'H5', 'H5-P1', 'H5-P2'],
 'S13v27': [(p or HEADS[i]) for i, p in enumerate(IDS)],
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
                 'march_note': '; '.join('%s: %s %s' % (p, 'r19 (first read)' if p.startswith('H2') else 'r19 (second read)'
                                         if p in R19_ORDER else 'b304', MARCH[p]) for p in ps),
                 'lint': lint('\n\n'.join(x for x in md if not x.startswith('#'))),
                 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, key
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b307.js'), '--name', 'B307'] + list(ITEMS), capture_output=True, text=True)
print(r.stdout[-3000:], r.stderr[-1500:])
for k, g in gate.items():
    print('%-16s %4d words  lint %-6s  march %s' % (k, g['words'], g['lint'], ' | '.join(g['march'][:4]) + (' ...' if len(g['march']) > 4 else '')))
