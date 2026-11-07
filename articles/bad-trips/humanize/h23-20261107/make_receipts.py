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
    'Hand on Heart and Gratitude 🫶🏿': {'payoff': 'they know this part is about a hand on the heart, gratitude and touch', 'follows': AFTER,
                                       'link': "none: a new section's heading; it opens the hand on the heart"},
    'Demons, Jinn, Entities, and Shadow Forces': {'payoff': 'they know this part is about demons and entities and how to meet them', 'follows': AFTER,
                                                  'link': "none: a new section's heading; it opens demons and entities"},
    'The Fear/Panic Loop': {'payoff': 'they know this part is about the fear loop and how to break it', 'follows': AFTER,
                            'link': "none: a new section's heading; it opens the fear/panic loop"},
    'Dealing With Sorrow: Missing Versus Sending Love': {'payoff': 'they know this part is about sorrow: missing someone against sending love', 'follows': AFTER,
                                                          'link': "none: a new section's heading; it opens sorrow, missing against sending love"},
}
NEW = {
    "A common loop is fear trying to solve fear.": ('they know the loop: fear trying to solve fear', "the section's point, after the heading",
         "none: the section's first sentence, its point, after the heading"),
    "Terror appears, and the mind answers it with metaphysics, diagnosis, conspiracy, spiritual certainty, or desperate action, which usually just feeds the terror.":
        ('they know how the loop runs and that the answers feed the terror', 'how the loop runs', 'Terror'),
    "Missing someone is a contraction.": ('they know missing someone contracts you', "the paragraph's point, after the heading",
         "none: the paragraph's first sentence, its point, after the heading"),
    "There's hunger and ache in it, it keeps circling back to you, and there's the painful fantasy that loving them means needing them to come back.":
        ('they know what the contraction is made of', 'what the contraction is', 'it'),
    "Sending love is different.": ('they know sending love is the other way', 'the contrast', 'Sending love'),
    "Sending love is pleasure in itself, even when the person is gone.": ('they know sending love feels good even with the person gone', 'how it differs', 'Sending love'),
    "Love can bless without grabbing.": ('they know love can give without holding on', 'what that means', 'Love'),
    "The difference is enormous.": ('they know the difference matters a lot', 'how much it matters', 'The difference'),
    "The mistake people often make in love states is simply enjoying the love – or sending heart emojis to everybody.": ('they know the common mistake in love states', "the paragraph's opening, after the heading",
         "none: the paragraph's first sentence, after the heading"),
    "That is nice, but it is not the deepest utility.": ('they know it is fine but not the best use', 'what is wrong with it', 'That'),
    "The deepest utility is sending love to the places where love is missing.": ('they know the best use: love where love is missing', 'the best use, after the mistake', 'The deepest utility'),
    "Send it to the person you miss without demanding they come back, and to the part of you that's still waiting for them, to the inner child who believed somebody else had to rescue him, and to the ashamed, angry, lonely, terrified and exiled parts.":
        ('they know where to send it: the person, the waiting part, the inner child, the exiled parts', 'where love is missing, named', 'it'),
    "Love is a better move, although it is difficult advice.": ('they know love is the better move, and hard', "the paragraph's point, after the heading", "none: the paragraph's first sentence, its point, after the heading"),
    "Almost nobody can authentically love what terrifies them while they are terrified.": ('they know why it is hard in the moment', 'why it is difficult', 'terrifies'),
    "So train before you need it, sending love to a frightening image, to someone you hate (without approving of what they did), to your shame and your body, to sickness and aging and fear and death, and to the inner child.":
        ('they know to practice beforehand, and on what', 'what to do about it', 'So'),
    "Practice being the space rather than the storm.": ('they know the aim of the practice', 'what the training is for', 'Practice'),
    "None of this is passive, though; it's about becoming unhookable.": ('they know love here is not passive: it makes them unhookable', "the paragraph's point, after the heading", "none: the paragraph's first sentence, its point, after the heading"),
    "A demon can fight hatred, feed on fear, argue with pride, and seduce grandiosity.": ('they know what a demon can grab onto', 'what unhookable means', 'A demon'),
    "Love gives it nothing to grab.": ('they know love leaves it nothing', 'the contrast', 'Love'),
    "Hatred, fear, shame, pride, and rage make hooks.": ('they know what makes hooks', "the paragraph's point, after the heading", "none: the paragraph's first sentence, its point, after the heading"),
    "Love removes hooks.": ('they know love removes them', 'the answer to the hooks', 'Love'),
    "The common mistake is fighting the terrifying thing with the very energy it feeds on, so panic fights panic and hatred fights hatred and pride fights pride, and before long a small war is running inside consciousness.":
        ('they know the common mistake and what it leads to', 'the mistake, after the hooks', 'none: the next paragraph names the mistake the hooks lead to'),
    "A hand on the heart can change the direction of a trip, especially when the problem is emotional contraction, grief, fear, or loneliness.": ('they know a hand on the heart can turn a trip, and when', "the section's point, after the heading", "none: the section's first sentence, its point, after the heading"),
    "There's no need to manufacture loving thoughts, you're just giving the body one simple signal: love is here.": ('they know it is a signal to the body, not forced thoughts', 'what the hand is for', 'loving thoughts'),
    "When somebody is medically, physically, or psychologically too overwhelmed to reach love, stabilize first.": ('they know to stabilize first when love is out of reach', "the paragraph's point, after the heading", "none: the paragraph's first sentence, its point, after the heading"),
    "Don't teach nondual demonology to somebody who needs the lights down and a doctor.": ('they know not to teach theory to someone who needs care', 'what that rules out', 'nondual demonology'),
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
                       "humanize/h23-20261107/RESULTS.md" % {'Hand on Heart and Gratitude 🫶🏿': 'the hand on the heart, gratitude and touch', 'Demons, Jinn, Entities, and Shadow Forces': 'his encounters, hooks, training, unhookable, the safety rule and stabilizing first', 'The Fear/Panic Loop': 'the loop and its breaker', 'Dealing With Sorrow: Missing Versus Sending Love': 'missing against sending love, the mistake and where to send it'}[head])
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
