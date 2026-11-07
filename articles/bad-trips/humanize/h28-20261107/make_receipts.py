#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's tests: his fix of the not-broken paragraph with two
typos fixed (A1), and his moves carried to seven stretches (build_tests.py says which). Each is the Human section,
Psychological First Aid to the reminder, then a section's heading and its part.

The Human section's sentences come from h13's receipt of the same base. The guide's unchanged sentences come from the
earlier receipts in this lane's folders, and the new sentences from NEW below.

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
EARLIER = {}
for f in sorted(HERE.parent.glob('h*/TEST-*.receipt.json')):
    if f.parent == HERE:
        continue
    try:
        for s in json.loads(f.read_text())['sentences']:
            if all(s.get(k) for k in ('payoff', 'follows', 'link')):
                EARLIER[s['s']] = s
    except (ValueError, KeyError):
        continue
HEADS = ['(Re)defining "Bad Trip"', 'Spiritual ≠ "Getting Your Ass Kicked"', 'The Fear/Panic Loop',
         'Demons, Jinn, Entities, and Shadow Forces', 'For the Person Helping: Calm Anchor, Not Guru',
         'Hand on Heart and Gratitude 🫶🏿', 'When the Trip Feels Amazing: Euphoric Certainty', 'After the Storm',
         'No Rash Actions: Visions Are Not Commands', 'Why Bad Trips Tend to Happen',
         'Dealing With Sorrow: Missing Versus Sending Love']
AFTER = "the next section's heading, after the reminder of where they are"
FIRST = "none: the section's first sentence, its point, after its heading"
NEW = {
    # A1: his version, two typos fixed
    "When too much hits you at once, your nervous system can become flooded, nothing makes sense, and we call it a bad trip.":
        ('they know what a bad trip is: too much at once, a flooded nervous system, nothing making sense', "the section's point, under its heading", FIRST),
    "It might feel in the moment like you're damaged for good, or that you're being punished for being spiritually impure.":
        ('they know the fears it brings are a feeling of the moment: damaged for good, punished for being impure', 'what it feels like from inside', 'It might feel'),
    "But more likely factors include the dose of what drug(s) you took and how your body handles them.":
        ('they know the likelier causes: the dose and how the body handles it', 'the likelier truth, against the feeling', 'But more likely'),
    "Old painful memories could have been triggered, or you may have gone in with a fearful mindset, or the setting or people around you could have fed into it.":
        ('they know the other likely causes: old memories, a fearful mindset, the setting and the people around', 'more of the likely causes', 'none: more of the likely factors the sentence before began'),
    "Be kind about it, to yourself or to whoever's going through it, because blaming anyone only makes it heavier.":
        ('they know what to do about it, and why: be kind, since blame makes it heavier', 'what follows from the causes', 'it'),
    # SP
    'When someone is shaking in the corner, it can feel wise to reach for an ultimate view, like "we are all One," "I don\'t exist," "this is all karma" or "everything is Love," while the person goes on shaking, and we call that bypassing.':
        ('they know what bypassing is: reaching for an ultimate view while the person shakes', 'the first side of the difference the sentence before names', 'none: the first side, after the colon'),
    "Practice says love is here too, but then it makes the room safer, calls for help if it's needed, and holds the experience without becoming it, because pretending helps nobody.":
        ('they know what practice does instead: the room safer, help called, the experience held, no pretending', 'the other side', 'Practice says love is here too'),
    # FL
    "When terror comes up, the mind tries to answer it, maybe with metaphysics or a diagnosis, a conspiracy or some spiritual certainty, or by doing something desperate, and we call that fear trying to solve fear.":
        ('they know the loop by its name: the mind answering terror with theories or desperate action', "the section's point, under its heading", FIRST),
    "It's a common loop, and it usually feeds the terror.":
        ('they know it is common and that it feeds the terror', 'what the loop does', "It's"),
    # HK
    "Hatred and fear, shame, pride and rage all give these things something to hook into, and love takes the hooks out.":
        ('they know what gives these things a hold, and what takes it away', 'what the response is, after saying it is mostly the same', 'these things'),
    "I don't have to settle whether these things are objectively real or internal formations because the response is mostly the same.":
        ('they know the response is the same whether these things are real or inner', "the section's point so far, under its heading", "none: the first sentence after the heading here; his stories before it are left out of this test"),
    "The common mistake is fighting the terrifying thing with the energy it already consumes.":
        ('they know the mistake: fighting it with what it already feeds on', 'what goes wrong instead of love', 'The common mistake'),
    "Panic fights panic, hatred fights hatred, pride fights pride, and suddenly a small war is running inside consciousness.":
        ('they know what that fight looks like inside', 'what the mistake looks like', 'none: the mistake shown, each feeling against itself'),
    # UH
    "It might look passive, but this is how you become unhookable.":
        ('they know that loving it is not giving in: it leaves nothing to hook', "the section's point, under its heading", 'It might look passive'),
    "A demon can fight your hatred, feed on your fear, argue with your pride or seduce your grandiosity, but there's nothing in love for it to grab.":
        ('they know how: each feeling gives it a hold, love gives none', 'why loving it works', 'none: what a demon can do with each feeling, against love'),
    # HP
    "As a sitter you might feel the pull to win a philosophy debate, play out a rescue fantasy, impose your own interpretation, or show how spiritually advanced you are.":
        ('they know the pulls a sitter feels and has to leave alone', "the section's point, under its heading", FIRST),
    "But the job is simpler, and Zendo-style harm reduction sums it up as creating a safe space, sitting rather than guiding, talking through rather than down, and remembering that difficult doesn't automatically mean bad.":
        ('they know the job instead: a safe space, sitting, talking through, difficult not meaning bad', 'the job, against those pulls', 'But the job'),
    # TC
    "It might feel compassionate to grab someone, hug them, restrain them, stroke them or crowd in close, but ask first: \"Would touch help, or would you rather have space?\"":
        ('they know to ask before touching, whatever feels compassionate', 'how touching someone else differs', 'none: touching someone else, after self-touch'),
    # BL
    "That bliss can feel like proof that you're safe, but more likely it's just making grounding less welcome.":
        ('they know bliss feels like safety but makes grounding harder', 'what the bliss does to the action lock', 'That bliss'),
    # FR
    "It can feel like the more cosmic the story sounds, the bigger the insight.":
        ('they know the feeling that a cosmic story means a big insight', "the section's point, under its heading", FIRST),
    "But the fruit of an insight is whether suffering goes down and love gets more available.":
        ('they know how to judge an insight: less suffering, more love', 'the likelier truth, against the feeling', 'But'),
    # the second batch
    "An intense altered state can make everything feel final, cosmic, and urgent, and it might feel like you have to act right now.":
        ('they know the state makes everything feel urgent, as if they must act now', "the section's point, under its heading", FIRST),
    "But more likely the urgency is just part of the state, and acting on it isn't safe.":
        ('they know the urgency is the state, and acting on it is not safe', 'the likelier truth, against the feeling', 'But more likely'),
    "Treat trip content first as experience-content, rather than fact-content.":
        ('they know how to hold what the trip showed: as experience, not fact', "the section's point, under its heading", FIRST),
    "Because you saw it, it might feel like you have to act on it, and because it felt cosmic, obeying it might seem wise.":
        ('they know the pulls: seeing it feels like a duty, its cosmic feel makes obeying seem wise', 'what makes trip content feel like fact', 'Because you saw it'),
    "But more likely you had an experience, and it can wait for you to be sober.":
        ('they know it was an experience, and it can wait until they are sober', 'the likelier truth, against the feeling', 'But more likely'),
    "Every hard experience can feel like a profound lesson.":
        ('they know a hard experience can feel like a deep lesson', "the section's point, under its heading", FIRST),
    "But sometimes the lesson is just to lower the dose or stop the practice, get some sleep and something to eat, pick safer people, and admit that the room is bad.":
        ('they know the lesson is often plain: the dose, the practice, sleep, food, safer people, a bad room', 'the likelier truth, against the feeling', 'But sometimes'),
    "That can feel like the whole point, and it's nice.":
        ('they know enjoying it feels like the point, and is nice', 'what that mistake feels like', 'That'),
    "Send love to the person you miss without demanding their return.":
        ('they know the first place to send love: the person they miss, asking nothing back', 'the places where love is missing, the first', 'none: the first item of the list the sentence before opens'),
    "Send love to the part of you still waiting for them.":
        ('they know the next place: the part of them still waiting', 'the next place', 'none: the next item of the list'),
    "Send love to the inner child who believed somebody else had to rescue him.":
        ('they know the next place: the inner child who waited to be rescued', 'the next place', 'none: the next item of the list'),
    "Send love to the ashamed, angry, lonely, terrified, and exiled parts.":
        ('they know the last place: the ashamed, angry, lonely, terrified and exiled parts', 'the last place', 'none: the last item of the list'),
    "But the deepest utility is sending love to the places where love is missing.":
        ('they know the deepest use: love sent where it is missing', 'the deeper use, against the mistake', 'But'),
}
Q = {
    'Q1': "PASS: each paragraph opens on its point: the first priority, the room fixes with their reason, what the reminder is for, then the new section's point under its heading",
    'Q2': "PASS: every act in the Human section is the helper's own, with its purpose; the new part says what is happening or what to do, in the reader's terms",
    'Q3': 'PASS: which things exactly: keys, stove, roads, balconies, pools, weapons, the phone; the lights, the extra people; place, date and time, the substance; the named feelings, views and acts',
    'Q4': "PASS: no terms a reader would not know; the guide's own terms are said in plain words around them",
    'Q5': "PASS: each turn has what it turns on: since a trip makes them lose track; it might feel like this, but more likely that",
    'Q6': "PASS: dangers, room, what to say, then the next section's point",
    'Q7': 'PASS: every fact is about the person in front of them, or how to see what is happening to them',
    'Q8': "PASS: the new part is its section's one point, under its heading",
    'Q9': "PASS: nothing compressed: the reminder's facts one a sentence, as said aloud; the new part's relations said ('might feel', 'but more likely', 'and we call that', 'because')",
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
    missing = []
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        elif s['s'] in EARLIER:
            for k in ('payoff', 'follows', 'link'):
                s[k] = EARLIER[s['s']][k]
        elif s['s'] == head:
            s['payoff'], s['follows'], s['link'] = ("they know what this part is about: %s" % head, AFTER,
                                                    "none: a new section's heading")
        else:
            missing.append(s['s'])
    if missing:
        raise SystemExit('%s: no entry for %r' % (name, missing))
    r['placement'] = ("Psychological First Aid to the reminder, then %s's heading and its part, with Joel's move carried "
                      "to it (round 22's lesson)" % head)
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next; its overlaps are in "
                       "humanize/h28-20261107/RESULTS.md")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
