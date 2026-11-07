# The cards of round 14, read by build_r14.py (which defines P, T, whole, span_of, replace_words, cut_block and card).
# P('B262') is the page block of GUIDE-SO-FAR-blocks.json's B262 (the guide after round 13). The checks are in
# articles/bad-trips/humanize/h17-20261107/RESULTS.md.

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h17-20261107/'

INTRO = [
    'Round 14 (2026-11-07). Round 13 is in. Who to Contact, and When, checked part by part after the Human first half of '
    'Psychological First Aid: its opening paragraph was the strongest pull toward AI, and its integration list reads Human '
    'as it is. One card, one sentence. The first list and the directories still read AI together; I\'m working on the '
    'words around their facts next, and For the Person Helping after that. Round 12\'s card is still open on its own page.',
]

card(id='CONTACT-PLAIN', type='plain', advice='approve',
     title='The contact list\'s opening, its second sentence said plainly',
     reading=('After the Human first half, the opening as the guide has it reads [63%%](%se4a25f65-49ee-4e2a-b1f5-7f93fa965ca4), '
              'its two sentences AI Medium and High.') % H,
     tested=('With this change: [Human Written](%s3328665a-ddf4-4fbc-998c-58a8906ada02), every window Human. Changing the '
             'first sentence instead read [68%%](%s2dffa905-8bfa-43f8-9558-581e8014b770). The whole section after the Human '
             'first half goes from 60%% to [47%%](%saffe4087-5803-44e5-966c-abfecdb4b424) with it; the lists are the rest.')
            % (H, H, H),
     what=('"Hours and services change, and not every option works in every country." becomes "Their hours and services '
           'change, and some only work in one country."'),
     why=('"Not every option works in every country" is a stock hedge; saying which ones (some only work in one country) '
          'is plainer and still true of the list: Fireside and 988 are U.S.-only, and Crisis Text Line names its partner '
          'lines.'),
     stays='The first sentence (save the links and numbers before you need them) and every list below it.',
     deciding='Approve puts the new sentence in; Revise lets you change it first.',
     advice_note='Approve: one sentence, the same caveat, and the opening reads Human with it.',
     found_by='Pangram after the Human first half, one part of the section at a time',
     receipt=[HD + 'CARD-B262.receipt.json', HD + 'TEST-base-KV2.receipt.json'],
     edits=[replace_words(P('B262'), 'Hours and services change, and not every option works in every country.',
                          'Their hours and services change, and some only work in one country.')],
     spans=[span_of(P('B262'), 'Hours and services change, and not every option works in every country.')])
