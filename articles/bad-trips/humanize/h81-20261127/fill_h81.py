#!/usr/bin/env python3
"""fill_h81.py - the making-sense receipts of turn 73's steps (his round-62 answers into B174 and B173), from the three fresh
reads of the section as first drafted with both answers in (reads/need-, his-, fit-final-bmg-sec.txt; the draft they saw is
in reads/prompt-*-final-bmg-sec.txt). Run from this folder after `sense_receipt.py make`, then `sense_receipt.py check`.

  python3 fill_h81.py [KEY...]
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ANS = 'review/r62/ANSWERS-R62-20261127-1716.json'

S = {  # every sentence of the steps: payoff (what the reader does with it), follows, and its tie at the start
    'In my experience, beach morning glory is the ultimate sledgehammer': (
        'they know what it is for: ending a psychedelic trip fast, when the trip has to stop',
        'the heading, Beach Morning Glory, under Need to Stop the Trip?', None),
    'By beach morning glory I mean': (
        'they get the one species, don\'t swap in a garden morning glory or another relative, and know they likely can\'t '
        'buy it from just any seller', 'the plant just named by its common name', 'By beach morning glory'),
    'The leaf is strong enough that even picking one': (
        'they keep the juice from the broken end off their own skin and from under their nails while they handle a leaf',
        'which plant, said before: how strong its leaf is, even its juice on the skin', 'The leaf is strong enough'),
    'Its juice works through the skin almost as well as eating it does.': (
        'they know the juice on skin acts almost as much as eating the leaf, so skin contact counts as a dose',
        'the juice on his skin, just said: how much it does there', 'Its juice'),
    'Its juice works through the skin almost as well as eating the leaf does.': (
        'they know the juice on skin acts almost as much as eating the leaf, so skin contact counts as a dose',
        'the juice on his skin, just said: how much it does there', 'Its juice'),
    'Its juice works through the skin almost as well as eating the leaf does, so': (
        'they have a second way to give it on purpose, the juice on the skin (under the armpits, for example), since it '
        'works there almost as well as eating the leaf', 'the juice on his skin, just said: how much it does there, and how '
        'to use that', 'Its juice'),
    'Eating a whole leaf can easily end the trip': (
        'they know eating a whole leaf is what ends a trip and may keep their friend from tripping for days, so they give a '
        'whole leaf only when the trip has to end', 'handling the leaf and its juice, said before: what eating it does, by '
        'how much', None),
    'A whole leaf can easily end the trip': (
        'they know a whole leaf is the amount that ends a trip and may keep their friend from tripping for days, so they '
        'give a whole leaf only when the trip has to end', 'handling the leaf, said before: how much of it does what', None),
    'A tiny nibble, though, can sometimes smooth': (
        'they know a small piece has another use, for nausea, that can leave the trip going',
        'the whole leaf, the large amount, just said', 'A tiny nibble, though'),
    'A tiny nibble can sometimes smooth': (
        'they know a small piece has another use, for nausea, that can leave the trip going',
        'the whole leaf, the large amount', 'A tiny nibble'),
    "For nausea I'd try 200mg of leaf at a time": (
        'they know how much to start with for nausea: 200mg of leaf at a time, or 10mg of the extract paste',
        'the nibble for nausea, just said: how big a nibble is', 'For nausea'),
    "I'd give more than that only if": (
        'they go past those amounts only for someone who doesn\'t mind their trip getting less intense',
        'the amounts just given: when to go past them', "I'd give more than that"),
    'But it takes only a little more than a nibble': (
        'they give it for nausea only to someone who has said they are fine with the trip ending',
        'the amounts, just given: how close they are to the amount that ends the trip', 'But it takes only a little more'),
}
CHECKED = {
    'p1': {'point': 'beach morning glory is Ipomoea pes-caprae, not morning glories in general; the relatives and cousins he '
                    'tried did not work the same way; as far as he knows nobody else sells it; in his experience it stops a '
                    'psychedelic trip cold and fast',
           'found': 'his post as of 2026-11-03, B171 and B172; B171 as it read Human High 56 (ecce6d40), unchanged',
           'still_needed': 'yes: they get the right plant and use it when a trip has to end', 'fate': 'kept'},
    'p3': {'point': 'picking a leaf can relax him when the juice from the broken part touches sensitive skin, especially under '
                    'the fingernails, so he keeps his skin away from the broken end; the juice works through the skin almost '
                    'as well as eating it; to give it on purpose, the juice can go under the armpits, for example',
           'found': 'his post as of 2026-11-03, B174; his round-62 answer (%s, card LEAF-JUICE): "touching the juice is '
                    'relaxing, especially on sensitive skin, it absorbs almost as well as eating it. can put it under armpits '
                    'for example to absorb well"' % ANS,
           'still_needed': 'yes: they keep the juice off their own skin, and can give it through the skin on purpose',
           'fate': 'changed'},
    'p2': {'point': 'a whole leaf can easily end the trip and may prevent tripping for days afterward; a tiny nibble can '
                    'smooth nausea and improve the trip without ending it; for nausea he would try 200mg of leaf at a time, or '
                    '10mg of the extract paste, and more only if the person doesn\'t mind the trip getting less intense; the '
                    'gap to a trip-ending amount is narrow, so he uses it for nausea only when the person is okay with the '
                    'trip ending',
           'found': 'his post as of 2026-11-03, B175 and B173; his round-62 answer (%s, card NIBBLE-SIZE): "i\'d try 10mg at '
                    'a time for nausea of the extract paste, or 200mg leaf at a time (more if they don\'t mind reducing trip '
                    'intensity)"' % ANS,
           'still_needed': 'yes: they know how much to start with for nausea and when to give more', 'fate': 'changed'},
}

# the draft the reads saw, sentence by sentence (the reads number them S1 to S12)
DRAFT = {}
for line in (HERE / 'reads' / 'prompt-his-final-bmg-sec.txt').read_text(encoding='utf-8').splitlines():
    m = re.match(r'^(S\d+): (.*)$', line)
    if m:
        DRAFT[m.group(1)] = m.group(2).strip()
assert DRAFT['S5'].startswith('A whole leaf') and DRAFT['S10'].startswith('I was rushing'), DRAFT

NEEDED_UNNEEDED = [DRAFT['S8'], 'though as far as I know nobody else sells it']
NEEDED_KEPT = {
    'though as far as I know nobody else sells it': (
        'they know they likely can\'t buy it from just any seller, so they look for the one source or plan without it; '
        'his fact from his post, in B171 as it read Human High 56 (ecce6d40)'),
}
HIS_MARKED = [{'s': DRAFT[k], 'difference': d} for k, d in (
    ('S3', '1, 4, 12: packs the juice, the skin, the fingernails and the absorbing into one sentence; "relax me" vague'),
    ('S4', '10, 16: "stops that" could be the relaxing or the absorbing; "absorbs well" repeats S3'),
    ('S5', '4, 12: "a whole leaf" gives no amount though S6 gives mg; no tie to the skin point'),
    ('S6', '1, 4, 10: packs the nibble, two amounts and the effect into one; "it" could be the nibble or the paste'),
    ('S7', '4, 10, 16: "a little more than a nibble" gives no amount; "give more" doesn\'t say more than what; the ending '
           'condition said twice'))]
HIS_KEPT = {
    DRAFT['S5']: ('the paragraph\'s first sentence, as it read Human High 67 by itself (6bc70ed9): "a whole leaf" is the amount '
                  'a sitter holds, and his amounts in mg come two sentences on; it opens a new step (how much does what), so '
                  'it needs no tie to the handling paragraph'),
    DRAFT['S7']: ('not in these texts as the reads saw it: "give more" now has its own sentence, "I\'d give more than that", '
                  'and the trip ending is said once; "only a little more than a nibble" stays, his words for how narrow the '
                  'margin is, with his amounts right before it'),
}
FIT_MARKED = [{'s': DRAFT[k], 'found': f} for k, f in (
    ('S4', 'CAN\'T TELL: no amount of juice or number of leaves for the armpits'),
    ('S6', 'CAN\'T TELL: no scale for 200mg of leaf or 10mg of paste; "tiny nibble" vague'),
    ('S7', 'CAN\'T TELL: "only a little more than a nibble" doesn\'t say where the line is'),
    ('S10', 'CAN\'T TELL: no amount for what she got'))]
FIT_KEPT = {
    DRAFT['S4']: ('he gave no amount for the skin route (LEAF-JUICE), and the amount is not mine to make up: it goes to him in '
                  'the next round (OWNER-QUESTIONS.md); the sentence now says the skin is one way to give it, "for example", '
                  'as he did'),
    DRAFT['S6']: ('his amounts are his answer to NIBBLE-SIZE, which asked for a size a sitter can see; he gave mg, so mg it is, '
                  'next to "a tiny nibble", what a sitter reaches for'),
    DRAFT['S7']: ('the line between easing nausea and ending the trip is narrow, which is what the sentence tells the reader; '
                  'his amounts, just before it, say where to start'),
    DRAFT['S10']: ('not in these texts: B176, his story as it read Human High 86 with B178 (2dfaa7bb), gives no amount because '
                   'his story has none'),
}
Q = {
    'Q1': 'PASS: each sentence opens on what it is about (the sledgehammer, which plant, the leaf\'s strength, its juice, the '
          'whole leaf, the nibble, the amounts for nausea, going past them, how close the end is)',
    'Q2': 'PASS: what he does is said as what he does ("I keep my skin away", "I\'d try 200mg", "I\'d give more than that '
          'only if", "I use it for nausea only when"), and the skin route as what the reader can do ("you can put the juice '
          'under the armpits")',
    'Q3': 'PASS: the broken end, sensitive skin under the fingernails, the armpits, 200mg of leaf at a time, 10mg of the '
          'extract paste',
    'Q4': 'PASS: "relax" is his word for what the juice does; "works through the skin" says what absorbing does for the '
          'reader; "aborts" not used here',
    'Q5': 'PASS: each tie is at the start ("By beach morning glory", "The leaf is strong enough", "Its juice", "A tiny '
          'nibble", "For nausea", "I\'d give more than that", "But it takes only a little more")',
    'Q6': 'PASS: which plant, handling the leaf and its juice on the skin, then how much does what, the amounts after the '
          'nibble they size',
    'Q7': 'PASS: each fact is something a sitter acts on: what to avoid, how else to give it, how much to start with, when '
          'not to go on',
    'Q8': 'PASS: no group of items left',
    'Q9': 'PASS: the draft\'s two packed sentences are split; each step adds one piece of his answer',
}
PLACE = {
    'c2-bmg-p1p3': 'B171 and the handling paragraph after it (B174), checked together as they read Human High 92 '
                   '(bb2893ad); step 1 of his LEAF-JUICE answer, his word for what the juice does ("relax")',
    'c3-bmg-p1p3': 'B171 and the handling paragraph (B174); step 2 of his LEAF-JUICE answer, that the juice works through the '
                   'skin almost as well as eating it, in a sentence of its own',
    'c4-bmg-p1p3': 'B171 and the handling paragraph (B174); step 2 again, "eating it" made "eating the leaf", since "it" could '
                   'be the juice or the leaf (step 2 read Medium 13 on that sentence, 5884722d)',
    'c5-bmg-p1p3': 'B171 and the handling paragraph (B174); step 3 of his LEAF-JUICE answer, his armpits as one way to give it '
                   'on purpose',
    'a3-bmg-p2': 'Beach Morning Glory\'s amounts paragraph (B173, with B175\'s whole leaf at its start), checked by itself as it '
                 'read Human High 67 (6bc70ed9); step 1 of his NIBBLE-SIZE answer, his two amounts after the nibble',
    'a4-bmg-p2': 'the amounts paragraph (B173); step 2 of his NIBBLE-SIZE answer, his "more", only for someone who doesn\'t '
                 'mind the trip getting less intense',
    'a6-bmg-p2': 'the amounts paragraph (B173) with both pieces of his NIBBLE-SIZE answer; "though" out again (it joined the '
                 'first two sentences into one window that read Low 37, b771d740), and the whole-leaf sentence says how the '
                 'leaf is taken, "Eating a whole leaf", as the his-fixes read asked',
    'a5-bmg-p2': 'the amounts paragraph (B173) with both pieces of his NIBBLE-SIZE answer; the nibble sentence, Medium 16 in '
                 'steps 1 and 2 (ddea8d92, 10d2a2a5), built differently from the sentence before it: "though" after its '
                 'subject',
}
SAME = {
    'c': 'none: read the section from its heading to the next; the juice on the skin is said only here, the amounts only in '
         'the paragraph after',
    'a': 'none: read the section from its heading to the next; the amounts are said only here, the skin route only in the '
         'handling paragraph before it',
}

ONLY = sys.argv[1:]


def fill(key, checked):
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
                             'drafted with both answers in (reads/need-final-bmg-sec.txt)',
                   'unneeded': NEEDED_UNNEEDED, 'kept': NEEDED_KEPT}
    r['his_fixes'] = {'reader': 'a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md and the section as first '
                                'drafted (reads/his-final-bmg-sec.txt); its marked sentences of that draft are rewritten as '
                                'these steps, but S5, kept',
                      'marked': HIS_MARKED, 'kept': HIS_KEPT}
    r['fit'] = {'reader': 'a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md and the section as first drafted '
                          '(reads/fit-final-bmg-sec.txt)', 'marked': FIT_MARKED, 'kept': FIT_KEPT}
    r['questions'] = dict(Q)
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


for k in ('c2-bmg-p1p3', 'c3-bmg-p1p3', 'c4-bmg-p1p3', 'c5-bmg-p1p3'):
    fill(k, ['p1', 'p3'])
for k in ('a3-bmg-p2', 'a4-bmg-p2', 'a5-bmg-p2', 'a6-bmg-p2'):
    fill(k, ['p2'])
