# The cards of round 50, read by build_r50.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 60: his round-49 steps and answers are in, quiz 1 is scored, and the
# medical part was read for advice that makes no sense in the moment (humanize/h68-20261122/RESULTS.md).
import json as _json

BUILT = '2026-11-22'
H = 'https://www.pangram.com/history/'
H68 = BLOB + 'articles/bad-trips/humanize/h68-20261122/'
LESSON = BLOB + 'docs/lessons/2026-11-22-1721-bad-trips.md'
QZ = [q for q in _json.loads((HERE.parent / 'QUIZZES.json').read_text(encoding='utf-8'))['quizzes'] if q['id'] == 'QUIZ-2'][0]
A4 = (HERE.parents[1] / 'humanize' / 'h68-20261122')
NALOX = A4.joinpath('TEST-a4-nalox.txt').read_text(encoding='utf-8').split('\n\n')[1].strip()
SS6_MINE = A4.joinpath('DRAFT-ss6.md').read_text(encoding='utf-8').strip()
SS6_HIS = A4.joinpath('DRAFT-ss6-his.md').read_text(encoding='utf-8').strip()

INTRO = [
    'Round 50 (2026-11-22). Round 49 is in the guide: your steps 1, 3, 4 and 7 as you sent them, with the CDC linked in 7; '
    'your step 8 with your answers (c), (d) and (e) in it ([Human High](%sa3c02dd9-5907-4ead-a975-1deb4f58e039)), and '
    'step 2 with your answer (a) ([Human High](%s9e72f856-d889-487a-9fbe-179b6a87a271)). Quiz 1 is scored: my "not sure" '
    'was right 4 times of 4 and my "reads right" 5 of 12 ([the scores](%sarticles/bad-trips/review/QUIZ-SCORES.md)). '
    'What you taught with it is in the repo for every lane, and from today my sense receipt refuses a sentence whose tie '
    'to the one before comes after its first five words ([the lessons](%s)).' % (H, H, BLOB, LESSON),
    '"i hope we don\'t have other nonsensical stuff in this guide": four fresh readers went through the whole medical '
    'part, asking of each line whether a helper could do it in that moment and whether it is right for that case. They '
    'flagged 122 lines, and each one has its fate in [the record](%sRESULTS.md): 48 are your own remedies and '
    'experience, said in the first person; 37 you decided in an earlier round, named there; 14 I left, with why; 5 were '
    'a reader who saw one part of the guide only; 4 are facts I checked against their sources today; 5 are your '
    'round-49 answers. The 9 that need you are on this page, with what I found.' % H68,
    '"make sure we are not repeating the same stuff over and over": I read the whole guide for lines that say the same '
    'thing twice. Few do, and most on purpose (card 6). In the steps, your hypertonic drink points to the signs in MDMA: '
    'Magnesium Alarm instead of saying them again.',
]

card(id='ADVICE-CALL', type='question', advice='ask',
     title='1. Call Medics For and the lines after it: insomnia, "acting delusional", and naloxone',
     whose=('his own: "severe insomnia" and "Another cue to get help is if they start acting delusional" are lines he '
            'wrote (his Risk of Harm paragraph and his If Someone Might Get Hurt paragraph)'),
     question=('a) "Severe insomnia" came into this list from your paragraph in round 35 ("my paragraph should not say '
               'anything that should be going in that above list"). There it was a reason to reach out; here it calls an '
               'ambulance, and a night without sleep is usual after MDMA or a trip, so readers took it for a sign they\'d '
               'always see. Did you mean days without sleep? Then it would read "No sleep for days", or it could go back '
               'to reaching out.\n'
               'b) "Another cue to get help is if they start acting delusional." Most bad trips bring delusions, so readers '
               'took it as "always get help". Did you mean acting on one (heading out the door because of it, as in the '
               'sentence before)?\n'
               'c) The guide never names naloxone. Fentanyl has turned up in pills sold as MDMA ([14 of 22 samples at one '
               'festival](https://pmc.ncbi.nlm.nih.gov/articles/PMC10698886/)), and naloxone, sold over the counter in '
               'the US, reverses an opioid overdose ([CDC](https://www.cdc.gov/stop-overdose/naloxone-faq/)); it does '
               'nothing to someone without opioids in them and wears off in 30 to 90 minutes, sooner than some opioids '
               '([Jed Foundation](https://jedfoundation.org/resource/naloxone-101-how-to-use-it-to-save-lives-from-opioid-'
               'overdose/)). Mine, as a paragraph after this list '
               '(quiz 2, card 3, scores my reading of it):\n"%s"\nIn, or not?' % NALOX),
     why=('the readers marked these as the lines a helper couldn\'t act on in the moment; (c) is a safety point the guide '
          'is missing'),
     stays='the list and both lines as they are',
     advice_note='a) days without sleep; b) acting on one; c) in',
     spans=[whole(P('B94', 4)), whole(P('B276'))])

card(id='ADVICE-ORAL', type='question', advice='ask',
     title='2. Swallowed Too Much?: slow breathing, or a slow heartbeat, with iboga?',
     whose=('his own: "Slow breathing is normal with iboga, but if cardiac irregularities come along with it, that\'s an '
            'extra danger sign." is from his version of this paragraph (round 35)'),
     question=('"Slow breathing is normal with iboga, but if cardiac irregularities come along with it, that\'s an extra '
               'danger sign." Ibogaine is known to slow the heart, not the breathing: in [a 2022 study](https://pmc.ncbi.'
               'nlm.nih.gov/articles/PMC9292417/) it lowered heart rate and blood pressure, and the deaths linked to it '
               'come from heart rhythm problems ([review](https://pubmed.ncbi.nlm.nih.gov/26807959/)). I found nothing on '
               'slow breathing. Did you mean "A slow heartbeat is normal with iboga, but if it comes with an irregular one, '
               'that\'s an extra danger sign"? Or is slow breathing something you have seen with it?'),
     why=('a helper reading "slow breathing is normal" may wait on the one sign the list above says to call for'),
     stays='the paragraph as it is',
     advice_note='the heartbeat, if that is what you meant',
     spans=[whole(P('B126'))])

Q_LINES = []
_where = None
for r in QZ['reading']:
    if r['step'] != _where:
        _where = r['step']
        Q_LINES.append('' if not Q_LINES else '')
        Q_LINES.append(_where[0].upper() + _where[1:])
    Q_LINES.append('S%d: "%s"\nMy reading: %s, %s.' % (r['n'], r['s'], r['mine'], r['why']))

card(id='QUIZ-2', type='quiz', advice='ask',
     title='3. Quiz 2, no Pangram: my reading of my new lines on this page',
     question=('These are the lines I wrote for this page: the dose in step 2, step 6 as I\'d pick it (card 4), the '
               'seizure in step 7 (card 5) and the naloxone paragraph (card 1). Three fresh readers read them once and I '
               'answered their marks; Pangram hasn\'t seen them, on purpose. Under each is my reading. Score each '
               'reading right or wrong ("S3 wrong: ..."), and name any sentence I read as right that you\'d mark.\n'
               + '\n'.join(Q_LINES).strip()),
     why=('quiz 1 showed my "reads right" is where I miss things (5 of 12 right), so this time I ran your four questions on '
          'each sentence before calling it: a tie at the start, the payoff early, each part following from the one before, '
          'and advice that makes sense in the moment ([the readers\' marks and what I changed](%sRESULTS.md#my-new-lines-quiz-2-not-checked-on-purpose)).' % H68),
     stays='none of these lines is in the guide or in Pangram until your score; after it I fix what you mark, then check',
     advice_note='score each reading, or rewrite any line yourself',
     spans=[whole(P('B136', 1)), whole(P('B136', 5)), whole(P('B136', 6))])

card(id='SS-DRINK', type='question', advice='ask',
     title='4. Step 6: your hypertonic drink in bold, and two things in it',
     question=('Your answer (b): "a hypertonic drink could be as simple as throwing in a bit extra salt, potassium and '
               'magnesium, or even just a salty potato soup with some epsom salt thrown in", with the bold you asked for. '
               'The signs it is for are in your MDMA: Magnesium Alarm (confusion or headache that worsens, vomiting that '
               'won\'t stop, muscles getting weaker), so step 6 points there instead of saying them again. Two things in '
               'it I\'d change, and one I\'d leave:\n'
               'a) Potassium. Serotonin syndrome can break muscle down into the blood (your step 5), broken muscle '
               'releases potassium, and too much of it can stop the heart ([StatPearls](https://www.ncbi.nlm.nih.gov/books/'
               'NBK448168/), [a review](https://pubmed.ncbi.nlm.nih.gov/19046720/)). It can also run low after MDMA, as '
               'your MDMA section says, and only a blood test tells which. I\'d add none and leave it to the ER.\n'
               'b) Epsom salt is magnesium sulfate, the laxative kind your MDMA section steers away from ("less likely to '
               'cause diarrhea than ... forms deliberately used as laxatives"), and diarrhea dries them out more. Potatoes '
               'are also high in potassium. I\'d use your magnesium chloride flakes, in broth.\n'
               'c) Magnesium is then in step 6\'s drink and in step 8; the drink\'s is a little, so I\'d leave both.\n\n'
               '1) As you put it:\n"%s"\n\n2) Mine, without potassium or Epsom salt (quiz 2, S2 to S4):\n"%s"'
               % (SS6_HIS, SS6_MINE)),
     why=('(a) is a safety point; (b) keeps step 6 from contradicting your MDMA section; and your answer asked whether the '
          'guide had said this before: it had, in MDMA: Magnesium Alarm, which step 6 now points to'),
     stays='step 6 as it is in the guide',
     advice_note='2',
     spans=[whole(P('B136', 5))])

card(id='SS-ASKED-2', type='question', advice='ask',
     title='5. The serotonin steps: what readers still couldn\'t tell',
     card_after=P('B136', 7),
     whose=('his own: steps 5, 7 and 8 are his round-48 and round-49 versions (the foot flexing, "the seizure", the '
            'Syrian rue oil line from his answer e)'),
     question=('a) Step 7: "Keep track of how their breathing is doing, as that\'s one of the main indicators of how '
               'dangerous the seizure is" comes before any seizure in the steps, so readers took "the seizure" for one '
               'they\'d missed. Mine (quiz 2, S5 and S6): "And if they have a seizure while you wait, do the first aid in '
               'Active Seizure above. Then I\'d tell the medics whether their breathing got better or worse afterward, '
               'since the CDC counts trouble breathing after a seizure as a danger sign." Or just "a seizure, if they have '
               'one".\n'
               'b) Step 2, the dose. The Maryland Poison Center\'s adult dose is 12 mg, then 2 mg every two hours while '
               'the symptoms last, up to 32 mg a day ([their sheet](https://www.mdpoison.com/media/SOP/mdpoisoncom/'
               'healthcareprofessionals/antidote-facts/Cyproheptadine%20Antidote%20Facts.pdf)). The ambulance comes long '
               'before a second dose, so mine gives the first only (quiz 2, S1). In, or leave dosing to whoever prescribes '
               'it?\n'
               'c) Step 8 gives niacin\'s reason for "I wouldn\'t use either one here", but not DMSO\'s. What\'s the reason '
               'for DMSO? (The guide before said only "DMSO is also not part of this branch.")\n'
               'd) Step 8, the oil: readers stop at "almost none of the harmala alkaloids" followed by "could help or '
               'harm": if there\'s almost none, what could harm? Your answer was "potentially helpful, potentially harmful '
               'with mdma", and if used, cautiously, raising the dose slowly. Say what could harm (a trace of an MAOI '
               'with MDMA?), or put it your way: "if you use it, start with a little and go up slowly"?\n'
               'e) Step 5: "fidgeting (especially of the calf muscle, flexing the feet)". Flexing the foot up is how '
               'doctors set off clonus, the muscle jerking in your Hunter list ([Cleveland Clinic Journal of Medicine]'
               '(https://www.ccjm.org/content/83/11/810)), and every jerk makes heat. Keep the feet, or fidgeting with the '
               'hands?'),
     why='each stopped a reader at a step; (a), (d) and (e) can change what a helper does',
     stays='the steps as the guide has them',
     advice_note='a) mine; b) in; c) your reason; d) say what could harm; e) the hands',
     spans=[whole(P('B136', 1)), whole(P('B136', 4)), whole(P('B136', 6)), whole(P('B136', 7))])

card(id='REPEATS', type='question', advice='ask',
     title='6. Said twice: the guide read for repeats',
     whose=('his own: the shungite paragraphs are his, from the start'),
     question=('I read every line of the guide against every other for the same thing said twice. Four pairs came up:\n'
               '- "train before you need it, sending love to a frightening image ..." is in Demons, Jinn, and Entities and in '
               'Plan a Trip or Ceremony, where you put it in round 31; it stays.\n'
               '- "This feeling is allowed to move through" is in Helping? Anchor, Not Guru from the start and in Alone at '
               '3 a.m., where you put it in round 31; it stays.\n'
               '- One hand on the heart and one on the solar plexus is in the Grounding Menu and in its own section, the '
               'menu pointing to it; it stays.\n'
               '- Here: "I mean the water after active ozonation has ended and residual ozone has dissipated" and, two '
               'paragraphs later, "No ozone gas was present; this was contact with the water after ozonation had ended '
               'and the residual ozone had dissipated." Cut the second to "No ozone gas was present, only the water."?'),
     why=('your "make sure we are not repeating the same stuff over and over": the medical part repeats less than it '
          'points, and the steps now point to MDMA: Magnesium Alarm and Active Seizure instead of saying them again'),
     stays='the paragraph as it is',
     advice_note='cut it',
     spans=[whole(P('B196'))])
