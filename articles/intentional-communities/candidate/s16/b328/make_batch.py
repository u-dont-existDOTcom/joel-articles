"""Batch 328g (2026-10-17): screens (E175) of section 16 draft v1 (../make_v1.py: Emulate round a with the published meaning
put back, the dedup of the repeats check, review-r1/DISPOSITIONS-r1.md). Every paragraph alone, or with each neighbor in its
subsection when it is under 50 words by spaces (H3-P9 with H3-P10 is 48 words, so H3-P9 goes with H3-P8 only); each
subsection with its heading; the whole section as a reader sees it (the caption in, the images out). Marches: review-r2 (two
readings). Run from candidate/: python3 s16/b328/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S16 = C / 's16'
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

V = 'v1'
DRAFT = S16 / (V + '.md')
SKIP = re.compile(r'^\[image \d+\]')
bl = [b.strip() for b in re.split(r'\n\s*\n', DRAFT.read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in bl if not SKIP.match(b)]
prose = [b for b in reader if not b.startswith('[caption]')]
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
assert len(prose) == len(IDS), (len(prose), len(IDS))
T = dict(zip(IDS, prose))
PARAS = [i for i in IDS if '-' in i]
L = [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
      (S16 / 'review-r2' / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']
r2 = json.loads((S16 / 'review-r2' / 'march-ids.json').read_text())
assert r2 == PARAS, (r2, PARAS)
MARCH = {p: [m[n] for m in L] for n, p in enumerate(PARAS, start=1)}
ITEMS = {}
for i, p in enumerate(PARAS):
    if len(plain(T[p]).split()) >= 50:
        ITEMS['S16%s-%s' % (V, p)] = [p]
        continue
    for j in (i - 1, i + 1):
        if 0 <= j < len(PARAS) and PARAS[j][:2] == p[:2]:
            pair = [PARAS[j], p] if j < i else [p, PARAS[j]]
            if len(' '.join(plain(T[x]) for x in pair).split()) >= 50:
                ITEMS['S16%s-%s+%s' % (V, pair[0], pair[1].split('-')[1])] = pair
SUB = {h: [h] + [p for p in PARAS if p.startswith(h + '-')] for h in ('H1', 'H2', 'H3')}
ITEMS.update({'S16%s-%s' % (V, h): ids for h, ids in SUB.items()})


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
for key, parts in ITEMS.items():
    drafts[key] = '\n\n'.join(plain(T[p].lstrip('#').strip()) if p in ('H1', 'H2', 'H3') else plain(T[p]) for p in parts)
    ps = [p for p in parts if p in MARCH]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in MARCH[p]], 'march_note': 's16/review-r2',
                 'lint': lint('\n\n'.join(T[p] for p in parts if not T[p].startswith('#'))), 'words': len(drafts[key].split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])
drafts['S16' + V] = '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b).lstrip('#').strip()) for b in reader)
gate['S16' + V] = {'kind': 'screen', 'march': [x for p in PARAS for x in MARCH[p]], 'march_note': 'every paragraph, s16/review-r2',
                   'lint': lint('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]')))), 'words': len(drafts['S16' + V].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b328.js'), '--name', 'B328'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b328-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
