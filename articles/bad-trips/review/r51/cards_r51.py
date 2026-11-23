# The cards of round 51, read by build_r51.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 61: his round-50 answers are in the guide, each new text checked through the
# Pangram API with his key first (humanize/h69-20261123/RESULTS.md), and the guide's sections linked where it mentions
# them (humanize/h69-20261123/links/LINKS.md).
import json as _json

BUILT = '2026-11-23'
H = 'https://www.pangram.com/history/'
H69 = BLOB + 'articles/bad-trips/humanize/h69-20261123/'
LESSON = BLOB + 'docs/lessons/2026-11-23-1915-bad-trips.md'
QZ = [q for q in _json.loads((HERE.parent / 'QUIZZES.json').read_text(encoding='utf-8'))['quizzes'] if q['id'] == 'QUIZ-3'][0]
SODIUM = (HERE.parents[1] / 'humanize' / 'h69-20261123' / 'TEST-a7-sodium.txt').read_text(encoding='utf-8').strip()
NEW_SODIUM = SODIUM[SODIUM.index('Low sodium seems'):SODIUM.index(' The following indicators')]

INTRO = [
    'Round 51 (2026-11-23). Round 50 is in the guide, each new text checked first through the Pangram API with your key: '
    'step 2 with your dose lines ([Human High](%saa1d1224-4106-443a-8c09-f4cf6adab51f)), step 5 with your tapping '
    '([Human High](%sf5546979-88b9-4cba-8a15-2fef4678cac0)), step 6 from your notes ([Human High](%s275f1d65-23ae-437f-b483-15860d710f80)), '
    'step 7 with the seizure while waiting for the ambulance ([Human High](%se44eb897-a235-468f-adf2-4c9f150eb4ed)), step 8 '
    'with your DMSO answer and Epsom salt ([Human High](%s0bc23ace-94e6-4140-a8f2-4b247d0a8fdc)), your naloxone paragraph '
    'after the call list as you checked it, "No sleep for days", "acting on a delusion" and the ozone repeat cut. Every '
    'try, with what each window read, is in [the record](%sRESULTS.md).' % (H, H, H, H, H, H69),
    '"make sure that sections are linked to when mentioned or when they should be referenced": I read every mention of a '
    'section\'s subject outside its section and every "above", "below" and "branch" that points at one. 35 links went on '
    'words already there, no word changed, and each mention left as it is has its reason ([every mention](%slinks/LINKS.md)).' % H69,
    'What you taught on round 50 is in the repo for every lane ([the lessons](%s)): the number and the unit together, '
    '"12mg", now refused on any card I show you; no two sentences in a row opening on "And", now a linter rule; and the '
    'reader\'s doubt answered where it comes up, the state an act needs said first, what you\'re waiting for named, and '
    'the medicine named rather than one brand of it, in the brief my fresh readers read against.' % LESSON,
]

card(id='MDMA-SODIUM', type='question', advice='ask',
     title='1. Your MDMA section: who is most at risk of low sodium, and how to tell',
     whose='his own: his MDMA: Magnesium Alarm paragraph (round 42, MED-MDMA), with two sentences of mine from his round-50 note',
     question=('Your note on round 50: "it shows that MDMA can cause dangerous hyponatremia in something like 1/4 of '
               'people at a festival even when they take one average dose, with women being most at risk by far in this '
               'study, but not in other studies". What the study found ([van Dijken 2013](https://pubmed.ncbi.nlm.nih.gov/23476039/)): '
               'at one rave, 14%% of those who took MDMA had low sodium, about one in four women and 3%% of men, all of it '
               'mild. Your review\'s title says the rest: "Rare but relevant". So I\'d say one in four women, mildly, '
               'rather than one in four people, dangerously.\n'
               'Your "strong broth" holds up: the wilderness medicine guidelines replace salt by mouth with bouillon cubes '
               'or ramen seasoning in a little water, after stopping the water ([AAFP](https://www.aafp.org/pubs/afp/issues/2021/0215/p252.html)).\n'
               'Two sentences of mine after your water sentence, and your review linked on "sodium dropping too low" (the '
               'paragraph reads [Human High as one window](%scc7b7331-932e-420d-bb42-4a8201641f8d)):\n"%s"\n'
               'A fresh reader paused at your next sentence, with "vomiting won\'t stop" as a reason to call and salty food '
               '"if they\'re alert and not vomiting", unsure whether to feed them or call. It is two cases (worse confusion '
               'or headache without vomiting: salty food while you wait), and it reads Human High, so I left it.\n'
               'In, or not?' % (H, NEW_SODIUM)),
     why=('your note asked for it, the numbers differ from what you wrote (one in four women, mildly), and the words go into '
          'your paragraph'),
     stays='your paragraph as it is',
     advice_note='in',
     spans=[whole(P('B119'))])

card(id='SS-OIL', type='question', advice='ask',
     title='2. Step 8: what could harm, with almost none of the harmalas?',
     question=('Step 8 says: "I\'d also leave out this guide\'s Syrian rue oil for now: made at home it has almost none of '
               'the harmala alkaloids, but I couldn\'t find any research on it with MDMA, so it could help or harm here." '
               'Readers stop at "almost none" followed by "could help or harm": if there is almost none, what could harm? '
               'On round 49 you said "potentially helpful, potentially harmful with mdma", and if used, cautiously, raising '
               'the dose slowly. Which harm do you have in mind: a trace of the harmalas, which act like an MAOI, on top of '
               'MDMA; something else in the oil; or no known harm, only no research? Your answer decides the words, and '
               'whether step 8 still says to leave it out; I\'ll write them and check them.'),
     why='round 50 asked this as (d) and no answer came back; the line reads Human High in step 8, so this is for sense only',
     stays='the line as it is',
     advice_note='tell me the harm, and whether to leave the oil out',
     spans=[whole(P('B136', 7))])

Q_LINES = []
for r in QZ['reading']:
    # two readings said "your words" / "your line" of lines I wrote from his answers; the page says what they are
    why = r['why'].replace('your trade-off in your words', 'your trade-off').replace(
        'your line with the one word that changed', 'the round-49 line with the one word that changed')
    Q_LINES.append('S%d (%s): "%s"\nMy reading: %s, %s.' % (r['n'], r['step'], r['s'], r['mine'], why))
card(id='QUIZ-3', type='quiz', advice='ask',
     title='3. Quiz 3, optional: my reading of my first tries, before Pangram',
     question=('Only if you think the quiz is worth your time (my answer is in the chat). These are my first tries of this '
               'round\'s lines, read by three fresh readers and fixed, then read by me before any Pangram check, on '
               'purpose. The API checks changed several of them after, so the guide now has later versions; your score of '
               'these readings still tells me where my reading misses. Score each reading right or wrong ("S3 wrong: '
               '...").\n' + '\n'.join(Q_LINES)),
     why=('in quizzes 1 and 2 my "not sure" was right 8 times of 9 and my "reads right" 7 of 16 ([the scores](%s)); this '
          'shows whether that is changing' % (BLOB + 'articles/bad-trips/review/QUIZ-SCORES.md')),
     stays='nothing in the guide changes from this card',
     advice_note='score the readings, or skip the card',
     spans=[whole(P('B136', 4)), whole(P('B136', 5)), whole(P('B136', 7))])
