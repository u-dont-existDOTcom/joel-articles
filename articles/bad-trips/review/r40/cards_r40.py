# The card of round 40, read by build_r40.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After his message of 2026-11-14 22:08 UTC and turn 44's checks
# (../../humanize/h54-20261114/RESULTS.md).

BUILT = '2026-11-14'
H = 'https://www.pangram.com/history/'
H54 = BLOB + 'articles/bad-trips/humanize/h54-20261114/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-14 22:08 UTC: "didn\'t understand why you gave me no cards and quit working tho"')

INTRO = [
    'Round 40 (2026-11-14). In from your message of 22:08 UTC, each read Human High by itself: the 1967 sentence with its '
    'anxiety patients ([Human High 142](%sa61095ce-e1ca-41bc-bef6-f2817b00676e)); creatine and mango leaf tea as two new '
    'entries after Humic Acid, creatine in your own words with how to smell it ([Human High 95](%s6ed0ec03-0325-4700-8ac5-'
    'e1cdcb155899)); and the sniffer\'s last line saying its formula has both now, and what to buy without one ([Human High '
    '161](%sdcc37bc4-c8a3-4fef-a125-93603bdc2e1c)).' % (H, H, H),
    'My Brain Feels Damaged\'s evidence paragraph now says the excitotoxicity study was in rat brain cells in a dish, and its '
    'human-trial sentence opens on the people ("Some patients whose stroke came from a clot ...", "a handful of patients"): '
    '[Human High 137](%s392c6ee4-a6fa-4193-a894-0c99c6b46159), one window.' % H,
    'Card 1 is Chest Pain\'s evidence paragraph: my best try reads Human with a Medium window over my sentence, and nothing '
    'below High goes in, so the guide still has the old paragraph, which read AI ([every test](%sRESULTS.md)).' % H54,
]

card(id='TEACH-CHEST-EVID', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. Chest Pain: what the heart research adds to your angina story',
     reading=('In the first batch, the section read [AI Detected, 78%%](%sce00d5dc-1e58-4c03-9b82-628409d40764), this '
              'paragraph in the AI High window.' % H),
     tested=('Your round-39 way (how far the evidence goes, each finding in plain words, the rats\' timing): [AI Assisted, '
             '50%%](%s2c13fbe7-3693-4dcf-9726-cf6fea660532), every sentence AI-Assisted.\n\n'
             'The rats cut (a fresh reader: given for three days before a heart attack, they tell a friend whose pain has '
             'started nothing), the clot first: "Chest pain can come from a clot starting to block an artery, so it\'s a good '
             'sign that DMSO slows clotting. It did in mice, and in human platelets (the blood cells that start clots) in a '
             'dish, though that\'s only animal and lab-dish research so far." With your angina story: [Human, Medium and '
             'Low](%sdbfa1b8b-a9f1-44a3-8bf5-d06f6c7e9a74) over those two sentences.\n\n'
             'One sentence, no hedge tail or bracket: "Chest pain can come from a clot starting to block an artery, and '
             'DMSO slowed clotting in mice and in a dish of human platelets, the blood cells that start clots." With your '
             'story: [Human, Medium](%sb70b36a6-0b12-4e00-bf07-02e196b050ac) over that sentence, your story High.')
             % (H, H, H),
     sense=('A fresh reader said the rats given DMSO before a heart attack tell a friend nothing once the pain has started, '
            'and another asked how "the same way" points when your story was pain going away and the studies measured '
            'heart muscle and clotting.'),
     why=('Your angina story reads Human High; every way I say what the research adds after it reads below High. The guide '
          'has more of these: the cyproheptadine evidence in the Serotonin Syndrome steps and the MDMA studies. How you\'d '
          'say why the heart research backs your story, or whether it\'s needed at all, teaches me how to say those.'),
     advice_note=('Edit it: what the heart research adds, in your words, or cut it if your story and the call list are '
                  'enough. The clotting studies (mice, and human platelets in a dish) are the ones that bear on pain that has '
                  'already started; the rat study gave DMSO for three days before the heart attack. Your version goes in '
                  'whole, and I carry what it teaches to the other evidence paragraphs.'),
     spans=[whole(P('B123'))])
