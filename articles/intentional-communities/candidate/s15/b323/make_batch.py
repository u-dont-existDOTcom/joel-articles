"""Batch 323g (2026-10-17): screens (E175) of section 15 draft v3 (../make_v3.py: v2 with the stretches that read AI in 322g
rewritten from Emulate round b, ../emu-b/). Every changed paragraph alone, or with a neighbor when it is under 50 words by
spaces (both neighbors where it has two); H1-P4's variant x (the workshop and the aunt as a question at the end,
../v3-variants.json) alone and inside its subsection; each subsection with its heading; the whole section as a reader sees it
(the captions in, the images and the page's embed lines out). The paragraphs v3 keeps from v2 (H1-P1 to H1-P3, H1-P5, H3-P6,
H3-P8) read Human alone in 322g with these words and are not sent again. Marches: review-r3 for the changed paragraphs and the
variant (two readings); the kept paragraphs keep theirs (H1 from review-r2d, the rest from review-r2).
Run from candidate/: python3 s15/b323/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S15 = C / 's15'
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

DRAFT = S15 / 'v3.md'
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video)')
bl = [b.strip() for b in re.split(r'\n\s*\n', DRAFT.read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in bl if not SKIP.match(b)]
prose = [b for b in reader if not b.startswith('[caption]')]
IDS = ['H1'] + ['H1-P%d' % i for i in range(1, 6)] + ['H2'] + ['H2-P%d' % i for i in range(1, 8)] + ['H3'] + ['H3-P%d' % i for i in range(1, 9)]
assert len(prose) == len(IDS)
T = dict(zip(IDS, prose))
PARAS = [i for i in IDS if '-' in i]
VAR = json.loads((S15 / 'v3-variants.json').read_text(encoding='utf-8'))
T.update(VAR)


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


def readings(rnd):
    return [labels(S15 / rnd / ('MARCH-labels-%s.txt' % x)) for x in 'ab']


MARCH, NOTE = {}, {}
R2, R2D = readings('review-r2'), readings('review-r2d')
for n, p in enumerate(['H1-P%d' % i for i in range(1, 6)] + ['H2-P%d' % i for i in range(1, 8)] + ['H3-P%d' % i for i in range(1, 9)], start=1):
    MARCH[p], NOTE[p] = [m[n] for m in R2], 'review-r2 T%d' % n
for n in range(1, 6):
    MARCH['H1-P%d' % n], NOTE['H1-P%d' % n] = [m[n] for m in R2D], 'review-r2d T%d' % n
R3 = readings('review-r3')
r3ids = json.loads((S15 / 'review-r3' / 'march-ids.json').read_text())
for m in R3:
    assert sorted(m) == list(range(1, len(r3ids) + 1)), sorted(m)
for n, p in enumerate(r3ids, start=1):
    MARCH[p], NOTE[p] = [m[n] for m in R3], 'review-r3 T%d' % n
# H2-P3 and H3-P3 got a break after round r3 (a question each; reading a found none in H2-P3, neither reading in H3-P3):
# their marches are round r3b's
R3B = readings('review-r3b')
for n, p in enumerate(json.loads((S15 / 'review-r3b' / 'march-ids.json').read_text()), start=1):
    MARCH[p], NOTE[p] = [m[n] for m in R3B], 'review-r3b T%d' % n
fixes = {x['id']: x for x in json.loads((S15 / 'v3-fixes.json').read_text(encoding='utf-8'))}
changed = [p for p in PARAS if fixes[p]['source'] != 'v2']
assert set(changed) | {'H1-P4x'} == set(r3ids), (changed, r3ids)

ITEMS = {}
for p in changed + ['H1-P4x']:
    if len(plain(T[p]).split()) >= 50:
        ITEMS['S15v3-' + p] = [p]
    else:
        base = p.rstrip('x')
        i = PARAS.index(base)
        for j in (i - 1, i + 1):
            if 0 <= j < len(PARAS) and PARAS[j][:2] == base[:2]:
                pair = [PARAS[j], p] if j < i else [p, PARAS[j]]
                ITEMS['S15v3-%s+%s' % (pair[0], pair[1].split('-')[1])] = pair
SUB = {h: [h] + [p for p in PARAS if p.startswith(h + '-')] for h in ('H1', 'H2', 'H3')}
ITEMS.update({'S15v3-' + h: ids for h, ids in SUB.items()})
ITEMS['S15v3x-H1'] = [x if x != 'H1-P4' else 'H1-P4x' for x in SUB['H1']]


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
drafts['S15v3'] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b)) for b in reader)
gate['S15v3'] = {'kind': 'screen', 'march': [x for p in PARAS for x in MARCH[p]], 'march_note': 'every paragraph, as above',
                 'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))), 'words': len(drafts['S15v3'].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b323.js'), '--name', 'B323'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b323-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), {k: (g['words'], g['lint']) for k, g in gate.items()})
