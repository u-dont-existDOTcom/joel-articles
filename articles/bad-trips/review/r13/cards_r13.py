# The cards of round 13, read by build_r13.py (which defines P, T, whole, span_of, replace_words, cut_block and card).
# P('B254') is the page block of GUIDE-SO-FAR-blocks.json's B254 (the guide after the repeats cut in and around Get One
# Human Anchor, experiments/t19-anchor). The checks are in articles/bad-trips/humanize/h14-20261106/RESULTS.md.

BUILT = '2026-11-06'
H = 'https://www.pangram.com/history/'
HD = 'articles/bad-trips/humanize/h14-20261106/'

INTRO = [
    'Round 13 (2026-11-06). Get One Human Anchor and the sections after it now say each thing once. Under your 19:43 rule '
    '("make the cuts regardless of pangram if it makes the guide read better") five repeats are cut. The committee line '
    'is gone, since the section\'s first sentences say too many people make it worse. The violence part\'s second "recruit '
    'one additional calm adult or crisis professional" is gone, since Get One Human Anchor says it with violence among its '
    'cases. Alone at 3 a.m. no longer repeats Stillness or Movement? (pacing, towels and a cup, sitting or lying under a '
    'blanket) or the list of services just above it; it keeps its own ways to move and "Then protect sleep." And Who to '
    'Contact, and When no longer says peer support doesn\'t replace crisis care, which the call-for-help part says.',
    'Two cards, for Get One Human Anchor\'s two paragraphs. Its two scripts read AI in every wording I tried, six each, and '
    'keep the whole section AI with or without these cards, so they stay as the guide has them for now and go on the later list (the fixing is mine). '
    'Round 12\'s card is still open on its own page.',
]

NEW_P1 = ("Many bad trips get worse because somebody is alone with a frightened or over-certain mind. Other times it's the "
          "opposite: too many people crowd in and start advising, arguing, spiritualizing, or panicking.")
NEW_P2 = ("So one calm person should be the anchor and take the lead. One person can only handle so much, though. When "
          "fatigue or logistics get to be too much, or keeping them safe does, or there's a risk of violence or self-harm, "
          "bring in one more calm adult or a crisis professional to back them up.")

card(id='ANCHOR-OPPOSITE', type='plain', advice='approve',
     title='The first paragraph, its second sentence said as talk',
     reading=('After the Human first half of Psychological First Aid, the paragraph as the guide has it reads [AI, '
              '100%%](%s1f88d659-f008-48ec-b942-b94461b68ff7), and turns the first half AI with it.') % H,
     tested=('With this change: [Mostly Human Written, 2%% AI](%s88fa84a3-9569-4e9b-84af-51c80a0efdd7), every window Human. '
             'Changing the first sentence instead read [19%%](%s817db2c8-d125-4c34-88f5-e79e2e0a2324).') % (H, H),
     what='"Others get worse because" becomes "Other times it\'s the opposite:"; the rest of the sentence stays.',
     why=('All three readers of the tell panel (Codex, Sonnet, Haiku) picked the same thing: the two sentences open the '
          'same way ("Many bad trips get worse because", "Others get worse because"), a mirrored pair. Saying the second '
          'as someone would breaks it and keeps every word they called human ("over-certain", "spiritualizing").'),
     stays='The first sentence, the four behaviors, and the paragraph\'s place under the heading.',
     deciding='Approve puts the new sentence in; Revise lets you change it first.',
     advice_note='Approve: one sentence, the same meaning, and the paragraph reads Human with it.',
     found_by='Pangram after the Human first half, one paragraph at a time, then the tell panel',
     receipt=[HD + 'CARD-P1.receipt.json', HD + 'TEST-base-V1-P1-s2.receipt.json'],
     edits=[{'block': P('B254'), 'before': T(P('B254')), 'after': NEW_P1}],
     spans=[span_of(P('B254'), 'Others get worse because')])

card(id='ANCHOR-BACKUP', type='plain', advice='approve',
     title='The second paragraph, with its limit said as an aside',
     reading=('After the Human first half and the first paragraph (changed), the paragraph as the guide has it reads [AI, '
              '100%%](%s9e494278-4014-467f-b6b0-7759ad833fcc), and so did every one-sentence change to it (folding "That '
              'is backup." in, or any one of its three sentences said differently).') % H,
     tested=('With this change: [40%% AI](%s308d1862-b705-47d8-91d7-fe67a22c725c), the first half Human again, three '
             'windows AI Low to Medium. Four other ways of saying it read 67%% to 81%%; the risks kept as a list read '
             '100%%. The whole section still reads [AI, 100%%](%s4ebe8d04-b233-4318-a65f-396a5ecb8208) with both cards, '
             'because of the scripts.') % (H, H),
     what=('Three sentences become: one calm person as the anchor who leads; one person can only handle so much; when '
           'fatigue, logistics, keeping them safe or a risk of violence or self-harm get to be too much, one more calm '
           'adult or a crisis professional backs them up. The bold stays on the two people it names.'),
     why=('The five-noun list ("safety, fatigue, logistics, violence, or self-harm risk") stayed in every try that read '
          '100%; said as the things that wear one person down, with the limit as an aside, it reads better. "That is '
          'backup." (all three readers) becomes "to back them up". Fatigue, logistics and the risk stay, as the fidelity '
          'keys hold them.'),
     stays=('One lead; one more calm adult or a crisis professional, and only when it is too much for one; fatigue, '
            'logistics, safety, violence and self-harm as the cases.'),
     deciding='Approve puts the three sentences in; Revise lets you change them first.',
     advice_note='Approve: the same rule and cases, and 40% instead of 100%.',
     found_by='Pangram after the Human first half and the first paragraph, one change at a time (14 tries)',
     receipt=[HD + 'CARD-P2.receipt.json', HD + 'TEST-base-X3-P2.receipt.json'],
     edits=[{'block': P('B255'), 'before': T(P('B255')), 'after': NEW_P2}],
     spans=[whole(P('B255'))])
