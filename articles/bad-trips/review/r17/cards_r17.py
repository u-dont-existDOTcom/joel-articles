# The cards of round 17, read by build_r17.py (which defines P, T, whole, span_of, replace_words, cut_block and card).
# P('B344') is the page block of GUIDE-SO-FAR-blocks.json's B344 (the guide after round 14 and the t21 cut). The checks are
# in articles/bad-trips/humanize/h21-20261107/RESULTS.md.

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h21-20261107/'

INTRO = [
    'Round 17 (2026-11-07). One card for The Other Bypass, one sentence. Rounds 12, 15 and 16 are still open on their own pages.',
]

card(id='OTHER-PAIR', type='plain', advice='approve',
     title='The young-parts line said in one breath',
     reading=('After the Human first half of Psychological First Aid, The Other Bypass (its last paragraph already cut, since the '
              'same section says it about your marriages) reads [Mostly Human, 8%%](%s01da05e9-2597-4fce-953d-3a74d91cc162): AI only '
              'on "Most negative mind-states aren\'t philosophical errors. They are young parts ..."') % H,
     tested=('With this change: [Human Written](%sa9f2e50e-cbe8-4802-be66-90025c935622), every window Human.') % H,
     what=('"Most negative mind-states aren\'t philosophical errors. They are young parts still waiting for love, protection, '
           'permission, and an explanation nobody gave them." becomes "Most negative mind-states aren\'t some error in your '
           'philosophy, they\'re just young parts of you that are still waiting for love and protection and permission, and for '
           'the explanation nobody ever gave them."'),
     why='The same point and the same four things they wait for, said in one breath instead of a "not this. That." pair.',
     stays='Love, protection, permission, and the explanation nobody gave them; the rest of the paragraph word for word.',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same point, and the section reads Human with it.',
     found_by='Pangram after the Human first half, The Other Bypass, then its shadow-work paragraph alone',
     receipt=[HD + 'CARD-PAIR.receipt.json', HD + 'TEST-base-OTHERfix.receipt.json'],
     edits=[replace_words(P('B344'),
                          "Most negative mind-states aren't philosophical errors. They are young parts still waiting for love, protection, permission, and an explanation nobody gave them.",
                          "Most negative mind-states aren't some error in your philosophy, they're just young parts of you that are still waiting for love and protection and permission, and for the explanation nobody ever gave them.")],
     spans=[span_of(P('B344'), "Most negative mind-states aren't philosophical errors. They are young parts still waiting for love, protection, permission, and an explanation nobody gave them.")])
