# The cards of round 37, read by build_r37.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After his round-36 answers (2026-11-12 14:45 UTC; ../r36/apply_r36.py,
# ../../humanize/h46-20261112/RESULTS.md).

BUILT = '2026-11-12'
H = 'https://www.pangram.com/history/'
H46 = BLOB + 'articles/bad-trips/humanize/h46-20261112/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-12 14:45 UTC, card MEDICAL-HOW: "a"')

INTRO = [
    'Round 37 (2026-11-12). Round 36 is in: your Serotonin Syndrome version, whole, with "the these" made "these" (as it '
    'goes in: [Human Written, the heading and first sentence Medium, the rest High](%s0dfe5d10-9de1-43ad-8062-4dedd8b8fea2); '
    'your exact text read High throughout, so card 2 asks which you want). And "a": one teaching card a round, as now.' % H,
    'Your question, how I write against how you fix: I read all 112 of your fixes in six lanes against the texts they '
    'replaced, and your eight tries step by step ([what you change, counted, what flipped Pangram in your words, and the '
    'eight ways my drafts differ](%shis-fixes/HOW-HE-FIXES.md)). Every text of mine now goes to a fresh reader with those '
    'eight differences before any check, and each sentence they mark changes first. Written that way, Chest Pain\'s branch '
    'paragraph and My Brain Feels Damaged\'s checks still read AI ([every try](%sRESULTS.md)), so card 1 is the next '
    'teaching card.' % (H46, H46),
]

card(id='TEACH-CHEST', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. Chest Pain: mild or serious, and what to do with each',
     reading=('The whole section in the first batch: [AI Detected, 78%%](%sce00d5dc-1e58-4c03-9b82-628409d40764), this '
              'paragraph in its AI High window.' % H),
     tested=('Written against your fixes, read by a fresh reader with the eight differences after each of three drafts and '
             'changed every time: "For chest pain that\'s mild and familiar, I\'d just use DMSO, as long as it\'s holding '
             'steady and they\'re fully alert. It\'s more serious if: ... Hard movement brought it on, like dancing or '
             'climbing stairs. ... When you\'re unsure which kind it is, treat it as the serious kind.": [AI Generated, '
             '100%%](%s2f1b6aa2-e672-4b5f-aeb4-6479ccf56025) (AI windows at High and Medium).\n\n'
             'My Brain Feels Damaged\'s checks, written the same way, read the same: [AI Generated, '
             '100%%](%s0eeefa6e-c72f-4ea6-b74e-fab541aca12f) (AI windows at Medium, High and Low).') % (H, H),
     sense=('A fresh reader of my version needed every sentence, "if the pain fades, still let the medics check them" '
            'among them, since DMSO can mask pain. The guide\'s paragraph sets the two kinds against each other ("Mild, '
            'familiar, non-progressive discomfort in a fully alert person is different from new, severe, persistent, '
            'worsening, radiating, or exertional pain--or pain with breathlessness, sweating, faintness, neurological '
            'changes, or collapse") and calls the serious one "the second branch".'),
     why=('Its shape, two cases, how to tell them apart and what to do when you can\'t, is one none of your lessons has had '
          'yet: you taught when to get help (Risk of Harm), what to find out (Recent Oral Toxic Ingestion) and which signs '
          'count (Serotonin Syndrome). Acute Medical and Neurological Rescue\'s opening (calm the trip where they are, or '
          'call) has it too.'),
     advice_note=('Edit it: say how you\'d tell mild chest pain from the serious kind, and what to do with each, in your '
                  'words. Keep each sign of the serious kind (new, severe, persistent, worsening, spreading, brought on by '
                  'effort, or with breathlessness, sweating, faintness, neurological changes or collapse), what to do when '
                  'unsure, and that DMSO can block pain. Your version goes in whole, and I test what it teaches on the '
                  'sections above.'),
     spans=[whole(P('B124'))])

THESE = 'One or more of these patterns makes the diagnosis more likely:'
card(id='SS-THESE', type='question', advice='ask', title='2. Serotonin Syndrome: "the these" fixed, or your exact text?',
     question=('Your version says "One or more of the these patterns makes the diagnosis more likely:". How each option '
               'would read:\n\n'
               'A (my pick): "%s", as the guide has it now: [Human Written, the heading and first sentence Medium, the rest '
               'High](%s0dfe5d10-9de1-43ad-8062-4dedd8b8fea2). Pro: no doubled word for a reader to trip on. Con: the first '
               'sentence reads Medium.\n\n'
               'B: your exact text, "the these" kept: [Human Written, High throughout](%s9e32c090-a4bd-4353-abcc-f56393b6b644). '
               'Pro: High everywhere. Con: a reader sees "the these".') % (THESE, H, H),
     why='It is your version, and fixing the doubled word lowers its first sentence from High to Medium.',
     stays='A, as it is now.',
     advice_note=('A, fairly sure: a reader trips on "the these", and a Medium window is fine by your rule (no Low window, '
                  'most of the text High).'),
     spans=[span_of(P('B132'), THESE)])
