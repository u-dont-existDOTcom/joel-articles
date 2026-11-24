#!/usr/bin/env python3
"""Receipts for the junk pass's second tries (t2/<key>.txt) of the three sections whose first try read one short Medium
window (34 "Your mom and dad?", 89 "Both people should get a chance to speak ...", 92 "They're suspicious of romance."):
the fills carried over by their words from the first try's receipt (its fresh reads and my verdicts), and mine for the
joined sentences. 92 is the article's text with only B477's fix and the join: B476 and B478 go to him as questions."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[6]
FILL = {
    'Who else is going to do it, your mom and dad?': (
        'they see that no one but a partner is placed to help them grow as adults.',
        'it asks who else would help them grow, after the claim that partners should.', 'Who else is going'),
    'And when you do ask friends for help, do it fairly, with the goal of resolving the conflict, not just getting approval for your own interpretation: both people should get a chance to speak, and good friends should hear both sides before validating either.': (
        'they bring a conflict to friends to resolve it, letting both people speak and asking friends to hear both sides first.',
        'it says how to ask the friends of the sentence before for help, and what fair means.', 'And when you do ask friends'),
    'To her people, marriage is an arranged, ritualized spiritual and communal responsibility, and they’re suspicious of romance.': (
        'they see how Somé\'s people treat marriage, and that they distrust romance.',
        'it says what her people believe, after naming where Somé came from.', 'To her people'),
    'A relationship like this is rare, and that’s probably why romantic love has been seen with suspicion as a destabilizing force throughout history.': (
        'they see why romance has long been distrusted: working ones are rare.',
        'it turns from what makes romance work to why it has been distrusted.', 'none: no words at its start tie it back; it turns from what makes romance work to why it has been distrusted'),
    'Also reminiscent of Somé, they also wore rose-colored glasses and taught me that everybody was basically good.': (
        'they see the second thing his parents taught him, that everybody was basically good, which the next sentence says left him unready.',
        'it adds a second way his parents were like Somé, after their not being romantic.', 'Also reminiscent of Somé'),
}
for k in ('r38-34-seeing-idealization-right', 'r38-89-gaslighting-in-the-dark', 'r38-92-tough-love-p1'):
    prev = json.loads((HERE.parent / 'receipts' / ('R-%s.json' % k)).read_text(encoding='utf-8'))
    have = {s['s']: s for s in prev['sentences']}
    out = HERE / ('R-%s.json' % k)
    subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / (k + '.txt')),
                    '--section', prev['section'], '--reader', prev['reader'], '--out', str(out)], check=True, capture_output=True)
    R = json.loads(out.read_text(encoding='utf-8'))
    for s in R['sentences']:
        if s['s'] in FILL:
            s['payoff'], s['follows'], s['link'] = FILL[s['s']]
        elif s['s'] in have:
            for f in ('payoff', 'follows', 'link'):
                s[f] = have[s['s']][f]
        else:
            print('NO FILL:', k, s['s'][:90])
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
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(HERE / (k + '.txt')), str(out)],
                       capture_output=True, text=True)
    print(k[4:40], (r.stdout + r.stderr).strip().replace('\n', ' | ')[:500])
