# The cards of round 54, read by build_r54.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 64: his round-53 answer is in the guide, and steps 6 and 8 have no Medium
# window left (humanize/h72-20261124/RESULTS.md).

BUILT = '2026-11-24'
H = 'https://www.pangram.com/history/'
R53 = BLOB + 'articles/bad-trips/review/r53/RESULTS-R53.md'
LESSON = BLOB + 'docs/lessons/2026-11-24-1420-bad-trips.md'

INTRO = [
    'Round 54 (2026-11-24). Your round-53 answer is in: the setting isn\'t what decides, so the sentence goes where it is '
    'the evidence for your suspicion of the pills, right after "I can barely move", couch lock '
    '([Human High, one window](%scbfb1b52-ceb9-4daa-99a9-d5d1793ac726)). Each point of your answer has its fate in '
    '[the record](%s).' % (H, R53),
    'Steps 6 and 8 under Act Now on SS have no Medium window left: step 6 '
    '([Human High, one window](%s912c56b9-750f-46bb-b953-b1432b6e5d0f)) and step 8 '
    '([Human High, one window](%se124ac32-130a-4d69-9315-0a04fbd514e2)). Step 8 took one small fix: its niacin line said '
    '"at the doses used to end a trip" in a sentence that had already said "for ending a trip", and "at that dose" took '
    'both of its Medium windows. Your oil and brew sentence never changed.' % (H, H),
    'Step 6 cost you half a sentence, which is the question below. What I took from your answer is in the repo for every '
    'lane ([the lessons](%s)).' % LESSON,
]

card(id='POTASSIUM-DRAIN', type='question', advice='ask',
     title='1. Your step 6: the second half of your potassium note',
     whose='his own: his QUIZ-3 answer of round 51, on high potassium bringing on vomiting and diarrhea',
     question=('You wrote: "with high potassium they are more likely to have vomiting and diarrhea (which then causes '
               'hypokalemia as it removes potassium)". Step 6 said that as "High potassium also brings on vomiting and '
               'diarrhea, which then drain it again, so if those start, I\'d stop the chips", and that sentence was the '
               'step\'s Medium window.\n'
               'What the three fresh readers found, each in the same place: the draining says the friend is losing '
               'potassium, which reads as a reason to give more chips, not to stop them. So the line now says the act '
               'first and leaves the draining out: "So if they start vomiting or get diarrhea, I\'d stop the chips, since '
               'too much potassium brings those on and the chips have to stop either way while they\'re being sick." The '
               'step reads Human High in one window that way.\n'
               'a) Leave it out, since the step already says potassium can be running high as well as low.\n'
               'b) Put it back, in your words in the box, and I\'ll check it before it goes in.\n'
               'c) Say it where the swing is, in the sentence before.'),
     why='it is your point, and half of it came out to clear the Medium window',
     stays='step 6 as it now reads, without the draining',
     advice_note='a: the reader does the same thing either way, and the sentence before already says potassium can go either way',
     spans=[whole(P('B136', 5))])
