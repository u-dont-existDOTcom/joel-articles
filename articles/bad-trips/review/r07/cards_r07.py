# The cards of round 7, read by build_r07.py (which defines P, T, whole, span_of, replace_words and card). P('N-CBD-2')
# is the page block of GUIDE-SO-FAR-blocks.json's N-CBD-2 (the guide after round 6). Each card's new words are the
# paragraph as it would read, in articles/bad-trips/humanize/h06-r07-20261105/R7-N.txt, with its making-sense receipt
# beside it (gate E365) and its newcomer reads in newcomer-R7-N/. The sources were opened on 2026-11-05 between 15:30 and
# 16:00 UTC (from his laptop: every link below answered 200 there, PubMed's through its E-utilities).

BUILT = '2026-11-05'
H = 'https://www.pangram.com/history/'
HUM = REPO / 'articles' / 'bad-trips' / 'humanize' / 'h06-r07-20261105'
RC = 'articles/bad-trips/humanize/h06-r07-20261105/%s.receipt.json'
FORUMS_TESTED_TEXT_SET = ('This version, my third, [Human Written, 0%%](%s59bba2ed-ed63-4db5-9884-5bcd465d4ec2), one window, '
                          'High.') % H
FORUMS_DECIDING = ('Three things of yours from round 6\'s page go: the CBD injection, the kind of seizure, and the last line. '
                   'The paragraph now ends on the rats and doesn\'t say what to do with THC at an aura; a fresh reader asked '
                   'whether it means not to use it. If you\'d say what you\'d do, Revise with that line, in your words.')


def R7(k):
    return (HUM / ('%s.txt' % k)).read_text(encoding='utf-8').rstrip('\n')


def to_text(i, new):
    """Block i as the receipt's text says it would read."""
    return {'block': i, 'before': T(i), 'after': new}


INTRO = [
    'Version 2 of round 7. Your round-6 answers reached two of my sessions (this chat, and the neuro de-armoring chat), '
    'and each made a round-7 page; this one puts them together, so it\'s the one to answer. The guide holds your round-6 '
    'words as you wrote them, and every change either session proposed is a card here, one per paragraph, with the '
    'other session\'s checks named on its card.',
    'Round 7 (2026-11-05), after your three round-6 versions and your placement went in. Your new paragraphs were checked in '
    'Pangram on your account first: the warning stage with your humic line, your cannabis paragraph and your topical CBD '
    'paragraph each read Human, High. Your forums paragraph read AI in the two sentences of mine you kept, so the last card '
    'fixes those.',
    'Where you asked "right?": yes, the warning-stage paragraph goes after the rescue medicine and before the paragraph that '
    'starts on CBD, so it sits above all the cannabis paragraphs. That move leaves the next paragraph\'s "also" and '
    '"adjuncts" pointing at the warning stage, which is the third card. And yes, the CBD evidence to go by for MDMA and '
    'psychedelic seizures is Dravet and Lennox-Gastaut\'s, whose trials counted generalized seizures (the second card); the '
    'third approved use, tuberous sclerosis, is mostly focal.',
    'Every card\'s new words were read for sense first, sentence by sentence, with a written receipt of what each sentence '
    'does for someone whose friend is having a seizure from MDMA or a psychedelic overdose, and two fresh readers each. That '
    'receipt is what would have caught the 7-OH-CBD point: a point that\'s correct after checking still goes when it does '
    'nothing for this reader.',
]

TYPES = {
    'fact': {'label': 'Checked against the source', 'about': 'a point in your paragraph changed to what its source says'},
    'order': {'label': 'After your move', 'about': 'what a paragraph needs once the one before it changed'},
    'mine': {'label': 'My words read AI', 'about': 'sentences of mine you kept, which read AI, fixed the next obvious way'},
}

ESCRIBA = 'https://escriba.camara.leg.br/escriba-servicosweb/html/58445'
CANALTECH = 'https://canaltech.com.br/saude/esta-e-a-maior-plantacao-legal-de-cannabis-medicinal-no-brasil-191927/'

card(id='ABRACE', type='fact', advice='approve', title='ABRACE: a patients\' association, and more than 30 tests',
     reading=('Your paragraph as it is, [Human Written, 0%%](%sae1cbe48-eeb7-4e04-8b62-bbb970071cb1), one window, High.') % H,
     tested=('With the two changes, [Human Written, 0%%](%sa5570612-ceb1-479d-815e-1cb646423ebc), one window, High.') % H,
     what=('Two changes in your cannabis paragraph: "by a company called ABRACE" becomes "by a patients\' association '
           'called ABRACE", and "in 30 tests" becomes "in more than 30 tests".'),
     why=('What was said in Congress ([the transcript](%s), the special committee on bill 399/2015, 19 November 2019): '
          'ABRACE\'s executive director, Cassiano Teixeira, told it "Nos mais de 30 testes que fizemos, as crianças voltaram '
          'em menos de 30 segundos" (in the more than 30 tests we did, the children came back in under 30 seconds), of a '
          'THC nasal spray. ABRACE (Associação Brasileira de Apoio Cannabis Esperança) is a non-profit association of '
          'patients and families in João Pessoa that the courts have let grow cannabis and supply its members since 2017 '
          '([Canaltech](%s)), and its products aren\'t registered as medicines. That matters to the reader: the tests are '
          'the makers\' own reports, not a trial. "Within 30 seconds" is what he said, and the video\'s title says it\'s '
          'their THC spray.') % (ESCRIBA, CANALTECH),
     stays='Everything else in the paragraph, in your words: "marketed", "within 30 seconds", the video.',
     deciding=('Two fresh readers asked what kind of tests these were. "tests they did" says they were the association\'s '
               'own; if you\'d rather say outright that they weren\'t a trial, Revise with your words.'),
     advice_note='Approve.', found_by='checking your new points against the testimony (gate E348)',
     receipt=RC % 'R7-1',
     edits=[to_text(P('N-CANNA-1'), R7('R7-1'))],
     spans=[span_of(P('N-CANNA-1'), 'a company'), span_of(P('N-CANNA-1'), 'in 30 tests')])

OBRIEN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9270696/'
card(id='AUTHORS', type='fact', advice='approve',
     title='The gel trial: what its authors said, and what it means for drug seizures',
     reading=('Your paragraph as it is, [Human Written, 0%%](%sb24a1f68-fe39-4ef8-bfef-a03bbce3dc1c), one window, High.') % H,
     tested=('With the changes, [Human Written, 0%%](%s954a53dc-72c4-457a-b5e2-3e87a8e4ade6), one window, High.') % H,
     what=('Your sentence "The study authors suggested the dosing may have been too low, or it works better for generalized '
           'rather than focal seizures." becomes two: "The study authors suggested the dosing may have been too low, or that '
           'adults with focal epilepsy just don\'t respond as well as people with the syndromes oral CBD is approved for. The '
           'seizures in Dravet and Lennox-Gastaut syndrome are mostly generalized." And your last sentence says what it means '
           'for the trial: "Generalized are the type people usually have with MDMA & psychedelic overdoses, so topical CBD '
           'might do better for those than it did in that trial."'),
     why=('The authors didn\'t say generalized. Their words ([O\'Brien et al. 2022](%s)): the response "in adults with focal '
          'epilepsy is not as robust as seen in patients with Dravet syndrome, Lennox-Gastaut syndrome, or tuberous sclerosis '
          'complex", and tuberous sclerosis is a condition "with primarily focal seizures" ([Thiele et al. 2021](https://'
          'pubmed.ncbi.nlm.nih.gov/33346789/)). So their point was the kind of patient. Your extrapolation still holds through '
          'Dravet and Lennox-Gastaut: the Dravet trial counted convulsive seizures ([Devinsky et al. 2017](https://pubmed.ncbi.'
          'nlm.nih.gov/28538134/)), the Lennox-Gastaut trial drop seizures ([Devinsky et al. 2018](https://pubmed.ncbi.nlm.nih.'
          'gov/29768152/)), both generalized kinds, and seizures caused by drugs are generalized ([a toxicology teaching note '
          'from the University of Calgary](https://cumming.ucalgary.ca/sites/default/files/teams/127/CPT%%20Pearl%%20Drug%%20'
          'Induced%%20Seizure.pdf), which lists MDMA). I left out the authors\' third reason, that the effect might take longer '
          'than 12 weeks to show, since it changes nothing for someone having a seizure now. The last clause is there because '
          'two fresh readers couldn\'t see what the generalized point meant for the trial; "might", because no study has tried '
          'CBD on a seizure a drug caused.') % OBRIEN,
     stays='Your first two sentences, and your last sentence\'s words.',
     deciding=('The closing clause is your extrapolation ("we should extrapolate from cbd evidence for that"), said as one. If '
               'you\'d rather leave the reader to draw it, Revise without it. The other session\'s shorter fix, "or that CBD just '
               'doesn\'t work as well for focal seizures as it does in Dravet syndrome, where many of the seizures are '
               'generalized.", also read Human, High ([its check](%saa293ceb-d603-4fe1-9007-2ddc9c6a72bb)); it names Dravet only and '
               'leaves the conclusion to the reader. Revise with it if you\'d rather.') % H,
     advice_note='Approve.', found_by='checking your new points against the trial\'s paper (gate E348), and your question about focal seizures',
     receipt=RC % 'R7-2',
     edits=[to_text(P('N-CBD-2'), R7('R7-2'))],
     spans=[span_of(P('N-CBD-2'), 'or it works better for generalized rather than focal seizures'),
            span_of(P('N-CBD-2'), 'Generalized are the type people usually have with MDMA & psychedelic overdoses.')])

card(id='AFTER-MOVE', type='order', advice='approve',
     title='The paragraph after your move: when, and no focal sentence',
     reading=('Checked with your other CBD paragraphs in round 6, [Human Written, 0%%](%s01b892a4-ee16-4f06-bb77-52090f1aa4e7), '
              'with its last sentence, "For focal seizures outside those syndromes, the evidence is mixed, but still '
              'long-term.", in a Low window.') % H,
     tested=('With the changes, alone, [Human Written, 0%%](%sffbdf673-64f0-4253-8712-88b419ddb4f4), one window, High.') % H,
     what=('It starts "During the seizure, alongside any rescue medicine, I would use topical magnesium chloride ..." where '
           'it said "I would also use ... as adjuncts", and its last sentence, on focal seizures, goes.'),
     why=('Your move put the warning stage between this paragraph and the rescue medicine, so its "also" and "as adjuncts" '
          'now add to the warning-stage list: two fresh readers asked "adjuncts to what?", one of them after reading the '
          'section from its start. "During the seizure" turns back to the seizure, and "alongside any rescue medicine" says '
          'what these go with, which "adjunct" said before the move. The focal sentence answers your question, "why are we '
          'talking about focal seizures": here we needn\'t, since the seizures drug overdoses cause are generalized, and it '
          'was the Low window in round 6\'s check.'),
     stays='Everything else in the paragraph, your words.',
     deciding=('Whether "alongside any rescue medicine" says it your way. "As adjunct remedies", your own fix from round 5, '
               'was the first thing I tried, and the fresh readers still asked what they were adjuncts to. The other session\'s '
               'card cut only the focal sentence, which also read Human, High ([its check](%s5d3d05f7-30aa-4aef-b6cf-08deb2f4bd96)); '
               'if you\'d rather keep "I would also use ... as adjuncts", Revise with just the cut.') % H,
     advice_note='Approve.', found_by='your move of the warning-stage paragraph, and your question about focal seizures',
     receipt=RC % 'R7-3',
     edits=[to_text(P('B111'), R7('R7-3'))],
     spans=[span_of(P('B111'), 'I would also use'), span_of(P('B111'), 'as adjuncts'),
            span_of(P('B111'), 'For focal seizures outside those syndromes, the evidence is mixed, but still long-term.')])

FORUMS_TESTED_TEXT = FORUMS_TESTED_TEXT_SET  # set at the top of the file once the check is read
card(id='FORUMS', type='mine', advice='approve', title='Your forums paragraph: my sentences that read AI',
     reading=('As it is, [AI Detected, 62%%](%s64d111ca-8c3a-4d94-adc5-beb4a8b32bf0): your first sentence Human (Low); "But '
              'other people say THC vapes and concentrates brought their seizures on, and in rats ... cut them about in half." '
              'AI (Medium); "So the THC may be what makes it go either way." AI (Low). Both are mine, from round 6.') % H,
     tested=FORUMS_TESTED_TEXT,
     what=('After your first sentence, my two become: "%s" Three things of mine go: the rats\' kind of seizure (the brief '
           'staring seizures called absence seizures), the injected CBD that cut their seizures about in half, and the last '
           'line, "So the THC may be what makes it go either way."' % R7('R7-4').split('she smoked. ', 1)[1]),
     why=('My first fix (split the long sentence, say why the rats are there, "cannabis" for "it") read [AI Detected, '
          '51%%](%sb8fbfcbc-c2d9-48b7-a1f8-0510320bb0a1): the split sentence went Human (Low), and the rats with the last line '
          'went AI (High). Three fresh readers then agreed on every one of those: the gloss on the rats\' seizures, the rats\' '
          'two results set in mirror image ("more ... while ... about in half") and the summing-up last line, which also '
          'didn\'t follow (a fresh reader: the rats show more seizures, not "either way"). So each goes, and only what this '
          'reader needs stays: that THC products brought some people\'s seizures on, and that the same happened to rats bred '
          'to have seizures ([Roebuck et al. 2022](https://pubmed.ncbi.nlm.nih.gov/33370468/): smoke from a high-THC cannabis '
          'raised their seizure discharges; injected THC did too, to over twice their usual number). The injected CBD is '
          'out because a helper can\'t inject CBD and the CBD evidence is in the paragraphs around this one; the kind of '
          'seizure, because it changes nothing for the reader. A second panel read on this version asked for "some" not to '
          'be said twice and for no trailing "too", so it says who ("a few people on the same forums") and adds the rats '
          'with "And". The other session\'s four tries at this paragraph all read AI ([62%%](%s2419edef-dd6d-4c05-9ed3-32bf737bef33), '
          'your version; [43%%](%sfd1df50a-5f61-44ee-ad14-ab61bda0542c); [98%%](%sd3ff8463-b3c1-40f3-8852-d81cedc403ed); '
          '[41%%](%sbbaa0976-fd6a-4cdb-bcb0-207e5e9d1265)), each keeping the rats\' two results and a closing line, which is what '
          'all three panel readers here named.') % (H, H, H, H, H),
     stays='Your first sentence, word for word, and the point that THC is what brought seizures on.',
     deciding=FORUMS_DECIDING,
     advice_note='Approve.', found_by='Pangram on your forums paragraph, then the making-sense read, a tell panel and fresh readers',
     receipt=RC % 'R7-4',
     edits=[to_text(P('N-CANNA-2'), R7('R7-4'))],
     spans=[span_of(P('N-CANNA-2'), 'But other people say THC vapes and concentrates brought their seizures on, and in rats '
                    'that get the brief staring seizures called absence seizures, high-THC smoke made them worse while injected '
                    'CBD cut them about in half.'),
            span_of(P('N-CANNA-2'), 'So the THC may be what makes it go either way.')])
