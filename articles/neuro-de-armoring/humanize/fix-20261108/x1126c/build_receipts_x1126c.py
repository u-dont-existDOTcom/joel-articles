"""The receipts for x1126c's folds (texts_x1126c.FOLD): his answer "72a" of 2026-11-26 23:30 UTC folds each warning's
label into its first sentence, the only change of mine in each (and "it" named as 5-HTP in the 5-HTP warning's last
sentence, which a fresh reader of the fold took two ways).

Two kinds of paragraph:
  - dmso, elec, ethno, rule, cog: my humanized versions. Their receipts are the last ones for the text as it stood
    (x1125a/v10/DMSO10, x1125a/v7/ELEC4, x1126a/ETHNO2, x1126a/RULE6, x1126a/COG-C5), carried over with the first
    sentence's new start; every sentence after it is unchanged.
  - iso, lma, agm, prec, htp: his own versions, from his cards. Fresh readers (Sonnet, 2026-11-26, as Fable's limit was
    reached) read each fold (x1126c/v1/{needed,his-fixes,fit}/KEY/READ.md); what they marked in his sentences stays,
    with why: 72a asks for the fold alone, and a change to his own words goes to him first.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1126c/build_receipts_x1126c.py [KEY ...]
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
sys.path.insert(0, str(FIX / 'x1123a'))
sys.path.insert(0, str(FIX / 'x1123b'))
sys.path.insert(0, str(HERE))
import build_receipts_x1123b as BB  # noqa: E402  (its fill allows a link of "none: why")
import texts_x1126c as T  # noqa: E402

B = BB.B
S = B.S
OUT = HERE / 'receipts'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
MSG = 'his answer "72a" of 2026-11-26 23:30 UTC (fix-20261108/joel-20261126-2330-message.txt)'
TOP = 'A Complete Guide to Bio-De-Armoring, the warnings at the top'
YOU = ('an adult with trauma or an addiction who has read the short introduction and is reading the warnings before '
       'starting the protocol, ')
REUSED = (' Reused for this fold, which changes only the label (' + MSG + '): every sentence it marked was changed before '
          'or is kept below with why.')


def text(key):
    return T.plain(T.FOLD[key])


def from_old(name, key, old, first, kept=None, extra='', t=None, swap=None, drop=()):
    """A receipt for FOLD[key] from the last receipt of the text as it stood (OLD, a path under fix-20261108): the same
    payoffs, links, checks and reads, the first sentence starting at FIRST (the label folded in). KEPT replaces kept
    reasons that named the label; EXTRA is the neighbour paragraph a pair is checked with."""
    r0 = json.loads((FIX / old).read_text(encoding='utf-8'))
    t = (t or text(key)) + ('\n\n' + T.plain(extra) if extra else '')
    spec = {}
    def find(k):          # a spec key by its first words (keys are each sentence's first 30 characters)
        (hit,) = [s for s in spec if s.startswith(k[:20]) or k.startswith(s)]
        return hit
    for i, x in enumerate(r0['sentences']):
        start = x['s'][:30] if (i > 0 or any(x['s'].startswith(k[:20]) for k in (swap or {}))) else first
        spec[start] = (x['payoff'], x['follows'], None if i == 0 else x.get('link'))
    for old_start, (new_start, pay, fol, link) in (swap or {}).items():
        del spec[find(old_start)]
        spec[new_start] = (pay, fol, link)
    for k in drop:         # a sentence joined to the one before: its payoff is in that one's
        del spec[find(k)]
    reads = []
    for k in ('needed', 'his_fixes', 'fit'):
        d = json.loads(json.dumps(r0[k]))
        d['reader'] = d['reader'] + REUSED
        for s, w in (kept or {}).get(k, {}).items():
            d['kept'][s] = w
        reads.append(d)
    return B.build(name, t, r0['section'], r0['reader'], spec, r0['opens']['why_reading'],
                   [(c['point'], c['found'], c['still_needed'], c['fate']) for c in r0['checked']], *reads,
                   r0['same_point'] + '; ' + MSG + ' folds its label into its first sentence', r0['placement'])


COG_S1 = 'Cognitive Warning: As you de-armor, you will feel naked and exposed.'
COG_KEPT = ('the label is folded in, by ' + MSG + ', so the sentence opens on the reader\'s own case; the rest is the '
            'post\'s; the reassurance the read asks for is S2, right after it, and the join it asks for (S1 and S2 in '
            'one sentence) is the next step if this one reads below High')


def dmso():
    return from_old('DMSO-F1', 'dmso', 'x1125a/v10/DMSO10.receipt.json', 'This protocol has you smell DMSO')


def elec():
    return from_old('ELEC-F1', 'elec', 'x1125a/v7/ELEC4.receipt.json', "You'll also be eating")


def ethno(name='ETHNO-F1', v='f1'):
    if v == 'f1':
        return from_old(name, 'ethno', 'x1126a/receipts/ETHNO2.receipt.json', 'The plant medicines in this protocol')
    return from_old(name, 'ethno', 'x1126a/receipts/ETHNO2.receipt.json', 'The plant medicines in this protocol',
                    t=T.plain(T.TRY2['ethno-' + v]),
                    swap={'Both are illegal in many juris': (
                        'Both are illegal in many juris', 'they learn both are illegal in many places and carry risks, '
                        'and that iboga can be dangerous for the heart, so they don\'t mix iboga with most medications, '
                        'heart and psych ones above all', 'it says what the two just named carry, and the rule that '
                        'follows from the heart danger, joined to it by "so"', 'Both')},
                    drop=['So never combine iboga with mo'])


def rule(name='RULE-F1', v='f1'):
    if v == 'f1':
        return from_old(name, 'rule', 'x1126a/receipts/RULE6.receipt.json', 'My rule for now is to seek')
    if v == 'b':
        return from_old(name, 'rule', 'x1126a/receipts/RULE6.receipt.json', 'My rule for now is to seek',
                        t=T.plain(T.TRY2['rule-b']),
                        swap={'The other kind, "Exciting Love': (
                            'A new romance or high-stakes', 'they learn what "Exciting Love" is by what brings it, a new '
                            'romance or high-stakes drama, and what it does (it spikes Phasic Dopamine and puts the armor '
                            'right back up), so they wait on starting a new romance or stepping into drama, and keep the '
                            'partner they have, the two named so the wait can\'t be read as one of the two kinds of love '
                            '(read-1126c F1.2)', 'it gives the other kind of love, the one to avoid for now, and what '
                            'follows for them, joined by "so"', 'none: it names the other kind of love by what brings '
                            'it, the opposite of the Boring Love just named')},
                        drop=['So this may not be a good time'])
    return from_old(name, 'rule', 'x1126a/receipts/RULE6.receipt.json', 'My rule for now is to seek',
                    t=T.plain(T.TRY2['rule-' + v]),
                    swap={'The other kind, "Exciting Love': (
                        'A new romance or high-stakes', 'they learn what "Exciting Love" is by what brings it, a new '
                        'romance or high-stakes drama, and what it does: it spikes Phasic Dopamine and puts the armor '
                        'right back up', 'it gives the other kind of love, the one to avoid for now', 'none: it names '
                        'the other kind of love by what brings it, the opposite of the Boring Love just named')})


def cog3(name='PAIR-COG-FACES-F3', faces=None):
    """The pair with the Cognitive Warning's first two sentences joined and the faces sentence's point first (FACES3), or
    as it read High with his verb (FACES4)."""
    if faces is not None:
        return from_old(name, 'cog', 'x1126a/receipts/COG-C5.receipt.json', 'As you de-armor, you will feel naked and '
                        'exposed, and',
                        {'his_fixes': {COG_S1: COG_KEPT}, 'fit': {COG_S1: COG_KEPT}}, faces, t=T.plain(T.COG2),
                        swap={'Cognitive Warning: As you de-ar': (
                                  'As you de-armor, you will feel naked and exposed, and', 'they expect to feel exposed as '
                                  'the armor comes off, and to think everyone can see their anxiety, though people see much '
                                  'less of it than they think', 'it is the next warning; the thought that comes with the '
                                  'feeling joined to it, as its read asked', None),
                              'Your armored brain also reads ': (
                                  'Your armored brain also proje', 'they learn the second way their read goes wrong: their '
                                  'armored brain projects the threat it feels onto neutral faces, so they will feel judged '
                                  'by people who are mostly thinking about themselves', 'it adds to the paragraph before, '
                                  'which said they will feel seen through, with his post\'s verb ("projects ... onto '
                                  'neutral faces")', 'also')},
                        drop=['You will assume everyone can se'])
    return from_old(name, 'cog', 'x1126a/receipts/COG-C5.receipt.json', 'As you de-armor, you will feel naked and '
                    'exposed, and',
                    {'his_fixes': {COG_S1: COG_KEPT}, 'fit': {COG_S1: COG_KEPT}}, T.FACES3, t=T.plain(T.COG2),
                    swap={'Cognitive Warning: As you de-ar': (
                              'As you de-armor, you will feel naked and exposed, and', 'they expect to feel exposed as the '
                              'armor comes off, and to think everyone can see their anxiety, though people see much less '
                              'of it than they think', 'it is the next warning; the thought that comes with the feeling '
                              'joined to it, as its read asked', None),
                          'Your armored brain also reads ': (
                              'You will also think people', 'they learn the second way their read goes wrong, first: they '
                              'will feel judged by people who are mostly thinking about themselves; then why: their armored '
                              'brain projects the threat it feels onto neutral faces', 'it adds to the paragraph before, '
                              'which said they will feel seen through, in his post\'s words ("You will think people are '
                              'judging you")', 'also')},
                    drop=['You will assume everyone can se'])


def cog_j(name='COG-J'):
    """The Cognitive Warning alone with its first two sentences joined (the edit on this turn's teaching card), as the
    marking page's block text has it: links as their words, the book's title in italics."""
    import re
    page = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', T.COG2)
    return from_old(name, 'cog', 'x1126a/receipts/COG-C5.receipt.json', 'As you de-armor, you will feel naked and '
                    'exposed, and', {'his_fixes': {COG_S1: COG_KEPT}, 'fit': {COG_S1: COG_KEPT}}, t=page,
                    swap={'Cognitive Warning: As you de-ar': (
                        'As you de-armor, you will feel naked and exposed, and', 'they expect to feel exposed as the armor '
                        'comes off, and to think everyone can see their anxiety, though people see much less of it than '
                        'they think', 'it is the next warning; the thought that comes with the feeling joined to it, as '
                        'its read asked', None),
                          'Nicholas Epley, Mindwise, call': (
                        'Nicholas Epley, *Mindwise*', 'they learn the mistake has a name and where to read about it',
                        'it names what the sentence before described', 'calls this')},
                    drop=['You will assume everyone can se'])


def cog(name='PAIR-COG-FACES-F1', v='f1'):
    if v == 'f1':
        return from_old(name, 'cog', 'x1126a/receipts/COG-C5.receipt.json', 'As you de-armor',
                        {'his_fixes': {COG_S1: COG_KEPT}, 'fit': {COG_S1: COG_KEPT}}, T.FACES)
    return from_old(name, 'cog', 'x1126a/receipts/COG-C5.receipt.json', 'As you de-armor',
                    {'his_fixes': {COG_S1: COG_KEPT}, 'fit': {COG_S1: COG_KEPT}}, T.FACES2,
                    swap={'Your armored brain also reads ': (
                        'Your armored brain also proje', 'they learn the second way their read goes wrong: their armored '
                        'brain projects the threat it feels onto neutral faces, so they will feel judged by people who are '
                        'mostly thinking about themselves', 'it adds to the paragraph before, which said they will feel '
                        'seen through, with his post\'s verb ("projects ... onto neutral faces")', 'also')})


# ---- his own versions, read fresh as folded

CARD = {'iso': 'his card on the Behavioral Warning, in his answers of 2026-11-26 00:50 UTC '
               '(x1125a/ANSWERS-X1125A-20261126-0050.json)',
        'lma': 'his card on the herbs, in his answers of 2026-11-24 18:40 UTC (x1123c/ANSWERS-X1123C-20261124-1840.json)',
        'agm': 'his card on the Agmatine Warning, in his answers of 2026-11-26 00:50 UTC '
               '(x1125a/ANSWERS-X1125A-20261126-0050.json)',
        'prec': 'his own Precautions paragraph, as his post has it (lineage W015-his)',
        'htp': 'his card on the warning for psychedelic users, in his answers of 2026-11-26 00:50 UTC '
               '(x1125a/ANSWERS-X1125A-20261126-0050.json)'}


def his_kept(key):
    return ('his own sentence, from ' + CARD[key] + ', unchanged in this step but for the label ' + MSG + ' folds in; '
            'a change to his own words goes to him first (AGENTS.md: a tested change goes in without a card "unless ... '
            'the words are his own"), so this mark goes to him in the turn\'s report with my best fix')


def v1(key, n):
    """Sentence N of the fold as the fresh readers read it (before the 5-HTP "it" was named)."""
    return S.sentences(T.plain(T.READ[key]))[n - 1]


def reader(kind, key):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Sonnet, 2026-11-26; Fable\'s usage limit was reached) given tools/humanization/%s and only '
            'the fold, one sentence a line (x1126c/v1/%s/%s/READ.md)' % (brief, kind, key))


def his(name, key, where, who, spec, opens, checked, unneeded, hf, fit, same, place, changed=(), t=None, also=None):
    """UNNEEDED: [(n, what the reader does with it)]; HF: [(n, difference)]; FIT: [(n, found)]. A sentence in CHANGED
    (numbers) was changed after the read, so its marks need no kept reason."""
    def kept_for(marks):
        k = {v1(key, n): his_kept(key) for n, _ in marks if n not in changed}
        k.update({v1(key, n): w for n, w in (also or {}).items()})
        return k
    return B.build(
        name, t or text(key), TOP + ': ' + where, YOU + who, spec, opens, checked,
        {'reader': reader('needed', key), 'unneeded': [v1(key, n) for n, _ in unneeded],
         'kept': {v1(key, n): w for n, w in unneeded}},
        {'reader': reader('his-fixes', key), 'marked': [{'s': v1(key, n), 'difference': d} for n, d in hf],
         'kept': kept_for(hf)},
        {'reader': reader('fit', key), 'marked': [{'s': v1(key, n), 'found': f} for n, f in fit], 'kept': kept_for(fit)},
        same + '; ' + MSG + ' folds its label into its first sentence', place)


ISO_S3 = {'f1': ('But don\'t fall', None),
          'a': ('But don\'t isolate completely', 'his own third sentence as his card has it, with his nickname after its '
                'don\'t, in brackets, as his label had it'),
          'b': ('But the isolation trap is', 'his nickname said as what it is, cutting yourself off completely, with his '
                'reason after it')}


def iso(name='ISO-F1', v='f1'):
    s3, how = ISO_S3[v]
    return his(
        name, 'iso', 'the Behavioral Warning, his nickname "the isolation trap" kept in its third sentence' +
        ('; ' + how if how else ''),
        'who tends to withdraw from people when working on themselves',
        {'This neural de-armoring': ('they learn the protocol asks them to cut the dopamine of chasing novelty, and what '
                                     'that dopamine does', 'it is the next warning after the plant medicines, the first '
                                     'about behavior', None),
         'The easiest way': ('they recognize the temptation the warning is about: to cut excitement by holing up alone',
                             'it names the easiest way to do what the sentence before asks', 'The easiest way'),
         s3: ('they don\'t cut themselves off completely, and know why: it spikes cortisol, the chronic stress hormone; '
              'his nickname names the mistake', 'it turns against the temptation just named', 'But'),
         'And cortisol': ('they learn what the cortisol does: it locks back in place the armor the protocol is removing',
                          'it says why a cortisol spike matters here', 'And cortisol'),
         'Calm company': ('they seek calm company, like a friend to walk in nature with, which works the other way',
                          'it gives what to do in place of isolating', 'none: it turns from the don\'t to what to do '
                          'instead, the step a reader expects after a don\'t'),
         'Good friends': ('they put their friendships ahead of the protocol when the two pull apart', 'it ends the '
                          'warning on his weighing of friends against the protocol', 'Good friends')},
        'they learn what the protocol asks them to give up, which the warning\'s trap comes from',
        [('isolation raises cortisol, which sensitizes the brain to glutamate', 'his own card version (' + CARD['iso'] +
          '); the article\'s section B on glutamate', 'yes: they see why cutting people off works against the protocol',
          'kept')],
        [(4, 'they learn isolating locks back in the armor the protocol is removing, which makes this a warning of the '
             'protocol\'s and not general advice; ' + his_kept('iso'))],
        [(1, '5, 1: opens on the protocol\'s demand, the reader outside it; "Phasic" with a definition'),
         (2, '10: "a break from that" points at the dopamine or the chase'),
         (3, '21: "the isolation trap" a label (his nickname, kept in the sentence by 72a)'),
         (4, '4, 1: glutamate unexplained; three ideas'), (5, '2, 10: two hormones glossed the same way'),
         (6, '6: a wise-sounding end, no act')],
        [(1, 'MISREAD: "starving your brain" sounds like a harsh deprivation until read as a break from novelty'),
         (2, 'MISREAD: "hole up alone" reads as permission until S3\'s "But"'),
         (3, 'CAN\'T TELL where "completely" begins')],
        'read the section for isolation and company: the rule right after it says which company, and the Aftermath '
        'says to build a tribe once de-armored; neither says why isolation harms',
        'fourth, where the post has it, with its rule after it', changed=() if v == 'f1' else (3,),
        t=None if v == 'f1' else T.plain(T.TRY2['iso-' + v]))


def lma():
    return his(
        'LMA-F1', 'lma', 'the herbs the protocol leaves out', 'who may already take lion\'s mane or ashwagandha, or be '
        'thinking of adding them for focus or stress',
        {'I\'m not advising': ('they learn he advises neither herb, though both are popular for focus and stress, and '
                               'why: some people report lasting anhedonia and sexual problems after stopping', 'it is the '
                               'next warning after the Cognitive Warning, the first about a supplement the protocol '
                               'leaves out', None),
         'Post-ashwa': ('they learn the lasting effect is rare, and is a kind of harm already known from SSRIs and '
                        'finasteride, so they weigh it before taking either herb', 'it weighs the reports the sentence '
                        'before gives', 'Post-ashwa')},
        'they learn his advice on two popular supplements they may be taking or considering, and why',
        [('regulators recognize the same kind of lasting effect after SSRIs and finasteride', 'the EMA recognized lasting '
          'sexual dysfunction after SSRIs and SNRIs in June 2019; the FDA added sexual problems continuing after stopping '
          'to finasteride\'s labels in 2011 and 2012 (x1122a/WARNINGS-SOURCES.md)', 'yes: they take the rare reports '
          'seriously enough to leave the herbs out', 'kept')],
        [(2, 'they learn the reports describe a rare harm of a kind regulators already recognize for SSRIs and '
             'finasteride, which is his reason the rare reports are worth heeding; ' + his_kept('lma'))],
        [(1, '1, 4, 9, 10: three ideas; "some people report" vague; the anhedonia gloss; "they" two ways'),
         (2, '1, 4, 6, 7, 9, 10, 12, 21: a coined name; "the same kind of thing" unsaid; "keep in mind" no act')],
        [(1, 'MISREAD: "I\'m not advising" as don\'t start or stop; "anhedonia (no desire)" as low libido only'),
         (2, 'CAN\'T TELL what to watch for; MISREAD: "rare" reassures while the comparison alarms')],
        'read the section for lion\'s mane and ashwagandha: no other warning names them, and the article advises neither',
        'after the Cognitive Warning and its second paragraph, before the agmatine warning, where his version has it')


AGM_S1 = {'f1': ('they learn what agmatine does in this protocol, a brake on glutamate signaling, under his nickname for '
                 'it', 'it is the next warning after the herbs, the first of three paragraphs on agmatine'),
          'a': ('they learn what agmatine does, a brake on glutamate signaling, under his nickname for it, and that this '
                'one, unlike the herbs just before, the protocol does use', 'it is the next warning after the herbs the '
                'protocol leaves out, and its "do" marks the contrast: this one it uses')}


def agm(name='AGM-F1', v='f1'):
    return his(
        name, 'agm', 'the agmatine warning, his nickname "voltage regulator" kept in its first sentence' +
        ('' if v == 'f1' else '; its opening tied to the herbs before it (72a: "then I fix ... agmatine\'s openings")'),
        'who takes some medication and is deciding whether agmatine is worth trying',
        {'Agmatine, the': AGM_S1[v] + (None,),
         'But we\'ll keep': ('they learn agmatine is optional, and why: it interacts with more medications than the '
                             'protocol\'s nutrients do', 'it turns from why it is used to why it is only optional', 'But'),
         'People may think': ('they stop assuming a common supplement is safe, and learn the three systems it acts on, '
                              'which the next paragraph\'s list of drugs follows from', 'it answers the reader who thinks '
                              'a shop supplement must be harmless', 'none: it answers the belief a reader brings to any '
                              'shop supplement, a new step after the interactions')},
        'they learn what agmatine is for here, so the warning is theirs if they take it',
        [('agmatine brakes NMDA activity', 'the article\'s own Shield section: "agmatine partially brakes NMDA activity", '
          '"a state-dependent brake"; Li et al. 1994; https://pmc.ncbi.nlm.nih.gov/articles/PMC1573177', 'yes: they see '
          'why it is in the protocol', 'kept')],
        [(1, 'they keep his nickname for agmatine, which ' + MSG + ' keeps in the sentence; the brake says what it does, '
             'and the nickname is how his post names it after this')],
        [(1, '4, 21: NMDA/glutamate unexplained; "voltage regulator" a label (his nickname, kept by 72a)'),
         (2, '4, 7: "a lot more medications" names none; "etc."'),
         (3, '1, 19, 4, 7, 2: a run of receptor names; "acts powerfully"; no act')],
        [(2, 'CAN\'T TELL which medications, e.g. a blood pressure pill'),
         (3, 'CAN\'T TELL whether my pill acts on these, or what caution means')],
        'his Precautions paragraph, right after, names the drugs; the Shield and section B say what agmatine is for',
        'where the post has it, before his Precautions paragraph', changed=() if v == 'f1' else (1,),
        t=None if v == 'f1' else T.plain(T.TRY2['agm-' + v]))


PREC_TAIL = {
    'f1': {'Not recommended': ('they leave agmatine out while pregnant or breast-feeding', 'it adds the next group who '
                               'should not take it', 'none: the next item of his precautions, which run as a list of who '
                               'should not take it'),
           'Use with extreme': ('they take extra care, or leave it out, after a psychotic episode, with low blood '
                                'pressure, or with kidney or liver problems', 'it gives the last group, those for whom it '
                                'needs extreme caution', 'none: the last item of his precautions list, those who need '
                                'extreme caution')},
    'a': {'It\'s not recommended': ('they leave agmatine out while pregnant or breast-feeding', 'it adds the next group '
                                    'who should not take it', 'none: the next item of his precautions, which run as a '
                                    'list of who should not take it'),
          'Use it with extreme': ('they take extra care, or leave it out, after a psychotic episode, with low blood '
                                  'pressure, or with kidney or liver problems', 'it gives the last group, those for whom '
                                  'it needs extreme caution', 'none: the last item of his precautions list, those who '
                                  'need extreme caution')},
    'c': {'It\'s not recommended': ('they leave agmatine out while pregnant or breast-feeding', 'it adds the next group '
                                    'who should not take it', 'none: the next item of his precautions, which run as a '
                                    'list of who should not take it'),
          'Use with extreme': ('they take extra care, or leave it out, after a psychotic episode, with low blood '
                               'pressure, or with kidney or liver problems', 'it gives the last group, those for whom it '
                               'needs extreme caution', 'none: the last item of his precautions list, those who need '
                               'extreme caution')},
    'b': {'It\'s not recommended': ('they leave agmatine out while pregnant or breast-feeding, and take extra care, or '
                                    'leave it out, after a psychotic episode, with low blood pressure, or with kidney '
                                    'or liver problems', 'it adds the last two groups, who should not take it or need '
                                    'extreme caution', 'none: the next items of his precautions, which run as a list of '
                                    'who should not take it')}}
TAIL_KEPT = ('his own words, with the subject named ("It\'s"%s), the near-miss step after the fold read Human Low over '
             'these two sentences (checks-1126r); the rest of what the read marks is his and goes to him with my best fix')


def prec(name='PREC-F1', v='f1'):
    also = {} if v == 'f1' else {2: TAIL_KEPT % (', "it"' if v == 'a' else '' if v == 'c' else ', and the two joined'),
                                 3: TAIL_KEPT % (', "it"' if v == 'a' else '' if v == 'c' else ', and the two joined')}
    if v == 'c':   # its last sentence is his, unchanged: his_kept says why its marks stay
        del also[3]
    return his(
        name, 'prec', 'his Precautions paragraph after the agmatine warning, its subject named', 'who takes some '
        'medication and is deciding whether agmatine is worth trying',
        {'Do not use agmatine': ('they check what they take against the drugs named, and don\'t combine agmatine with any '
                                 'of them without a physician who can weigh the interactions', 'it names the medications '
                                 'the warning before says agmatine interacts with', None), **PREC_TAIL[v]},
        'they learn which medications agmatine must not be combined with, so they can check their own',
        [('the drugs and groups to keep agmatine away from', CARD['prec'] + '; the article\'s agmatine section names the '
          'same', 'yes: they check their own medications and conditions against it', 'kept')],
        [],
        [(1, '1, 19, 4, 10, 5, 13: four drug groups in one sentence; "complex psychoactive stacks"; "(will reduce '
             'tolerance)" two ways'),
         (2, '12, 7: a new case standing alone; no reason'), (3, '19, 15, 4, 12, 13: "extreme caution" no act')],
        [(1, 'CAN\'T TELL how far apart counts as "concurrently"; what "competent" means'),
         (3, 'CAN\'T TELL whether my blood pressure counts as low; "extreme caution" no act')],
        'read the section for agmatine\'s interactions: the warning before says it interacts with more medications, '
        'and this names them; the article\'s agmatine section gives the same list',
        'right after the agmatine warning, where the post has it', t=None if v == 'f1' else T.plain(T.TRY2['prec-' + v]),
        also=also)


def htp():
    return his(
        'HTP-F1', 'htp', 'the warning for people who use psychedelics, its subject named', 'who uses psychedelics now and '
        'then and may take an antidepressant or other medication',
        {'Uridine and 5-HTP': ('they learn the two supplements can change how strongly a psychedelic hits, so they don\'t '
                               'start everything at once', 'it is the last warning, for those who use psychedelics', None),
         'Especially dangerous': ('they don\'t take 5-HTP with anything else that raises serotonin, and know why',
                                  'it turns to the one of the two with a danger of its own', 'Especially dangerous'),
         'That\'s how': ('they learn the danger is serotonin syndrome, which can kill, and where the article says more',
                         'it names what the mix in the sentence before leads to', 'That\'s how'),
         'The following drugs': ('they check what they take against the list and leave 5-HTP out if one is there',
                                 'it names the drugs the sentence before means', 'The following drugs are especially '
                                 'dangerous'),
         'Do not use 5-HTP': ('they keep 5-HTP away from iboga, microdoses included, and know why', 'it adds the '
                              'protocol\'s own plant medicine, which the list leaves out', 'none: a new case after the '
                              'list, iboga, the protocol\'s own plant medicine')},
        'they see the warning is for them if they use psychedelics, and what not to mix',
        [('MAOIs include ayahuasca', 'the harmala alkaloids of ayahuasca\'s vine inhibit MAO-A, which breaks serotonin '
          'down (https://pmc.ncbi.nlm.nih.gov/articles/PMC9121195)', 'yes: they see ayahuasca is on the list', 'kept'),
         ('noribogaine is in iboga\'s effect', 'the primary, long-lived metabolite of ibogaine, a serotonin uptake '
          'inhibitor (https://www.ebi.ac.uk/chebi/CHEBI:146264; https://pubmed.ncbi.nlm.nih.gov/11303040/)', 'yes: they '
          'see why iboga gets its own line', 'kept'),
         ('"it" in the last sentence', 'a fresh reader of the fold took it as the list\'s drugs (v1/fit/htp)', 'yes: they '
          'know the line is about 5-HTP, now named', 'changed')],
        [],
        [(1, '4, 15: "everything" names nothing; no act'), (3, '10, 4: "That" two ways; the syndrome not pictured'),
         (4, '1, 16, 19: twelve names after a lead S2 already gave'),
         (5, '10, 12, 4, 21: "it" two ways; "anywhere near" no gap')],
        [(1, 'CAN\'T TELL what to stagger, or by how long'), (2, 'CAN\'T TELL whether psilocybin counts'),
         (3, 'CAN\'T TELL the signs'), (4, 'CAN\'T TELL what to do if my SSRI is on it'),
         (5, 'CAN\'T TELL how far apart is safe; MISREAD: "it" as the list')],
        'the 5-HTP section gives the stop signs and the interactions in his words; this is the short form at the top, '
        'which the post has in both places, and the uridine paragraph follows it',
        'last of the warnings, where the post has it', changed=(5,))


def concat(name, parts, firsts, where, who, same, place):
    """A receipt for paragraphs checked together: each part's receipt (written above, in OUT) gives its sentences'
    payoffs, links, checks and reads; FIRSTS gives the link of each later paragraph's first sentence."""
    rs = [json.loads((OUT / (p + '.receipt.json')).read_text(encoding='utf-8')) for p in parts]
    t = '\n\n'.join((OUT / (p + '.txt')).read_text(encoding='utf-8').rstrip('\n') for p in parts)
    spec = {}
    for i, r in enumerate(rs):
        for j, x in enumerate(r['sentences']):
            link = x.get('link')
            if j == 0:
                link = None if i == 0 else firsts[i - 1]
            spec[x['s']] = (x['payoff'], x['follows'], link)

    def merge(k, field):
        out = {'reader': '; '.join(r[k]['reader'] for r in rs), field: [m for r in rs for m in r[k].get(field, [])],
               'kept': {}}
        for r in rs:
            out['kept'].update(r[k].get('kept', {}))
        return out
    return B.build(name, t, where, who, spec, rs[0]['opens']['why_reading'],
                   [(c['point'], c['found'], c['still_needed'], c['fate']) for r in rs for c in r['checked']],
                   merge('needed', 'unneeded'), merge('his_fixes', 'marked'), merge('fit', 'marked'), same, place)


NEXT = 'none: the next warning in the list, a new item'


def stretch():
    for f in (rule, cog, lma, agm):
        assert not f()
    return concat('STRETCH-RULE-AGM-F1', ['RULE-F1', 'PAIR-COG-FACES-F1', 'LMA-F1', 'AGM-F1'], [NEXT] * 3,
                  TOP + ': the five from The Rule to the agmatine warning, each with its label folded in',
                  YOU + 'who reads the warnings one after another', 'each warning in the stretch makes its own point; '
                  'none repeats another (read from The Rule to the agmatine warning)', 'the middle of the warnings, '
                  'where the post has them, between the Behavioral Warning and his Precautions paragraph')


ALL = {'dmso': dmso, 'elec': elec, 'ethno': ethno, 'iso': iso, 'rule': rule, 'cog': cog, 'lma': lma, 'agm': agm,
       'prec': prec, 'htp': htp,
       'iso-a': lambda: iso('ISO-F2A', 'a'), 'iso-b': lambda: iso('ISO-F2B', 'b'),
       'rule-a': lambda: rule('RULE-F2A', 'a'), 'rule-b': lambda: rule('RULE-F3B', 'b'),
       'ethno-a': lambda: ethno('ETHNO-F2A', 'a'), 'cog-c': cog3, 'cog-j': cog_j, 'cog-d': lambda: cog3('PAIR-COG-FACES-F4', T.FACES4), 'cog-b': lambda: cog('PAIR-COG-FACES-F2', 'b'), 'agm-a': lambda: agm('AGM-F2A', 'a'),
       'prec-a': lambda: prec('PREC-F2A', 'a'), 'prec-c': lambda: prec('PREC-F3', 'c'), 'prec-b': lambda: prec('PREC-F2B', 'b'), 'stretch': stretch}

if __name__ == '__main__':
    keys = sys.argv[1:] or list(ALL)
    bad = [x for k in keys for x in ALL[k]()]
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')
    sys.exit(1 if bad else 0)
