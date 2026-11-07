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
    'Hand on Heart and Gratitude 🫶🏿': {'payoff': 'they know this part is about a hand on the heart, gratitude and touch', 'follows': AFTER, 'link': "none: a new section's heading; it opens the hand on the heart"},
    'The Fear/Panic Loop': {'payoff': 'they know this part is about the fear loop and how to break it', 'follows': AFTER, 'link': "none: a new section's heading; it opens the fear/panic loop"},
    'After the Storm': {'payoff': 'they know this part is about the days after a hard trip', 'follows': AFTER, 'link': "none: a new section's heading; it opens the aftermath"},
    'No Rash Actions: Visions Are Not Commands': {'payoff': 'they know this part is about not acting on what the trip shows', 'follows': AFTER,
                                                  'link': "none: a new section's heading; it opens not acting on visions"},
    'When the Trip Feels Amazing: Euphoric Certainty': {'payoff': 'they know this part is for when the trip feels amazing and certain', 'follows': AFTER,
                                                        'link': "none: a new section's heading; it opens the case of euphoric certainty"},
}
NEW = {
    "Use a 24–72 hour action lock.": ('they know the rule: a 24–72 hour lock on acting', "the section's rule, after the heading", "none: the section's rule, its first line, after the heading"),
    "Until you have slept and eaten, don't drive, travel, break up, quit your job, confess everything, confront anybody, accuse anybody, send the message, post the revelation, give away possessions, make a grand purchase, call your ex, call your parents to explain the universe, or decide that you are permanently enlightened or permanently damaged.":
        ('they know what not to do until they have slept and eaten', 'the lock spelled out', 'Until you have slept and eaten'),
    "The action lock matters especially when the state feels blissful: I am God.": ('they know the lock matters most when it feels blissful, and what that sounds like', "the section's point, under its heading", 'The action lock'),
    "I am chosen.": ('another thing it sounds like', 'the next example', 'none: the next example of what bliss says, after the first'),
    "Everybody must hear this tonight.": ('another thing it sounds like', 'the next example', 'none: the next example of what bliss says, after the second'),
    "I finally understand everything.": ('the last example', 'the last example', 'none: the last example of what bliss says, after the third'),
    "Bliss is not proof of safety, and it often makes grounding less welcome.": ('they know bliss proves nothing about safety', 'after the examples, what they mean', 'Bliss'),
    "Two questions while glowing:": ('they know two questions follow', 'the lead into the questions', 'none: introduces the two questions that follow, after the point'),
    "1. Have I slept?": ('they know the first question: have I slept', 'the first question', 'none: the first of the two questions the line before opens'),
    "Sleep comes before mission.": ('they know sleep comes first', 'the answer to the first question', 'Sleep'),
    "2. Has this happened before, and how did it end?": ('they know the second question', 'the second question', 'none: the second of the two questions, after the first'),
    "A recurring pattern with lost sleep, racing thoughts, pressured speech, or everyone saying you are not yourself needs grounded support before action.": ('they know what a recurring pattern needs', 'what the second question is for', 'A recurring pattern'),
    "The revelation will still exist after breakfast.": ('they know the revelation can wait', "the paragraph's point", "none: the paragraph's first sentence, its point, after the questions"),
    "If it is true, it survives sleep.": ('they know a true revelation survives sleep', 'the reason it can wait', 'it'),
    "If it cannot survive one night of rest, it was an emergency impulse wearing angel wings.": ('they know what it was if it does not survive', 'the other case', 'one night of rest'),
    "1.": ('they know the first question comes', 'the number of the first question', 'none: the number of the first of the two questions'),
    "Have I slept?": ('they know the first question: have I slept', 'the first question', 'none: the first of the two questions the line before opens'),
    "2.": ('they know the second question comes', 'the number of the second question', 'none: the number of the second of the two questions'),
    "Has this happened before, and how did it end?": ('they know the second question', 'the second question', 'none: the second of the two questions, after the first'),
    'Touch, Consent, and Compassion': ('they know a part on touch follows', "the part's heading, after the section's", 'none: a part heading; it opens touch and consent'),
    'Self-touch is different from somebody else touching you.': ('they know touching yourself differs from being touched', "the part's point, after its heading", "none: the part's first sentence, its point, after its heading"),
    "Compassion doesn't mean you get to grab someone, or hug them, hold them down, stroke them or crowd in on them.": ('they know what compassion does not allow', 'what not to do', 'Compassion'),
    'Ask first: "Would touch help, or would you rather have space?"': ('they know to ask first, and how', 'what to do instead', 'Ask first'),
    'Good support may be silent presence from six feet away.': ('they know support can be quiet and at a distance', 'another way to help', 'Good support'),
    'When the person says stop, freezes, pulls away, or seems unsure, stop.': ('they know when to stop', 'the stop rule', 'stop'),
    "Touch must remain nonsexual, consensual, and unrelated to the helper's needs.": ('they know what touch must stay', 'the limits of touch', 'Touch'),
    'Loop breaker:': ('they know the steps that break the loop follow', 'the lead into the steps', 'none: introduces the steps that break the loop, after the heading'),
    'Name it: "This is fear trying to solve fear."': ('they know the first step: name it', 'the first step', 'none: the first step of the list the line before opens'),
    "Stop debating: while you're peaking, it's no time for metaphysics, diagnosis or life decisions.": ('they know the second step: stop debating while peaking', 'the next step', 'Stop debating'),
    'Move down the ladder: room → body → human → time.': ('they know the third step: move down the ladder', 'the next step', 'none: the third step of the same list, after the second'),
    'Repeat: "This is a wave.': ('they know the fourth step: repeat this', 'the last step', 'none: the fourth step of the same list, after the third'),
    'I don\'t have to solve it while peaking."': ('they know the rest of what to repeat', 'the rest of the last step', 'it'),
    'Minimum Viable Integration': ('they know a part on the least integration follows', "the part's heading, after the section's", 'none: a part heading; it opens minimum integration'),
    'First 24 hours: sleep, food, water, warmth, ordinary contact, and no big moves.': ('they know what the first day needs', 'the first step', 'none: the first step of the part, after its heading'),
    'Next few days: write the facts – substance, dose when known, setting, events, triggers, what helped, and what made things worse.': ('they know what to write in the next days', 'the next step', 'none: the next step of the same list, after the first day'),
    'Then: think about what it might have meant for your feelings, your spiritual life and your relationships, or just in practical terms.': ('they know to think about what it meant', 'the next step', 'it'),
    'Last: make small behavioral changes that reduce suffering and increase love.': ('they know the last step: small changes', 'the last step', 'none: the last step of the same list, after the third'),
    'What Kind of Aftermath Is This?': ('they know a part on kinds of aftermath follows', "the part's heading, after the section's", 'none: a part heading; it opens the kinds of aftermath'),
    'When symptoms linger, name the pattern rather than collapsing everything into "I\'m broken," because different patterns need different support.': ('they know to name the pattern, and why', "the part's point, after its heading", "none: the part's first sentence, its point, after its heading"),
    'Anxiety and fear: grounding, routine, reduced stimulation, CBT-style reality testing, and therapy when it persists.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
    'Sleep disturbance and nightmares: sleep hygiene, no more substances, and professional help when severe or prolonged.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
    'Derealization and depersonalization: ordinary-world grounding, exercise, nature, outside attention, less rumination, peer or family support, and therapy when needed.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
    'Visual distortions or HPPD-like symptoms: reduce stress and substance use; seek professional support when symptoms interfere with life.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
    'Social disconnection and shame: one or two safe humans, peer support, and no social-media crowdsourcing while raw.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
    'Existential shock: write it down, slow down, and return to practical love before building a metaphysical system.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
    'Trauma material: trauma-informed therapy or integration support, without immediate confrontation while destabilized.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
    'Paranoia or psychosis-like beliefs: professional support quickly, especially when beliefs drive unsafe action.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
    'Somatic hyperarousal: gentle movement, breathing, grounding, and medical care for severe, unusual, or worrying symptoms.': ('they know one pattern and the support it needs', 'an item of the list of patterns', "none: an item of the list of patterns the part's point opens"),
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
                       "humanize/h26-20261107/RESULTS.md" % {'Hand on Heart and Gratitude 🫶🏿': 'the hand on the heart, gratitude and touch', 'The Fear/Panic Loop': 'the loop and its breaker', 'After the Storm': 'not rushing, minimum integration, the kinds of aftermath, no another ceremony, the questions and the fruit of insight', 'No Rash Actions: Visions Are Not Commands': 'the lock, its list, writing it down, experience-content and no revelation making harm safe', 'When the Trip Feels Amazing: Euphoric Certainty': 'the lock in bliss, the two questions and the revelation after breakfast'}[head])
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
