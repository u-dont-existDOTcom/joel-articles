#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's narrowing tests of Who to Contact, and When (the
Human section, Psychological First Aid to the reminder, then the section's heading and one part with one sentence
changed).

The Human section's sentences are filled from h13's receipt of the same base (TEST-base-L1.receipt.json); the
section's from NEW below.

  python3 make_receipts.py NAME...     make and check TEST-base-NAME.receipt.json for each NAME
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
BASE = json.loads((HERE.parent / 'h13-20261106/TEST-base-L1.receipt.json').read_text())
OLD = {s['s']: s for s in BASE['sentences']}
HEAD = {'payoff': 'they know this part is for when the person talks about harming someone',
        'follows': "a heading in the helper's section, after the reminder of where they are (a narrowing test)",
        'link': "none: a new subsection's heading; it opens the case of talk turning to harm"}
NEW = {
    'When somebody says, "I am God, so I can kill," leading with "No you\'re not" or "That\'s delusional" can turn the encounter into a status fight.': (
        'they know not to open by contradicting a grandiose threat', "the subsection's first point, under its heading", 'I am God'),
    "Nodding along as though harm is spiritually neutral is also unacceptable.": (
        'they know not to agree with it either', 'the other wrong way, after the first', 'also'),
    "But don't nod along either, as if hurting someone were spiritually neutral.": (
        'they know not to agree with it either', 'the other wrong way, after the first', 'either'),
    "Treat the statement as a safety signal and build a bridge back toward non-harm.": (
        'they know what to do instead: take it as a safety signal and lead back to non-harm', 'what to do, after the two wrong ways', 'the statement'),
    "Take it as a warning sign, and steer them back toward not hurting anyone.": (
        'they know what to do instead: take it as a warning and steer back to not hurting anyone', 'what to do, after the two wrong ways', 'it'),
}
Q = {
    'Q1': 'PASS: each paragraph opens on its point: the first priority, the room fixes with their reason, what the reminder is for, then the anchor part\'s point',
    'Q2': "PASS: every act is the helper's own, with its purpose: the dangers removed, the lights dimmed and the extra people out because they're overwhelmed, the reminder because a trip can make them lose track; one calm person as the lead, a second as backup when it's more than one can hold",
    'Q3': 'PASS: which things exactly: keys, stove, roads, balconies, pools, weapons, the phone; the lights, the extra people; place, date and time, the substance; who leads and who backs up, and when',
    'Q4': 'PASS: no terms a reader would not know; "anchor" is the heading\'s word, said in the sentence as the calm person who leads',
    'Q5': 'PASS: each turn has what it turns on: since a trip makes them lose track; the opposite of alone is too many people; backup when one person cannot hold it',
    'Q6': 'PASS: dangers, room, what to say, then who should be with them',
    'Q7': 'PASS: every fact is about the person in front of them now',
    'Q8': 'PASS: the anchor part is one point, under its heading',
    'Q9': "PASS: nothing compressed: the reminder's facts one a sentence, as said aloud; the anchor part one step a sentence",
}
for name in sys.argv[1:]:
    text = HERE / ('TEST-base-%s.txt' % name)
    out = HERE / ('TEST-base-%s.receipt.json' % name)
    subprocess.run([sys.executable, str(SR), 'make', str(text), '--section',
                    'Psychological First Aid: The First Five Minutes, and When the Content Turns Toward Harm', '--reader',
                    'someone sitting with a person on a bad psychedelic trip, or tripping themselves, who needs to know what to do in the first five minutes, and what to do when talk turns to harm',
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text())
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] == 'When the Content Turns Toward Harm':
            s.update(HEAD)
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        else:
            raise SystemExit('no entry for: %r' % s['s'])
    r['placement'] = ("Psychological First Aid to the reminder, then When the Content Turns Toward Harm's heading and one paragraph with one "
                      "sentence changed (a narrowing test)")
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the subsection from its heading to the next for the two wrong ways, the safety signal, "
                       "the grounding lines and the escalation; the Don't list's partial repeats are in humanize/h18-20261107/RESULTS.md")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
