#!/usr/bin/env python3
"""fill_h80.py - the making-sense receipts of turn 72's Beach Morning Glory try 1 (h80c), from the three fresh reads of
the section as it stood (reads/need-asis-bmg-sec.txt, his-asis-bmg-sec.txt, fit-asis-bmg-sec.txt). Run from this folder
after `sense_receipt.py make`, then `sense_receipt.py check TEXT RECEIPT`.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

S = {  # every sentence of the try: payoff (what the reader does with it), follows, and its tie at the start
    'In my experience, beach morning glory is the ultimate sledgehammer': (
        'they know what it is for: ending a psychedelic trip fast, when the trip has to stop',
        'the heading, Beach Morning Glory, under Need to Stop the Trip?', None),
    'By beach morning glory I mean': (
        'they get the one species, and don\'t swap in a garden morning glory or another relative (and in try 2, that '
        'it is hard to buy)',
        'the plant just named by its common name', 'By beach morning glory'),
    "It isn't sold anywhere else": (
        'they know they likely can\'t buy it in a shop, so they plan on it only if they already have it',
        'which plant exactly, just said', "It isn't sold"),
    'A whole leaf can easily end the trip': (
        'they know how much ends a trip, a whole leaf, and that psychedelics may not work for days after, so they give a '
        'leaf only when the trip has to end', 'the sledgehammer, said before: how much of it does that', None),
    'A tiny nibble can sometimes smooth': (
        'they know a small piece has another use, for nausea, that can leave the trip going',
        'the whole leaf, the large amount', 'A tiny nibble'),
    'A tiny nibble sometimes smooths': (
        'they know a small piece has another use, for nausea, that can leave the trip going',
        'the whole leaf, the large amount', 'A tiny nibble'),
    'But it takes only a little more than a nibble': (
        'they give it for nausea only to someone who has said they are fine with the trip ending',
        'the nibble for nausea: how close it is to the amount that ends the trip', 'But it takes only a little more'),
    'The leaf is strong enough that even picking one': (
        'they hold the leaf by its unbroken parts and keep its juice off their skin and from under their nails',
        'the sledgehammer and which plant, said before: how strong the leaf is, even its juice on the skin',
        'The leaf is strong enough'),
    "I've seen it work on someone else too: I once gave beach morning glory to a woman who was nauseous and miserable on a psychedelic, and within a couple of minutes she was very happy, though": (
        'they can expect it to work on their friend too, within minutes, and give less than they would in a rush',
        'his own reactions, said before', "I've seen it work on someone else too"),
    "I've seen it work on someone else too": (
        'they can expect it to work on their friend too, within minutes',
        'his own reactions, said before', "I've seen it work on someone else too"),
    'I was rushing to help her': (
        'they give less than they would in a rush', 'the woman, just described', 'I was rushing to help her'),
    "The trips I've seen it stop were psychedelic ones": (
        'they don\'t count on it for MDMA, and go to the MDMA section instead',
        'the woman\'s psychedelic trip, just told', "The trips I've seen it stop"),
}
CHECKED = {
    'p1': {'point': 'beach morning glory is Ipomoea pes-caprae, not morning glories in general; the relatives and cousins he '
                    'tried did not work the same way; as far as he knows nobody else sells it; in his experience it stops a '
                    'psychedelic trip cold and fast',
           'found': 'his post as of 2026-11-03, B171 and B172 (the guide\'s text since); "The distinction matters." cut (the '
                    'needed read: it only announces what the next words say)',
           'still_needed': 'yes: they get the right plant and use it when a trip has to end', 'fate': 'changed'},
    'p2': {'point': 'a whole leaf can easily end the trip and may prevent tripping for days afterward; a tiny nibble can smooth '
                    'nausea and improve the trip without ending it; the gap to a trip-ending amount is narrow; he uses it for '
                    'nausea only when the person is comfortable with the trip ending',
           'found': 'his post as of 2026-11-03, B175 and B173; the whole leaf now first, so the reader has the scale before the '
                    'nibble (the fit read could not judge the nibble against the amount that ends a trip)',
           'still_needed': 'yes: they know which amount does what and when to give the small one', 'fate': 'changed'},
    'p3': {'point': 'picking a leaf can affect him when the broken juicy part touches sensitive skin, especially under the '
                    'fingernails; avoiding contact with the broken part prevents it',
           'found': 'his post as of 2026-11-03, B174', 'still_needed': 'yes: they handle the leaf without the juice on their skin',
           'fate': 'changed'},
    'p4': {'point': 'he once gave it to a woman with nausea and dysphoria on a psychedelic; within a couple of minutes she went '
                    'from miserable to very happy; he was rushing and may have given more than he would now; it is not only '
                    'his body that reacts',
           'found': 'his post as of 2026-11-03, B176; "This was not only personal." cut (the needed read), and its point said '
                    'first ("I\'ve seen it work on someone else too")',
           'still_needed': 'yes: they can expect it to work on their friend, and give less than a rush would', 'fate': 'changed'},
    'p5': {'point': 'no data yet that pes-caprae aborts MDMA; MDMA has its own branch (the list of what that branch covers cut: '
                    'magnesium, overheating, sodium, potassium, water and seizures are in MDMA: Magnesium Alarm, serotonin '
                    'toxicity in Serotonin Syndrome (SS)?)',
           'found': 'his post as of 2026-11-03, B178; the list\'s only warning word, "toxicity", is part of "serotonin toxicity" '
                    '(his CHARCOAL-WORDS "a", FIDELITY-KEYS-R61.json not_cautions)',
           'still_needed': 'yes: they don\'t count on it for MDMA and go to the MDMA section', 'fate': 'changed'},
}
NEEDED_UNNEEDED = ['The distinction matters.', 'This was not only personal.']
HIS_MARKED = ['The distinction matters.', 'I have tried many related plants and cousins, and they did not work the same way.',
              'As far as I know, nobody else sells it.', 'Its primary role in this guide is not ordinary nausea control.',
              'A tiny nibble can sometimes smooth psychedelic nausea and improve the trip without killing it, but the difference between that amount and a trip-aborting amount is narrow.',
              'Even picking a leaf can affect me when the broken juicy part touches sensitive skin, especially under the fingernails.',
              'Avoiding contact with the broken portion prevents that effect.',
              'A whole leaf can easily end the trip and, in my experience, may prevent tripping for days afterward.',
              'This was not only personal.', 'I was rushing to help and may have given more than I would now.',
              "That helped convince me the effect wasn't limited to my body.",
              'I do not yet have data showing that pes-caprae aborts MDMA.',
              'MDMA remains [a separate branch](#§mdma-magnesium-alarm) centered on magnesium, temperature, sodium, potassium, hydration, serotonin toxicity, seizure, and cardiovascular symptoms.']
FIT_MARKED = HIS_MARKED[4:5] + ['I was rushing to help and may have given more than I would now.', 'This was not only personal.']
Q = {
    'Q1': 'PASS: each sentence opens on what it is about (the sledgehammer, which plant, how much, the nibble, the juice, the '
          'woman, the trips it stopped); the needed read\'s two announcing lines are cut',
    'Q2': 'PASS: what he does is said as what he does ("I use it for nausea only when ...", "I keep my skin away from the '
          'broken end", "go to MDMA: Magnesium Alarm")',
    'Q3': 'PASS: a whole leaf, a tiny nibble, the broken end, sensitive skin under the fingernails; the nibble\'s size is his '
          'to give (round 62, NIBBLE-SIZE), and the whole leaf now comes first as its scale',
    'Q4': 'PASS: "dysphoria" said in plain words ("nauseous and miserable"); "aborts" kept, his warning key (W053)',
    'Q5': 'PASS: each tie is at the start ("By beach morning glory", "A tiny nibble", "But it takes only a little more", "The '
          'leaf is strong enough", "I\'ve seen it work on someone else too", "The trips I\'ve seen it stop")',
    'Q6': 'PASS: what it is for, which plant, how much does what, handling, someone else, where it doesn\'t apply',
    'Q7': 'PASS: each fact is something a sitter acts on; the MDMA list went to the link, where each item is',
    'Q8': 'PASS: no group of items left; the MDMA list is cut',
    'Q9': 'PASS: the nibble sentence split in two; no run of category words left',
}


import sys
ONLY = sys.argv[1:]


def fill(key, checked, placement, same_point):
    if ONLY and key not in ONLY:
        return
    p = HERE / ('TEST-%s.receipt.json' % key)
    r = json.loads(p.read_text(encoding='utf-8'))
    for x in r['sentences']:
        hit = sorted([k for k in S if x['s'].startswith(k)], key=len)[-1:]
        assert len(hit) == 1, x['s']
        pay, fol, link = S[hit[0]]
        x['payoff'], x['follows'] = pay, fol
        if 'link' in x:
            x['link'] = link or 'none: the paragraph\'s first sentence, which opens on what the paragraph is about'
    r['checked'] = [CHECKED[c] for c in checked]
    r['placement'] = placement
    r['opens']['why_reading'] = S[sorted([k for k in S if r['opens']['first_sentence'].startswith(k)], key=len)[-1]][0]
    r['same_point'] = same_point
    r['needed'] = {'reader': 'a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md and the section as it '
                             'stood (reads/need-asis-bmg-sec.txt)', 'unneeded': NEEDED_UNNEEDED, 'kept': {}}
    r['his_fixes'] = {'reader': 'a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md and the section as it '
                                'stood (reads/his-asis-bmg-sec.txt); every marked sentence is rewritten or cut',
                      'marked': HIS_MARKED, 'kept': {}}
    r['fit'] = {'reader': 'a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md and the section as it stood '
                          '(reads/fit-asis-bmg-sec.txt)', 'marked': FIT_MARKED, 'kept': {}}
    r['questions'] = dict(Q)
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


fill('a1-bmg-p1', ['p1'], 'Beach Morning Glory\'s first paragraph (B171, with B172 joined in), checked by itself (55 words)',
     'merged here: B172 (what it is for) joins B171, and block B172 is deleted; none other: read the section from its heading to the next for what it is for and which plant')
fill('a1-bmg-p2', ['p2'], 'the paragraph after it (B173, with B175\'s whole leaf moved to its start), checked by itself (67 words)',
     'merged here: B175 (the whole leaf) moves to the start of B173, and block B175 is deleted; none other: read the section from its heading to the next for the amounts')
fill('a1-bmg-p2p3', ['p2', 'p3'], 'B173 (with B175) and the handling paragraph after it (B174), checked together since B174 '
     'is 36 words', 'merged here: B175 (the whole leaf) moves to the start of B173, and block B175 is deleted; none other: read the section from its heading to the next for the amounts and the handling')
fill('a1-bmg-p4p5', ['p4', 'p5'], 'the woman paragraph (B176) and the MDMA line after it (B178), the section\'s last two, '
     'checked together since B178 is 29 words', 'none: read the section from its heading to the next for the case and the MDMA limit; the MDMA list is said in MDMA: Magnesium Alarm and Serotonin Syndrome (SS)?, which the link opens')
fill('a2-bmg-p1', ['p1'], 'Beach Morning Glory\'s first paragraph (B171, with B172 joined in), try 2, checked by itself '
     '(54 words)', 'merged here: B172 (what it is for) joins B171, and block B172 is deleted; none other: read the section '
     'from its heading to the next for what it is for and which plant')
fill('b1-bmg-p3p4', ['p3', 'p4'], 'the handling paragraph (B174, 36 words) with the woman paragraph after it (B176), checked '
     'together; with the paragraph before it, B174 read Human Low (16784f2b)', 'none: read the section from its heading to '
     'the next for the handling and the case')
fill('b2-bmg-p3p4', ['p3', 'p4'], 'the handling paragraph (B174, 36 words) with the woman paragraph after it (B176, try 2), '
     'checked together', 'none: read the section from its heading to the next for the handling and the case')
fill('a2-bmg-p4p5', ['p4', 'p5'], 'the woman paragraph (B176, try 2) and the MDMA line after it (B178), checked together since '
     'B178 is 29 words', 'none: read the section from its heading to the next for the case and the MDMA limit; the MDMA list is '
     'said in MDMA: Magnesium Alarm and Serotonin Syndrome (SS)?, which the link opens')
fill('b3-bmg-p3p4', ['p3', 'p4'], 'the handling paragraph (B174, 36 words) with the woman paragraph after it (B176, try 3), '
     'checked together', 'none: read the section from its heading to the next for the handling and the case')
fill('a3-bmg-p4p5', ['p4', 'p5'], 'the woman paragraph (B176, try 3) and the MDMA line after it (B178), checked together since '
     'B178 is 29 words', 'none: read the section from its heading to the next for the case and the MDMA limit; the MDMA list is '
     'said in MDMA: Magnesium Alarm and Serotonin Syndrome (SS)?, which the link opens')
fill('c1-bmg-p1p3', ['p1', 'p3'], 'the handling paragraph (B174, 36 words) moved up after the first paragraph (B171), '
     'checked with it: the leaf\'s strength comes before the amounts (a whole leaf, then a nibble)', 'merged here: B172 joins '
     'B171 (block B172 deleted); B174 moves up before B173; none other: read the section from its heading to the next for '
     'which plant and the handling')
fill('a2-bmg-p2', ['p2'], 'the amounts paragraph (B173, with B175\'s whole leaf at its start), try 2, checked by itself '
     '(67 words)', 'merged here: B175 (the whole leaf) moves to the start of B173, and block B175 is deleted; none other: read '
     'the section from its heading to the next for the amounts')
print('filled')
