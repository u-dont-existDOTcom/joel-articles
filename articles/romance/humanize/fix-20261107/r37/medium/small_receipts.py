#!/usr/bin/env python3
"""Receipts for the smaller tries (small/<key>.txt) of the three sections whose full fix the ledger's near-miss rule
refused (a try of at most 20% after a try with a Human window): each made from its text, the fills carried over by their
words from the full try's receipt (its fresh reads and my verdicts), and my fill for the sentences the full try had
changed and this one keeps as the article has them, or changes by a word or two."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FILL = {
    'Their meditations may have helped them a lot, but I still had no idea how either woman would act when a relationship got ugly.': (
        'they don\'t take someone\'s meditation as proof of how they\'ll act when a relationship gets ugly.',
        'it says what the meditation he saw couldn\'t tell him.', 'Their meditations may have'),
    'If somebody starts with enough trauma, huge progress can still leave a lot unresolved.': (
        'they expect a lot to be left unresolved in someone who started with a lot of trauma.',
        'it gives the reason the meditation couldn\'t tell him.', 'none: no words at its start tie it back; it gives the reason the sentence before couldn\'t be known'),
    'On my side, the blind spot is that I have trouble understanding where people are at mentally and emotionally.': (
        'they know his blind spot, which the next lines show with fawning.',
        'it turns from the women\'s side to his own.', 'On my side'),
    'A partner may agree with everything I say and then tell me later, “Didn’t you understand I was FAWNING?”': (
        'they see what fawning looks like from outside: agreeing with everything.',
        'it shows the blind spot of the sentence before.', 'none: no words at its start tie it back; it shows the blind spot just named'),
    'No, I really didn’t.': (
        'they hear that he really couldn\'t tell.', 'it answers the partner\'s question.', 'none: no words at its start tie it back; it answers the question just asked'),
    'If you’re fawning, tell me when you can, because I can’t know what’s happening in your head just from how obvious it feels to you.': (
        'they tell a partner when they\'re fawning, instead of expecting it to be seen.',
        'it says what to do about the blind spot of the sentences before.', 'none: no words at its start tie it back; it says what to do about the blind spot just shown'),
    'I don’t think equality means dividing every role 50/50.': (
        'they don\'t take a lead he takes as against equality.', 'it answers what taking initiative means for equality.',
        'none: no words at its start tie it back; it answers what the initiative of the paragraph before means for equality'),
    'If I like driving and for her it’s cooking, great.': (
        'they split roles by what each likes.', 'it gives an example of roles not split 50/50.', 'If I like driving'),
    'If she’s way better at something, she’ll probably do more of it.': (
        'they let the one who is better at something do more of it.', 'it gives the second way roles get split.',
        'If she’s way better'),
    'If one person goes down, the other becomes the whole backup system for housing, money, children, health, and emotional crises, so who even has time for the relationship itself at that point?': (
        'they see what falls on one partner when the other goes down, and what it leaves no time for.',
        'it says why it is a terrible time, the sentence before.', 'If one person goes down'),
    'Maybe an unusually strong couple can get away without much outside support, but I think that’s rare.': (
        'they don\'t count on being the rare couple that needs no one else.', 'it turns to whether a couple can do without outside support.',
        'none: no words at its start tie it back; it turns to the couples who might manage alone'),
    'Often, a friend who actually knows us both sees the dysfunctional pattern before either of us does.': (
        'they look for friends who know them both, who see the pattern first.', 'it says what outside support gives.',
        'none: no words at its start tie it back; it says what the outside support of the sentence before gives'),
    'They’re only hearing your side, usually while you’re upset, and they may just be trying to protect you, so take what they say with a grain of salt.': (
        'they take a separate confidant\'s advice with a grain of salt.', 'it says how the bias of the sentence before shows.',
        'none: no words at its start tie it back; it says how the bias just named shows'),
}
for k in ('r36-28-my-flaws-p2', 'r36-56-muses-directors-p3', 'r36-67-two-pillars-don-t-hold-the-roof-up-p1'):
    full = json.loads((HERE / 'receipts' / ('R-%s.json' % k)).read_text(encoding='utf-8'))
    have = {s['s']: s for s in full['sentences']}
    out = HERE / 'small' / ('R-%s.json' % k)
    subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / 'small' / (k + '.txt')),
                    '--section', full['section'], '--reader', full['reader'], '--out', str(out)], check=True, capture_output=True)
    R = json.loads(out.read_text(encoding='utf-8'))
    for s in R['sentences']:
        if s['s'] in FILL:
            s['payoff'], s['follows'], s['link'] = FILL[s['s']]
        else:
            for f in ('payoff', 'follows', 'link'):
                s[f] = have[s['s']][f]
    for f in ('placement', 'same_point', 'questions', 'needed', 'his_fixes', 'fit'):
        R[f] = full[f]
    R['opens']['why_reading'] = full['opens']['why_reading']
    keep = {s['s'] for s in R['sentences']}
    R['needed']['unneeded'] = [u for u in R['needed']['unneeded'] if u in keep]
    R['needed']['kept'] = {u: v for u, v in R['needed']['kept'].items() if u in keep}
    for read in ('his_fixes', 'fit'):
        R[read]['marked'] = [m for m in R[read]['marked'] if m['s'] in keep]
        R[read]['kept'] = {u: v for u, v in R[read]['kept'].items() if u in keep}
    out.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(HERE / 'small' / (k + '.txt')),
                        str(out)], capture_output=True, text=True)
    print(k[4:30], (r.stdout + r.stderr).strip().replace('\n', ' | ')[:400])
