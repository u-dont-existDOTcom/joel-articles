#!/usr/bin/env python3
"""The receipt for section 42's try 5 (r36-42-from-flow-to-nitty-gritty.txt): its last sentence said from his answer to
the seventh page's Q-42 ("Bee would accuse me of manipulating her, even though I was making an effort not to, and
ironically she actually wanted me to manipualte her more"). The fills are carried over by their words from try 3's
receipt (r37/medium/t5/) and r32's, and mine for the two sentences this try changes or adds."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
K = 'r36-42-from-flow-to-nitty-gritty'
FILL = {
    'All that works wonderfully until I’m in a romantic relationship and suddenly I’m expected to mind-read, silences included, and check in constantly, without ever manipulating her.': (
        'they see what a relationship suddenly asks of someone used to living alone: reading her mind and her silences, checking in all the time, and never manipulating her.',
        'it turns from the freedom of living alone to what a relationship asks.', 'All that works'),
    'Bee would accuse me of manipulating her even when I was making an effort not to, and ironically, she actually wanted me to manipulate her more.': (
        'they see how hard the last of those demands can be: he was accused of manipulating her while trying not to, by someone who wanted more of it.',
        'it gives his own case of the last demand in the sentence before.', 'Bee would accuse me of manipulating'),
}
prev = json.loads((HERE.parents[1] / 'r37' / 'medium' / 't5' / ('R-%s.json' % K)).read_text(encoding='utf-8'))
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
        print('NO FILL:', s['s'])
for f in ('placement', 'same_point', 'questions', 'needed', 'his_fixes', 'fit'):
    R[f] = prev[f]
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
print((r.stdout + r.stderr).strip().replace('\n', ' | ')[:600])
