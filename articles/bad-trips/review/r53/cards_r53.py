# The cards of round 53, read by build_r53.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 63: his round-52 answers are in the guide, each new text checked through the
# Pangram API first (humanize/h71-20261124/RESULTS.md).

BUILT = '2026-11-24'
H = 'https://www.pangram.com/history/'
R52 = BLOB + 'articles/bad-trips/review/r52/RESULTS-R52.md'
LESSON = BLOB + 'docs/lessons/2026-11-24-0126-bad-trips.md'

INTRO = [
    'Round 53 (2026-11-24). Round 52 is in the guide, each new text checked first through the Pangram API with your key: '
    'your MDMA paragraph with your sentence that women are most at risk and what it rests on '
    '([Human High, one window](%s09d08885-83ba-48db-a16a-cba1ff1e5b3a)), and a new paragraph after it from your dance '
    'answer, with the field vs lab note right after your suspicion of the pills, since your answer ties the two '
    '([Human High, one window](%s73794d7e-87cd-4f99-b07a-e2fc2f0188ef)). Each point of your comments has its fate in '
    '[the record](%s).' % (H, H, R52),
    'Main now counts a Medium window as work to do, as you said in the romance lane. Your MDMA paragraph\'s Medium window '
    '(my why-plain-water line) is gone; steps 6 and 8 under Act Now on SS still have theirs from last turn, and they are '
    'next.',
    'What I took from your answers is in the repo for every lane ([the lessons](%s)): the field and the lab both said, '
    'with how they differed; your experience kept as yours once you have seen the studies; a caveat said as what '
    'happens.' % LESSON,
]

card(id='MAPS-SETTING', type='question', advice='ask',
     title='1. Your dance paragraph: the MAPS trials',
     whose='his own: his DANCE-ENERGY answer of round 52, in the paragraph after his MDMA paragraph',
     question=('Your new paragraph says real MDMA "isn\'t the kind people want to dance on, which is why you don\'t see '
               'people in the MAPS trials of MDMA therapy saying "I NEED TO DANCE!" No, they\'re sitting there doing the '
               'therapy".\n'
               'What I found: in those sessions people settle into a comfortable position and are encouraged to put on '
               'eyeshades and listen to a set playlist, turned inward, and the trial\'s own write-up contrasts that with '
               'recreational use, which it describes as focused outward '
               '([the trial\'s therapy description](https://psychiatryonline.org/doi/suppl/10.1176/appi.ajp.20230681/suppl_file/appi.ajp.20230681.ds001.pdf)). '
               'One of my fresh readers, reading as someone going to a festival, said the same: the trials are a clinic '
               'setting, not a festival.\n'
               'a) Keep it as it is.\n'
               'b) Say the setting is part of it, in your words in the box.\n'
               'c) Cut the MAPS line and let "I can barely move" carry it.'),
     why='it is your argument, and the setting is a reason a reader could give that the studies I sent last round did not cover',
     stays='the paragraph as it is',
     advice_note='b: a reader who knows the trials will think of the setting, and saying it yourself keeps them with you',
     spans=[whole(P('R52-DANCE'))])
