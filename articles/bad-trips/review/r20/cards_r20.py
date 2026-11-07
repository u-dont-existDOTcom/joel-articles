# The cards of round 20, read by build_r20.py (which defines P, T, whole, span_of, replace_words, cut_words, cut_block and
# card). P('B409') is the page block of GUIDE-SO-FAR-blocks.json's B409 (the guide after round 14 and the t21 and t22
# cuts). The checks are in articles/bad-trips/humanize/h24-20261107/RESULTS.md.

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h24-20261107/'
TRUE_OLD = 'It may be psychologically true, symbolically true, literally true, partly true, or false in the form it first appeared.'
TRUE_NEW = 'It could be true psychologically, or symbolically, or literally, or only partly true, or false in the form it first took.'

INTRO = [
    'Round 20 (2026-11-07). One card for Abuse Memories, the last gain of the first pass through the whole guide. Rounds 12, '
    '15, 16, 17, 18 and 19 are still open on their own pages.',
]

card(id='ABUSE-TRUE', type='plain', advice='approve',
     title='True in which way, said as talk',
     reading=('After the Human first half of Psychological First Aid, Abuse Memories\' last paragraph reads '
              '[38%%](%s6cc98b14-969e-4383-963c-b74e68eb3a1f), its "%s" AI High.') % (H, TRUE_OLD),
     tested=('With this change: [18%%](%s9701ce68-7f42-484c-a964-69f4ef16cf8b). The AI High window is gone; AI Low is left on the '
             'paragraph.') % H,
     what='"%s" becomes "%s"' % (TRUE_OLD, TRUE_NEW),
     why='The same five possibilities in the same order, said with their small words instead of five matching "true"s.',
     stays='"The experience may matter deeply." and "You don\'t have to decide tonight." word for word.',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same point, and the paragraph reads less AI with it.',
     found_by='Pangram after the Human first half, one part of Abuse Memories at a time',
     receipt=[HD + 'CARD-TRUE.receipt.json', HD + 'TEST-base-A3b.receipt.json'],
     edits=[replace_words(P('B409'), TRUE_OLD, TRUE_NEW)],
     spans=[span_of(P('B409'), TRUE_OLD)])
