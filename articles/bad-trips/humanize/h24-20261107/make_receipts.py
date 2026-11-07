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
    'Abuse Memories, Recovered Memories, and Certainty': {'payoff': 'they know this part is about abuse memories and how sure to be of them', 'follows': AFTER,
                                                          'link': "none: a new section's heading; it opens abuse memories and certainty"},
    'Dealing With Shadow Thoughts': {'payoff': 'they know this part is about shadow thoughts', 'follows': AFTER,
                                     'link': "none: a new section's heading; it opens shadow thoughts"},
}
NEW = {
    "Psychedelics can bring up true trauma, symbolic material, distorted fragments, fears, fantasies, archetypes, past-life narratives, and mixtures of all of them.": ('they know what can come up, true and not', "the section's point, after the heading", "none: the section's first sentence, its point, after the heading"),
    "Don't dismiss what arises, but don't treat intoxicated certainty as evidence either.": ('they know to take it seriously without taking it as proof', 'what to do with it', 'what arises'),
    "Don't confront tonight": ('they know the rule: no confronting tonight', "the part's label, after the heading", "none: the part's label, after the heading"),
    "When you see or remember abuse, betrayal, murder, past lives, hidden crimes, or cosmic plots, write it down and get safe.": ('they know what to do when it comes up: write it down, get safe', 'the first step, under the label', 'write it down'),
    "Don't confront anybody while intoxicated or destabilized.": ('they know not to confront anyone in that state', 'the rule itself', 'confront'),
    "Come back to it once you've slept, with a trauma-informed therapist or an integration specialist, or just a grounded person you trust.": ('they know when and with whom to come back to it', 'what to do instead', 'Come back to it'),
    "The experience may matter deeply.": ('they know it may matter a lot', "the paragraph's point, after the heading", "none: the paragraph's first sentence, its point, after the heading"),
    "It could be true psychologically, or symbolically, or literally, or only partly true, or false in the form it first took.": ('they know the ways it may or may not be true', 'how it may matter', 'It'),
    "You don't have to decide tonight.": ('they know they need not decide tonight', 'what follows for tonight', 'tonight'),
    "During a trip, you don't need to identify with every shadow thought, or suppress it, or confess it to everybody, or turn it into a permanent diagnosis.": ('they know what not to do with a shadow thought', "the paragraph's point, after the heading", "none: the paragraph's first sentence, its point, after the heading"),
    'Notice: "A thought is here.': ('they know what to notice instead', 'what to do instead', 'Notice'),
    'A feeling is here.': ('they know the second thing to notice', 'the next line of the notice', 'none: the next line of the same notice, after the thought'),
    'It is intense, but it is not the whole of me."': ('they know it is intense but not all of them', 'the last line of the notice', 'It'),
    "Then return to room, body, human, time, and love.": ('they know where to come back to', 'what comes after noticing', 'Then'),
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
                       "humanize/h24-20261107/RESULTS.md" % {'Abuse Memories, Recovered Memories, and Certainty': 'what comes up, not confronting tonight and true in which way', 'Dealing With Shadow Thoughts': 'opposites, co-arising, unweaving, the Hermetic claim and noticing during a trip'}[head])
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
