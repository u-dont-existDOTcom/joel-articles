#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's narrowing tests of Why Bad Trips Tend to Happen (the Human section, Psychological First Aid to the reminder, then a
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
    'After the Storm': {'payoff': 'they know this part is about the days after a hard trip', 'follows': AFTER,
                        'link': "none: a new section's heading; it opens the aftermath"},
}
NEW = {
    "Don't rush to turn a hard experience into content.": ('they know not to rush to make content of it', "the section's point, after the heading", "none: the section's first sentence, its point, after the heading"),
    "Sleep, eat simple food, drink water, go for a walk, journal, and pray or meditate gently.": ('they know the plain things to do instead', 'what to do instead', 'none: what to do instead of rushing, after the point'),
    "Talk with one grounded person, rather than twenty chaotic people.": ('they know who to talk with: one grounded person', 'who to talk with', 'grounded person'),
    "Don't make huge decisions, diagnose yourself from one intense night, or assume every vision was literal and every fear was false.": ('they know what not to decide or assume', 'what not to do', 'huge decisions'),
    "Let the system settle.": ('they know to let things settle', 'the sum of it', 'settle'),
    'No "another ceremony will fix this" reflex.': ('they know the rule: no rushing back to another ceremony', "the part's label, after the heading", "none: the part's label, after the heading"),
    'Don\'t take more psychedelics, cannabis, ketamine, intense breathwork, fast, push kundalini, deprive yourself of sleep, meditate or stretch to extremes, or schedule "another ceremony to fix it" while destabilized.': ('they know what not to take or do while destabilized', 'the rule spelled out', 'another ceremony'),
    "Get steady again with sleep and food and routine, sober people around you, and your ordinary body in the ordinary world.": ('they know how to get steady instead', 'what to do instead', 'steady'),
    "Deep practice can wait until the floor is back.": ('they know deep practice can wait', 'when deep practice comes back', 'Deep practice'),
    "Then ask what actually happened: what was medical or environmental, what was emotional, what was old trauma or fantasy, what was useful, what changed behavior, and what needs therapy, an apology, rest, or plain practical action.": ('they know the questions to ask about what happened', "the paragraph's point, after the heading", "none: the paragraph's first sentence, its point, after the heading"),
}
Q = {
    'Q1': "PASS: each paragraph opens on its point: the first priority, the room fixes with their reason, what the reminder is for, then the new section's point under its heading",
    'Q2': "PASS: every act in the Human section is the helper's own, with its purpose; the new part says what something means or what practice does, in the reader's terms",
    'Q3': 'PASS: which things exactly: keys, stove, roads, balconies, pools, weapons, the phone; the lights, the extra people; place, date and time, the substance; the named views and acts',
    'Q4': 'PASS: no terms a reader would not know; spiritual terms are the guide\'s own, each said in plain words around it',
    'Q5': "PASS: each turn has what it turns on: since a trip makes them lose track; what it is not, then what it is; bypassing, then practice",
    'Q6': "PASS: dangers, room, what to say, then the next section's point",
    'Q7': 'PASS: every fact is about the person in front of them, or how to see what is happening to them',
    'Q8': "PASS: the new part is one point, under its heading",
    'Q9': "PASS: nothing compressed: the reminder's facts one a sentence, as said aloud; the new part's relations said ('just means', 'that's exactly why')",
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
    r['placement'] = ("Psychological First Aid to the reminder, then %s's heading and one part with one sentence changed "
                      "(a narrowing test)" % head)
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next for %s; its overlaps are in "
                       "humanize/h25-20261107/RESULTS.md" % {'After the Storm': 'not rushing, minimum integration, the kinds of aftermath, no another ceremony, the questions and the fruit of insight'}[head])
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
