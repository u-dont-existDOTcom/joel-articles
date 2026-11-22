#!/usr/bin/env python3
"""fill_receipts3.py - the receipt of turn 58's third try at steps 5 and 6 of the serotonin steps (B136): the second try's
steps in his first person ("I'd", "I wouldn't"), the register of his own step 2, which read Human by itself and carried
its pair; every step of mine in the second person read AI, step 1 by itself included. Its three fresh reads are
reads/*-g4c-ss56-4.txt; every sentence they marked was changed before the check.

  python3 fill_receipts3.py        then sense_receipt.py check TEST-g4c-ss56-4.txt TEST-g4c-ss56-4.receipt.json
"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fill_receipts as F  # noqa: E402

F.READ = READ = 'g4c-ss56-4'
F.NEED = F.NEED.replace('g1-ss-steps-2', READ).replace('the whole list as I first drafted it', 'steps 5 and 6 as drafted in their third try')
F.HISF = F.HISF.replace('g1-ss-steps-2', READ).replace('the whole first draft', 'the third try\'s draft')
F.FIT = F.FIT.replace('g1-ss-steps-2', READ).replace('the whole first draft', 'the third try\'s draft')
F.PAY = {
    "Keep them still in a calm room.": (
        'they keep their friend from moving about, in a quiet room', 'the next step, after cooling', None),
    "They're already overstimulated, so I'd clear out the crowd and stop any arguing.": (
        'they clear people out and stop any arguing, knowing why', 'what a calm room means', 'so'),
    "Pacing or exercising to \"burn it off\" only makes more heat, and it raises the risk of their muscles breaking down into the blood, which hurts the kidneys (rhabdomyolysis).": (
        'they stop pacing and exercise, knowing the two dangers of it, the second said plainly and named',
        'what keeping still is for', 'Pacing or exercising to'),
    "If they feel a strong urge to keep moving (akathisia), I'd stay with them and talk them into keeping still anyway.": (
        'they keep their friend still by staying with them and talking, even when the urge is strong, and know its name',
        'the case where keeping still is hard', 'anyway'),
    "Give fluids only if they're fully alert, able to swallow and not vomiting, and then just small sips of an electrolyte drink.": (
        'they know when they can give a drink, which drink and how much', 'the next step, after keeping them still', None),
    "But if they're confused, vomiting or sleepy, I wouldn't push anything into them, not even pills or charcoal, since they could choke.": (
        'they give nothing by mouth to a friend who is confused, vomiting or sleepy, and know why',
        'the other case, when they can\'t give fluids', 'But if'),
    "The same goes if they might have a seizure.": (
        'they give nothing by mouth to a friend who might have a seizure either', 'the last case', 'The same goes'),
}
F.KEEP_NEED, F.KEEP_HIS, F.KEEP_FIT = {}, {}, {}
F.CHECKED = [F.CHECKED[0]]
F.CHECKED[0] = dict(F.CHECKED[0], point='rhabdomyolysis, said as the muscles breaking down into the blood, which hurts the kidneys')
F.KEYS = {'g4c-ss56-4': ('steps 5 and 6', F.KEYS['g1c-ss56-2'][1])}
F.PLACE = F.PLACE.replace('in place of the eight steps as they are;', 'in place of the eight steps as they are, in his first '
                          'person where a step says what to do, as his own step 2 is;')
F.Q = dict(F.Q)
F.Q['Q9'] = ('PASS: one point a sentence, of different lengths; the tell panel\'s agreed sentences changed '
            '(panel-g4c/PANEL.md): the matched opening, the glosses said his way (the plain words, then the term in '
            'brackets; "able to swallow" from his step 2), the trailing qualifier and the tidy list gone')

if __name__ == '__main__':
    F.fill('g4c-ss56-4')
    print('filled g4c-ss56-4')
