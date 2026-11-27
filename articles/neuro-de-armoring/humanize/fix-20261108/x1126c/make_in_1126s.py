"""IN.json for batch x1126s: try 2 of the two folds that read below High by themselves (checks-1126r), and the stretch
from The Rule to the agmatine warning with its folds, which read AI with labels (90%) and without them (28%)."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
R = HERE / 'receipts'
ISO1 = 'https://www.pangram.com/history/1b56b276-2c25-4f76-893c-26049942c2b8'
PREC1 = 'https://www.pangram.com/history/60d582cd-02cb-4328-a574-dc87abe2aacd'
ISO_D = ('the fold read Human Written by itself (%s) with two Medium windows: its third sentence, where the fold put his '
         'nickname ("But don\'t fall into the isolation trap of cutting yourself off completely, because ..."), and his '
         'last ("Good friends are ultimately more vital ..."), which read High inside one window before the fold. ' % ISO1)
PREC_D = ('the fold read Human Written by itself (%s) with a Low window over his last two sentences ("Not recommended for '
          'use in pregnancy or breast-feeding. Use with extreme caution in those with ..."): once the label is gone they '
          'have no subject, a run of fragments. ' % PREC1)
DEC = ('whether this try goes in; the near-miss rule takes the next try from the better of the two, a word or two a reader '
       'could take two ways')
ITEMS = {
    'iso-f2a': dict(lineage='W-ISO-his', receipt='ISO-F2A', chance=0.65, name='Behavioral Warning, try 2: his own third '
                    'sentence back, his nickname in brackets after its don\'t', diag=ISO_D + 'This try puts his own '
                    'third sentence back ("But don\'t isolate completely, because ...") with "(the isolation trap)" after '
                    'its don\'t, as his label had it in brackets.',
                    ff='payoff: the don\'t leads the third sentence as his card had it, the nickname right after it; join: '
                       'none, his sentences stay as they were; plain: his own "isolate completely" back in place of my '
                       '"fall into the isolation trap of cutting yourself off completely"',
                    tells='"Good friends are ultimately more vital than any brain repair protocol" (a wise-sounding '
                          'end; his, unchanged)',
                    human='his own card version: "But don\'t isolate completely, because that actually spikes cortisol"'),
    'iso-f2b': dict(lineage='W-ISO-his', receipt='ISO-F2B', chance=0.6, name='Behavioral Warning, try 2: the isolation '
                    'trap said as what it is', diag=ISO_D + 'This try says what the trap is ("But the isolation trap is '
                    'cutting yourself off completely, which actually spikes cortisol").',
                    ff='payoff: the third sentence says what the isolation trap is first, then why it harms; join: none; '
                       'plain: "fall into the isolation trap of" became "the isolation trap is"',
                    tells='"Good friends are ultimately more vital than any brain repair protocol" (a wise-sounding '
                          'end; his, unchanged)',
                    human='his own card version: "The easiest way for most folks to take a break from that is to hole up '
                          'alone"'),
    'prec-f2a': dict(lineage='W015-his', receipt='PREC-F2A', chance=0.6, name='Precautions, try 2: its last two sentences '
                     'given their subject ("It\'s", "it")', diag=PREC_D + 'This try gives them their subject ("It\'s not '
                     'recommended ...", "Use it with extreme caution ...").',
                     ff='payoff: the last two sentences say whose precautions they are, agmatine\'s ("It\'s", "it"); join: '
                        'none; plain: none, his words stay',
                     tells='"Use it with extreme caution in those with" (supplement-label wording)',
                     human='his own paragraph: "without having a physician competent to consider the likelihoods of '
                           'problematic interactions"'),
    'prec-f2b': dict(lineage='W015-his', receipt='PREC-F2B', chance=0.6, name='Precautions, try 2: its last two sentences '
                     'joined, with their subject', diag=PREC_D + 'This try joins them, with their subject ("It\'s not '
                     'recommended ..., and calls for extreme caution in those with ...").',
                     ff='payoff: the last sentence says whose precautions they are, agmatine\'s ("It\'s"); join: his two '
                        'short sentences joined, as his fixes join short sentences that carry one thought; plain: "Use '
                        'with extreme caution in" became "calls for extreme caution in"',
                     tells='"calls for extreme caution in those with" (supplement-label wording)',
                     human='his own paragraph: "without having a physician competent to consider the likelihoods of '
                           'problematic interactions"'),
    'rule-f2a': dict(lineage='W-RULE', receipt='RULE-F2A', chance=0.7, name='The Rule, folded, its second sentence '
                     'opening on what brings "Exciting Love"',
                     diag='the fold read Human High by itself '
                          '(https://www.pangram.com/history/4c06658e-a4ce-4452-95b2-0e8fdce2b992), but in the stretch '
                          'with the labels off its second sentence read AI High '
                          '(https://www.pangram.com/history/b9f4952c-eb3b-456d-a757-9b9ed17a259f): "The other kind, '
                          '\'Exciting Love\', is the rush of ...", a definition built like the one before it. 72a asks me '
                          'to fix that opening; this try says what brings it first ("A new romance or high-stakes drama '
                          'gives you the rush of \'Exciting Love\'"). The stretch has used its two tries, so the section\'s '
                          'last check is where this is seen in its place.',
                     ff='payoff: the second sentence leads with what brings Exciting Love (a new romance or drama), then '
                        'what it does; join: none, it was one sentence and stays one; plain: "The other kind, ... is the '
                        'rush of" became "gives you the rush of"',
                     tells='"meaning parallel play" (a gloss after a coined name)',
                     human='his post\'s names "Boring Love" and "Exciting Love"',
                     decides='whether this goes in before the section\'s last check; below High, the fold stays as it '
                             'read High by itself'),
    'agm-f2a': dict(lineage='W-AGMINTRO-his', receipt='AGM-F2A', chance=0.65, name='Agmatine warning, folded, its opening '
                    'tied to the herbs the protocol leaves out',
                    diag='the fold read Human High by itself '
                         '(https://www.pangram.com/history/4da98590-43d7-4e90-99ec-488c28a02a4c), but in the stretch with '
                         'the labels off its opening read AI Medium '
                         '(https://www.pangram.com/history/b9f4952c-eb3b-456d-a757-9b9ed17a259f), a new topic straight '
                         'after the two herbs I advise against. 72a asks me to fix that opening; this try ties it to them '
                         'with one word, as the near-miss rule takes from his version ("which is why we do use it in this '
                         'protocol").',
                    ff='payoff: the first sentence says what agmatine does, then that this one the protocol does use, '
                       'against the herbs before it; join: none; plain: none, his words stay but for the one word',
                    tells='"which is why we do use it in this protocol" (an emphatic do)',
                    human='his own card version: "People may think it\'s pretty safe, since it\'s a common health '
                          'supplement"',
                    decides='whether this goes in before the section\'s last check; below High, the fold stays as it read '
                            'High by itself'),
}
out = {}
for k, v in ITEMS.items():
    t = (R / (v['receipt'] + '.txt')).read_text(encoding='utf-8').rstrip('\n')
    d = {'lineage': 'neuro-de-armoring/' + v['lineage'], 'scope': v.get('scope', 'paragraph'), 'name': v['name'],
         'text': t, 'chance': v['chance'], 'receipt': str(R / (v['receipt'] + '.receipt.json')), 'diagnosis': v['diag'],
         'decides': v.get('decides', DEC), 'first_fix': v['ff'], 'tells': v['tells'], 'human_tells': v['human'],
         'humanized': 'the label folded into the first sentence (72a) and, in try 2, the window below High worked a word '
                      'or two at a time; every other word is as it read Human High'}
    if v.get('narrowed'):
        d['narrowed'] = v['narrowed']
    out[k] = d
(HERE / 'checks-1126s' / 'IN.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(out), 'items')
