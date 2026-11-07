# The cards of round 18, read by build_r18.py (which defines P, T, whole, span_of, replace_words, cut_words, cut_block and
# card). P('B361') is the page block of GUIDE-SO-FAR-blocks.json's B361 (the guide after round 14 and the t21 and t22
# cuts); P('B368', 3) is its list's fourth item. The checks are in articles/bad-trips/humanize/h22-20261107/RESULTS.md.

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h22-20261107/'
LESSON_OLD = 'Sometimes the lesson is to lower the dose, stop the practice, sleep, eat, choose safer people, and admit that the room is bad.'
LESSON_NEW = ('Sometimes the lesson is just to lower the dose or stop the practice, get some sleep and something to eat, pick safer '
              'people, and admit that the room is bad.')
FORCE = 'They do not force music, touch, interpretation, confession, prayer, or insight.'

INTRO = [
    'Round 18 (2026-11-07). Two cards: Why Bad Trips Tend to Happen and Give the Session a Beginning and an End. Rounds 12, '
    '15, 16 and 17 are still open on their own pages.',
]

card(id='WHY-LESSON', type='plain', advice='approve',
     title='The plain lessons said the way you\'d say them',
     reading=('After the Human first half of Psychological First Aid, "Every hard experience is not a profound lesson. '
              '%s" reads [72%%](%sa27de647-4b62-44b0-85c3-c9fd47f7d44f).') % (LESSON_OLD, H),
     tested=('With this change: [41%%](%sa114b017-50de-4589-920c-fcc6cc917fff). The paragraph\'s own window reads Human; what '
             'still reads AI is the Human first half\'s opening and reminder next to it.') % H,
     what='"%s" becomes "%s"' % (LESSON_OLD, LESSON_NEW),
     why='The same six plain lessons in the same order, said in pairs the way you\'d say them instead of a run of six.',
     stays='"lower the dose", "stop the practice", "admit that the room is bad", and the first sentence word for word.',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same lessons, and the paragraph reads Human with it.',
     found_by='Pangram after the Human first half, one part of Why Bad Trips Tend to Happen at a time',
     receipt=[HD + 'CARD-LESSON.receipt.json', HD + 'TEST-base-W3b.receipt.json'],
     edits=[replace_words(P('B361'), LESSON_OLD, LESSON_NEW)],
     spans=[span_of(P('B361'), LESSON_OLD)])

card(id='SESSION-FORCE-ONCE', type='repeat', advice='approve',
     title='What the sitter doesn\'t force, said once',
     reading=('After the Human first half, Give the Session a Beginning and an End\'s list reads [67%%](%s03337b38-0f20-4ae5-9bfe-4105c06fb86b).') % H,
     tested=('Without the repeated line: [66%%](%sa0dd01b9-90e1-4b0e-87f8-f635943614b3). The list reads AI either way; this '
             'card takes out the part that only repeats.') % H,
     what=('In the list\'s Low-directivity support item, "%s" goes, and "confession" joins For the Person Helping\'s line: '
           '"Don\'t force eye contact, touch, music, prayer, chanting, interpretation, confession, or insight."') % FORCE,
     why=('For the Person Helping already says it, with more in its list (eye contact, chanting). Confession was the one thing '
          'the list here had that it didn\'t, so it moves there. It\'s your call rather than mine because the safety check '
          'tracks this line\'s "do not"; with the cut, the point lives in For the Person Helping\'s "Don\'t force ...".'),
     stays='"the sitter protects safety and offers choices" in the list, and For the Person Helping\'s line with confession added.',
     deciding='Approve makes both changes; Reject keeps both lines as they are.',
     advice_note='Approve: the point stays where a helper reads it first, and nothing in it is lost.',
     found_by='the say-it-once look across the guide, stopped by the fidelity check (the line holds a "do not")',
     receipt=[HD + 'CARD-SUPPORT.receipt.json', HD + 'CARD-FORCE.receipt.json', HD + 'TEST-base-G1x.receipt.json'],
     edits=[cut_words(P('B368', 3), FORCE), replace_words(P('B284', 2), 'interpretation, or insight.', 'interpretation, confession, or insight.')],
     spans=[span_of(P('B368', 3), FORCE), span_of(P('B284', 2), 'interpretation, or insight.')])
