"""Batch 326g (2026-10-17): screens (E175) of section 15 draft v5 (../make_v5.py: v4 with review round r4's fixes,
../review-r4/DISPOSITIONS-r4.md). Every paragraph v5 changes, alone or with each neighbor when it is under 50 words by spaces;
H1-P4's variant s (../v5-variants.json) alone and inside its subsection; each subsection with its heading; the whole section
as a reader sees it. Marches: review-r5 for the changed paragraphs and the variant (two readings); H2-P1 (variant b) from
review-r4b; the rest from the rounds that read them (H1-P2 and H1-P3 review-r2d, H2-P5 review-r2, H2-P6 review-r3, H3-P6
review-r2). Run from candidate/: python3 s15/b326/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S15 = C / 's15'
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

V = 'v5'
DRAFT = S15 / (V + '.md')
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video)')
bl = [b.strip() for b in re.split(r'\n\s*\n', DRAFT.read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in bl if not SKIP.match(b)]
prose = [b for b in reader if not b.startswith('[caption]')]
IDS = ['H1'] + ['H1-P%d' % i for i in range(1, 6)] + ['H2'] + ['H2-P%d' % i for i in range(1, 8)] + ['H3'] + ['H3-P%d' % i for i in range(1, 9)]
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
PARAS = [i for i in IDS if '-' in i]
VAR = json.loads((S15 / 'v5-variants.json').read_text(encoding='utf-8'))
T.update(VAR)


def labels(rnd):
    return [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
             (S15 / rnd / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']


MARCH, NOTE = {}, {}
def take(rnd, mapping):
    L = labels(rnd)
    for p, n in mapping.items():
        MARCH[p], NOTE[p] = [m[n] for m in L], '%s T%d' % (rnd, n)
take('review-r2d', {'H1-P2': 2, 'H1-P3': 3})
take('review-r2', {'H2-P5': 10, 'H3-P6': 18})
take('review-r3', {'H2-P6': 6})
take('review-r4b', {'H2-P1': 2})
r5 = json.loads((S15 / 'review-r5' / 'march-ids.json').read_text())
take('review-r5', {p: n for n, p in enumerate(r5, start=1)})
assert set(PARAS) <= set(MARCH), set(PARAS) - set(MARCH)
v4 = dict(zip(IDS, [b for b in [x.strip() for x in re.split(r'\n\s*\n', (S15 / 'v4.md').read_text(encoding='utf-8')) if x.strip()]
                    if not SKIP.match(b) and not b.startswith('[caption]')]))
changed = [p for p in PARAS if T[p] != v4[p]] + ['H2-P1']   # H2-P1 changed in v4 (variant b), read in 325g with P2 as it was
ITEMS = {}
for p in changed + list(VAR):
    if len(plain(T[p]).split()) >= 50:
        ITEMS['S15%s-%s' % (V, p)] = [p]
    else:
        base = p.rstrip('s')
        i = PARAS.index(base)
        for j in (i - 1, i + 1):
            if 0 <= j < len(PARAS) and PARAS[j][:2] == base[:2]:
                pair = [PARAS[j], p] if j < i else [p, PARAS[j]]
                ITEMS['S15%s-%s+%s' % (V, pair[0], pair[1].split('-')[1])] = pair
SUB = {h: [h] + [p for p in PARAS if p.startswith(h + '-')] for h in ('H1', 'H2', 'H3')}
ITEMS.update({'S15%s-%s' % (V, h): ids for h, ids in SUB.items()})
ITEMS['S15%ss-H1' % V] = [x if x != 'H1-P4' else 'H1-P4s' for x in SUB['H1']]


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
for key, parts in ITEMS.items():
    drafts[key] = '\n\n'.join(plain(T[p].lstrip('#').strip()) if p in ('H1', 'H2', 'H3') else plain(T[p]) for p in parts)
    ps = [p for p in parts if p in MARCH]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in MARCH[p]],
                 'march_note': '; '.join('%s %s' % (p, NOTE[p]) for p in ps),
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])
drafts['S15' + V] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b)) for b in reader)
gate['S15' + V] = {'kind': 'screen', 'march': [x for p in PARAS for x in MARCH[p]], 'march_note': 'every paragraph, as above',
                   'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))), 'words': len(drafts['S15' + V].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b326.js'), '--name', 'B326'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b326-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
