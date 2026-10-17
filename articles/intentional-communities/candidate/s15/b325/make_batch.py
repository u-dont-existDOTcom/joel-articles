"""Batch 325g (2026-10-17): screens (E175) of H2-P1's three variants (../make_v4.py, ../v4-variants.json): a and b by hand,
c from Emulate round c (../emu-c/). The paradise subsection read "Mostly Human" in 323g, a 40-word AI window over its heading
and P1, while P1 with P2 read Human without the heading. Each variant goes with the heading and P2 (P1 is under 50 words), and
inside the whole subsection. Marches: review-r4b (two readings) for the variants, the rest of the subsection as in 323g.
Run from candidate/: python3 s15/b325/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
S15 = C / 's15'
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

VAR = json.loads((S15 / 'v4-variants.json').read_text(encoding='utf-8'))
G323 = json.loads((S15 / 'b323' / 'GATE.json').read_text(encoding='utf-8'))
D323 = json.loads((S15 / 'b323' / 'drafts.json').read_text(encoding='utf-8'))
sub = D323['S15v3-H2']
assert sub.count(VAR['v3']) == 1


def labels(path):
    return {int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M)}


R4B = [labels(S15 / 'review-r4b' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
ids = json.loads((S15 / 'review-r4b' / 'march-ids.json').read_text())
M = {p[-1]: [m[n] for m in R4B] for n, p in enumerate(ids, start=1)}
# the subsection's other marches, from 323g's gate record of the subsection (its first two entries are v3's H2-P1)
rest = G323['S15v3-H2']['march'][2:]


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


P2 = sub.split('\n\n')[2]
assert P2.startswith('Sénégal passed a law')
drafts, gate = {}, {}
for v in 'abc':
    p1 = plain(VAR[v])
    drafts['S15v4%s-H2h-P1+P2' % v] = 'All is not well in paradise\n\n' + p1 + '\n\n' + P2
    drafts['S15v4%s-H2' % v] = sub.replace(VAR['v3'], p1)
    p2m = G323['S15v3-H2-P2']['march']
    gate['S15v4%s-H2h-P1+P2' % v] = {'kind': 'screen', 'march': M[v] + p2m, 'march_note': 'H2-P1%s review-r4b; H2-P2 review-r3' % v,
                                     'lint': lint(p1 + '\n\n' + P2), 'words': len(drafts['S15v4%s-H2h-P1+P2' % v].split())}
    gate['S15v4%s-H2' % v] = {'kind': 'screen', 'march': M[v] + rest, 'march_note': 'H2-P1%s review-r4b; the rest as in 323g' % v,
                              'lint': lint('\n\n'.join(drafts['S15v4%s-H2' % v].split('\n\n')[1:])), 'words': len(drafts['S15v4%s-H2' % v].split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b325.js'), '--name', 'B325'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b325-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), {k: (g['words'], g['lint']) for k, g in gate.items()})
