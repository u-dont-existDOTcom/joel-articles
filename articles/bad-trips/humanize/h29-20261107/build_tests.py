#!/usr/bin/env python3
"""build_tests.py - the test texts of 2026-11-07's third pass: Joel's round-22 export of 15:38 UTC (both teaching cards
answered; ../../review/r22/ANSWERS-R22-20261107-1538.json, his words also in ../../experiments/t24-answers/), and then
his moves carried to the instruction stretches still reading AI.

  NB  his final not-broken paragraph (history 96a465a6, Human High alone), with "I might feel" to "It might feel", "no
      that" to "or that", a double space, and "Be kind about to yourself" to "Be kind to yourself" fixed
  AS  his After the Storm paragraph, the version he prefers ("altho i like the version where i'm betting better, sounds
      more human"; history ff7e9099, Human High alone), with a double space fixed

Each test is the Human base (Psychological First Aid to the reminder), then the section's heading and its part.

  python3 build_tests.py [NAME...]      writes TEST-base-NAME.txt
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

HIS_NB = ("When too much hits you at once, your nervous system can become flooded, nothing makes sense, and we call it a bad "
          "trip. It might feel in the moment like you're damaged for good, or that you're being punished for being spiritually "
          "impure. But more likely factors include the dose of what drug(s) you took and how your body handles them. Old "
          "painful memories could have been triggered, or you may have gone in with a fearful mindset, or the setting or people "
          "around you could have fed into it. Be kind to yourself or to whoever's going through it, because blaming anyone only "
          "makes it heavier.")
HIS_AS = ("Don't make huge decisions or diagnose yourself from an intense night. You don't need to assume every vision was "
          "literal, nor that anything you realized is actually true (or false). Ask your body what it needs from you now. I'm "
          "betting it will tell you: Give me sleep, natural food, pure water, a nice nature walk. It helps to integrate the "
          "experience via journaling your feelings, and talking with someone grounded (not the 20 chaotic people who are still "
          "coming down). To prevent your mind from giving spirituality a negative connotation, engage in some sober prayer or "
          "gentle meditation.")
# His After the Storm moves, carried to the instruction stretches still reading AI, after a fresh reader read each for sense
# (unclear words, claims that don't hold up, repeats, missing reasons): give the reader agency in the middle of the
# commands ("Ask your body what it needs from you now"); say why, not just what ("It helps to integrate the experience via
# ..."); leave a claim a little unbalanced ("true (or false)"); "a" or "an" for "one"; and his denial move where one stands.
NEW = {
    'B428': ('While you\'re still shaky, more can look like the answer: more psychedelics, cannabis or ketamine, intense '
             'breathwork, fasting, pushing kundalini energy, skipping sleep, meditating or stretching to extremes, or booking '
             '"another ceremony to fix it." Would you tell a friend this rattled to do any of that? I\'d guess '
             'you\'d tell them to sleep, eat, keep to their routine, stay near sober people, and let their body and the ordinary '
             'world steady them first, and save deep practice for when they\'re back on their feet.'),
    'B415': ('During a trip, a shadow thought can feel like the truth about you, and the urge is to fight it, confess it to '
             'everybody, or turn it into a permanent diagnosis. Just notice it: **"A thought is here. A feeling '
             'is here. It is intense, but it is not the whole of me."** Then come back to the room, your body, a person, the '
             'time, and love.'),
    'B318': ('What really can\'t wait until you\'ve slept and eaten? Usually nothing, so don\'t '
             'drive, travel, break up, quit your job, confess everything, confront anybody, accuse anybody, send the message, '
             'post the revelation, give away possessions, make a grand purchase, call your ex, call your parents to explain the '
             'universe, or decide that you are permanently enlightened or permanently damaged.'),
    'B408': ('Write down what you see or remember, whether it\'s abuse, betrayal, murder, past lives, hidden crimes, or cosmic '
             'plots, and get yourself somewhere safe, though it may feel like it has to be dealt with tonight. '
             'Don\'t confront anybody while you\'re intoxicated or shaky; it rarely goes the way you hope. After you\'ve slept, go '
             'back to what you wrote with a therapist who works with trauma, an integration specialist (someone who helps '
             'people make sense of a trip afterward), or a grounded person you trust.'),
    'B274': ('If your body still needs to move, ask it what would calm it down rather than wind it up. Usually that\'s something '
             'small and boring: brushing your teeth, stretching gently, a calm shower, or a few slow wall push-ups. Then let '
             'yourself sleep, or at least lie down and rest.'),
    'B250': ('If lying down starts to feel like a prison, get up and pace slowly somewhere contained. If the pacing starts '
             'turning into an escape (you keep drifting toward the door), sit against a wall or lie down under a blanket. Either '
             'way, you\'re letting your nervous system burn off the charge while staying clear of any new danger.'),
    'B372': ('When terror comes up, the mind starts hunting for an answer, in metaphysics, a diagnosis, a conspiracy, some '
             'spiritual certainty, or a desperate plan. Notice whether the answer is calming you down or winding you up. '
             'If it\'s winding you up, you\'re in a common loop, fear trying to solve fear, and that usually feeds the terror '
             '(maybe not every time, but often enough to stop and notice).'),
    'B280': ('As a sitter, think about what the person in front of you needs right now. I doubt it\'s a philosophy '
             'debate, someone acting out a rescue fantasy, your interpretation of what\'s happening, or a show of how spiritually '
             'advanced you are. Zendo-style harm reduction sums up what helps as creating a safe space, sitting with them rather '
             'than guiding them, talking them through rather than down, and remembering that a difficult experience can still be '
             'a good one.'),
    'B423': ('1. **First 24 hours:** sleep, food, water, warmth, the people you normally see, and no big moves.\n'
             '2. **Next few days:** write down the facts while you still remember them – substance, dose when known, setting, '
             'events, triggers, what helped, and what made things worse.\n'
             '3. **Then:** think about what the experience may have meant emotionally, spiritually, relationally, or '
             'practically (it may mean less than it felt like, or more).\n'
             '4. **Last:** make small changes in how you live that reduce suffering and increase love.'),
    'B391': ('Touching yourself, like a hand on your own heart, is one thing, and somebody else touching you is another. As the '
             'helper, it might feel compassionate to grab the person, hug them, restrain them, stroke them or crowd in close, but '
             'they may feel it as a threat. So ask first: **"Would touch help, or would you rather have space?"** Sometimes the '
             'best support is sitting quietly six feet away.'),
    'B392': ('If they say stop, freeze, pull away, or just seem unsure, stop, because any of those can mean no. And keep any '
             'touch nonsexual, consensual, and about their needs, never yours.'),
}
# The quoted-voice try (his device exactly: the list said in the body's own words, "Give me sleep, natural food, pure
# water, a nice nature walk", which alone took his paragraph from AI to Human High: 51b0103f against ff7e9099)
NEW2 = {
    'B274': ('If your body still needs to move, keep it small and ask it what it wants. It\'ll probably say something like: Let '
             'me brush my teeth, stretch a bit, stand under a warm shower, or do a few slow push-ups against the wall. Then let '
             'yourself sleep, or at least lie down and rest.'),
    'B428': ('While you\'re still shaky, more can look like the answer: more psychedelics, cannabis or ketamine, intense '
             'breathwork, fasting, pushing kundalini energy, skipping sleep, meditating or stretching to extremes, or booking '
             '"another ceremony to fix it." Picture a friend this rattled asking whether to do any of that. You\'d probably say: '
             'Go to bed, eat something, keep your routine, stay around sober people, and save the deep stuff for when you\'re '
             'back on your feet.'),
}
TESTS = {
    'AL2': (['B271', 'B272', 'B273', 'B274'], {'B274': NEW2['B274']}),
    'AF2': (['B419', 'B427', 'B428'], {'B428': NEW2['B428']}),
    'NB': (['B329', 'B331'], {'B331': HIS_NB}),
    'AS': (['B419', 'B420'], {'B420': HIS_AS}),
    'AF': (['B419', 'B427', 'B428'], {'B428': NEW['B428']}),
    'SH': (['B410', 'B415'], {'B415': NEW['B415']}),
    'NR': (['B315', 'B317', 'B318'], {'B318': NEW['B318']}),
    'AB': (['B405', 'B407', 'B408'], {'B408': NEW['B408']}),
    'AL': (['B271', 'B272', 'B273', 'B274'], {'B274': NEW['B274']}),
    'ST': (['B248', 'B250'], {'B250': NEW['B250']}),
    'FL2': (['B371', 'B372'], {'B372': NEW['B372']}),
    'HP2': (['B279', 'B280'], {'B280': NEW['B280']}),
    'MV': (['B419', 'B422', 'B423'], {'B423': NEW['B423']}),
    'TC2': (['B385', 'B390', 'B391', 'B392'], {'B391': NEW['B391'], 'B392': NEW['B392']}),
}


def text(name):
    order, repl = TESTS[name]
    return BASE + '\n\n' + '\n\n'.join(plain(repl.get(k, BY_ID[k]['md'])) for k in order)


if __name__ == '__main__':
    for name in (sys.argv[1:] or TESTS):
        (HERE / ('TEST-base-%s.txt' % name)).write_text(text(name) + '\n')
        print(name, len(text(name).split()), 'words')
