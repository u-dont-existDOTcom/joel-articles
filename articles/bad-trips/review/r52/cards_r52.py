# The cards of round 52, read by build_r52.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 62: his round-51 answers are in the guide, each new text checked through the
# Pangram API first, and the call list said plainly (humanize/h70-20261123/RESULTS.md).

BUILT = '2026-11-23'
H = 'https://www.pangram.com/history/'
H70 = BLOB + 'articles/bad-trips/humanize/h70-20261123/'
R51 = BLOB + 'articles/bad-trips/review/r51/RESULTS-R51.md'
LESSON = BLOB + 'docs/lessons/2026-11-23-2335-bad-trips.md'

INTRO = [
    'Round 52 (2026-11-23). Round 51 is in the guide, each new text checked first through the Pangram API with your key: '
    'step 6 with the chips and the magnesium on the skin ([Human](%s90be4010-7d11-4c2e-9ce6-59ccd81f22e6)), step 8 with '
    'DMSO first and the oil as a last resort ([Human](%s3ea237f3-fe3b-483f-a47b-80720d93ab03)), and your MDMA paragraph '
    'with no dancing, why plain water lowers sodium, and how much salt ([Human](%sc5f90479-96de-4fbd-b326-72bb2bc71a65)); '
    'none has a Low window. Each point of your comments has its fate in [the record](%s).' % (H, H, H, R51),
    'The Call Medics For list said every sign as what you see, the way your Active Seizure list does, every sign kept: '
    '[Human High as one window](%s20e18c3d-043c-43b2-ba62-411b433db4da), where it read AI High before.' % H,
    'What you taught on round 51 is in the repo for every lane ([the lessons](%s)): the things to do before the things '
    'not to do, one subject in one place, advice a person will actually take, a "So" that follows, and a study\'s number '
    'with what it rests on.' % LESSON,
]

card(id='WOMEN-RISK', type='question', advice='ask',
     title='1. Your MDMA section: do women get a sentence?',
     whose='his own: his MDMA: Magnesium Alarm paragraph (round 42), and his sentence from his QUIZ-3 answer of round 51',
     question=('You wrote that GPT found other reviews give men and women the same risk, and you\'d cut my sentence, or use '
               'yours: "Women are most at risk of this, based on results we have from one study done at raves, where '
               'sodium was low in 1/4 women vs only 3% of men."\n'
               'What I found: in a controlled study where people took MDMA and drank water, women\'s sodium did not drop '
               'more than men\'s ([Baggott 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4923534/)). Outside the lab it '
               'goes the other way: among MDMA cases reported to California\'s poison control, women had four times the '
               'odds of low sodium and higher odds of a coma from it ([Rosenson 2007](https://pubmed.ncbi.nlm.nih.gov/17084942)), '
               'and most of the severe and fatal cases in the reports are young women.\n'
               'a) Your sentence, after "so have them sip an electrolyte drink when they\'re thirsty instead", with the '
               'poison control numbers added as what it rests on.\n'
               'b) Leave it out.\n'
               'If (a), I\'ll write it from your sentence and check it before it goes in.'),
     why='it is your paragraph, and you leaned toward cutting it before seeing the poison control numbers',
     stays='your paragraph as it is, with no sentence on women',
     advice_note='a: the poison control numbers are about real cases, which is what a reader at a festival faces',
     spans=[whole(P('B119'))])

card(id='DANCE-ENERGY', type='question', advice='ask',
     title='2. Your MDMA section: why not to dance',
     whose='his own: his MDMA-SODIUM answer of round 51, with the line it put in his MDMA paragraph',
     question=('Your paragraph now says: "While it\'s natural to want to dance on MDMA, I\'d tell everyone not to dance at all, '
               'since dancing makes the heat and the sweat that drain their salt." You also wrote: "real mdma doesn\'t give '
               'you any energy to dance so i\'m highly suspicious that contains amphetamines or it\'s not real mdma maybe '
               '6apb".\n'
               'What I found: in controlled studies of pure MDMA, people\'s ratings of their energy go up with the dose '
               '([Kolbrich 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2587205)), and MDMA shows "some effects commonly '
               'associated with stimulant drugs" ([Harris 2002](https://pubmed.ncbi.nlm.nih.gov/12172693/)). So I left your '
               'reason about the pills out of the guide for now.\n'
               'a) Keep the line as it is, with the heat and the sweat as the reason.\n'
               'b) Add your suspicion as yours, for example: "In my experience pure MDMA doesn\'t make me want to dance, so a '
               'pill that does may have something else in it." I\'d check it before it goes in.\n'
               'c) Something else: say it in the box.'),
     why='it is your belief, and the studies I found say pure MDMA does raise energy, so it is your call how to say it',
     stays='the line as it is',
     advice_note='a, or b said as your own experience',
     spans=[whole(P('B119'))])
