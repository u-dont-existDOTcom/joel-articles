"""Batch 322g (2026-10-17): screens (E175) of section 15 draft v2 (../make_v2.py: v1, ../make_v1.py, with a break in each paragraph round r1's march found none in): every paragraph alone, or with a neighbor
when it is under 50 words by spaces (H2-P5 is published; H2-P6, published too, lost a sentence shaped like a list of three, so the pair goes again), each subsection with its heading, and the whole section as a reader sees it (the captions in, the images and the
page's embed lines out). Marches: review-r2 (two readings). Run from candidate/: python3 s15/b322/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

DRAFT = C / 's15' / 'v2.md'
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video)')
bl = [b.strip() for b in re.split(r'\n\s*\n', DRAFT.read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in bl if not SKIP.match(b)]
prose = [b for b in reader if not b.startswith('[caption]')]
IDS = ['H1'] + ['H1-P%d' % i for i in range(1, 6)] + ['H2'] + ['H2-P%d' % i for i in range(1, 8)] + ['H3'] + ['H3-P%d' % i for i in range(1, 9)]
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
PARAS = [i for i in IDS if '-' in i]


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


M = [labels(C / 's15' / 'review-r2' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
for m in M:
    assert sorted(m) == list(range(1, len(PARAS) + 1)), sorted(m)
MARCH = {p: [m[n] for m in M] for n, p in enumerate(PARAS, start=1)}
# H2-P1 changed after round r2 (its first break wasn't one to either reader): its march is round r2b's (T1 of
# review-r2b/MARCH-PROMPT.txt)
R2B = [labels(C / 's15' / 'review-r2b' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
MARCH['H2-P1'] = [m[1] for m in R2B]
# H1-P4 changed after round r2 (the aunt joke in one sentence, for the linter's landings): the first subsection's marches are
# round r2d's (T1 to T5 of review-r2d)
R2D = [labels(C / 's15' / 'review-r2d' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
for n in range(1, 6):
    MARCH['H1-P%d' % n] = [m[n] for m in R2D]
# H2-P6 changed after round r2 (its sentence shaped like a list of three): its march is round r2c's (T2 of review-r2c)
R2C = [labels(C / 's15' / 'review-r2c' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
MARCH['H2-P6'] = [m[2] for m in R2C]
SUB = {h: [h] + [p for p in PARAS if p.startswith(h + '-')] for h in ('H1', 'H2', 'H3')}
ITEMS = {'S15v2-H1-P1+P2': ['H1-P1', 'H1-P2'], 'S15v2-H1-P3': ['H1-P3'], 'S15v2-H1-P4': ['H1-P4'],
         'S15v2-H1-P5': ['H1-P5'], 'S15v2-H2-P1+P2': ['H2-P1', 'H2-P2'], 'S15v2-H2-P2': ['H2-P2'],
         'S15v2-H2-P3+P4': ['H2-P3', 'H2-P4'], 'S15v2-H2-P5+P6': ['H2-P5', 'H2-P6'], 'S15v2-H2-P7': ['H2-P7']}
ITEMS.update({'S15v2-H3-P%d' % i: ['H3-P%d' % i] for i in range(1, 9)})
ITEMS.update({'S15v2-' + h: ids for h, ids in SUB.items()})


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
for key, parts in ITEMS.items():
    drafts[key] = '\n\n'.join(plain(T[p]) for p in parts)
    ps = [p for p in parts if p in MARCH]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in MARCH[p]], 'march_note': 's15/review-r2/MARCH-labels-a.txt, -b.txt; H1 from review-r2d; H2-P1 from review-r2b; H2-P6 from review-r2c',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])
drafts['S15v2'] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b)) for b in reader)
gate['S15v2'] = {'kind': 'screen', 'march': [x for p in PARAS for x in MARCH[p]], 'march_note': 'every paragraph, s15/review-r2',
                 'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))), 'words': len(drafts['S15v2'].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b322.js'), '--name', 'B322'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-500:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b322-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), {k: g['words'] for k, g in gate.items()})
