# The cards of round 1, read by build_r01.py (which defines P, T, whole, span_of, cut_block, cut_words, replace_words and
# card). Block numbers are the page's (original-page.md); P('B107') is the page block of original-blocks.json's B107.

BUILT = '2026-11-03'

INTRO = [
    'This is your whole Bad Trips guide as it is published today (it matches the editor HTML you pasted, block for '
    'block), with my suggestions marked where they apply. Nothing changes until you approve it.',
    'The first card is the one big question: how the quick version and the long version split the work. Most of the '
    'repetition is between the checklist, the Longer Triage and the long sections, so those cuts wait for your answer. '
    'The other cards are repeats and safety lines inside the long part, which come out whichever way you answer, and '
    'seven questions only you can answer (in six of them the guide says two things that don\'t fit together). Three '
    'fresh readers are reading the whole guide for this, two for repeats and one for safety lines: the cards come from '
    'my read, both repeat readers\' reports and the first half of the safety reader\'s, and every quote on them was '
    'checked against your text.',
    'Pangram (your extension, on the published post) reads the guide as AI overall. The full analysis didn\'t open from '
    'here, so there are no window readings on this page yet. Humanizing starts once the structure is settled, so no '
    'work goes into paragraphs that are about to be cut.',
]

# ---------------------------------------------------------------- the structure question

card(id='ST-1', type='structure', advice='ask', title='How should the quick and long versions split the work?',
     question=(
         'A (my pick): the Quick Bad Trip Checklist stays at the top, but each step becomes its heading and one or two of '
         'your own lines saying what to do, with a link to its section below. Step 1 keeps its danger signs in full, '
         'since someone in an emergency shouldn\'t have to click. Everything else is said once, in the long part. The '
         'Longer Triage goes: its paragraphs that aren\'t said anywhere else (the emergency room isn\'t magic; the body '
         'writing the horror story; love isn\'t stubbornness) move to the sections they belong to. '
         'B: keep today\'s order (checklist, Longer Triage, outside help, medical rescue, remedies, tripsitting, the '
         'shadow-work essays) and only cut the repeats inside it, keeping the fuller copy each time. '
         'C: take the quick version out of the post, since the web app at ibogaqueen.com/1625-2/ already is one, and '
         'open the post with a short "In a crisis right now?" box: the danger signs, the brain-damage branch and the '
         'link to the app.'),
     why=('Most of the guide\'s advice is told three or four times: in the checklist (15 steps), in the Longer Triage '
          '(5 questions), and again in the long sections. The brain-damage order is told six times, "I do not yet have '
          'data that pes-caprae aborts MDMA" five times, the support lines three times, and one 38-word quote ("I hear '
          'how vast and certain this feels...") twice word for word. A quick version that only points to the long part '
          'lets each thing be said once.'),
     stays=('Whichever you pick, each checklist step keeps its heading and its first action in your words, and every '
            'paragraph that goes is listed with the place that already says it.'),
     advice_note=('A: it keeps the quick read you want and takes out the third and fourth tellings. B leaves most of the '
                  'repetition between the checklist and the long part. C makes the post depend on the web app for the '
                  'quick version. With A, the next page shows the new checklist in full, step by step, for your OK.'),
     spans=[whole(P('B3')), whole(P('B68'))], card_after=P('B4'))

# ---------------------------------------------------------------- inside the long part

core = [P('B144', k) for k in range(5)]
card(id='RP-1', type='repeat', advice='approve', title='The brain-damage order, told twice in the long part',
     what=('The numbered Core Order list moves up into "If Someone Says “My Brain Feels Damaged”", in place of the '
           'paragraph that says the same steps in prose ("After DMSO, the second move depends on the drug..."). The '
           'list\'s heading ("The Core Order When the Brain Feels Damaged") and the paragraph after it ("After medical '
           'danger, environment, dose...") go. Item 4 drops its last sentence, which the beach morning glory section '
           'says ("I do not yet have data showing that pes-caprae aborts MDMA").'),
     why=('The section and the list give the same five steps (DMSO first, check the symptoms, pes-caprae for a '
          'psychedelic, magnesium for MDMA, medics in parallel), in two sections a few screens apart. The list is quicker to '
          'follow in a crisis and has one thing the prose doesn\'t (the Metta NMT sniffer). '
          'The paragraph after the list says the remedies are done ("After medical danger ... have been considered"), '
          'but the remedies come after it; "That finishes the rescue-chemistry side of the guide" already does that job '
          'at the right place.'),
     stays=('The section keeps its reasons and evidence: why you take the report seriously, the checks, the stroke '
            'studies, and the treatment-window warning with "while someone calls medics".'),
     deciding='Whether you\'d rather keep the prose and drop the list (then the sniffer goes into the prose).',
     advice_note='Approve: the list is your clearest version, and it sits where a reader in trouble looks.',
     found_by='my read; readers A and B',
     edits=[cut_block(P('B107')), cut_block(P('B143')), cut_words(core[3], ' I do not yet have data that pes-caprae aborts MDMA.'),
            cut_block(P('B145'))],
     moves=[{'blocks': core, 'before': P('B108'), 'seq': 1}],
     spans=[whole(P('B107')), whole(P('B143')), span_of(core[3], 'I do not yet have data that pes-caprae aborts MDMA.'),
            whole(P('B145'))],
     card_after=P('B107'))

card(id='RP-2', type='repeat', advice='approve', title='Beach morning glory repeats the brain-damage order',
     what='"When somebody says their brain feels damaged, I am not interested in merely calming the experience anymore. '
          'I use DMSO first, then pes-caprae to terminate the psychedelic state." goes.',
     why=('It is the brain-damage order again, told inside the plant\'s own section; the section on the brain-damage '
          'feeling gives it with the steps around it.'),
     stays=('The plant\'s section keeps that it is your sledgehammer for stopping a psychedelic trip, the dose warning, '
            'the woman you gave it to, and that you have no data on MDMA.'),
     deciding='Whether a reader who lands on this section first needs the reminder of when to use it.',
     advice_note='Approve.', found_by='my read; readers A and B',
     edits=[cut_block(P('B177'))], spans=[whole(P('B177'))])

card(id='SF-1', type='safety', advice='approve', title='When to call for help, in one section',
     what=('"When Peer Support Isn\'t Enough" moves, with its three paragraphs (when to get urgent help; "I might kill '
           'someone to test this theory"; local emergency services, 988 and 911), from the tripsitting part up into '
           '"When to Bring In Outside Help", as its third part, under its own heading at the same level as the other '
           'two. The mental-health list\'s first item ("The person may be unsafe to themselves or others.") goes, since '
           'the moved paragraph says it with the details.'),
     why=('Today the guide lists when to call for help in about seven places (checklist steps 1 and 9, the Longer Triage, '
          'the two lists here, When Peer Support Isn\'t Enough, and the harm section). You asked for the safety lines in one '
          'spot: this puts the medics list, the mental-health list and the urgent-help paragraph together where a '
          'reader looks for them.'),
     stays=('The danger signs in checklist step 1, and the call-for-help lines inside each emergency (the seizure\'s '
            'five minutes, the chest-pain line, serotonin syndrome, the harm script), stay where the reader acts on '
            'them.'),
     deciding='Whether the tripsitting part should keep a one-line pointer to this section where the heading was.',
     advice_note='Approve.', found_by='my read; reader C',
     inserts=[{'before': P('B98'), 'kind': 'h2', 'text': 'When Peer Support Isn’t Enough', 'seq': 1}],
     moves=[{'blocks': [P('B276'), P('B277'), P('B278')], 'before': P('B98'), 'seq': 2}],
     edits=[cut_block(P('B275')), cut_block(P('B97', 0))],
     spans=[whole(P('B275')), whole(P('B97', 0))], card_after=P('B97', 6))

card(id='SF-2', type='safety', advice='leave', title='The seizure and chest-pain thresholds, in the list and in their sections',
     what=('A reader would cut "Call medics for a convulsive seizure lasting about five minutes..." from Active Seizure, '
           'since the medics list says the same seizure line (and the chest-pain section\'s thresholds repeat the list\'s '
           'chest-pain line).'),
     why=('Someone in the middle of a seizure or a chest-pain scare is reading that section, not the list: the threshold '
          'changes what they do right there. The list is for scanning before anything happens.'),
     stays='Both stay as they are, unless you say otherwise.',
     deciding='Whether two places is one too many for these two thresholds.',
     advice_note='Leave: each is where the reader acts on it, which is your rule for safety lines.',
     found_by='reader B',
     edits=[cut_block(P('B112'))], spans=[whole(P('B112'))])

card(id='RP-3', type='repeat', advice='approve', title='"Medics in parallel", said again',
     what=('"Some branches call for medics in parallel. Others describe severe but physiologically stable altered '
           'states where a fast field remedy may be more useful than waiting hours to be given a generic sedative." '
           'goes from the opening of My Acute Rescue Hierarchy.'),
     why=('"An emergency means act now...", which opens the section before (Acute Medical and Neurological Rescue), '
          'says both.'),
     stays='The hierarchy\'s first sentence stays: it is for acute situations, not merely uncomfortable trips.',
     deciding='None that I can see.', advice_note='Approve.', found_by='my read',
     edits=[cut_words(P('B139'), 'Some branches call for medics in parallel. Others describe severe but physiologically '
                                 'stable altered states where a fast field remedy may be more useful than waiting hours '
                                 'to be given a generic sedative.')],
     spans=[span_of(P('B139'), 'Some branches call for medics in parallel.')])

card(id='RP-4', type='repeat', advice='approve', title='Why the hierarchy comes first, said a third time',
     what='"The hierarchy appears before the mystical sections because love doesn’t require us to ignore the body..." '
          '(the whole paragraph) goes.',
     why=('The two paragraphs before it make the point (not every crisis is emotional; a gut or brain problem belongs '
          'in a different branch), and "Every hard experience is not a profound lesson..." in Why Bad Trips Tend to '
          'Happen says its last two lines.'),
     stays='"Psychedelic culture often treats every crisis as emotional or spiritual..." and the paragraph after it.',
     deciding='Whether "A gut-driven mental hell is not automatically shadow work" is a line you want to keep somewhere.',
     advice_note='Approve.', found_by='my read; reader A',
     edits=[cut_block(P('B142'))], spans=[whole(P('B142'))])

card(id='RP-5', type='repeat', advice='approve', title='Swallowing charcoal, explained twice',
     what='"Ingesting the charcoal itself can improve toxic gut feelings while also adsorbing the drugs and reducing the '
          'trip. I generally avoid the charcoal itself unless losing part of the trip is acceptable." goes.',
     why='Actual Activated Charcoal, a few sections up, says both: it can help gut toxicity, it adsorbs drugs and can '
         'reduce a trip, and you use zeolite when you want to keep the trip.',
     stays='The charcoal-water section keeps its first line ("...different from zeolite and from swallowing charcoal") '
           'and goes straight on to "What I usually use is the water portion".',
     deciding='None that I can see.', advice_note='Approve.', found_by='my read',
     edits=[cut_block(P('B191'))], spans=[whole(P('B191'))])

card(id='RP-6', type='repeat', advice='approve', title='Music: the same two points in two places',
     what=('In The First Five Minutes, "Music is optional." and "and keep the person able to stop or change it immediately" '
           'go. The paragraph reads: "Ask “music or quiet?” If a track starts pulling the experience somewhere unwanted, '
           'change it. This is a bad time to defend the playlist."'),
     why=('The Grounding Menu\'s Music list says both ("Silence is a real option." and "Keep the stop or change control '
          'immediate..."), and both repeat readers took the menu as music\'s home.'),
     stays='The Music list stays whole: silence, familiar music, no forced arc, drumming or harp-like music, the stop control.',
     deciding='Whether you\'d rather keep this paragraph whole and trim the menu instead.',
     advice_note='Approve.', found_by='my read; readers A and B',
     edits=[replace_words(P('B241'), 'Music is optional. Ask “music or quiet?” and keep the person able to stop or change it '
                                     'immediately.', 'Ask “music or quiet?”')],
     spans=[span_of(P('B241'), 'Music is optional.'), span_of(P('B241'), 'and keep the person able to stop or change it immediately')])

card(id='RP-7', type='repeat', advice='approve', title='Movement, in the menu again',
     what=('Two items go from the Grounding Menu\'s Body list ("Try two minutes of safe movement: ..." and "Then ask '
           'whether movement made you clearer or more impulsive..."), and two from its Ordinary world list ("Do one '
           'ordinary task you can clearly finish when the body wants movement." and "Pace along a clear contained path '
           'when pacing helps.").'),
     why='Stillness or Movement? says the two-minute test and its question, pacing in a contained space, and the small '
         'task with an endpoint; Alone at 3 a.m. lists the movements (pacing, stretching, a few slow wall push-ups).',
     stays='The Body list keeps feet, hands on heart and belly, something with weight, unclenching. Ordinary world keeps '
           'food, walking with a sober person, going outside safely, and the strenuous-exercise warning.',
     deciding='"Shaking out the arms and legs" is said only here and in checklist step 4; if step 4 shrinks too, say if you '
              'want it kept somewhere.', advice_note='Approve.', found_by='my read; reader B',
     edits=[cut_block(P('B298', 4)), cut_block(P('B298', 5)), cut_block(P('B312', 1)), cut_block(P('B312', 2))],
     spans=[whole(P('B298', 4)), whole(P('B298', 5)), whole(P('B312', 1)), whole(P('B312', 2))],
     card_after=P('B312', 5))

card(id='RP-8', type='repeat', advice='approve', title='The lead anchor\'s backup, in the menu again',
     what='"When safety is slipping, let that person bring in one additional calm adult or crisis professional." goes '
          'from the Grounding Menu\'s Human list.',
     why='Get One Human Anchor says it, and says when ("When safety, fatigue, logistics, violence, or self-harm risk '
         'exceeds what one person can hold...").',
     stays='The Human list keeps asking one calm person, letting them remind you where you are, and not processing with '
           'the most reactive person in your life.',
     deciding='None that I can see.', advice_note='Approve.', found_by='my read; readers A and B',
     edits=[cut_block(P('B308', 2))], spans=[whole(P('B308', 2))])

card(id='RP-9', type='repeat', advice='approve', title='Practice-induced states, told twice',
     what='"For practice-induced states: “I stopped the practice. Food, ordinary contact, and sleep help the system come '
          'down.”" goes from the Grounding Menu\'s Time list.',
     why='The First Five Minutes says it ("A non-drug altered state may have a less predictable clock... stop the '
         'practice, eat something ordinary when safe, let the body settle, keep warm, and sleep."), along with the '
         'line to say ("I am in an intense state. I am stopping the practice now...").',
     stays='The Time list keeps the date and place, effects rising and changing, and tomorrow\'s notebook.',
     deciding='None that I can see.', advice_note='Approve.', found_by='my read',
     edits=[cut_block(P('B310', 2))], spans=[whole(P('B310', 2))])

card(id='RP-10', type='repeat', advice='approve', title='"Don\'t debate to win", twice in one section',
     what='"Don’t debate to win. Don’t validate violence." goes from When the Content Turns Toward Harm; the paragraph '
          'starts at "Redirect within the person’s value-world...".',
     why='The Don\'t list just above opens with the same two points ("Don’t try to win an argument with visions... '
         'Don’t validate harmful conclusions.").',
     stays='The rest of the paragraph: redirect toward peace and protection, more containment, crisis support early.',
     deciding='None that I can see.', advice_note='Approve.', found_by='my read; reader A',
     edits=[cut_words(P('B290'), 'Don’t debate to win. Don’t validate violence. ')],
     spans=[span_of(P('B290'), 'Don’t debate to win. Don’t validate violence.')])

card(id='RP-11', type='repeat', advice='approve', title='"Nondual demonology", the same line twice',
     what='"Don’t teach nondual demonology to somebody who needs the lights down and a doctor." goes from the Don\'t '
          'list for the person helping.',
     why='The same sentence closes Demons, Jinn, Entities, and Shadow Forces, word for word, where demonology is the '
         'subject and it follows "stabilize first".',
     stays='The Don\'t list\'s other four items.', deciding='Whether you\'d rather keep it in the list and cut it there.',
     advice_note='Approve.', found_by='my read; readers A and B',
     edits=[cut_block(P('B284', 4))], spans=[whole(P('B284', 4))])

card(id='RP-12', type='repeat', advice='approve', title='"If it’s true, it survives breakfast", twice',
     what='"“If it’s true, it survives breakfast.”" goes from the Other useful lines in When the Content Turns Toward '
          'Harm.',
     why='When the Trip Feels Amazing ends on the full version ("The revelation will still exist after breakfast. If it '
         'is true, it survives sleep. If it cannot survive one night of rest, it was an emergency impulse wearing angel '
         'wings."), and the checklist has it too.',
     stays='The other two lines ("Maybe you are touching something divine..." and "Tonight the commandment is no harm, '
           'no proof, no mission, sleep first.").',
     deciding='Whether it works better as a line a sitter says than as the section\'s ending.',
     advice_note='Approve.', found_by='my read; readers A and B',
     edits=[cut_words(P('B289'), '“If it’s true, it survives breakfast.” ')],
     spans=[span_of(P('B289'), '“If it’s true, it survives breakfast.”')])

card(id='RP-13', type='repeat', advice='leave', title='No entity or revelation overrides safety, twice',
     what=('A reader would cut "No entity, deity, demon, ancestor, angel, algorithm, mission, kundalini surge, or insight '
           'overrides basic safety." from No Rash Actions, since Demons, Jinn, Entities has its own safety rule ("Even a '
           'completely real-feeling entity does not make decisions for your body...").'),
     why='It is the same rule, but in two situations a reader meets separately: a revelation pushing you to act, and an '
         'entity telling you to.',
     stays='Both stay as they are, unless you say otherwise.',
     deciding='Whether a reader would feel told the same thing twice.',
     advice_note='Leave: each sits where a reader in that situation looks.', found_by='readers A and B',
     edits=[cut_words(P('B320'), ' No entity, deity, demon, ancestor, angel, algorithm, mission, kundalini surge, or '
                                 'insight overrides basic safety.')],
     spans=[span_of(P('B320'), 'No entity, deity, demon, ancestor, angel, algorithm, mission, kundalini surge, or insight '
                               'overrides basic safety.')])

card(id='RP-14', type='repeat', advice='approve', title='Two "Additional Resources" headings, and the support lines a third time',
     what=('The appendix\'s second heading ("Additional Resources", and the divider above it) goes, so the appendix is one '
           'list under "Appendix: Additional Resources"; its note ("If somebody is actively in trouble, use the checklist '
           'first...") moves up to open it. "Free tripsitting hotline at The Fireside Project as well as ICEERS.org" goes.'),
     why='The appendix has two headings with the same name. Fireside and ICEERS are in Who to Contact, and When, with their '
         'hours, coverage and what each is for.',
     stays='Every other resource in the appendix: alternativementalhealth.com, the Berkeley class, Ajahn Jayasaro, your '
           'visions answer, the Hopkins/Griffiths protocol, the Zendo manuals and the Greer and Tolbert method.',
     deciding='None that I can see.', advice_note='Approve.', found_by='my read; readers A and B',
     edits=[cut_block(P('B435')), cut_block(P('B436')), cut_block(P('B438', 1))],
     moves=[{'blocks': [P('B437')], 'before': P('B433', 0), 'seq': 1}],
     spans=[whole(P('B436')), whole(P('B437')), whole(P('B438', 1))], card_after=P('B438', 1))

card(id='RP-15', type='repeat', advice='approve', title='Calling medics while using a remedy, said twice',
     what=('In the first paragraph of Acute Medical and Neurological Rescue, "Some symptom patterns call for medics while you '
           'use an immediate remedy; " goes, so the sentence starts "Some severe but physically stable altered states may '
           'respond faster to field rescue..."'),
     why=('The line under the medics list, a few lines up, says it ("The remedies below can begin while help is '
          'being arranged...") and adds that using a remedy doesn\'t mean giving up a time-sensitive medical option. All three readers took that '
          'line as the home of the point.'),
     stays='"An emergency means act now", the ambulance line, and the stable-state line.',
     deciding='None that I can see.', advice_note='Approve.', found_by='readers A, B and C',
     edits=[replace_words(P('B100'), 'Some symptom patterns call for medics while you use an immediate remedy; some severe',
                          'Some severe')],
     spans=[span_of(P('B100'), 'Some symptom patterns call for medics while you use an immediate remedy;')])

card(id='RP-16', type='repeat', advice='approve', title='Magnesium: "not one exceptional episode" says the paragraph before again',
     what='"This was not one exceptional episode. I have repeatedly needed large amounts when taking MDMA. My practical endpoint '
          'is the jaw releasing, rather than taking one conventional supplement dose and assuming the problem has been handled." '
          'goes.',
     why='The paragraph before says each part: "On multiple occasions", the amounts, "A token dose may not be enough", and '
         '"before my jaw fully released".',
     stays='Every dose, amount and timing in the magnesium paragraphs (they are all in the paragraph before).',
     deciding='Whether "my practical endpoint is the jaw releasing" says it more plainly than the paragraph before does.',
     advice_note='Approve.', found_by='reader A',
     edits=[cut_block(P('B116'))], spans=[whole(P('B116'))])

card(id='RP-17', type='repeat', advice='approve', title='Zeolite\'s symptom list, a fourth time',
     what='"Zeolite is what helps me when mental distress seems driven by gut toxicity, parasite die-off, nausea, diarrhea, '
          'or the sick-stomach feeling." goes; the paragraph keeps "That water doesn’t fix the gut the way zeolite does."',
     why='The zeolite section lists the same symptoms ("sick stomach, nausea, diarrhea, toxic heaviness, a dirty body-feeling, '
         'parasite die-off..."), as do checklist step 10 and the start of the hierarchy.',
     stays='The contrast: the water acts on the overloaded mind, zeolite on the gut (the next paragraph says the first half).',
     deciding='None that I can see.', advice_note='Approve.', found_by='readers A and B',
     edits=[cut_words(P('B193'), ' Zeolite is what helps me when mental distress seems driven by gut toxicity, parasite die-off, '
                                 'nausea, diarrhea, or the sick-stomach feeling.')],
     spans=[span_of(P('B193'), 'Zeolite is what helps me when mental distress seems driven by gut toxicity')])

card(id='SF-3', type='safety', advice='approve', title='Not inhaling ozone, said four times',
     what='"I am never recommending ozone inhalation." goes from the charcoal-water paragraph; its instruction stays ("I mean the '
          'water after active ozonation has ended and residual ozone has dissipated.").',
     why=('The guide says you mean the water, not ozone gas, at its first mention (the zeolite: "I mean ozonating water, '
          'never inhaling ozone gas"), again here, again beside the crying baby ("No ozone gas was present"), and in the '
          'story of the time you smelled it ("I don’t recommend inhaling ozone."). The first mention and the story are the '
          'two a reader needs.'),
     stays='The zeolite line, the baby line, your story, and this paragraph\'s next sentence (the water after ozonation has ended).',
     deciding='Whether you\'d rather keep this line and drop the one at the end of your story.',
     advice_note='Approve.', found_by='readers A, B and C (C would keep this line and cut the one in your story)',
     edits=[cut_words(P('B192'), 'I am never recommending ozone inhalation. ')],
     spans=[span_of(P('B192'), 'I am never recommending ozone inhalation.')])

card(id='SF-4', type='safety', advice='approve', title='A caveat about the evidence labels that changes nothing',
     what='"I use the strongest applicable evidence without pretending every useful rescue has already received the trial it '
          'deserves." goes from How I label the evidence.',
     why='The four labels above it already say how strong each kind of evidence is; this line defends them and changes nothing '
         'a reader does.',
     stays='The four labels.', deciding='None that I can see.', advice_note='Approve.', found_by='reader C',
     edits=[cut_block(P('B149'))], spans=[whole(P('B149'))])

card(id='RP-18', type='repeat', advice='approve', title='Love becoming practical, twice',
     what='"Grounding is love becoming practical." goes from the start of the Grounding Menu; it starts "Choose one or two '
          'options rather than all of them."',
     why='Stillness or Movement? ends on the same line ("When the nervous system is on fire, love becomes practical first."), '
         'earlier in the same part.',
     stays='The menu\'s advice to choose one or two, and why.',
     deciding='Whether it works better as the menu\'s first line than as that paragraph\'s last.',
     advice_note='Approve.', found_by='reader A',
     edits=[cut_words(P('B295'), 'Grounding is love becoming practical. ')],
     spans=[span_of(P('B295'), 'Grounding is love becoming practical.')])

card(id='RP-19', type='repeat', advice='approve', title='Shadow work defined twice, four paragraphs apart',
     what='In the Eshwar sentence, "—bringing love and awareness to trauma-formed negative states and tendencies—" goes: "My '
          'friend Eshwar, however, found that shadow work made up about 99% of his path to heart-chakra awakening."',
     why='"Shadow work to me is neither BDSM nor “feeding your demons.” It means bringing loving awareness to the parts of the '
         'mind built in fear..." defines it in full four paragraphs later.',
     stays='Eshwar and his 99%.', deciding='Whether a reader needs the short definition the first time shadow work comes up.',
     advice_note='Approve.', found_by='readers A and B',
     edits=[replace_words(P('B340'), 'shadow work—bringing love and awareness to trauma-formed negative states and tendencies—made up',
                          'shadow work made up')],
     spans=[span_of(P('B340'), '—bringing love and awareness to trauma-formed negative states and tendencies—')])

card(id='RP-20', type='repeat', advice='approve', title='Life forcing the lesson, twice, three paragraphs apart',
     what=('"Sometimes the real-world smackdown is unavoidable for deeper learning." goes, and so does "I would love for '
           'everybody to do this in the safe room." from the paragraph that starts "Skip this inner work".'),
     why=('The two passages tell the same three steps: skipped shadow work shows up in life, the safe room is better, and '
          'sometimes life forces it. Your marriages line and your wish for the safer rooms stay in the first; the second keeps '
          'where it leaks and "the morning you realize the enlightened persona was mostly a nice outfit".'),
     stays='"When shadow work is bypassed..." with your two marriages; "Skip this inner work..." without the safe-room sentence.',
     deciding=('The first sentence of each passage still says the same thing ("When shadow work is bypassed... it may appear in '
               'ordinary life" and "Skip this inner work, and the trauma doesn’t vanish"); say if you want one of them to go too.'),
     advice_note='Approve.', found_by='readers A and B (they differ on which passage to keep)',
     edits=[cut_block(P('B343')), cut_words(P('B346'), 'I would love for everybody to do this in the safe room. ')],
     spans=[whole(P('B343')), span_of(P('B346'), 'I would love for everybody to do this in the safe room.')],
     card_after=P('B346'))

card(id='RP-21', type='repeat', advice='approve', title='The planned-session list, then the same list as arrows',
     what='"Preparation → physical safety → intention → low-directivity support → closure → sleep and food → next-day '
          'integration." goes; "Use this sequence for planned sessions..." follows the list directly.',
     why='It says the list just above it again, in the same order ("Integration time" becomes "sleep and food → next-day integration").',
     stays='The list, and "Use this sequence for planned sessions. Once somebody is already in trouble, return to the acute '
           'checklist..."',
     deciding='Whether the one-line chain helps as a summary to remember.', advice_note='Approve.', found_by='reader A',
     edits=[cut_block(P('B369'))], spans=[whole(P('B369'))])

card(id='RP-22', type='repeat', advice='approve', title='The calm pet, twice in the Grounding Menu',
     what='In the Body list, "or sit near a calm pet when that feels safe" goes; the item reads "Hold something with weight or texture."',
     why=('The next entry, A familiar object, says it with more care: "A calm pet can offer the same quiet company when the '
          'animal is comfortable and the situation is safe." Both repeat readers took that line as the home.'),
     stays='The familiar-object entry, its pet line included.',
     deciding='Whether the pet belongs with the body practices rather than with the familiar object; then the other line goes instead.',
     advice_note='Approve.', found_by='readers A and B',
     edits=[replace_words(P('B298', 2), 'Hold something with weight or texture, or sit near a calm pet when that feels safe.',
                          'Hold something with weight or texture.')],
     spans=[span_of(P('B298', 2), ', or sit near a calm pet when that feels safe')])

card(id='RP-23', type='repeat', advice='approve', title='The helper\'s Do and Don\'t lists: two lines said just above',
     what='"Speak slowly and use fewer words." goes from the Do list, and "Don’t crowd them with five worried friends." from the Don\'t list.',
     why=('The First Five Minutes says the first word for word ("Ask before touching. Speak slowly and use fewer words. Please '
          'don’t explain the universe at somebody who is already frightened by it."), and Get One Human Anchor says the second '
          'with its reason ("A committee of frantic people rarely improves anyone’s nervous system."). Both repeat readers '
          'found both.'),
     stays='The rest of both lists.',
     deciding=('Whether you want the Do and Don\'t lists complete on their own, for a helper who reads only that section; then '
               'both lines stay.'),
     advice_note='Approve.', found_by='readers A and B',
     edits=[cut_block(P('B282', 0)), cut_block(P('B284', 2))],
     spans=[whole(P('B282', 0)), whole(P('B284', 2))], card_after=P('B284', 2))

# ---------------------------------------------------------------- questions only you can answer

card(id='Q-1', type='question', advice='ask', title='Humic acid: lick it first, or smell it first?',
     question=('The Core Order\'s first step says "Smell humic acid, take a 5mg lick of it", and Humic Acid Brings Brain to '
               'Optimal Function says a 5mg lick sends your brain "into hyperfunctionality". Some Remedies Require More '
               'Caution says eating it "can produce a hyperintelligent state", could destabilize somebody prone to mania, '
               '"I wouldn’t use it casually during a bad trip", and "I’d start with" smelling it. Which should the guide '
               'say for someone whose brain feels damaged: (a) smell it, and lick a tiny bit only if smelling doesn\'t '
               'help and they aren\'t prone to mania; (b) smell it and lick 5mg, as the Core Order says; (c) your words?'),
     why='A reader who follows the Core Order would do what the caution section warns against.',
     stays='All three passages stay as they are until you answer.',
     advice_note='(a): it fits both passages, and the lick stays available when smelling isn\'t enough.',
     spans=[span_of(P('B144', 0), 'Smell humic acid, take a 5mg lick of it.'),
            span_of(P('B219'), 'I wouldn’t use it casually during a bad trip.')],
     card_after=P('B144', 0))

card(id='Q-2', type='question', advice='ask', title='Where does "Hello, Lovey Bunny!" go?',
     question=('Your greeting, the MAPS video and the Challenging Psychedelic Experiences Project paragraph sit under '
               'Shadow Work and Tripsitting Yourself or Others, about 7,500 words into the post, where the post first '
               'began. (a) Leave them there, as the opening of the tripsitting and shadow-work half; (b) move the greeting '
               'to the very top, above the checklist; (c) your words?'),
     why='A reader meets the greeting after the medical chemistry, which reads like a second start.',
     stays='Everything stays where it is until you answer.',
     advice_note='(a): someone opening the guide in trouble needs the checklist first, and the greeting opens the half '
                 'they read once they are safe.',
     spans=[whole(P('B231'))])

card(id='Q-3', type='question', advice='ask', title='DMSO first: two cautions from the DMSO section',
     question=('The brain-damage branch puts DMSO first, whatever the drug. The DMSO section says "Don’t take it with drugs '
               'that should not absorb rapidly, including corticosteroids, NSAIDs, and harmalas", and ayahuasca is a harmala '
               'brew (the serotonin section says "harmala/ayahuasca-type MAOI exposure"). It also says "Don’t combine it with '
               'blood-thinning medication because DMSO also thins the blood", while the stroke paragraph uses DMSO at once '
               'though "DMSO cannot identify whether the problem is a clot, a hemorrhage". What holds for (a) someone on '
               'ayahuasca and (b) a possible bleed? If DMSO still comes first in both, the DMSO section is what changes; if '
               'not, the brain-damage branch says what to do instead. Tell me which, in your words, and I\'ll draft the line '
               'for your OK.'),
     why='A reader in that situation meets both instructions and can\'t follow both. Readers A and B each found this.',
     stays='Everything stays as it is until you answer.',
     advice_note='This one is yours: only you know what you do with DMSO in these two cases.',
     spans=[span_of(P('B205', 2), 'and harmalas'), span_of(P('B205', 4), 'because DMSO also thins the blood'),
            span_of(P('B106'), 'DMSO cannot identify whether the problem is a clot, a hemorrhage')],
     card_after=P('B106'))

card(id='Q-4', type='question', advice='ask', title='How long the action lock lasts',
     question=('The 3 a.m. note in checklist step 6 says "No big actions until morning." No Rash Actions says "Use a 24–72 hour action lock." and '
               '"Until you have slept and eaten, don’t drive...". (a) Leave them: the note covers the first night and the lock '
               'is the full rule; (b) make the 3 a.m. note say the same as the lock; (c) your words. (The Alone at 3 a.m. '
               'section quotes the note as "No actions until morning", without "big"; I\'d make it match whichever you pick.)'),
     why='Readers A and B each found the three lengths, with nothing saying which applies when.',
     stays='All three stay as they are until you answer.',
     advice_note='(a): each fits the person reading it, and the lock section is where the full rule lives.',
     spans=[span_of(P('B31'), 'No big actions until morning.'), span_of(P('B272'), 'No actions until morning'),
            whole(P('B317')), span_of(P('B318'), 'Until you have slept and eaten')], card_after=P('B318'))

card(id='Q-5', type='question', advice='ask', title='Room first, or body first?',
     question=('The checklist says "Use this in order." and puts the room before the body ("fix the room, help the body, find '
               'one calm human"). Stillness or Movement?, the fear loop and the shadow-thoughts section put the body first '
               '("body → room → human → time"). (a) Room first everywhere, as the checklist says; (b) body first everywhere; '
               '(c) leave them, if the difference is on purpose.'),
     why='A reader who follows the checklist and then the loop breaker gets two orders, with no reason for the change.',
     stays='All four places stay as they are until you answer.',
     advice_note='(a): the checklist is the order the reader is told to follow; only the word order changes in the other three.',
     spans=[span_of(P('B4'), 'fix the room, help the body'), span_of(P('B252'), 'body → room → human → time → meaning'),
            span_of(P('B375', 2), 'body → room → human → time'), span_of(P('B415'), 'body, room, human, time, and love')],
     card_after=P('B252'))

card(id='Q-6', type='question', advice='ask', title='Ocean water and charcoal water: different, or alike?',
     question=('Ocean water\'s section says its effect is "different from DMSO, aged ozonated-charcoal water, zeolite, or beach '
               'morning glory". The next section opens, right under its heading, "These work similarly to ocean water." (a) Take '
               '"aged ozonated-charcoal water" out of the first list; (b) change the second to say how they differ; (c) your '
               'words.'),
     why='Read together, the two lines say opposite things.',
     stays='Both stay as they are until you answer.',
     advice_note='(a): it takes one item out of that list and keeps both sections as you wrote them.',
     spans=[span_of(P('B188'), 'aged ozonated-charcoal water'), span_of(P('B190'), 'These work similarly to ocean water.')],
     card_after=P('B190'))

card(id='Q-7', type='question', advice='ask', title='Charcoal: only after a recent oral ingestion?',
     question=('Checklist step 12 (stopping a trip) says "Charcoal belongs only in the separate recent-oral-ingestion branch." '
               'The gut tools use it outside that branch: "Activated charcoal can help gut toxicity, but it adsorbs drugs. '
               'Sometimes that is exactly the point.", "When the goal is to reduce drug absorption or stop a toxic gut '
               'situation, charcoal may be relevant.", and after a ferment, "which then requires activated charcoal to reduce '
               'gut histamine". (a) Limit the sentence to stopping a trip: "To stop a trip, charcoal belongs only in the '
               'separate recent-oral-ingestion branch."; (b) take that sentence out of step 12; (c) your words.'),
     why=('A reader who follows step 12 would never use charcoal for the gut problems the long part uses it for. Readers A '
          'and B each found this.'),
     stays='Everything stays as it is until you answer.',
     advice_note=('(b): step 12\'s next paragraph and step 10 already say when charcoal fits and when it is dangerous, so '
                  'nothing is lost and the contradiction goes.'),
     spans=[span_of(P('B54'), 'Charcoal belongs only in the separate recent-oral-ingestion branch.'),
            span_of(P('B154'), 'which then requires activated charcoal to reduce gut histamine'),
            span_of(P('B160'), 'Activated charcoal can help gut toxicity'),
            span_of(P('B161'), 'or stop a toxic gut situation, charcoal may be relevant')],
     card_after=P('B161'))
