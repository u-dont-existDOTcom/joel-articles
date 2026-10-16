"""Batch 294g (2026-10-15, after Joel's 32 b): the section 13 paragraphs whose records came back clean in gate round r11
(s13/review-r11/, DISPOSITIONS-r11.md). H1-P2 from Emulate round g (v17) alone, after H1-P1, and with the section's heading
over both; H3-P1 in its three ways (A in v17, B in v17b, C in v17c), each alone and under "Resources, Land, and Exit Terms";
H4-P5 with the founding-agreements fix (v15), alone. Run from candidate/: python3 s13/b294/make_batch.py
"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
R = C / 's13' / 'review-r11'
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402


def blocks(fn):
    return [p.strip() for p in re.split(r'\n\s*\n', (C / 's13' / fn).read_text(encoding='utf-8')) if p.strip()]


def labels(fn):
    return dict((int(k), v.strip()) for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+)\s*$', (R / fn).read_text(), re.M))


V = {'A': blocks('v17.md'), 'B': blocks('v17b.md'), 'C': blocks('v17c.md')}
P = V['A']
heads = [i for i, p in enumerate(P) if p.startswith('#')]
order = [(h, n) for h in range(len(heads)) for n in range(1, (heads[h + 1] if h + 1 < len(heads) else len(P)) - heads[h])]
T = {hn: i + 1 for i, hn in enumerate(order)}
MA, MB = labels('MARCH-labels-a.txt'), labels('MARCH-labels-b.txt')
VA, VB = labels('MARCH-variants-labels-a.txt'), labels('MARCH-variants-labels-b.txt')
COLD = {'A': 'SENSE-a.md, SENSE-b.md (v17)', 'B': 'SENSE-B-a.md, SENSE-B-b.md (v17b)', 'C': 'SENSE-C-a.md, SENSE-C-b.md (v17c)'}
TRACE = {(0, 1): 'review-r7/trace-T1.md (OK; unchanged since v9)', (0, 2): 'review-r11/trace-T1.md (OK)',
         (2, 1): 'review-r11/trace-T1.md (OK)', (3, 5): 'review-r11/trace-T3.md (its one finding, "Yes, it\'s a lot of homework!", kept: review-r11/DISPOSITIONS-r11.md)'}


def para(way, hn):
    return V[way][heads[hn[0]] + hn[1]]


def march(way, hn):
    if way == 'A' or hn != (2, 1):
        return [MA[T[hn]], MB[T[hn]]]
    k = {'B': 1, 'C': 2}[way]
    return [VA[k], VB[k]]


ITEMS = {'S13v17-1P2': ('A', [(0, 2)], False), 'S13v17-1P1P2': ('A', [(0, 1), (0, 2)], False),
         'S13v17-1hP1P2': ('A', [(0, 1), (0, 2)], True),
         'S13v17-3P1': ('A', [(2, 1)], False), 'S13v17-3hP1': ('A', [(2, 1)], True),
         'S13v17b-3P1': ('B', [(2, 1)], False), 'S13v17b-3hP1': ('B', [(2, 1)], True),
         'S13v17c-3P1': ('C', [(2, 1)], False), 'S13v17c-3hP1': ('C', [(2, 1)], True),
         'S13v17-4P5': ('A', [(3, 5)], False)}
drafts, gate = {}, {}
for key, (way, parts, with_head) in ITEMS.items():
    md = [para(way, hn) for hn in parts]
    if with_head:
        md = [V[way][heads[parts[0][0]]]] + md
    text = '\n\n'.join(plain(x) for x in md)
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write('\n\n'.join(x for x in md if not x.startswith('#')) + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    lint = re.search(r'verdict: (\w+)', r.stdout).group(1)
    drafts[key] = text
    g = {'kind': 'draft', 'march': [m for hn in parts for m in march(way, hn)],
         'march_note': 's13/review-r11/' + ('MARCH-labels-a.txt and -b.txt, ' + ', '.join('T%d' % T[hn] for hn in parts)
                                            if way == 'A' else 'MARCH-variants-labels-a.txt and -b.txt, T%d' % {'B': 1, 'C': 2}[way]),
         'cold': 'OK', 'cold_note': 's13/review-r11/' + COLD[way] + ': OK for these paragraphs',
         'grounding': 'OK', 'grounding_note': '; '.join('s13/' + (TRACE[hn] if way == 'A' or hn != (2, 1)
                                                                   else 'review-r11/trace-T4.md (way %s: OK)' % way) for hn in parts),
         'stance': 0, 'stance_note': 's13/review-r11/STANCE-pub.md, STANCE-sofar.md: no conflicts in these paragraphs',
         'lint': lint, 'missing': [], 'words': len(text.split())}
    if way != 'A':
        g['stance'] = 'same claims as S13v17-3P1'
        g['stance_note'] = 'way %s makes the same claims as way A (trace T4: every clause EQUIVALENT to the published)' % way
    gate[key] = g
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, v in gate.items():
    print(k, v['words'], v['lint'], v['march'], drafts[k][:70].replace('\n', ' / '))
