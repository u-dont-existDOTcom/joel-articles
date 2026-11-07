# The cards of round 19, read by build_r19.py (which defines P, T, whole, span_of, replace_words, cut_words, cut_block and
# card). P('B380') is the page block of GUIDE-SO-FAR-blocks.json's B380 (the guide after round 14 and the t21 and t22
# cuts). The checks are in articles/bad-trips/humanize/h23-20261107/RESULTS.md.

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h23-20261107/'
MISS_OLD = 'Missing is contraction: hunger, ache, self-reference, and the painful fantasy that love means needing the person to return.'
MISS_NEW = ("Missing someone is a contraction. There's hunger and ache in it, it keeps circling back to you, and there's the painful "
            "fantasy that loving them means needing them to come back.")
SIG_OLD = 'The point is not to manufacture loving thoughts. Give the body one simple signal: love is here.'
SIG_NEW = "There's no need to manufacture loving thoughts, you're just giving the body one simple signal: love is here."
TRAIN_OLD = ('Train before the emergency: send love to a frightening image, a hated person without approving what they did, your '
             'shame, your body, sickness, aging, fear, death, and the inner child.')
TRAIN_NEW = ('So train before you need it, sending love to a frightening image, to someone you hate (without approving of what they '
             'did), to your shame and your body, to sickness and aging and fear and death, and to the inner child.')

INTRO = [
    'Round 19 (2026-11-07). Four cards: Dealing With Sorrow, Hand on Heart and Demons. Rounds 12, 15, 16, 17 and 18 are still '
    'open on their own pages.',
]

card(id='SORROW-MISSING', type='plain', advice='approve',
     title='What missing is, said as its point and then its parts',
     reading=('After the Human first half of Psychological First Aid, the paragraph from "%s" to "The difference is enormous." reads '
              '[47%%](%sd9c97d81-0969-44b3-995c-bfcc836e9c8d), its first sentence AI High.') % (MISS_OLD, H),
     tested=('With this change: [21%%](%s1b525a1e-07b3-42ae-9129-1d287c0eed8b). Every window of the paragraph reads Human; what still '
             'reads AI is the Human first half\'s opening sentence.') % H,
     what='"%s" becomes "%s"' % (MISS_OLD, MISS_NEW),
     why=('The same four things, said as the point first and then what it\'s made of. "Self-reference" becomes "it keeps circling '
          'back to you". Your "Missing is contraction" becomes "Missing someone is a contraction"; if you\'d rather keep your '
          'phrase, Revise.'),
     stays='"Sending love is different.", "Love can bless without grabbing." and "The difference is enormous." word for word.',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same point, and the paragraph reads Human with it.',
     found_by='Pangram after the Human first half, one part of Dealing With Sorrow at a time',
     receipt=[HD + 'CARD-MISSING.receipt.json', HD + 'TEST-base-S2b.receipt.json'],
     edits=[replace_words(P('B380'), MISS_OLD, MISS_NEW)],
     spans=[span_of(P('B380'), MISS_OLD)])

card(id='HAND-SIGNAL', type='plain', advice='approve',
     title='The hand on the heart: a signal, said in one breath',
     reading=('After the Human first half, the opening paragraph of Hand on Heart and Gratitude reads [44%%](%s46f93e63-6a3b-4113-a972-721cfdff1d35).') % H,
     tested=('With this change: [22%%](%s098d0d20-13aa-4ad5-bf5e-bc4cb6a2f255). Every window of the paragraph reads Human; what still '
             'reads AI is the Human first half\'s opening sentence.') % H,
     what='"%s" becomes "%s"' % (SIG_OLD, SIG_NEW),
     why='The same point, no forced loving thoughts and one simple signal, said in one sentence instead of a "not this. Do that." pair.',
     stays='The first sentence and "love is here" word for word.',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same point, and the paragraph reads Human with it.',
     found_by='Pangram after the Human first half, one part of Hand on Heart at a time',
     receipt=[HD + 'CARD-SIGNAL.receipt.json', HD + 'TEST-base-H1b.receipt.json'],
     edits=[replace_words(P('B386'), SIG_OLD, SIG_NEW)],
     spans=[span_of(P('B386'), SIG_OLD)])

card(id='DEMON-TRAIN', type='plain', advice='approve',
     title='Train before you need it: the list said in pairs',
     reading=('After the Human first half, the demons section\'s "Love is a better move" paragraph reads '
              '[37%%](%s3326e141-9b6d-41a3-b447-fca507f1ec46), AI only on "Train before the emergency: ..."') % H,
     tested=('With this change: [19%%](%sb722b1c6-0655-41c5-90f0-44ca00eac656). Every window of the paragraph reads Human.') % H,
     what='"%s" becomes "%s"' % (TRAIN_OLD, TRAIN_NEW),
     why='The same nine things to send love to, in the same order, said in pairs with their small words instead of a colon and a run.',
     stays='"Love is a better move ...", "Almost nobody can authentically love ...", and "Practice being the space rather than the storm."',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same practice, and the paragraph reads Human with it.',
     found_by='Pangram after the Human first half, one part of Demons, Jinn, Entities at a time',
     receipt=[HD + 'CARD-TRAIN.receipt.json', HD + 'TEST-base-DCb.receipt.json'],
     edits=[replace_words(P('B400'), TRAIN_OLD, TRAIN_NEW)],
     spans=[span_of(P('B400'), TRAIN_OLD)])

card(id='DEMON-SAFETY-ONCE', type='safety', advice='approve',
     title='The entity safety rule, already in No Rash Actions',
     reading=('After the Human first half, the "Safety rule" and its two sentences read [AI, 100%%](%sd0780839-89bc-4170-8d81-03560c37af1a).') % H,
     tested=('Not a wording change: the card takes out a repeat. The section then ends on stabilize first, which reads '
             '[Human Written](%sc8a28685-11ef-431e-8b64-68eb96089247) after the Human first half.') % H,
     what=('The "Safety rule" label and "Even a completely real-feeling entity does not make decisions for your body. No entity may '
           'tell you to hurt yourself or another person, drive, jump, flee, accuse somebody, cross a sexual boundary, or make a life '
           'decision tonight." go.'),
     why=('No Rash Actions: Visions Are Not Commands already says this for anything a trip shows you, entities included. Its don\'ts '
          'cover driving, accusing and life decisions, and it says "No revelation makes murder, assault, coercion, sexual '
          'boundary-crossing, reckless driving, or self-harm safe tonight." Jumping falls under self-harm there, and leaving is in '
          'Psychological First Aid ("if they want to leave, have someone go with them"). Reject if you want the rule repeated right '
          'where a frightened reader meets an entity.'),
     stays='No Rash Actions whole, and the demons section\'s last paragraph (stabilize first).',
     deciding='Approve cuts the label and its two sentences; Reject keeps them.',
     advice_note='Approve: the rule lives where the guide sets out what not to act on.',
     found_by='the say-it-once look across the guide',
     receipt=[HD + 'TEST-base-DF.receipt.json'],
     edits=[cut_block(P('B402')), cut_block(P('B403'))],
     spans=[whole(P('B402')), whole(P('B403'))])
