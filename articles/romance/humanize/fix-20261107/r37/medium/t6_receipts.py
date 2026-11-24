#!/usr/bin/env python3
"""The receipt for the fourth try of section 67 (t6/<key>.txt): the writer's full fix of the first and last Medium
windows (texts/, which the near-miss rule held back until two small tries had been checked), with the r32 confidants
paragraph whose two small changes both read Low, its two halves joined with ", but". The fills are carried over by their
words from the section's earlier receipts, and mine for the joined sentence."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
K = 'r36-67-two-pillars-don-t-hold-the-roof-up-p1'
FILL = {
    'Sometimes you need privacy from your partner and somewhere else to say what you’re feeling, but if your confidant doesn’t have a good connection with your partner, the conversation can turn into an echo chamber very easily.': (
        'they see both sides of a separate confidant: privacy and somewhere to say what they feel, and an echo chamber if the confidant has no connection with their partner.',
        'it says how the confidants of the sentence before help and how they harm.', 'none: no words at its start tie it back; it gives the help and the harm the sentence before names'),
}
have = {}
for src in ('t5', 'small', 'receipts'):
    prev = json.loads((HERE / src / ('R-%s.json' % K)).read_text(encoding='utf-8'))
    have.update({s['s']: s for s in prev['sentences']})
base = json.loads((HERE / 'receipts' / ('R-%s.json' % K)).read_text(encoding='utf-8'))
out = HERE / 't6' / ('R-%s.json' % K)
subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / 't6' / (K + '.txt')),
                '--section', base['section'], '--reader', base['reader'], '--out', str(out)], check=True, capture_output=True)
R = json.loads(out.read_text(encoding='utf-8'))
for s in R['sentences']:
    if s['s'] in FILL:
        s['payoff'], s['follows'], s['link'] = FILL[s['s']]
    elif s['s'] in have:
        for f in ('payoff', 'follows', 'link'):
            s[f] = have[s['s']][f]
    else:
        print('NO FILL:', s['s'])
for f in ('placement', 'same_point', 'questions', 'needed', 'his_fixes', 'fit'):
    R[f] = base[f]
R['opens']['why_reading'] = base['opens']['why_reading']
keep = {s['s'] for s in R['sentences']}
R['needed']['unneeded'] = [u for u in R['needed']['unneeded'] if u in keep]
R['needed']['kept'] = {u: v for u, v in R['needed']['kept'].items() if u in keep}
for read in ('his_fixes', 'fit'):
    R[read]['marked'] = [m for m in R[read]['marked'] if m['s'] in keep]
    R[read]['kept'] = {u: v for u, v in R[read]['kept'].items() if u in keep}
out.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(HERE / 't6' / (K + '.txt')), str(out)],
                   capture_output=True, text=True)
print((r.stdout + r.stderr).strip().replace('\n', ' | ')[:600])
