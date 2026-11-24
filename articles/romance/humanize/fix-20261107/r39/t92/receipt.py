#!/usr/bin/env python3
"""The receipt for "Tough Love", part 1, with B476 and B478 said from his answers on the eighth page: "yes, i mean a
passionate romantic relationship that's also stable" and "because Somé saw the universe as good, saw everyone as
naturally good when in their natural environment/flowing with life the way our ancestors showed us. so both my parents
and Somé were like that, trusting the universe". The fills are carried over by their words from the junk pass's second
try (r38/junk/t2/), and mine for the two sentences his answers change."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
K = 'r38-92-tough-love-p1'
FILL = {
    'A passionate romantic relationship that’s also stable is rare, and that’s probably why romantic love has been seen with suspicion as a destabilizing force throughout history.': (
        'they see why romance has long been distrusted: a passionate relationship that also stays stable is rare.',
        'it turns from what makes romance hard to sell to why it has been distrusted.', 'A passionate romantic relationship'),
    'And like Somé, who saw everyone as naturally good in their natural environment, flowing with life the way our ancestors showed us, they trusted the universe, rose-colored glasses and all, and taught me that everybody was basically good.': (
        'they see where his parents\' trust in people came from, the same trust Somé had, and why it left him unready.',
        'it gives a second way his parents were like Somé, after their agreeing with her on community.', 'And like Somé'),
}
prev = json.loads((HERE.parents[1] / 'r38' / 'junk' / 't2' / ('R-%s.json' % K)).read_text(encoding='utf-8'))
have = {s['s']: s for s in prev['sentences']}
out = HERE / ('R-%s.json' % K)
subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / (K + '.txt')),
                '--section', prev['section'], '--reader', prev['reader'], '--out', str(out)], check=True, capture_output=True)
R = json.loads(out.read_text(encoding='utf-8'))
for s in R['sentences']:
    if s['s'] in FILL:
        s['payoff'], s['follows'], s['link'] = FILL[s['s']]
    elif s['s'] in have:
        for f in ('payoff', 'follows', 'link'):
            s[f] = have[s['s']][f]
    else:
        print('NO FILL:', s['s'][:90])
for f in ('placement', 'same_point', 'questions', 'needed', 'his_fixes', 'fit'):
    R[f] = prev[f]
R['questions']['Q3'] = ('PASS: "A passionate romantic relationship that’s also stable" and the Somé link are said from his answers on '
                        'the eighth page; the rest names its things where they come')
R['opens']['why_reading'] = prev['opens']['why_reading']
keep = {s['s'] for s in R['sentences']}
R['needed']['unneeded'] = [u for u in R['needed']['unneeded'] if u in keep]
R['needed']['kept'] = {u: v for u, v in R['needed']['kept'].items() if u in keep}
for read in ('his_fixes', 'fit'):
    R[read]['marked'] = [m for m in R[read]['marked'] if m['s'] in keep]
    R[read]['kept'] = {u: v for u, v in R[read]['kept'].items() if u in keep}
out.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(HERE / (K + '.txt')), str(out)],
                   capture_output=True, text=True)
print((r.stdout + r.stderr).strip().replace('\n', ' | ')[:500])
