#!/usr/bin/env python3
"""build_tests.py - the test texts of 2026-11-07's fifth pass: his list fix (round 23, bad-trips-2026-11-07j; SKILL.md,
"Writing for Pangram", fix 5) carried properly to four long lists that read AI, after a fresh reader's sense read
(sense/SENSE-READ.md) and the linter. Each list is taken apart, not reworded around: a short list of plain verbs at most,
the rest in sentences built differently, each item something a reader can picture, slack where safety allows.

  DL   For the Person Helping, its Don't list (B284), as a paragraph
  QS   After the Storm, the questions paragraph (B429), with Minimum Viable Integration's facts to write down folded in
  DS   Why Bad Trips Tend to Happen, the distortions lead-in and list (B362, B363), as a paragraph
  GS   Give the Session a Beginning and an End, its opening, lead-in and list (B366 to B368), as a paragraph

Each test is the Human base (Psychological First Aid to the reminder), then the section's heading and its part.

  python3 build_tests.py [NAME...]      writes TEST-base-NAME.txt
  python3 build_tests.py --guide OUT    writes the guide with every replacement, for the fidelity check before testing
"""
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
spec = importlib.util.spec_from_file_location('h28', HERE.parent / 'h28-20261107/build_tests.py')
H28 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H28)
plain, BASE = H28.plain, H28.BASE
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text())
BY_ID = {b['id']: b for b in BLOCKS}

NEW = {
    'B284': ("Don't try to win an argument with visions. Maybe they're sure the being in the corner is real, or that they "
             "finally know what the universe is for, and a memory that just came back can feel just as certain. That argument "
             "can wait until tomorrow, or forever. But don't validate harmful conclusions either. Reflect the feeling (\"that "
             "sounds terrifying\"), then bring them back to tonight's plan: nobody gets hurt, and the night ends with sleep. "
             "Don't call them crazy, broken, weak, punished or failing the medicine. And don't force anything on them. Eye "
             "contact and touch are their call, and so is your music. Prayer or chanting waits until they ask, and your "
             "interpretation of what it all means can wait longer still. A confession or an insight has to come from them, "
             "if it comes at all."),
    'B429': ("Once you've slept, write down what happened while it's still fresh: what you took and roughly how much, where "
             "you were, who was around, and what made it better or worse. Then go through it piece by piece. Maybe the panic "
             "hit right when the cannabis did, or right when the room got crowded. Maybe part of it was grief you've been "
             "carrying for years, or an old trauma. And maybe the part that felt like prophecy at 3 a.m. was a fantasy. "
             "Notice what was useful, and what you've already started doing differently. Some of it might call for therapy "
             "or an apology, some just for a long rest. And some of it is as plain as finding a better sitter, or keeping a "
             "bottle of water within reach next time."),
    'B362': ("Cognitive Behavioral Therapy (CBT) has names for the ways a frightened mind twists what it sees, and in a hard "
             "trip they can feed the crisis and keep it going. Catastrophizing is the voice that says \"This will never "
             "end.\" Emotional reasoning goes \"It feels true, so it must be true.\" In mind reading you're sure everyone can "
             "see you're broken, and in fortune-telling you've already decided your life is ruined now. All-or-nothing "
             "thinking says you're either enlightened or doomed. Personalization makes the whole cosmic horror specifically "
             "your fault. Then there's spiritual bypassing: \"Because everything is love, I don't need boundaries, doctors, "
             "sleep, or consequences.\""),
    'B363': '',
    'B366': ("If you're planning a session, think through how it will start and end, and what happens in between, before you "
             "take anything. Rest and timing come first: don't begin already depleted, and ideally start earlier in the day, "
             "so there's time afterward for food, some normal company and sleep. Know what you're taking and roughly how "
             "much, and look up what it mixes badly with and any medical concerns. Set up the room, and decide ahead of time "
             "what would make you call for outside help. Go in curious about what might come up, without a wish list of "
             "revelations, buried memories, good cries or spiritual breakthroughs. During it, the sitter (the sober person "
             "with you) keeps you safe and offers you choices. As it winds down, give it some closure. Stop adding "
             "stimulation, and check where you are and what day it is. Eat and drink when it's safe, then jot down the basic "
             "facts and let your body know the session is over. Keep the rest of the day free, and the next morning too if "
             "possible, "
             "because sleep and food come before turning any of it into a new life plan."),
    'B367': '',
    'B368': '',
}

# the second batch (bad-trips-2026-11-07j, after the first four read AI): what carried his version, measured on his own
# paragraph, and my Don't list with the kind of specifics his has
HIS_DT = ("Until you have slept and eaten, maybe don't drive, travel, break up, make up, quit your job, confess everything, "
          "confront or accuse that list of people you've been meaning to... Think twice before sending whatever ridiculous "
          "message you're planning on to Judge Amos, posting that revelation you'll forget tomorrow, giving away your BMW, buying "
          "a new BMW. After you decide that you are permanently enlightened or permanently damaged, and you explained the whole "
          "universe to your parents in 42 seconds, you can still change your mind the next day.")
ABLATE = {
    # AB1: his paragraph with its three absurd specifics made generic, everything else his
    'AB1': HIS_DT.replace("message you're planning on to Judge Amos", "message you're planning on sending")
                 .replace("giving away your BMW, buying a new BMW", "giving away your stuff, buying expensive stuff")
                 .replace("the whole universe to your parents in 42 seconds", "the whole universe to your parents"),
    # AB3: his specifics kept, his structure undone: one flat don't sentence, no hedge, no slack ending
    'AB3': ("Until you have slept and eaten, don't drive, travel, break up, make up, quit your job, confess everything, confront "
            "or accuse anybody, send the ridiculous message to Judge Amos, post the revelation, give away your BMW, buy a new BMW, "
            "explain the universe to your parents in 42 seconds, or decide that you are permanently enlightened or permanently "
            "damaged."),
}
DLJ = ("Don't try to win an argument with visions. You won't talk them out of it tonight, and you don't have to, whether "
       "they've decided the shadow in the corner is their great-aunt Doris, back from the dead to complain about the funeral, "
       "or that they cracked what the universe is for about ten minutes ago. A memory that suddenly came back can feel just as certain, so "
       "leave that alone too. Just don't validate harmful conclusions. Reflect the feeling (\"that sounds terrifying\") and steer "
       "back to the only plan for tonight, which is that nobody gets hurt and everybody sleeps eventually. Please don't call them "
       "crazy, broken, weak, punished or failing the medicine, even if they said it first. And whatever you think would really "
       "help (eye contact, touch, your music, a prayer, some chanting, your interpretation of what it all means, a confession, "
       "the big insight they're surely about to have), don't force it. If they want any of it, they'll "
       "ask.")


# the third batch: his frame as the ablations measured it (AB1 Human without his jokes, AB3 AI with them in the old form):
# a condition, a hedged don't and a short list ending on something from the reader's own life, with a trailing "...";
# "Think twice before ..."; and a slack ending. No reasons, examples or asides added. Safety-critical don'ts stay firm.
THIRD = {
    'AFF': ("While you're still shaky, maybe don't take more psychedelics, cannabis, ketamine, or do intense breathwork, fast, "
            "push kundalini, skip sleep, meditate or stretch to extremes... Think twice before you schedule \"another ceremony "
            "to fix it\" with whoever's hosting this weekend. Sleep and eat something, then spend a few days doing your "
            "normal stuff around people who are sober, and the deep practice will keep until you're back on your feet."),
    'DLF': ("Until they've come down a bit, maybe don't try to win an argument with the visions, the entities, the memories, "
            "or whatever cosmic conclusions they reached ten minutes ago... But don't validate anything harmful either, "
            "like a plan that ends with somebody getting hurt. Say something like \"that sounds terrifying,\" and nudge them "
            "back toward the room and the idea of sleep. Don't call them crazy, broken, weak, punished or failing the "
            "medicine, and don't force eye contact, touch, music, prayer, chanting, your interpretation, a confession or an "
            "insight on them. After they've slept, you can talk about all of it, or none of it."),
    'SHF': ("During a trip, maybe don't believe every shadow thought, suppress it, confess it to everybody, or turn it into "
            "that permanent diagnosis you've half been expecting... Just notice it: **\"A thought is here. A feeling is here. "
            "It is intense, but it is not the whole of me.\"** Then look around the room, feel your feet on the floor, find "
            "whoever's with you and check what time it is, and come back to whatever love you can find right now."),
}


# the fourth batch: a writer of another family (Codex, on his laptop), given tell_panel.py rewrite-prompt with his three
# Human, High paragraphs as his voice (brief-*/REWRITE-PROMPT.txt); only the standard swap applied (no em dash, straight quotes), and in CXSH "diagnose yourself for life" said as "a permanent diagnosis", a fidelity key
CODEX = {
 "CXAF": "Don't book \"another ceremony to fix it\" while you're unsettled, or take more psychedelics or cannabis. Leave ketamine alone too. Deep practice can wait until you're steady; don't fast, push kundalini, do intense breathwork, skip sleep, or meditate or stretch to extremes. Sleep and eat first. Keep your routine, with sober people around you, and settle into your body and everyday life.",
 "CXDL": "If they look away, don't force eye contact, or touch, music, prayer, chanting, interpretation, confession or insight. Don't try to win an argument with visions, entities, memories or cosmic conclusions, and don't validate harmful conclusions either. Reflect what they're feeling and steer back toward safety, no harm, sleep and the room you're sitting in. Don't tell them they're crazy, broken, weak or punished. And don't tell them they're \"failing the medicine.\"",
 "CXSH": "Don't give yourself a permanent diagnosis over a shadow thought during a trip. Notice it: **\"A thought is here. A feeling is here. It is intense, but it is not the whole of me.\"** Don't suppress it either, or identify with every shadow thought. And don't confess it to everybody. Then come back to the room and your body, to love and a person. Check the time."
}

TESTS = {
    'DL': (['B279', 'B283', 'B284'], ('B284',)),
    'QS': (['B419', 'B429', 'B430'], ('B429',)),
    'DS': (['B356', 'B362', 'B363'], ('B362', 'B363')),
    'GS': (['B364', 'B366', 'B367', 'B368', 'B370'], ('B366', 'B367', 'B368')),
    'AB1': (['B315', 'B317', 'B318'], ('B318',)),
    'AB3': (['B315', 'B317', 'B318'], ('B318',)),
    'DLJ': (['B279', 'B283', 'B284'], ('B284',)),
    'AFF': (['B419', 'B427', 'B428'], ('B428',)),
    'DLF': (['B279', 'B283', 'B284'], ('B284',)),
    'SHF': (['B410', 'B415'], ('B415',)),
    'CXAF': (['B419', 'B427', 'B428'], ('B428',)),
    'CXDL': (['B279', 'B283', 'B284'], ('B284',)),
    'CXSH': (['B410', 'B415'], ('B415',)),
}
SECOND = {'AB1': ABLATE['AB1'], 'AB3': ABLATE['AB3'], 'DLJ': DLJ, **THIRD, **CODEX}


def text(name):
    order, mine = TESTS[name]
    parts = [plain((SECOND[name] if name in SECOND else NEW[k]) if k in mine else BY_ID[k]['md']) for k in order]
    return BASE + '\n\n' + '\n\n'.join(p for p in parts if p.strip())


def guide(names):
    """The guide's Markdown with the named tests' replacements (an empty replacement drops the block)."""
    ids = {k for n in names for k in TESTS[n][1]}
    out = []
    for b in BLOCKS:
        md = NEW[b['id']] if b['id'] in ids else b['md']
        if md:
            out.append(md)
    return '\n\n'.join(out) + '\n'


if __name__ == '__main__':
    args = sys.argv[1:]
    if args[:1] == ['--guide']:
        pathlib.Path(args[1]).write_text(guide(args[2:] or list(TESTS)))
        sys.exit(0)
    for name in (args or TESTS):
        (HERE / ('TEST-base-%s.txt' % name)).write_text(text(name) + '\n')
        print(name, len(text(name).split()), 'words')
