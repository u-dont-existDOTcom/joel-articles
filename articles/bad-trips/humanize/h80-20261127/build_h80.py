#!/usr/bin/env python3
"""build_h80.py - turn 72's texts for Pangram, built from the guide's blocks so his text is copied, never retyped; only the
sentences I change are written here.

  python3 build_h80.py h80a       writes batch h80a's TEST-KEY.txt (as the guide stood at the turn's start)
  python3 build_h80.py            writes Beach Morning Glory's try-1 texts (h80c)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
# the guide's blocks as they stood when the turn started (main at 87e90c44, before round 61's answers went in), so his text
# is copied from Git, never retyped, and the texts rebuild the same way after the guide changes
import subprocess  # noqa: E402
START = '87e90c44edfe82ba744e126196a5123cf388ff53'
B = {x['id']: x['md'] for x in json.loads(subprocess.run(
    ['git', 'show', START + ':articles/bad-trips/GUIDE-SO-FAR-blocks.json'], cwd=HERE, capture_output=True, text=True,
    check=True).stdout)}
B['B155'] = {x['id']: x['md'] for x in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}['B155']  # his round-61 version


def swap(text, old, new):
    if old not in text and text.count(new) == 1:   # already in the guide (applied after its check)
        return text
    assert text.count(old) == 1, (old, text)
    return text.replace(old, new)


# FROM-POST (round 61): the rubbing is with zeolite mixed in water (his comment: "yes mix in water when rubbing on body")
B158 = swap(B['B158'], 'Rubbing the zeolite on my body,', 'Rubbing zeolite mixed in water on my body,')
# the section check's short Medium lines in B156 (b9d02255), joined to the sentences that draw their point
B156 = swap(B['B156'], 'because ozone destroys plastic. I mean ozonating water',
            'because ozone destroys plastic, and I mean ozonating water')
B156 = swap(B156, 'however much zeolite was in the water. Less time didn\'t work as well, and more time didn\'t noticeably '
            'improve the zeolite.', 'however much zeolite was in the water: less time didn\'t work as well, and more time '
            'didn\'t noticeably improve it.')

TEXTS = {
    'a3-b158': B158,
    'his-b155-b156': B['B155'] + '\n\n' + B['B156'],
    'a3-b156': B156,
    'asis-b171-b172': B['B171'] + '\n\n' + B['B172'],
    'asis-b173-b174': B['B173'] + '\n\n' + B['B174'],
    'asis-b175-b176': B['B175'] + '\n\n' + B['B176'],
    'asis-b176-b178': B['B176'] + '\n\n' + B['B178'],
}

if __name__ == '__main__' and sys.argv[1:] == ['h80a']:
    for k, t in TEXTS.items():
        (HERE / ('TEST-%s.txt' % k)).write_text(t.strip() + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words')

# Beach Morning Glory, try 1 (h80c): the three reads of the section as it stands (reads/*-asis-bmg-sec.txt), written his
# ways: "The distinction matters." and "This was not only personal." cut (the needed read); B172 joined to B171 and B175
# moved up into B173, so the whole leaf comes before the nibble; each sentence's tie at its start; the MDMA list cut to
# the link (every item of it is in the medical part: MDMA: Magnesium Alarm, and Serotonin Syndrome (SS)?)
BMG = {
    'P1': ("In my experience, beach morning glory is the ultimate sledgehammer for stopping a psychedelic trip cold and fast. "
           "By beach morning glory I mean *Ipomoea pes-caprae*, not morning glories in general, since none of the many "
           "relatives and cousins I tried worked the same way. It isn't sold anywhere else, as far as I know."),
    'P2': ("A whole leaf can easily end the trip and, in my experience, may keep you from tripping for days afterward. A tiny "
           "nibble can sometimes smooth psychedelic nausea and even improve the trip without ending it. But it takes only a "
           "little more than a nibble to end the trip, so I use it for nausea only when the person is okay with their trip "
           "possibly ending."),
    'P3': ("The leaf is strong enough that even picking one can affect me if the juice from the broken part touches "
           "sensitive skin, especially under my fingernails, so I keep my skin away from the broken end."),
    'P4': ("I've seen it work on someone else too: I once gave beach morning glory to a woman who was nauseous and miserable "
           "on a psychedelic, and within a couple of minutes she was very happy. I was rushing to help her and may have "
           "given more than I would now."),
    'P5': ("The trips I've seen it stop were psychedelic ones, and I don't yet have data showing that pes-caprae aborts MDMA, "
           "so for MDMA, go to [MDMA: Magnesium Alarm](#§mdma-magnesium-alarm) instead."),
}
TEXTS.update({
    'a1-bmg-p1': BMG['P1'],
    'a1-bmg-p2': BMG['P2'],
    'a1-bmg-p2p3': BMG['P2'] + '\n\n' + BMG['P3'],
    'a1-bmg-p4p5': BMG['P4'] + '\n\n' + BMG['P5'],
})

if __name__ == '__main__':
    for k in ('a1-bmg-p1', 'a1-bmg-p2', 'a1-bmg-p2p3', 'a1-bmg-p4p5'):
        (HERE / ('TEST-%s.txt' % k)).write_text(TEXTS[k].strip() + '\n', encoding='utf-8')
    for k, v in BMG.items():
        print(k, len(v.split()), 'words')

# try 2 of the first paragraph (h80d): try 1 (c747346c) read High 46 with its short last line Medium 11; that line joins
# the sentence before, with the relation it has to it ("though": you need this one, though nobody else sells it)
P1_A2 = BMG['P1'].replace("worked the same way. It isn't sold anywhere else, as far as I know.",
                          "worked the same way, though as far as I know nobody else sells it.")
assert P1_A2 != BMG['P1']
TEXTS.update({'a2-bmg-p1': P1_A2, 'b1-bmg-p3p4': BMG['P3'] + '\n\n' + BMG['P4']})
if __name__ == '__main__':
    for k in ('a2-bmg-p1', 'b1-bmg-p3p4'):
        (HERE / ('TEST-%s.txt' % k)).write_text(TEXTS[k].strip() + '\n', encoding='utf-8')

# try 2 of the woman paragraph (h80e): beside the handling paragraph its last sentence read Human Low 15 (60554a64), though
# it read High beside the MDMA line (7a332a1b); the sentence says how the rush led to the amount ("so"), two words
P4_A2 = BMG['P4'].replace('I was rushing to help her and may have given more than I would now.',
                          'I was rushing to help her, so I may have given her more than I would now.')
assert P4_A2 != BMG['P4']
TEXTS.update({'b2-bmg-p3p4': BMG['P3'] + '\n\n' + P4_A2, 'a2-bmg-p4p5': P4_A2 + '\n\n' + BMG['P5']})
if __name__ == '__main__':
    for k in ('b2-bmg-p3p4', 'a2-bmg-p4p5'):
        (HERE / ('TEST-%s.txt' % k)).write_text(TEXTS[k].strip() + '\n', encoding='utf-8')

# try 3 of the woman paragraph (h80f): at the end of a check its rushing sentence read Low 15 (60554a64), then Medium 17 with
# "so" (e1ccdb68), and High in the middle of one (7a332a1b, caae0369). A join is refused after a near miss (the ledger counts
# a joined sentence's words as new: 21%), so one word: "more than I would now" could stop short of its verb, "would give"
P4_A3 = P4_A2.replace('so I may have given her more than I would now.', 'so I may have given her more than I would give now.')
assert P4_A3 != BMG['P4']
TEXTS.update({'b3-bmg-p3p4': BMG['P3'] + '\n\n' + P4_A3, 'a3-bmg-p4p5': P4_A3 + '\n\n' + BMG['P5']})
if __name__ == '__main__':
    for k in ('b3-bmg-p3p4', 'a3-bmg-p4p5'):
        (HERE / ('TEST-%s.txt' % k)).write_text(TEXTS[k].strip() + '\n', encoding='utf-8')

# the handling paragraph moved up (h80g): beside the woman paragraph its own words read High three times (60554a64,
# e1ccdb68, 64cb7a2a) but the pair's last line, the woman paragraph's rushing sentence, stays below High at the end of a
# check (Low 15, Medium 17, Medium 18) and High inside one (7a332a1b, caae0369, 2dfaa7bb). Its place is also better after
# which plant and before the amounts: the leaf's strength ("even picking one"), then a whole leaf, then a nibble
P1_FINAL, P3_FINAL, P4_FINAL = P1_A2, BMG['P3'], P4_A3
TEXTS.update({'c1-bmg-p1p3': P1_FINAL + '\n\n' + P3_FINAL})
if __name__ == '__main__':
    (HERE / 'TEST-c1-bmg-p1p3.txt').write_text(TEXTS['c1-bmg-p1p3'].strip() + '\n', encoding='utf-8')

# try 2 of the amounts paragraph (h80i): by itself it read High (6bc70ed9), but beside the handling paragraph its first two
# sentences read Low twice (16784f2b, and in the section, e1629a55): two sentences built the same way, "A whole leaf can
# easily end ..." and "A tiny nibble can sometimes smooth ..." (way 2). The second says what the nibble does without the
# hedge its "sometimes" already makes; the whole leaf keeps its "can", which is the claim
P2_A2 = BMG['P2'].replace('A tiny nibble can sometimes smooth psychedelic nausea and even improve the trip',
                          'A tiny nibble sometimes smooths psychedelic nausea and even improves the trip')
assert P2_A2 != BMG['P2']
P2_FINAL = BMG['P2']   # try 2 read Medium 35 by itself (99d65f8f), worse than try 1's High 67: try 1 stays
TEXTS.update({'a2-bmg-p2': P2_A2})
if __name__ == '__main__':
    (HERE / 'TEST-a2-bmg-p2.txt').write_text(TEXTS['a2-bmg-p2'].strip() + '\n', encoding='utf-8')
