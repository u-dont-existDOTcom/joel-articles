# The cards of round 6, read by build_r06.py (which defines P, T, whole, span_of, replace_words and card). P('N-CBD-2')
# is the page block of GUIDE-SO-FAR-blocks.json's N-CBD-2 (the guide after round 5): his second CBD paragraph, the one on
# topical CBD. The sources were opened on 2026-11-04 between 22:50 and 23:30 UTC (the trial's full text through Europe
# PMC and the FDA label as text, from his laptop; every link below answered 200 from there).

BUILT = '2026-11-05'
H = 'https://www.pangram.com/history/'

INTRO = [
    'Version 2 of this page (2026-11-05, after your research of 00:13 UTC). Every new paragraph on it was checked in '
    'Pangram on your account first; each card says what it read, with the links.',
    'Two of my paragraphs passed: the trial sentences (Human Written, 0%) and the warning-stage paragraph (Human, High). Two '
    'didn\'t, after four tries each with your making-sense read and a tell panel: the cannabis paragraph from your research '
    'and the first five minutes\' movement paragraph, which even takes your dangers paragraph to AI when it follows it. '
    'Those two are yours to rewrite if you will, like round 5.',
]

TYPES = {
    'yours': {'label': 'Your version', 'about': 'a paragraph every version of mine read AI on: your words are the fix'},
    'more': {'label': 'Says more than the study', 'about': 'a point the paper backs only in part, changed to what it shows'},
    'new': {'label': 'From your note', 'about': 'something you mentioned, checked against its sources, as a line for the guide'},
}

TRIAL_OLD = ('and it did show that transdermal absorption works like oral CBD\'s but the dosing was too low, and transdermal '
             'CBD also doesn\'t get converted to the potentially more active form (7-OH-CBD) by the liver.')
TRIAL_NEW = ('and it didn\'t do any better than placebo. The gel got CBD into the blood at about the levels of the starting '
             'oral dose, 5 to 10mg/kg. The approved oral doses go up to 20 or 25mg/kg a day, so the dosing may have been '
             'too low. And CBD through the skin goes straight into the blood, while swallowed CBD passes through the liver '
             'first. The liver is where some of it gets converted to 7-OH-CBD, which stopped seizures in mice about as well '
             'as CBD itself, so the gel may have missed out on that too.')

card(id='CBD-TRIAL', type='more', advice='approve', title='The skin-gel trial: what it found, and the 7-OH-CBD point',
     reading=('Your three CBD paragraphs as they are now, with your video link, read [Human Written, 0%%](%s01b892a4-ee16-4f06-bb77-52090f1aa4e7), '
              'two windows High and two Low: "For focal seizures outside those syndromes, the evidence is mixed, but still '
              'long-term." and your last sentence, "I\'d treat it as a plausible experimental adjunct remedy ...".') % H,
     tested=('This paragraph with the new sentences, [Human Written, 0%%](%sb50d4304-fb72-49b6-a5cf-b55f1fd269a7): High, Medium, '
             'High, Medium, High (my second try; the first, [Human Written, 1%%](%sfc22bbd5-30f8-44fe-a91f-0558402a2430), read '
             'its 7-OH-CBD sentence Low, because it used "first pass" without saying what it meant).') % (H, H),
     what=('The end of your second CBD paragraph becomes: "... where they used a CBD skin gel, %s"' % TRIAL_NEW),
     why=('Three things, from the trial\'s paper ([O\'Brien et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9270696/)) '
          'and the [Epidiolex label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/210365s024s029s030lbl.pdf). '
          'First, the sentence never says what the trial found, so a reader can\'t tell why the dose comes up: neither dose '
          'of the gel cut seizures more than placebo did. Second, the paper doesn\'t say the dose was too low. It says the '
          'gel reached blood levels that "overlap those reported with oral cannabidiol (5-10 mg/kg)", and that benefit had '
          'been seen with higher gel doses (500 to 1,000mg a day) in children with other epilepsies; the label\'s oral '
          'doses start at 5mg/kg a day and go up to 20 (Lennox-Gastaut, Dravet) or 25 (tuberous sclerosis). So "may have '
          'been too low" holds, and "was too low" says more than anyone has shown. Third, CBD through the skin still gets '
          'broken down by the liver once it\'s in the blood; what it skips is the first pass, where swallowed CBD gets '
          'converted before it reaches the rest of the body. And 7-OH-CBD stopped seizures in mice about as well as CBD '
          'did, not better ([Whalley et al., AES 2017](https://aesnet.org/abstractslisting/the-human-metabolite-of-'
          'cannabidiol--7-hydroxy-cannabidiol--but-not-7-carboxy-cannabidiol--is-anticonvulsant-in-the-maximal-'
          'electroshock-seizure-threshold-test-(mest)-in-mouse)), so "potentially more active" goes.'),
     stays=('Your opening ("And topical CBD hasn\'t been well-studied. There was a short 12-week trial done, where they used '
            'a CBD skin gel"), your point that the dose may have been too low, and your 7-OH-CBD point, which still says '
            'why the skin route might do less.'),
     deciding=('The new words are mine, in your sentence\'s shape; they read Human. If you\'d rather say it your way, Revise '
               'with your words.'),
     advice_note='Approve.', found_by='checking your new points against the trial\'s paper (gate E348)',
     edits=[replace_words(P('N-CBD-2'), TRIAL_OLD, TRIAL_NEW)],
     spans=[span_of(P('N-CBD-2'), 'it did show that transdermal absorption works like oral CBD\'s but the dosing was too low'),
            span_of(P('N-CBD-2'), 'doesn\'t get converted to the potentially more active form (7-OH-CBD) by the liver')])

WARN = ('Some people get a warning before a seizure takes hold, which is called an aura. That\'s when the things people '
        'report can still stop it, depending on what sets their seizures off. If it\'s flashing or flickering light, cover '
        'one eye with a hand and turn away from the light, because closing the eyes doesn\'t block enough of it. Some people '
        'stop a seizure at the warning stage with a strong smell like jasmine, and some train themselves to link one smell '
        'with feeling calm and then sniff it when a seizure threatens. When overstimulation is what sets it off, a cool, '
        'quiet, dark and comfortable space can help.')

WARN_B = ('As for cannabis, people do smoke or vape it at the start of an aura, while they\'re still awake enough to do it on '
          'purpose. Some swear it stops the seizure from going any further, and there was one woman whose EEG showed fewer '
          'seizure discharges on the days she smoked. But other people say THC vapes and concentrates brought their '
          'seizures on, and in rats that get the brief staring seizures called absence seizures, high-THC smoke made them '
          'worse while injected CBD cut them about in half. So the THC may be what makes it go either way.')

card(id='SEIZ-WARN', type='new', advice='approve', title='What can help before a seizure takes hold, and cannabis at an aura (from your note and your research)',
     tested=('The first paragraph, [Human Written, 0%%](%s9b155e42-fc18-433e-9eb8-e53c737cbc50), one window, High (my second '
             'try; the first read [AI Detected, 26%%](%sf6fce8a6-b90d-4e4d-82f7-158db03e8ca8), its opening AI Low). The '
             'cannabis paragraph, four tries, all AI: [100%%](%sd0c33c95-5464-4a8f-8b75-28eaedc6e4c8) (High, Medium, High), '
             '[100%%](%sce0a18e3-fcf7-4e9c-bd45-8b96081343d9) (Medium, Low, Medium, High), [100%%](%sa93d2e44-7bfa-4308-b7f7-'
             '762fb9997b9b) (Medium, High, Medium) and the version on this card, [100%%](%s7e0bcdff-ef6d-432e-842f-'
             '24d7a0c30df8), one window, Medium.') % (H, H, H, H, H, H),
     what=('Two new paragraphs after your DMSO paragraph, before the call-for-help line: "%s" and "%s"' % (WARN, WARN_B)),
     inserts=[{'before': P('B112'), 'kind': 'p', 'text': WARN, 'seq': 1},
              {'before': P('B112'), 'kind': 'p', 'text': WARN_B, 'seq': 2}],
     why=('Your note listed what people report, the Epilepsy Foundation included, "but there\'s nothing that works for '
          'everyone of course". Checked one by one: covering one eye is the standard advice for light-triggered seizures, '
          'with a hand, and not closing the eyes ([Epilepsy Action](https://www.epilepsy.org.uk/info/seizure-triggers/'
          'photosensitive-epilepsy): "cover one eye with your hand and turn away. Do not close your eyes"). A strong smell '
          'at the warning stage stopped one patient\'s seizures in a classic case report ([Efron 1956](https://pubmed.ncbi.'
          'nlm.nih.gov/13364083/)), and in Tim Betts\'s clinic people who learned to link an oil\'s smell (jasmine, ylang '
          'ylang, lavender, camomile) with feeling relaxed smelled it when a seizure threatened; a third were seizure-free '
          'a year later, in a study with no control group ([Epilepsy Society, July 2026](https://epilepsysociety.org.uk/'
          'sites/default/files/2026-07/ComplementarytherapiesJuly2026.pdf), which also warns that some oils can make '
          'epilepsy worse). The cool, quiet, dark and comfortable space is your experience; I found no study of it. I left out splashing '
          'water (nothing I found, and first-aid advice for a seizure doesn\'t include it) and music (its studies are of '
          'listening every day for weeks, not during a seizure). All of these are for the warning stage: once someone is '
          'convulsing, the section\'s first paragraph and the call-for-help line are what applies, which is why it goes '
          'just before that line. The second paragraph is from your research of 00:13 UTC, each study checked on '
          'PubMed: the young woman\'s EEG ([Sivakumar et al. 2017](https://pubmed.ncbi.nlm.nih.gov/27763968/): fewer '
          'discharges between seizures on the days she smoked, and fewer seizure-length ones in the time-series '
          'analysis, though not in the first test), and the rats ([Roebuck et al. 2022](https://pubmed.ncbi.nlm.nih.gov/'
          '33370468/): high-THC smoke increased absence-seizure discharges, high-CBD smoke did nothing significant, '
          'injected CBD halved them). The aura reports are the forum posts your research quotes, and the THC vapes and '
          'concentrates on the other side are from the same threads. In a different model THC stopped seizures outright '
          '([Wallace et al. 2003](https://pubmed.ncbi.nlm.nih.gov/12954810/), rats with temporal-lobe epilepsy), so I '
          'didn\'t write that THC makes seizures worse in general. None of it is CBD alone, so your line that no study '
          'has tested CBD as a rescue still holds. Two people whose seizures came back hard when they stopped smoking '
          '([Hegde et al. 2012](https://pubmed.ncbi.nlm.nih.gov/23159379/)) I left out: it\'s about stopping, not the '
          'warning stage.'),
     stays='Everything else in the section, in its order.',
     deciding=('The first paragraph passed and can go in as it is. The cannabis paragraph still reads AI after four tries: the '
               'three readers on my second try all saw a balanced review (some say this, others say that, a study each way, '
               'a safety line to close; [their notes](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/'
               'bad-trips-20261103/articles/bad-trips/humanize/h05-checks-20261105/panel-B2/PANEL.md)), and moving the point '
               'first, then writing it the way your CBD paragraph brings in studies, each took it only from High to Medium. '
               'What it has to keep: people try it at the very start of an aura, while still awake enough to do it on '
               'purpose; some say it stops the seizure going further; the woman\'s EEG; others say THC vapes and '
               'concentrates brought seizures on; the rats (high-THC smoke worse, CBD better); and that THC may be why it '
               'goes either way.'),
     advice_note=('Revise with your version of the cannabis paragraph, and I\'ll put the first paragraph in as it is; or '
                  'Approve to take both as they are (the second reads AI), or Reject to leave both out.'), found_by='your note on the CBD card',
     spans=[whole(P('N-CBD-3'))], card_after=P('N-CBD-3'))


card(id='MOVE-YOURS', type='yours', advice='edit', title='The first five minutes: the movement paragraph, in your words',
     reading=('Never checked alone, since it\'s 17 words; the published post\'s check read it AI, High. With your dangers '
              'paragraph before it (which read Human alone), four versions of mine, each read AI, your paragraph included: '
              '[100%%](%s0993c7c4-386c-4a5b-821b-f15f3beb738d) (High, Medium, High, Medium), [100%%](%sf1b3e3bb-30f2-4399-8398-82bd3998b413), '
              '[100%%](%s525ce8ca-ff4d-49cd-a47f-6304b4217035) and [100%%](%s60fb8654-35a6-479d-b242-a9ee25f68002), the last three one window, High.') % (H, H, H, H),
     why=('This was my first how-to paragraph done your way, and the making-sense read wasn\'t enough. What I tried, in '
          'order: each rule given its purpose ("pacing can help them burn off some of the fear", "since that only makes it '
          'stronger and longer", "in case they get lost"); the three "if they want to" frames taken out, since mine echoed '
          'the last sentence of yours (all three readers named them: [their notes](https://github.com/u-dont-existDOTcom/'
          'joel-articles/blob/claude/bad-trips-20261103/articles/bad-trips/humanize/h05-checks-20261105/panel-P4D4/PANEL.md)); '
          'and each sentence made an act on a thing, the way yours are ("let them walk laps of the room or the yard", "Put '
          'the rest of whatever they took out of reach too", "walk with them"). Every one took your paragraph to AI with '
          'it, so whatever reads AI in mine, I can\'t see it. The last version: "Pacing is fine, so let them walk laps of '
          'the room or the yard if they need to. Put the rest of whatever they took out of reach too, since more only makes '
          'the trip stronger and longer. Having it out with somebody can wait until it\'s worn off, and if they insist on '
          'leaving the house, walk with them." What it has to keep: moving around is fine; no more of the substance; no '
          'confrontations; no leaving alone. "No driving" is in your dangers paragraph already, with the keys.'),
     advice_note=('Edit it: say it your way, keeping those points. Your version shows me what I\'m missing for the rest of the '
                  'how-to sections. Or Keep it as it is.'),
     found_by='the humanize pass, first section, the paragraph after yours',
     spans=[whole(P('B237'))])
