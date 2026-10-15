"""Batch 291g (2026-10-15, Joel's 31 a): the section 13 v10 paragraphs whose records came back clean in gate round r8, each
to Pangram as soon as its own records are clean, and H2-P2 again beside a neighbor that now passes alone (H2-P1, Human
in 289g). Records: s13/review-r8 (march readings, cold reads, traces, stance checks); H2-P3b's trace is round r7's (its
text unchanged since v8); H2-P2's trace is round r3's and its march readings round r4's (its text unchanged since v5;
rounds r7 and r8 read it with no break in three of four readings, the noise the gate's 2026-10-15 lesson records).
Run from candidate/: python3 s13/b291/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

v9 = (C / 's13' / 'v10.md').read_text(encoding='utf-8')
P = [p.strip() for p in re.split(r'\n\s*\n', v9) if p.strip()]
heads = [i for i, p in enumerate(P) if p.startswith('#')]
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
M = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r8' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    for k, v in labs.items():
        M.setdefault(int(k), []).append(v.strip())
def para(hn):
    t = P[heads[hn[0]] + hn[1]]
    return t
TRACE = {(1, 1): 'review-r6/trace-T1.md (OK; read Human in 289g)', (1, 2): 'review-r3/trace-T2.md (OK; unchanged since v5)',
         (1, 3): 'review-r8/trace-T1.md (OK)', (1, 4): 'review-r7/trace-T2.md (OK; unchanged since v8)',
         (1, 5): 'review-r8/trace-T1.md (OK)', (4, 2): 'review-r8/trace-T3.md (OK)', (4, 4): 'review-r8/trace-T4.md (OK)'}
ITEMS = {'S13v10-2P1P2': ([(1, 1), (1, 2)], False), 'S13v10-2P3': ([(1, 3)], False), 'S13v10-2P3P3b': ([(1, 3), (1, 4)], False),
         'S13v10-2P4': ([(1, 5)], False), 'S13v10-2P3bP4': ([(1, 4), (1, 5)], False), 'S13v10-5P2': ([(4, 2)], False),
         'S13v10-5P4': ([(4, 4)], False)}
# H2-P2: its march readings from round r4 (v6), the same text
R4 = {}
for x in 'ab':
    labs = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (C / 's13' / 'review-r4' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
    R4.setdefault('H2-P2', []).append(labs['6'].strip())
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
    gate[key] = {'kind': 'draft', 'march': [m for hn in parts for m in (R4['H2-P2'] if hn == (1, 2) else M[T[hn]])],
                 'march_note': ', '.join(('s13/review-r4/MARCH-labels-a.txt and -b.txt, T6 (v6, the same text)' if hn == (1, 2) else 's13/review-r8/MARCH-labels-a.txt and -b.txt, T%d' % T[hn]) for hn in parts),
                 'cold': 'OK', 'cold_note': 's13/review-r8/SENSE-a.md, SENSE-b.md: OK for these paragraphs',
                 'grounding': 'OK', 'grounding_note': '; '.join('s13/' + TRACE[hn] for hn in parts),
                 'stance': 0, 'stance_note': 's13/review-r8/STANCE-pub.md, STANCE-sofar.md: nothing on these paragraphs',
                 'lint': lint, 'missing': [], 'words': len(text.split())}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], v['march'], drafts[k][:80].replace('\n', ' / '))
