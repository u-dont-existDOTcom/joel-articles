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
HEAD = {'payoff': 'they know this part is for when the trip feels amazing and certain',
        'follows': "the next section's heading, after the reminder of where they are (a narrowing test)",
        'link': "none: a new section's heading; it opens the case of euphoric certainty"}
NEW = {
    "The action lock matters especially when the state feels blissful: I am God.": ('they know the lock matters most when it feels blissful, and what that sounds like', "the section's point, under its heading", 'The action lock'),
    "I am chosen.": ('another thing it sounds like', 'the next example', 'none: the next example of what bliss says, after the first'),
    "Everybody must hear this tonight.": ('another thing it sounds like', 'the next example', 'none: the next example of what bliss says, after the second'),
    "I finally understand everything.": ('the last example', 'the last example', 'none: the last example of what bliss says, after the third'),
    "Bliss is not proof of safety, and it often makes grounding less welcome.": ('they know bliss proves nothing about safety', 'after the examples, what they mean', 'Bliss'),
    "Feeling that good proves nothing about being safe, and it usually makes grounding the last thing you want.": ('they know bliss proves nothing about safety and makes grounding unwelcome', 'after the examples, what they mean', 'Feeling that good'),
    "The revelation will still exist after breakfast.": ('they know the revelation can wait', "the paragraph's point", 'none: the paragraph\'s first sentence, its point, after the questions'),
    "If it is true, it survives sleep.": ('they know a true revelation survives sleep', 'the reason it can wait', 'it'),
    "If it cannot survive one night of rest, it was an emergency impulse wearing angel wings.": ('they know what it was if it does not survive', 'the other case', 'one night of rest'),
    "The revelation will still exist after breakfast, and if it's true it'll survive a night's sleep.": ('they know the revelation can wait and a true one survives sleep', "the paragraph's point", 'none: the paragraph\'s first sentence, its point, after the questions'),
    "If it can't, it was an emergency impulse wearing angel wings.": ('they know what it was if it does not survive', 'the other case', "If it can't"),
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
                    'Psychological First Aid: The First Five Minutes, and When the Trip Feels Amazing', '--reader',
                    'someone sitting with a person on a bad psychedelic trip, or tripping themselves, who needs to know what to do in the first five minutes, and what to do when the trip feels amazing',
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text())
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] == 'When the Trip Feels Amazing: Euphoric Certainty':
            s.update(HEAD)
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        else:
            raise SystemExit('no entry for: %r' % s['s'])
    r['placement'] = ("Psychological First Aid to the reminder, then When the Trip Feels Amazing's heading and one paragraph with one "
                      "sentence changed (a narrowing test)")
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next for the lock in bliss, the danger list, the two "
                       "questions and the revelation after breakfast; its danger list's overlap with No Rash Actions is in humanize/h20-20261107/RESULTS.md")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
