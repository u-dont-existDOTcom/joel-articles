# The cards of round 46, read by build_r46.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 54: his C1 to C4 answers in (../../humanize/h62-20261120/RESULTS.md), and
# his "short tags on headings could be good" (2026-11-20 22:40 UTC).

BUILT = '2026-11-20'
H62 = BLOB + 'articles/bad-trips/humanize/h62-20261120/'
NB = ' '
IND = NB * 4

# Each remedy heading as the guide has it (its B id) and, under A, its tag. The tags say what each section rests the
# remedy on, read from the section itself on 2026-11-20 (turn 54): his own experience ("In my experiments", "helps my
# nausea", "I've found", "I just discovered", "People tell me", "for me and friends"), a study in people (DMSO: the 1967
# trial in psychiatric patients), or a standard medical use (activated charcoal for a poisoning).
HEADS = [
    ('B152', 'Zeolite and Ferment in ZHoly3O', 'My Experience'),
    ('B159', 'Actual Activated Charcoal', 'Standard for Poisoning'),
    ('B166', 'Coffee Cherry for Nausea and Brain Recharge', 'My Experience'),
    ('B181', 'Metta NMT Sniffer Makes the Trip Chill & Lovey!', 'My Experience'),
    ('B183', 'Humic Acid Brings Brain to Optimal Function', 'My Experience'),
    ('H54-CREATINE-H', 'Creatine Is Blissful and Good for the Brain', 'My Experience'),
    ('H54-MANGO-H', 'Mango Leaf Tea Relaxes Without Killing the Trip', 'My Experience'),
    ('R30-OILS1', 'Authentic Calming Essential Oils (or a Lime Peel)', 'My Experience'),
    ('B199', 'DMSO', 'Some Human Studies'),
    ('R30-RUE1', 'Syrian Rue Oil Makes the Trip Gentle & Sweet', 'My Experience'),
    ('B185', 'Ocean Water to Calm & Protect the Energetic Field', 'My Experience'),
    ('B189', 'Shungite, Aged Ozonated-Charcoal Water, or Boiled Charcoal Water', 'My Experience'),
    ('B170', 'Beach Morning Glory--Ipomoea pes-caprae', 'My Experience'),
    ('B210', 'A Final Trip Killer: Niacin (a Form of Vitamin B3)', 'My Experience'),
]
OLD = {'My Experience': 'Personal Field Signal', 'Some Human Studies': 'Limited Human Evidence',
       'Standard for Poisoning': 'Established Acute Treatment'}

A_LIST = '\n'.join('%s%s [%s]' % (IND, h, tag) for _, h, tag in HEADS)
B_LIST = '\n'.join('%s%s [%s]' % (IND, h, OLD[tag]) for _, h, tag in HEADS if tag != 'My Experience')
C_LINE = ('Unless a heading says otherwise, a remedy here rests on my own experience and what people I\'ve given it to '
          'have told me.')

INTRO = [
    'Round 46 (2026-11-20). Your C1 to C4 answers are in, each checked first ([the checks and what went in](%sRESULTS.md)), '
    'and your Systema video is linked in your breathing line.' % H62,
    'You said short tags on the headings could be good. This card shows each remedy heading with its tag as it would '
    'read, and two other ways to do it.',
]

card(id='TAGS', type='question', advice='ask',
     title='Short evidence tags on the 14 remedy headings',
     question=('Each tag says what its section rests the remedy on, as the section itself says it: your own experience '
               '("In my experiments", "helps my nausea", "I\'ve found", "for me and friends"), a study in people (DMSO: '
               'the 1967 trial in psychiatric patients), or a standard medical use (activated charcoal for a poisoning). '
               'How each heading would read:\n\n'
               'A (my pick): a tag in square brackets at the end of each heading:\n%s\n'
               'Pro: a reader scanning the headings in a hurry sees at a glance which remedies have studies behind them '
               'and which rest on your experience. Con: twelve of the fourteen say the same thing.\n\n'
               'B: the same, in the guide\'s old evidence labels (the How I label the evidence section, cut in round 33), '
               'Personal Field Signal on the twelve and:\n%s\n'
               'Pro: the labels you had. Con: "Personal Field Signal" needs explaining, and the section that explained '
               'it is gone.\n\n'
               'C: tags only where there is more than your experience (DMSO and activated charcoal, as in A), and one line '
               'under My Acute Rescue Hierarchy of Remedies:\n%s%s\n'
               'Pro: two tags stand out instead of fourteen. Con: a reader who skips that line can take an untagged '
               'heading as tested.\n\n'
               'Two things only you know: do your humic acid, coffee cherry or creatine notes cite studies in people or '
               'animals? If they do, that heading\'s tag says so instead ("Some Human Studies" or "Animal Studies"). '
               'And are the words right: "My Experience", "Some Human Studies", "Standard for Poisoning"?')
     % (A_LIST, B_LIST, IND, C_LINE),
     why=('The tags go on your headings, and what each remedy rests on is partly in your notes, which I couldn\'t open '
          'from here this turn. Ocean Water\'s heading also gets title case ("to Calm & Protect the Energetic Field"), '
          'the headings rule every lane follows since 20 November.'),
     stays=('The headings as they are, until you answer. Then each changed heading is checked with its first paragraph '
            'before it goes in, and every link to its section is fixed in the same pass, since a heading\'s words make '
            'its link.'),
     advice_note=('A, fairly sure of the brackets and the three tags; less sure of humic acid, coffee cherry and creatine '
                  'until you say what your notes cite.'),
     spans=[whole(P(bid)) for bid, _, _ in HEADS], card_after=P('B152'))
