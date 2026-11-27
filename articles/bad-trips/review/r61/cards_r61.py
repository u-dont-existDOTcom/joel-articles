# The cards of round 61, read by build_r61.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 71: his round-60 answers in the guide, and the zeolite and charcoal paragraphs
# checked (humanize/h79-20261126/RESULTS.md). No string here is %-formatted.

BUILT = '2026-11-27'
H = 'https://www.pangram.com/history/'
R60 = BLOB + 'articles/bad-trips/review/r60/RESULTS-R60.md'
H79 = BLOB + 'articles/bad-trips/humanize/h79-20261126/RESULTS.md'
LEFT = BLOB + 'articles/bad-trips/humanize/h79-20261126/LEFT.md'
POST = 'https://ibogaqueen.substack.com/p/here-is-why-everyone-should-use-zeocharge'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-14 22:08 UTC: "didn\'t understand why you gave me no cards and quit working tho"')

INTRO = [
    'Round 61 (2026-11-27). Your "a" on round 60 keeps the gut-driven paragraphs as they are. Your answer on the '
    'ferments is in, nearly word for word, and the paragraph reads [Human High in one window](' + H +
    'cd5a0e49-7df7-451b-9bc3-0728297b1b7b). [Each point and where it went](' + R60 + ').',
    'For the questions you left open, I read [your ZeoCharge post](' + POST + '), which the section\'s heading links. It '
    'answers some of them, and card 1 shows what I took from it. Three zeolite paragraphs now read Human High by '
    'themselves ([how you take it](' + H + 'fe031537-bb41-4546-9e44-43acdd13df98), [how you ozonate it](' + H +
    'e36188fb-6982-4218-a048-6bf30476bc3f), and [the metal paragraph with it](' + H +
    'c6363909-7c94-4758-82e9-ecfc47240fef)). The fourth is card 3. Activated Charcoal reads [Human High](' + H +
    'ae42aae9-c334-4a8f-a606-2ed5c9d313b9) in my version, but the warning check won\'t let it in without your word: '
    'card 2 ([every check](' + H79 + '); [what is left](' + LEFT + ')).',
]

card(id='FROM-POST', type='question', advice='ask',
     title='1. ZeoCharge & Ferment: what I took from your ZeoCharge post, and one dose line I left out',
     whose='the post\'s paragraphs, drafted by a model from his practice, with facts from his ZeoCharge post',
     question=('Your post answered three of the questions you left open, and these went in (highlighted):\n'
               '1.1 "a spoonful of zeolite into a cup of water or juice", from your "mix a spoon or 2 of the zeolite into a '
               '(non-metal) cup of water ... or juice".\n'
               '1.2 "however much zeolite was in the water", from your "this works regardless of how much zeolite I am '
               'ozonating". Your post says 20 minutes at 1000mg an hour; the guide\'s ten minutes at two grams an hour is '
               'the same amount of ozone, so the guide\'s numbers stay.\n'
               '1.3 "Zeolite binds metals, which is part of why it is used for heavy-metal removal, so I don\'t put it into a '
               'metal thing or use a metal spoon", from your "Zeolite binds metals, so don\'t put it into a metal thing or use '
               'a metal spoon."\n'
               '1.4 "holding its jar in my hand", from your "HOLD the zeolite in your hand".\n'
               'One line I left out: "If the zeolite dose at 5g makes you feel worse (or only slightly better), you (usually) '
               'need to take MORE. But if taking more does make you feel worse, then you might have a bad zeolite!" It answers '
               'two of your questions (whether to repeat it, and how to tell a bad zeolite). But in a guide for someone '
               'sitting with a friend, it says to give more to a person who feels worse, so I didn\'t put it in.\n'
               'Still open: rubbing it on the body, is that the dry powder or the mix in water?\n'
               '(a) fine as they are, and the 5g line stays out; (b) add the 5g line after the dose sentence; or write the line as you\'d say it. '
               'And a word on the rubbing, if you like.'),
     why=('the facts come from your ZeoCharge post but weren\'t in this guide, and the 5g line is a dosing call only you '
          'can make'),
     stays='the paragraphs as highlighted, which are in the guide now',
     advice_note='(a): the 5g line would need its "feel worse" explained before a sitter could act on it safely',
     spans=[whole(P('B158')), whole(P('B156')), whole(P('B157'))])

card(id='CHARCOAL-WORDS', type='question', advice='ask',
     title='2. Activated Charcoal: may two lines with no caution in them be said in other words?',
     whose='the post\'s paragraphs, drafted by a model from his practice',
     question=('As your post has it, Activated Charcoal reads [AI, High](' + H + '73098017-5efb-41ae-9b5f-92560768e5bd). '
               'My version keeps every fact and reads [Human High in one window](' + H +
               'ae42aae9-c334-4a8f-a606-2ed5c9d313b9):\n'
               '"I don\'t treat charcoal and zeolite as interchangeable, because drugs bind to activated charcoal as well as '
               'gut toxins, so it can flatten or reduce a trip.\n'
               'So if someone took too much, or the gut itself is toxic, I give charcoal. If the trip is going fine and only '
               'the gut feels bad, I give zeolite, which leaves the trip alone.\n'
               'Medicines bind to charcoal too, so I\'d think twice before giving it to someone who depends on one, and I\'d '
               'tell any medics who come that charcoal was taken."\n'
               'It isn\'t in the guide yet. The check that guards your warnings holds two of the post\'s lines word for word, '
               'because each has a warning word in it ("toxicity" and "stop"): "Activated charcoal can help gut toxicity, but '
               'it adsorbs drugs." and "When the goal is to reduce drug absorption or stop a toxic gut situation, charcoal may '
               'be relevant." Neither line is a caution. A version that keeps their exact words would have to bring back "may '
               'be relevant", which two readers marked as the line\'s AI hedge.\n'
               '(a) my version goes in, and from now on a line whose only warning word isn\'t a caution may be said in other '
               'words, as long as every fact stays; (b) my version goes in, this time only; (c) your post\'s words stay.'),
     why=('the check\'s rule is your call: it was set so that no warning gets reworded without you'),
     stays='the three paragraphs as your post has them, until you answer',
     advice_note='(a): it would also let the guide\'s other lines with "stop" or "risk" in a plain sentence be fixed without a card each',
     spans=[whole(P('B160')), whole(P('B161')), whole(P('B162'))])

card(id='TEACH-B155', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='3. ZeoCharge & Ferment: the two sentences on which zeolite to buy',
     reading=('As your post has it, with the paragraph before it: [Human, but Low and Medium](' + H +
              '25652097-7c2d-444d-ab06-9e9af3c993c1). It is under 50 words, so it can only be checked with a neighbour.'),
     tested=('My version, from your ZeoCharge post: "I use powdered zeolite rather than nano-liquid zeolite. Many products '
             'did nothing for me, I think because most zeolites have clogged pores that haven\'t been cleaned, but ZeoCharge '
             'is sold as cleaned." Its reading changes with whatever sits next to it.\n\n'
             'With the paragraph before it: its first sentence High, its second Medium ([check](' + H +
             '38bb7235-8994-4644-92bf-a05d500f19b0)).\n\n'
             'With the ozone paragraph after it: High for both sentences, but the ozone paragraph\'s safety line goes Medium '
             '([check](' + H + 'bf5f7b19-a34b-42e8-9158-22e90c45ac1c)).\n\n'
             'With the safety line joined to the sentence before: the first sentence Medium, and the whole ozone paragraph '
             'Medium ([check](' + H + '9363878c-76d1-498c-a49d-4388cf31a388)).\n\n'
             'Six earlier tries with the paragraph before it, ending in Low and Medium. The ozone paragraph by itself '
             'reads [High](' + H + 'e36188fb-6982-4218-a048-6bf30476bc3f).'),
     sense=('Fresh readers asked of the post\'s version: what "nano-liquid zeolite" is, how to tell a good product before a '
            'trip when sober people feel little, and what "cleaned" means. Your post says ZeoCharge is sold "cleaned and '
            'remineralized", but not whether ozonating is what cleans the others.'),
     why=('Both of its sentences are short, and every way I join them pushes a neighbour below High. How you\'d say which '
          'zeolite to buy, and why most don\'t work, would teach me how to write the short connecting paragraphs the guide '
          'has between its longer ones.'),
     advice_note=('Edit it: which zeolite to get and why, in your words. If ozonating is what cleans the pores, saying so '
                  'here links it to the next paragraph.'),
     spans=[whole(P('B155'))])
