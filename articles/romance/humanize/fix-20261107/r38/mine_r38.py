#!/usr/bin/env python3
"""My tested change of this round as a layer after HIS-T7.json: MINE-R38.json, which whole/build.py applies.

- Section 42, "From flow to nitty gritty": its last clause, "without manipulating based on all that expert “management”",
  which a fresh reader couldn't parse (junk-read B210), said from his answer to the seventh page's Q-42 ("Bee would
  accuse me of manipulating her, even though I was making an effort not to, and ironically she actually wanted me to
  manipualte her more"): "without ever manipulating her", then his story as its case, in his words. The section with it
  read Human High, one window (https://www.pangram.com/history/2d6004a1-e6e4-4270-9f50-2fb4f96c8d13). The rest of the
  paragraph is r32's text, which the ledger's best try kept; r37's two plainer phrases go with the clause.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
repl = {int(k): v for k, v in json.loads((FIX / 'whole' / 'REPLACEMENTS.json').read_text(encoding='utf-8')).items()}
# REPLACEMENTS.json holds this layer once whole/build.py has run with it: take it back out first
if (HERE / 'MINE-R38.json').exists():
    for ch in reversed(json.loads((HERE / 'MINE-R38.json').read_text(encoding='utf-8'))['changes']):
        now = repl[ch['live']]
        k = now.index(ch['after'][0])
        repl[ch['live']] = now[:k] + [ch['before']] + now[k + 1:]
new = (HERE / 't42' / 'r36-42-from-flow-to-nitty-gritty.txt').read_text(encoding='utf-8').split('\n\n')
before = repl[199][1]
assert before.startswith('Dealing with somebody else’s emotional insecurities'), before[:60]
assert repl[199][0] == new[0], 'the opening is try 3s, as the check had it'
changes = [{'card': 'R38-42', 'kind': 'para', 'live': 199, 'before': before, 'after': [new[1]],
            'his_checks': ['https://www.pangram.com/history/2d6004a1-e6e4-4270-9f50-2fb4f96c8d13'],
            'why': 'the clause a reader couldn\'t parse, said from his answer to Q-42 (seventh page), with his story as its case'}]
(HERE / 'MINE-R38.json').write_text(json.dumps({
    'about': 'My tested change of 2026-11-24 (r38): section 42\'s last clause from his answer to Q-42; a layer after '
             'r38/HIS-T7.json.', 'whose': 'mine', 'changes': changes}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('MINE-R38:', len(changes), 'change')
