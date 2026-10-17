"""Batch 347g (2026-10-17): the whole section reads AI over the same two stretches in every draft so far (344g to 346g: the
caption and H2-P2 to H2-P4 or H2-P3 to H2-P5; H3-P5 to H3-P7 or H3-P8), though every paragraph, every pair and H2 alone read
Human. Pangram cuts the whole section into windows, and a window over the stretch alone is what reads AI. So this batch screens
the stretches as Pangram cut them, in the drafts that have them (v10 db's H2, v11 (a, a)'s H2 and H3, v9's H3 shape a), to see
which stretch reads AI alone. Every paragraph has its marches (rounds r2 to r22). Run from candidate/: python3 s16/b347/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S16 = C / 's16'
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402
SKIP = re.compile(r'^\[image \d+\]')
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])


def labels(folder):
    return [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
             (folder / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']


MARCH = {}
for rnd in ['review-r2', 'review-r3', 'review-r3b', 'review-r3c', 'review-r3d', 'review-r5', 'review-r6', 'review-r8', 'review-r9',
            'review-r10', 'review-r11', 'review-r12', 'review-r14', 'review-r15', 'review-r16', 'review-r17', 'review-r18',
            'review-r20', 'review-r21', 'review-r22']:
    L = labels(S16 / rnd)
    for n, p in enumerate(json.loads((S16 / rnd / 'march-ids.json').read_text()), start=1):
        if p.startswith('s15-'):
            continue
        MARCH[p[4:] if p.startswith('s16-') else p] = [m[n] for m in L]
MARCH['H2-P3'] = MARCH['H2-P3a']
MARCH['H2-P5'] = MARCH['H2-P5d']
MARCH['H3-P4'] = MARCH['H3-P4x']


def draft(script, args, out):
    subprocess.run([sys.executable, str(S16 / script)] + args, check=True, capture_output=True)
    bl = [b.strip() for b in re.split(r'\n\s*\n', (S16 / out).read_text(encoding='utf-8')) if b.strip()]
    reader = [b for b in bl if not SKIP.match(b)]
    return reader


def run(reader, first, last, caption=False):
    """the reader blocks from paragraph first to last (ids), with the caption before H2-P2 when asked"""
    prose = [b for b in reader if not b.startswith('[caption]')]
    T = dict(zip(IDS, prose))
    parts = [T[p] for p in IDS[IDS.index(first):IDS.index(last) + 1]]
    if caption:
        cap = [b for b in reader if b.startswith('[caption]')][0]
        parts = [re.sub(r'^\[caption\]\s*', '', cap)] + parts
    return '\n\n'.join(plain(x) for x in parts), parts


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
def add(key, reader, first, last, M, caption=False):
    text, parts = run(reader, first, last, caption)
    drafts[key] = text
    ps = IDS[IDS.index(first):IDS.index(last) + 1]
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in M[p]], 'march_note': 'as in 344g to 346g',
                 'lint': lint('\n\n'.join(x for x in parts if not x.startswith('Too bad'))), 'words': len(text.split())}


V10 = draft('make_v10.py', ['db'], 'v10.md')
M10 = dict(MARCH); M10['H3-P6'] = MARCH['H3-P6a']
add('S16v10-cap+H2-P2-P4', V10, 'H2-P2', 'H2-P4', M10, caption=True)
add('S16v10-H2-P3-P5', V10, 'H2-P3', 'H2-P5', M10)
add('S16v10-H3-P4-P6', V10, 'H3-P4', 'H3-P6', M10)
add('S16v10-H3-P5-P7', V10, 'H3-P5', 'H3-P7', M10)
V11 = draft('make_v11.py', ['a', 'a'], 'v11.md')
M11 = dict(M10)
for p in ('H2-P2', 'H2-P3', 'H2-P4', 'H3-P4', 'H3-P5', 'H3-P6'):
    M11[p] = MARCH[p + 'e']
add('S16v11-cap+H2-P2-P4', V11, 'H2-P2', 'H2-P4', M11, caption=True)
add('S16v11-H2-P3-P5', V11, 'H2-P3', 'H2-P5', M11)
add('S16v11-H3-P5-P7', V11, 'H3-P5', 'H3-P7', M11)
subprocess.run([sys.executable, str(S16 / 'make_v12.py')], check=True, capture_output=True)
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b347.js'), '--name', 'B347'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b347-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), {k: (g['words'], g['lint']) for k, g in gate.items()})
