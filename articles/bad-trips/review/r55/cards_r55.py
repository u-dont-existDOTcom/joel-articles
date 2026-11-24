# The cards of round 55, read by build_r55.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 65: his round-54 answer recorded, and five paragraphs of MDMA: Magnesium
# Alarm tried through the Pangram API (humanize/h73-20261124/RESULTS.md).

BUILT = '2026-11-24'
H = 'https://www.pangram.com/history/'
R54 = BLOB + 'articles/bad-trips/review/r54/RESULTS-R54.md'
H73 = BLOB + 'articles/bad-trips/humanize/h73-20261124/RESULTS.md'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-14 22:08 UTC: "didn\'t understand why you gave me no cards and quit working tho"')

INTRO = [
    'Round 55 (2026-11-24). Your (a) on round 54 is in: the draining clause stays out of step 6, and it is on the guide\'s '
    'list of cuts you meant, so nothing puts it back ([the record](%s)).' % R54,
    'Then the MDMA section\'s paragraphs that still read AI from its check of 2026-11-11. The one with your amounts now '
    'reads [Human High, one window](%s8afe7ed1-f282-4c1f-b49d-79eab672623a), with every dose word for word. The other four '
    'read AI in both of my tries (every check is in [the record](%s)), so the guide keeps them as your post had them for '
    'now. Two of them are yours to say, which is what the cards below ask.' % (H, H73),
]

card(id='TEACH-JAW', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. MDMA: Magnesium Alarm, the first paragraph: what a tense jaw means, and what you have seen',
     reading=('The section read [AI Detected, 96%%](%s08beb99e-4d7b-45b4-ac6f-32c9bfe3823a) on 2026-11-11, this paragraph '
              'in its first window, AI High.' % H),
     tested=('Try 1, your claim kept and the evidence said as what you\'ve seen: "With MDMA, I treat meaningful jaw tension '
             'as the earliest warning that the body needs more magnesium. Nobody has tested this in a trial that I know '
             'of, so it\'s from what I\'ve seen again and again: everyone I know who took enough magnesium chloride for the '
             'jaw tension to fully release avoided the other complications I\'ve seen in people who let the tension keep '
             'going." [AI Generated](%s9e4a7d71-5ad6-4947-ad6f-b59269f9af9d): the first sentence AI Low, the rest AI '
             'High.\n\n'
             'Try 2, the long sentence split and its mirror taken out: "... so it\'s from what I\'ve seen myself. Everyone I '
             'know who took enough magnesium chloride for the jaw tension to fully release avoided the other complications '
             'that showed up when people let the tension keep going." [AI Generated](%s25bc9042-d058-40dd-b052-f7c2c6ab660f): '
             'AI Medium, then AI High.' % (H, H)),
     sense=('Fresh readers asked what "meaningful" jaw tension is, when nearly everyone\'s jaw clenches on MDMA, and which '
            '"other complications" taking enough magnesium spared people. I couldn\'t answer either without putting words '
            'in your mouth.'),
     why=('It is your claim and what you have seen, and the guide\'s fidelity check holds its words ("meaningful", '
          '"earliest", "warning"). How you\'d say a claim from your own experience, with what it rests on, teaches me the '
          'guide\'s other paragraphs like it.'),
     advice_note=('Edit it: what a tense jaw on MDMA means, and what you\'ve seen happen with and without enough magnesium, '
                  'in your words. If you can say what "meaningful" tension looks like, or which complications you mean, '
                  'that answers both readers.'),
     spans=[whole(P('B114'))])

card(id='TEACH-WIFE', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='2. MDMA: Magnesium Alarm, your second wife\'s story and what you took from it',
     reading=('The section read [AI Detected, 96%%](%s08beb99e-4d7b-45b4-ac6f-32c9bfe3823a) on 2026-11-11, this paragraph '
              'AI-Assisted Low for the story and AI High for the lesson after it.' % H),
     tested=('Try 1: "What happened to my second wife is why I look past magnesium: she had severe convulsions after an MDMA '
             'overdose, and at the hospital they found her potassium critically low, described to me as essentially zero. IV '
             'potassium was the only treatment they gave her. So I treat serious MDMA toxicity as a broader electrolyte '
             'emergency, potassium included, even though magnesium is still the first and most useful intervention once '
             'the jaw tenses." [AI Generated](%s6840df55-84e4-4d02-9a14-086676b419a5): AI High, AI Medium, AI High.\n\n'
             'Try 2, the story opening on itself and the short line joined to it: "My second wife had severe convulsions '
             'after an MDMA overdose, and at the hospital they found her potassium critically low, described to me as '
             'essentially zero, and IV potassium was the only treatment they gave her. So I treat ..." '
             '[AI Generated](%s162c5eaf-11c9-4eca-bdb6-e90cee404bc5): the story AI Medium, the lesson AI High.' % (H, H)),
     sense=('A fresh reader said the paragraph opens a new story with nothing saying why it follows the magnesium talk, and '
            'that "a broader electrolyte emergency" doesn\'t say what to do differently. The lesson read AI High in every '
            'try, and the guide\'s fidelity check holds its words ("toxicity", "intervention", "broader"), so I can\'t say '
            'it plainer without your say.'),
     why=('It is your story, and only you can tell it in your words. How you\'d say what it taught you shows me how the '
          'guide\'s other lessons from your life should read.'),
     advice_note=('Edit it: what happened to her, and what it means for someone sitting with a friend on MDMA, in your '
                  'words. Every fact of hers stays as you tell it; the words the fidelity check holds can change if you '
                  'change them.'),
     spans=[whole(P('B118'))])
