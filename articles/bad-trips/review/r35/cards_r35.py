# The cards of round 35, read by build_r35.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After his round-34 answers (2026-11-11 23:57 UTC; ../r34/apply_r34.py,
# ../../humanize/h44-20261112/RESULTS.md).

BUILT = '2026-11-12'
H = 'https://www.pangram.com/history/'
H44 = BLOB + 'articles/bad-trips/humanize/h44-20261112/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"')

INTRO = [
    'Round 35 (2026-11-12). Round 34 is in: your Risk of Harm version, whole, from your check '
    '([Human, High](%saa15e193-4ea0-43f9-b851-a8aee94d62cc)), and Active Seizure\'s DMSO sentence as B. "Make sure this is '
    'only said once": the reasons to get urgent help now live in your paragraph, so the Call medics list\'s violence line, '
    'the helper\'s "Call for help early when safety is slipping.", and the harm part\'s list of when to call are cut, and '
    'the 911 line keeps only what your paragraph doesn\'t say (a weapon, a crime in progress). Your moves are in the shared '
    'rules for every lane as the sixth fix.' % H,
    'Two cards. Card 1 is the one overlap left, the body\'s warning signs, which your paragraph and the Call medics list '
    'both name. Card 2: your moves, carried in my words, read AI in every paragraph of Recent Oral Toxic Ingestion, so it '
    'is the next teaching card ([every try](%sRESULTS.md)).' % H44,
]

LIST_NOW = ('the Call medics list just above it has "Trouble breathing, blue or gray lips, or respiratory depression" and '
            '"Dangerous overheating, severe rigidity, or clonus with fever"')
card(id='BODY-ONCE', type='question', advice='ask', title='1. The body\'s warning signs: said in two places?',
     question=('Your Risk of Harm paragraph says "If their body is flashing warning signs like severe overheating (not just '
               'regular sweating), severe insomnia, or trouble breathing ... reach out", and %s. How each option would '
               'read:\n\n'
               'A (my pick): both stay as they are. Your paragraph says when to reach out at all; the list says which signs '
               'need an ambulance, with what your examples don\'t have (blue or gray lips, slow breathing, rigid muscles, '
               'jerking muscles with a fever). Pro: no safety sign is lost. Con: overheating and trouble breathing show up '
               'twice, a few lines apart.\n\n'
               'B: the list keeps only what your paragraph doesn\'t say: "Blue or gray lips, or respiratory depression" and '
               '"Severe rigidity, or clonus with fever". Pro: each sign is said once. Con: someone scanning the list for '
               'when to call medics won\'t find "trouble breathing" or "overheating" there.') % LIST_NOW,
     why=('You asked that the reasons to get urgent help be said only once. This is the one overlap I didn\'t cut myself, '
          'since cutting either side loses something a reader acts on in an emergency.'),
     stays='A, as it is.',
     advice_note='A, fairly sure: the list is where people look in an emergency, and your examples are why to reach out.',
     spans=[whole(P('R34-HARM-2'))])

card(id='TEACH-ORAL', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='2. Recent Oral Toxic Ingestion: what to do when someone swallowed too much',
     reading=('The whole section in the first batch: [AI Generated, 100%%](%sbb092688-faa8-46b1-9b14-b124951061eb).' % H),
     tested=('Your Risk of Harm moves carried in my words (the point and its bar first, plain words with the term in an '
             'aside, "etc." for the rest of the list, the reader\'s own judgment), each paragraph checked by itself:\n\n'
             '1. "Before you pick a remedy for an "overdose", find out what they actually swallowed, how much and when, '
             'because that word alone doesn\'t tell you much. Then look at what their body is doing. ...": [AI Generated, '
             '100%%](%s1ed58643-6c98-4d83-b332-e610947a03e1).\n\n'
             '2. The charcoal paragraph: [AI Generated, 100%%](%sb822edbf-12eb-484e-a059-e0fbbc2a4f65).\n\n'
             '3. The poison control paragraph: [AI Generated, 100%%](%sc4970058-7666-4483-ad93-79165d24f15a).\n\n'
             'The 911 line in Risk of Harm, said the same way, read the same: [AI Generated, '
             '100%%](%s45f31361-e5f6-4f1f-ace2-9a70cf644649).') % (H, H, H, H),
     sense=('A fresh reader of my version needed each step (what was swallowed, the body\'s state, when charcoal helps and '
            'when it\'s dangerous, when poison control is worth it) and flagged only the heading, the source link\'s label '
            'and my last line as ones a reader could lose. The guide\'s first paragraph asks the reader '
            'to sort the body into ten clinical states ("respiratory depression, stimulant toxicity, serotonin toxicity, '
            '... objective neurological dysfunction ..."), most of which they can\'t name in the moment.'),
     why=('Its shape, what to find out and what to do in a medical moment, said in clinical terms, is the medical part\'s '
          'other common shape: Acute Medical and Neurological Rescue, Suspected Serotonin Syndrome, Chest Pain\'s branch '
          'line and Active Seizure\'s first part all read AI in the first batch. Your Risk of Harm version taught me the '
          'firm list; this one is calmer, "find out, then decide", and my words in your frame still read AI.'),
     advice_note=('Edit it: say what you\'d tell someone whose friend swallowed too much of something, in your words. Keep '
                  'the steps that keep them safe (charcoal only when they can swallow safely, never when they\'re vomiting, '
                  'sedated or seizing), or tell me which can go. I\'ll carry what you do to the sections named above, test '
                  'each, and put the ones that read Human straight in.'),
     spans=[whole(P('B126'))])
