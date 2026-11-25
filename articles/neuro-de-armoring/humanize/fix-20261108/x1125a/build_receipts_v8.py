"""The receipts for x1125a's third batch (texts_x1125a.V8): the Isolation Trap and the Agmatine Warning's first
paragraph after their tell panels (panel-iso, panel-agm, and panel-iso8, panel-agm8 on the first version 8), the 5-HTP
warning's next small step from version 7, and the Cognitive Warning's first paragraph with its neighbour (version 7's,
which is in the article at Human High by itself). The reads are the ones each paragraph had: version 5's fresh reads
for the two rewritten ones (v5/needed, v5/his-fixes, v5/fit), version 2's for the small steps. Every sentence a read
marked is changed, or kept with why.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/build_receipts_v8.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_receipts_v6 as M  # noqa: E402

R, T, B, S = M.R, M.T, M.B, M.S
OUT = HERE / 'v8'
OUT.mkdir(exist_ok=True)
B.HERE = OUT
M.OUT = OUT


def main():
    R.REGISTER_ONLY = True
    for k in R.ALL:
        R.ALL[k]()
    V = T.V8
    bad = []
    p = M.P('iso')
    bad += M.build('iso', 'v5', T.plain(V['iso']), p['where'], p['who'],
                   {'Behavioral Warning': ('they learn what the protocol has them cut and the trap in it: the easiest '
                                           'way to cut it is to hole up alone', 'the next warning, the first about '
                                           'behavior', None),
                    'But do not isolate': ('they don\'t cut people off altogether, and know why: isolation spikes '
                                           'cortisol, which locks the armor in place, addiction or not', 'it gives the '
                                           'don\'t and its reason, against the temptation just named', 'But'),
                    'You still need': ('they keep people around them, the calm kind of company, which the rule in the '
                                       'next paragraph spells out', 'it gives what to do in place of isolating',
                                       'You still need')},
                   'they learn what the protocol asks them to give up and the trap in it, which the warning is about',
                   [], [(1, '19'), (2, '9; 4'), (3, '16')], [(2, 'FROM: addiction')], p['same'], p['place'],
                   name='ISO8')
    p = M.P('agm')
    bad += M.build('agm', 'v5', T.plain(V['agm']), p['where'], p['who'],
                   {'Agmatine Warning': ('they learn agmatine is optional, and that being sold as a supplement doesn\'t '
                                         'make it a nutrient: it is a neuromodulator, in the protocol as a brake on '
                                         'NMDA/glutamate signaling', 'the next warning, the first of three paragraphs '
                                         'on agmatine', None),
                    'It can interact': ('they learn it can interact with far more medications than a nutrient like '
                                        'magnesium would, and why (it acts on three other systems too), and read the '
                                        'precautions that follow with that in mind', 'it says what follows from what '
                                        'agmatine is', 'It can interact')},
                   p['opens'],
                   [('agmatine brakes NMDA activity', 'the article\'s own Shield section: "agmatine partially brakes '
                     'NMDA activity", "a state-dependent brake"; ' + M.SRC.get('agmatine', 'Li et al. 1994; '
                     'https://pmc.ncbi.nlm.nih.gov/articles/PMC1573177'), 'yes: they see why it is in the protocol',
                     'kept')],
                   [(1, '2'), (2, '1')], [(2, 'MISREAD: sounds as if agmatine acts like an opioid')],
                   p['same'], p['place'], name='AGM8')
    # the two small steps: version 4's parts and reads (build_receipts_x1125a.py), as version 7's receipts used them
    T.V4 = dict(T.V4, htp=V['htp'], cog=V['cog'], proj=T.V7['proj'])
    p = R.PARTS['htp']
    remap = {'In practice they': ('But they can', 'But'), "That's because": ("Ayahuasca's harmalas are",
                                                                            "Ayahuasca's harmalas are MAOIs themselves")}
    p['spec'] = {(remap[k][0] if k in remap else k): ((v[0], v[1], remap[k][1]) if k in remap else v)
                 for k, v in p['spec'].items()}
    p['checked'] = p['checked'] + [
        ('ayahuasca\'s harmalas are MAOIs', 'harmine and harmaline are reversible inhibitors of MAO-A ('
         + M.SRC['mao-a'] + '); the article\'s own 5-HTP section: "ayahuasca\'s harmala MAOI chemistry"',
         'yes: they see ayahuasca is already on the list above, under MAOIs', 'kept'),
        ('serotonin syndrome usually comes from mixing', 'his own sentence in the 5-HTP section: "Serotonin syndrome '
         'usually comes from mixing 5-HTP casually with anything else that raises serotonin"', 'yes: they know the danger '
         'is in the mixing, so they check what else they take', 'kept')]
    R.REGISTER_ONLY = False
    bad += R._build('HTP8', T.plain(T.V4['htp']), ['htp'], {})
    p = R.PARTS['proj']
    p['spec'] = {("So during this protocol" if k == 'So the rule' else k): ((v[0], v[1], 'So during this protocol') if
                                                                             k == 'So the rule' else v)
                 for k, v in p['spec'].items()}
    text = T.plain(T.V4['cog']) + '\n\n' + T.plain(T.V4['proj'])
    bad += R._build('PAIR-COG-PROJ8', text, ['cog', 'proj'], {'proj': 'Your armored brain also'})
    print('\n'.join(bad) or 'receipts: PASS')


if __name__ == '__main__':
    main()
