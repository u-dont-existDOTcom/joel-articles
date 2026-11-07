#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's narrowing tests of (Re)defining "Bad Trip", Spiritual
≠ "Getting Your Ass Kicked" and The Other Bypass (the Human section, Psychological First Aid to the reminder, then a
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
    'Spiritual ≠ "Getting Your Ass Kicked"': {'payoff': 'they know this part is about suffering and spiritual practice',
                                              'follows': AFTER,
                                              'link': "none: a new section's heading; it opens why suffering alone is not spiritual"},
    'The Other Bypass: Feeling Good Forever': {'payoff': 'they know this part is about chasing good feelings and skipping shadow work',
                                               'follows': AFTER,
                                               'link': "none: a new section's heading; it opens the other bypass, feeling good forever"},
}
NEW = {
    "A bad trip does not prove that you are broken, punished, unspiritual, impure, or permanently damaged.":
        ('they know a bad trip proves nothing bad about them', "the section's point, under its heading",
         "none: the paragraph's first sentence, its point, after the heading"),
    "It just means more came at you than your nervous system, your body and the part of you that makes sense of things could handle, whether it came from the setting, your memories, the dose, or the people in your life.":
        ('they know what a bad trip is instead: more than they could handle, and where it came from',
         'after what it does not prove, what it does mean', 'It just means'),
    "The response is care rather than blame.": ('they know to answer it with care, not blame', 'what to do about it, after what it is',
                                                'The response'),
    "This is one side of the difference between spiritual bypassing and spiritual practice:":
        ('they know a contrast between bypassing and practice comes next', "the part's opening, under the heading",
         "none: the part's first sentence, after the heading"),
    'Bypassing reaches for an ultimate view – "we are all One," "I don\'t exist," "this is all karma," "everything is Love" – while ignoring the person shaking in the corner.':
        ('they know what bypassing looks like: a big view while the person suffers', 'the first side of the contrast', 'Bypassing'),
    "Practice says yes, love is here, and that's exactly why we make the room safer, call for help when it's needed, stop pretending, and hold the experience without becoming it.":
        ('they know what practice does instead: make the room safe, get help, stop pretending, hold it', 'the other side of the contrast',
         'love is here'),
    "That is tripsitting, shadow work, and the path becoming practical.": ('they know what that practice amounts to',
                                                                          'what the contrast adds up to', 'That'),
    "Having a bad trip doesn't mean you're broken, or that you're being punished, or that you're unspiritual or impure, or damaged for good.":
        ('they know a bad trip proves nothing bad about them', "the section's point, under its heading",
         "none: the paragraph's first sentence, its point, after the heading"),
    "It means the nervous system, meaning-making system, body, environment, memories, dose, or relationships became overwhelmed.":
        ('they know what a bad trip is instead: something got overwhelmed, and which things can', 'after what it does not mean, what it does mean',
         'It means'),
    'Bypassing grabs for some ultimate view, like "we are all One," "I don\'t exist," "this is all karma," or "everything is Love," and meanwhile the person in the corner is still shaking.':
        ('they know what bypassing looks like: a big view while the person suffers', 'the first side of the contrast', 'Bypassing'),
    "Practice says love is here, so we make the room safer, call for help when needed, stop pretending, and hold the experience without becoming it.":
        ('they know what practice does instead: make the room safe, get help, stop pretending, hold it', 'the other side of the contrast',
         'Practice'),
    'Shadow work to me is neither BDSM nor "feeding your demons."': ('they know what shadow work is not, for him', "the paragraph's opening, under the heading",
         "none: the paragraph's first sentence, after the heading"),
    "It means bringing loving awareness to the parts of the mind built in fear, pain, humiliation, rejection, and survival.":
        ('they know what shadow work is: loving awareness for the parts built in fear and pain', 'after what it is not, what it is', 'It means'),
    "Inner-child reparenting is central.": ('they know inner-child reparenting is the heart of it', 'the central practice of that work',
         'none: names the central practice of the shadow work just defined, inner-child reparenting'),
    "Most negative mind-states aren't some error in your philosophy, they're just young parts of you that are still waiting for love and protection and permission, and for the explanation nobody ever gave them.":
        ('they know what negative mind-states are: young parts waiting for love', 'why inner-child work is central', 'young parts'),
    'A well-rounded trip should offer practical lessons and contact with suffering as well as freedom from suffering, lest we become "so spiritually high that we are no earthly good."':
        ('they know a good trip should touch suffering too, not only freedom from it', "the section's point, under its heading",
         "none: the section's first sentence, its point, after the heading"),
    '"Life is full of suffering" is Buddha\'s First Noble Truth.': ('they know where that view of suffering comes from', 'the authority for the point', 'suffering'),
    'Ignoring that side of life becomes dissociation or spiritual bypassing in the opposite direction, followed eventually by statements like "Everything is Love, including violence."':
        ('they know what ignoring suffering turns into', 'what happens if the point is ignored', 'that side of life'),
    "Many people meditate or take psychedelics to feel good.": ('they know why many people do this', "the paragraph's opening, a turn to feeling good",
         "none: opens a new paragraph on feeling good, after the warning about ignoring suffering"),
    "I am definitely one of them, and Buddha also said meditation should generally feel good.": ('they know he is one of them, and Buddha agreed it should feel good', 'his own case', 'one of them'),
    "My friend Eshwar, however, found that shadow work made up about 99% of his path to heart-chakra awakening.":
        ('they know a friend found the path was almost all shadow work', 'the other side, in a real case', 'however'),
    "Modern people carry so much trauma – and some people did even in Buddha's time – that shadow work and inner-child reparenting may need to come first, even before authentic liberation from the identity illusion.":
        ('they know shadow work may need to come first, because of trauma', 'why that can be', 'shadow work'),
    "When shadow work is bypassed in meditation and therapy, it may appear in ordinary life without explaining itself.":
        ('they know skipped shadow work shows up in ordinary life', 'what happens if it is skipped', 'shadow work is bypassed'),
    "I encountered a lot of it in my first two marriages, to my bewilderment.": ('they know he met it in his marriages', 'his own case of it', 'it'),
    "I wish everybody could keep shadow work inside the safer rooms of meditation, therapy, journaling, prayer, and honest conversation.":
        ('they know where he wishes it would stay', 'his wish, after the cost', 'shadow work'),
    "Begin with my Inner Child Therapy guide and app, and my Self-Hypnosis guide and app.": ('they know where to begin', 'where to start the work just described',
         'Begin'),
    "Having a bad trip doesn't make you broken, and it doesn't mean you're being punished, or that you're unspiritual or impure, or damaged for good.":
        ('they know a bad trip proves nothing bad about them', "the section's point, under its heading",
         "none: the paragraph's first sentence, its point, after the heading"),
    "It just means too much hit you at once.": ('they know what a bad trip is instead: too much at once', 'after what it does not mean, what it does', 'It just means'),
    "Your nervous system and your body got flooded and your mind couldn't make sense of it all, and the setting, old memories, the dose or what's going on with the people around you could all have fed into that.":
        ('they know what got flooded and what can feed it', 'what too much at once looks like', 'that'),
    "So be kind about it, to yourself or to whoever's going through it, because blaming anyone only makes it heavier.":
        ('they know to meet it with kindness, not blame', 'what to do about it', 'So'),
    'When someone\'s shaking in the corner and the people around them reach for an ultimate view instead of reaching for them, like "we are all One" or "I don\'t exist," or "this is all karma," or "everything is Love," that\'s spiritual bypassing, or one side of it anyway.':
        ('they know what bypassing looks like: a big view instead of the person', "the part's opening, after the heading",
         "none: the part's first sentence, after the heading"),
    "Spiritual practice agrees the love is here, and that's exactly why you make the room safer and call for help if it's needed.":
        ('they know practice acts on the love: a safer room, help when needed', 'the other way, after bypassing', 'the love is here'),
    "You also quit pretending, and you stay with what's happening without getting lost in it.": ('they know practice also means no pretending and staying present',
         'the rest of what practice does', 'also'),
    "To me that's what tripsitting and shadow work come down to, and it's where the path stops being theory.":
        ('they know that is what tripsitting and shadow work are, for him', 'what it all adds up to', 'that'),
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
                       "humanize/h21-20261107/RESULTS.md" % {'(Re)defining "Bad Trip"': 'shadow work called a bad trip and what a bad trip is not',
                                                           'Spiritual ≠ "Getting Your Ass Kicked"': 'suffering by itself and bypassing against practice',
                                                           'The Other Bypass: Feeling Good Forever': 'feeling good, shadow work first and where to begin'}[head])
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
