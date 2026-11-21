# The cards of round 48, read by build_r48.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 58: the serotonin steps (B136), whose every wording of mine read AI in three
# tries (../../humanize/h65-20261121/RESULTS.md).

BUILT = '2026-11-21'
H = 'https://www.pangram.com/history/'
H65 = BLOB + 'articles/bad-trips/humanize/h65-20261121/'
ASKED = ('he asked: Joel, 2026-11-08 17:22 UTC: "give me your best tries and what would teach you the best and i\'ll do '
         'that"; 2026-11-14 22:08 UTC: "didn\'t understand why you gave me no cards and quit working tho"')

TRY3 = ('Keep them still in a calm room. They\'re already overstimulated, so I\'d clear out the crowd and stop any arguing. '
        'Pacing or exercising to "burn it off" only makes more heat, and it raises the risk of their muscles breaking down '
        'into the blood, which hurts the kidneys (rhabdomyolysis). If they feel a strong urge to keep moving (akathisia), '
        'I\'d stay with them and talk them into keeping still anyway.\n\n'
        'Give fluids only if they\'re fully alert, able to swallow and not vomiting, and then just small sips of an '
        'electrolyte drink. But if they\'re confused, vomiting or sleepy, I wouldn\'t push anything into them, not even '
        'pills or charcoal, since they could choke. The same goes if they might have a seizure.')

INTRO = [
    'Round 48 (2026-11-21). Your round-47 headings are in the guide, with the evidence tags under eight remedy headings '
    '([what went in](%sarticles/bad-trips/review/r47/RESULTS-R47.md)). One card: the serotonin steps.' % BLOB,
    'I can\'t get the serotonin steps to read Human in my words. Three tries on each pair of steps read AI, and so did '
    'four steps checked by themselves; the only part of the list that reads Human is your own step 2 '
    '([every check](%sRESULTS.md)). Steps 5 and 6 are the card: how you\'d say them teaches me steps 1, 3, 4, 7 and 8.' % H65,
]

card(id='TEACH-SS-STEPS', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
     title='1. Act Now on SS: steps 5 and 6 (keep them still, give fluids only if)',
     reading=('The eight steps by themselves, as the guide has them: [AI Generated, 100%%, AI High over all 326 words]'
              '(%s2d3e8386-31e3-45f8-8968-f875710a2470).' % H),
     tested=('**Try 1**, each sentence your fixes\' way (the drug list in groups, akathisia and rhabdomyolysis explained '
             'where first used, the reasons joined with "since" and "so"): steps 5 and 6 [AI High 133]'
             '(%s25df9e03-eb53-458f-a136-c238e6650e3a).\n\n'
             '**Try 2**, in the form of your Active Seizure list (a lead line and short items): [AI High 121]'
             '(%sfc3db895-2d16-4e30-a626-635f44022fd1); step 5 by itself [AI High 69]'
             '(%sd85068d3-ebac-4a40-b630-efaf22aebf26). Steps 1 and 2 together read [Human]'
             '(%s8ad45936-f8e3-4d22-bcbc-0564508d234f), but step 1 by itself read [AI High 65]'
             '(%s49c25418-8bd1-4238-afe2-927a59031592): it was your step 2 carrying the pair.\n\n'
             '**Try 3**, in your first person like your step 2, after the tell panel\'s fixes: [AI Medium 7, AI High 122]'
             '(%sf4275573-6c55-4088-b703-de8331ec99b9):\n\n> %s' % (H, H, H, H, H, H, TRY3.replace('\n\n', '\n>\n> '))),
     sense=('Three fresh readers on every try, then the tell panel twice on try 3 (Sonnet and Haiku: '
            '[first](%spanel-g4c/PANEL.md), [after its fixes](%spanel-g4c-2/PANEL.md); Codex, the panel\'s reader from '
            'another family, runs from your laptop, which wasn\'t connected). After its first fixes the panel flagged six '
            'of seven sentences: the parallel conditions ("fully alert, able to swallow and not vomiting"), the terms in '
            'brackets, the if/but pair, and the paragraph built evenly, a rule and its reason in every sentence.'
            % (H65, H65)),
     why=('I can\'t find any more AI tells here that I can fix, and I see some human tells, like "burn it off" in your '
          'quote marks, "talk them into keeping still anyway" and "They\'re already overstimulated". Can you help show me '
          'the tells I\'m missing? Every wording of mine reads AI, in three forms; your step 2 is the one part that '
          'reads Human. What the tell panel found: [its record](%spanel-g4c-2/PANEL.md).' % H65),
     advice_note=('Edit it: steps 5 and 6 in your words, or my try 3 (above) with your changes. Your version goes in '
                  'whole, and I carry its ways to the other steps.'),
     list_part=('steps 5 and 6 only: the whole list is 460 words, and these two hold the kinds of sentence every other '
                'step has (what to do, why, and the case where not to), so your version of them teaches the rest; your '
                'step 2 and your C1 step 3 opening stay as they are'),
     spans=[whole(P('B136', 4)), whole(P('B136', 5))])
