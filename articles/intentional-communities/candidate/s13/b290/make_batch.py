"""Batch 290g (2026-10-15, Joel's 31 a): the section 13 v9 paragraphs whose records came back clean in gate round r7, each
to Pangram as soon as its own records are clean. Records: s13/review-r7 (march readings a and b, cold reads, traces,
stance checks) and review-r7/DISPOSITIONS-r7.md for the two asides kept (H4-P2, H4-P5); H4-P1 (read Human in 288g) and
H4-P4 (read Human in 289g) as neighbors, with their own records. Alone, and with a neighbor when under 50 words.
Run from candidate/: python3 s13/b290/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

v9 = (C / 's13' / 'v9.md').read_text(encoding='utf-8')
P = [p.strip() for p in re.split(r'\n\s*\n', v9) if p.strip()]
heads = [i for i, p in enumerate(P) if p.startswith('#')]
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
M = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r7' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    for k, v in labs.items():
        M.setdefault(int(k), []).append(v.strip())
def para(hn):
    t = P[heads[hn[0]] + hn[1]]
    return t
TRACE = {(0, 4): 'review-r7/trace-T1.md (OK)', (3, 1): 'review-r4/trace-T2.md (OK; read Human in 288g)',
         (3, 2): 'review-r7/trace-T3.md (its one finding, the aside, kept: review-r7/DISPOSITIONS-r7.md)',
         (3, 3): 'review-r7/trace-T3.md (OK)', (3, 4): 'review-r6/trace-T4.md (OK; read Human in 289g)',
         (3, 5): 'review-r7/trace-T4.md (its one finding, the remark, kept: review-r7/DISPOSITIONS-r7.md)',
         (3, 9): 'review-r7/trace-T5.md (OK)'}
ITEMS = {'S13v9-1P4': ([(0, 4)], False), 'S13v9-4P2': ([(3, 2)], False), 'S13v9-4P1P2': ([(3, 1), (3, 2)], False),
         'S13v9-4P3P4': ([(3, 3), (3, 4)], False), 'S13v9-4P5': ([(3, 5)], False), 'S13v9-4P9': ([(3, 9)], False)}
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
                 'march_note': 's13/review-r7/MARCH-labels-a.txt and -b.txt, ' + ', '.join('T%d' % T[hn] for hn in parts),
                 'cold': 'OK', 'cold_note': 's13/review-r7/SENSE-a.md, SENSE-b.md: OK for these paragraphs',
                 'grounding': 'OK', 'grounding_note': '; '.join('s13/' + TRACE[hn] for hn in parts),
                 'stance': 0, 'stance_note': 's13/review-r7/STANCE-pub.md, STANCE-sofar.md: nothing on these paragraphs',
                 'lint': lint, 'missing': [], 'words': len(text.split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], v['march'], drafts[k][:80].replace('\n', ' / '))
