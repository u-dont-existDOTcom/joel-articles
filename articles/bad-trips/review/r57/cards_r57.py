# The cards of round 57, read by build_r57.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 67: his round-56 answers in the guide, and the kidney paragraph still AI High
# after two more methods (humanize/h75-20261124/RESULTS.md). No string here is %-formatted except where it ends in "% (...)".

BUILT = '2026-11-24'
H = 'https://www.pangram.com/history/'
R56 = BLOB + 'articles/bad-trips/review/r56/RESULTS-R56.md'
H75 = BLOB + 'articles/bad-trips/humanize/h75-20261124/RESULTS.md'
PANEL = BLOB + 'articles/bad-trips/humanize/h75-20261124/panel-b120/PANEL.md'
LEFT = BLOB + 'articles/bad-trips/humanize/h75-20261124/LEFT.md'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-14 22:08 UTC: "didn\'t understand why you gave me no cards and quit working tho"')

INTRO = [
    'Round 57 (2026-11-24). Both of your answers are in. The absorption study\'s link is out, and the sentence says your '
    'claim as what you know: "I use it mostly because it\'s what I know works best: it absorbs faster and better than any '
    'other form, so you can see how it\'s helping, usually within a minute." The paragraph reads '
    '[Human High in one window](' + H + 'f330e220-03a5-4821-9919-6427d4660e2a). Your second wife\'s paragraph ends "since '
    'potassium gets depleted once magnesium runs low" and reads '
    '[Human High in one window](' + H + 'e74a7e6b-7047-4e54-af54-64070d2b5879). Each point has its fate in '
    '[the record](' + R56 + ').',
    'Round 56\'s first question showed you a doubled percent sign after the 4. That was a slip in how I built the card, '
    'and the page tool now refuses one.',
    'One paragraph of the MDMA section still reads AI, the kidney one, and it is the card below. Every other paragraph '
    'of the section reads Human High by itself ([every check](' + H75 + ')). After it the work goes down '
    '[the list of what is left](' + LEFT + ').',
]

card(id='TEACH-KIDNEY', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. MDMA: Magnesium Alarm, the kidney paragraph: the last one in the section that reads AI',
     reading=('By itself, the paragraph as your post has it reads [AI Generated, High, in one window](' + H +
              'df3704bf-5de7-4067-aa11-f5b231f3e310).'),
     tested=('Five tries of mine by three methods, each keeping your five points in your order.\n\n'
             'Tries 1 and 2 (turn 65), the warnings reworded: [Mixed](' + H + '258a5b17-a2da-49d3-8da5-86655418be03), with '
             'your first two sentences Human Low and the rest AI, then [AI Generated](' + H +
             '230891b4-4860-4f70-aa2b-f80f19baecb2) after one clause changed.\n\n'
             'Try 3 (turn 66), from your text with the ways of your round-55 fixes: [AI Generated](' + H +
             'e2566e53-84ec-45c7-880d-87b8cbdcecda).\n\n'
             'Try 4 (this turn), a small fix for each of the four sentences two fresh readers agreed on: "... But they '
             'should be far more worried about the MDMA, since MDMA can cause acute kidney injury and rhabdomyolysis, on '
             'top of the overheating and dangerous electrolyte shifts. That makes kidney impairment a strong reason not to '
             'take MDMA, although once they\'ve taken it, they still shouldn\'t sit there with worsening jaw tension. I '
             'just wouldn\'t tell somebody with serious kidney impairment to copy my one-gram-per-minute approach blindly, '
             'since that\'s a higher-risk situation where they should get help sooner." [AI Generated](' + H +
             '7afc3e5b-d752-4d67-bf4c-41045d98fb45).\n\n'
             'Try 5, another writer\'s rewrite from those readers\' notes, in short plain statements: "... Kidney '
             'impairment is a strong reason to skip MDMA altogether. Once someone has taken it and their jaw tension is '
             'getting worse, the kidneys are no reason to sit there with it. Someone with serious kidney impairment should '
             'not copy my one-gram-per-minute approach blindly. Treat the situation as higher-risk and get help sooner." '
             '[AI Generated](' + H + 'f880b3a3-fb7c-4da4-828b-80b9f6bba5cf).'),
     sense=('Two fresh readers ([their notes](' + PANEL + ')) flagged four of its five sentences and said the same thing '
            'about the whole: a caution, a pivot, a list of risks, a contrast and a closing disclaimer, each given the same '
            'weight. Readers of the section also asked "get help sooner" than what, and one read "not a reason to sit '
            'there with worsening jaw tension" as "kidney problems are no reason to hold back magnesium", which your next '
            'sentence then takes back.'),
     why=('Rewording each sentence didn\'t move the reading, so what reads AI is the order of the points and their even '
          'weight. Changing that means choosing which point leads, and saying what you\'d have someone with bad kidneys do '
          'differently. I can\'t write that for you: it is a medical caution, and anything I added would be my advice '
          'under your name. How you\'d say a caution also teaches me the guide\'s other cautions.'),
     advice_note=('Edit it: what you\'d tell someone with impaired kidneys whose jaw is tensing on MDMA, in your words and '
                  'your order. If you can say what "get help sooner" means for them, or what you\'d change about the one '
                  'gram per minute, that answers both readers.'),
     spans=[whole(P('B120'))])
