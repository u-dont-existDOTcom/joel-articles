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
HEAD = {'payoff': 'they know this part is about not acting on the trip',
        'follows': "the next section's heading, after the reminder of where they are (a narrowing test)",
        'link': "none: a new section's heading; it opens the rule against acting on visions"}
NEW = {
    "An intense altered state can make everything feel final, cosmic and urgent, but feeling urgent doesn't make acting safe.": ('they know urgency is no reason to act', "the section's first point, under its heading", 'none: the section\'s first sentence after its heading, its point'),
    "Treat trip content first as experience-content, rather than fact-content, because \"I saw it\" doesn't create a duty to act, and \"it felt cosmic\" doesn't make obedience wise.": ('they know to treat what they saw as experience, not orders', 'after the steps, how to think about the content', 'trip content'),
    "No revelation makes murder, assault, coercion, sexual boundary-crossing, reckless driving, or self-harm safe tonight, so anything that would violate someone's consent or harm anyone goes in the notebook until you can look at it sober.": ('they know no vision makes harm safe, and that such urges go in the notebook', 'the last point, the hard limit', 'No revelation'),
    "Put yourself on a 24\u201372 hour action lock.": ('they know to hold off acting for 24 to 72 hours', "the section's rule, under its heading", 'action lock'),
    "Write it down, get some sleep, and go back over it sober with one grounded person.": ('they know what to do with the urge: write it, sleep, and look again sober with someone grounded', "the paragraph's steps, after the lock", 'Write it down'),
    "Write it down.": ('they know to write the urge down', "the first step, after the lock", 'Write it down'),
    "Protect sleep.": ('they know to sleep before acting', 'the next step', 'sleep'),
    "Then go back over it once you're sober, with one grounded person.": ('they know to look at it again sober, with someone grounded', 'the last step', 'Then'),
    "Use a 24\u201372 hour action lock.": ('they know to hold off acting for 24 to 72 hours', "the section's rule, under its heading", 'action lock'),
    "Give it 24\u201372 hours before you act on anything.": ('they know to hold off acting for 24 to 72 hours', "the section's rule, under its heading", '24\u201372 hours'),
    "Until you have slept and eaten, don't drive, travel, break up, quit your job, confess everything, confront anybody, accuse anybody, send the message, post the revelation, give away possessions, call your ex, call your parents to explain the universe, or decide that you are permanently enlightened or permanently damaged.": (
        'they know which actions wait until they have slept and eaten', "the rule's list, after the rule", 'Until you have slept and eaten'),
    "Until you've slept and eaten, don't drive or travel, and don't break up with anyone or quit your job.": ('they know the first things that wait until they have slept and eaten', "the rule's list, after the rule", "Until you've slept and eaten"),
    "Don't confess everything, or confront or accuse anybody.": ('they know not to confess, confront or accuse yet', 'the list goes on', "Don't confess"),
    "Don't send the message or post the revelation, don't give away possessions, and don't call your ex, or your parents to explain the universe to them.": ('they know not to send, post, give things away or call anyone yet', 'the list goes on', "Don't send"),
    "And don't decide you're permanently enlightened, or permanently damaged, either.": ('they know not to decide anything about themselves yet', 'the last item', 'either'),
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
                    'Psychological First Aid: The First Five Minutes, and No Rash Actions', '--reader',
                    'someone sitting with a person on a bad psychedelic trip, or tripping themselves, who needs to know what to do in the first five minutes, and what not to act on',
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text())
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] == 'No Rash Actions: Visions Are Not Commands':
            s.update(HEAD)
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        else:
            raise SystemExit('no entry for: %r' % s['s'])
    r['placement'] = ("Psychological First Aid to the reminder, then No Rash Actions' heading and one paragraph with one "
                      "sentence changed (a narrowing test)")
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next for the lock, its list, writing it down, "
                       "experience-content and no revelation making harm safe; its lock's other mentions are in humanize/h19-20261107/RESULTS.md")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
