# The card of round 9, read by build_r09.py (which defines P, T, whole, span_of, cut_block, replace_words and card).
# P('B238') is the page block of GUIDE-SO-FAR-blocks.json's B238 (the guide after round 8). The card's new words are
# articles/bad-trips/humanize/h08-20261106/FIX-P5P6.txt (its second try), with its making-sense receipt beside it (gate
# E365) and its newcomer reads in newcomer-P5P6/. Every check is in that folder's RESULTS.md.

BUILT = '2026-11-06'
H = 'https://www.pangram.com/history/'
HUM = REPO / 'articles' / 'bad-trips' / 'humanize' / 'h08-20261106'
FIX = (HUM / 'FIX-P5P6.txt').read_text(encoding='utf-8').rstrip('\n')


def to_text(i, new):
    """Block i as the receipt's text says it would read."""
    return {'block': i, 'before': T(i), 'after': new}


INTRO = [
    'Round 9 (2026-11-06). Your round-8 version is in the guide: the fixes and the music as you wrote them, the text of '
    'your check that read [Human Written, 0%%](%s26e9138d-9b91-44e0-bb5c-7a21a7e4dddc). Your first two paragraphs stay '
    'as they were until you answer the card below.' % H,
    'Why the card had you editing only the second part: the box held all four paragraphs, but my card listed what to keep '
    'as the fixes and said I had kept your three lines as you wrote them, so the questions and the annoying-room line looked '
    'settled. They weren\'t; that pair had read AI in my check too. A card like that now gives each paragraph its own '
    'reading and says every one is yours to change.',
    'What your fix showed is now in the shared rules for every lane: where you\'ve asked for a guide\'s AI quips to go, your '
    'own lines that readers take for quips go too; the reason comes first, in plain words; and each instruction says its '
    'exact act, as "Ask if they\'d like a hand on the shoulder" does.',
    'The card is your exercise, the first part, which reads Human on its own. In place before your second part, the stretch '
    'reads AI, and so does the stretch as the guide has it now, all yours, so the stretch itself is the next work.',
]

TYPES = {
    'exercise': {'label': 'Your exercise', 'about': 'the part you left to me, fixed the way you fixed yours'},
}

card(id='ROOM-FIRST', type='exercise', advice='approve',
     title='The room\'s first part, fixed the way you fixed the second',
     reading=('Your two paragraphs as they are, [AI, 100%%](%s6fe58138-deba-4e92-a9ca-f11e83774d7a): Medium on "Then look at '
              'the room.", High on the rest.') % H,
     tested=('This version, [Human Written, 0%%](%s07e19481-bb99-4b40-932f-ab16315f4502): High on its first sentence, Medium '
             'on the next three, Low on the last. In place before your second part, the three paragraphs read '
             '[AI, 100%%, High](%s34d92f15-18c7-4849-9972-983239961bf9) in one window, and so does the stretch as the guide '
             'has it now, all yours: [AI, 100%%, High](%s54b7312f-53eb-4ee7-89d8-b3b7d5c45052).') % (H, H, H),
     what=('Your two paragraphs become one. Your annoying-room line comes first, said plainly as the reason: "A lot of what '
           'looks like a deep psychedelic crisis is a scared person in a room that\'s getting on their nerves, so look around '
           'the room next." Then the checks: two as statements, your crowd question in your words, and the body last.'),
     why=('The point came after five questions, the payoff too late, as you found in the second part. My first try kept your '
          'line word for word as the opening reason and read [AI, 100%%, High](%s8e79642a-8589-4524-a59d-e8b88cf6ff1b); said '
          'plainly, it read Human. That follows your order for this guide to remove or humanize its AI quips: three readers '
          'had called that line a quip in every panel.') % H,
     stays=('Every check: the light, the music, five concerned people, unwanted touch, somebody they don\'t trust, too hot, '
            'too cold, desperate for the bathroom.'),
     deciding=('If you\'d keep your line, Revise with it and I\'ll check that version. The last sentence reads Low: giving it '
               'a reason and an act ("can get to them as well, so sort those out") took the whole paragraph to '
               '[AI, 100%%](%sb2a7067f-443e-4caa-91c2-34a748bb9cc6), so it stays plain.') % H,
     advice_note='Approve, or Revise with your line back.',
     found_by='your round-8 comment: "an exercise for you to fix now"',
     receipt='articles/bad-trips/humanize/h08-20261106/FIX-P5P6.receipt.json',
     edits=[to_text(P('B238'), FIX), cut_block(P('B239'))],
     spans=[whole(P('B238')), whole(P('B239'))])
