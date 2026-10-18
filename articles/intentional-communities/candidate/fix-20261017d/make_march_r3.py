"""March round r3 (2026-10-17 night): section 13's conflict paragraph with its last question kept (round r2 found no break
without it), before (v35) and after (the final v36). Run from the repo root:
python3 articles/intentional-communities/candidate/fix-20261017d/make_march_r3.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

blocks = lambda md: [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]
a = blocks((C / 's13' / 'v35.md').read_text(encoding='utf-8'))
b = blocks((C / 's13' / 'v36.md').read_text(encoding='utf-8'))
pick = [(x, y) for x, y in zip(a, b) if x != y and y.startswith('Also, don')]
assert len(pick) == 1
M = HERE / 'march-r3'
M.mkdir(exist_ok=True)
ids = ['s13-c2-was', 's13-c2-new']
(M / 'march-in.md').write_text('\n\n'.join(plain(t) for p in pick for t in p) + '\n', encoding='utf-8')
(M / 'march-ids.json').write_text(json.dumps(ids, indent=1) + '\n', encoding='utf-8')
subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py'), 'march', str(M / 'march-in.md'),
                str(M / 'MARCH-PROMPT.txt'), '--style', str(C.parent / 'STYLE.json'), '--about',
                'a friendly first-person article about starting an intentional community'], check=True)
