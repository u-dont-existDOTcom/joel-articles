# The cards of round 31, read by build_r31.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words and card). Round 31 carries out his round-28 answers that waited for the contents: METHOD-WHERE ("a ...
# do your best but keep in mind how confident you are that this is the best idea in this case, ask me for teaching cards
# when unsure about anything, make sure i'm able to see the options and how theyh would really look") and AFT-HOW-MUCH
# ("if it were right after this section it would be an easy choice"), now that round 30's contents is in.

BUILT = '2026-11-09'
NB = ' '
R31 = 'articles/bad-trips/review/r31/'
ALONE = (REPO / R31 / 'MW-ALONE.txt').read_text(encoding='utf-8').strip()
BREATH = (REPO / R31 / 'MW-BREATH.txt').read_text(encoding='utf-8').strip()
PREP = (REPO / R31 / 'MW-PREP.txt').read_text(encoding='utf-8').strip()
TRAIN = ('And train before you need it, sending love to a frightening image, to someone you hate (without approving of what '
         'they did), and to the inner child.')
DEREAL = T(P('B426', 2))
PARANOIA = T(P('B426', 6))
POINTER = ('Derealization and depersonalization, paranoia or psychosis-like beliefs: see Bring in mental-health support, '
           'right below.')

INTRO = [
    'Round 31 (2026-11-09). Round 30 is in: the contents as A, with the brain section first and the three headings renamed '
    'so readers can find them, your Syrian rue oil and essential-oils entries, and the herbs named. A fourth fresh reader '
    'read the renamed contents and found every section on the first pick, with 3 guesses where the first two readers had '
    'made 6 and 5. Your caution about vaping the whole seeds stays as your entry says it, and mine is out; your note about '
    'trying any new substance in small amounts first is already in My Acute Rescue Hierarchy\'s opening ("try all these '
    'things in very low, increasing doses").',
    'Now the places people use in trouble get your method. Three cards each put a line the guide already has where it '
    'will be used, in the four places round 28 named but one: the thinking traps now sit two sections before your "young '
    'parts of you that are still waiting for love" line, so they need nothing. And with the support section right after '
    'the aftermath list, one card asks where paranoia and derealization go, with each option as it would read.',
]

card(id='AFT-PLACE', type='structure', advice='ask', title='1. Paranoia and derealization: in the support section, or where they are?',
     question=('Bring in mental-health support when: now comes right after What Kind of Aftermath Is This?, which you said would '
               'make moving these two there an easy choice. How each option would read:\n\n'
               'A (your idea): both move under the support list, after its six lines, as you wrote them, and your aftermath '
               'list keeps one line where they were:\n'
               '%s- %s\n'
               'and the support section ends:\n'
               '%s- %s\n%s- %s\n'
               'Pro: the two kinds most likely to need a professional sit with the lines on when to bring one in. Con: '
               'that list says when to get help, and your two items say what helps, so it becomes two kinds of list; and a '
               'reader a week on still looks in the aftermath list first (the fresh readers did), then has to follow the '
               'line.\n\n'
               'B: only paranoia moves, with the same kind of line left in your list. Your paranoia item says to bring '
               'in professional support; your derealization item\'s help is all things the reader can do (people, walks, '
               'yin yoga, Somatic Experiencing), so it stays with the other kinds. Pro: each kind sits with what it '
               'asks for. Con: the support list still changes what it is, for one item.\n\n'
               'C (my pick): both stay where they are, and the support list now follows them. Pro: nothing moves; '
               'readers find them where they look first; your paranoia item already says to seek professional support, '
               'and the next thing they read is when to. Con: the two kinds that may need a professional sit just above '
               'the support list rather than in it.') % (NB * 4, POINTER, NB * 4, DEREAL, NB * 4, PARANOIA),
     why=('Your round-28 answer: "i suppose those last two might be better in the bring outside help in section, but we '
          'should make sure the aftermath section points to that section then briefly for the cases that got moved i '
          'guess... also depends on where that section is placed, if it were right after this section it would be an easy '
          'choice". It is right after now, so moving is easy; the question is whether it still helps.'),
     stays='Both items as they are, where they are, until you answer.',
     advice_note=('C, and I\'m fairly sure: with the two sections side by side, the move adds a step for the reader and gains '
                  'little. If you\'d rather have them with the support lines, B fits your items best.'),
     spans=[whole(P('B426', 6))])

card(id='MW-ALONE', type='method', advice='approve', title='Alone at 3 a.m.: your method for someone with no sitter',
     what='A new paragraph after "Send the human-anchor script.": "%s"' % ALONE,
     why=('Someone alone at 3 a.m. has nobody there to bring them love, so the section gives them a way to do it for '
          'themselves, in the guide\'s own lines: the hand on the heart from the Grounding Menu, and the self-talk from '
          'For the Person Helping ("This feeling is allowed to move through. I don\'t have to become it. I can love the part '
          'of me that feels it."). "While you wait" ties it to the message just sent.'),
     stays='The lamp, the keys, "No big actions until morning", the script, and the movement lines.',
     deciding='Approve puts it in; Revise to say it your way; Reject leaves the section as it is.',
     advice_note=('Approve, and I\'m fairly sure: it\'s the one moment in the guide where nobody else can do the loving. The '
                  'cost is that the self-talk is said twice, here and for the helper.'),
     ask_because='downside: the self-talk is said again here, as For the Person Helping already says it',
     found_by='round 28\'s METHOD-WHERE card, from a fresh reader\'s list of where the guide is generic',
     inserts=[{'before': P('B274'), 'kind': 'p', 'seq': 1, 'text': ALONE}],
     spans=[whole(P('B273'))],
     receipt=R31 + 'MW-ALONE.receipt.json')

card(id='MW-BREATH', type='method', advice='approve', title='Grounding Menu, Breath: "I can love the part of me that feels it."',
     what='The breath list\'s last line, "Whisper: "This is a wave."", becomes "%s"' % BREATH,
     why=('The breath lines say how to breathe but nothing of love; the line from the helper\'s self-talk gives the reader '
          'something to do with the feeling while the breath slows, not only wait it out.'),
     stays='The other breath lines, and "This is a wave."',
     deciding='Approve adds it; Reject leaves the line as it is.',
     advice_note='Approve, and I\'m sure of this one: one sentence added to a line the reader is already saying.',
     ask_because='downside: the line is said again here, as For the Person Helping already says it',
     found_by='round 28\'s METHOD-WHERE card, from a fresh reader\'s list of where the guide is generic',
     edits=[replace_words(P('B302', 4), T(P('B302', 4)), BREATH)],
     spans=[whole(P('B302', 4))],
     receipt=R31 + 'MW-BREATH.receipt.json')

card(id='MW-PREP', type='method', advice='approve', title='Planning a Trip or Ceremony?: train love before you need it',
     whose='his own: his round-24 version of Give the Session a Beginning and an End (2026-11-08)',
     what=('One sentence added to your preparation paragraph, after "spiritual breakthroughs.": "%s" It\'s your Demons '
           'line, "So train before you need it, sending love to a frightening image, to someone you hate (without approving '
           'of what they did), to your shame and your body, ...", with its list cut to three.') % TRAIN,
     why=('Your preparation says to go in with gentle intentions and that preparing to open up to love can make the trip '
          'unneeded, but not how to prepare that love. Your Demons section says how, and says to do it beforehand; '
          'someone planning reads this section, not Demons.'),
     stays='The rest of your paragraph, word for word, and the Demons line as it is.',
     deciding='Approve adds it; Revise to say it your way or keep the whole list; Reject leaves your paragraph as it is.',
     advice_note=('Approve, and I\'m fairly sure: it\'s the practice your next sentence counts on. Less sure of the cut list: '
                  'Revise if the shame, the body, sickness and death belong in the preparation too.'),
     ask_because='his own: your preparation paragraph (round 24), with a sentence of your Demons section added',
     found_by='round 28\'s METHOD-WHERE card, from a fresh reader\'s list of where the guide is generic',
     edits=[replace_words(P('B366b'), 'spiritual breakthroughs. Sometimes', 'spiritual breakthroughs. %s Sometimes' % TRAIN)],
     spans=[span_of(P('B366b'), 'spiritual breakthroughs.')],
     receipt=R31 + 'MW-PREP.receipt.json')
