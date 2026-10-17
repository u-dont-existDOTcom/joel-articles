"""Batch 309g (2026-10-16): screens of section 13 draft v29 and three one-fix variants (E175). v29 (../make_v29.py) is v28
with the sentences at 308g's four AI windows taken back to Emulate's own: H1-P3's first sentence (v29a), H2-P3 from round j's
call B and H2-P4 from call A (v29b), and H3-P1's last two sentences from round i's call A (v29c); v29 has all three. The
variants show which fix moves which window, since a change anywhere in the section can move a window elsewhere (section 12's
lesson). Marches: review-r19's fourth read (the first three subsections of v29), its third (v28's versions and the last
subsection), and b304's records for the land and visitor subsections. Run from candidate/: python3 s13/b309/make_batch.py"""
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


def load(name):
    bl = [b.strip() for b in re.split(r'\n\s*\n', (S13 / name).read_text(encoding='utf-8')) if b.strip()]
    assert len(bl) == len(IDS), name
    return {(p or HEADS[i]): b for i, (p, b) in enumerate(zip(IDS, bl))}


V = {k: load(k + '.md') for k in ('v28', 'v29', 'v29a', 'v29b', 'v29c')}


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


R4 = [labels(S13 / 'review-r19' / ('MARCH-labels-4%s.txt' % x)) for x in 'ab']
R4_ORDER = ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4',
            'H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5']
R3 = [labels(S13 / 'review-r19' / ('MARCH-labels-3%s.txt' % x)) for x in 'ab']
R3_ORDER = ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
for r, order in [(r, R4_ORDER) for r in R4] + [(r, R3_ORDER) for r in R3]:
    assert sorted(r) == list(range(1, len(order) + 1)), sorted(r)
M29 = {p: [r[n] for r in R4] for n, p in enumerate(R4_ORDER, start=1)}   # the paragraphs as in v29
M28 = {p: [r[n] for r in R3] for n, p in enumerate(R3_ORDER, start=1)}   # the paragraphs as in v28
g304 = json.loads((S13 / 'b304' / 'GATE.json').read_text(encoding='utf-8'))
for key, sub in (('S13v26-H3', ['H3-P%d' % i for i in range(1, 6)]), ('S13v26-H4', ['H4-P%d' % i for i in range(1, 10)])):
    m = g304[key]['march']
    for i, p in enumerate(sub):
        M28.setdefault(p, m[2 * i:2 * i + 2])


def march(way, p):
    """The readings of paragraph p as it stands in the way's text."""
    if V[way][p] == V['v29'][p] and p in M29:
        return M29[p], 'r19 read 4'
    if V[way][p] == V['v28'][p] and p in M28:
        return M28[p], ('r19 read 3' if p in R3_ORDER else 'b304')
    raise SystemExit('no march read for %s in %s' % (p, way))


SUB = {'H1': ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], 'H2': ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       'H3': ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'], 'H5': ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']}
WHOLE = [(p or HEADS[i]) for i, p in enumerate(IDS)]
ITEMS = {
 'S13v29': ('v29', WHOLE), 'S13v29a': ('v29a', WHOLE), 'S13v29b': ('v29b', WHOLE), 'S13v29c': ('v29c', WHOLE),
 'S13v29-H1': ('v29', ['H1'] + SUB['H1']), 'S13v29-H2': ('v29', ['H2'] + SUB['H2']),
 'S13v29-H3': ('v29', ['H3'] + SUB['H3']), 'S13v29-J1': ('v29', ['H1-P3', 'H1-P4', 'H2'] + SUB['H2']),
}


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
for key, (way, parts) in ITEMS.items():
    md = [V[way][p] for p in parts]
    drafts[key] = '\n\n'.join(plain(x) for x in md)
    ps = [p for p in parts if '-' in p]
    ms = [march(way, p) for p in ps]
    gate[key] = {'kind': 'screen', 'march': [x for m, _ in ms for x in m],
                 'march_note': '; '.join('%s: %s %s' % (p, src, m) for p, (m, src) in zip(ps, ms)),
                 'lint': lint('\n\n'.join(x for x in md if not x.startswith('#'))), 'words': len(drafts[key].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b309.js'), '--name', 'B309'] + list(ITEMS), capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-1500:])
for k, g in gate.items():
    print('%-12s %4d words  lint %-6s  march %s' % (k, g['words'], g['lint'], ' | '.join(g['march'][:6]) + ' ...'))
