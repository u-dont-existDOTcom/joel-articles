# The cards of round 36, read by build_r36.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After his round-35 answers (2026-11-12 13:37 UTC; ../r35/apply_r35.py,
# ../../humanize/h45-20261112/RESULTS.md).

BUILT = '2026-11-12'
H = 'https://www.pangram.com/history/'
H45 = BLOB + 'articles/bad-trips/humanize/h45-20261112/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"')

INTRO = [
    'Round 36 (2026-11-12). Round 35 is in: your Recent Oral Toxic Ingestion version, whole, from your check ([Human, '
    'High](%s7e898f05-9c97-4f23-9513-cfca78be8905)), with the doubled "from" fixed. "My paragraph should not say anything '
    'that should be going in that above list": its warning signs moved into the Call medics list ("Dangerous overheating '
    '(not just regular sweating)" and a new line, "Severe insomnia"; trouble breathing was there already), and your '
    'paragraph now goes straight to "If for whatever reason you feel like this is more than you can handle, reach out." '
    'What your five tries teach is in the shared rules for every lane, with the sixth fix: the list as the questions you '
    'ask of the body, "requires different treatment from ... as would" for "is different from ... both are different '
    'from", "Slow and shallow" for "Slow, shallow", and every state kept.' % H,
    'Your moves, carried in my words to Acute Medical and Neurological Rescue and to Serotonin Syndrome\'s recognition '
    'part, read AI in both tries of each ([every try](%sRESULTS.md)). With round 34\'s four, that\'s eight tries in the '
    'medical part, all AI, while both versions you wrote there read Human, High. So card 1 asks how you want to do the '
    'rest of the medical part, and card 2 is the next teaching card.' % H45,
]

card(id='MEDICAL-HOW', type='question', advice='ask',
     title='1. The rest of the medical part: a whole version a round, or a line or two for each section?',
     question=('Nine sections of the medical part read AI in the first batch and haven\'t been fixed: Call medics for, Who '
               'to Contact, Acute Medical and Neurological Rescue (these two paragraphs), My Brain Feels Damaged, Active '
               'Seizure\'s first part, MDMA\'s jaw tension, Chest Pain, Recent Oral Toxic Ingestion\'s charcoal and poison '
               'control paragraphs, and Serotonin Syndrome. How each option would go:\n\n'
               'A: as now: one teaching card a round, and I carry what you do to the others and test them. Pro: you write '
               'one section a round. Con: my carries of your two medical versions read AI in all eight tries, so so far '
               'only the section you write turns Human.\n\n'
               'B (my pick): next round, a short box for each of those sections, for a line or two of your own there: what '
               'you\'ve seen, what you\'d do, or what you think of the standard advice. I build each section around what '
               'you write and test it. Pro: the whole part in a round or two, and it\'s how my fixes went Human in the remedies, '
               'where something you wrote was near (Nausea Smoothers, DMSO, the ocean water). Con: untried on clinical text; '
               'a section that still reads AI comes back to you as a teaching card.'),
     why=('Since round 34, every Human read in the medical part is a version you wrote, and none of my eight carries '
          'passed ([this round\'s four](%sRESULTS.md)). That changes how much a teaching round can do, so how to spend '
          'your time on the rest is your call.' % H45),
     stays='A, as now.',
     advice_note=('B, not sure: it\'s where my fixes have read Human so far, but I haven\'t tried it on clinical text.'),
     spans=[whole(P('B100')), whole(P('B76'))])

SS_NOW = [whole(P('B132'))] + [whole(i) for i in PALL('B133')] + [whole(P('B134'))]
card(id='TEACH-SS', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='2. Suspected Serotonin Syndrome: how to recognize it',
     reading=('The whole section in the first batch: [AI Generated, 100%%](%s4a5da2d5-a8b4-44f4-87d1-b86df0781db3).' % H),
     tested=('Your round-35 moves carried in my words, each checked by itself with its heading:\n\n'
             '1. The patterns as the questions you\'d ask of the body, the clinical term in brackets after each ("Are their '
             'muscles contracting and relaxing in a rhythm on their own, with nothing setting it off (spontaneous clonus)? '
             '..."): [AI Generated, 100%%](%s02fb701a-4fdd-44dc-b43b-c8cfba529429).\n\n'
             '2. One term for the whole list and the rest in plain words, the questions looser ("Are their muscles jerking '
             'in a rhythm by themselves, with nothing setting it off (that\'s called clonus)? ... Are they shaking, with '
             'reflexes that are way too brisk? ..."): [AI Generated, 100%%](%s38a740c3-c190-4716-b0f3-5db42b93a213).\n\n'
             'Acute Medical and Neurological Rescue\'s first two paragraphs, said the same way, read the same both times: '
             '[first](%seedc2eec-ceb0-493b-a41b-366d703ab11c), [second](%s49d3772f-dead-4b30-a92e-72051c07b5dd).')
            % (H, H, H, H),
     sense=('A fresh reader of my tries needed every pattern, the 38°C, "don\'t wait for all of them" and the call-for-help '
            'line, and found the name "the Hunter criteria" a source label the reader doesn\'t act on, so my tries leave it '
            'out. The guide\'s version names the five patterns by their clinical terms ("Spontaneous clonus", "Inducible '
            'clonus plus agitation or sweating", "Tremor plus hyperreflexia", ...), most of which a reader would have to '
            'look up in the moment.'),
     why=('Its shape, the signs that point to one condition, is the medical part\'s third common shape after the two you '
          'taught (when to get help; what to find out, then decide): Chest Pain\'s warning signs, the checks in My Brain '
          'Feels Damaged and the Call medics list share it. It\'s also the largest part of the guide that reads AI (the '
          'whole section, 512 words).'),
     advice_note=('Edit it: say how you\'d tell someone to recognize serotonin toxicity, in your words. Keep the five '
                  'patterns, each with its companion sign, and the 38°C (100.4°F); the last line\'s "dangerous", '
                  '"deserves" and "rigidity" are kept as warnings, so keep those words or say they can change. Whatever you '
                  'pick on card 1, your version goes in whole, and I test what it teaches on the sections above.'),
     spans=SS_NOW)
