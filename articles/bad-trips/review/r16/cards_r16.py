# The cards of round 16, read by build_r16.py (which defines P, T, whole, span_of, replace_words, cut_block and card).
# P('B317') is the page block of GUIDE-SO-FAR-blocks.json's B317 (the guide after round 14). The checks are in
# articles/bad-trips/humanize/h19-20261107/RESULTS.md.

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h19-20261107/'

INTRO = [
    'Round 16 (2026-11-07). Two cards for No Rash Actions, each one line. Rounds 12 and 15 are still open on their own pages.',
]

card(id='NRA-WRITE', type='plain', advice='approve',
     title='Write it down, sleep, look again: one sentence instead of three',
     reading=('After the Human first half of Psychological First Aid, "Write it down. Protect sleep. Revisit it sober with one '
              'grounded person." reads [59%%](%s47f6a611-74f9-442e-ac5c-662ce2bfa8f8).') % H,
     tested=('With this change: [Human Written](%s795e7185-2001-4eb5-ae47-9e7c0deb0dd9), every window Human. Changing only the '
             'last sentence read [100%%](%s72c11a90-eb11-4ee5-ab6f-9e501f8c1f34): it was the clipped three-beat rhythm.') % (H, H),
     what=('"Write it down. Protect sleep. Revisit it sober with one grounded person." becomes "Write it down, get some sleep, '
           'and go back over it sober with one grounded person." It stays bold.'),
     why='The same three steps in the same order, said as one sentence the way you\'d say it.',
     stays='Writing it down, sleep, sober, one grounded person.',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same steps, and it reads Human.',
     found_by='Pangram after the Human first half, one paragraph of No Rash Actions at a time',
     receipt=[HD + 'CARD-WRITE.receipt.json', HD + 'TEST-base-N3a.receipt.json'],
     edits=[{'block': P('B319'), 'before': T(P('B319')),
             'after': 'Write it down, get some sleep, and go back over it sober with one grounded person.'}],
     spans=[whole(P('B319'))])

card(id='NRA-LOCK', type='plain', advice='approve',
     title='The action lock said as something you do',
     reading=('After the Human first half, the lock with its list of don\'ts reads [AI, 100%%](%s173cdc51-97bf-4765-ba5a-87b141a65ca8).') % H,
     tested=('With this change: [76%%](%s0c651fc6-530f-4429-9918-0e98a3e817ac), the first half Human again. "Give it 24–72 hours '
             'before you act on anything." read about the same ([73%%](%s424017ee-a823-4d47-bff5-fa5903d0f8c0)) but drops the '
             'name "action lock", which When the Trip Feels Amazing refers back to. The list of don\'ts said as chained sentences '
             'read [100%%](%s5b3f9722-7d9b-4386-b4e7-a8c633fa0e3c), so the list stays.') % (H, H, H),
     what='"Use a 24–72 hour action lock." becomes "Put yourself on a 24–72 hour action lock." It stays bold.',
     why='The same rule and the same 24–72 hours, said as something the reader does rather than a tool to use.',
     stays='"24–72", the name "action lock", and the list of don\'ts word for word.',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same rule, and the paragraph reads less AI with it.',
     found_by='Pangram after the Human first half, one paragraph of No Rash Actions at a time',
     receipt=[HD + 'CARD-LOCK.receipt.json', HD + 'TEST-base-N2c.receipt.json'],
     edits=[{'block': P('B317'), 'before': T(P('B317')), 'after': 'Put yourself on a 24–72 hour action lock.'}],
     spans=[whole(P('B317'))])
