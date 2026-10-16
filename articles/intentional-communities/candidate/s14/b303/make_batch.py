"""Batch 303g (2026-10-16): section 14 draft v3 as screens (E175). v3 is v2 with round r3's fixes (make_v3.py,
review-r3/DISPOSITIONS-r3.md) and four endings for P6 and P7 (W1, W2, W3, W5), which read AI together in v2 (301g, 302g).
Each ending's march read is in the section around it (review-r4/MARCH-labels-W*-a.txt and -b.txt: read alone, without the
section, the review-r2b rewrites' P6 had no break). Lint REVIEW, keys PASS for every ending. Groups of at least 50 words: the
heading with P1 and P2, P2 alone, P5, and for each ending whose two readings both see a break in every paragraph: P6 with
P7, P5 to P7, and the whole section. Run from candidate/: python3 s14/b303/make_batch.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

R4 = C / 's14' / 'review-r4'


def section(w):
    bl = [b.strip() for b in re.split(r'\n\s*\n', (C / 's14' / ('v3-%s.md' % w)).read_text(encoding='utf-8')) if b.strip()]
    bl = [b for b in bl if not b.startswith('[image')]
    assert bl[0] == '# Dissolution and Exit' and len(bl) == 8
    return dict(zip(['H', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'], [plain(b) for b in bl]))


def labels(w):
    out = {}
    for x in 'ab':
        f = R4 / ('MARCH-labels-%s-%s.txt' % (w, x))
        if not f.exists():
            return None
        for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', f.read_text(encoding='utf-8'), re.M):
            out.setdefault('P' + k, []).append(v)
    return out if all(len(out.get('P%d' % i, [])) == 2 for i in range(1, 8)) else None


ENDINGS = [w for w in ('W1', 'W2', 'W3', 'W5') if labels(w) and all('B' in m.split() for v in labels(w).values() for m in v)]
GROUPS = {'S14v3-1P12': ('W1', ['H', 'P1', 'P2']), 'S14v3-P2': ('W1', ['P2']), 'S14v3-P5': ('W1', ['P5'])}
for w in ENDINGS:
    GROUPS['S14v3%s-P67' % w] = (w, ['P6', 'P7'])
    GROUPS['S14v3%s-P567' % w] = (w, ['P5', 'P6', 'P7'])
    GROUPS['S14v3%s' % w] = (w, ['H', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'])
drafts, gate = {}, {}
for k, (w, parts) in GROUPS.items():
    P, M = section(w), labels(w)
    drafts[k] = '\n\n'.join(P[x] for x in parts)
    gate[k] = {'kind': 'screen', 'march': [m for x in parts if x != 'H' for m in M[x]],
               'march_note': 's14/review-r4/MARCH-labels-%s-a.txt and -b.txt: %s' % (w, ', '.join(x for x in parts if x != 'H')),
               'lint': 'REVIEW', 'lint_note': 's14/LINT-v3-%s.txt' % w, 'keys': 'PASS', 'words': len(drafts[k].split())}
    assert gate[k]['words'] >= 50, k
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b303.js'), '--name', 'B303'] + list(GROUPS), capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-800:])
print('endings:', ENDINGS)
for k in GROUPS:
    print(k, gate[k]['words'], drafts[k][:90].replace('\n', ' / '))
