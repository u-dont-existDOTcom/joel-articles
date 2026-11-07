#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's tests (h31): his list fix (round 23) carried to four
long lists (build_tests.py says which). Each is the Human section, Psychological First Aid to the reminder, then a
section's heading and its part.

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
HEADS = ['For the Person Helping: Calm Anchor, Not Guru', 'After the Storm', 'Why Bad Trips Tend to Happen',
         'Give the Session a Beginning and an End', 'No Rash Actions: Visions Are Not Commands', 'Dealing With Shadow Thoughts']
AFTER = "the next section's heading, after the reminder of where they are"
FIRST = "none: the section's first sentence, its point, after its heading"
NEW = {
    # AB1 and AB3: his No Rash Actions paragraph ablated (what carried it)
    "Think twice before sending whatever ridiculous message you're planning on sending, posting that revelation you'll forget tomorrow, giving away your stuff, buying expensive stuff.":
        ("they know the next things to hold off on: the message, the post, giving away and buying", "the second sentence of his list", "Think twice before"),
    "After you decide that you are permanently enlightened or permanently damaged, and you explained the whole universe to your parents, you can still change your mind the next day.":
        ("they know a big conclusion can be undone the next day", "the slack at the end of his list", "you can still change your mind"),
    "Until you have slept and eaten, don't drive, travel, break up, make up, quit your job, confess everything, confront or accuse anybody, send the ridiculous message to Judge Amos, post the revelation, give away your BMW, buy a new BMW, explain the universe to your parents in 42 seconds, or decide that you are permanently enlightened or permanently damaged.":
        ("they know everything to hold off on until slept and fed", "the lock's list", "Until you have slept and eaten"),
    # DLJ: the Don't list with the kind of specifics his list has
    "You won't talk them out of it tonight, and you don't have to, whether they've decided the shadow in the corner is their great-aunt Doris, back from the dead to complain about the funeral, or that they cracked what the universe is for about ten minutes ago.":
        ("they know why not to argue, and can picture what the visions might be", "the reason for the first don't", "talk them out of it"),
    "A memory that suddenly came back can feel just as certain, so leave that alone too.":
        ("they know a returned memory gets the same treatment", "more of what not to argue with", "just as certain"),
    "Just don't validate harmful conclusions.":
        ("they know the limit: agreeing with harm is out", "the other side of not arguing", "Just"),
    'Reflect the feeling ("that sounds terrifying") and steer back to the only plan for tonight, which is that nobody gets hurt and everybody sleeps eventually.':
        ("they know what to say instead, with an example, and where to steer: no harm, then sleep", "what to do between arguing and agreeing", "Reflect the feeling"),
    "Please don't call them crazy, broken, weak, punished or failing the medicine, even if they said it first.":
        ("they know which labels to keep out of the room, even ones the tripper used", "the next don't", "none: the next don't on the list"),
    "And whatever you think would really help (eye contact, touch, your music, a prayer, some chanting, your interpretation of what it all means, a confession, the big insight they're surely about to have), don't force it.":
        ("they know the last don't, and can picture what forcing might be", "the last don't", "And"),
    "If they want any of it, they'll ask.":
        ("they know what to do instead of forcing: wait to be asked", "what follows from not forcing", "any of it"),
    # the third batch: his frame as measured, after the tell panels
    "While you're still shaky, maybe don't take more psychedelics, cannabis, ketamine, or do intense breathwork, fast, push kundalini, skip sleep, meditate or stretch to extremes...":
        ("they know what to hold off on while shaky", "the bold line's reflex, said as what not to do", "none: the paragraph's first sentence, after the bold line it explains"),
    "Think twice before you schedule \"another ceremony to fix it\" with whoever's hosting this weekend.":
        ("they know the ceremony is the thing to think twice about", "the reflex the bold line names", "Think twice"),
    "Sleep and eat something, then spend a few days doing your normal stuff around people who are sober, and the deep practice will keep until you're back on your feet.":
        ("they know what to do instead, and that practice can wait", "what to do instead of more", "then"),
    "Until they've come down a bit, maybe don't try to win an argument with the visions, the entities, the memories, or whatever cosmic conclusions they reached ten minutes ago...":
        ("they know the first don't: arguing with what the tripper sees and concludes", "the part's point, under its subheading", "none: the part's first sentence, its point, after its subheading"),
    "But don't validate anything harmful either, like a plan that ends with somebody getting hurt.":
        ("they know the limit, with an example: agreeing with harm is out", "the other side of not arguing", "But"),
    'Say something like "that sounds terrifying," and nudge them back toward the room and the idea of sleep.':
        ("they know what to say instead, and where to steer", "what to do between arguing and agreeing", "Say something like"),
    "Don't call them crazy, broken, weak, punished or failing the medicine, and don't force eye contact, touch, music, prayer, chanting, your interpretation, a confession or an insight on them.":
        ("they know which labels to keep out and what not to force", "the last don'ts", "none: the next don'ts on the list"),
    "After they've slept, you can talk about all of it, or none of it.":
        ("they know the talk can wait, or never happen", "the slack after the don'ts", "all of it"),
    "During a trip, maybe don't believe every shadow thought, suppress it, confess it to everybody, or turn it into that permanent diagnosis you've half been expecting...":
        ("they know what not to do with a shadow thought during a trip", "the section's part for during a trip, after its heading", "none: the section's part for during a trip, after its heading"),
    "Then look around the room, feel your feet on the floor, find whoever's with you and check what time it is, and come back to whatever love you can find right now.":
        ("they know where to go after noticing: the room, the body, the person, the time, love", "what comes after noticing", "Then"),
    # the fourth batch: Codex's rewrites (a writer of another family), the standard swap applied
    'Don\'t book "another ceremony to fix it" while you\'re unsettled, or take more psychedelics or cannabis.':
        ("they know the first things not to do while unsettled: the ceremony, more psychedelics or cannabis", "the bold line's reflex, said as what not to do", "none: the paragraph's first sentence, after the bold line it explains"),
    "Leave ketamine alone too.":
        ("they know ketamine is out too", "one more substance not to take", "too"),
    "Deep practice can wait until you're steady; don't fast, push kundalini, do intense breathwork, skip sleep, or meditate or stretch to extremes.":
        ("they know deep practice waits, and which practices are out for now", "the practices after the substances", "none: the practices, after the substances the sentences before named"),
    "Sleep and eat first.":
        ("they know what comes first instead", "what to do instead", "first"),
    "Keep your routine, with sober people around you, and settle into your body and everyday life.":
        ("they know the rest of what steadies them", "more of what to do instead", "none: more of what to do, after sleep and food"),
    "If they look away, don't force eye contact, or touch, music, prayer, chanting, interpretation, confession or insight.":
        ("they know not to force anything, starting with eye contact", "the part's first don't, under its subheading", "none: the part's first sentence, after its subheading"),
    "Don't try to win an argument with visions, entities, memories or cosmic conclusions, and don't validate harmful conclusions either.":
        ("they know not to argue with the visions, and not to agree with harm", "the next don'ts", "none: the next don'ts on the list"),
    "Reflect what they're feeling and steer back toward safety, no harm, sleep and the room you're sitting in.":
        ("they know what to do instead, and where to steer", "what to do between arguing and agreeing", "Reflect what they're feeling"),
    "Don't tell them they're crazy, broken, weak or punished.":
        ("they know which labels to keep out", "the next don't", "none: the next don't on the list"),
    'And don\'t tell them they\'re "failing the medicine."':
        ("they know the last label to keep out", "the last don't", "And"),
    "Don't give yourself a permanent diagnosis over a shadow thought during a trip.":
        ("they know the first thing not to do with a shadow thought during a trip", "the section's part for during a trip, after its heading", "none: the section's part for during a trip, after its heading"),
    "Don't suppress it either, or identify with every shadow thought.":
        ("they know two more things not to do with it", "more don'ts after noticing", "it"),
    "And don't confess it to everybody.":
        ("they know the last thing not to do with it", "the last don't", "And"),
    "Then come back to the room and your body, to love and a person.":
        ("they know where to go after noticing: the room, the body, love, a person", "what comes after noticing", "Then"),
    "Check the time.":
        ("they know to check the time too", "one more thing to come back to", "none: the last of the things to come back to, after the sentence before"),
    'Notice it: "A thought is here.':
        ("they know what to do instead: notice it, with the words to say", "what to do instead of the diagnosis", "it"),
    # the guide's own, after GS's paragraph (B370)
    "Use this sequence for planned sessions.":
        ("they know when to use this: planned sessions", "what the paragraph before is for", "this sequence"),
    "Once somebody is already in trouble, return to the triage app instead of trying to improve the ceremony plan.":
        ("they know what to do once someone is in trouble: the triage app", "when the plan no longer applies", "Once somebody"),
    # DL: For the Person Helping, its Don't list as a paragraph
    "Don't":
        ("they know this part lists what a helper shouldn't do", "the Do list's partner, under the section's heading",
         "none: a subheading names its part, after the section's opening and its Do list"),
    "Don't try to win an argument with visions.":
        ("they know the first don't: arguing with what the tripper sees", "the part's point, under its subheading",
         "none: the part's first sentence, its point, after its subheading"),
    "Maybe they're sure the being in the corner is real, or that they finally know what the universe is for, and a memory that just came back can feel just as certain.":
        ("they can picture what the visions are: a being, the universe's meaning, a returned memory", "what the visions might be",
         "Maybe they're sure"),
    "That argument can wait until tomorrow, or forever.":
        ("they know the argument isn't for tonight", "what to do with the argument instead", "That argument"),
    "But don't validate harmful conclusions either.":
        ("they know the limit: agreeing with harm is out too", "the other side of not arguing", "But"),
    'Reflect the feeling ("that sounds terrifying"), then bring them back to tonight\'s plan: nobody gets hurt, and the night ends with sleep.':
        ("they know what to say instead, with an example, and where to steer: no harm, then sleep", "what to do between arguing and agreeing",
         "Reflect the feeling"),
    "Don't call them crazy, broken, weak, punished or failing the medicine.":
        ("they know which labels to keep out of the room", "the next don't", "none: the next don't on the list"),
    "And don't force anything on them.":
        ("they know the last don't: forcing anything", "the last don't", "And"),
    "Eye contact and touch are their call, and so is your music.":
        ("they can picture what not to force: eye contact, touch, music", "what forcing might look like", "their call"),
    "Prayer or chanting waits until they ask, and your interpretation of what it all means can wait longer still.":
        ("they know prayer, chanting and their own interpretation wait for the tripper", "more of what not to force", "waits until they ask"),
    "A confession or an insight has to come from them, if it comes at all.":
        ("they know confession and insight come from the tripper or not at all", "the last of what not to force", "come from them"),
    # QS: After the Storm, the questions with the facts to write down
    "Once you've slept, write down what happened while it's still fresh: what you took and roughly how much, where you were, who was around, and what made it better or worse.":
        ("they know the first thing to do after sleep: write down the facts, and which facts", "what comes once they are steady",
         "none: the next step after stabilizing, the paragraph before"),
    "Then go through it piece by piece.":
        ("they know the next step: go through it", "what to do with what they wrote", "Then"),
    "Maybe the panic hit right when the cannabis did, or right when the room got crowded.":
        ("they can picture a medical cause and a setting cause", "an example of going through it", "Maybe the panic"),
    "Maybe part of it was grief you've been carrying for years, or an old trauma.":
        ("they can picture an emotional cause and old trauma", "more of what they might find", "Maybe part of it"),
    "And maybe the part that felt like prophecy at 3 a.m. was a fantasy.":
        ("they can tell a fantasy from a prophecy", "the last kind of thing they might find", "And maybe"),
    "Notice what was useful, and what you've already started doing differently.":
        ("they know to keep what helped and see what changed", "what else to look for", "Notice"),
    "Some of it might call for therapy or an apology, some just for a long rest.":
        ("they know what some of it might need: therapy, an apology, rest", "what follows from going through it", "Some of it"),
    "And some of it is as plain as finding a better sitter, or keeping a bottle of water within reach next time.":
        ("they can picture the plain practical fixes", "the last kind of follow-up", "some of it"),
    # DS: Why Bad Trips Tend to Happen, the distortions as a paragraph
    "Cognitive Behavioral Therapy (CBT) has names for the ways a frightened mind twists what it sees, and in a hard trip they can feed the crisis and keep it going.":
        ("they know what the distortions are and why they matter here: they feed the crisis", "another cause of a crisis, after the lesson line",
         "none: another way a crisis starts or lasts, after the causes before it"),
    'Catastrophizing is the voice that says "This will never end."':
        ("they know the first distortion by its words", "the first of the names", "Catastrophizing"),
    'Emotional reasoning goes "It feels true, so it must be true."':
        ("they know the second distortion by its words", "the next name", "Emotional reasoning"),
    "In mind reading you're sure everyone can see you're broken, and in fortune-telling you've already decided your life is ruined now.":
        ("they know two more distortions by what they feel like", "the next two names", "mind reading"),
    "All-or-nothing thinking says you're either enlightened or doomed.":
        ("they know the next distortion by its words", "the next name", "All-or-nothing thinking"),
    "Personalization makes the whole cosmic horror specifically your fault.":
        ("they know the next distortion by what it does", "the next name", "Personalization"),
    'Then there\'s spiritual bypassing: "Because everything is love, I don\'t need boundaries, doctors, sleep, or consequences."':
        ("they know the last distortion by its words", "the last name", "Then there's"),
    # GS: Give the Session a Beginning and an End, as a paragraph
    "If you're planning a session, think through how it will start and end, and what happens in between, before you take anything.":
        ("they know the section's point: plan the start, the middle and the end first", "the section's point, under its heading", FIRST),
    "Rest and timing come first: don't begin already depleted, and ideally start earlier in the day, so there's time afterward for food, some normal company and sleep.":
        ("they know the first part of the start: rest, and an early start, and why", "the first thing to plan", "Rest and timing come first"),
    "Know what you're taking and roughly how much, and look up what it mixes badly with and any medical concerns.":
        ("they know the safety homework: the substance, the dose, combinations, medical concerns", "the next thing to plan", "none: the next thing to plan before starting"),
    "Set up the room, and decide ahead of time what would make you call for outside help.":
        ("they know to prepare the room and the threshold for help", "more of the start", "ahead of time"),
    "Go in curious about what might come up, without a wish list of revelations, buried memories, good cries or spiritual breakthroughs.":
        ("they know the attitude to start with: curious, not demanding a result", "the last part of the start", "Go in curious"),
    "During it, the sitter (the sober person with you) keeps you safe and offers you choices.":
        ("they know what the sitter does in the middle", "the middle of the session", "During it"),
    "As it winds down, give it some closure.":
        ("they know the end needs closure", "the end of the session", "As it winds down"),
    "Stop adding stimulation, and check where you are and what day it is.":
        ("they know the first closure steps", "what closure means", "none: the first of the closure steps the sentence before named"),
    "Eat and drink when it's safe, then jot down the basic facts and let your body know the session is over.":
        ("they know the last closure steps", "more of closure", "then"),
    "Keep the rest of the day free, and the next morning too if possible, because sleep and food come before turning any of it into a new life plan.":
        ("they know the time after: keep it free, and why", "after the session", "the rest of the day"),
}
Q = {
    'Q1': "PASS: each new paragraph opens on its point: the first don't (no arguing with visions); write down the facts once slept; what CBT's distortions are and what they do; plan the start and the end before taking anything",
    'Q2': "PASS: every act is the reader's own or the helper's, with its purpose; the distortions are what the reader's own mind does",
    'Q3': "PASS: which things exactly: the being in the corner, a memory that came back, eye contact, touch, music, prayer, chanting; what you took and how much, the cannabis, the crowded room, grief, prophecy at 3 a.m., a better sitter, a bottle of water; each distortion's own words; the substance and dose, what it mixes badly with, the room, food, company and sleep",
    'Q4': "PASS: the fresh reader's unclear terms (sense/SENSE-READ.md) answered in their sentences: the sitter is the sober person with you, cognitive distortions are the ways a frightened mind twists what it sees, low-directivity support is keeping you safe and offering choices, and 'return to the room and date' is checking where you are and what day it is; 'failing the medicine' stays, as the label a ceremony might put on a tripper",
    'Q5': "PASS: each turn has what it turns on: 'But' for the limit on not arguing, 'then' for the steps, 'and maybe' for the last kind of thing found, 'because' for keeping the day free",
    'Q6': "PASS: in the reader's order: the don'ts, then what to say instead; write, then sort, then what follows; the distortions one by one; before, during, the end, after",
    'Q7': "PASS: every fact is about the person in front of them, or their own session",
    'Q8': "PASS: each new part is its section's one point, under its heading",
    'Q9': "PASS: nothing compressed: each list taken apart into sentences, an item or a pair each, with the small words that carry the relations ('but', 'then', 'and maybe', 'because')",
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
    r['placement'] = ("Psychological First Aid to the reminder, then %s's heading and its part, with his list fix carried "
                      "to it (round 23's lesson)" % head)
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next; its overlaps are in "
                       "humanize/h31-20261107/RESULTS.md")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
