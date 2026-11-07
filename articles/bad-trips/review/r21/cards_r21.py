# The cards of round 21, read by build_r21.py (which defines P, T, whole, span_of, replace_words, cut_words, cut_block and
# card). P('B325') is the page block of GUIDE-SO-FAR-blocks.json's B325 (the guide after round 14 and the t21 and t22
# cuts). The checks are in articles/bad-trips/humanize/h26-20261107/RESULTS.md.

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h26-20261107/'

INTRO = [
    'Round 21 (2026-11-07). One card: the euphoria section\'s danger list, said already in No Rash Actions right above it. '
    'Rounds 12 and 15 to 20 are still open on their own pages.',
]

card(id='AMZ-DANGER-ONCE', type='repeat', advice='approve',
     title='The euphoria danger list, said already in No Rash Actions',
     reading=('After the Human first half of Psychological First Aid, When the Trip Feels Amazing reads '
              '[64%%](%s2a4c4ead-ab91-4b56-8d68-547a3f2f64de), and its danger list by itself '
              '[51%%](%s0a74e60d-e2df-4e94-a98b-de112484f1a6).') % (H, H),
     tested=('Without the list: [59%%](%s3918fb96-95eb-44a0-b0ec-b63e8d9b4a24); the section\'s other parts still read AI. With '
             '"make a grand purchase" added, No Rash Actions\' list reads [100%%](%s9ebe7736-c21e-4f4d-8e5e-67387e046e30), as it '
             'did without it.') % (H, H),
     what=('"The danger may be action rather than panic: the 3 a.m. broadcast, confession, drive, grand purchase, sexual '
           'boundary-crossing, public prophecy, violent test of a theory, or \"I never need sleep again\" plan." goes, and '
           '"make a grand purchase" joins No Rash Actions\' list after "give away possessions".'),
     why=('No Rash Actions, the section just above, already covers it. Its list has the message and the posted revelation (the 3 '
          'a.m. broadcast and the public prophecy), confessing everything and driving, and its "No revelation makes murder, '
          'assault, coercion, sexual boundary-crossing, reckless driving, or self-harm safe tonight." covers the boundary-crossing '
          'and the violent test. The "never need sleep" plan is the first of the two questions right after ("Have I slept? Sleep '
          'comes before mission."). The grand purchase was the only thing not said there, so it moves. It\'s your call rather '
          'than mine because the safety check tracks this list\'s words ("3 a.m.", "broadcast", "prophecy", "never").'),
     stays='"The action lock matters especially when the state feels blissful ...", the two questions, the revelation after breakfast, and No Rash Actions whole.',
     deciding='Approve makes both changes; Reject keeps both lists as they are.',
     advice_note='Approve: the danger is said once, right above, and nothing in it is lost.',
     found_by='the say-it-once look across the guide, stopped by the fidelity check (the list holds W099\'s words)',
     receipt=[HD + 'CARD-PURCHASE.receipt.json', HD + 'TEST-base-AMZx.receipt.json'],
     edits=[cut_block(P('B325')), replace_words(P('B318'), 'give away possessions, call your ex', 'give away possessions, make a grand purchase, call your ex')],
     spans=[whole(P('B325')), span_of(P('B318'), 'give away possessions, call your ex')])
