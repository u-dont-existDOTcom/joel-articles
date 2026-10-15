"""Batch 288g (2026-10-15, after Joel's 31 a): the section 13 v6 paragraphs whose gate records are clean and that
Pangram hasn't read yet, alone, with a neighbor when under 50 words, and each heading with its paragraph. Records:
s13/review-r4 (march, cold reads, traces of the changed pairs, stance), s13/review-r3 for the unchanged H2-P2's trace.
Run from candidate/: python3 s13/b288/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

v6 = (C / 's13' / 'v6.md').read_text(encoding='utf-8')
P = [p.strip() for p in re.split(r'\n\s*\n', v6) if p.strip()]
heads = [i for i, p in enumerate(P) if p.startswith('#')]
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
M = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r4' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    for k, v in labs.items():
        M.setdefault(int(k), []).append(v.strip())
def para(hn):
    return P[heads[hn[0]] + hn[1]]
TRACE = {(0, 4): 'review-r4/trace-T1.md (OK)', (1, 1): 'review-r4/trace-T1.md (OK)', (1, 2): 'review-r3/trace-T2.md (OK; unchanged since v5)',
         (1, 3): 'review-r4/trace-T1.md (OK)', (1, 4): 'review-r4/trace-T1.md (OK)', (3, 1): 'review-r4/trace-T2.md (OK)'}
ITEMS = {'S13v6-1P4': ([(0, 4)], False), 'S13v6-2P1': ([(1, 1)], False), 'S13v6-2P1h': ([(1, 1)], True), 'S13v6-2P1P2': ([(1, 1), (1, 2)], False),
         'S13v6-2P3': ([(1, 3)], False), 'S13v6-2P4': ([(1, 4)], False), 'S13v6-4P1': ([(3, 1)], False), 'S13v6-4P1h': ([(3, 1)], True)}
drafts, gate = {}, {}
for key, (parts, with_head) in ITEMS.items():
    md = [para(hn) for hn in parts]
    if with_head:
        md = [P[heads[parts[0][0]]]] + md
    text = '\n\n'.join(plain(x) for x in md)
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write('\n\n'.join(x for x in md if not x.startswith('#')) + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    lint = re.search(r'verdict: (\w+)', r.stdout).group(1)
    drafts[key] = text
    gate[key] = {'kind': 'draft', 'march': [m for hn in parts for m in M[T[hn]]],
                 'march_note': 's13/review-r4/MARCH-labels-a.txt and -b.txt, ' + ', '.join('T%d' % T[hn] for hn in parts),
                 'cold': 'OK', 'cold_note': 's13/review-r4/SENSE-a.md, SENSE-b.md: OK for these paragraphs',
                 'grounding': 'OK', 'grounding_note': '; '.join('s13/' + TRACE[hn] for hn in parts),
                 'stance': 0, 'stance_note': 's13/review-r4/STANCE-pub.md, STANCE-sofar.md: nothing on these paragraphs',
                 'lint': lint, 'missing': [], 'words': len(text.split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], v['march'], drafts[k][:80].replace('\n', ' / '))
