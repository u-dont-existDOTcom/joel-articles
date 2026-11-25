"""The receipts for x1125a's second tries (texts_x1125a.V6): the DMSO item, Electrolytes, the Isolation Trap, the
Cognitive Warning's second paragraph, the Agmatine Warning's first paragraph and the 5-HTP warning, after batch x1125c.
For the four rewritten ones the reads are v5/needed, v5/his-fixes and v5/fit (fresh Fable readers, 2026-11-25, of
version 5); for the DMSO item and Electrolytes, whose changes are the ones their check called for, the reads are v2's.
Every sentence a read marked is changed, or kept here with why.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/build_receipts_v6.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_receipts_x1125a as R  # noqa: E402

T, B, S, YOU, TOP, SRC = R.T, R.B, R.S, R.YOU, R.TOP, R.SRC
OUT = HERE / 'v6'
B.HERE = OUT
POST = 'the post\'s own words, which the fidelity keys hold to their meaning; '


def rd(kind, key, ver):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Fable, 2026-11-25) given tools/humanization/%s and only the text, one sentence a line, of '
            'version %s (x1125a/%s/%s/%s/READ.md)' % (brief, ver[1:], ver, kind, key))


def build(key, ver, text, where, who, spec, opens, checked, his, fit, same, place, his_kept=None, fit_kept=None,
          name=None, link2=None):
    o = S.sentences(T.plain(T.VERSIONS[ver][key]))
    return B.build(
        name or key.upper() + '6', text, where, YOU + who, spec, opens, checked,
        {'reader': rd('needed', key, ver), 'unneeded': [], 'kept': {}},
        {'reader': rd('his-fixes', key, ver), 'marked': [{'s': o[n - 1], 'difference': d} for n, d in his],
         'kept': {o[n - 1]: w for n, w in (his_kept or {}).items()}},
        {'reader': rd('fit', key, ver), 'marked': [{'s': o[n - 1], 'found': f} for n, f in fit],
         'kept': {o[n - 1]: w for n, w in (fit_kept or {}).items()}},
        same, place)


def P(key):
    return R.PARTS[key]


def main():
    R.REGISTER_ONLY = True
    for k in R.ALL:
        R.ALL[k]()          # fills R.PARTS
    V = T.V6
    bad = []
    p = P('dmso')
    spec = {k: v for k, v in p['spec'].items() if not k.startswith('My full')}
    spec['Your lungs count too'] = ('a smoker breathes in only a little at a time and stops at the first sign, and '
                                    'knows his reference has the rest', spec['Your lungs count too'][1],
                                    'Your lungs count too')
    bad += build('dmso', 'v2', T.plain(V['dmso']), p['where'], p['who'], spec, p['opens'], p['checked'],
                 [(6, '4, 7')], [(6, 'ANYWAY: weak on any day; CAN\'T TELL: how much is much, and what to do')],
                 p['same'], p['place'])
    p = P('elec')
    bad += build('elec', 'v2', T.plain(V['elec']), p['where'], p['who'],
                 {'Electrolytes:': ('they learn the protocol means much more potassium (potatoes and greens every '
                                    'day), who sees a doctor first, and what goes wrong: potassium builds up in the '
                                    'blood', 'the next warning after DMSO', None)},
                 p['opens'], p['checked'], [(2, '4, 10')],
                 [(2, 'CAN\'T TELL: which pill is one; MISREAD: sounds like heart patients only')], p['same'], p['place'])
    p = P('iso')
    bad += build('iso', 'v5', T.plain(V['iso']), p['where'], p['who'],
                 {'Behavioral Warning': ('they learn what the protocol has them cut, the trap that follows (holing up '
                                         'alone) and the don\'t', 'the next warning, the first about behavior', None),
                  'Total social isolation': ('they learn why: isolation spikes cortisol, which locks the armor in '
                                             'place, addiction or not', 'it gives the reason for the don\'t just '
                                             'before it', 'Total social isolation'),
                  "We're social animals": ('they keep the calm kind of company, and look to the rule below for what '
                                           'counts', 'it gives what to do in place of isolating',
                                           "We're social animals, so what")},
                 'they learn what the protocol asks them to give up and the trap in it, which the warning is about',
                 [], [(1, '19'), (2, '9; 4'), (3, '16')], [(2, 'FROM: addiction')], p['same'], p['place'],
                 his_kept={1: 'the three are the post\'s own bracket for what phasic dopamine is, what the rule below '
                              'is about; a case from the reader\'s life would be mine to invent',
                           2: POST + 'the article is for trauma and addiction by its title, and the clause tells the '
                              'reader with no addiction that this is theirs too; glutamate is explained where the '
                              'protocol takes it up (section B), and a gloss here, with cortisol\'s, read as the '
                              'explainer register in the check of version 4 (100% AI)'},
                 fit_kept={2: 'the article\'s title names addiction ("Healing for Trauma & Addiction"), which the '
                              'reader of the brief didn\'t have'})
    p = P('proj')
    bad += build('proj', 'v5', T.plain(V['proj']), p['where'], p['who'],
                 {"You'll also feel": ('they learn the second way their read goes wrong: they will feel judged by '
                                       'people mostly thinking about themselves, and why', 'it adds to the paragraph '
                                       'before, which said they will feel seen through', None),
                  'So during this protocol': ('they don\'t go by their read of people during the protocol',
                                              'it gives the rule the two paragraphs lead to', 'So during this protocol'),
                  'A racing heart': ('they treat every room as misread at least until their heart rate is back down, '
                                     'and know why the heart is the test', 'it gives the rule its test, the state '
                                     'first', 'A racing heart means')},
                 p['opens'], p['checked'], [(2, '16, 25, 10, 4')],
                 [(2, 'ANYWAY: pulse is up in any room; CAN\'T TELL: which bar, and whether a calm pulse is enough')],
                 p['same'], p['place'])
    p = P('agm')
    bad += build('agm', 'v5', T.plain(V['agm']), p['where'], p['who'],
                 {'Agmatine Warning': ('they learn agmatine is optional and not to think of it as a nutrient because '
                                       'it is sold as a supplement', 'the next warning, the first of three paragraphs '
                                       'on agmatine', None),
                  "It's a neuromodulator": ('they learn what it is and that it works on several systems at once',
                                            'it says what it is, after what it isn\'t', "It's a neuromodulator"),
                  'So it can clash': ('they check what they take against the precautions below', 'it says what '
                                      'follows from working on those systems', 'So')},
                 p['opens'], [], [(1, '2'), (2, '1')], [(2, 'MISREAD: sounds as if agmatine acts like an opioid')],
                 p['same'], p['place'],
                 his_kept={1: POST + 'the two nutrients are the ones the article sets agmatine against in "Agmatine vs '
                              'PS vs Phosphatidylcholine", and both names are held'})
    p = P('htp')
    bad += build('htp', 'v5', T.plain(V['htp']), p['where'], p['who'],
                 {'Uridine & 5-HTP': ('they don\'t use either supplement to boost a trip, and go lower than their '
                                      'usual dose until they see how it hits', 'the last warning, for those who use '
                                      'psychedelics', None),
                  '5-HTP is the one': ('they learn why 5-HTP is the risky one: serotonin syndrome, which can kill, '
                                       'comes from mixing it with anything else that raises serotonin', 'it turns to '
                                       'the one of the two with a danger of its own', '5-HTP is the one'),
                  'So do not combine': ('they check what they take against the list', 'it gives the act the danger '
                                        'calls for', 'So do not combine it'),
                  'Rule: psychedelics': ('they keep 5-HTP off trip days, and away from ayahuasca and iboga '
                                         'altogether, iboga microdoses too', 'it takes the same danger to '
                                         'psychedelics', 'psychedelics act on serotonin too'),
                  "Ayahuasca's MAO-A": ('they know why those two get the stricter rule', 'it gives the reason for the '
                                        'rule\'s second half', "Ayahuasca's MAO-A inhibition")},
                 p['opens'], [c for c in p['checked'] if not c[0].startswith(('MAO-A breaks', 'noribogaine'))],
                 [(1, '3; 4, 7'), (2, '1; 10'), (3, '1, 4'), (4, '5; 1; 4; 13')],
                 [(1, 'CAN\'T TELL: stronger or weaker'), (3, 'CAN\'T TELL: my antidepressant\'s class'),
                  (4, 'CAN\'T TELL: how many days; do microdoses count')],
                 p['same'], p['place'],
                 his_kept={3: POST + 'every compound stays as it went in. Said in groups with what each is ("the '
                              'antibiotic linezolid", "the cough suppressant DXM"), it read AI Medium and Low in the '
                              'check of version 4, and the groups are a question for him'},
                 fit_kept={3: 'the list names classes as the post does; which brand is in which class is his to add, '
                              'or a pharmacist\'s to say (a question for him)'})
    # the two pairs, with the paragraphs as they now stand
    for (k1, k2, name, link) in (('iso', 'rule', 'PAIR-ISO-RULE6', 'none: a new paragraph, the rule the one before it '
                                                                   'points to'),
                                 ('cog', 'proj', 'PAIR-COG-PROJ6', "You'll also feel")):
        r1 = B.json.loads(((OUT if k1 == 'iso' else HERE / 'v4') / (k1.upper() + ('6' if k1 == 'iso' else '4') + '.receipt.json')).read_text('utf-8'))
        r2 = B.json.loads(((OUT if k2 == 'proj' else HERE / 'v4') / (k2.upper() + ('6' if k2 == 'proj' else '4') + '.receipt.json')).read_text('utf-8'))
        text = T.plain(V[k1]) + '\n\n' + T.plain(V[k2])
        r = S.make(text, r1['section'] + '; ' + r2['section'], r2['reader'])
        both = {x['s']: x for x in r1['sentences'] + r2['sentences']}
        for n, x in enumerate(r['sentences']):
            src = both[x['s']]
            x['payoff'], x['follows'] = src['payoff'], src['follows']
            if 'link' in x:
                x['link'] = src.get('link') or link
        r['opens'] = {'first_sentence': r['sentences'][0]['s'], 'why_reading': r1['opens']['why_reading']}
        r['checked'] = r1['checked'] + r2['checked']
        for f in ('needed', 'his_fixes', 'fit'):
            a, b = r1[f], r2[f]
            r[f] = {'reader': a['reader'] + '; ' + b['reader'],
                    ('unneeded' if f == 'needed' else 'marked'): a.get('unneeded', a.get('marked', [])) +
                    b.get('unneeded', b.get('marked', [])), 'kept': dict(a['kept'], **b['kept'])}
        r['same_point'], r['placement'] = r1['same_point'] + ' / ' + r2['same_point'], r1['placement'] + ' / ' + r2['placement']
        r['questions'] = r1['questions']
        (OUT / (name + '.receipt.json')).write_text(B.json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        (OUT / (name + '.txt')).write_text(text + '\n', encoding='utf-8')
        bad += ['%s: %s' % (name, x) for x in S.check(text, r)]
    print('\n'.join(bad) or 'receipts: PASS')


if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    main()
