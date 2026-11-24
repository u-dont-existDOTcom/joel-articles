#!/usr/bin/env python3
"""The receipt for "Twin Flames?" with "Senegal" spelled as he asked on 2026-11-24 ("senegal should be corrected"): every
fill carried over by its words from the junk pass's receipt of the same section (r38/junk/receipts/), the one changed
sentence's from its old spelling."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
prev = json.loads((HERE.parents[1] / 'r38' / 'junk' / 'receipts' / 'R-r38-64-twin-flames.json').read_text(encoding='utf-8'))
have = {s['s'].replace('Sênêgal', 'Senegal'): s for s in prev['sentences']}
text = next((HERE.parent / 'checks').glob('CHECK-r40-64-*.txt'))
out = HERE / 'R-r40-64-twin-flames.json'
subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--section',
                prev['section'], '--reader', prev['reader'], '--out', str(out)], check=True, capture_output=True)
R = json.loads(out.read_text(encoding='utf-8'))
for s in R['sentences']:
    old = have[s['s']]
    for f in ('payoff', 'follows', 'link'):
        if f in old:
            s[f] = old[f]
for f in ('placement', 'same_point', 'questions', 'needed', 'his_fixes', 'fit', 'checked'):
    R[f] = prev[f]
R['opens']['why_reading'] = prev['opens']['why_reading']
out.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                   capture_output=True, text=True)
print((r.stdout + r.stderr).strip().replace('\n', ' | ')[:600])
