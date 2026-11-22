# The cards of round 38, read by build_r38.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After his round-37 answers and message (2026-11-12 16:47 and 16:48 UTC;
# ../r37/apply_r37.py, ../../humanize/h47-20261112/CALIBRATION.md, ../../humanize/h48-20261112/RESULTS.md).

BUILT = '2026-11-12'
H = 'https://www.pangram.com/history/'
H47 = BLOB + 'articles/bad-trips/humanize/h47-20261112/'
H48 = BLOB + 'articles/bad-trips/humanize/h48-20261112/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-12 14:45 UTC, card MEDICAL-HOW: "a"')

INTRO = [
    'Round 38 (2026-11-12). Round 37 is in: your Chest Pain version, whole, with magnesium chloride on the chest said only '
    'there. "These" stays in Serotonin Syndrome, and obvious corrections in your versions now go in without a card.',
    'Your five problems (what makes no sense, what a word points to, overlap, compression, a late payoff): I scored two '
    'fresh readers against what you flagged in seven of your fixes, and neither finds what you find ([the scores](%s'
    'CALIBRATION.md)). Both missed "Ask before touching", the one reading against your fixes found none of your four '
    'problems in my Chest Pain draft, and both flagged things you kept. So I check the shape myself: the linter now flags a '
    'list or a run of questions whose action comes after it.' % H47,
    'Your try 7, carried: Acute Medical\'s opening, rebuilt around what to do first and pointing to the Call medics list '
    'instead of saying its signs again, read [Human Written, High](%s97bf9589-ad17-4cee-835f-a51fe47956fd) and is in. My '
    'Brain Feels Damaged\'s checks with only the action moved read [AI Generated, 100%%](%s33a63991-6b34-445a-b107-'
    'c9b91f1906a1), so they are card 1 ([both tests](%sRESULTS.md)).' % (H, H, H48),
]

card(id='TEACH-BRAIN', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. My Brain Feels Damaged: the checks, and what to do when one shows a sign',
     reading=('The whole section in the first batch: [AI Detected, 65%%](%s4076db14-325a-4854-88b1-fc3c82da040a).' % H),
     tested=('Written against your fixes, read by a fresh reader after each of three drafts, with the action after the '
             'checks ("So if you see any of these signs, keep the DMSO going while someone calls medics."): [AI Generated, '
             '100%%](%s0eeefa6e-c72f-4ea6-b74e-fab541aca12f).\n\n'
             'Then only your Chest Pain move, the action before the checks ("If any check turns up a problem (or they\'re '
             'too out of it to answer you), keep the DMSO going while someone calls medics:"), the checks and the last line '
             'as they were: [AI Generated, 100%%](%s33a63991-6b34-445a-b107-c9b91f1906a1), AI High over the heading '
             'through the first check, Low, Medium over the checks, and High over the last line.') % (H, H),
     sense=('A fresh reader needed every sentence of my version. The reader against your fixes marked "Several of these '
            'checks look for recognized stroke warning signs." as opening on an authority, with the reader outside it.'),
     why=('Your move carried in Acute Medical, where I built the paragraph around it, and not here, where I set it onto '
          'checks that already read AI. A list of checks someone runs on a body is the shape I can\'t do yet; the steps '
          'under Suspected Serotonin Syndrome ("Do this immediately ...") and Active Seizure\'s first aid have it too.'),
     advice_note=('Edit it: how you\'d have someone check a friend whose brain feels damaged while the DMSO works, and '
                  'what to do when a check shows a sign, in your words. Keep each check (awake, breathing, temperature, '
                  'speech, the face, both arms, balance and walking, bladder or bowel control, a seizure, vomiting that '
                  'keeps coming back, a really bad headache, chest pain, vision), that several are recognized stroke '
                  'warning signs, that someone who can\'t answer hasn\'t passed, and what to do when every check passes but '
                  'the feeling stays. Your version goes in whole, and I carry what it teaches to the sections above and test '
                  'them.'),
     spans=[whole(P('B104'))])
