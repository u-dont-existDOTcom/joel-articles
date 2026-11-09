# The cards of round 33, read by build_r33.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). His round-32 note on GROUND-ROOM (2026-11-09 20:08 UTC): "this is too much boilerplate
# stuff that ai added in to my guide. help mne locate more boilerplate stuff that could be removed". Four fresh readers
# read the guide a part each for it (../../humanize/h41-20261109/boilerplate/); ../../humanize/h41-20261109/RESULTS.md has
# every finding's fate. Lesson bad-trips-2026-11-09i.

BUILT = '2026-11-09'
NB = ' '
IND = NB * 4
H41 = BLOB + 'articles/bad-trips/humanize/h41-20261109/'
FOUND = 'a fresh reader of the guide for boilerplate (round 33\'s read, after your round-32 note)'


def li(i):
    return {'text': '- ' + T(i)}


def para(i, note=None):
    r = {'text': T(i)}
    if note:
        r['note'] = note
    return r


def head(i, kind):
    return {'text': T(i), 'kind': kind}


INTRO = [
    'Round 33 (2026-11-09). Round 32 is in: the aura heading as you picked it, the room-first order at the top of the '
    'Grounding Menu without its second "love becomes practical" line, your definition of shadow work and where to begin '
    'opening the Shadow Work part, and your cuts: Room, the familiar object and "Say the date, place, and approximate '
    'time." With Room gone from the menu, the order at its top now starts with the room itself, which your first five '
    'minutes sets up; say if you want that changed.',
    'You asked me to find more boilerplate like that. Four fresh readers went through the guide, a part each, and '
    'flagged 64 pieces ([each one, and what I did with it](%sRESULTS.md)). I left what you wrote or approved, the safety '
    'lines (when to call for help, warning signs), the studies behind your remedies, and your Appendix, so the medical '
    'part has nothing to cut. The rest is on six cards, one per section, each showing the section as it would read '
    'without it, and one card of seven smaller ones, with my pick for each. Card 4 is your lime-peel thought.'
    % H41,
]

SMELL = ('Scratch & sniff a lime peel, or smell an authentic calming essential oil, the Metta NMT sniffer or humic acid '
         'powder (see Mental Stabilizers That Don\'t Abort the Trip).')

card(id='SMELL', type='question', advice='ask', title='4. A Smell part in the Grounding Menu?',
     question=('You wrote that smelling a nice natural scent like a lime peel would be more useful in the menu, but '
               'weren\'t sure, since the guide says it in several places. It does, all in the remedies: your essential '
               'oils entry with the lime peel, the Metta NMT sniffer, humic acid powder, and smelling the ferment. The '
               'menu is where someone in trouble picks one or two things to do now, and it has no smell in it. How each '
               'option would read:\n\n'
               'A (my pick): a Smell part right after Body, one line pointing to the remedies:\n'
               '%sSmell\n%s- %s\n'
               'Pro: the menu offers what you reach for yourself, in one line that names where the guide explains it, '
               'so nothing is said twice. Con: one more part in a menu you\'re trimming.\n\n'
               'B: no Smell part. Pro: nothing added. Con: someone who opens the menu for something to do now won\'t meet '
               'smell there.') % (IND, IND, SMELL),
     why='Your round-32 note: "more useful would be smelling a nice natural scent like lime peel or something, but idk i '
         'feel like this is all said in multiple places also".',
     stays='The menu without a Smell part.',
     advice_note='A, and I\'m fairly sure: it points to your remedies rather than repeating them.',
     spans=[whole(P('B297'))], card_after=P('B298', 3))

MENU_CUT = [P('B298', 0), P('B298', 2), P('B298', 3), P('B302', 1), P('B302', 2), P('B304', 0), P('B304', 4),
            P('B308', 0), P('B308', 1), P('B314')]
card(id='MENU-CUTS', type='boilerplate', advice='approve',
     title='3. Grounding Menu: the rest of the standard grounding lines',
     what=('Ten lines go: three of Body\'s ("Feel both feet against the floor.", "Hold something with weight or '
           'texture.", "Slowly unclench the jaw, hands, belly, and shoulders."), two of Breath\'s (the four-six count and '
           'the Buteyko breath, with the Buteyko evidence note under the menu), two of Music\'s ("Silence is a real '
           'option.", "Keep the stop or change control immediate."), and two of Human\'s ("Ask one calm person to stay '
           'as the lead anchor.", "Let them remind you where you are.").'),
     why=('They\'re the same kind of line as Room: grounding and breathing techniques any guide gives. Holding something '
          'with weight is the familiar object again. Human\'s two lines are said by the very next section, Get One Human '
          'Anchor ("one calm person should be the anchor"), and by your first five minutes ("remind them where they '
          'are").'),
     stays=('Your hand on the heart and solar plexus; the longer exhale, the warning against forced breath-holds and '
            'your whisper line; your music lines (no forced playlist, the drum and the harp, Chantress Seba); "Don\'t '
            'process with the most reactive person in your life."; Time; and Ordinary world with its safety lines.'),
     deciding='Approve cuts all ten; Revise to keep any (say which); Reject keeps the menu as it is.',
     advice_note=('Approve, and I\'m fairly sure: each is what you cut Room for. Least sure of the breathing count, since '
                  'some readers already know four-six breathing and reach for it.'),
     ask_because=('downside: the menu loses the standard techniques a reader may know from elsewhere (feet on the floor, '
                  'four-six breathing, the Buteyko breath and its note)'),
     found_by=FOUND,
     edits=[cut_block(i) for i in MENU_CUT],
     spans=[whole(i) for i in MENU_CUT],
     reads=[head(P('B294'), 'h2'), para(P('B295')), para(P('B252'), 'then the menu\'s picture'), para(P('B297')),
            li(P('B298', 1)), para(P('B301')), li(P('B302', 0)), li(P('B302', 3)), li(P('B302', 4)), para(P('B303')),
            li(P('B304', 1)), li(P('B304', 2)), li(P('B304', 3)), para(P('B307')), li(P('B308', 2)), para(P('B309')),
            li(P('B310', 0)), li(P('B310', 1)), para(P('B311')), li(P('B312', 0)), li(P('B312', 1)), li(P('B312', 2)),
            li(P('B312', 3))],
     reads_label='The Grounding Menu as it would read')

STILL = [P('B248'), P('B249'), P('B250'), P('B251'), P('B313')]
card(id='STILL-CUT', type='boilerplate', advice='approve',
     title='2. Stillness or Movement?: the whole subsection',
     what=('The subsection at the end of your first five minutes goes: its heading, the two-minute test, pacing versus '
           'lying under a blanket, parallel processing, and the Movement evidence note.'),
     why=('Your first five minutes already says what a reader needs about moving: "Letting them move around is fine, and '
          'pacing can help, but keep them from taking more of any substance." The rest is standard advice and an '
          'evidence note for it. I moved that note here this afternoon; your round-32 note showed I should have offered '
          'to cut it instead.'),
     stays='Your first five minutes, word for word, with its pacing line; the Grounding Menu\'s walking and exercise lines.',
     deciding='Approve cuts the subsection; Revise to keep a paragraph (say which); Reject keeps it.',
     advice_note=('Approve, and I\'m fairly sure of all but parallel processing. If that one is your own, Revise to keep it '
                  'and it ends your first five minutes.'),
     ask_because=('downside: parallel processing (one part of attention stays with the feeling while another finishes a '
                  'small task) is said nowhere else in the guide, and it may be yours'),
     found_by=FOUND,
     edits=[cut_block(i) for i in STILL],
     spans=[whole(i) for i in STILL],
     reads=[para(P('R27-PFA5'), 'the last paragraph of your first five minutes, as it is'), head(P('B294'), 'h2')],
     reads_label='Where your first five minutes would end')

ANCHOR = [P('B259'), P('B260'), P('B274')]
card(id='ANCHOR-CUTS', type='boilerplate', advice='approve',
     title='5. Get One Human Anchor: the sitter\'s script and the 3 a.m. movement tips',
     what=('Three paragraphs go: "Script for the sitter or friend:" with its script ("I\'m here. You\'re not alone. This '
           'is a wave. ..."), and Alone at 3 a.m.\'s "When the body still needs movement, keep it contained and boring: '
           'brush your teeth, stretch gently, take a calm shower, or do a few slow wall push-ups. Then protect sleep."'),
     why=('The sitter\'s script says what your first five minutes and the Do list already say ("don\'t try to win an '
          'argument", "I\'m with you"), and "This is a wave" is your breath line. The 3 a.m. tips are a standard list.'),
     stays=('The script for the person in the altered state, which Alone at 3 a.m. tells them to send; your 3 a.m. line, '
            'which then ends the section.'),
     deciding='Approve cuts all three; Revise to keep one (say which); Reject keeps them.',
     advice_note='Approve, and I\'m fairly sure.',
     ask_because=('downside: a sitter loses ready words to say, and someone alone at 3 a.m. loses small things to do when '
                  'the body needs to move'),
     found_by=FOUND,
     edits=[cut_block(i) for i in ANCHOR],
     spans=[whole(i) for i in ANCHOR],
     reads=[head(P('B253'), 'h2'), para(P('B254')), para(P('B255'), 'then the section\'s picture'), para(P('B257')),
            para(P('B258')), head(P('B271'), 'h3'), para(P('B272')), para(P('B273')), para(P('R31-ALONE'))],
     reads_label='Get One Human Anchor as it would read')

HELP = [P('B282', 1), P('B282', 2), P('B282', 4), P('B290')]
card(id='HELPER-CUTS', type='boilerplate', advice='approve',
     title='6. For the Person Helping: the Do lines your first five minutes already says',
     what=('Three lines of the Do list go ("Reflect without arguing: ...", "Keep the room quiet, private, warm, and '
           'physically safe, and move anyone they\'re wary of somewhere else.", "Translate metaphysics into shared safety '
           'values: ..."), and the harm part\'s summary, "Redirect within the person\'s value-world toward peace and '
           'protection, increase containment, and bring in crisis support as early and as non-coercively as the situation '
           'allows."'),
     why=('Your first five minutes says the first two ("don\'t try to win an argument with their visions", "dim the '
          'lights, and clear out the extra people around them"), the scripts in the harm part say the third, and the '
          'summary repeats those scripts and the call-for-help line under them.'),
     stays=('"Ask simple questions: ...", "Call for help early when safety is slipping.", "Set behavioral boundaries '
            'without humiliation: ...", and the harm part\'s example, scripts and safety lines.'),
     deciding='Approve cuts all four; Revise to keep one (say which); Reject keeps them.',
     advice_note='Approve, and I\'m fairly sure.',
     ask_because=('downside: two details are said nowhere else, a warm room and moving anyone they\'re wary of somewhere '
                  'else'),
     found_by=FOUND,
     edits=[cut_block(i) for i in HELP],
     spans=[whole(i) for i in HELP],
     reads=[head(P('B281'), 'h3'), li(P('B282', 0)), li(P('B282', 3)), li(P('B282', 5)), head(P('B285'), 'h3'),
            para(P('B286')), para(P('B287')), para(P('B288')), para(P('B289')), para(P('B291')), para(P('B292'))],
     reads_label='The Do list and the harm part as they would read')

REDEF = [P('B360'), P('B362')] + PALL('B363')
card(id='REDEFINE-CUTS', type='boilerplate', advice='approve',
     title='7. (Re)defining "Bad Trip": the list of causes and the CBT thinking traps',
     what=('Two lists go: "A bad trip or destabilizing state may also come from drug interactions, sleep deprivation, '
           '..." and "Cognitive distortions from Cognitive Behavioral Therapy (CBT) can create or prolong the crisis:" '
           'with its seven traps.'),
     why=('The thinking traps are a textbook list with a clinical name. The causes list is the standard one too; your '
          'own paragraphs above it already give the dose, the body, the setting and the mindset.'),
     stays='Your (Re)defining paragraphs, word for word, and the blockage line with its picture, which then ends the section.',
     deciding='Approve cuts both lists; Revise to keep one (say which); Reject keeps them.',
     advice_note='Approve, and I\'m sure of the thinking traps; fairly sure of the causes.',
     ask_because=('downside: the causes list names a few causes the guide says nowhere else (sexual or social pressure, '
                  'retreat pressure, hunger), and round 24 kept it for that'),
     found_by=FOUND,
     edits=[cut_block(i) for i in REDEF],
     spans=[whole(i) for i in REDEF],
     reads=[head(P('B329'), 'h2'), para(P('B330a')), para(P('B330b')), para(P('B330c')),
            para(P('B357'), 'then its picture, "Universe Sends What You Need"'), head(P('B332'), 'h2')],
     reads_label='(Re)defining "Bad Trip" as it would read')

LABELS = [P('B147')] + PALL('B148')
card(id='LABELS-CUT', type='boilerplate', advice='approve',
     title='1. How I label the evidence: the whole section',
     what=('The section goes: its heading and its four labels (established acute treatment, limited human evidence, '
           'mechanism or preclinical evidence, personal field signal).'),
     why=('No remedy in the guide is tagged with these labels, so the legend explains a system the page never uses. '
          'It\'s a standard evidence-grading note.'),
     stays='Everything else in My Acute Rescue Hierarchy of Remedies.',
     deciding='Approve cuts the section; Reject keeps it.',
     advice_note='Approve, and I\'m fairly sure.',
     ask_because=('downside: it\'s in the contents you chose in round 30, and its last label says how you weigh your own '
                  'observations'),
     found_by=FOUND,
     edits=[cut_block(i) for i in LABELS],
     spans=[whole(i) for i in LABELS],
     reads=[para(P('B141'), 'the hierarchy\'s opening, as it is, ends here'), head(P('B217'), 'h2')],
     reads_label='Where the hierarchy\'s opening would lead')

card(id='SMALL-CUTS', type='boilerplate', advice='ask', title='8. Seven smaller ones: which go?',
     question=('Each as it is now, with my pick. Answer with the letters that go, or "none".\n\n'
               'a. For the Person Helping\'s opening paragraph: "%s" My pick: keep. It opens the section with a known '
               'group\'s approach, which your first five minutes agrees with.\n\n'
               'b. After the Storm: "%s" My pick: keep. It\'s the only place the guide asks a reader to look back at '
               'what happened.\n\n'
               'c. Abuse Memories, Recovered Memories, and Certainty, its first and last paragraphs: "%s" and "%s" My '
               'pick: keep. "Don\'t treat the certainty you feel in that state as evidence" and "It could be true '
               'psychologically, or symbolically, or literally" are your view of a trip\'s memories: neither dismissed '
               'nor taken as fact.\n\n'
               'd. Tripsitting Yourself or Others\' opening: "%s" My pick: keep: it points people who "gamble and lose" to help.\n\n'
               'e. Euphoric Certainty\'s last paragraph: "%s" My pick: cut. No Rash Actions already says it can wait '
               'until the state has passed, and "an emergency impulse wearing angel wings" is the kind of quip you\'ve '
               'cut before.\n\n'
               'f. Niacin: "A vitamin is not automatically harmless." My pick: cut. Its side effects, two paragraphs '
               'down, name the real risk.\n\n'
               'g. The Grounding Menu\'s "Twelve simultaneous techniques can become another form of panic." My pick: '
               'cut. The menu no longer has twelve, and its heading says to choose one or two.')
     % (T(P('B280')), T(P('B429')), T(P('B406')), T(P('B409')), T(P('B232')), T(P('B328'))),
     why='The readers flagged these too, but each has a reason to stay, or is one line; your call either way.',
     stays='All seven as they are.',
     advice_note='e, f and g go; a to d stay.',
     spans=[whole(P('B280')), whole(P('B429')), whole(P('B406')), whole(P('B409')), whole(P('B232')), whole(P('B328')),
            span_of(P('B212'), 'A vitamin is not automatically harmless.'),
            span_of(P('B295'), 'Twelve simultaneous techniques can become another form of panic.')],
     card_after=P('B429'))
