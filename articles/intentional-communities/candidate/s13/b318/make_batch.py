"""Batch 318g (2026-10-17): the three paragraphs of section 13 draft v34 that the install check
(tools/humanization/paragraphs_alone.py, run by s13/install/install_s13_v34.py) found with no Pangram check of their exact
text alone: H3-P5, the book line (31 words by spaces, so with H3-P4, which v34 changed), and H4-P6 and H5-P4, which v32
made plainer at the pause tally ("think someone's safe just because they're going along with everyone else", "Six months
with someone", "ombudsperson") and no batch read alone since. Screens as batch 317g's. Run from candidate/:
python3 s13/b318/make_batch.py"""
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
bl = [b.strip() for b in re.split(r'\n\s*\n', (C / 's13' / 'v34.md').read_text(encoding='utf-8')) if b.strip()]
assert len(bl) == len(IDS)
T13 = {(p or HEADS[i]): b for i, (p, b) in enumerate(zip(IDS, bl))}
PARAS13 = [p for p in IDS if p]


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


M13 = [labels(C / 's13' / 'review-r21' / ('MARCH-labels-2%s.txt' % x)) for x in 'ab']
H4M = [labels(C / 's13' / 'review-r21' / ('MARCH-labels-4%s.txt' % x)) for x in 'ab']
for m, h in zip(M13, H4M):
    assert sorted(h) == list(range(1, 10)), sorted(h)
    for i in range(9):
        m[15 + i] = h[i + 1]   # H4-P1..P9 are T15..T23 of the whole-section read
H2M = [labels(C / 's13' / 'review-r24c' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
# round r24c read the subsection after H2-P4's last fix; H2-P1 to H2-P3b haven't changed since round r24b read them, so a
# paragraph whose r24c reading misses a break keeps r24b's two readings (convergent review: an unchanged item keeps its verdict;
# r24c's read a found no break in H2-P3b, which r24 and r24b found in all four readings)
H2B = [labels(C / 's13' / 'review-r24b' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
for n in range(1, 5):
    if not all('B' in h[n].split() for h in H2M):
        print('march of H2 paragraph %d, unchanged since round r24b, from r24b:' % n, [h[n] for h in H2B])
        for h, hb in zip(H2M, H2B):
            h[n] = hb[n]
for m, h in zip(M13, H2M):
    assert sorted(h) == list(range(1, 6)), sorted(h)
    for i in range(5):
        m[5 + i] = h[i + 1]
H3M = [labels(C / 's13' / 'review-r21' / ('MARCH-labels-5%s.txt' % x)) for x in 'ab']
for m, h in zip(M13, H3M):
    assert sorted(h) == list(range(1, 6)), sorted(h)
    for i in range(5):
        m[10 + i] = h[i + 1]   # H3-P1..P5 are T10..T14 (the land subsection read again after the book line's last change)
for m in M13:
    assert sorted(m) == list(range(1, len(PARAS13) + 1)), sorted(m)
MARCH = {p: [m[n] for m in M13] for n, p in enumerate(PARAS13, start=1)}
# a paragraph unchanged since v31 whose new readings miss its break keeps its earlier march (convergent review: an unchanged
# item keeps its verdict), as batch 311g did: round r19's reads 5 and 6, and b304's for the visitor subsection
v31 = [b.strip() for b in re.split(r'\n\s*\n', (C / 's13' / 'v31.md').read_text(encoding='utf-8')) if b.strip()]
V31 = {(p or HEADS[i]): b for i, (p, b) in enumerate(zip(IDS, v31))}
R5_ORDER = ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4',
            'H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
R5 = [labels(C / 's13' / 'review-r19' / ('MARCH-labels-5%s.txt' % x)) for x in 'ab']
OLD = {p: [r[n] for r in R5] for n, p in enumerate(R5_ORDER, start=1)}
for p in PARAS13:
    if T13[p] == V31[p] and not all('B' in m.split() for m in MARCH[p]) and p in OLD:
        MARCH[p] = OLD[p]
        print('march of unchanged', p, 'from round r19 read 5:', OLD[p])
T = dict(T13)
SUB = {'H1': ['H1', 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'],
       'H3': ['H3', 'H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'],
       'H4': ['H4'] + ['H4-P%d' % i for i in range(1, 10)]}
ITEMS = {
    'S13v34-H3-P4+P5': ['H3-P4', 'H3-P5'], 'S13v34-H4-P6': ['H4-P6'], 'S13v34-H5-P4': ['H5-P4'],
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
                 'march_note': 's13: review-r21/MARCH-labels-2a.txt, -2b.txt, the visitor subsection from -4a.txt, -4b.txt, the land subsection from -5a.txt, -5b.txt; the values subsection from review-r24c (v34 as it is now); H3-P4 and H4-P8 changed one word group each in v34 (trace fixes), their sentences and breaks unchanged',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b318.js'), '--name', 'B318'] + list(ITEMS), capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b318-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), {k: g['words'] for k, g in gate.items()})
