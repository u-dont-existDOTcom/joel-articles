"""Batch 296g (2026-10-15, after Joel's 32 b): H4-P6 (his "good person" detector back) and H5-P4 (consent to the shared
life), whose records came back clean in gate round r13 (s13/review-r13/, DISPOSITIONS-r13.md), each alone, from v20 (v21
doesn't change them). Run from candidate/: python3 s13/b296/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

v9 = (C / 's13' / 'v20.md').read_text(encoding='utf-8')
P = [p.strip() for p in re.split(r'\n\s*\n', v9) if p.strip()]
heads = [i for i, p in enumerate(P) if p.startswith('#')]
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
M = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r13' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    for k, v in labs.items():
        M.setdefault(int(k), []).append(v.strip())
def para(hn):
    t = P[heads[hn[0]] + hn[1]]
    return t
TRACE = {(3, 6): 'review-r13/trace-T2.md (OK)', (4, 4): 'review-r13/trace-T3.md (OK)'}
ITEMS = {'S13v20-4P6': ([(3, 6)], False), 'S13v20-5P4': ([(4, 4)], False)}
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
                 'march_note': 's13/review-r13/MARCH-labels-a.txt and -b.txt, ' + ', '.join('T%d' % T[hn] for hn in parts),
                 'cold': 'OK', 'cold_note': 's13/review-r13/SENSE-a.md, SENSE-b.md: OK for these paragraphs',
                 'grounding': 'OK', 'grounding_note': '; '.join('s13/' + TRACE[hn] for hn in parts),
                 'stance': 0, 'stance_note': 's13/review-r13/STANCE-pub.md, STANCE-sofar.md: no conflicts in these paragraphs (theirs are in H3-P5, H4-P5 and H5-P3, fixed in v21)',
                 'lint': lint, 'missing': [], 'words': len(text.split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], v['march'], drafts[k][:80].replace('\n', ' / '))
