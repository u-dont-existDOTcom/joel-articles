"""Batch 338g (2026-10-17): section 15 draft v12 whole (../make_v12.py: v9 with round d's H1-P4 c, the only H1-P4 shape that
reads Human alone), the check before its install; every paragraph already has its Human result alone (paragraphs_alone.py
PASS over batches 322g to 335g). H1 with c read Human in 327g (S15v6c-H1, the same text). Marches as in 335g for every
paragraph, s15/review-r6 for H1-P4 c. Run from candidate/: python3 s15/b338/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S15, S16 = C / 's15', C / 's16'
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video)')
IDS = ['H1'] + ['H1-P%d' % i for i in range(1, 6)] + ['H2'] + ['H2-P%d' % i for i in range(1, 8)] + ['H3'] + ['H3-P%d' % i for i in range(1, 9)]
PARAS = [i for i in IDS if '-' in i]
bl = [b.strip() for b in re.split(r'\n\s*\n', (S15 / 'v12.md').read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in bl if not SKIP.match(b)]


def labels(folder):
    return [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
             (folder / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']


MARCH = {}
def take(folder, mapping):
    L = labels(folder)
    for p, n in mapping.items():
        MARCH[p] = [m[n] for m in L]
take(S15 / 'review-r2d', {'H1-P2': 2, 'H1-P3': 3})
take(S15 / 'review-r2', {'H2-P5': 10, 'H3-P6': 18})
take(S15 / 'review-r3', {'H2-P6': 6})
take(S15 / 'review-r4b', {'H2-P1': 2})
take(S15 / 'review-r5', {p: n for n, p in enumerate(json.loads((S15 / 'review-r5' / 'march-ids.json').read_text()), start=1)})
for rnd in ('review-r5', 'review-r6', 'review-r8'):
    ids = json.loads((S16 / rnd / 'march-ids.json').read_text())
    take(S16 / rnd, {p[4:]: n for n, p in enumerate(ids, start=1) if p.startswith('s15-')})
take(S15 / 'review-r6', {'H1-P4': json.loads((S15 / 'review-r6' / 'march-ids.json').read_text()).index('H1-P4c') + 1})
with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
    f.write('\n\n'.join(b for b in reader if not b.startswith(('#', '[caption]'))) + '\n')
lint = re.search(r'verdict: (\w+)', subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name],
                                                    capture_output=True, text=True).stdout).group(1)
drafts = {'S15v12': '\n\n'.join(plain(re.sub(r'^\[caption\]\s*', '', b)) for b in reader)}
gate = {'S15v12': {'kind': 'screen', 'march': [x for p in PARAS for x in MARCH[p]], 'march_note': 'every paragraph', 'lint': lint,
                   'words': len(drafts['S15v12'].split())}}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b338.js'), '--name', 'B338'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-400:], r.stderr[-800:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b338-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), {k: (g['words'], g['lint']) for k, g in gate.items()})
