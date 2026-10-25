#!/usr/bin/env python3
"""Turn 110: fill GATE.md's results table from GATE-OUTCOMES.json and the reviews (run after run_gate.py)."""
import json
import pathlib

E = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t110-gate/'

HERE = pathlib.Path(__file__).resolve().parent
res = json.loads((HERE / 'GATE-OUTCOMES.json').read_text(encoding='utf-8'))
lines = ['| Name | Preservation | Cold read 1 | Cold read 2 | The gate |', '|---|---|---|---|---|']
for n, r in res.items():
    v = r['reviews']
    lines.append('| %s | %s | %s | %s | %s |' % (n, v['preservation'], v['cold_read_1'], v['cold_read_2'],
                                               ('admitted ([the sentence](%s%s/FOR-JOEL.txt), [its proof](%s%s/FOR-JOEL.proof.json))' % (E, n, E, n)) if r['admitted'] else 'blocked: ' + r['gate'][:200].replace('|', '/')))
notes = ('\n\nThe reviewers\' own notes outside the changes, for a later pass: in Don\'t Give the Inner Adult Away, the paragraph before P2 has '
         '"makes me more grounded, truthful, and free", a "me" in a paragraph that otherwise says "you" (preservation and cold read 1); '
         'and the preservation reviewer couldn\'t check from P6\'s section alone whether another section recommends forgiving a parent or '
         'picturing their childhood (How to Forgive Without Forgetting is the one that discusses it). Cold read 1 also reported that a hook had '
         'added the repository\'s [AGENTS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/AGENTS.md) to its context, so each reviewer had that file too, beside the brief and its files; it says '
         'nothing about these drafts. The first cold reader 2 ran out of output room before writing anything, and a second one, in a '
         'fresh context with its own context id, wrote the cold-read-2 reports.')
p = HERE / 'GATE.md'
s = p.read_text(encoding='utf-8')
assert 'RESULTS_TABLE' in s
p.write_text(s.replace('RESULTS_TABLE', '\n'.join(lines) + notes), encoding='utf-8')
print('\n'.join(lines))
