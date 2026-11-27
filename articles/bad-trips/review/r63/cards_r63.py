# The cards of round 63, read by build_r63.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 73: his round-62 LEAF-JUICE answer in B174 (Human High 122 with B171), his
# NIBBLE-SIZE amounts tried in B173 in six steps (humanize/h81-20261127/RESULTS.md). No string here is %-formatted.

BUILT = '2026-11-27'
H = 'https://www.pangram.com/history/'
R62 = BLOB + 'articles/bad-trips/review/r62/RESULTS-R62.md'
H81 = BLOB + 'articles/bad-trips/humanize/h81-20261127/RESULTS.md'
LEFT = BLOB + 'articles/bad-trips/humanize/h81-20261127/LEFT.md'

ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-14 22:08 UTC: "didn\'t understand why you gave me no cards and quit working tho"')

INTRO = [
    'Round 63 (2026-11-27). Your LEAF-JUICE answer is in the handling paragraph, put in one piece at a time and checked '
    'after each: "relax" for "affect", then the juice working through the skin almost as well as eating the leaf, then '
    'your armpits, "for example" kept. With the paragraph before it, it reads [Human High in one window](' + H +
    '6026d11b-3fe2-4dc8-b6dc-da84f960f053). [Each point and where it went](' + R62 + ').',
    'Your NIBBLE-SIZE amounts went into the amounts paragraph the same way, and every step reads Human, but one sentence '
    'in it stays at Medium in a window of its own, and the paragraph has used its six tries. So it comes to you with my '
    'best try, for your version (the second card). The first asks the one amount the skin route still lacks ([every '
    'check](' + H81 +
    '); [what is left](' + LEFT + ')).',
]

card(id='TEACH-B173', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='2. Beach Morning Glory: the amounts paragraph, with your amounts in',
     reading=('As the guide has it now, without your amounts, by itself: [Human High in one window](' + H +
              '6bc70ed9-07ac-4541-8f72-68f9ab8c5e2a).'),
     tested=('My best try with all of your answer in: "Eating a whole leaf can easily end the trip and, in my experience, '
             'may keep you from tripping for days afterward. A tiny nibble can sometimes smooth psychedelic nausea and even '
             'improve the trip without ending it. For nausea I\'d try 200mg of leaf at a time, or 10mg of the extract '
             'paste. I\'d give more than that only if the person doesn\'t mind their trip getting less intense. But it '
             'takes only a little more than a nibble to end the trip, so I use it for nausea only when the person is okay '
             'with their trip possibly ending." It reads High, Medium 16, High ([check](' + H +
             '5772af1d-708e-42f6-90a6-5126b6148ad9)): the Medium is the nibble sentence, in a window of its own.\n\n'
             'Your amounts in, as a sentence of their own: High, Medium 16 on the nibble sentence, High ([check](' + H +
             'ddea8d92-30a7-4ecc-9c27-92b2fcaddfee)).\n\n'
             'Your "more" added as its own sentence: the same, High, Medium 16, High ([check](' + H +
             '10d2a2a5-4b40-4e70-be85-78168a936f31)).\n\n'
             '"A tiny nibble, though, can ...": the first two sentences went into one window, Low 37 ([check](' + H +
             'b771d740-e2d4-4d0d-90b0-b12e30a8ccc5)).\n\n'
             '"Eating a whole leaf", which a fresh reader asked for (how the leaf is taken): the check above.'),
     sense=('Fresh readers of my first draft with your amounts in asked how to measure 200mg of leaf or 10mg of paste '
            'without a scale, and where the line is between easing nausea and ending the trip ("only a little more than a '
            'nibble"). The guide doesn\'t say anywhere what the extract paste is.'),
     why=('With your amounts in, every step reads Human, but the nibble sentence sits apart at Medium, and the paragraph '
          'has used its six tries. How you would say the paragraph with your amounts teaches me how to say a sentence that '
          'Pangram keeps setting apart from the ones around it.'),
     advice_note=('Edit it: the paragraph in your words, with your amounts. "A tiny nibble can sometimes smooth psychedelic '
                  'nausea and even improve the trip without ending it." is the sentence that reads Medium. If there is a '
                  'way to judge 200mg without a scale, or a word on what the extract paste is, saying it here helps a '
                  'sitter too.'),
     spans=[whole(P('B173'))])

card(id='SKIN-AMOUNT', type='question', advice='ask',
     title='1. Beach Morning Glory: how much juice on the skin?',
     whose='his round-62 answer, in the handling paragraph since turn 73 (Human High 122 with the paragraph before it)',
     question=('The handling paragraph now says the juice "works through the skin almost as well as eating the leaf does, '
               'so to give it on purpose, you can put the juice under the armpits, for example." A fresh reader couldn\'t '
               'tell how much juice to put there, and since it works almost as well as eating, too much could end the '
               'trip.\n'
               'How much would you use, the juice of how much leaf, say? Write it as you\'d say it, and it goes into that '
               'sentence. Or (a): leave it as it is.'),
     why='a sitter giving it through the skin needs a starting amount as much as one giving it to eat',
     stays='the paragraph as it reads now (highlighted), which is in the guide',
     advice_note='an amount you\'d name: I can\'t work it out from the amounts for eating, since the skin takes it in a bit less',
     spans=[whole(P('B174'))])
