# The cards of round 62, read by build_r62.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 72: his round-61 answers in the guide, ZeoCharge & Ferment Human High as a
# section, and Beach Morning Glory rewritten (humanize/h80-20261127/RESULTS.md). No string here is %-formatted.

BUILT = '2026-11-27'
H = 'https://www.pangram.com/history/'
R61 = BLOB + 'articles/bad-trips/review/r61/RESULTS-R61.md'
H80 = BLOB + 'articles/bad-trips/humanize/h80-20261127/RESULTS.md'
LEFT = BLOB + 'articles/bad-trips/humanize/h80-20261127/LEFT.md'

INTRO = [
    'Round 62 (2026-11-27). Your three round-61 answers are in. Your own B155 went in whole: you had checked it [by '
    'itself](' + H + '00eb45f1-8b99-4337-929b-b4489859cf23) and [with the paragraph before it](' + H +
    '54b91410-ee03-4ebe-969b-03777505918f), both Human High in one window, and with the ozone paragraph after it, it reads '
    '[Human High in one window](' + H + 'dc4e6e82-d4cd-49cc-a0e0-14ede9962595) through the API too. Activated Charcoal is '
    'in as my version (your "a"), and from now on the warning check frees a line whose only warning word is no caution, '
    'each one named with its reason. I read your FROM-POST answer as (a), so the 5g line stays out, and the rubbing line now '
    'says "zeolite mixed in water" ([Human High by itself](' + H + 'e067e728-1f20-4c3f-bf99-96430965defd)). [Each point and '
    'where it went](' + R61 + ').',
    'With your B155 in, the whole of ZeoCharge & Ferment reads [Human High in one window](' + H +
    '7447e8b4-1a7f-46f0-bf4b-c33046e98efe), so its three short lines needed no change. Then Beach Morning Glory: as it '
    'stood it read AI ([its last two paragraphs](' + H + '55e4ae84-ccba-40f7-9156-b6a358c99a43)). Every paragraph of my '
    'rewrite reads Human High by itself or with a neighbour, and the section reads [Human](' + H +
    'e1629a55-218a-4f9a-a755-c7cdced59265), with some windows still at Medium and one at Low, which I keep working on. Two '
    'things in it only you can say are the cards below ([every check](' + H80 + '); [what is left](' + LEFT + ')).',
]

card(id='LEAF-JUICE', type='question', advice='ask',
     title='1. Beach Morning Glory: what does the juice do when it touches your skin?',
     whose='the post\'s paragraph, drafted by a model from his practice, rewritten in turn 72 (Human High with the paragraph '
           'before it)',
     question=('The handling line says even picking a leaf "can affect me" when the juice from the broken part touches '
               'sensitive skin, especially under the fingernails. A fresh reader couldn\'t tell what that effect is.\n'
               '(a) you feel the plant\'s effect, as you would from eating some (a trip starts to end); (b) a skin reaction, '
               'like a rash or a sting; or say it as you\'d say it, and it goes into that sentence.'),
     why='a sitter who picks or breaks leaves needs to know what to watch for in themselves',
     stays='the line as it reads now (highlighted), which is in the guide',
     advice_note='(a) or (b), or the effect as you\'d describe it: I can\'t tell which from your post',
     spans=[whole(P('B174'))])

card(id='NIBBLE-SIZE', type='question', advice='ask',
     title='2. Beach Morning Glory: how big is the nibble for nausea?',
     whose='the post\'s paragraph, drafted by a model from his practice, rewritten in turn 72 (Human High by itself)',
     question=('A fresh reader sitting with a friend couldn\'t judge "a tiny nibble" against the amount that ends a trip, '
               'and the paragraph says it takes only a little more than a nibble to end one, so a sitter could easily give '
               'too much.\n'
               'How big is the nibble you\'d give for nausea? Write it as you\'d say it, as something a sitter can see (a '
               'part of a leaf, say), and it goes into that sentence. Or (a): leave it as "a tiny nibble".'),
     why='the amount is yours, and a sitter who guesses too big ends the trip they meant to keep going',
     stays='the paragraph as it reads now (highlighted), which is in the guide',
     advice_note=('a size you\'d name: the whole leaf now comes first, so the reader has one amount to judge by, but not '
                  'the nibble\'s'),
     spans=[whole(P('B173'))])
