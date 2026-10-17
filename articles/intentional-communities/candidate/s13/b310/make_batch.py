"""Batch 310g (2026-10-16): screens of section 13 draft v30 (E175), v29 with the fixes of its meaning reviews, round r19
(../make_v30.py, ../review-r19/DISPOSITIONS-r19.md). v29 read 100% Human as a whole (309g); v30 changes words in ten of its
paragraphs, so the whole section and each changed subsection go to Pangram again. Marches: review-r19's fifth read (the first,
second, third and last subsections of v30), its sixth (the land subsection, after H3-P5's break was reworded), and b304's
records for the visitor subsection, unchanged since v26. Run from candidate/: python3 s13/b310/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

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
bl = [b.strip() for b in re.split(r'\n\s*\n', (S13 / 'v30.md').read_text(encoding='utf-8')) if b.strip()]
assert len(bl) == len(IDS)
TEXT = {(p or HEADS[i]): b for i, (p, b) in enumerate(zip(IDS, bl))}


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


R5 = [labels(S13 / 'review-r19' / ('MARCH-labels-5%s.txt' % x)) for x in 'ab']
R5_ORDER = ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4',
            'H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
R6 = [labels(S13 / 'review-r19' / ('MARCH-labels-6%s.txt' % x)) for x in 'ab']
R6_ORDER = ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5']
for r, order in [(r, R5_ORDER) for r in R5] + [(r, R6_ORDER) for r in R6]:
    assert sorted(r) == list(range(1, len(order) + 1)), sorted(r)
MARCH = {p: ([r[n] for r in R5], 'r19 read 5') for n, p in enumerate(R5_ORDER, start=1)}
MARCH.update({p: ([r[n] for r in R6], 'r19 read 6') for n, p in enumerate(R6_ORDER, start=1)})
g304 = json.loads((S13 / 'b304' / 'GATE.json').read_text(encoding='utf-8'))
m = g304['S13v26-H4']['march']
for i in range(9):
    MARCH['H4-P%d' % (i + 1)] = (m[2 * i:2 * i + 2], 'b304')
SUB = {'H1': ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], 'H2': ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       'H3': ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'], 'H5': ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']}
ITEMS = {
 'S13v30': [(p or HEADS[i]) for i, p in enumerate(IDS)],
 'S13v30-H1': ['H1'] + SUB['H1'], 'S13v30-H2': ['H2'] + SUB['H2'], 'S13v30-H3': ['H3'] + SUB['H3'],
 'S13v30-H5': ['H5'] + SUB['H5'], 'S13v30-J1': ['H1-P3', 'H1-P4', 'H2'] + SUB['H2'],
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
    ps = [p for p in parts if '-' in p]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in MARCH[p][0]],
                 'march_note': '; '.join('%s: %s %s' % (p, MARCH[p][1], MARCH[p][0]) for p in ps),
                 'lint': lint('\n\n'.join(x for x in md if not x.startswith('#'))), 'words': len(drafts[key].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b310.js'), '--name', 'B310'] + list(ITEMS), capture_output=True, text=True)
print(r.stdout[-1200:], r.stderr[-1500:])
pool, defs = [], []
for k in ITEMS:
    idx = []
    for p in drafts[k].split('\n\n'):
        if p not in pool:
            pool.append(p)
        idx.append(pool.index(p))
    assert '\n\n'.join(pool[i] for i in idx) == drafts[k]
    defs.append([k, idx, hashlib.sha256(drafts[k].encode('utf-8')).hexdigest()])
(HERE / 'run310-compact.js').write_text('const P = ' + json.dumps(pool) + ';\nconst defs = ' + json.dumps(defs) +
                                        ';\nwindow.__run("B310", defs.map(([k, ix, s]) => [k, ix.map(i => P[i]).join("\\n\\n"), s])); "started"',
                                        encoding='utf-8')
print({k: g['words'] for k, g in gate.items()})
