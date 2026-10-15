"""Batch 289g (2026-10-15, Joel's 31 a): the section 13 paragraphs whose records came back clean in gate round r6, each to
Pangram as soon as its own records are clean. Texts are from v9 (these six paragraphs are the same in v8 and v9).
Records: s13/review-r6 (march readings a and b, cold reads, traces, stance checks) and review-r6/DISPOSITIONS-r6.md for
H1-P2's one trace finding, kept. Alone, with a neighbor when under 50 words, and the heading with its paragraph.
Run from candidate/: python3 s13/b289/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

v8 = (C / 's13' / 'v8.md').read_text(encoding='utf-8')
v9 = (C / 's13' / 'v9.md').read_text(encoding='utf-8')
P = [p.strip() for p in re.split(r'\n\s*\n', v9) if p.strip()]
P8 = [p.strip() for p in re.split(r'\n\s*\n', v8) if p.strip()]
heads = [i for i, p in enumerate(P) if p.startswith('#')]
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
M = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r6' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    for k, v in labs.items():
        M.setdefault(int(k), []).append(v.strip())
def para(hn):
    t = P[heads[hn[0]] + hn[1]]
    assert t in P8, ('changed since v8, whose records these are', hn)
    return t
TRACE = {(0, 2): 'review-r6/trace-T1.md (its one finding, "relational pl/ork", kept: review-r6/DISPOSITIONS-r6.md)',
         (1, 1): 'review-r6/trace-T1.md (OK)', (2, 4): 'review-r6/trace-T3.md (OK)', (2, 5): 'review-r6/trace-T3.md (OK)',
         (3, 4): 'review-r6/trace-T4.md (OK)', (3, 6): 'review-r6/trace-T4.md (OK; the pair with H4-P7, OK)'}
ITEMS = {'S13v9-1P2': ([(0, 2)], False), 'S13v9-2P1': ([(1, 1)], False), 'S13v9-2P1h': ([(1, 1)], True),
         'S13v9-3P4': ([(2, 4)], False), 'S13v9-3P4P5': ([(2, 4), (2, 5)], False), 'S13v9-4P4': ([(3, 4)], False),
         'S13v9-4P6': ([(3, 6)], False)}
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
                 'march_note': 's13/review-r6/MARCH-labels-a.txt and -b.txt, ' + ', '.join('T%d' % T[hn] for hn in parts),
                 'cold': 'OK', 'cold_note': 's13/review-r6/SENSE-a.md, SENSE-b.md: OK for these paragraphs',
                 'grounding': 'OK', 'grounding_note': '; '.join('s13/' + TRACE[hn] for hn in parts),
                 'stance': 0, 'stance_note': 's13/review-r6/STANCE-pub.md, STANCE-sofar.md: nothing on these paragraphs',
                 'lint': lint, 'missing': [], 'words': len(text.split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], v['march'], drafts[k][:80].replace('\n', ' / '))
