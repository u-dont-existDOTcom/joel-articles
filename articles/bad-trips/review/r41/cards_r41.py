# The cards of round 41, read by build_r41.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After his round-40 export of 2026-11-19 00:52 UTC and turn 45's checks
# (../../humanize/h55-20261119/RESULTS.md).

BUILT = '2026-11-19'
H = 'https://www.pangram.com/history/'
H55 = BLOB + 'articles/bad-trips/humanize/h55-20261119/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-14 22:08 UTC: "didn\'t understand why you gave me no cards and quit working tho"')

INTRO = [
    'Round 41 (2026-11-19). Your Chest Pain version is in, whole, from your check [e8688033](%se8688033-21f1-4b0c-bc76-'
    'bdae42a7bdfd) (Human High 88), with its three studies linked on your words. What it taught (the limit that decides '
    'whether the findings bear on the reader goes first; the simple past; no abbreviation in three sentences in a row) is '
    'now a lesson, a ninth way in the read against your fixes, and two linter rules.' % H,
    'I carried it to three passages this turn ([every test](%sRESULTS.md)). Card 1 is the only one that reads Human High: '
    'My Brain Feels Damaged\'s bleed paragraph with your lines first. It comes to you because your lines move and two of '
    'mine change. Cards 2 and 3 are the MDMA paragraph and the cyproheptadine step, where every way I tried read AI.' % H55,
]

B106_NEW = ("If someone is worried about a bleed, I'd probably skip DMSO, but it depends on how severe their issue is. It's "
            "not a powerful blood thinner like heparin, unless maybe injected; it's basically a dietary blood thinner. I've "
            "never had any issues with bleeding too much from consuming DMSO, and never heard of it either, but if bleeding "
            "is already a medical issue I'd want to think about that more. They can feel better on DMSO with a clot or a "
            "bleed still there. So if any of the checks above fail, call medics right away, before the window for treating "
            "a stroke closes.")

card(id='B106-ORDER', type='plain', advice='approve',
     title='1. My Brain Feels Damaged: your bleed lines first, mine after in plain words',
     what=('Your three bleed lines ("If someone is worried about a bleed, I\'d probably skip DMSO, ..."), word for word, '
           'move to the start of the paragraph. My two sentences before them ("DMSO cannot identify whether the problem is a '
           'clot, a hemorrhage, low oxygen, an electrolyte crisis, or something else. The larger adjacent risk is losing a '
           'treatment window or missing a bleed because the symptoms improved enough to feel reassuring.") become two after '
           'them: "They can feel better on DMSO with a clot or a bleed still there. So if any of the checks above fail, call '
           'medics right away, before the window for treating a stroke closes."'),
     reading=('By itself as it stands: [AI Detected](%s7caaa2f9-b611-4d1f-931c-de6584ed18e0), my two sentences AI High (40 '
              'words) and your three lines Human High (75 words).' % H),
     tested=('[Human Written, 0%% AI, one window Human High](%sd7836ec9-5d7c-416d-ba7b-ffb6102f6bab) over all 109 words.' % H),
     why=('Your round-40 move: say first whether what follows bears on the reader\'s case. Here that\'s the bleed line, whether '
          'DMSO is for someone who may be bleeding at all, so it leads; mine follows with what to do about it (keep the '
          'stroke checks going even when DMSO makes them feel better). "Low oxygen, an electrolyte crisis" go: the checks '
          'above and the electrolytes in the section\'s opening carry them.'),
     stays='Your three lines, every word; the checks above it and the steps after it.',
     deciding=('Approve puts it in. Revise if you\'d say mine your way. The fresh readers asked two things of the bleed lines, '
               'for you to weigh, not changed: "how severe their issue is" is something a friend can\'t judge at home, and '
               '"I\'d probably skip DMSO" comes after the section has already had them take it.'),
     advice_note='Approve: it reads Human High by itself, and nothing a reader needs goes.',
     ask_because=('his own: his three bleed lines (his message of 2026-11-03 22:04 UTC, KEEP-AS-IS K4) move to the start of '
                  'the paragraph, and a caution says its point in other words: "The larger adjacent risk is losing a '
                  'treatment window or missing a bleed ..." becomes "call medics right away, before the window for treating '
                  'a stroke closes"'),
     whose='his own: his three bleed lines, from his message of 2026-11-03 22:04 UTC and round 2\'s card AN-Q3b (KEEP-AS-IS K4)',
     receipt='articles/bad-trips/humanize/h55-20261119/TEST-b106-c2.receipt.json',
     found_by='your round-40 lesson carried, and its check by itself',
     edits=[{'block': P('B106'), 'before': T(P('B106')), 'after': B106_NEW}],
     spans=[whole(P('B106'))])

card(id='TEACH-CYP', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='3. Serotonin Syndrome, step 2: cyproheptadine and how far its evidence goes',
     reading=('The whole Serotonin Syndrome section read [AI Generated, 100%%](%s4a5da2d5-a8b4-44f4-87d1-b86df0781db3), '
              'one AI window over all of it.' % H),
     tested=('Your round-40 shape, the limit first and said once: "If the person is fully alert and able to swallow, I '
             'would give cyproheptadine early, since it blocks serotonin receptors. So far, the evidence for it has only '
             'been case reports, and a recent review found them too weak to show that it works. I wouldn\'t wait to see '
             'whether it does before doing the other steps." [AI Detected, 79%%](%s33e3c66b-d1ae-4d23-b27a-36eaaee156da): '
             'the first sentence Human Low, the rest AI Medium.\n\n'
             'The study back after the limit, as your rats are: "So far, the evidence for it has only been case reports, '
             'where nobody could compare it against people who didn\'t get it. When doctors gave it to five patients, three '
             'had no signs left within two hours, and the other two took longer, so keep going with the other steps while '
             'you see whether it works." [AI Generated, 100%%](%sf65ebe7a-5080-4218-870a-59159cea92bb).' % (H, H)),
     sense=('Three fresh readers each time. The five-patient series read to them as proof it works, and its "second dose" '
            'as an instruction with no amount; one said the step never says how much to give. The guide has never given '
            'an amount.'),
     why=('Every wording I tried reads AI, and the step is the guide\'s one remedy for serotonin syndrome. How you\'d say '
          'what cyproheptadine is, how far its evidence goes and what to do meanwhile teaches me the evidence passages '
          'still in my words.'),
     advice_note=('Edit it: the step in your words. If you\'d give an amount, say it there; if the case series isn\'t '
                  'worth its line, cut it. Your version goes in whole, its two studies linked on your words.'),
     list_part=('only step 2 reads as evidence in my words; the other seven steps are instructions, and step 8 already says '
                'what hospitals do'),
     spans=[whole(P('B136', 1))])

card(id='TEACH-MDMA', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='2. MDMA: what else to do once the jaw tenses, and which signs mean medics',
     reading=('The MDMA section read [AI Detected, 96%%](%s08beb99e-4d7b-45b4-ac6f-32c9bfe3823a), this paragraph in its '
              'last AI High window, with your second wife\'s story.' % H),
     tested=('The two lists taken apart, the trial said as what decides it (a lot of plain water) and what to do (sip an '
             'electrolyte drink): [AI Detected, 87%%](%sadc38bd4-0651-498e-90be-4f06c7540ad8), the first line Human Low, '
             'the water line AI Medium, the three sign lines AI High.\n\n'
             'Each sign line built its own way: "A headache that gets worse and worse is how low sodium tends to show up, '
             'often with throwing up or confusion, and it\'s time to call medics. The same goes for muscles getting weaker '
             'and weaker, or palpitations where the heart skips beats, which can mean their potassium is low. And a seizure '
             'or collapse means the MDMA toxicity has become an emergency, so get medics there right away." [AI Generated, '
             '100%%](%s1ffa53a8-6c90-4b25-9ea5-9a1523a572cf).' % (H, H)),
     sense=('A fresh reader on MDMA\'s signs: a headache, throwing up, a pounding heart and tired muscles come with MDMA '
            'anyway, so only "keeps getting worse" tells them something\'s wrong, and they can\'t tell low potassium from an '
            'ordinary MDMA heartbeat. Another read "drink less water" as "restrict water", which could push toward '
            'overheating; the trial\'s point is plain water by the bottle, and the guide already says to sip.'),
     why=('Your story before it reads more human than anything I put after it. How you\'d say what to watch for and when '
          'to call medics teaches me the guide\'s other "what to watch for" paragraphs.'),
     advice_note=('Edit it: what to do after the jaw tenses and which signs mean medics, in your words. The trial (one '
                  'normal dose, low sodium only in those drinking freely) stays linked on your words; the kidney review '
                  'can move to the next paragraph\'s "acute kidney injury", which says the same.'),
     spans=[whole(P('B119'))])
