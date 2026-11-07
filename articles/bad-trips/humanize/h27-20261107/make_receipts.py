#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's teaching tries (the not-broken paragraph and After the Storm's first paragraph) (the Human section, Psychological First Aid to the reminder, then a
section's heading and one part with one sentence changed).

The Human section's sentences are filled from h13's receipt of the same base (TEST-base-L1.receipt.json); the
sections' from HEADS and NEW below.

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
AFTER = "the next section's heading, after the reminder of where they are (a narrowing test)"
HEADS = {
    '(Re)defining "Bad Trip"': {'payoff': 'they know this part says what a bad trip is and is not', 'follows': AFTER,
                                'link': "none: a new section's heading; it opens what a bad trip means"},
    'After the Storm': {'payoff': 'they know this part is about the days after a hard trip', 'follows': AFTER,
                        'link': "none: a new section's heading; it opens the aftermath"},
}
NEW = {
    "A bad trip doesn't mean you're broken or being punished, or that you're unspiritual or impure or damaged for good, it just means too much came at once for your nervous system and your body and the way you make sense of things, whether from the setting, old memories, the dose or the people around you.":
        ('they know a bad trip is not proof that something is wrong with them, only that too much came at once, and from where', "the section's point, under its heading", "none: the section's first sentence, its point, after its heading"),
    "The response is care rather than blame.": ('they know what to do about it: care, not blame', 'what follows from the point', 'The response'),
    "Don't rush to turn a hard experience into content, your system just needs time to settle.": ('they know not to rush to make content of it, and why: the system needs time to settle', "the section's point, under its heading", "none: the section's first sentence, its point, after its heading"),
    "Sleep, eat something simple, drink some water and take a walk.": ('they know the plain things to do while it settles', 'what to do instead of rushing', 'none: the first things to do while it settles, after the reason'),
    "Journaling helps, and so does praying and meditating gently.": ('they know journaling and gentle prayer and meditation help', 'more of what helps', 'Journaling'),
    "Talk it over with one grounded person rather than twenty chaotic ones.": ('they know who to talk it over with', 'who to talk to', 'it'),
    "And for now, hold off on huge decisions, and don't diagnose yourself from one intense night or assume every vision was literal and every fear was false.": ('they know what to hold off on for now', 'what not to do yet', 'for now'),
}
Q = {
    'Q1': "PASS: each paragraph opens on its point: the first priority, the room fixes with their reason, what the reminder is for, then the new section's point under its heading",
    'Q2': "PASS: every act in the Human section is the helper's own, with its purpose; the new part says what something means or what practice does, in the reader's terms",
    'Q3': 'PASS: which things exactly: keys, stove, roads, balconies, pools, weapons, the phone; the lights, the extra people; place, date and time, the substance; the named views and acts',
    'Q4': 'PASS: no terms a reader would not know; spiritual terms are the guide\'s own, each said in plain words around it',
    'Q5': "PASS: each turn has what it turns on: since a trip makes them lose track; what a bad trip is not, then what it is; don't rush, because the system needs time",
    'Q6': "PASS: dangers, room, what to say, then the next section's point",
    'Q7': 'PASS: every fact is about the person in front of them, or how to see what is happening to them',
    'Q8': "PASS: the new part is one point, under its heading",
    'Q9': "PASS: nothing compressed: the reminder's facts one a sentence, as said aloud; the new part's relations said ('it just means', 'whether from', 'your system just needs time')",
}
for name in sys.argv[1:]:
    text = HERE / ('TEST-base-%s.txt' % name)
    out = HERE / ('TEST-base-%s.receipt.json' % name)
    head = next(h for h in HEADS if ('\n\n%s\n\n' % h) in text.read_text())
    subprocess.run([sys.executable, str(SR), 'make', str(text), '--section',
                    'Psychological First Aid: The First Five Minutes, and %s' % head, '--reader',
                    'someone sitting with a person on a bad psychedelic trip, or tripping themselves, who needs to know what to do in the first five minutes, and how to see what is happening',
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text())
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] in HEADS:
            s.update(HEADS[s['s']])
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        else:
            raise SystemExit('no entry for: %r' % s['s'])
    r['placement'] = ("Psychological First Aid to the reminder, then %s's heading and my best try at its first paragraph "
                      "(a teaching try)" % head)
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next for %s; its overlaps are in "
                       "humanize/h27-20261107/RESULTS.md" % {'(Re)defining "Bad Trip"': 'shadow work called a bad trip and what a bad trip means', 'After the Storm': 'not rushing, minimum integration, the kinds of aftermath, no another ceremony, the questions and the fruit of insight'}[head])
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
