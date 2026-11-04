#!/usr/bin/env python3
"""Batch 2 units from r01.md: LGF (the fuels stretch under Leaky gut, which stays there: Joel's s3/G4), ST1 and ST2
(the Optional Ready-Made Gut Stacks section, split to stay inside the API's six-paragraph limit), and NX (his NOTE
with the approved G1 explainer, checked as it is). Writes UNITS-r01-b2.json. No API calls."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r01' / 'r01.md').read_text(encoding='utf-8')
lines = md.split('\n')


def between(start, stop):
    i = next(n for n, l in enumerate(lines) if l.lstrip().startswith(start))
    j = next(n for n, l in enumerate(lines) if n > i and l.lstrip().startswith(stop))
    return '\n'.join(lines[i:j]).strip()


u = {
    'LGF': between('- Mitochondrial & Cellular Energy Starvation', '- IBS (Phase 4)'),
    'ST1': between('## Optional Ready-Made Gut Stacks', 'The best general commercial stack'),
    'ST2': between('The best general commercial stack', '### Paid Subscribers'),
    'NX': between('I have consolidated the top 9', 'This protocol is designed'),
}
(HERE / 'UNITS-r01-b2.json').write_text(json.dumps(u, ensure_ascii=False, indent=1), encoding='utf-8')
for k, v in u.items():
    print(k, len(v.split()), 'words |', v[:80].replace('\n', ' / '))
