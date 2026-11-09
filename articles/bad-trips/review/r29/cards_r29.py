# The cards of round 29, read by build_r29.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words and card). Both are typos in paragraphs he wrote himself, found by the word-for-sense read of the whole
# guide (gate E331; articles/bad-trips/humanize/h38-20261109/sense-read/RESULTS.md). The read's slips in the guide's
# drafted text were fixed without asking (fix_slips.py beside RESULTS.md; lesson bad-trips-2026-11-09a).

BUILT = '2026-11-09'
READ = BLOB + 'articles/bad-trips/humanize/h38-20261109/sense-read/RESULTS.md'
FOUND = ('the word-for-sense read of the whole guide: a fresh reader for each third, tested with errors I planted where '
         'they couldn\'t see the list (all nine found)')

INTRO = [
    'Round 29 (2026-11-09). The word-for-sense read of the whole guide is done: three fresh readers, a third each, asked of '
    'every word whether it\'s the word meant, and the read was tested with errors I planted where they couldn\'t see the '
    'list. They found all nine, so what they didn\'t flag can be trusted too ([what each finding was, and what came of '
    'it](%s)).' % READ,
    'Three slips were in the guide\'s drafted text, so I fixed them: the medics heading is now "Call medics for:" (the line '
    'under its list already says the remedies can begin while help is arranged), "Test them" under Stillness or '
    'Movement? now says "Test stillness and movement", and the list after "Don\'t take more" now goes "cannabis or '
    'ketamine, do intense breathwork, fast, ...", since breathwork and fasting aren\'t taken. Two are in paragraphs you '
    'wrote yourself, and they\'re these two cards. Three stay as they are: "often mistaken as shadow work" is your round-1 '
    'wording, "the first thread" is the poster\'s thread of the two you link, and a "2." that looked stray was only in my '
    'copy for the readers.',
]

card(id='TYPO-AYA', type='typo', advice='approve', title='Metta NMT Sniffer: "ayahauasca" to "ayahuasca"',
     whose='his own: the sniffer-stick paragraph, as he wrote it in his post of 3 November',
     owner_text='his own: his sniffer-stick paragraph, with the word spelled the way he spells it two sentences later',
     what='"But when I\'m on ayahauasca or loveyhuasca" becomes "But when I\'m on ayahuasca or loveyhuasca".',
     why=('A typo that has been there since your post: two sentences later the paragraph has "It turns regular ayahuasca '
          'into loveyhuasca even."'),
     stays='Everything else in the paragraph, word for word.',
     deciding='Approve fixes the spelling; Reject keeps it as it is.',
     advice_note='Approve.',
     ask_because='his own: your sniffer-stick paragraph, from your post of 3 November',
     found_by=FOUND,
     edits=[replace_words(P('B182'), 'on ayahauasca or', 'on ayahuasca or')],
     spans=[span_of(P('B182'), 'ayahauasca')])

card(id='TYPO-HYPER', type='typo', advice='approve',
     title='Some Remedies Require More Caution: "hyper intelligent" to "hyperintelligent"',
     whose='his own: the humic acid paragraph, as he wrote it in his post of 3 November',
     owner_text='his own: his humic acid paragraph, with the word spelled the way its first sentence spells it',
     what=('"Smelling it does not produce that hyper intelligent state" becomes "Smelling it does not produce that '
           'hyperintelligent state", the way the paragraph\'s first sentence has it ("can produce a hyperintelligent state '
           'for me").'),
     why='One spelling for the one state, so the reader sees it\'s the same state both times.',
     stays='Everything else in the paragraph, word for word.',
     deciding='Approve makes the two the same; Reject keeps both as they are.',
     advice_note='Approve.',
     ask_because='his own: your humic acid paragraph, from your post of 3 November',
     found_by=FOUND,
     edits=[replace_words(P('B219'), 'that hyper intelligent state', 'that hyperintelligent state')],
     spans=[span_of(P('B219'), 'hyper intelligent')])
