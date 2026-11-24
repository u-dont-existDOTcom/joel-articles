#!/usr/bin/env python3
"""Receipts for r41's checks of texts with a change of mine in them: the Labels section with Q-C1's words (fills carried
over by their words from the junk pass's receipt, mine for the changed sentence), and part 1 of "Primal attraction" with
"in recent years" (his Q-S5 answer; fills carried from r40's)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FIX = HERE.parents[1]
JOBS = [
    ('09', FIX / 'r38' / 'junk' / 'receipts' / 'R-r38-09-labels-are-descriptive-not-prescriptive.json', {
        'I don’t need to promise that on paper, and if a promise had to stand in for that closeness, that would be more like a red flag.': (
            'a written promise of help is a red flag when it stands in for the closeness that should make it unnecessary',
            'it says what the readiness just described needs, and doesn\'t, from paper',
            'I don’t need to promise')}, {}),
    ('52', FIX / 'r40' / 'primal' / 'R-52.json', {}, {'in recent years': 'in modern years'}),
]
for k, prev_path, NEW, BACK in JOBS:
    prev = json.loads(prev_path.read_text(encoding='utf-8'))
    have = {s['s']: s for s in prev['sentences']}
    text = next((FIX / 'r41' / 'checks').glob('CHECK-r41-%s-*.txt' % k))
    out = HERE / ('R-r41-%s.json' % k)
    subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--section',
                    prev['section'], '--reader', prev['reader'], '--out', str(out)], check=True, capture_output=True)
    R = json.loads(out.read_text(encoding='utf-8'))
    for s in R['sentences']:
        if s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
            continue
        key = s['s']
        for a, b in BACK.items():
            key = key.replace(a, b)
        old = have.get(key)
        assert old, ('NO FILL', k, s['s'][:80])
        for f in ('payoff', 'follows', 'link'):
            if f in old:
                s[f] = old[f]
    for f in ('placement', 'same_point', 'questions', 'needed', 'his_fixes', 'fit', 'checked'):
        if f in prev:
            R[f] = prev[f]
    R['opens']['why_reading'] = prev['opens']['why_reading']
    keep = {s['s'] for s in R['sentences']}
    if isinstance(R.get('his_fixes'), dict):
        for read in ('his_fixes', 'fit'):
            R[read]['marked'] = [m for m in R[read].get('marked', []) if m['s'] in keep]
            R[read]['kept'] = {u: v for u, v in R[read].get('kept', {}).items() if u in keep}
    if NEW:
        R['questions']['Q1'] = ('PASS: the changed sentence says first that he needs no promise on paper, then when one would '
                                'be a red flag (his answer on Q-C1: "right you are correct")')
    out.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    print(k, (r.stdout + r.stderr).strip().replace('\n', ' | ')[:500])
