# The cards of round 43, read by build_r43.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 49's pass on the first batch's Medium windows, the lesson-19b way
# (../../humanize/h57-20261119/RESULTS.md).

BUILT = '2026-11-19'
H = 'https://www.pangram.com/history/'
H57 = BLOB + 'articles/bad-trips/humanize/h57-20261119/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-14 22:08 UTC: "didn\'t understand why you gave me no cards and quit working tho"')

INTRO = [
    'Round 43 (2026-11-19). Your round-42 answer is in. This turn took the Medium and Low windows of the first batch, '
    'the way your round-41 versions showed: each paragraph checked by itself as the guide has it first, then from that '
    'near miss a word or two a reader could take two ways, checked after each change ([every check](%sRESULTS.md)).' % H57,
    'Ten paragraphs read Human High by themselves as they already stood, and seven more do now and are in: DMSO\'s side '
    'effects, niacin\'s side effects and its other forms, Get One Human Anchor\'s backup line, the ordinary-world list, '
    'Shadow Work\'s opening and the Appendix\'s list. Two of mine didn\'t move in three tries each, so they are this '
    'round\'s two cards: how you\'d say them teaches me the ones like them.',
]

card(id='TEACH-DMSO-WATER', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. DMSO beside aged ozonated-charcoal water: which to give, or both',
     reading=('By itself, as the guide has it: [Human Written, two windows Medium](%s2da90d18-b6ed-485d-8e6e-b25258a0cda0), '
              '"Sometimes DMSO works better; sometimes the water does." (9 words) and the last sentence (19 words); the '
              'rest High.' % H),
     tested=('Both semicolon pairs joined with "and", "in my experience" said once: [the same two Medium windows]'
             '(%s137ef380-fff3-4675-9d16-e7a9e92f3351).\n\n'
             '"Sometimes DMSO calms a trip better, and sometimes the charcoal water does." (what each does better, and '
             'which water): [worse, Medium over the first four sentences and Low on the last]'
             '(%s7549911f-5de2-4da7-81e2-777652365122), though the last sentence was word for word the guide\'s.'
             % (H, H)),
     sense=('Three fresh readers each time. Read alone, "It" points at nothing (in the guide it is DMSO, named in your '
            'paragraph before); "Sometimes ... sometimes" gives no way to choose; "taking both or mixing them" could mean '
            'one after the other or in one drink; and "perfect safety profile" read to one reader like a drug label, '
            'reassuring more than one person\'s experience can.'),
     why=('It is your experience, in your voice, and three small changes didn\'t move its windows (the third made them '
          'worse). How you would say which to give, and that both is fine, teaches me the other first-person remedy '
          'paragraphs still Medium.'),
     advice_note='Edit it: the paragraph in your words. Your version goes in whole.',
     list_part='',
     spans=[whole(P('B201'))])

card(id='TEACH-OPPOSITES', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='2. Dealing With Shadow Thoughts: why the opposite thought shows up',
     reading=('With the identity line before it, by itself: [Human, the last sentence Medium]'
              '(%s7d46b28c-82de-4c65-a74d-af218111b4e4) ("In the subconscious world of concepts, however, two sides are '
              'often considered together.", 13 words); the rest High.' % H),
     tested=('"In the subconscious world of concepts, however, the mind often keeps both together." (who considers them, '
             'and which two): [Medium again](%sa4b0fea1-f9bb-472b-a32c-2a383f29e503).\n\n'
             '"In the subconscious world of concepts, though, each idea often comes paired with its opposite." (what happens '
             'to a concept): [Medium again](%s8479bdd0-0087-4b23-ae89-e3d0ea85def7).' % (H, H)),
     sense=('Fresh readers: "the subconscious world of concepts" can be read several ways, and "the two sides" could be '
            'love and hate or the Hermetic opposites. One reader, in a dark moment, heard "a hated baby does not feel love" '
            'as being about their own past before it turned out to be an example, and another found the first three '
            'sentences (unweaving the identity illusion, your pamphlet, the Hermetic claim) give such a reader nothing to '
            'hold; I changed none of those, since they are your teaching and read High.'),
     why=('The last sentence is the one that says why opposite thoughts come, and it stays Medium in every wording I tried. '
          'How you would say it teaches me the other lines in the shadow part that explain the mind.'),
     advice_note=('Edit it: the last sentence, or the paragraph, in your words. If you\'d also change the sentences before '
                  'it, they are yours to.'),
     list_part='',
     spans=[whole(P('B414'))])
