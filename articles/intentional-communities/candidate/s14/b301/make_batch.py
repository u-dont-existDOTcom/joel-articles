"""Batch 301g (2026-10-16): section 14 draft v2 as screens (E175): Emulate round a's call A with the preservation keys and
Emulate's meaning slips put back (make_v1.py), and a break in each paragraph (make_v2.py), which both march readings now see
(review-r2/MARCH-labels-a.txt and -b.txt). Lint REVIEW, keys PASS. Screens go to Pangram before the meaning reviews; only those
that read Human go on to them, and a screen is never installed. Groups of at least 50 words: the heading with P1 and P2, P2
alone, P3 with P4, P5, P6 with P7, and the whole section. Run from candidate/: python3 s14/b301/make_batch.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

bl = [b.strip() for b in re.split(r'\n\s*\n', (C / 's14' / 'v2.md').read_text(encoding='utf-8')) if b.strip()]
bl = [b for b in bl if not b.startswith('[image')]
assert bl[0] == '# Dissolution and Exit' and len(bl) == 8
P = dict(zip(['H', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'], [plain(b) for b in bl]))
la = (C / 's14' / 'review-r2' / 'MARCH-labels-a.txt').read_text(encoding='utf-8').split('\n')
lb = (C / 's14' / 'review-r2' / 'MARCH-labels-b.txt').read_text(encoding='utf-8').split('\n')
march = {'P%d' % i: [la[i - 1].split(': ', 1)[1], lb[i - 1].split(': ', 1)[1]] for i in range(1, 8)}
GROUPS = {'S14v2-1P12': ['H', 'P1', 'P2'], 'S14v2-P2': ['P2'], 'S14v2-P34': ['P3', 'P4'], 'S14v2-P5': ['P5'],
          'S14v2-P67': ['P6', 'P7'], 'S14v2': ['H', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']}
drafts, gate = {}, {}
for k, parts in GROUPS.items():
    drafts[k] = '\n\n'.join(P[x] for x in parts)
    gate[k] = {'kind': 'screen', 'march': [m for x in parts if x != 'H' for m in march[x]],
               'march_note': 's14/review-r2/MARCH-labels-a.txt and -b.txt: ' + ', '.join(x for x in parts if x != 'H'),
               'lint': 'REVIEW', 'lint_note': 's14/LINT-v2.txt', 'keys': 'PASS', 'words': len(drafts[k].split())}
    assert gate[k]['words'] >= 50, k
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b301.js'), '--name', 'B301'] + list(GROUPS), capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-800:])
for k in GROUPS:
    print(k, gate[k]['words'], drafts[k][:80].replace('\n', ' / '))
