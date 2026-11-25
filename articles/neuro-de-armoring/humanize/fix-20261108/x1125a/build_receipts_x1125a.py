"""The receipts for x1125a's third versions (texts_x1125a.V3): the warnings at the top, each fixed for sense first.
The reads are v2/needed, v2/his-fixes and v2/fit (fresh Fable readers, 2026-11-25, of the version before this one);
every sentence they marked is changed in V3, or kept here with why. Sources for what was checked: texts_x1125a.SOURCES.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/build_receipts_x1125a.py [KEY ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'x1123a'))
sys.path.insert(0, str(HERE.parent / 'x1123b'))
sys.path.insert(0, str(HERE))
import build_receipts_x1123b as BB  # noqa: E402  (its fill allows a link of "none: why")
import texts_x1125a as T  # noqa: E402

B = BB.B
S = B.S
OUT = HERE / 'v4'  # build_receipts_v6.py sets B.HERE to v6 for the second tries
B.HERE = OUT
TOP = 'A Complete Guide to Bio-De-Armoring, the warnings at the top'
YOU = ('an adult with trauma or an addiction who has read the short introduction and is reading the warnings before '
       'starting the protocol, ')
SRC = T.SOURCES


def reader(kind, key):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-25) given tools/humanization/%s and only the text, one sentence a line, of '
            'the version before this one (x1125a/v2/%s/%s/READ.md)' % (brief, kind, key))


def old(key):
    return S.sentences(T.plain(T.V2[key]))


PARTS = {}
REGISTER_ONLY = False   # build_receipts_v6.py takes each paragraph's parts without building version 4 again


def build(key, where, who, spec, opens, checked, unneeded, his, fit, same, place, his_kept=None, fit_kept=None,
          needed_kept=None):
    PARTS[key] = dict(where=where, who=who, spec=spec, opens=opens, checked=checked, unneeded=unneeded, his=his, fit=fit,
                      same=same, place=place, his_kept=his_kept or {}, fit_kept=fit_kept or {},
                      needed_kept=needed_kept or {})
    if REGISTER_ONLY:
        return []
    return _build(key.upper() + '4', T.plain(T.V4[key]), [key], {})


def pair(k1, k2, link2):
    """A paragraph under 50 words with its neighbour, as the check reads them: both paragraphs, a blank line between.
    LINK2 is the link of the second paragraph's first sentence (it has one here, being no longer the text's first)."""
    for k in (k1, k2):
        if k not in PARTS:
            ALL[k]()
    text = T.plain(T.V4[k1]) + '\n\n' + T.plain(T.V4[k2])
    return _build('PAIR-%s-%s4' % (k1.upper(), k2.upper()), text, [k1, k2], link2)


def _build(name, text, keys, link2):
    P = [PARTS[k] for k in keys]
    spec = {}
    for n, (k, p) in enumerate(zip(keys, P)):
        for start, (pay, fol, link) in p['spec'].items():
            if n and link is None:
                link = link2[k]
            spec[start] = (pay, fol, link)

    def marks(field):
        return [(k, n, d) for k, p in zip(keys, P) for n, d in p[field]]

    def kept(field):
        return {old(k)[n - 1]: w for k, p in zip(keys, P) for n, w in p[field].items()}
    key = keys[-1] if len(keys) > 1 else keys[0]
    return B.build(
        name, text, '; '.join(p['where'] for p in P), YOU + P[-1]['who'], spec, P[0]['opens'],
        [c for p in P for c in p['checked']],
        {'reader': '; '.join(reader('needed', k) for k in keys),
         'unneeded': [old(k)[n - 1] for k, p in zip(keys, P) for n in p['unneeded']], 'kept': kept('needed_kept')},
        {'reader': '; '.join(reader('his-fixes', k) for k in keys),
         'marked': [{'s': old(k)[n - 1], 'difference': d} for k, n, d in marks('his')], 'kept': kept('his_kept')},
        {'reader': '; '.join(reader('fit', k) for k in keys),
         'marked': [{'s': old(k)[n - 1], 'found': f} for k, n, f in marks('fit')], 'kept': kept('fit_kept')},
        ' / '.join(p['same'] for p in P), ' / '.join(p['place'] for p in P))


def dmso():
    return build(
        'dmso', TOP + ': the first item, DMSO Safety', 'who has never used DMSO',
        {'DMSO Safety:': ('they learn the protocol will have them smell DMSO, and what for, so the warning is about '
                          'something they will do', 'it is the first warning under the section\'s heading', None),
         "It's a solvent": ('they learn what DMSO is and the one thing every rule after it rests on: it carries what is '
                            'with it into the blood', 'it says what the thing just named is', "It's a solvent"),
         'So you should use': ('they buy the pure grade, in glass, and know why each', 'it is the first thing that '
                               'follows from what it carries in: what is in the bottle', 'So'),
         "It's sold on Amazon": ('they know an ordinary seller will do, from his own experience', 'it says where to get '
                                 'the kind just named', "It's sold"),
         'Before using it': ('they wash lotions and products off their hands and nose first', 'it is the second thing '
                             'that follows: what is on them', 'Before using it'),
         'Your lungs count too': ('a smoker breathes in only a little at a time and stops at the first sign', 'it takes '
                                  'the third place the warning names, the lungs', 'Your lungs count too'),
         'My full DMSO reference': ('they know his reference has the other ways to use it and the rest of what to watch '
                                    'for', 'it closes the item, as the post does',
                                    'none: the pointer to his reference, which the post\'s item ends on')},
        'they learn the protocol will have them smell DMSO, so this warning is for them before they buy any',
        [('glass over plastic', 'DMSO is not compatible with many plastics and can extract compounds from them (' +
          SRC['glass'] + ')', 'yes: they choose a glass bottle and know why', 'kept'),
         ('clean skin, and a smoker\'s lungs', SRC['dmso-smoker'], 'yes: they wash products off first, and a smoker '
          'breathes in less and stops when weak', 'kept')],
        [], [(6, '4, 7')], [(6, 'ANYWAY: weak on any day; CAN\'T TELL: how much is much, and what to do')],
        'read the section from its heading to the next for DMSO: no other warning names it; the Shield\'s DMSO item and '
        'the Fog rescue give the use, and his experience paragraph gives nebulizing',
        'first under the heading, where the post has it, before the other substances\' warnings')


def elec():
    return build(
        'elec', TOP + ': Electrolytes', 'who may have a kidney or heart condition or take blood pressure pills',
        {'Electrolytes:': ('they learn the protocol means much more potassium, and that with kidney disease, a heart '
                           'condition or such a drug they see a doctor first', 'the next warning after DMSO', None),
         'Those are the ACE': ('they can match their own pill by its name, and learn what goes wrong: potassium builds '
                               'up in the blood', 'it says which drugs the sentence before means', 'Those are')},
        'they learn the protocol means much more potassium than they eat now, and who sees a doctor first',
        [('ACE inhibitors and ARBs hold on to potassium; names end in -pril and -sartan',
          SRC['ace'] + '; https://www.kidney.org/kidney-topics/ace-inhibitors-and-arbs (generic names end in "-pril" and '
          '"-sartan"; they can raise the level of potassium in the blood)', 'yes: they check the name of their pill and '
          'ask a doctor before the potassium', 'kept')],
        [], [(2, '4, 10')], [(2, 'CAN\'T TELL: which pill is one; MISREAD: sounds like heart patients only')],
        'the Electrolytes paragraph in the Shield gives the same caution beside the potassium target; this is its short '
        'form at the top, which the post has in both places',
        'second, where the post has it')


def ethno():
    return build(
        'ethno', TOP + ': Ethnobotanicals', 'who may be on medication and has never taken iboga',
        {'Ethnobotanicals:': ('they learn which two plant medicines the protocol uses and what iboga is',
                              'the next warning', None),
         'Both are illegal': ('they check the law where they are, and take iboga\'s danger to the heart and nervous '
                              'system seriously', 'it says what holds for the two just named', 'Both'),
         'So never combine': ('they don\'t take iboga with a medication until they have checked it in his guide, and '
                              'know where the dosing is', 'it follows from the danger just named', 'So')},
        'they learn which plant medicines the protocol uses, before the law and the risks',
        [('iboga\'s risk is to the heart and nervous system', 'the article\'s own 5-HTP warning: "ibogaine and '
          'noribogaine ... already carry serious cardiac and neurological risk"', 'yes: they treat iboga as the '
          'dangerous one of the two', 'kept')],
        [], [(2, '2, 4'), (3, '4, 5')], [(2, 'ANYWAY: both act on the nervous system'),
                                         (3, 'CAN\'T TELL: which medications, how far apart, which to leave out')],
        'read the section for iboga: the 5-HTP warning gives its serotonin and heart risks for 5-HTP users; this is '
        'the one place for the law and for medications in general',
        'third, where the post has it')


def iso():
    return build(
        'iso', TOP + ': the Behavioral Warning', 'who tends to withdraw from people when working on themselves',
        {'Behavioral Warning': ('they learn what the protocol has them cut: the bursts from excitement, novelty and the '
                                'chase', 'the next warning, the first about behavior', None),
         'The easiest way': ('they don\'t shut themselves away to do it, and know why: total isolation raises cortisol, '
                             'which locks the armor in place, addiction or not', 'it says what cutting excitement '
                             'tempts them to do', 'The easiest way to do'),
         "Since we're social": ('they keep company that calms them, and look to the rule below for which kind',
                                'it gives what to do in place of isolating', "Since we're social animals, what")},
        'they learn what the protocol asks them to give up, which the warning is about',
        [],
        [], [(1, '19'), (2, '8; 9, 13'), (3, '10, 12; 7'), (4, '5, 12; 4; 21')],
        [(2, 'CAN\'T TELL: how much contact is enough; FROM: addiction; MISREAD: "completely" lets me off'),
         (3, 'MISREAD: "It"; "sensitizes" sounds good'), (4, 'CAN\'T TELL: what counts as calm company')],
        'read the section for isolation and company: the rule right after it says which company, and the Aftermath at '
        'the end says to build a tribe once de-armored; neither says why isolation harms',
        'fourth, where the post has it, with its rule after it',
        his_kept={1: 'the three are the post\'s own bracket for what phasic dopamine is, and what the rule below is '
                     'about; a case from the reader\'s life would be mine to invent, not the article\'s'},
        fit_kept=None)


def rule():
    return build(
        'rule', TOP + ': the rule after the Behavioral Warning', 'who has just read not to isolate completely',
        {'The Rule:': ('they look for company side by side, like reading next to someone, and touch that feels safe',
                       'it is the rule the paragraph before points to', None),
         'As tempting as': ('they stay out of romance and high-stakes drama for now, knowing the pull is expected and '
                            'that it puts the armor back up', 'it gives the other kind, the one to avoid',
                            'As tempting as')},
        'they get the kind of company to look for, which the paragraph before promised',
        [],
        [], [(1, '4'), (2, '2, 14; 4, 10')],
        [(1, 'CAN\'T TELL: what touch is safe; FROM: child-safety wording'),
         (2, 'CAN\'T TELL: a new romance or the partner I have; MISREAD: stay away from my partner')],
        'none: read the section for which company to keep; only this rule says it',
        'right after the Behavioral Warning, whose last sentence hands over to it')


def cog():
    return build(
        'cog', TOP + ': the Cognitive Warning', 'who gets anxious around people',
        {'Cognitive Warning:': ('they expect to feel more exposed than usual as the armor comes off, and know that '
                                'others see far less of their anxiety than it feels like', 'the next warning', None)},
        'they learn they will feel exposed, and that it isn\'t as visible as it feels',
        [('what the "Illusion of Transparency" is', 'a tendency to overestimate how much others can discern one\'s '
          'internal states (Gilovich, Savitsky and Medvec, 1998: https://pubmed.ncbi.nlm.nih.gov/9731312/); the post '
          'credits Epley\'s book, which describes it', 'yes: they know the feeling of being seen through is a known '
          'illusion', 'kept')],
        [2], [(2, '5, 11, 7')], [],
        'the paragraph after it gives the second half of the warning (reading threat into faces) and the rule',
        'fifth, where the post has it')


def proj():
    return build(
        'proj', TOP + ': the second paragraph of the Cognitive Warning', 'who often feels judged in a room',
        {'Your armored brain': ('they learn the second way their read goes wrong: they will feel judged by people who '
                                'are mostly thinking about themselves', 'it adds to the paragraph before, which said '
                                'they will feel seen through', None),
         'So the rule': ('they distrust their read of a room during the protocol, at least until their heart rate is '
                         'back down, and know why the heart rate is the test', 'it gives the rule both paragraphs lead '
                         'to', 'So the rule')},
        'they learn why they will feel judged, right after learning they will feel seen through',
        [('a racing heart means the reasoning brain is offline', 'the article\'s section A (blood flow shifts away '
          'from the cortex once the heart rate goes up) and Scenario A ("your Reasoning Brain is offline")',
          'yes: they know why the heart rate is the test', 'kept')],
        [], [(1, '21'), (2, '5, 14, 16'), (3, '16, 4, 10')],
        [(2, 'MISREAD: wider than feeling judged'), (3, 'ANYWAY: pulse is up in any room; CAN\'T TELL: which bar; '
                                                    'MISREAD: calm pulse means my read is right')],
        'the heart-rate test is also in Scenario A and Scenario C, in the same words (his 62a)',
        'right after the Cognitive Warning\'s first paragraph')


def agm():
    return build(
        'agm', TOP + ': the Agmatine Warning, before his Precautions paragraph',
        'who takes some medication and is deciding whether agmatine is worth trying',
        {'Agmatine Warning': ('they learn agmatine is optional and, though sold as a supplement, acts on several brain '
                              'signaling systems at once', 'the next warning, the first of three paragraphs on '
                              'agmatine', None),
         'That means': ('they go by the precautions below if they take it, since it can clash with drugs that work on '
                        'the same systems', 'it says what follows from acting on several systems', 'That means')},
        'they learn agmatine is optional, so the warning is theirs only if they take it',
        [],
        [], [(1, '1, 2'), (2, '10')], [],
        'his Precautions paragraph, right after, names the drugs; the Shield and section B say what agmatine is for',
        'where the post has it, before his Precautions paragraph',
        his_kept={1: 'the plain meaning comes first and the four systems after it in brackets, the way his own UMP '
                     'paragraph gives its technical names, and his Precautions paragraph right below names the drugs '
                     'each one matters for, so a clause on each here would say them twice; the two nutrients are the '
                     'ones the article sets agmatine against in "Agmatine vs PS vs Phosphatidylcholine"'})


def htp():
    return build(
        'htp', TOP + ': the warning for people who use psychedelics', 'who uses psychedelics now and then and may take '
        'an antidepressant or other medication',
        {'Uridine & 5-HTP': ('they don\'t reach for either supplement to boost a trip', 'the last warning, for those who '
                             'use psychedelics', None),
         'In practice they': ('they stop counting on their usual dose acting the way it used to', 'it gives the reason '
                              'for the don\'t before it', 'In practice they'),
         '5-HTP is also': ('they learn the second danger, of 5-HTP alone: on top of anything else that raises '
                           'serotonin it can cause serotonin syndrome, which can kill', 'it turns to the one of the two '
                           'that has a danger of its own', '5-HTP is also'),
         'So never take': ('they check what they take against the list and leave the 5-HTP out if one is there',
                           'it gives the act the danger calls for', 'So never take it'),
         'Rule: psychedelics': ('they keep 5-HTP off trip days, and away from ayahuasca and iboga altogether, iboga '
                                'microdoses too', 'it takes the same danger to psychedelics',
                                'psychedelics act on serotonin too'),
         "That's because": ('they know why those two get the stricter rule', 'it gives the reason for the rule\'s '
                            'second half', "That's because")},
        'they see the warning is for them if they use psychedelics, and the first don\'t',
        [('MAO-A breaks serotonin down, and harmalas inhibit it', SRC['mao-a'], 'yes: they see why ayahuasca is on '
          'the list', 'kept'),
         ('noribogaine is what the body turns ibogaine into', SRC['noribogaine'], 'yes: they can place the second '
          'name', 'kept'),
         ('iboga microdoses count', 'his own Weeks 3-7 line: "don\'t take 5-HTP at all while you\'re microdosing iboga '
          'or elliptica"', 'yes: they don\'t take 5-HTP in the weeks they microdose iboga', 'kept'),
         ('psychedelics act on serotonin', 'his own Weeks 3-7 line ("Mushrooms act on serotonin too") and the 5-HTP '
          'section ("serotonergic psychedelics/entactogens")', 'yes: they see why a trip day is ruled out', 'kept')],
        [], [(1, '14'), (2, '4, 12, 16'), (4, '4'), (5, '2, 4, 5, 13'), (6, '1, 4, 7, 12')],
        [(2, 'CAN\'T TELL: which way; MISREAD: sounds like they work on a trip'),
         (4, 'CAN\'T TELL: my antidepressant\'s class; things taken once'),
         (5, 'CAN\'T TELL: how many days; do microdoses count'), (6, 'MISREAD: alarm about the protocol\'s own iboga')],
        'the 5-HTP section gives the stop signs and the interactions in his words; this is the short form at the top, '
        'which the post has in both places, and the uridine paragraph follows it',
        'last of the warnings, where the post has it, with the 5-HTP rule moved up into it from the next paragraph so '
        'everything about 5-HTP is in one place',
        his_kept={1: 'the quoted "trip enhancers" is the pull itself; the why-you\'d-want-to is said once in this '
                     'section already (the Isolation Trap), and lesson neuro-2026-11-24f is against a rule applied '
                     'everywhere'})


def uri():
    return build(
        'uri', TOP + ': the uridine half of the warning for people who use psychedelics', 'who uses psychedelics now and '
        'then and knows their usual dose',
        {'Uridine (the UMP': ('they learn uridine\'s caution is a different one from 5-HTP\'s, where it comes from, and '
                              'what it is: within a day, psychedelics can hit harder', 'it turns to the second of the '
                              'two supplements the warning names', None),
         'So do not take UMP': ('they keep UMP off trip days and take less than their old dose on the first trip after '
                                'starting it', 'it gives the act', 'So'),
         'It may also': ('they know the vivid dreams and weaker cravings are what UMP is for, not a danger sign',
                         'it adds the other changes the post lists', 'It may also')},
        'they learn the serotonin danger just described isn\'t uridine\'s, and what uridine\'s is',
        [('within a day; psychedelics hit harder; dreams and cravings', 'his uridine section: Scott\'s cravings "fell '
          'hard" within a day and his tolerance "seemed to drop too"; "Vivid dreams and increased sensitivity to '
          'psychedelics are the hoped-for benefits of UMP ... you should not take the old high doses of your psychedelic '
          'at first"', 'yes: they take less on the first trip after starting it', 'kept')],
        [], [(1, '1, 4'), (2, '9, 10'), (3, '2, 4, 24')],
        [(1, 'MISREAD: reads like a list of perks'), (2, 'MISREAD: "this" covers the serotonin claim too'),
         (3, 'CAN\'T TELL: how much less; whether a microdose day counts')],
        'the uridine section says the same of its benefits and of the old high doses, in his words; this is the short '
        'form at the top',
        'right after the 5-HTP paragraph, which names both supplements')


ALL = {'dmso': dmso, 'elec': elec, 'ethno': ethno, 'iso': iso, 'rule': rule, 'cog': cog, 'proj': proj, 'agm': agm,
       'htp': htp, 'uri': uri}

PAIRS = {'pair-iso-rule': lambda: pair('iso', 'rule', {'rule': 'none: a new paragraph, the rule the one before it '
                                                             'hands over to'}),
         'pair-cog-proj': lambda: pair('cog', 'proj', {'proj': 'Your armored brain also'})}

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    bad = []
    for k in (sys.argv[1:] or list(ALL) + list(PAIRS)):
        bad += (ALL.get(k) or PAIRS[k])()
    print('\n'.join(bad) or 'receipts: PASS')
