"""Batch 297g (2026-10-15, after Joel's 32 b): every paragraph v21 changed, whose records came back clean in gate round
r14 (s13/review-r14/, DISPOSITIONS-r14.md): H2-P3 alone, H3-P5 after H3-P4 (it is under 50 words), H4-P5 alone, H5-P3
alone. H3-P4's trace is round r6's (unchanged since v8). Run from candidate/: python3 s13/b297/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

v9 = (C / 's13' / 'v21.md').read_text(encoding='utf-8')
P = [p.strip() for p in re.split(r'\n\s*\n', v9) if p.strip()]
heads = [i for i, p in enumerate(P) if p.startswith('#')]
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
M = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r14' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    for k, v in labs.items():
        M.setdefault(int(k), []).append(v.strip())
def para(hn):
    t = P[heads[hn[0]] + hn[1]]
    return t
TRACE = {(1, 3): 'review-r14/trace-T1.md (OK)',
         (2, 4): 'review-r6/trace-T3.md (OK; unchanged since v8)',
         (2, 5): 'review-r14/trace-T1.md (its one finding, the reading-list pointer, kept: review-r14/DISPOSITIONS-r14.md)',
         (3, 5): 'review-r14/trace-T2.md (OK)',
         (4, 3): 'review-r14/trace-T2.md (its one finding, the Zapatista clause, kept: review-r14/DISPOSITIONS-r14.md)'}
ITEMS = {'S13v21-2P3': ([(1, 3)], False), 'S13v21-3P4P5': ([(2, 4), (2, 5)], False), 'S13v21-4P5': ([(3, 5)], False),
         'S13v21-5P3': ([(4, 3)], False)}
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
                 'march_note': 's13/review-r14/MARCH-labels-a.txt and -b.txt, ' + ', '.join('T%d' % T[hn] for hn in parts),
                 'cold': 'OK', 'cold_note': 's13/review-r14/SENSE-a.md, SENSE-b.md: OK for all 27 paragraphs',
                 'grounding': 'OK', 'grounding_note': '; '.join('s13/' + TRACE[hn] for hn in parts),
                 'stance': 0, 'stance_note': 's13/review-r14/STANCE-pub.md, STANCE-sofar.md: no conflicts',
                 'lint': lint, 'missing': [], 'words': len(text.split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], v['march'], drafts[k][:80].replace('\n', ' / '))
