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
    'Give the Session a Beginning and an End': {'payoff': 'they know this part is about planning a session from start to end', 'follows': AFTER,
                                                'link': "none: a new section's heading; it opens planning a session"},
    'Why Bad Trips Tend to Happen': {'payoff': 'they know this part says why bad trips happen', 'follows': AFTER,
                                     'link': "none: a new section's heading; it opens the causes of bad trips"},
}
NEW = {
    "Every hard experience is not a profound lesson.": ('they know not every hard trip is a lesson', "the paragraph's point, after the heading",
         "none: the paragraph's first sentence, its point, after the heading"),
    "Sometimes the lesson is just to lower the dose or stop the practice, get some sleep and something to eat, pick safer people, and admit that the room is bad.":
        ('they know the plain lessons: less dose or stop, sleep, food, safer people, a bad room admitted', 'what the lesson often is instead', 'the lesson'),
    "In CBT (Cognitive Behavioral Therapy) these are called cognitive distortions, and any of them can start the crisis or make it last longer:":
        ('they know a list of thinking traps follows, each able to start or prolong the crisis', "the part's opening, after the heading",
         "none: the part's first sentence, after the heading"),
    'Catastrophizing: "This will never end."': ('they know the first trap and how it sounds', 'the first item', 'none: the first item of the list the sentence before opens'),
    'Emotional reasoning: "It feels true, so it must be true."': ('they know the next trap and how it sounds', 'the next item', 'none: the next item of the same list, after the first'),
    'Mind reading: "Everyone can see I am broken."': ('they know the next trap and how it sounds', 'the next item', 'none: the next item of the same list, after the second'),
    'Fortune-telling: "My life is ruined now."': ('they know the next trap and how it sounds', 'the next item', 'none: the next item of the same list, after the third'),
    'All-or-nothing thinking: "Either I am enlightened or I am doomed."': ('they know the next trap and how it sounds', 'the next item', 'none: the next item of the same list, after the fourth'),
    'Personalization: "This cosmic horror is specifically my fault."': ('they know the next trap and how it sounds', 'the next item', 'none: the next item of the same list, after the fifth'),
    'Spiritual bypassing: "Because everything is love, I don\'t need boundaries, doctors, sleep, or consequences."': ('they know the last trap and how it sounds', 'the last item', 'none: the last item of the same list, after the sixth'),
    "A few of the thinking habits CBT (Cognitive Behavioral Therapy) calls cognitive distortions can set off the crisis, and once it's going they'll keep feeding it:":
        ('they know a list of thinking habits follows that can start the crisis and keep it going', "the part's opening, after the heading",
         "none: the part's first sentence, after the heading"),
    'All-or-nothing thinking, where it\'s either "I\'m enlightened" or "I\'m doomed" and nothing in between.': ('they know the next trap and how it sounds', 'the next item', 'none: the next item of the same list, after the fourth'),
    'Personalization, the sense that all this cosmic horror is somehow your fault.': ('they know the next trap and how it feels', 'the next item', 'none: the next item of the same list, after the fifth'),
    'And spiritual bypassing, the one that goes "everything is love, so I don\'t need boundaries, doctors, sleep, or consequences."': ('they know the last trap and how it sounds', 'the last item', 'And'),
    "For planned altered-state work, think through the beginning, middle, and end before starting.": ('they know to plan the whole session before it starts', "the section's point, after the heading",
         "none: the section's first sentence, its point, after the heading"),
    "When you have a choice:": ('they know a list of choices follows', 'the lead into the list', 'none: introduces the list of choices that follows, after the point'),
    "Rest and timing: don't begin already depleted.": ('they know not to start depleted', 'the first item', 'none: the first item of the list the line before opens'),
    "When possible, begin earlier in the day so there is still time for the experience, food, ordinary contact, and sleep afterward.": ('they know to start early so there is time after', 'the rest of the first item', 'begin earlier'),
    "Physical safety: know the substance and approximate dose, review combinations and medical concerns, prepare the room, and decide in advance what requires outside help.": ('they know the safety steps before starting', 'the next item', 'none: the next item of the same list, after rest and timing'),
    "Intention without a script: know what you are open to exploring without demanding a particular revelation, memory, emotional arc, or spiritual result.": ('they know to be open without demanding a result', 'the next item', 'none: the next item of the same list, after physical safety'),
    "Low-directivity support: the sitter protects safety and offers choices.": ('they know what the sitter does: safety and choices', 'the next item', 'none: the next item of the same list, after intention'),
    "Closure: stop adding stimulation, return to the room and date, eat and hydrate when safe, write down the basic facts, and let the body understand that the session has ended.": ('they know how to close the session', 'the next item', 'none: the next item of the same list, after the support item'),
    "Integration time: leave the rest of the day and, when possible, the next morning free.": ('they know to keep time free after', 'the last item', 'none: the last item of the same list, after closure'),
    "Sleep and food come before turning the experience into a new life plan.": ('they know sleep and food come before big plans', 'the rest of the last item', 'Sleep and food'),
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
                       "humanize/h22-20261107/RESULTS.md" % {'Why Bad Trips Tend to Happen': 'the blockage frame, the causes, not every lesson and the distortions', 'Give the Session a Beginning and an End': 'the plan, the list of choices and the pointer back to the triage app'}[head])
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
