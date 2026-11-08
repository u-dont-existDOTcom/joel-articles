# The cards of round 26, read by build_r26.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words and card).
# P('B280') is the page block of GUIDE-SO-FAR-blocks.json's B280 (the guide after humanize/h34-20261108's two fixes). What
# the repeats reads found, and what each finding came to, is in articles/bad-trips/humanize/h34-20261108/RESULTS.md.

BUILT = '2026-11-08'
H = 'https://www.pangram.com/history/'
H33 = BLOB + 'articles/bad-trips/humanize/h33-20261108/'
HD = BLOB + 'articles/bad-trips/humanize/h34-20261108/'

INTRO = [
    'Round 26 (2026-11-08). What carries your round-24 versions, measured one thing at a time ([the results](%sRESULTS.md)). '
    'Your Give the Session without the Kenya story, the sitter joke and the redosing aside still reads Human, High '
    '([its check](%s22506017-45a9-43c3-bcd2-ccb3c5732ed7)). Your anchor line and don\'ts without the demon line still read '
    'Human, the don\'ts at Medium ([its check](%s2a2e7aa4-5375-460b-8412-4480c5b5c3a5); the text starts with the first five '
    'minutes: that\'s the base each part is checked after, not a merge), so the demon line\'s break is what lifts them to '
    'High. My words in your frame read AI in all three tries on What Kind of Aftermath Is This?, the last written from a '
    'fresh reader\'s comparison of your Give the Session with my try ([its check](%s0ec38b6c-3395-42a6-b2ff-438096efe532), the '
    'paragraphs alone). So I stopped trying them and did what you asked first: say each thing once.' % (H33, H, H, H),
    'Two fresh readers read the stretches round 24 named against the whole guide ([What Kind of Aftermath Is '
    'This?](%sREPEATS-AFTERMATH.md), [the others](%sREPEATS-NAMED.md)). Most of what they found adds something no other '
    'line says (a remedy, a threshold, a script line), so it stays. One sentence only repeated your After the Storm lines '
    'and loses nothing, so it\'s gone: "Stabilize through sleep, food, routine, sober support, ordinary body, and ordinary '
    'world." And "Zendo-style" is explained where the guide first names it: "The Zendo Project, a harm-reduction group that '
    'offers peer support at festivals and other events to people having a hard time in an altered state, sums up its '
    'approach in four principles: ..."' % (HD, HD),
    'Two cards, each a cut with a small downside.',
]

card(id='HELPER-OPEN-CUT', type='repeat', advice='approve', title='"A good sitter is not there to ..." said once',
     what='The first sentence goes, so the section opens on the Zendo Project\'s four principles.',
     why=('Your anchor line and don\'ts under Don\'t now say three of its four points: "win a philosophy debate" is your '
          '"don\'t try to win an argument with their visions ...", "impose an interpretation" is your "While many '
          'interpretations are possible ..." and "Don\'t force ... an insight on them", and "demonstrate spiritual '
          'advancement" is your "not the witch doctor guru who knows magic spells".'),
     stays='The Zendo sentence after it, and your anchor line and don\'ts.',
     deciding='Approve cuts the sentence; Reject keeps it as the section\'s first line.',
     advice_note='Approve: it\'s the opening your new Don\'t section repeats.',
     ask_because=('downside: its fourth point, "perform a rescue fantasy" (the helper casting themselves as the hero who '
                  'saves the person), is said nowhere else in the guide'),
     found_by='a fresh reader\'s read of what this paragraph\'s reader needs, after your round-24 versions went in',
     edits=[cut_words(P('B280'), 'A good sitter is not there to win a philosophy debate, perform a rescue fantasy, impose an '
                      'interpretation, or demonstrate spiritual advancement. ')],
     spans=[span_of(P('B280'), 'A good sitter is not there to win a philosophy debate, perform a rescue fantasy, impose an '
                    'interpretation, or demonstrate spiritual advancement.')],
     receipt='articles/bad-trips/humanize/h34-20261108/HELPER-OPEN-AFTER.receipt.json')

card(id='AFT-TRAUMA-ONCE', type='repeat', advice='approve', title='What Kind of Aftermath Is This?: the trauma line said once',
     what='The "Trauma material" line goes from the list.',
     why=('Abuse Memories, Recovered Memories, and Certainty says all of it: "Return to it after sleep with a '
          'trauma-informed therapist, integration specialist, or grounded person you trust." and "Don\'t confront anybody '
          'while intoxicated or destabilized." When to bring in help is in "Bring in mental-health support when:" ("The '
          'trauma material is bigger than the room can hold.").'),
     stays='The list\'s other eight lines, and Abuse Memories as it is.',
     deciding='Approve cuts the line; Reject keeps it in the list.',
     advice_note='Approve: the fresh reader found nothing in it that Abuse Memories doesn\'t say.',
     ask_because=('downside: the list of kinds of aftermath no longer names trauma, so a reader with old trauma coming up '
                  'afterward finds it under Abuse Memories instead'),
     found_by='a fresh reader\'s repeats read of the section against the whole guide (linked in the introduction)',
     edits=[cut_block(P('B426', 6))],
     spans=[whole(P('B426', 6))])
