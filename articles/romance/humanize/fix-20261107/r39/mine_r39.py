#!/usr/bin/env python3
"""My tested change of this round as a layer after HIS-T8.json: MINE-R39.json, which whole/build.py applies.

- "Tough Love", part 1: B476 and B478 said from his answers on the eighth page ("yes, i mean a passionate romantic
  relationship that's also stable"; "because Somé saw the universe as good, saw everyone as naturally good when in
  their natural environment/flowing with life the way our ancestors showed us. so both my parents and Somé were like
  that, trusting the universe"), in his words. The section with them read Human High, one window
  (https://www.pangram.com/history/1b53e70a-1249-449a-a802-bed1dda0dab2).
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
plain = lambda t: re.sub(r'\[([^\]]+)\]\((?:[^()\s]|\([^()\s]*\))+\)', r'\1', t)
repl = {int(k): v for k, v in json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8')).items()}
if (HERE / 'MINE-R39.json').exists():   # take this layer back out of REPLACEMENTS.json first
    for ch in reversed(json.loads((HERE / 'MINE-R39.json').read_text(encoding='utf-8'))['changes']):
        now = repl[ch['live']]
        k = now.index(ch['after'][0])
        repl[ch['live']] = now[:k] + [ch['before']] + now[k + 1:]
post = {}
for line in (FIX / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        post[r['n']] = r['text']
cur = lambda n: repl.get(n, [post[n]])
old = (FIX / 'r38' / 'checks' / 'CHECK-r38-92-tough-love-p1.txt').read_text(encoding='utf-8').strip().split('\n\n')
new = (HERE / 't92' / 'r38-92-tough-love-p1.txt').read_text(encoding='utf-8').strip().split('\n\n')
changes = []
for i, (o, n) in enumerate(zip(old, new)):
    if o == n:
        continue
    hits = [(m, j) for m in post for j, x in enumerate(cur(m)) if norm(plain(x)) == norm(o)]
    assert len(hits) == 1, (o[:60], hits)
    live, j = hits[0]
    before = cur(live)[j]
    assert '](' not in before, 'a link in the paragraph: put it back'
    changes.append({'card': 'R39-92', 'kind': 'para', 'live': live, 'before': before, 'after': [n],
                    'his_checks': ['https://www.pangram.com/history/1b53e70a-1249-449a-a802-bed1dda0dab2'],
                    'why': 'said from his answer on the eighth page (Q-B476 or Q-B478), in his words'})
(HERE / 'MINE-R39.json').write_text(json.dumps({
    'about': 'My tested change of 2026-11-24 (r39): Tough Love\'s B476 and B478 from his eighth-page answers; a layer '
             'after r39/HIS-T8.json.', 'whose': 'mine', 'changes': changes}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('MINE-R39:', len(changes), 'changes:', [c['live'] for c in changes])
