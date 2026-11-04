# The cards of round 3, read by build_r03.py (which defines P, T, whole, span_of, cut_block, cut_words, replace_words and
# card). P('B205', 2) is the page block of GUIDE-SO-FAR-blocks.json's B205, third list item. Every source below was opened
# on 2026-11-04 (PubMed, the drug labels and the AHA page); the check with all 149 lines is
# ../../experiments/t05-warnings/WARNINGS-CHECK.md.

BUILT = '2026-11-04'
CHECK = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261103/articles/bad-trips/experiments/t05-warnings/WARNINGS-CHECK.md'
FOUND = 'the warnings check (E344): its research helper\'s searches, with each source re-opened by me'

INTRO = [
    'You asked me to check the guide\'s warnings ("some of those warnings i\'m not even sure about i think many came from '
    'old stupid gemini models"). I checked every line in the rescue sections that states a risk, an interaction, a '
    'threshold or a "don\'t": 149 lines, against PubMed, drug labels and first-aid pages, with every source opened.',
    'Most hold up. 93 have something behind them and stay. 38 are your own experience and stay as yours, and 5 are your '
    'views, such as the emergency room lines, and stay too. 5 generic lines, such as "A vitamin is not automatically '
    'harmless", wait for the humanizing, where your rules on AI quips and "X does not Y" apply. These 9 cards are the '
    'rest: 2 warnings with nothing behind them, 5 lines that say more than their studies, a new study on beach morning '
    'glory, and the one place where the guide parts from the American Heart Association. Nothing changes until you '
    'approve it. The whole check is <a href="%s" target="_blank" rel="noopener noreferrer">here, line by line</a>.'
    % CHECK,
]

TYPES = {
    'nothing': {'label': 'Nothing behind it', 'about': 'a warning I found no study behind: it goes, unless it\'s your '
                'own experience'},
    'more': {'label': 'Says more than the studies', 'about': 'a line the studies back only in part, changed to what they '
             'show'},
    'new': {'label': 'New study', 'about': 'a study the guide doesn\'t mention yet, on one of your remedies'},
    'call': {'label': 'Your call', 'about': 'where the guide parts from standard advice'},
}

CBD_OLD = ('CBD has established antiseizure activity in several epilepsy syndromes, and transdermal CBD reaches systemic '
           'circulation, although it has not been validated as rapid seizure rescue.')
CBD_NEW = ('CBD has established antiseizure activity in several epilepsy syndromes. In a 12-week trial, a CBD skin gel '
           'reached the blood at levels like oral CBD\'s but did no better than placebo against focal seizures, and it '
           'hasn\'t been tested as rapid seizure rescue.')
card(id='W-CBD', type='more', advice='approve', title='CBD through the skin: what the linked trial found',
     what=('The CBD sentence becomes two: "%s" The link moves to "12-week trial".' % CBD_NEW),
     why=('The trial this line links gave 188 adults with focal epilepsy a CBD gel twice a day. It reached the blood at '
          'levels that "overlap those reported with oral cannabidiol", but over 12 weeks neither dose cut seizures more '
          'than placebo did (PubMed: [O\'Brien et al. 2022](https://doi.org/10.1001/jamanetworkopen.2022.20189)). So the '
          'link backs "reaches the blood", and a reader who opens it finds the gel didn\'t work for seizures.'),
     stays=('"CBD has established antiseizure activity in several epilepsy syndromes" (that\'s oral CBD, in Dravet and '
            'similar syndromes), your plan of topical DMSO with a known CBD preparation, and the DMSO seizure lines.'),
     deciding=('Whether the result changes your advice to consider topical CBD at all. It was a daily gel for focal '
               'epilepsy, not one dose in a crisis, so it doesn\'t settle the rescue question either way.'),
     advice_note='Approve.', found_by=FOUND,
     edits=[replace_words(P('B111'), CBD_OLD, CBD_NEW)],
     spans=[span_of(P('B111'), 'and transdermal CBD reaches systemic circulation, although it has not been validated as '
                    'rapid seizure rescue')])

card(id='W-SS', type='more', advice='approve', title='Which psychedelics bring on serotonin syndrome',
     what=('"Psychedelics" becomes "Ayahuasca and other MAOI brews", and "MAOIs" becomes "other MAOIs": "Ayahuasca and '
           'other MAOI brews, MDMA, DXM, many antidepressants, tramadol, linezolid, other MAOIs, and some opioids can '
           'contribute, especially in combinations."'),
     why=('One review\'s table lists LSD among the drugs tied to serotonin syndrome, with Syrian rue and harmine among the '
          'MAOIs (PubMed: [Scotton et al. 2019](https://doi.org/10.1177/1178646919873925)). A review of psychedelics and '
          'serotonin toxicity says true toxicity typically comes from an overdose or an MAOI, and that serotonergic drugs '
          'without an MAOI "are low risk in combination with psychedelics that also do not contain MAOIs" (PubMed: '
          '[Malcolm & Thomas 2022](https://doi.org/10.1007/s00213-021-05876-x)). So the psychedelics that carry the risk '
          'are the MAOI brews, and naming ayahuasca warns a reader who doesn\'t know it contains one.'),
     stays='The rest of the list and of the paragraph.',
     deciding='"Psychedelics" isn\'t wrong, since LSD is on one review\'s list. It\'s broader than the risk.',
     advice_note='Approve.', found_by=FOUND,
     edits=[replace_words(P('B130'), 'Psychedelics, MDMA, DXM, many antidepressants, tramadol, linezolid, MAOIs, and some',
                          'Ayahuasca and other MAOI brews, MDMA, DXM, many antidepressants, tramadol, linezolid, other '
                          'MAOIs, and some')],
     spans=[span_of(P('B130'), 'Psychedelics'), span_of(P('B130'), 'MAOIs, and some')])

card(id='W-ITCH', type='more', advice='approve', title='Why a ferment can make someone itch',
     what='"somebody low in histamine-processing bacteria" becomes "somebody who breaks down histamine poorly".',
     why=('Ferments are high in histamine, and itching is one of the signs of histamine intolerance. But the review on it '
          'puts the intolerance down mainly to low levels of DAO, an enzyme of the gut lining: one study it cites found '
          'low DAO in 80% of 316 people with symptoms (PubMed: [Comas-Basté et al. 2020](https://doi.org/10.3390/'
          'biom10081181)). The bacteria it discusses are the ones that make histamine, in food. Charcoal took out 61% of '
          'the histamine in fish sauce (PubMed: [In et al. 2024](https://doi.org/10.1016/j.foodchem.2024.140169)); no '
          'study tests it in the gut, so that part stays as your experience.'),
     stays='Your ferments, smelling them first, and activated charcoal for the itching.',
     deciding='Whether the bacteria were your own idea, one you\'d rather keep as your view.',
     advice_note='Approve.', found_by=FOUND,
     edits=[replace_words(P('B154'), 'somebody low in histamine-processing bacteria',
                          'somebody who breaks down histamine poorly')],
     spans=[span_of(P('B154'), 'low in histamine-processing bacteria')])

card(id='W-SLEEP', type='more', advice='approve', title='DMSO and sleep: what the rats showed',
     what='"This is proven in rats." becomes "In rats, higher doses made sleep lighter." (the same link).',
     why=('The linked study gave 20 rats one injection of DMSO at the start of their sleep period and recorded the next '
          '3 hours. The two higher doses made sleep lighter, with more light sleep and less deep sleep (PubMed: '
          '[Cavas et al. 2005](https://doi.org/10.1016/j.toxlet.2005.02.003)). It found lighter sleep, not shorter '
          'sleep, and it didn\'t test late doses or days in a row, so "proven" says more than it found.'),
     stays='Your lines on how DMSO shortens your sleep and builds up, and that some people sleep better with it.',
     deciding='Nothing much: your experience stays as yours, and the rat line now says what the rats showed.',
     advice_note='Approve.', found_by=FOUND,
     edits=[replace_words(P('B203', 2), 'This is proven in rats.', 'In rats, higher doses made sleep lighter.')],
     spans=[span_of(P('B203', 2), 'This is proven in rats.')])

card(id='W-TAR', type='nothing', advice='approve', title='Nebulizing DMSO with tar in the lungs',
     what='The bullet goes.',
     why=('I found no study of inhaled DMSO carrying tar or smoke residue into the blood, or of weakness from it. DMSO '
          'does dissolve the particles in cigarette smoke (labs use it to extract them, as in PubMed: [Huang et al. '
          '2013](https://doi.org/10.1159/000350866)), so the idea isn\'t strange. But the studies of nebulized DMSO '
          'after smoke inhalation, in sheep, found it protected the lungs: all 7 sheep given DMSO with heparin survived, '
          'and all 7 untreated died within 72 hours (PubMed: [Brown et al. 1988](https://doi.org/10.1097/'
          '00004630-198801000-00007); also [Kimura et al. 1988](https://pubmed.ncbi.nlm.nih.gov/2458858/), no DOI).'),
     stays='The other interactions.',
     deciding=('If it\'s your experience, or someone\'s you know, Reject and it stays. A comment saying so lets me mark it '
               'as yours.'),
     advice_note='Approve, unless it\'s your experience.', found_by=FOUND,
     edits=[cut_block(P('B205', 1))],
     spans=[whole(P('B205', 1))])

NSAID_OLD = 'Don\'t take it with drugs that should not absorb rapidly, including corticosteroids and NSAIDs.'
NSAID_NEW = 'Don\'t take it with drugs that should not absorb rapidly: DMSO can strengthen other medicines taken with it.'
card(id='W-NSAID', type='more', advice='approve', title='DMSO with corticosteroids and NSAIDs',
     what='"including corticosteroids and NSAIDs" becomes ": DMSO can strengthen other medicines taken with it".',
     why=('Both drug classes it names are given with DMSO on purpose. An FDA-approved diclofenac (NSAID) solution for knee '
          'arthritis contains DMSO ([its FDA label](https://nctr-crs.fda.gov/fdalabel/services/spl/set-ids/'
          '609c5344-9c97-4fa8-ad53-d0f622ce64ec/spl-doc); PubMed: [Marren 2011](https://doi.org/10.3810/'
          'psm.2011.09.1923)), and DMSO with triamcinolone, a corticosteroid, is a bladder treatment tested in a '
          'randomized trial (PubMed: [Moss et al. 2023](https://doi.org/10.1002/nau.25142)). The rule itself holds: '
          'DMSO\'s US label says "Some data indicate that dimethyl sulfoxide potentiates other concomitantly administered '
          'medications" ([RIMSO-50 label](https://www.drugs.com/pro/rimso-50.html)).'),
     stays='The rule, and your harmala timing.',
     deciding=('If you want one named drug: the label of sulindac, an NSAID, says "Concurrent use of dimethyl sulfoxide and '
               'sulindac is not recommended". The pair lowers sulindac\'s active form, and nerve damage has been reported '
               'with it ([UK label](https://www.medicines.org.uk/emc/product/8783/smpc/print), [US label](https://'
               'medlibrary.org/lib/rx/meds/sulindac/page/5/)). Revise to add it.'),
     advice_note='Approve.', found_by=FOUND,
     edits=[replace_words(P('B205', 2), NSAID_OLD, NSAID_NEW)],
     spans=[span_of(P('B205', 2), 'including corticosteroids and NSAIDs')])

card(id='W-CHOLINE', type='nothing', advice='approve', title='"DMSO depletes choline"',
     what=('"Supplement extra choline because DMSO depletes it." goes. The bullet keeps your cholinergic line: "Don\'t '
           'combine it with cholinergic drugs because DMSO is also cholinergic, although I haven\'t found anecdotes of '
           'this causing a real problem."'),
     why=('I found no study showing that DMSO lowers choline, in people or in animals. The nearest is a dish of rat nerve '
          'endings, where DMSO at 2 to 10% slowed their uptake of choline (PubMed: [North & Mrak 1989](https://'
          'pubmed.ncbi.nlm.nih.gov/2626218/), no DOI).'),
     stays='Your cholinergic line.',
     deciding='If it\'s your experience, Reject and it stays.',
     advice_note='Approve, unless it\'s your experience.', found_by=FOUND,
     edits=[replace_words(P('B205', 3), ' Supplement extra choline because DMSO depletes it.', '')],
     spans=[span_of(P('B205', 3), 'Supplement extra choline because DMSO depletes it.')])

GLORY_ADD = (' Daily use is another matter: in a 2026 study, a leaf tea given every day to mice with tumors, at a dose '
             'scaled from the traditional tea, caused skin sores and killed 7 of 10 within 15 days, though one large dose '
             'did healthy mice no immediate harm.')
card(id='W-GLORY', type='new', advice='approve', title='A 2026 study on beach morning glory\'s safety',
     what=('A sentence after "A whole leaf can easily end the trip and, in my experience, may prevent tripping for days '
           'afterward.":%s It would link the study.' % GLORY_ADD),
     why=('PubMed: [Llerenas-Aguirre et al. 2026](https://doi.org/10.3390/nu18142248). Mice carrying human breast tumors '
          '(bred without a working immune system, so the tumors take) drank a tea of Ipomoea pes-caprae leaves every '
          'day, at a dose scaled from the traditional Mexican tea of 12 to 14 dried leaves in a liter a day. By day 10, '
          '4 of the 10 had blistering skin sores. By day 15, 7 of 10 had died, and the tea was stopped. None of the '
          'untreated mice had sores or died. A single large dose given to 7 healthy mice did no immediate harm. The '
          'authors warn that sick mice may be more vulnerable than people. It\'s the only study I found on the plant\'s '
          'safety, and the guide has nothing on it yet.'),
     stays='Your whole-leaf line and everything else on beach morning glory.',
     deciding=('Whether you want it at all: it\'s daily dosing in sick mice, and one leaf is about a thirteenth of that '
               'tea\'s daily leaves. If you do, you may want it in your words (Revise).'),
     advice_note='Approve, or Revise it into your words.', found_by=FOUND,
     edits=[replace_words(P('B175'), 'may prevent tripping for days afterward.',
                          'may prevent tripping for days afterward.' + GLORY_ADD)],
     spans=[span_of(P('B175'), 'may prevent tripping for days afterward.')])

CHEST_OLD = 'In the second branch, I would use DMSO while arranging medical evaluation.'
CHEST_NEW = CHEST_OLD + ' If you\'re not sure which branch it is, treat it as the second.'
card(id='W-CHEST', type='call', advice='approve', title='Mild, familiar chest discomfort',
     what='A line after "In the second branch, I would use DMSO while arranging medical evaluation.": "If you\'re not '
          'sure which branch it is, treat it as the second."',
     why=('The American Heart Association says "Call 911 if you have any symptoms of heart attack", notes that some heart '
          'attacks "start slowly with mild pain or discomfort", and adds "Even if you\'re not sure it\'s a heart attack, '
          'get checked out" ([AHA, warning signs](https://www.heart.org/health-topics/heart-attack/warning-signs-of-a-'
          'heart-attack)). Your second branch and the call-medics list match its signs. The first branch, mild and '
          'familiar discomfort, has no call, which is where the guide parts from the AHA. The new line settles only the '
          'cases a reader can\'t place.'),
     stays='Both branches, DMSO in each, and the pain-signal line.',
     deciding=('Whether the first branch should stay as it is (Reject). That\'s your judgment, and the call-medics list '
               'already covers the dangerous signs.'),
     advice_note='Approve.', found_by=FOUND,
     edits=[replace_words(P('B124'), CHEST_OLD, CHEST_NEW)],
     spans=[span_of(P('B124'), 'Mild, familiar, non-progressive discomfort in a fully alert person')])
