#!/usr/bin/env python3
"""Receipts for the third tries (t3/<key>.txt): the fills carried over by their words from the section's last receipt,
and my fill for the sentence each try changes."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = {'r36-16-and-deeper-is-the-point': 'receipts', 'r36-20-dating-app-horror-show-p2': 'receipts',
       'r36-28-my-flaws-p2': 'small', 'r36-56-muses-directors-p3': 'small', 'r36-54-muses-directors-p1': 'receipts'}
FILL = {
    'But if the connection gets deep enough, sex appeal isn’t the basis of the relationship anymore.': (
        'they expect a deep enough connection to outlast sex appeal.', 'it turns from why sex matters to what holds when the connection is deep.', 'But if the connection'),
    'Girls are usually more selective, but they often go for guys who aren’t respectful or mature, so they need to think twice too.': (
        'they see that being selective doesn\'t protect girls from picking disrespectful or immature guys.', 'it turns the advice of the sentence before to girls.', 'Girls are usually more'),
    'Their meditations may have helped them a lot, but I still had no idea how either woman would act when a relationship got ugly, because if somebody starts with enough trauma, huge progress can still leave a lot unresolved.': (
        'they don\'t take someone\'s spiritual progress as proof of how they\'ll act when things get ugly, and see why.', 'it says what the meditation he saw couldn\'t tell him, and why.', 'Their meditations may have'),
    'I don’t think equality means dividing every role 50/50, so if I like driving and for her it’s cooking, great.': (
        'they split roles by what each likes, without counting halves.', 'it says what the initiative of the paragraph before means for equality.',
        'none: no words at its start tie it back; it says what the initiative of the paragraph before means for equality'),
    'One time, Bee said she almost got enlightened, but woops, I came too fast.': (
        'they get the punchline of his story about Bee, his own joke.', 'it gives the story of the psychic experiences just named.', 'One time, Bee said'),
}
for k, src in SRC.items():
    prev = json.loads((HERE / src / ('R-%s.json' % k)).read_text(encoding='utf-8'))
    have = {s['s']: s for s in prev['sentences']}
    out = HERE / 't3' / ('R-%s.json' % k)
    subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / 't3' / (k + '.txt')),
                    '--section', prev['section'], '--reader', prev['reader'], '--out', str(out)], check=True, capture_output=True)
    R = json.loads(out.read_text(encoding='utf-8'))
    for s in R['sentences']:
        if s['s'] in FILL:
            s['payoff'], s['follows'], s['link'] = FILL[s['s']]
        else:
            for f in ('payoff', 'follows', 'link'):
                s[f] = have[s['s']][f]
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
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(HERE / 't3' / (k + '.txt')), str(out)],
                       capture_output=True, text=True)
    print(k[4:30], (r.stdout + r.stderr).strip().replace('\n', ' | ')[:400])
