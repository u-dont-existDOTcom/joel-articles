# The cards of round 60, read by build_r60.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 70: his round-59 answers in the guide, and the first gut-tool paragraphs
# checked by themselves (humanize/h78-20261126/RESULTS.md). No string here is %-formatted.

BUILT = '2026-11-26'
H = 'https://www.pangram.com/history/'
R59 = BLOB + 'articles/bad-trips/review/r59/RESULTS-R59.md'
H78 = BLOB + 'articles/bad-trips/humanize/h78-20261126/RESULTS.md'
LEFT = BLOB + 'articles/bad-trips/humanize/h78-20261126/LEFT.md'

INTRO = [
    'Round 60 (2026-11-26). Your (b) for the poison control paragraph is in. Your two GUT-SIGNS answers are in as three '
    'paragraphs, each of which read Human High on its first check: [the signs](' + H +
    '7a9e0fdc-ffcf-43a1-998b-f5c550196b56), [what to do](' + H + 'af2c0ec5-7b77-48e2-b574-00d5dfa88c63) and '
    '[the opening of the gut tools](' + H + 'a53a2ce3-838c-409f-801f-bfa6d403d9d9). Card 1 shows them and names what I '
    'left out. [Each point of your answers and where it went](' + R59 + ').',
    'Then the work went on down the list. In ZeoCharge & Ferment, the ferments paragraph reads '
    '[Human High as it stands](' + H + 'c293133e-f9b6-46a2-98eb-85e71e6a6ae0), and its first paragraph reads '
    '[Human High](' + H + '73808644-46a4-47a2-a77d-b71197500b29) with the two remedies put first. The four zeolite '
    'paragraphs after them still read below High, and what the fresh readers could not follow there is facts, which is '
    'card 2 ([every check](' + H78 + '); [what is left](' + LEFT + ')).',
]

card(id='GUT-SIGNS-IN', type='question', advice='ask',
     title='1. Your GUT-SIGNS answers as they went in, and two things I left out',
     whose=('his own: his round-59 answers 2.1 and 2.2, made into paragraphs for the reader by me; "A gut-driven mental hell '
            'is often mistaken as shadow work." is his line, word for word'),
     question=('The four highlighted paragraphs hold your answers. From 2.1: loss of bodily control is "someone wetting or '
               'soiling themselves, or not being able to sit up, stand, walk or talk", and neurological disorganization is '
               '"my catch-all for that loss of control plus a whole lot more". From 2.2: "address the gut first" and "You '
               'don\'t need to try to tell which is from what", and under Gut-Toxin & Die-Off Tools the paragraph that '
               'starts "After all, nausea and diarrhea are common on psychedelics".\n'
               'Two things I left out, and one I added:\n'
               '1.1 The list of symptoms GPT gave for neurological disorganization. Most of it (confusion, shaking, light '
               'and sound being too much) is what any strong trip brings, so a friend could not use it to tell. I linked '
               'your brain checks instead, which are tests a friend can do.\n'
               '1.2 "if the gut is fine obviously it\'s not related to the gut". Two fresh readers said it told them '
               'nothing, and a fine gut does not rule out the brain, which the paragraph before it names.\n'
               '1.3 Added: losing control of the body "is on the list to call medics for". Wetting or soiling themselves, '
               'not being able to walk normally and losing the ability to speak are all on your Call Medics For list, and '
               'without the pointer a reader could treat someone who cannot talk or walk with a remedy only.\n'
               '(a) fine as they are; (b) put back what I left out, or take out what I added (say which); or edit any of '
               'the four.'),
     why=('the words come from your answers, I chose what to leave out of them, and the call-medics pointer is mine from '
          'your own list'),
     stays='the four paragraphs, which are in the guide now',
     advice_note='(a); fairly sure. If you want examples for neurological disorganization, name the ones a trip does not bring by itself',
     spans=[whole(P('B141')), whole(P('R59-GUT-DO')), whole(P('B151')), whole(P('R59-GUT-COMMON'))])

card(id='ZEO-FACTS', type='question', advice='ask',
     title='2. ZeoCharge & Ferment: six things about zeolite only you know',
     whose='the post\'s paragraphs, drafted by a model from his practice',
     question=('These four paragraphs still read below High. The two on taking zeolite read Human, but Low and Medium, as '
               'they stand ([check](' + H + '25652097-7c2d-444d-ab06-9e9af3c993c1)) and after two small joins ([check](' + H +
               '86a0478d-42dc-4596-8cc8-ff8b777f8734)). The two on ozonating read AI as they stand ([check](' + H +
               '859d5bdf-7aeb-4f53-b5d5-9f7bf44ca04f)) and after a first small try ([check](' + H +
               '07cec6fa-57a0-406c-b839-0bd71249e4ec)). I can\'t find more AI tells in them that I know how to fix, and '
               'apart from the facts you gave, none of it is your own writing. What three fresh readers could not get '
               'from them is facts:\n'
               '2.1 Is the fermented beet juice the ZHoly3O ferment, or a different one?\n'
               '2.2 How much water for the spoonful of zeolite, and do you repeat it if the nausea keeps on?\n'
               '2.3 Rubbing it on the body: the dry powder, or the mix in water?\n'
               '2.4 "Many products did nothing for me, and quality mattered enormously." How does a reader tell a good '
               'zeolite before a trip, when sober people don\'t feel much? Is the answer ZeoCharge?\n'
               '2.5 "Most zeolites have clogged pores because they haven\'t been cleaned." Is the ozonating what cleans '
               'them?\n'
               '2.6 How much powder and water go under the ozone for those ten minutes?\n'
               'A line on any of them and I\'ll write it in; or say which to leave unanswered.'),
     why=('a reader deciding what to buy or make cannot act on these paragraphs yet, and each answer gives a sentence '
          'something to say'),
     stays='the four paragraphs as they are in your post',
     advice_note='2.1, 2.4 and 2.5 first: they change what a reader buys or makes',
     spans=[whole(P('B158')), whole(P('B155')), whole(P('B156')), whole(P('B157'))])
