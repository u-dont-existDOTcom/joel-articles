#!/usr/bin/env python3
"""build_tests.py - what carries his two round-24 versions, measured one thing of his at a time (the way h31 measured
his don't list), before it is carried to the stretches round 24's cards named (docs/lessons/2026-11-08-1507-bad-trips.md).

Each test takes out what I can't write myself, his own story, joke, opinion and images, and keeps his frame, so a Human
result says the frame carries:
  SNOJ   his Give the Session as the guide has it (the section, Human High as one window: 14a16456) without the Kenya
         story, the joke on "sitter" and his redosing aside: the order of a session, the reasons and the branches stay
  FNOJ   the Human base (the first five minutes to his reminder), then his anchor line and don'ts (Human High as one
         window: 82851dc3) without the witch doctor guru picture and the demon line with its aside: the role line, the
         scene items, the example, the concession and the soft end stay

  python3 build_tests.py      writes TEST-NAME.txt for each
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
B = {b['id']: b for b in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}


def plain(md):
    md = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md)
    md = re.sub(r'^#+\s*', '', md)
    return md.replace('**', '').replace('*', '')


def cut(t, s):
    assert t.count(s) == 1, s
    return re.sub(r'  +', ' ', t.replace(s, '')).strip()


SESSION = [B['B366%s' % k]['md'] for k in 'abcdefg']
s = list(SESSION)
assert s[2].startswith('One woman I met in Kenya')
del s[2]                                     # the Kenya story
s[3] = s[3].replace(' (the sober person with you, not literally someone sitting on your face!)', ' (the sober person with you)')
s[4] = cut(s[4], ' (I really don\'t like the MDMA protocols that include redosing, as it amplifies the neurotoxicity concerns)')
SNOJ = '\n\n'.join(['Give the Session a Beginning and an End'] + [plain(x) for x in s])

BASE = '\n\n'.join(['Psychological First Aid: The First Five Minutes'] + [plain(B[i]['md']) for i in ('B236', 'B240', 'B242')])
anchor = B['B284a']['md'].replace(', not the witch doctor guru who knows magic spells.', ', not a guru.')
assert anchor != B['B284a']['md']
donts = cut(B['B284b']['md'], "If they're being attacked by a demon, let your care help them connect to love, which cancels fear. "
                              "Hopefully they've been practicing that prior.")
FNOJ = '\n\n'.join([BASE, plain(anchor), plain(donts)])

for name, text in (('SNOJ', SNOJ), ('FNOJ', FNOJ)):
    (HERE / ('TEST-%s.txt' % name)).write_text(text)
    print(name, len(text.split()), 'words')
