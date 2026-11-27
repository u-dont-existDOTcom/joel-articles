#!/usr/bin/env python3
"""fill_h82.py - the making-sense receipts of turn 74's steps (his round-63 answers), from the three fresh reads of the
section as first drafted with both answers in (reads/need-, his-, fit-draft-bmg-sec.txt; the draft is TEST-draft-bmg-sec.txt).
Each receipt maps his answers' claims to the sentences that carry them (his_answer, lesson bad-trips-2026-11-27k).

  python3 fill_h82.py [KEY...]
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
A62 = 'review/r62/ANSWERS-R62-20261127-1716.json'
A63 = 'review/r63/ANSWERS-R63-20261127-2003.json'

S = {  # every sentence of the steps: payoff (what the reader does with it), follows, and its tie at the start
    'In my experience, beach morning glory is the ultimate sledgehammer': (
        'they know what it is for: ending a psychedelic trip fast, when the trip has to stop',
        'the heading, Beach Morning Glory, under Need to Stop the Trip?', None),
    'By beach morning glory I mean': (
        'they get the one species, don\'t swap in a garden morning glory or another relative, and know they likely can\'t '
        'buy it from just any seller', 'the plant just named by its common name', 'By beach morning glory'),
    'People still find it growing in some places': (
        'they look for it growing, and search for it under another name, railroad vine',
        'nobody else sells it, just said: where else to get it', 'People still find it'),
    'The leaf is strong enough that even picking one': (
        'they keep the juice from the broken end off their own sensitive skin and from under their nails while they '
        'handle a leaf', 'the plant and how much of it does what, said before: how strong its leaf is, even its juice '
        'on sensitive skin', 'The leaf is strong enough'),
    'Its juice works through sensitive skin almost as well as eating the leaf does, so': (
        'they have a second way to give it on purpose, on sensitive skin (under the armpits, for example), since it '
        'works there almost as well as eating it', 'the juice on his sensitive skin, just said: what it does there, and '
        'how to use that', 'Its juice'),
    "I'd use about the same amounts as by mouth": (
        'they give the same amounts on the skin as by mouth, or a few drops of fresh juice, so the skin route does what '
        'the same amount eaten would', 'the skin route, just said: how much', "I'd use about the same amounts"),
    'Eating a whole leaf can easily end the trip': (
        'they know eating a whole leaf is what ends a trip and may keep their friend from tripping for days, so they give '
        'a whole leaf only when the trip has to end', 'which plant and where to find it, said before: how much of it does '
        'what, and taken how', None),
    "I've seen it work on someone else too": (
        'they can expect it to work on their friend too, within minutes', 'how to give it and how much, said before: '
        'that it works on others', "I've seen it work on someone else too"),
    'I once gave beach morning glory to a woman': (
        'they can expect it to work on their friend too, within minutes', 'it works on others, just said: the case',
        'I once gave beach morning glory to a woman'),
    'I may have given her more than I would give now': (
        'they give less than they would in a rush', 'the woman, just described: how much she got',
        'I may have given her more'),
    "The trips I've seen it stop were psychedelic ones": (
        'they don\'t count on it for MDMA, and go to the MDMA section instead',
        'the woman\'s psychedelic trip, just told', "The trips I've seen it stop"),
    'A whole leaf can easily end the trip': (
        'they know a whole leaf is the amount that ends a trip and may keep their friend from tripping for days, so they '
        'give a whole leaf only when the trip has to end', 'which plant and where to find it, said before: how much of '
        'it does what', None),
    'A tiny nibble can sometimes smooth psychedelic nausea and even smooth the trip': (
        'they know a small piece has another use, for nausea, that can smooth the trip and leave it going',
        'the whole leaf, the large amount, just said', 'A tiny nibble'),
    "For nausea I'd try 200mg of leaf at a time": (
        'they know how much to start with for nausea, and what the extract paste is',
        'the nibble for nausea, just said: how big a nibble is', 'For nausea'),
    'But it takes only a little more than a nibble': (
        'they give it for nausea only to someone who has said they are fine with the trip ending',
        'the amounts, just given: how close they are to the amount that ends the trip', 'But it takes only a little more'),
}
CHECKED = {
    'p4': {'point': 'he once gave it to a woman with nausea and dysphoria on a psychedelic; within a couple of minutes she went '
                    'from miserable to very happy; he was rushing and may have given more than he would now; it is not only '
                    'his body that reacts',
           'found': 'his post as of 2026-11-03, B176, as it read Human High 86 with B178 (2dfaa7bb)',
           'still_needed': 'yes: they can expect it to work on their friend, and give less than a rush would', 'fate': 'changed'},
    'p5': {'point': 'no data yet that pes-caprae aborts MDMA; MDMA has its own section, which the link opens',
           'found': 'his post as of 2026-11-03, B178, as it read Human High 86 with B176 (2dfaa7bb)',
           'still_needed': 'yes: they don\'t count on it for MDMA and go to the MDMA section', 'fate': 'kept'},
    'p1': {'point': 'beach morning glory is Ipomoea pes-caprae, not morning glories in general; the relatives and cousins he '
                    'tried did not work the same way; as far as he knows nobody else sells it; in his experience it stops a '
                    'psychedelic trip cold and fast',
           'found': 'his post as of 2026-11-03, B171 and B172; B171 as it read Human High 56 (ecce6d40), unchanged',
           'still_needed': 'yes: they get the right plant and use it when a trip has to end', 'fate': 'kept'},
    'p1v': {'point': 'as p1, and: people can still find it growing in some places, and railroad vine is one name used for '
                     'it; he sells the extract paste but doesn\'t want the guide to say so (a sales pitch), and it doesn\'t',
            'found': 'his post as of 2026-11-03, B171; his round-63 comment (%s, card TEACH-B173): "nobody is selling it '
                     'other than me but ppl can find it in some places growing (railroad vine is one name used)"' % A63,
            'still_needed': 'yes: they get the right plant, and look for it growing under a name they can search',
            'fate': 'changed'},
    'p3': {'point': 'picking a leaf can relax him when the juice from the broken part touches sensitive skin, especially under '
                    'the fingernails, so he keeps his skin away from the broken end; the juice works through sensitive skin '
                    'almost as well as eating it; to give it on purpose it can go under the armpits, for example, in about '
                    'the same amounts as by mouth, or maybe a few drops of the juice',
           'found': ('his round-62 answer (%s, card LEAF-JUICE) and his round-63 answer (%s, card SKIN-AMOUNT): "you forgot '
                     'the most important part, sensitive skin... that\'s why i said under the armpits ... i said like 200mg '
                     'of leaf or 10mg of the extract (dried juice paste)... maybe a few drops of the juice altho i don\'t '
                     'think anyone has the juice"' % (A62, A63)),
           'still_needed': 'yes: they keep the juice off their own sensitive skin, and can give it through the skin on '
                           'purpose, in amounts they know', 'fate': 'changed'},
    'p2': {'point': 'a whole leaf can easily end the trip and may prevent tripping for days afterward; a tiny nibble can '
                    'smooth nausea and even smooth the trip without ending it; for nausea he would try 200mg of leaf at a '
                    'time, or 10mg of the extract paste, which is the dried juice; the gap to a trip-ending amount is narrow, '
                    'so he uses it for nausea only when the person is okay with the trip ending',
           'found': ('his round-63 version (%s, card TEACH-B173), whole: his check, Human High 84 in one window '
                     '(09e42ca2, review/r63/HIS-CHECKS-R63.json); "(the dried juice)" from his comment there, "it\'s the '
                     'dried juice"' % A63),
           'still_needed': 'yes: they know how much to start with for nausea, and when not to give it', 'fate': 'changed'},
}
DRAFT = {}
for line in (HERE / 'reads' / 'prompt-his-draft-bmg-sec.txt').read_text(encoding='utf-8').splitlines():
    m = re.match(r'^(S\d+): (.*)$', line)
    if m:
        DRAFT[m.group(1)] = m.group(2).strip()
assert DRAFT['S3'].startswith('People can still') and DRAFT['S10'].startswith('But it takes'), DRAFT

NEEDED_UNNEEDED = ['though as far as I know nobody else sells it', DRAFT['S11'], DRAFT['S12'], DRAFT['S13'],
                   "maybe a few drops of the juice, although I don't think anyone has the juice"]
NEEDED_KEPT = {
    DRAFT['S11']: ('they know it works on other people too, not only on him, so they can expect it to work on their friend; '
                   'it is the start of the sentence that tells the case'),
    DRAFT['S12']: ('they see how fast it works on someone else (within a couple of minutes), so they know when to look for '
                   'the change in their friend; his only case of giving it to someone else'),
    'though as far as I know nobody else sells it': (
        'they know they won\'t find it for sale, so they look for it growing, under names like railroad vine (the next '
        'sentence in the guide); his fact from his post'),
}
HIS_MARKED = [{'s': DRAFT[k], 'difference': d} for k, d in (
    ('S3', '4, 1: "in some places" names no place; two ideas joined'),
    ('S4', '1, 4, 12: packed; "relax me" vague; no tie to finding the plant'),
    ('S5', '10, 4: "it" could be the juice, the leaf or the paste; "for example" leaves other places open'),
    ('S6', '10, 19, 4, 7, 15: "For that" two ways; three options alike; "a few drops" no amount; the juice offered, then '
           'said nobody has it'))]
HIS_KEPT = {
    DRAFT['S4']: ('his handling line as it read High with B171 (bb2893ad) and with his LEAF-JUICE in (6026d11b); "relax '
                  'me" is his word ("touching the juice is relaxing"), and the clauses are his: what the juice does, where, '
                  'and what he does about it; it follows the amounts paragraph now, so it needs no tie to finding the plant'),
    DRAFT['S5']: ('"it" is the plant in whatever form: the next sentence says the amounts, as by mouth (leaf or paste), or '
                  'drops of fresh juice; "for example" is his ("can put it under armpits for example")'),
    DRAFT['S3']: ('rewritten as "People still find it growing in some places, under names like railroad vine.": one '
                  'idea, where to find it and the name to look for; "some places" is his, and he named none'),
}
FIT_MARKED = [{'s': DRAFT[k], 'found': f} for k, f in (
    ('S6', 'CAN\'T TELL: no scale, "a few drops" vague; MISREAD: "For that", and the skin dose looks like a second dose'),
    ('S9', 'CAN\'T TELL: no scale, "at a time"; MISREAD: matches the skin amount, so which one ends the trip'),
    ('S10', 'CAN\'T TELL: where a nibble stops'),
    ('S13', 'CAN\'T TELL: no amount for what she got'))]
FIT_KEPT = {
    DRAFT['S9']: ('his amounts, from his version: he gave mg (round 62, NIBBLE-SIZE, when asked for a size a sitter can '
                  'see); the MISREAD came from the skin amounts said before them, and the skin route now comes after them '
                  'as "the same amounts as by mouth"'),
    DRAFT['S10']: 'his sentence, in his version whole: the narrow margin is what it tells the reader',
    DRAFT['S13']: 'not in these texts: B176, his story as it read Human High 86 with B178 (2dfaa7bb)',
}
Q = {
    'Q1': 'PASS: each sentence opens on what it is about (the sledgehammer, which plant, where to find it, the leaf\'s '
          'strength, its juice, the amounts on the skin, the whole leaf, the nibble, the amounts for nausea, how close the '
          'end is)',
    'Q2': 'PASS: what he does is said as what he does ("I keep my skin away", "I\'d use about the same amounts", "I\'d try '
          '200mg", "I use it for nausea only when"), and the skin route as what the reader can do',
    'Q3': 'PASS: sensitive skin under the fingernails, the armpits, the same amounts as by mouth, 200mg of leaf at a time, '
          '10mg of the extract paste (the dried juice), railroad vine',
    'Q4': 'PASS: "the extract paste" is said as the dried juice where it is first used; "relax" and "smooth" are his words',
    'Q5': 'PASS: each tie is at the start ("By beach morning glory", "People still find it", "The leaf is strong '
          'enough", "Its juice", "I\'d use about the same amounts", "A tiny nibble", "For nausea", "But it takes only a '
          'little more")',
    'Q6': 'PASS: which plant and where to find it, how much does what by mouth, then handling and the skin route, whose '
          'amounts point back to the ones just given',
    'Q7': 'PASS: each fact is something a sitter acts on: where to get it, how much by mouth, what to keep off their skin, '
          'how to give it through the skin',
    'Q8': 'PASS: no group of items left; the draft\'s three skin options are now "the same amounts as by mouth, or a few '
          'drops of fresh juice"',
    'Q9': 'PASS: each step adds one piece of his answers',
}
LJ = 'touching the juice is relaxing, especially on sensitive skin, it absorbs almost as well as eating it'
B174_S4 = ('The leaf is strong enough that even picking one can relax me if the juice from the broken part touches sensitive '
           'skin, especially under my fingernails, so I keep my skin away from the broken end.')
B174_S5_JUICE = ('Its juice works through sensitive skin almost as well as eating the leaf does, so to give it on purpose, you '
                 'can put the juice under the armpits, for example.')
B174_S5_IT = B174_S5_JUICE.replace('put the juice under', 'put it under')
B174_S6 = "I'd use about the same amounts as by mouth, or maybe a few drops of fresh juice if you have any."
ABSORB = {'absorbs': 'said as "works through"', 'absorb': 'said as "works through"'}
MINE_TO_HIM = ('his note to me on what my sentence had dropped ("sensitive skin"), not a claim for the reader; "sensitive" '
               'and "armpits" are in the sentence')
HIS = {
    'c6': lambda s5: [
        {'said': LJ, 'in': B174_S4 + ' ' + s5, 'words': ABSORB},
        {'said': 'can put it under armpits for example to absorb well', 'in': s5, 'words': ABSORB},
        {'said': "you forgot the most important part, sensitive skin... that's why i said under the armpits", 'in': s5,
         'words': {w: MINE_TO_HIM for w in ('forgot', 'most', 'important', 'part')}}],
    'c7': lambda s5: HIS['c6'](s5) + [
        {'said': 'i said like 200mg of leaf or 10mg of the extract (dried juice paste)', 'in': B174_S6,
         'words': {w: ('in the amounts by mouth, the paragraph before this one in the guide (B173: "200mg of leaf at a time, '
                       'or 10mg of the extract paste (the dried juice)"), which "the same amounts as by mouth" points to')
                   for w in ('leaf', 'extract', 'dried', 'paste')}},
        {'said': "maybe a few drops of the juice altho i don't think anyone has the juice", 'in': B174_S6,
         'words': {'think': 'said as "if you have any": he doubts many people have the juice itself',
                   'anyone': 'said as "if you have any": he doubts many people have the juice itself'}}],
    'f1b173': lambda _: [
        {'said': "it's the dried juice",
         'in': "For nausea I'd try 200mg of leaf at a time, or 10mg of the extract paste (the dried juice)."}],
    'none': lambda _: [],
    'v1': lambda _: [
        {'said': 'ppl can find it in some places growing (railroad vine is one name used)',
         'in': 'People still find it growing in some places, under names like railroad vine.',
         'words': {'used': 'said as "under names like"'}}],
    'd1': lambda _: [
        {'said': "it's the dried juice",
         'in': "For nausea I'd try 200mg of leaf at a time, or 10mg of the extract paste (the dried juice)."}],
}
PLACE = {
    'f1-bmg-b173': ('the amounts paragraph (B173), his version with "(the dried juice)" (Human High 87 by itself, bf3ae1f3), '
                    'after the section\'s second check read its first two sentences Medium 36 (3a2d2b12): one word, '
                    '"Eating", how the leaf is taken'),
    'f1-bmg-p4p5': ('the woman paragraph (B176) and the MDMA line after it (B178), checked together as they read Human High 86 '
                    '(2dfaa7bb), after the section\'s second check read B176\'s last line Medium 18 (3a2d2b12): its payoff first'),
    'c6-bmg-p1p3': ('B171 and the handling paragraph (B174), checked together as in turn 73 (Human High 122, 6026d11b); '
                    'step 1 of his SKIN-AMOUNT answer, the "sensitive skin" my sentence dropped'),
    'c7-bmg-p1p3': ('B171 and the handling paragraph (B174); step 2 of his SKIN-AMOUNT answer, the amounts, said as the same '
                    'amounts as by mouth, since B174 now follows the amounts paragraph (B173), and his drops of fresh juice'),
    'v1-bmg-p1': ('Beach Morning Glory\'s first paragraph (B171) by itself, as it read Human High 56 (ecce6d40); his comment '
                  'on TEACH-B173: where people can still find it, and a name to look for'),
    'd1-bmg-b173': ('the amounts paragraph (B173), his TEACH-B173 version whole (his check, Human High 84, 09e42ca2), with '
                    'what the extract paste is said where it is first used, since it now comes before the handling paragraph'),
}
SAME = {
    'f': 'none: read the section from its heading to the next; the amounts are said only in the amounts paragraph, the case '
         'and the MDMA limit only in the last two',
    'c': 'none: read the section from its heading to the next; the skin route is said only here, the amounts by mouth '
         'only in the paragraph before',
    'v': 'none: read the section from its heading to the next; where to find it is said only here',
    'd': 'none: read the section from its heading to the next; the amounts are said only here, and the skin route points '
         'back to them',
}
ONLY = sys.argv[1:]


def fill(key, checked, his_key, s5=None):
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
    r['section'] = 'Beach Morning Glory'
    r['reader'] = ('someone sitting with a friend whose psychedelic trip has gone bad enough that they want it over, or whose '
                   'nausea won\'t stop, deciding how to give beach morning glory and how much')
    r['checked'] = [CHECKED[c] for c in checked]
    r['placement'] = PLACE[key]
    r['opens']['why_reading'] = S[sorted([k for k in S if r['opens']['first_sentence'].startswith(k)], key=len)[-1]][0]
    r['same_point'] = SAME[key[0]]
    r['needed'] = {'reader': 'a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md and the section as first '
                             'drafted with both answers in (reads/need-draft-bmg-sec.txt)',
                   'unneeded': NEEDED_UNNEEDED, 'kept': NEEDED_KEPT}
    r['his_fixes'] = {'reader': 'a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md (with way 30) and the '
                                'section as first drafted (reads/his-draft-bmg-sec.txt)',
                      'marked': HIS_MARKED, 'kept': HIS_KEPT}
    r['fit'] = {'reader': 'a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md and the section as first drafted '
                          '(reads/fit-draft-bmg-sec.txt)', 'marked': FIT_MARKED, 'kept': FIT_KEPT}
    r['his_answer'] = HIS[his_key](s5)
    r['questions'] = dict(Q)
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


fill('f1-bmg-b173', ['p2'], 'f1b173')
fill('f1-bmg-p4p5', ['p4', 'p5'], 'none')
fill('c6-bmg-p1p3', ['p1', 'p3'], 'c6', B174_S5_JUICE)
fill('c7-bmg-p1p3', ['p1', 'p3'], 'c7', B174_S5_IT)
fill('v1-bmg-p1', ['p1v'], 'v1')
fill('d1-bmg-b173', ['p2'], 'd1')
