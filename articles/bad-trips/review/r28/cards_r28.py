# The cards of round 28, read by build_r28.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words and card). Round 28 answers his round-27 comment on the aftermath card (2026-11-09 01:24 UTC): "so do your
# best first, give me your suggestions, pros and cons for each, and the most impactful choices i can make in order to
# address all this" (lesson bad-trips-2026-11-09a).

BUILT = '2026-11-09'
H = 'https://www.pangram.com/history/'
HB = BLOB + 'articles/bad-trips/humanize/h37-20261108/beliefs/'
RUE1 = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3841998/'


def both(i, pairs):
    """Block i with each (old, new) in PAIRS replaced, as one edit."""
    t = T(i)
    after = t
    for old, new in pairs:
        assert after.count(old) == 1, (i, old)
        after = after.replace(old, new)
    return {'block': i, 'before': t, 'after': after}


INTRO = [
    'Round 28 (2026-11-09). Your round 27 is in: both sentences of your post are back, your first five minutes is one piece '
    'again with the panic loop and your story of the voice, and your aftermath list is in as you wrote it. The helper\'s '
    'Don\'t heading and its two paragraphs went, since your first five minutes says them now. I kept the practice paragraph '
    '("If a practice like meditation or fasting brought this on, ...") right after your reminder, since it\'s that '
    'reminder\'s practice case. Typos fixed: "chanting, on them", "aftewards", "for benefit all involved" (to "to benefit '
    'all involved"), "onr", and the shame guide\'s link, which needed its http:// to open.',
    'You asked for my best first, then options with pros and cons, and the choices that matter most. The first card is '
    'what I could fix: three terms in your aftermath list explained where they\'re used. The other five are the choices, '
    'most impactful first: how your method gets into the parts people use in trouble, the Fear/Panic Loop now that your '
    'first five minutes has it, how much of the aftermath list the guide needs, what For the Person Helping is now for, '
    'and one safety point, Syrian rue, to settle before the guide goes live. Each says what I\'d pick and why.',
]

card(id='AFT-TERMS', type='sense', advice='approve', title='What Kind of Aftermath Is This?: three terms said where they\'re used',
     what=('"CBT-style reality testing" gets ", checking the frightening thought against what\'s actually happening,"; '
           '"Derealization and depersonalization" gets "(when the world, or you yourself, feel unreal)"; and "Somatic '
           'Experiencing therapy" becomes "Somatic Experiencing, a therapy that works through body sensations".'),
     why=('A reader days after a hard trip can\'t match "derealization" or "depersonalization" to what they feel, or do '
          '"reality testing", without being told what it is. CBT itself is spelled out earlier, in (Re)defining "Bad Trip".'),
     stays='Everything else in your list, word for word.',
     deciding='Approve puts the three in; Revise if you\'d say any of them differently.',
     advice_note='Approve: each is the smallest gloss that lets the reader recognize the kind or do the step.',
     ask_because='downside: they\'re words added to your version, which read High as you wrote it',
     found_by='a fresh reader\'s sense read of the list, and a needed read of the two lines with the glosses in',
     edits=[both(P('B426', 0), [('CBT-style reality testing is one way', 'CBT-style reality testing, checking the frightening '
                                 'thought against what\'s actually happening, is one way')]),
            both(P('B426', 2), [('Derealization and depersonalization:', 'Derealization and depersonalization (when the world, '
                                 'or you yourself, feel unreal):'),
                                ('and Somatic Experiencing therapy.', 'and Somatic Experiencing, a therapy that works through '
                                 'body sensations.')])],
     spans=[span_of(P('B426', 0), 'CBT-style reality testing'),
            span_of(P('B426', 2), 'Derealization and depersonalization'),
            span_of(P('B426', 2), 'Somatic Experiencing therapy')],
     receipt=['articles/bad-trips/review/r28/AFT-ANX.receipt.json', 'articles/bad-trips/review/r28/AFT-DEREAL.receipt.json'])

card(id='METHOD-WHERE', type='structure', advice='ask', title='1. Your method in the parts people use in trouble: how?',
     question=('A fresh reader found 15 places where the guide gives generic advice where your method would change what the '
               'reader or helper does ([where](%sGENERIC.md)). Your first five minutes, your don\'ts and your aftermath list '
               'now carry it, which leaves 10: the sitter\'s script, Alone at 3 a.m., the helper\'s Do list, the Grounding '
               'Menu\'s hand on the heart and breath line, the thinking traps, Give the Session\'s preparation, Abuse '
               'Memories\' step after sleep, Shadow Thoughts\' in-trip move, and the questions after the aftermath list.\n\n'
               'A (my pick): I move or quote sentences the guide already has, where it gives your method, into those places, one approve card '
               'each, starting with the four that matter most: Alone at 3 a.m. (someone with no sitter: "Can I send love to '
               'the one who\'s suffering?" and the hand on the heart), the breath line ("I can love the part of me that '
               'feels it."), Give the Session\'s preparation ("So train before you need it, sending love to a frightening '
               'image ...") and the thinking traps ("young parts of you that are still waiting for love ..."). Pro: your '
               'method where it\'s used, in sentences the guide already has, quick for you to approve. Con: a moved sentence can need a joining '
               'word, and the places read AI now, so they may still need your hand for Pangram.\n\n'
               'B: teaching cards, one or two places at a time, for you to write each with your method in it. Pro: your '
               'voice and your view, and they read Human. Con: your time, ten places.\n\n'
               'C: leave them. Pro: no work. Con: the guide stays generic where it\'s used.') % HB,
     why=('This is the change that matters most to what the guide is: your method, not generic trip-sitting advice, at the '
          'moment someone needs it.'),
     stays='Whichever you pick, nothing is written for you: only sentences the guide already has, moved, or your own versions.',
     advice_note='A, then B for any place where a moved sentence doesn\'t fit.',
     spans=[whole(P('B272'))])

card(id='LOOP-ONCE', type='structure', advice='ask',
     whose=('his own: the panic-loop paragraph he wrote into the first five minutes in round 27 (2026-11-09 01:24 UTC), beside the guide\'s Fear/Panic Loop section'), title='2. The Fear/Panic Loop, now that your first five minutes has it',
     question=('A (my pick): cut the section. Your first five minutes now says the loop and what helps ("sometimes feelings '
               'just need to be felt, so they can move and release"), and the loop breaker\'s other steps are said where '
               'the reader uses them: the order (room, body, human, time) in Stillness or Movement? and the Grounding Menu, '
               '"This is a wave" in the sitter\'s script and the breath line. Pro: said once, in your words, with your view '
               'of what helps. Con: it drops four quick steps someone alone might use, and two protected warnings ("Stop '
               'debating ..." and "Repeat ...") and one of the four places your room-first order appears go with it.\n\n'
               'B: keep only the four steps, moved right under your panic-loop paragraph, with the "ladder" said as the '
               'order it is and each line said as the person\'s or the helper\'s. Pro: the quick steps stay, next to your '
               'paragraph. Con: their view (name it, wait it out) sits beside yours (feel it so it can release), and a '
               'fresh reader found "ladder", "at the peak" and "Stop debating" unclear.\n\n'
               'C: leave the section as it is. Pro: nothing lost. Con: the loop is said twice, the second time without '
               'your view.'),
     why='Your first five minutes now has the panic loop in your words, so this section says it again, the generic way.',
     stays='Your panic-loop paragraph in the first five minutes, whichever you pick.',
     advice_note='A: your paragraph does the section\'s job with your view, and the steps live on where the reader uses them.',
     spans=[whole(P('B372')), whole(P('B374'))] + [whole(i) for i in PALL('B375')])

card(id='AFT-HOW-MUCH', type='structure', advice='ask', title='3. What Kind of Aftermath Is This?: how much of it?',
     question=('A (my pick): keep all eight kinds as your version has them, with the three terms on the first card and the '
               'Syrian rue question settled. Pro: each kind now says what to do and why, with your remedies, and it read '
               'High as you wrote it. Con: it\'s long (about 520 words), and two kinds, visual distortions and paranoia, '
               'are medical enough that the reader also needs the call-for-help lists at the top.\n\n'
               'B: keep the five kinds a reader can recognize in themselves (anxiety and fear, sleep, shame, existential '
               'shock, bodily restlessness) and move visual distortions, derealization and paranoia to "Bring in '
               'mental-health support when:", each with your remedy in a line. Pro: shorter, and the three that may need a '
               'professional sit with the call-for-help lines. Con: it splits your version, and those remedies move away '
               'from the days-after list where the reader looks.\n\n'
               'C: cut the list to its first paragraph and point to the sections that cover each kind. Pro: shortest. Con: '
               'loses your remedies and the days-after view.'),
     why='You asked whether this even needs to be here, or how much of it.',
     stays='Your first paragraph, whichever you pick.',
     advice_note='A: nothing else in the guide says what to do days later for each of these, and now it says it your way.',
     spans=[whole(P('B425'))])

card(id='HELPER-NOW', type='structure', advice='ask',
     whose=('his own: the anchor line and don\'ts he wrote in rounds 24 and 27, now in the first five minutes'), title='4. For the Person Helping, now that your first five minutes has the anchor',
     question=('Your anchor line ("not the witch doctor guru who knows magic spells") and don\'ts are in the first five '
               'minutes now. The section keeps the Zendo Project\'s four principles, "Crying, grieving, remembering, ...", the '
               'helper\'s self-talk ("This feeling is allowed to move through ..."), the Do list and When the Content Turns '
               'Toward Harm.\n\n'
               'A (my pick): keep it as it is. Pro: it\'s what a helper needs once the first minutes pass, and "Calm Anchor, '
               'Not Guru" still names its Zendo principles. Con: the heading echoes your anchor line from much earlier.\n\n'
               'B: move its Do list up into the first five minutes, after your piece. Pro: the first minutes get the '
               'helper\'s concrete questions ("Would less light help?" "Music or quiet?"). Con: it lengthens your piece, '
               'which reads Human now, and may change how it reads.\n\n'
               'C: retitle the section in your words. Pro: the heading says what\'s in it now. Con: one more thing for you '
               'to write.'),
     why='Your version moved its anchor line and don\'ts into the first five minutes, so the section is different now.',
     stays='Everything in the section, whichever you pick, unless B moves the Do list.',
     advice_note='A: nothing in it repeats your piece now, and its heading still fits.',
     spans=[whole(P('B279'))])

card(id='RUE-SAFETY', type='safety', advice='ask',
     whose=('his own: the paranoia and bodily-restlessness lines of the aftermath list he wrote in round 27 (2026-11-09 01:24 UTC)'), title='5. Syrian rue in your paranoia line: a safety point',
     question=('Your paranoia line names "the relatively safe and natural antipsychotics mentioned in this guide, like DMSO, '
               'syrian rue OIL, and niacin". The guide doesn\'t mention Syrian rue anywhere else, and its serotonin syndrome '
               'section lists "harmala/ayahuasca-type MAOI exposure" among the things to stop. Syrian rue (Peganum harmala) '
               'is the classic harmala source: its seed extracts strongly inhibit MAO-A, mainly through harmaline and '
               'harmine, and that inhibition is the main cause of its toxic effects ([a review](%s)). Someone with lingering '
               'paranoia may still be on an antidepressant or an MDMA-type drug, the combination the guide warns about.\n\n'
               'A (my pick): say what "syrian rue OIL" is (if it\'s an oil used on the skin or by smell, as your capitals '
               'suggest, say so), and add the harmala warning where it\'s named: not with antidepressants, MDMA, other '
               'MAOIs or the rest of the serotonin list. Pro: keeps your remedy with what a reader needs to use it safely. '
               'Con: a few more words in your line.\n\n'
               'B: take Syrian rue out of the line until it has its own place in the guide, with its warning. Pro: the '
               'safest wording now. Con: your remedy goes for now.\n\n'
               'C: keep the line as it is. Con: it names a remedy the guide never explains, next to a warning against it.\n\n'
               'Also, in the bodily-restlessness line, "my trusty relaxing herbs and natural antipsychotics listed above": '
               'no herbs are listed above it. Name them, or point to "Mental Stabilizers That Don\'t Abort the Trip".') % RUE1,
     why='It\'s the one place in your new lines where a reader could get hurt following the guide as written.',
     stays='Everything else in the line, whichever you pick.',
     advice_note='A, or B if the oil isn\'t different from the seeds.',
     spans=[span_of(P('B426', 6), 'syrian rue OIL'), span_of(P('B426', 7), 'listed above')])
