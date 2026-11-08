# The cards of round 25, read by build_r25.py (which defines P, PALL, T, whole, span_of, cut_block and card). P('B330b') is
# the page block of GUIDE-SO-FAR-blocks.json's B330b (the guide after his round-24 versions and humanize/h32-20261108's
# merge and fixes). The checks are in articles/bad-trips/humanize/h32-20261108/RESULTS.md.

BUILT = '2026-11-08'
H = 'https://www.pangram.com/history/'
HD = BLOB + 'articles/bad-trips/humanize/h32-20261108/'

INTRO = [
    'Round 25 (2026-11-08). Your four versions are in as you sent them: the reminder in the first five minutes, the anchor '
    'line and your don\'ts for the person helping, your (Re)defining "Bad Trip", and your Give the Session. Your '
    '(Re)defining reads Human by itself, every window, three of them Medium ([its check](%sc192b361-98f5-4c64-bdc4-6df38dd0b62f)); '
    'the other three you checked yourself.' % H,
    'Why Bad Trips Tend to Happen is under your (Re)defining now, said once: its picture, the causes your paragraph doesn\'t '
    'name (drug interactions, sleep, cannabis, hunger, fasting, breathwork, retreat pressure and the rest) and the CBT '
    'thinking traps moved there, and its "That frame can be useful" line and the causes you already give went. The guide '
    'also no longer assumes a drug where it speaks generally: 16 lines ([the list](%sDRUG-READ.md)). Two were in your new '
    'versions, so each went in only after its check read Human: "or how hard you pushed a practice" '
    '([Human](%sf99fb1f0-34d7-4013-a3bb-95dc4b86645c)), and "think through beforehand" for "before you take anything" (your '
    'whole section, [Human, High](%s14a16456-64d6-4f7e-b4b6-0e6686fa3d9e)). A third, "once your head is clear" for '
    '"sober" in No Rash Actions\' bold line, sits in a stretch that read Mixed before, so it gets its check with that '
    'stretch.' % (HD, H, H),
    'One card is left from the merge, because it would drop a warning the fidelity check holds.',
]

card(id='WHY-LESSON-CUT', type='repeat', advice='approve', title='"Sometimes the lesson is just to ..." said once',
     what='The paragraph goes.',
     why=('Its points are all said elsewhere now: stopping the practice and the room in the first five minutes, food and sleep '
          'in your Give the Session, the people in your (Re)defining, and lowering the dose in your "make sure you\'re not '
          'jumping into the deep end all at once". It came over with the merge.'),
     stays='Everything around it; the causes before it and the thinking traps after it.',
     deciding='Approve cuts it; Reject keeps it where it is now, after the causes.',
     advice_note='Approve: it\'s the repeat you pointed at in Why Bad Trips Tend to Happen.',
     ask_because=('downside: it holds a fidelity key, warning W102 ("Sometimes the lesson is to lower the dose, stop the '
                  'practice, sleep, eat, choose safer people, and admit that the room is bad"), and only you can let a '
                  'keyed warning go'),
     found_by='the merge of Why Bad Trips Tend to Happen into your (Re)defining, and the fidelity check',
     edits=[cut_block(P('B361'))],
     spans=[whole(P('B361'))])
