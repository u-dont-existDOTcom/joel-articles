# The cards of round 49, read by build_r49.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 59: his steps 5 and 6 are in, and his lesson (sense first, Pangram after);
# quiz 1 is my reading of my steps 1, 3, 4 and 7 before any Pangram check (../QUIZZES.json, ../QUIZ-SCORES.md).
import json as _json

BUILT = '2026-11-21'
H = 'https://www.pangram.com/history/'
H67 = BLOB + 'articles/bad-trips/humanize/h67-20261121/'
LESSON = BLOB + 'docs/lessons/2026-11-21-1557-bad-trips.md'
QZ = _json.loads((HERE.parent / 'QUIZZES.json').read_text(encoding='utf-8'))['quizzes'][0]

INTRO = [
    'Round 49 (2026-11-21). Your steps 5 and 6 are in the guide whole, with one obvious fix (the comma after "Since"), '
    'and so are "Coffee Cherry, Brain Too" and "Who to Contact" ([what went in](%sarticles/bad-trips/review/r48/RESULTS-R48.md)). '
    'Your lesson is in the repo for every lane: fix for sense until it reads right, and only then check '
    '([the lesson](%s)).' % (BLOB, LESSON),
    'I wrote steps 1, 3, 4, 7 and 8 your way and had fresh readers read them four times before any check. Then step 8 '
    'read Human High, and 1, 3, 4 and 7 read AI, with two of my five predictions right ([the checks](%sRESULTS.md)). '
    'So the first quiz you suggested is my next version of those four, with my reading of every sentence, before '
    'Pangram sees it.' % H67,
]

Q_LINES = []
for st in (1, 3, 4, 7):
    Q_LINES.append('Step %d' % st)
    for r in QZ['reading']:
        if r['step'] == st:
            Q_LINES.append('S%d: "%s"\nMy reading: %s, %s.' % (r['n'], r['s'], r['mine'], r['why']))
    Q_LINES.append('')

card(id='QUIZ-1', type='quiz', advice='ask',
     title='1. Quiz 1, no Pangram: my reading of my serotonin steps 1, 3, 4 and 7',
     question=('These are my steps 1, 3, 4 and 7 as I\'d now put them, written your way, read four times by fresh '
               'readers and not checked by Pangram, on purpose. Under each sentence is my reading of it. Score each '
               'reading right or wrong ("S3 wrong: ..."), and name any sentence I read as right that you\'d mark.\n\n'
               + '\n'.join(Q_LINES).strip()),
     why=('Your suggestion: "we should do some quizes for you without pangram first maybe". The last version showed you '
          'were right that I can\'t read my own writing yet: two of my five predictions were right, and the sentences I '
          'named as likeliest to read AI were half the ones that did. The fresh reader against your fixes can\'t stand '
          'in for you either: it marked the two sentences of step 1 that had read Human High. Your score of my reading '
          'is the teaching; [the scores are counted here](%sarticles/bad-trips/review/QUIZ-SCORES.md).' % BLOB),
     stays=('the four steps stay out of the guide, and out of Pangram, until your score; the guide keeps its eight steps '
            'with your 2, 5 and 6'),
     advice_note=('score each reading in the box, or rewrite any step yourself; after your score I fix what you mark '
                  'and only then check'),
     spans=[whole(P('B136', 0)), whole(P('B136', 2)), whole(P('B136', 3)), whole(P('B136', 6))])

_s8 = (HERE.parents[1] / 'humanize' / 'h67-20261121' / 'TEST-v6-ss8.txt').read_text(encoding='utf-8').strip()
card(id='SS-STEP8', type='plain', advice='approve',
     title='2. Act Now on SS: step 8, your way (reads Human High)',
     edits=[{'block': P('B136', 7), 'before': T(P('B136', 7)), 'after': _s8}],
     spans=[whole(P('B136', 7))],
     receipt='articles/bad-trips/humanize/h67-20261121/TEST-v6-ss8.receipt.json',
     tested='[Human Written, Human High 75](%s6f055cb9-2165-4807-bb0e-4aeff880d999), by itself.' % H,
     what=('step 8 opens on what the reader may reach for while they wait, this guide\'s other remedies, says why not '
           'niacin or DMSO, and turns to your magnesium line; the hospital line goes, and the magnesium line links to '
           'your MDMA: Magnesium Alarm section for the amounts'),
     why=('two needed reads found the reader does nothing with "Hospitals may use benzodiazepines, ...", and every fit '
          'reader asked why niacin and DMSO came up at all (they appear nowhere else in the steps)'),
     stays=('"niacin is unsafe with serotonin syndrome", your magnesium line with its condition, MDMA-related jaw tension '
            'and muscle activity'),
     ask_because=('meaning: the hospital line goes (it was in your guide); DMSO is named for brain injuries, seizures and '
                  'chest pain, where the guide uses it; and your magnesium line now says "fully alert and able to '
                  'swallow", like your step 2, where it said "fully alert"'),
     deciding='whether step 8 goes in as it reads here; Revise to change it',
     advice_note='approve')

card(id='SS-ASKED', type='question', advice='ask',
     title='3. What readers couldn\'t tell in the serotonin steps, yours and mine',
     question=('Fresh readers asked these in all four rounds, and I can\'t answer them from the guide:\n'
               'a) Step 2: where would a friend get cyproheptadine at night, and how much would they give?\n'
               'b) Step 6: what do "symptoms of lack of electrolytes" look like, and is a hypertonic drink something they '
               'would have at home?\n'
               'c) Step 8: why is niacin unsafe with serotonin syndrome? The step says it is, but not why.\n'
               'd) Step 8: your step 5 says the kidneys are at risk; magnesium leaves the body through the kidneys. Does '
               'the magnesium line still belong here, or does it need your kidney caution from MDMA: Magnesium Alarm?\n'
               'e) My step 1 (quiz 1) names Syrian rue as a harmala brew to stop, which it is; your stabilizers suggest Syrian rue '
               'oil. Is the oil a risk with serotonin syndrome too, and should step 8 say so?'),
     why=('each one stopped a reader at a step, and (c), (d) and (e) are about safety; only you can answer them, from '
          'what you know and have seen'),
     stays='the steps as the guide has them, with your 2, 5 and 6 as you wrote them',
     advice_note=('answer the ones you want in the steps, in a line each; I\'d answer (c), (d) and (e) at least'),
     spans=[whole(P('B136', 1)), whole(P('B136', 5)), whole(P('B136', 7))])

card(id='BOLD-56', type='question', advice='ask',
     title='4. Bold in the serotonin steps: your 5 and 6 have none',
     question=('Your step 2 starts with its act in bold ("If the person is fully alert and able to swallow, I would give '
               'cyproheptadine early"), and steps 1, 3, 4 and 7 bold their act the same way. Your 5 and 6 have no bold, '
               'so someone scanning the list in a hurry sees no act there.\n'
               'a) Bold "clear out the crowd and stop any arguing" in 5 and "small sips of an electrolyte drink" in 6.\n'
               'b) Leave 5 and 6 as they are.\n'
               'c) No bold in any step.'),
     why='the list is read in an emergency, often by scanning for what to do',
     stays='every word of steps 5 and 6, whatever you pick',
     advice_note='a',
     spans=[whole(P('B136', 4)), whole(P('B136', 5))])
