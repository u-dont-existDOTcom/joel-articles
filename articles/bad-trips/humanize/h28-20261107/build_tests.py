#!/usr/bin/env python3
"""build_tests.py - the test texts of 2026-11-07's second pass: Joel's fix of the not-broken paragraph (round 22,
TEACH-NOT-BROKEN, answered 13:51 to 14:02 UTC with two Pangram links), and his moves carried to the seven stretches the
card named.

His two versions, read from his Pangram history:
  14fa25d1 (AI 99.99%): "... It's not that you're damaged for good, nor that you're being punished for being spiritually
           impure. More likely factors include ..."
  68752b7e (Human, High and Medium): "... I might feel in the moment like  you're damaged for good, no that you're being
           punished for being spiritually impure. But more likely factors include ..."
Only that sentence and "But" differ, so the "it's not that X" denial is what read AI. His moves, carried here:
  1. the denial said as how it feels ("it might feel like X"), then "but more likely Y";
  2. what happens said first, in plain words, then named ("and we call it a bad trip");
  3. a list said as causes, one at a time, with verbs ("could have been triggered", "may have gone in with");
  4. the verdict said as advice with its reason ("because blaming anyone only makes it heavier").

Each test is the Human base (Psychological First Aid to the reminder), then the section's heading and its part, laid out
as the earlier test of the same stretch was.

  python3 build_tests.py      writes TEST-base-NAME.txt for each test
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BASE = (HERE.parent / 'h14-20261106/BASE-human-PFA.txt').read_text().rstrip('\n')
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text())
BY_ID = {b['id']: b for b in BLOCKS}

HIS_SENT = ("When too much hits you at once, your nervous system can become flooded, nothing makes sense, and we call it a "
            "bad trip. I might feel in the moment like  you're damaged for good, no that you're being punished for being "
            "spiritually impure. But more likely factors include the dose of what drug(s) you took and how your body handles "
            "them. Old painful memories could have been triggered, or you may have gone in with a fearful mindset, or the "
            "setting or people around you could have fed into it. Be kind about it, to yourself or to whoever's going through "
            "it, because blaming anyone only makes it heavier.")
HIS_FIXED = HIS_SENT.replace("I might feel in the moment like  you're damaged for good, no that",
                             "It might feel in the moment like you're damaged for good, or that")
assert HIS_FIXED != HIS_SENT

NEW = {
    'B335': ('When someone is shaking in the corner, it can feel wise to reach for an ultimate view, like "we are all One," '
             '"I don\'t exist," "this is all karma" or "everything is Love," while the person goes on shaking, and we call '
             'that bypassing.'),
    'B336': ('Practice says love is here too, but then it makes the room safer, calls for help if it\'s needed, and holds the '
             'experience without becoming it, because pretending helps nobody.'),
    'B372': ('When terror comes up, the mind tries to answer it, maybe with metaphysics or a diagnosis, a conspiracy or some '
             'spiritual certainty, or by doing something desperate, and we call that fear trying to solve fear. It\'s a common '
             'loop, and it usually feeds the terror.'),
    'B398': 'Hatred and fear, shame, pride and rage all give these things something to hook into, and love takes the hooks out.',
    'B401': ('It might look passive, but this is how you become unhookable. A demon can fight your hatred, feed on your fear, '
             'argue with your pride or seduce your grandiosity, but there\'s nothing in love for it to grab.'),
    'B280': ('As a sitter you might feel the pull to win a philosophy debate, play out a rescue fantasy, impose your own '
             'interpretation, or show how spiritually advanced you are. But the job is simpler, and Zendo-style harm '
             'reduction sums it up as creating a safe space, sitting rather than guiding, talking through rather than down, '
             'and remembering that difficult doesn\'t automatically mean bad.'),
    'B391': ('Self-touch is different from somebody else touching you. It might feel compassionate to grab someone, hug them, '
             'restrain them, stroke them or crowd in close, but ask first: **"Would touch help, or would you rather have '
             'space?"** Good support may be silent presence from six feet away.'),
    'B324': ('The action lock matters especially when the state feels blissful: *I am God. I am chosen. Everybody must hear '
             'this tonight. I finally understand everything.* That bliss can feel like proof that you\'re safe, but more likely '
             'it\'s just making grounding less welcome.'),
    'B430': ('It can feel like the more cosmic the story sounds, the bigger the insight. But the fruit of an insight is whether '
             'suffering goes down and love gets more available.'),
    # the second batch: the guide's other plain denials, where the denial is the tell
    'B316': ('An intense altered state can make everything feel final, cosmic, and urgent, and it might feel like you have to '
             'act right now. But more likely the urgency is just part of the state, and acting on it isn\'t safe.'),
    'B320': ('Treat trip content first as **experience-content**, rather than fact-content. Because you saw it, it might feel '
             'like you have to act on it, and because it felt cosmic, obeying it might seem wise. But more likely you had an '
             'experience, and it can wait for you to be sober.'),
    'B361': ('Every hard experience can feel like a profound lesson. But sometimes the lesson is just to lower the dose or stop '
             'the practice, get some sleep and something to eat, pick safer people, and admit that the room is bad.'),
    'B382': ('The mistake people often make in love states is simply enjoying the love – or sending heart emojis to everybody. '
             'That can feel like the whole point, and it\'s nice.'),
    'B383': 'But the deepest utility is sending love to the places where love is missing.',
}

TESTS = {   # name: (blocks in order, replacements)
    'A0': (['B329', 'B331'], {'B331': HIS_SENT}),
    'A1': (['B329', 'B331'], {'B331': HIS_FIXED}),
    'SP': (['B332', 'B334', 'B335', 'B336', 'B337'], {k: NEW[k] for k in ('B335', 'B336')}),
    'FL': (['B371', 'B372'], {'B372': NEW['B372']}),
    'HK': (['B394', 'B397', 'B398', 'B399'], {'B398': NEW['B398']}),
    'UH': (['B394', 'B401'], {'B401': NEW['B401']}),
    'HP': (['B279', 'B280'], {'B280': NEW['B280']}),
    'TC': (['B385', 'B390', 'B391', 'B392'], {'B391': NEW['B391']}),
    'BL': (['B323', 'B324', 'B326', 'B327', 'B328'], {'B324': NEW['B324']}),
    'FR': (['B419', 'B430'], {'B430': NEW['B430']}),
    'N1': (['B315', 'B316'], {'B316': NEW['B316']}),
    'N4': (['B315', 'B320'], {'B320': NEW['B320']}),
    'W3': (['B356', 'B361'], {'B361': NEW['B361']}),
    'S3': (['B376', 'B382', 'B383', 'B384'], {k: NEW[k] for k in ('B382', 'B383')}),
}


def plain(md):
    """A block's Markdown as the page shows its text: no heading marks, emphasis or link targets."""
    t = re.sub(r'^#{1,6}\s+', '', md)
    t = re.sub(r'(?m)^- ', '', t)   # a bullet list shows its items without the marks
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = t.replace('**', '')
    t = re.sub(r'(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])', r'\1', t)
    return t


def text(name):
    order, repl = TESTS[name]
    return BASE + '\n\n' + '\n\n'.join(plain(repl.get(k, BY_ID[k]['md'])) for k in order)


if __name__ == '__main__':
    import sys
    for name in (sys.argv[1:] or TESTS):
        (HERE / ('TEST-base-%s.txt' % name)).write_text(text(name) + '\n')
        print(name, len(text(name).split()), 'words')
