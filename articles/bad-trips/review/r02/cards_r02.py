# The cards of round 2, read by build_r02.py (which defines P, T, whole, span_of, cut_block, cut_words, replace_words and
# card). Block numbers are the page's (GUIDE-SO-FAR-page.md); P('B107') is the page block of GUIDE-SO-FAR-blocks.json's
# B107 (the block ids of his post, kept through round 1).

BUILT = '2026-11-03'
SUB = 'https://ibogaqueen.substack.com/i/170920118/'   # his post's section links (each heading's own link on Substack)

INTRO = [
    'Your round-1 answers are in: the guide after round 1 is the file sent with this page, and every card\'s fate is '
    'recorded. This page carries out your structure answer, A: the Quick Bad Trip Checklist keeps each step\'s heading '
    'and one or two of your lines, step 1 keeps its danger signs in full, and each step ends with a link to the section '
    'that has the rest. The Longer Triage goes; the few things only it says move into the long part.',
    'Three cards at the end turn your round-1 answers into lines (Q-3 and Q-6, in your words as far as I could keep '
    'them, and your advice to try the remedies in low doses first). Nothing changes until you approve it. Humanizing '
    'starts after this round, with your three new rules: AI quips go or get humanized, "one ordinary" goes everywhere, '
    'and "X does not Y" gets changed.',
]

TYPES['words'] = {'label': 'From your answer', 'about': 'a line drafted from what you wrote in round 1, for your OK'}


def more(before_bid, slug, title, cid):
    """The step's last line: a link to the section with the rest (the page shows its words; the link goes in on apply)."""
    return {'before': P(before_bid), 'kind': 'p', 'text': 'More: %s' % title, 'href': SUB + slug, 'seq': 9,
            'card': cid}


def after(i, edits):
    """Block i's text as the card's edits leave it ('' when it goes)."""
    for e in edits:
        if e['block'] == i:
            return e['after']
    return T(i)


def reads_for(blocks, edits, ins, head=None):
    """The step as it would read: its heading, each kept block, and the More line (marked as new)."""
    out = []
    if head is not None:
        out.append({'text': T(head), 'kind': 'h2'})
    for i in blocks:
        t = after(i, edits)
        if t:
            out.append({'text': t, 'kind': BL[i]['kind'] if BL[i]['kind'] in ('h1', 'h2', 'h3', 'h4') else 'p'})
    out.append({'text': ins['text'], 'new': [ins['text']]})
    return out


def step(cid, title, head_bid, kept_bids, edits, ins, what, why, stays, deciding, found_by='my read; readers A, B and C',
         spans=None, advice_note='Approve.'):
    blocks = []
    for b in kept_bids:
        blocks += MAP[b]
    card(id=cid, type='structure', advice='approve', title=title, what=what, why=why, stays=stays, deciding=deciding,
         advice_note=advice_note, found_by=found_by, edits=edits, inserts=[ins],
         spans=spans if spans is not None else [whole(e['block']) if not e['after'] else
                                                 span_of(e['block'], removed(e)) for e in edits] or [whole(P(head_bid))],
         reads=reads_for(blocks, edits, ins, head=P(head_bid)), reads_label='The step as it would read',
         card_after=ins['before'] - 1)


def removed(e):
    """The words an edit takes out (its first changed stretch), for the highlight."""
    b, a = e['before'], e['after']
    i = 0
    while i < min(len(b), len(a)) and b[i] == a[i]:
        i += 1
    j = 0
    while j < min(len(b), len(a)) - i and b[-1 - j] == a[-1 - j]:
        j += 1
    return b[i:len(b) - j].strip() or b


# ---------------------------------------------------------------- the checklist, step by step (ST-1, A)

step('CL-1', 'Step 1: kept in full, with its link', 'B5', ['B6', 'B7'], [],
     more('B8', 'when-to-bring-in-outside-help', 'When to Bring In Outside Help', 'CL-1'),
     what=('Step 1 stays as it is: the danger signs and "Get urgent help while giving basic first aid...". It ends with '
           '"More: When to Bring In Outside Help", linked to [that section](%swhen-to-bring-in-outside-help).' % SUB),
     why='Your answer A: step 1 keeps its danger signs in full.',
     stays='All of step 1.', deciding='Whether you\'d word the link line differently ("More:" is the same on every step).',
     spans=[whole(P('B6')), whole(P('B7'))])

e = [cut_words(P('B9'), 'The phrase is not a diagnosis, but intoxication does not make it meaningless, and somebody with real '
                        'neurological trouble may be unable to describe the problem better. '),
     replace_words(P('B10'), 'I do not yet have evidence that pes-caprae aborts MDMA; for MDMA, move', 'For MDMA, move'),
     cut_words(P('B10'), ' Get medical help in parallel when objective danger signs appear or basic stability cannot be established.'),
     cut_block(P('B11'))]
# the two B10 edits are one change on the page: combine them
b10 = [x for x in e if x['block'] == P('B10')]
b10_after = T(P('B10')).replace('I do not yet have evidence that pes-caprae aborts MDMA; for MDMA, move', 'For MDMA, move').replace(
    ' Get medical help in parallel when objective danger signs appear or basic stability cannot be established.', '')
e = [x for x in e if x['block'] != P('B10')] + [{'block': P('B10'), 'before': T(P('B10')), 'after': b10_after}]
e.sort(key=lambda x: x['block'])
step('CL-1b', '"My brain feels damaged": the check and the next move, nothing else', 'B8', ['B9', 'B10', 'B11'], e,
     more('B12', 'if-someone-says-my-brain-feels-damaged-dmso-humic-acid-first',
          'If Someone Says “My Brain Feels Damaged”: DMSO + Humic Acid First', 'CL-1b'),
     what=('Kept: "Take that seriously even if they are high.", DMSO at once while checking (the whole list of checks, '
           'with the stroke link), and the next move ("DMSO comes first, then Ipomoea pes-caprae..." and "For MDMA, move '
           'from DMSO to the magnesium-and-electrolyte branch."). Goes: "The phrase is not a diagnosis...", the MDMA '
           'caveat, the medics line and the humic acid note. It ends with a link to the brain-damage section.'),
     why=('Each one that goes is said in the long part: "Do not dismiss that report because the person is high or cannot '
          'explain it in clinical language... the person experiencing it may be the least able to describe it neatly." '
          '(the brain-damage section); "I do not yet have data showing that pes-caprae aborts MDMA" (beach morning glory); '
          '"Bring in medical help in parallel for objective neurological signs..." (the Core Order, step 5) and step 1; '
          'and the humic acid note in its own section ("I\'ve found if I take too much ayahuasca or loveyhuasca and I feel '
          '“out of it” and bad, simply smelling the humic acid powder fixes it pretty much instantly...").'),
     stays='What a reader does in the first minutes: take it seriously, DMSO while checking, then pes-caprae or magnesium.',
     deciding=('This step keeps three of your lines, not two, because the second move depends on the drug. Say if you\'d '
               'keep the humic acid note here too (it reads Human in Pangram, in your words).'),
     spans=[span_of(P('B9'), 'The phrase is not a diagnosis, but intoxication does not make it meaningless, and somebody with real '
                             'neurological trouble may be unable to describe the problem better.'),
            span_of(P('B10'), 'I do not yet have evidence that pes-caprae aborts MDMA; for'),
            span_of(P('B10'), 'Get medical help in parallel when objective danger signs appear or basic stability cannot be established.'),
            whole(P('B11'))])

step('CL-2', 'Step 2: kept, with its link', 'B12', ['B13', 'B14'], [],
     more('B15', 'psychological-first-aid-the-first-five-minutes', 'Psychological First Aid: The First Five Minutes', 'CL-2'),
     what='Step 2\'s two lines stay as they are. It ends with a link to The First Five Minutes.',
     why='Its two lines are the whole step; The First Five Minutes says them again with the room, so that is the link.',
     stays='Both lines.', deciding='None that I can see.', spans=[whole(P('B13')), whole(P('B14'))])

e = [cut_words(P('B16'), ' Music can also steer the state in the wrong direction, so use something familiar and keep the stop or '
                         'change button within reach. Steady drumming may give a scattered body one rhythm to follow; airy '
                         'harp-like or meditative music may feel more spiritually uplifting.'),
     cut_block(P('B17'))]
step('CL-3', 'Step 3: the room check and your music page', 'B15', ['B16', 'B17'], e,
     more('B18', 'psychological-first-aid-the-first-five-minutes', 'Psychological First Aid: The First Five Minutes', 'CL-3'),
     what=('Kept: "Check the obvious things: light, sound, temperature..." and the Chantress Seba line with your music page. '
           'Goes: the rest about music, and "Usually one calm sober person is the best main anchor..." (that is step 5).'),
     why=('The Grounding Menu\'s Music list says the rest: "Use familiar music when possible...", "Try a steady drum rhythm '
          'for stabilization or grounding; try airy harp-like or meditative music...", "Keep the stop or change control '
          'immediate." Get One Human Anchor says the anchor line: "Use one calm human anchor as the lead. When safety, '
          'fatigue, logistics, violence, or self-harm risk exceeds what one person can hold, bring in one additional calm '
          'adult or crisis professional."'),
     stays='The room check, and your music page, which is said only here.', deciding='None that I can see.')

step('CL-4', 'Step 4: the two-minute test and the exercise limit', 'B18', ['B19', 'B20', 'B21'],
     [cut_block(i) for i in MAP['B20']],
     more('B22', 'stillness-or-movement', 'Stillness or Movement?', 'CL-4'),
     what=('Kept: "Don’t make this ideological. Try the safest option for two minutes and see what actually happens." and '
           '"Avoid strenuous exercise with overheating...". Goes: the four "If stillness helps..." lines, "one boring '
           'ordinary task" with them. It ends with a link to Stillness or Movement?'),
     why=('Stillness or Movement? says each: "Try one for two minutes", "When lying down feels like imprisonment, pace '
          'slowly in a contained space. When pacing begins to resemble escape, sit against a wall or lie under a blanket.", '
          'and the folding-towels task ("sort ten objects, draw, fold five towels, or wash one cup"); hand on heart has its '
          'own section.'),
     stays='The test and the safety limit on exercise.',
     deciding=('"Shaking out the arms and legs" is said only in these lines now (round 1 cut the menu\'s copy). Say if you '
               'want it kept, and where; if you keep the list, its "one boring ordinary task" becomes "a boring task".'))

e = [replace_words(P('B23'), 'Contact one grounded person if you can. Say:', 'Contact one grounded person if you can.')] + \
    [cut_block(P(b)) for b in ('B24', 'B25', 'B26', 'B27', 'B28')]
step('CL-5', 'Step 5: contact one person; the scripts are in the anchor section', 'B22',
     ['B23', 'B24', 'B25', 'B26', 'B27', 'B28'], e,
     more('B29', 'get-one-human-anchor', 'Get One Human Anchor', 'CL-5'),
     what=('Kept: "Contact one grounded person if you can." Goes: the three scripts. It ends with a link to Get One Human '
           'Anchor, where the script to send is.'),
     why=('Get One Human Anchor has the same script ("I’m in an intense psychedelic or altered state and I need grounding. '
          'I don’t need you to solve my life. Please stay with me, speak slowly, remind me where I am, and help me not '
          'make any big decisions until tomorrow.") and the sitter\'s, and The First Five Minutes has the place-and-time '
          'line and the stopping-the-practice line ("I am in an intense state. I am stopping the practice now. My job is '
          'ordinary safety."). Reader B counted the anchor script among the five repeats a reader would most notice.'),
     stays='The step\'s first action.',
     deciding=('Whether the script to send should stay here for someone in trouble who reads only the checklist; then '
               'the anchor section\'s copy could go instead. The "I took something..." line said in your own voice is '
               'only here.'))

step('CL-6', 'Step 6: the 3 a.m. plan stays, its movement lines go', 'B29', ['B30', 'B31', 'B32'], [cut_block(P('B32'))],
     more('B33', 'alone-at-3-am', 'Alone at 3 a.m.', 'CL-6'),
     what=('Kept: "One lamp on. Blanket. Water nearby. Keys away..." and the note ("This will change. No big actions until '
           'morning."). Goes: "If your body needs to move, do something safe and boring..." It ends with a link to Alone '
           'at 3 a.m.'),
     why=('Alone at 3 a.m. starts from this plan ("The quick checklist above contains the stripped-down 3 a.m. plan") and '
          'says the movement part with more in it: "pace the same hallway, fold towels, wash a cup, brush your teeth, '
          'stretch gently, take a calm shower, or do a few slow wall push-ups. When movement makes you more frantic, sit '
          'with both feet against the floor or lie under a blanket. Then protect sleep."'),
     stays='The plan Alone at 3 a.m. points back to.', deciding='None that I can see.')

e = [replace_words(P('B35'), 'Try grounding before chemically or forcefully changing the state:',
                   'Try grounding before chemically or forcefully changing the state.')] + \
    [cut_block(i) for i in MAP['B36']] + [cut_block(P('B37'))]
step('CL-7', 'Step 7: the condition and the first move; the menu has the rest', 'B33', ['B34', 'B35', 'B36', 'B37'], e,
     more('B38', 'grounding-menu-choose-one-or-two-things', 'Grounding Menu: Choose One or Two Things', 'CL-7'),
     what=('Kept: "Use this calming branch only after the quick neurological screen is reassuring..." and "Try grounding '
           'before chemically or forcefully changing the state." Goes: the six grounding options and the over-breathing '
           'note. It ends with a link to the Grounding Menu.'),
     why=('The Grounding Menu has each option: hand on heart and belly, the longer exhale, the Buteyko-style breathing with '
          '"Never force breath-holds while intoxicated or panicked", silence or familiar music, slow pacing; and its '
          'Buteyko evidence note says the over-breathing point with the same Hopkins source ("panic-related over-breathing '
          'can lower CO2 and directly cause tingling, lightheadedness, confusion, and unreality feelings").'),
     stays='When to use the calming branch, and its first move.', deciding='None that I can see.')

step('CL-8', 'Step 8: kept but for its breakfast line', 'B38', ['B39', 'B40', 'B41'], [cut_block(P('B41'))],
     more('B42', 'when-the-trip-feels-amazing-euphoric-certainty', 'When the Trip Feels Amazing: Euphoric Certainty', 'CL-8'),
     what=('Kept: "Some dangerous states feel wonderful..." and "The action-lock applies double...". Goes: "If the revelation '
           'is true, it will survive sleep and breakfast." It ends with a link to the euphoria section.'),
     why=('The euphoria section ends on the same test ("If it is true, it survives sleep."), and it is the kind of quip you '
          'asked to remove or humanize.'),
     stays='The warning and the action lock.', deciding='None that I can see.')

step('CL-9', 'Step 9: what to do and when to call; the God script is in the harm section', 'B42',
     ['B43', 'B44', 'B45', 'B46'], [cut_block(P('B44')), cut_block(P('B45'))],
     more('B47', 'when-the-content-turns-toward-harm', 'When the Content Turns Toward Harm', 'CL-9'),
     what=('Kept: "Don’t try to win a metaphysical argument. Don’t agree with harmful conclusions either. Reflect the feeling, '
           'then redirect..." and "Get crisis or emergency help when there is a specific target, a weapon...". Goes: "A '
           'useful response sounds like this:" and the God script. It ends with a link to the harm section.'),
     why=('When the Content Turns Toward Harm has the script word for word ("I hear how vast and certain this feels. Many '
          'traditions say God is in everyone..."). Reader B counted it first among the repeats a reader would most notice.'),
     stays='What to do, and when to call for help.', deciding='Whether the script should stay here instead, and go there.')

e = [cut_words(P('B49'), ' That is a personal field note, rather than standard emergency medicine.'), cut_block(P('B50'))]
step('CL-10', 'Step 10: the gut signs and zeolite first; charcoal is in its own sections', 'B47', ['B48', 'B49', 'B50'], e,
     more('B51', 'gut-toxin-and-parasite-die-off-tools', 'Gut-Toxin and Parasite-Die-Off Tools', 'CL-10'),
     what=('Kept: "Nausea, diarrhea, a dirty or toxic feeling... But don’t let “toxins” distract from repeated vomiting..." '
           'and "My personal first thought here is ozonated zeolite rather than charcoal...". Goes: "That is a personal field '
           'note, rather than standard emergency medicine." and the activated charcoal paragraph. It ends with a link to '
           'the gut tools.'),
     why=('"My personal first thought" already says it is yours, and How I label the evidence names personal field '
          'signals. Recent Oral Toxic Ingestion says the charcoal paragraph with the same review: "It does not bind every '
          'toxin, can adsorb necessary medication, and creates aspiration risk in somebody who is vomiting, sedated, '
          'seizing, or unable to protect the airway."'),
     stays='The signs to watch for, and your first remedy.', deciding='None that I can see.')

step('CL-11', 'Step 11: the nausea rule; pes-caprae\'s margin is in its section', 'B51', ['B52'],
     [cut_words(P('B52'), ' Ipomoea pes-caprae is not my ordinary first-line nausea remedy, because the difference between '
                          'smoothing the nausea and stopping the trip can be narrow.')],
     more('B53', 'nausea-smoothers-when-the-person-wants-to-preserve-the-trip',
          'Nausea Smoothers When the Person Wants to Preserve the Trip', 'CL-11'),
     what=('Kept: "Use nausea smoothers that are unlikely to abort the trip when the person wants to preserve it." Goes: the '
           'pes-caprae sentence. It ends with a link to the nausea section.'),
     why=('Beach morning glory says it: "Its primary role in this guide is not ordinary nausea control." and "the difference '
          'between that amount and a trip-aborting amount is narrow".'),
     stays='The step\'s rule.', deciding='None that I can see.')

b54_after = T(P('B54')).replace(' For neurological concern, DMSO comes first and pes-caprae follows.', '').replace(
    ' I do not yet have data showing that pes-caprae aborts MDMA.', '')
step('CL-12', 'Step 12: the sledgehammer and the backup', 'B53', ['B54', 'B55'],
     [{'block': P('B54'), 'before': T(P('B54')), 'after': b54_after}, cut_block(P('B55'))],
     more('B56', 'when-the-goal-is-to-stop-a-psychedelic-trip', 'When the Goal Is to Stop a Psychedelic Trip', 'CL-12'),
     what=('Kept: "...Ipomoea pes-caprae is my ultimate sledgehammer." and "Niacin is a backup trip killer." Goes: "For '
           'neurological concern, DMSO comes first and pes-caprae follows.", the MDMA caveat, and the charcoal paragraph. '
           'It ends with a link to the trip-stopping section.'),
     why=('The brain-damage step and section say DMSO first; beach morning glory says "I do not yet have data showing that '
          'pes-caprae aborts MDMA."; the ingestion section and Actual Activated Charcoal say when charcoal fits and when '
          'it is dangerous.'),
     stays='Your two trip stoppers.',
     deciding='Round 1 (Q-7) took this step\'s charcoal sentence out; this takes the charcoal paragraph after it too.',
     spans=[span_of(P('B54'), 'For neurological concern, DMSO comes first and pes-caprae follows.'),
            span_of(P('B54'), 'I do not yet have data showing that pes-caprae aborts MDMA.'), whole(P('B55'))])

step('CL-13', 'Step 13: what to use; the order is the checklist\'s first line', 'B56', ['B57'],
     [cut_words(P('B57'), ' Meaning still waits until the person is safe, hydrated, oriented, and unlikely to do anything rash.')],
     more('B58', 'shadow-work-and-tripsitting-yourself-or-others', 'Shadow Work and Tripsitting Yourself or Others', 'CL-13'),
     what=('Kept: "Then use love, awareness, inner-child reparenting, somatic release, and gentle witnessing." Goes: "Meaning '
           'still waits until..." It ends with a link to the shadow-work half.'),
     why='The checklist opens with it: "...protect sleep, and only then start interpreting anything."',
     stays='What to use.', deciding='None that I can see.')

step('CL-14', 'Step 14: kept, with your love link', 'B58', ['B59'], [],
     more('B60', 'dealing-with-sorrow-missing-versus-sending-love', 'Dealing With Sorrow: Missing Versus Sending Love', 'CL-14'),
     what=('Step 14 stays as it is, and "love" in its heading links to your love page (http://love.u-dont-exist.com/), as '
           'the Longer Triage\'s "Can love be reached yet?" did; that is the only place the link was. It ends with a link '
           'to Dealing With Sorrow.'),
     why='The Longer Triage goes (LT-1); its fifth question says what step 14 says ("Stabilize first. Then love.").',
     stays='Step 14\'s line.', deciding='None that I can see.', spans=[whole(P('B59'))])

e = [cut_words(P('B61'), ' Coverage and hours vary by country.')] + [cut_block(i) for i in MAP['B62']] + [cut_block(P('B63'))]
step('CL-15', 'Step 15: save the numbers first; the lines are in Who to Contact', 'B60', ['B61', 'B62', 'B63'], e,
     more('B64', 'who-to-contact-and-when', 'Who to Contact, and When', 'CL-15'),
     what=('Kept: "Identify local crisis and peer-support resources before you need them." Goes: "Coverage and hours vary '
           'by country.", the five services, and "Bottom line: safety, room, body, human, no rash actions, sleep if '
           'possible, then meaning." It ends with a link to Who to Contact, and When.'),
     why=('Who to Contact, and When has all five with their numbers and hours, and more ("Hours and services change, and '
          'not every option works in every country."). The bottom line is the checklist\'s first line again.'),
     stays='The step\'s instruction.', deciding='Whether the five links should stay here for a reader in a hurry.')

# ---------------------------------------------------------------- the Longer Triage

lt_cut = ['B68', 'B69', 'B70', 'B71', 'B72', 'B73', 'B74', 'B75', 'B78', 'B79', 'B80', 'B81', 'B85', 'B88', 'B89', 'B90']
card(id='LT-1', type='structure', advice='approve', title='The Longer Triage goes',
     what=('The section goes: its heading, its picture, its five question labels, and the paragraphs the long part already '
           'says, each listed under Why. Four things only it says move (LT-2 to LT-5); the love link goes into step 14\'s '
           'heading (CL-14).'),
     why=('Where each one is said: "what could hurt them now?" and the body-mind-room split: The First Five Minutes ("Begin '
          'with whatever could hurt somebody in the next five minutes") and the hierarchy. The failing-body paragraph: step 1 '
          'and the medics list. "my brain feels damaged" and the DMSO check: the brain-damage section (its checks, and "A '
          'person who cannot answer or cooperate has not passed the screen"). The DMSO-while-medics paragraph: the Core '
          'Order. The room paragraphs: The First Five Minutes ("Then look at the room. Is the light too bright?..." and "A '
          'huge amount of what gets called profound psychedelic crisis is a frightened nervous system stuck in an annoying '
          'room."). "Stabilize first. Then love.": step 14 ("When you can’t, stabilize the room, body, breath, human contact, '
          'time orientation, and sleep. Then try again.").'),
     stays=('What moves: the "reassuring screen" line (LT-2), the stable-state test and the ER paragraph (LT-3), the real '
            'emotional material (LT-4), the body writing the horror story (LT-5).'),
     deciding=('Its picture goes with it; say if it belongs somewhere else. The other two ways of saying it ("my brain is '
               'broken", "I’m losing control of my body") go too; say if you want them in the brain-damage section.'),
     advice_note='Approve.', found_by='my read; readers A, B and C',
     edits=[cut_block(i) for b in lt_cut for i in MAP[b]],
     spans=[whole(i) for b in lt_cut for i in MAP[b]],
     card_after=P('B91') - 1)

card(id='LT-2', type='structure', advice='approve', title='The Longer Triage\'s "reassuring screen" line moves to the brain-damage checks',
     what=('"If the screen is reassuring but the brain-damage feeling remains, continue the DMSO-first route and reassess '
           'promptly." moves to the end of the brain-damage section\'s checks.'),
     why='Nothing else in the guide says what to do when the checks pass but the feeling stays.',
     stays='The checks paragraph, with this line after "their neurological status is still unknown."',
     deciding='None that I can see.', advice_note='Approve.', found_by='my read',
     edits=[replace_words(P('B104'), 'their neurological status is still unknown.',
                          'their neurological status is still unknown. If the screen is reassuring but the brain-damage '
                          'feeling remains, continue the DMSO-first route and reassess promptly.')],
     spans=[span_of(P('B75'), 'If the screen is reassuring but the brain-damage feeling remains, continue the DMSO-first route '
                              'and reassess promptly.'), span_of(P('B104'), 'their neurological status is still unknown.')],
     card_after=P('B104'))

b77_after = T(P('B77')).replace(' Calling for help is not the same thing as receiving good care.', '').replace(
    ' That is why the decision belongs to the actual symptom pattern rather than the word “overdose.”', '')
card(id='LT-3', type='structure', advice='approve', title='What counts as stable, and the ER\'s limits, move under the rescue section\'s first paragraph',
     what=('The Longer Triage\'s stable-state test ("When the person is breathing normally, not dangerously hot, not seizing, '
           'has no neurological-injury concern, remains conscious enough to cooperate, and can be kept physically safe, '
           'calming and stabilizing the trip may be enough.") and its ER paragraph move under "An emergency means act now..." '
           'at the start of Acute Medical and Neurological Rescue. The ER paragraph loses "Calling for help is not the same '
           'thing as receiving good care." and "That is why the decision belongs to the actual symptom pattern rather than '
           'the word “overdose.”"'),
     why=('That first paragraph ends "Some severe but physically stable altered states may respond faster to field rescue '
          'than to hours in an emergency room." The test says what physically stable means, and the ER paragraph says why, '
          'so all three readers took them as one point. The first cut line changes nothing a reader does (reader C); the '
          'second is the ingestion section\'s ("“Overdose” is too vague to choose a remedy.").'),
     stays='The test, the benzodiazepine and antipsychotic reasons, and "The emergency room is not magic...".',
     deciding='None that I can see.', advice_note='Approve.', found_by='my read; readers A, B and C',
     edits=[cut_words(P('B76'), 'A severe altered state that is only too intense belongs in a different branch. '),
            {'block': P('B77'), 'before': T(P('B77')), 'after': b77_after}],
     moves=[{'blocks': [P('B76'), P('B77')], 'before': P('B101'), 'seq': 1}],
     spans=[whole(P('B76')), whole(P('B77'))], card_after=P('B100'))

card(id='LT-4', type='structure', advice='approve', title='Real emotional material moves to For the Person Helping',
     what=('"Crying, grieving, remembering, or touching a genuine wound calls for loving awareness...", "Stay present. A '
           'useful phrase is..." and "Don’t drag somebody out of real grief..." move to For the Person Helping, after '
           '"A good sitter is not there to win a philosophy debate..." and before its Do list.'),
     why=('Nothing else in the guide says what to do with real grief in the moment, and these are a sitter\'s choices, '
          'next to the sitter\'s other ones.'),
     stays='All three paragraphs, as you wrote them.', deciding='Whether they fit better in Dealing With Sorrow.',
     advice_note='Approve.', found_by='my read',
     moves=[{'blocks': [P('B82'), P('B83'), P('B84')], 'before': P('B281'), 'seq': 1}],
     spans=[whole(P('B82')), whole(P('B83')), whole(P('B84'))], card_after=P('B84'))

card(id='LT-5', type='structure', advice='approve', title='"The body writing the horror story" moves into the hierarchy',
     what=('"Sometimes the mind isn’t in a metaphysical crisis. The body feels awful and the altered mind writes cosmic '
           'horror to explain it..." and "A horrible thought isn’t automatically a revelation..." move into My Acute Rescue '
           'Hierarchy, in place of "Psychedelic culture often treats every crisis as emotional or spiritual..."'),
     why=('Both say the body can be the problem; the Longer Triage\'s two say how it turns into spiritual content, which is '
          'why both repeat readers took them as the home of the point. What goes with the hierarchy\'s paragraph '
          '("poisoned, dealing with an electrolyte problem, reacting to a bad combination") has its own rescue sections.'),
     stays=('The hierarchy then reads: "This hierarchy is for acute situations...", these two, and "A trip with diarrhea, '
            'nausea... A gut-driven mental hell is often mistaken as shadow work."'),
     deciding='Whether you\'d rather keep the hierarchy\'s paragraph and let these two go.',
     advice_note='Approve.', found_by='readers A and B',
     edits=[cut_block(P('B140'))],
     moves=[{'blocks': [P('B86'), P('B87')], 'before': P('B141'), 'seq': 1}],
     spans=[whole(P('B86')), whole(P('B87')), whole(P('B140'))], card_after=P('B140'))

# ---------------------------------------------------------------- lines from your round-1 answers

card(id='AN-Q3a', type='words', advice='approve', title='DMSO and harmalas, in your words (your answer to Q-3)',
     what=('The DMSO interaction line becomes: "Don’t take it with drugs that should not absorb rapidly, including '
           'corticosteroids and NSAIDs. With harmalas, don\'t put the harmala in the DMSO or take them at exactly the same '
           'time; taking them a bit apart is totally fine, and the point is to take DMSO if you\'ve already absorbed the '
           'harmalas and the aya is too crazy."'),
     why=('Your answer: "don\'t take DMSO literally with harmalas like don\'t put the harmala in the dmso or take them exactly '
          'at the same time, but it\'s totally fine to take them a bit apart like and there is no reason to take them '
          'together anyway the point is to take dmso if you already absorbed the harmalas and the aya is too crazy." I left '
          'out "there is no reason to take them together anyway", since the rest says it.'),
     stays='The rest of DMSO\'s interactions, the blood-thinning line included.',
     deciding='Any word of it you\'d say differently (your words keep the apostrophes you typed).',
     advice_note='Approve, or revise it in your words.', found_by='your answer to Q-3',
     edits=[replace_words(P('B205', 2), 'Don’t take it with drugs that should not absorb rapidly, including corticosteroids, NSAIDs, '
                          'and harmalas.',
                          'Don’t take it with drugs that should not absorb rapidly, including corticosteroids and NSAIDs. With '
                          'harmalas, don\'t put the harmala in the DMSO or take them at exactly the same time; taking them a bit '
                          'apart is totally fine, and the point is to take DMSO if you\'ve already absorbed the harmalas and the '
                          'aya is too crazy.')],
     spans=[span_of(P('B205', 2), 'and harmalas')])

card(id='AN-Q3b', type='words', advice='approve', title='A possible bleed, in your words (your answer to Q-3)',
     what=('The stroke paragraph gains, after "...because the symptoms improved enough to feel reassuring.": "If someone is '
           'worried about a bleed, I\'d probably skip DMSO, but it depends on how severe their issue is. It\'s not a powerful '
           'blood thinner like heparin, unless maybe injected; it\'s basically a dietary blood thinner. I\'ve never had any '
           'issues with bleeding too much from consuming DMSO, and never heard of it either, but if bleeding is already a '
           'medical issue I\'d want to think about that more."'),
     why=('Your answer: "if someone is worried about a bleed, i\'d prob skip dmso but it depends on how severe their issue is, '
          'it\'s not a powerful blood thinner like heperin or something unless maybe injected, it\'s a dietary blood thinner '
          'basically ... i\'ve never had any issues with bleeding too much because of consuming dmso myself. never heard of '
          'it either but if that\'s already a medical issue i\'d wanna think about that more". You asked me to check how '
          'strong it is: the human platelet study your chest-pain section already links found a mild effect in donated '
          'blood (platelets stuck about 15% less under flow, and aggregation fell about 6%), which fits "not a powerful '
          'blood thinner" (PubMed: [Asmis et al. 2010](https://doi.org/10.1016/j.bbrc.2009.12.102)). I found no study '
          'of bleeding in people taking it by mouth, so the line stays your experience.'),
     stays='The rest of the stroke paragraph.',
     deciding='Whether it belongs here or with the DMSO section\'s blood-thinning line.',
     advice_note='Approve, or revise it in your words.', found_by='your answer to Q-3',
     edits=[replace_words(P('B106'), 'because the symptoms improved enough to feel reassuring.',
                          'because the symptoms improved enough to feel reassuring. If someone is worried about a bleed, I\'d '
                          'probably skip DMSO, but it depends on how severe their issue is. It\'s not a powerful blood thinner '
                          'like heparin, unless maybe injected; it\'s basically a dietary blood thinner. I\'ve never had any '
                          'issues with bleeding too much from consuming DMSO, and never heard of it either, but if bleeding '
                          'is already a medical issue I\'d want to think about that more.')],
     spans=[span_of(P('B106'), 'DMSO cannot identify whether the problem is a clot, a hemorrhage')])

card(id='AN-Q6', type='words', advice='approve', title='Ocean water and charcoal water, in your words (your answer to Q-6)',
     what=('"These work similarly to ocean water." becomes: "I honestly can\'t say how different these are from ocean water, '
           'because I\'ve only used them a handful of times, but I do believe they\'re different in certain ways. Ocean water '
           'seems to reduce the intensity of the trip a bit more, while aged ozonated-charcoal water seems more peaceful '
           'without necessarily reducing intensity, and ocean water seems more reliable for some reason."'),
     why=('Your answer: "i honestly cannot say if they are so different because i\'ve only used them a handful of times but i '
          'do believe they are different in certain ways. i feel like the ocean water can reduce the intesnity of the trip '
          'a bit more than the ozonated charcoal water which seems more like peaceful without necessarily reducing '
          'intensity, and i also feel like the ocean water is more reliable for some reason..."'),
     stays='"Aged ozonated-charcoal water is different from zeolite and from swallowing charcoal.", and the ocean water section.',
     deciding='Any word of it you\'d say differently.', advice_note='Approve, or revise it in your words.',
     found_by='your answer to Q-6',
     edits=[replace_words(P('B190'), 'These work similarly to ocean water.',
                          'I honestly can\'t say how different these are from ocean water, because I\'ve only used them a '
                          'handful of times, but I do believe they\'re different in certain ways. Ocean water seems to reduce '
                          'the intensity of the trip a bit more, while aged ozonated-charcoal water seems more peaceful '
                          'without necessarily reducing intensity, and ocean water seems more reliable for some reason.')],
     spans=[span_of(P('B190'), 'These work similarly to ocean water.')])

card(id='AN-Q1', type='words', advice='approve', title='Try the remedies in low doses first, in your words (from your answer to Q-1)',
     what=('A new line after the hierarchy\'s first one ("This hierarchy is for acute situations..."): "In general it\'s good '
           'to try all these things in very low, increasing doses before they are needed in crisis."'),
     why=('Your answer: "smell it first for sure, that\'s like an allergy test, some ppl are super sensitive... some ppl also '
          'super sensitive to dmso altho that\'s more rare. in general it\'s good to try all these things in very low, '
          'increasing doses before they are needed in crisis." Round 1 put "smell it first" into the Core Order\'s first '
          'step ("Smell humic acid first; if that doesn’t help, take a 5mg lick of it."); this is the general advice, '
          'said once, where the remedies start.'),
     stays='The hierarchy as it is.', deciding='Whether it fits better at the start of Some Remedies Require More Caution.',
     advice_note='Approve.', found_by='your answer to Q-1',
     inserts=[{'before': P('B140'), 'kind': 'p', 'text': 'In general it\'s good to try all these things in very low, increasing '
               'doses before they are needed in crisis.', 'seq': 1}],
     spans=[whole(P('B139'))], card_after=P('B139'))
