#!/usr/bin/env python3
"""Receipts for the third tries of sections 42 and 67 (t5/<key>.txt), whose earlier tries read worse than the article's
text (42: AI High in its last window, eb7c696e; 67: Low windows, a3e48bae): each a small try from the r32 text, the
lineage's best (the ledger's near-miss rule). The fills are carried over by their words from the section's earlier
receipts (their fresh reads and my verdicts), and mine for the sentences this try changes or keeps as the article has
them where an earlier try had changed them."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = {'r36-42-from-flow-to-nitty-gritty': ['receipts'], 'r36-67-two-pillars-don-t-hold-the-roof-up-p1': ['small', 'receipts']}
FILL = {
    'All that works wonderfully until I’m in a romantic relationship and suddenly I’m expected to read her mind, even her silences, and check in constantly, without manipulating her with all that expert “management.”': (
        'they see what a relationship suddenly asks of someone used to living alone: reading her mind and her silences, checking in all the time, and doing it without manipulating her.',
        'it turns from the freedom of living alone to what a relationship asks.', 'All that works'),
    'If one person goes down, the other becomes the whole backup system for housing, money, children, health, and emotional crises.': (
        'they see what falls on one partner when the other goes down.', 'it says why it is a terrible time, the sentence before.',
        'If one person goes down'),
    'Who even has time for the relationship itself at that point?': (
        'they see that the backup work leaves no time for the relationship.', 'it asks what the load of the sentence before leaves time for.',
        'none: no words at its start tie it back; it asks what the load just named leaves time for'),
    'On the other hand, If both people are falling apart, there is only so much anyone else can do.': (
        'they don\'t expect friends to save a couple when both are falling apart.', 'it gives the limit of the outside support just named.',
        'On the other hand'),
    'Separate confidants help when you need privacy from your partner and somewhere else to say what you’re feeling.': (
        'they see what a separate confidant is good for: privacy from their partner and somewhere to say what they feel.',
        'it turns from friends who know both partners to confidants of one.', 'none: no words at its start tie it back; it opens a new step, confidants each partner has alone'),
    'If you do have separate confidants, you need enough emotional maturity to remember they will automatically be biased toward you, because they’re only hearing your side, usually while you’re upset, and they may just be trying to protect you.': (
        'they remember a separate confidant is biased toward them, and why: one side, heard while they\'re upset, from someone protecting them.',
        'it says what to do if they choose separate confidants, after the sentence before weighed both ways.', 'If you do have separate'),
}
for k, srcs in SRC.items():
    have = {}
    for src in reversed(srcs):
        prev = json.loads((HERE / src / ('R-%s.json' % k)).read_text(encoding='utf-8'))
        have.update({s['s']: s for s in prev['sentences']})
    prev = json.loads((HERE / srcs[0] / ('R-%s.json' % k)).read_text(encoding='utf-8'))
    out = HERE / 't5' / ('R-%s.json' % k)
    subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / 't5' / (k + '.txt')),
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
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(HERE / 't5' / (k + '.txt')), str(out)],
                       capture_output=True, text=True)
    print(k[4:30], (r.stdout + r.stderr).strip().replace('\n', ' | ')[:600])
