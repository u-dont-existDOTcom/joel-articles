"""Batch 292g (2026-10-15, Joel's 31 a): the section 13 v12 paragraphs whose records came back clean in gate round r9, each
to Pangram as soon as its own records are clean, with the headings of the first, third and fifth subsections over their
first paragraphs. Records: s13/review-r9 (march readings, cold reads, traces, stance checks), and for H1-P2 the one trace
finding kept ("relational pl/ork", review-r6/DISPOSITIONS-r6.md); H1-P1's trace is round r7's (its text unchanged since
v9). Run from candidate/: python3 s13/b292/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

v9 = (C / 's13' / 'v12.md').read_text(encoding='utf-8')
P = [p.strip() for p in re.split(r'\n\s*\n', v9) if p.strip()]
heads = [i for i, p in enumerate(P) if p.startswith('#')]
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
M = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r9' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    for k, v in labs.items():
        M.setdefault(int(k), []).append(v.strip())
def para(hn):
    t = P[heads[hn[0]] + hn[1]]
    return t
TRACE = {(0, 1): 'review-r7/trace-T1.md (OK; unchanged since v9)',
         (0, 2): 'review-r9/trace-T1.md (its one finding, "relational pl/ork", kept: review-r6/DISPOSITIONS-r6.md)',
         (2, 1): 'review-r9/trace-T2.md (OK)', (3, 7): 'review-r9/trace-T4.md (OK)', (4, 1): 'review-r9/trace-T5.md (OK)'}
ITEMS = {'S13v12-1hP1P2': ([(0, 1), (0, 2)], True), 'S13v12-1P1P2': ([(0, 1), (0, 2)], False), 'S13v12-1P2': ([(0, 2)], False),
         'S13v12-3P1': ([(2, 1)], False), 'S13v12-3hP1': ([(2, 1)], True), 'S13v12-4P7': ([(3, 7)], False),
         'S13v12-5P1': ([(4, 1)], False), 'S13v12-5hP1': ([(4, 1)], True)}
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
                 'march_note': 's13/review-r9/MARCH-labels-a.txt and -b.txt, ' + ', '.join('T%d' % T[hn] for hn in parts),
                 'cold': 'OK', 'cold_note': 's13/review-r9/SENSE-a.md, SENSE-b.md: OK for these paragraphs',
                 'grounding': 'OK', 'grounding_note': '; '.join('s13/' + TRACE[hn] for hn in parts),
                 'stance': 0, 'stance_note': 's13/review-r9/STANCE-pub.md, STANCE-sofar.md: no conflicts in the rewrite',
                 'lint': lint, 'missing': [], 'words': len(text.split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], v['march'], drafts[k][:80].replace('\n', ' / '))
