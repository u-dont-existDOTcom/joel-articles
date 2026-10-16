"""Batch 306g (2026-10-16): section 14 draft v5 (make_v5.py) as drafts, every record complete. v4 is v3 with ending W2, which
read Human in every group as a screen (303g), and round r5's two P2 fixes (the published "childcare and schooling" and
"bridging ... food, housing and care"). Records: march review-r4 (ending W2, in the section around it), cold reads review-r5
(OK for all seven paragraphs of v3 with W2), traces review-r3 and review-r5 with their dispositions, stance review-r3 (no
conflicts; v3 and v4 put published words back and their endings make the same claims), repeats review-r3 (answered in
DISPOSITIONS-r3.md), lint REVIEW and keys PASS on v4. Groups of at least 50 words, then the whole section. Only the whole section runs: every group's text is one that 305g or 305g-x already read Human (same SHA-256).
Run from candidate/: python3 s14/b306/make_batch.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

S14 = C / 's14'
bl = [b.strip() for b in re.split(r'\n\s*\n', (S14 / 'v5.md').read_text(encoding='utf-8')) if b.strip()]
bl = [b for b in bl if not b.startswith('[image')]
assert bl[0] == '# Dissolution and Exit' and len(bl) == 8
P = dict(zip(['H', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'], [plain(b) for b in bl]))
M = {}
for x in 'ab':
    for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (S14 / 'review-r4' / ('MARCH-labels-W2-%s.txt' % x)).read_text(), re.M):
        M.setdefault('P' + k, []).append(v)
TRACE = {'P1': 's14/review-r5/trace-T1.md ("Who would?" kept, review-r3/DISPOSITIONS-r3.md and review-r5/DISPOSITIONS-r5.md)',
         'P2': 's14/review-r5/trace-T1.md (its SHIFT and LOST fixed in v4 with the published words; "That\'s a lot of loose ends!" kept)',
         'P3': 's14/review-r3/trace-T2.md (OK)',
         'P4': 's14/review-r3/trace-T2.md ("Who wants that?" kept, DISPOSITIONS-r3.md)',
         'P5': 's14/review-r5/trace-T2.md (OK)',
         'P6': 's14/review-r5/trace-T2.md ("(as you may have noticed!)" kept, DISPOSITIONS-r5.md)',
         'P7': 's14/review-r5/trace-T2.md ("I hope so, anyway." kept, DISPOSITIONS-r5.md)'}
GROUPS = {'S14v5-1P12': ['H', 'P1', 'P2'], 'S14v5-P2': ['P2'], 'S14v5-P34': ['P3', 'P4'], 'S14v5-P5': ['P5'],
          'S14v5-P67': ['P6', 'P7'], 'S14v5-P567': ['P5', 'P6', 'P7']}
drafts, gate = {}, {}
for k, parts in GROUPS.items():
    md = '\n\n'.join(bl[['H', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'].index(x)] for x in parts if x != 'H')
    f = HERE / ('lint-%s.md' % k); f.write_text(md + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), str(f)], capture_output=True, text=True)
    f.unlink()
    drafts[k] = '\n\n'.join(P[x] for x in parts)
    ps = [x for x in parts if x != 'H']
    gate[k] = {'kind': 'draft', 'march': [m for x in ps for m in M[x]],
               'march_note': 's14/review-r4/MARCH-labels-W2-a.txt and -b.txt: ' + ', '.join(ps),
               'cold': 'OK', 'cold_note': 's14/review-r5/SENSE-a.md, SENSE-b.md: OK for all seven paragraphs (v3 with W2)',
               'grounding': 'OK', 'grounding_note': '; '.join(TRACE[x] for x in ps),
               'stance': 0, 'stance_note': 's14/review-r3/STANCE-pub.md, STANCE-sofar.md: no conflicts; v3 and v4 put published words back',
               'lint': re.search(r'verdict: (\w+)', r.stdout).group(1), 'keys': 'PASS', 'missing': [],
               'words': len(drafts[k].split())}
    assert gate[k]['words'] >= 50, k
drafts['S14v5'] = '\n\n'.join(P[x] for x in ['H', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'])
gate['S14v5'] = {'kind': 'section', 'parts': ['S14v5-1P12', 'S14v5-P34', 'S14v5-P567'], 'repeats': 0,
                 'repeats_note': 's14/review-r3/REPEATS.md, answered in s14/review-r3/DISPOSITIONS-r3.md (1 fixed, 5 kept)'}
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b306.js'), '--name', 'B306'] + ['S14v5'], capture_output=True, text=True)
print(r.stdout[-1800:], r.stderr[-800:])
