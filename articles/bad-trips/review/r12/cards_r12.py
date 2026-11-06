# The cards of round 12, read by build_r12.py (which defines P, T, whole, span_of, replace_words, cut_block and card).
# P('B244') is the page block of GUIDE-SO-FAR-blocks.json's B244 (the guide after the repeats cut from Psychological First
# Aid). The checks are in articles/bad-trips/humanize/h12-20261106/RESULTS.md.

BUILT = '2026-11-06'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h12-20261106/'

INTRO = [
    'Round 12 (2026-11-06). Psychological First Aid now says each thing once. Under your 19:43 rule ("make the cuts '
    'regardless of pangram if it makes the guide read better") four repeats are cut. The room paragraph is gone: Why Bad '
    'Trips Tend to Happen says the room can be the problem, the Do and Don\'t lists cover light and music, Get One Human '
    'Anchor the crowd, Touch, Consent, and Compassion the touch. The two things only it said, the bathroom and someone '
    'they\'re wary of, are now in the Do list. The last paragraph is gone too: it pointed to the next two sections, and '
    'No Rash Actions and When the Trip Feels Amazing say the sleep and meaning parts in full. The reminder\'s last two '
    'sentences are gone, because the sitter\'s script in Get One Human Anchor says them in your post\'s words ("This is a '
    'wave. We don\'t have to solve your whole life right now."). And the intro line is gone: the triage app is the '
    'guide\'s first line and its picture is under the heading, and taking pressure off the person is For the Person '
    'Helping.',
    'One card: the practice case, which rewrites lines you approved in round 11. With it the whole section reads Mostly '
    'Human Written, every window Human.',
]

NEW_PRACTICE = ("If a practice like meditation or fasting brought this on, have them stop it now, since doing more of it only "
                "makes this stronger. There's no drug wearing off here, so it could be over soon or take a while.")

card(id='PFA-PRACTICE', type='repeat', advice='approve',
     title='The practice case, said once',
     reading=('With the practice part as the guide has it, the rest of the section reads AI too: the section\'s first '
              'half and these three paragraphs, [AI, 100%%](%sff2a6888-cd9c-49c3-9152-ec0cc6b5bb45).') % H,
     tested=('The whole section with this change: [Mostly Human Written](%secd2cd08-c8e7-4924-bd15-3155a3cbeb2a), every '
             'window Human (High, Medium, High, Medium, Low, Medium, Low). The same without its second sentence read '
             '[Human Written](%s2b5c21b4-dc7b-4505-b3b6-bda2e6981027), but that loses the one thing only this part says.')
            % (H, H),
     what=('The lead-in, the script and the food line become two sentences: have them stop the practice, and why; and '
           'that with no drug wearing off it could be over soon or take a while.'),
     why=('The script\'s "I\'m in an intense state" is the opener of the person\'s script in Get One Human Anchor ("I\'m in '
          'an intense psychedelic or altered state"), "my only job is to stay safe" is the guide\'s rule everywhere (No '
          'Rash Actions, Alone at 3 a.m.), and eating and warmth are in the Grounding Menu\'s Ordinary world and the '
          'aftercare\'s first 24 hours ("sleep, food, water, warmth"). What only this part said stays: stop the practice, '
          'because more of it makes the state stronger, and a practice state keeps no drug\'s schedule. Fresh readers also '
          'asked who says the script, and why the food line comes after the clock.'),
     stays=('Stopping the practice, the reason, meditation and fasting as the examples, and that it keeps no schedule; the '
            'reminder before it and everything above.'),
     deciding='Approve puts the two sentences in for the three paragraphs; Revise lets you change them first.',
     advice_note='Approve: it says the practice case once, and the section reads Human with it.',
     found_by='the say-it-once look across the guide (gate bad-trips-2026-11-06a), then Pangram beside the Human first half',
     receipt=[HD + 'RECEIPT-PRACTICE-V3.json', HD + 'TEST-practice-V3.receipt.json'],
     edits=[{'block': P('B244'), 'before': T(P('B244')), 'after': NEW_PRACTICE},
            cut_block(P('B245')), cut_block(P('B247'))],
     spans=[whole(P('B244')), whole(P('B245')), whole(P('B247'))])
