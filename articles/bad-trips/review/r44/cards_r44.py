# The cards of round 44, read by build_r44.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words, card and BLOB). After turn 50: his round-43 versions in, his two points on turn 49's fixes, the
# paragraph he left to fix in Dealing With Shadow Thoughts, and his own paragraphs below High
# (../../humanize/h58-20261120/RESULTS.md).

BUILT = '2026-11-20'
H = 'https://www.pangram.com/history/'
H58 = BLOB + 'articles/bad-trips/humanize/h58-20261120/'
H57 = BLOB + 'articles/bad-trips/humanize/h57-20261119/'

INTRO = [
    'Round 44 (2026-11-20). Your round-43 versions are in, whole: DMSO beside the charcoal water, and Dealing With Shadow '
    'Thoughts up to "So relax ..." ([every check of this turn](%sRESULTS.md)).' % H58,
    '"Sensitivity varies" is back in DMSO\'s nausea line, with what to do about it: "Sensitivity to DMSO varies, so start '
    'with less than you planned." Niacin\'s liver line now puts the risk where you said it is: "Sustained-release niacin, '
    'or repeated doses through the day, can create a real risk of liver damage ...", with the trial that compared the two '
    'forms linked. Both read Human High by themselves.',
    'The paragraph you left me after your rewrite ("you can try to fix p5") read AI as it stands and in both of my tries, '
    'so it is card 1. Your own four paragraphs that read below High by themselves didn\'t lift with a word or two of mine (two read '
    'worse), so they are cards 2 to 5: the words are yours.',
]

card(id='TEACH-TRIP-SHADOW', type='teach', advice='edit', keep_label='skip this one',
     whose=('he asked: Joel, 2026-11-20 00:01 UTC, on the paragraph after his rewrite of Dealing With Shadow Thoughts: '
            '"you can try to fix p5"'),
     title='1. Dealing With Shadow Thoughts: what to do with the thought during a trip',
     reading=('By itself, as the guide has it: [AI, one window High over the whole paragraph]'
              '(%see4961ce-4aee-4b77-b6ce-e01284c48936).' % H),
     tested=('The four don\'ts unpacked, each with its reason from your paragraphs above it, the script and your room-first '
             'line as they are: [AI High in every window](%s1eac3d57-ac94-4ce3-95f0-fbe122bbadb2).\n\n'
             'Then two fresh readers listed what reads machine-made ([the panel](%spanel-d02/PANEL.md)): they agreed on four '
             'of the five sentences, and on the whole (an even run of sentences of one length, no specific detail). So the '
             'next try showed what a shadow thought looks like on a trip (suddenly hating someone you love, being sure '
             'you\'re a fraud) and put the confession in the reader\'s own night (texting your whole family at 3 a.m.): '
             '[AI High again](%saa4b1c55-60dd-454c-a017-07052bab050d).' % (H, H58, H)),
     sense=('Fresh readers each time: "identify with" can mean relate to or take as yourself; "hold off on confessing it to '
            'everybody" sounded to one like keeping it from the sitter, who is the one to tell; and "return to room, body, '
            'human, time, and love" lists the Grounding Menu\'s order without saying so ("time" is hard to come back to when '
            'time is warped, and "human" could be a person or being human). Each try kept room before body, your Q-5.'),
     why=('Your section above it now reads Human High as a whole, and this is the one paragraph that tells someone what to '
          'do in the moment. Both my tries read AI, as my lists of don\'ts in your frame have before. How you\'d say '
          'it teaches me the other in-the-moment paragraphs of the shadow part (Demons, Abuse Memories, Spiritual).'),
     advice_note='Edit it: the paragraph in your words. Your version goes in whole.',
     list_part='',
     spans=[whole(P('B415'))])

card(id='EDIT-AFTERMATH', type='teach', advice='edit', keep_label='keep it as it is',
     whose='his own: What Kind of Aftermath Is This?, his first paragraph, from his post',
     title='2. What Kind of Aftermath Is This?: your first paragraph',
     reading=('With its heading, by itself: [Human, two windows Medium](%s522cc1a4-33ad-47e3-a862-12feefed7d9a): the heading '
              'with "When symptoms linger, people too often put everything into the "I\'m broken" bucket, which solves '
              'nothing." (23 words), and "Try to find the underlying psychological and/or physiological patterns driving '
              'the symptoms:" (13); the sentence between them High.' % H),
     tested=('"When symptoms linger after a trip" and "psychological or physical patterns": [worse, the first window Low]'
             '(%s27e479d3-fd5e-4906-95d5-124241ea80ac), the last still Medium.' % H),
     sense=('Fresh readers: "obviate", read fast, sounds like you probably won\'t need a professional, which could reassure '
            'someone who does; "patterns" doesn\'t say what to look for until the list does; and "which solves nothing" sums '
            'up where the next line could say what to do instead.'),
     why=('It\'s yours, and two words of mine made it read worse. How you\'d say it teaches me the other lead-ins to your '
          'lists.'),
     advice_note='Keep it as it is, or edit it: your version goes in whole.',
     list_part='',
     spans=[whole(P('B425'))])

card(id='EDIT-SS-LEAD', type='teach', advice='edit', keep_label='keep it as it is',
     whose='his own: Recognizing serotonin toxicity, his round-36 version (its lead-in and list)',
     title='3. Recognizing serotonin toxicity: your lead-in to the Hunter criteria',
     reading=('With its heading and your list, by itself: [Human, the heading and first sentence Medium]'
              '(%s67e584da-4b07-42fa-bffa-d2f38b631225) (17 words); the rest High.' % H),
     tested=('"We can use the Hunter criteria, the same checklist clinicians use to diagnose serotonin syndrome." (the term '
             'explained where it is first used): [much worse, AI Low over the heading, the lead-in and the first two '
             'patterns](%s7d957923-c842-4fe2-9e01-b29a6145fda1).' % H),
     sense=('Fresh readers: "the diagnosis" doesn\'t say of what, or in whom; the third pattern ends "another pattern '
            'together", which has no verb; and one reader, picturing a friend on MDMA, said sweating, shaking and eye jitter '
            'come with MDMA anyway, so the list may alarm before it helps, and asked what to do once a pattern is there. '
            'The list is your round-36 version and reads High, so I changed none of it.'),
     why=('Explaining the term made it read like a model. How you\'d say what the Hunter criteria are, and how to use them, '
          'teaches me the other places a clinical term needs a word of explanation.'),
     advice_note='Keep it as it is, or edit it: the lead-in, and the third pattern if you like.',
     list_part='',
     spans=[whole(P('B132'))])

card(id='EDIT-CONFRONT', type='teach', advice='edit', keep_label='keep it as it is',
     whose='his own: Psychological First Aid: The First Five Minutes, his dangers paragraph',
     title='4. The First Five Minutes: "If they want to go confront somebody, that can wait."',
     reading=('By itself: [Human, this line Medium](%s189231bd-2c54-4e79-af24-7d7e5101c8b6) (10 words); the rest High.' % H),
     tested=('"... that can wait until tomorrow." (wait how long): [Medium again](%s0c280db0-c80f-4662-b865-d26025d48d03) '
             '(12 words).' % H),
     sense=('Fresh readers: three sentences in a row open "If they want to ..."; and "that can wait" says what\'s true where '
            'the helper needs what to do (tell them it can wait? stay with them?).'),
     why='One line of yours. How you\'d say it teaches me the short instructions in the tripsitting part.',
     advice_note='Keep it as it is, or edit the line (or the paragraph).',
     list_part='',
     spans=[span_of(P('B236'), 'If they want to go confront somebody, that can wait.')])

card(id='EDIT-REDEFINING', type='teach', advice='edit', keep_label='keep it as it is',
     whose=('his own: (Re)defining "Bad Trip", his third paragraph, from his post; the line after it ("Sometimes focusing '
            'on what we want makes the blockage visible:") is mine'),
     title='5. (Re)defining "Bad Trip": samsara, and reducing the trip\'s own trauma',
     reading=('With the line after it, by itself: [AI Detected, 44%%](%s3b646eb8-8eb9-44ec-8950-ad7843c5eb14): "Samsara '
              'offers no shortage of difficult experiences to process." AI Low, "It still makes sense to reduce '
              'present-moment trauma so we can address what was already there." AI Medium, and my line AI Low; your first '
              'three sentences Human (High, Medium, Low).' % H),
     tested=('"Samsara, the cycle of ordinary existence," "the trauma the trip itself is causing" and "shows us what\'s '
             'blocking it": [AI, 49%%, the two sentences now one AI Medium window](%sb1dff865-6bc2-4bbe-b2a6-bf72c6d77a89).'
             % H),
     sense=('Fresh readers: "might have come too late" doesn\'t say too late for what; "Samsara" isn\'t explained, and one '
            'reader felt the paragraph reads on without that sentence; "present-moment trauma", read fast, calls the '
            'reader\'s rough trip trauma; and "the blockage" doesn\'t say which.'),
     why=('Your reasoning for why a bad trip is still worth reducing. How you\'d say it teaches me the shadow part\'s '
          'paragraphs that explain why.'),
     advice_note='Keep it as it is, or edit it (and my line after it, if you like).',
     list_part='',
     spans=[whole(P('B330c')), whole(P('B357'))])
