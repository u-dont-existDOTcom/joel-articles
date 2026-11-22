# The cards of round 32, read by build_r32.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). Round 32 is his next step after the contents (HELPER-NOW, 2026-11-09 17:22 UTC: "make
# sure the ToC is optimized then we can make sure the stuff in each section is what belongs there"): three fresh readers
# read the guide section by section (../../humanize/h40-20261109/section-read/), the five moves that keep the meaning went
# in without a card (../../humanize/h40-20261109/fix_sections.py), and ../../humanize/h40-20261109/RESULTS.md has every
# proposal's fate.

BUILT = '2026-11-09'
NB = ' '
IND = NB * 4
H40 = BLOB + 'articles/bad-trips/humanize/h40-20261109/'

INTRO = [
    'Round 32 (2026-11-09). Round 31 is in: your Alone at 3 a.m. version as you wrote it, with the solar plexus (the '
    'Grounding Menu\'s "one on the belly or solar plexus" now says only the solar plexus too, since it was the same '
    'error), the breath line, the training sentence in your preparation, and paranoia and derealization staying where they '
    'are.',
    'Then your next step after the contents: whether what\'s in each section belongs there. Three fresh readers read the '
    'guide section by section and proposed 18 changes ([each one, and what I did with it](%sRESULTS.md)). Five only move '
    'whole paragraphs, word for word, to where they belong, so I made them ([the moves](%sfix_sections.py)): the bridge '
    'into tripsitting ("Once the body is stable and those tools have done what they can ...") is back at the end of the '
    'remedies, since round 30\'s contents had left it above them; in Active Seizure, when to call medics comes right after '
    'the rescue medicine; in Zeolite, how you take it comes before how you prepare it; the Movement evidence note sits in '
    'Stillness or Movement?, with the movement lines it was written for; and in After the Storm, "No "another ceremony '
    'will fix this" reflex." and the three paragraphs after it join the opening paragraph, since they\'re for everyone '
    'after a hard trip, so the aftermath list leads straight into Bring in mental-health support when:. Say if you want '
    'any of them back.' % (H40, H40),
    'Four cards: two questions, each with its options as they\'d read, and two moves in the Grounding Menu that change '
    'where a reader starts. Ten proposals I\'d leave, mostly because they\'d move or cut what you wrote where you put it: '
    'your round-27 first five minutes, the hierarchy sentence you approved putting back that round, and your "But more '
    'likely" turn.',
]

SEIZE_A = 'What Else May Help: At the Aura, and Alongside Rescue Medicine'
SEIZE_B = 'What Else May Help: Magnesium, CBD, THC and DMSO'

card(id='SEIZE-HEAD', type='structure', advice='ask', title='1. Active Seizure: a heading where the extras start?',
     question=('Active Seizure now opens with first aid, the rescue medicine and when to call medics (that line moved up; '
               'see the top of the page). Six paragraphs follow on what else may help: the aura, magnesium with DMSO and '
               'CBD, the ABRACE spray, the forums, the CBD gel trial, and DMSO in rats. Nothing marks where the '
               'essentials stop. How each option would read:\n\n'
               'A (my pick):\n'
               '%s... or a seizure substantially different from the person\'s known pattern.\n'
               '%s### %s\n'
               '%sSome people get a warning before a seizure takes hold, which is called an aura. ...\n'
               'Pro: someone with a seizing friend sees that what they need is above it, and the heading says when the '
               'rest applies, with "alongside any rescue medicine" from the magnesium paragraph. Con: it names none of the '
               'remedies, so someone scanning the headings for CBD has to read on to find it.\n\n'
               'B: the same place, "### %s". Pro: someone scanning the headings for CBD or DMSO finds them. Con: it '
               'leaves out the aura, which the first paragraph under it is about.\n\n'
               'C: no heading. Pro: nothing added, and the essentials come first now anyway. Con: the six paragraphs run '
               'on from the first aid with nothing to say they\'re extras.') % (IND, IND, SEIZE_A, IND, SEIZE_B),
     why=('A fresh reader, reading each section for what belongs under its heading: "the reader has to dig out the '
          'first-aid steps from the research tour." Moving the call-medics line up did most of that; a heading would do '
          'the rest, and it\'s new words, so it comes to you.'),
     stays='The section as it is now, with when to call medics right after the rescue medicine.',
     advice_note='A, and I\'m fairly sure a heading helps; less sure of its wording, so write yours if neither fits.',
     spans=[whole(P('N-WARN'))], card_after=P('B112'))

card(id='GROUND-ORDER', type='structure', advice='approve', title='2. Grounding Menu: the room-first order at its top',
     what=('"A useful order is room → body → human → time → meaning. ..." moves from the end of Stillness or Movement? '
           'to the Grounding Menu, after "Grounding is love becoming practical. Choose one or two options rather than all '
           'of them. ...". No words change.'),
     why=('The order lists the menu\'s own kinds (room, body, human, time), and someone who goes to the Grounding Menu '
          'from the contents misses it where it is now. After "Choose one or two options", it reads as where to start, '
          'not as five things to do.'),
     stays=('Every line of both sections, word for word. Stillness or Movement? then ends on parallel processing and the '
            'Movement evidence note.'),
     deciding='Approve moves it; Revise if you\'d cut one of the two "love ... practical" sentences; Reject leaves it where it is.',
     advice_note=('Approve, and I\'m sure it belongs with the menu. The cost is the repeat: "love becomes practical first" '
                  'comes three sentences after "Grounding is love becoming practical."'),
     ask_because=('downside: "When the nervous system is on fire, love becomes practical first." comes three sentences after '
                  '"Grounding is love becoming practical.", so the menu\'s opening says it twice'),
     found_by='a fresh reader of each section, for what belongs under its heading (round 32\'s section read)',
     moves=[{'blocks': [P('B252')], 'before': P('B296'), 'seq': 1}],
     spans=[whole(P('B252'))],
     reads=[{'text': T(P('B294')), 'kind': 'h2'},
            {'text': T(P('B295'))},
            {'text': T(P('B252')), 'note': ('moved here from the end of Stillness or Movement?; the menu\'s picture and its '
                                            'kinds follow as they are')}],
     reads_label='The Grounding Menu\'s opening as it would read')

card(id='GROUND-ROOM', type='structure', advice='approve', title='3. Grounding Menu: Room first, as in the order',
     what=('Room, with its three lines ("Name five ordinary objects." ...), moves from fifth in the menu to first, ahead '
           'of Body. The menu then runs Room, Body, A familiar object, Breath, Music, Human, Time, Ordinary world. No words '
           'change.'),
     why=('You chose room first in all four places the guide gave the order (Q-5, round 1), but the menu itself starts '
          'with Body and has Room fifth. With the order at the menu\'s top (card 2), someone going down the menu would '
          'meet them the other way round.'),
     stays='Every heading and line of the menu, word for word; only Room\'s place changes.',
     deciding='Approve moves Room first; Reject keeps Body first.',
     advice_note=('Approve, and I\'m fairly sure, most of all if card 2 goes in. Not more than fairly: the body lines (feet '
                  'on the floor, a hand on the heart) are what most people reach for first, and they\'d come second.'),
     ask_because='meaning: someone going down the menu starts with the room, not the body',
     found_by='me, from card 2: the menu\'s own order against the room-first order at its top',
     moves=[{'blocks': [P('B305')] + PALL('B306'), 'before': P('B297'), 'seq': 1}],
     spans=[whole(P('B305'))])

card(id='SHADOW-START', type='structure', advice='ask',
     title='4. The Other Bypass turns into what shadow work is: a heading, or the start of Shadow Work?',
     question=('The Other Bypass is about the bypass of only wanting to feel good; from "Modern people carry so much '
               'trauma ..." it\'s about shadow work: why it may come first, how it shows up when skipped, what it is, and '
               'where to begin. Since the contents put this section at the end of Shadow Work, the part\'s only words on '
               'what shadow work is come last. How each option would read:\n\n'
               'A (a fresh reader\'s idea): a heading above "Modern people carry so much trauma ...":\n'
               '%s### Why Shadow Work Comes First\n'
               'Pro: marks the turn. Con: a third level in a six-paragraph section, and Shadow Work still opens with '
               'nothing on what it is.\n\n'
               'B (my pick): the last two paragraphs open the Shadow Work part, right under its heading:\n'
               '%s# Shadow Work\n%s%s\n%s%s\n%s## %s\n'
               'and The Other Bypass ends:\n'
               '%s... I encountered a lot of it in my first two marriages, to my bewilderment. I wish everybody could '
               'keep shadow work inside the safer rooms of meditation, therapy, journaling, prayer, and honest '
               'conversation.\n'
               'Pro: someone who opens Shadow Work first reads what you mean by it and where to begin, before the sections '
               'that do it, as in your post, where The Other Bypass came before them. Con: the "young parts of you that '
               'are still waiting for love" sentence would no longer come two sections after the list of cognitive '
               'distortions in (Re)defining "Bad Trip"; it would come five sections before it.\n\n'
               'C: leave it. Pro: nothing moves. Con: the section turns halfway with nothing to mark it, and the '
               'definition comes at the part\'s end.')
     % (IND, IND, IND, T(P('B344')), IND, T(P('B345')), IND, T(P('B376')), IND),
     why=('A fresh reader, reading each section for what belongs under its heading, proposed A. Looking at where the '
          'section sits since the contents, I think B fixes more, but it moves your definition, so it\'s your call.'),
     stays='The section as it is.',
     advice_note=('B, and I\'m fairly sure: Shadow Work opens straight into Sorrow, with nothing on what shadow work is '
                  'until its last section.'),
     spans=[whole(P('B344')), whole(P('B345'))], card_after=P('B345'))
