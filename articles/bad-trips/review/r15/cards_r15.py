# The cards of round 15, read by build_r15.py (which defines P, T, whole, span_of, replace_words, cut_block and card).
# P('B264', 1) is the page block of GUIDE-SO-FAR-blocks.json's B264, second item (the guide after round 14). The checks are
# in articles/bad-trips/humanize/h17-20261107/RESULTS.md (the list) and h16-20261107/RESULTS.md (For the Person Helping).

BUILT = '2026-11-07'
H = 'https://www.pangram.com/history/'
H17 = 'articles/bad-trips/humanize/h17-20261107/'
H16 = 'articles/bad-trips/humanize/h16-20261107/'

INTRO = [
    'Round 15 (2026-11-07). Round 14 is in. Three cards: one line in Who to Contact\'s first list, one lead-in in For the '
    'Person Helping, and the "real grief" paragraph cut as a repeat. That cut is yours to decide rather than mine, because the '
    'safety check tracks two of its warnings (dragging someone out of grief, trapping them in a loop). Round 12\'s card is '
    'still open on its own page.',
]

card(id='CONTACT-TRIPSIT', type='plain', advice='approve',
     title='The TripSit line said as talk',
     reading=('After the Human first half of Psychological First Aid and the contact list\'s opening (round 14), the first '
              'list as the guide has it reads [65%%](%scd42656f-b28f-40af-87e9-70acb8df1bf6).') % H,
     tested=('With this change: [45%%](%s453eec39-0c0e-4e62-ac20-b4eb1aa94def), the TripSit line\'s windows Human. The '
             'Fireside line said differently instead read [67%%](%s9b81a50c-69b1-48c1-bb94-a623596a4943).') % (H, H),
     what=('"browser-based harm-reduction chat for people using drugs and the people supporting them" becomes "a '
           'harm-reduction chat you open in your browser, for people using drugs and for whoever\'s looking after them".'),
     why='The same facts (harm reduction, in the browser, for users and the people with them), said the way you\'d tell someone.',
     stays='The name and its link, and the Fireside line above it (its number, hours and "U.S.-only" exactly).',
     deciding='Approve puts the new line in; Revise lets you change it first.',
     advice_note='Approve: the same facts, and the list reads better with it.',
     found_by='Pangram after the Human first half and the contact opening, one line at a time',
     receipt=[H17 + 'CARD-TRIPSIT.receipt.json', H17 + 'TEST-base-DV1.receipt.json'],
     edits=[replace_words(P('B264', 1), 'browser-based harm-reduction chat for people using drugs and the people supporting them',
                          "a harm-reduction chat you open in your browser, for people using drugs and for whoever's looking after them")],
     spans=[span_of(P('B264', 1), 'browser-based harm-reduction chat for people using drugs and the people supporting them')])

card(id='HELPER-PHRASE', type='plain', advice='approve',
     title='The stay-present phrase, its lead-in said to the sitter',
     reading=('After the Human first half, the paragraph as the guide has it reads [60%%](%s94e4bf77-43c1-445b-b9f2-cf75d80fb451).') % H,
     tested=('With this change: [45%%](%s2410f074-0033-4869-8dac-a1949eb371d3), the phrase\'s lines Human. The phrase itself '
             'is unchanged.') % H,
     what='"A useful phrase is:" becomes "If it helps, you can say to yourself:".',
     why=('The readers flagged "A useful phrase is:" as advice-article scaffolding. Saying who says the phrase (the sitter, to '
          'themselves) is plainer and makes clear it\'s for steadying the helper.'),
     stays='"Stay present.", both phrases word for word, and their italics.',
     deciding='Approve puts the new lead-in in; Revise lets you change it first.',
     advice_note='Approve: the same phrase, and the paragraph reads better with it.',
     found_by='Pangram after the Human first half, then the tell panel (Codex, Sonnet, Haiku)',
     receipt=[H16 + 'CARD-PHRASE.receipt.json', H16 + 'TEST-base-R3-phrase.receipt.json'],
     edits=[replace_words(P('B83'), 'A useful phrase is:', 'If it helps, you can say to yourself:')],
     spans=[span_of(P('B83'), 'A useful phrase is:')])

card(id='HELPER-GRIEF-CUT', type='repeat', advice='approve',
     title='The "real grief" paragraph, said already',
     reading=('After the Human first half, the paragraph by itself reads [AI, 100%%](%s763fcc5d-16e6-42d3-be3f-47f0dd2b9a04), '
              'and all three readers flagged all three of its sentences. Rewording it read AI too (the quip cut, [100%%](%se31e6cea-2eb3-4f5a-9e7c-3dad46058085); '
              'the two don\'ts joined, [83%%](%s959f47f9-1338-4ccd-bede-0ce54ce78326)).') % (H, H, H),
     tested=('The opening without it, after the Human first half: [79%%](%s0fe50afc-728a-4281-ab3b-5d3df305842c). The opening\'s '
             'other paragraphs still read AI; this card takes out the part that only repeats.') % H,
     what='"Don\'t drag somebody out of real grief. Don\'t trap them inside a loop that is grinding them down either. Love isn\'t stubbornness." goes.',
     why=('"Don\'t drag somebody out of real grief" is the paragraph two above ("Crying, grieving, remembering, or touching a '
          'genuine wound calls for loving awareness."). Not leaving them stuck in a grinding loop is what The Fear/Panic Loop '
          'section is for. The last line is a quip. It\'s your call rather than mine because the safety check tracks two of its '
          'warnings, dragging someone out of grief and trapping them in a loop; with the cut they live in those two places.'),
     stays='The grief paragraph above it, "Stay present." and its phrase, and The Fear/Panic Loop section.',
     deciding='Approve cuts the paragraph; Reject keeps it.',
     advice_note='Approve: both points are already made where a reader needs them.',
     found_by='the say-it-once look across the guide, stopped by the fidelity check (it holds two warnings)',
     receipt=[H16 + 'TEST-base-R1-nogrief.receipt.json'],
     edits=[cut_block(P('B84'))],
     spans=[whole(P('B84'))])
