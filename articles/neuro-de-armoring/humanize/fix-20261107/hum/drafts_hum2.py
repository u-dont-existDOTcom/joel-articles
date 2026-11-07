#!/usr/bin/env python3
"""Round 2 for blocks 38 and 42, after their tell panels (panel-b038/PANEL.md, panel-b042/PANEL.md).

What the panels agreed on, and what each got:
- B038 S3 and S4, the sweeping "Everything measured in people so far points one way:" and the balanced pair ending
  "does it too": joined and made concrete, the cases first, the verdict gone.
- B038 S5, the colon metaphor "a floor the signal can't drop below" and "which is what hyper-vigilance would be":
  replaced by what the reader would feel ("you never come down to a baseline").
- B038 S6, the "Nobody has tested that ... and someone can, because" pivot: ends on the fact instead.
- B038 S2, the "everyone had taken for scaffolding" reveal: one clause, no reveal.
- B038 S1 is his own question, kept (gate E373).
- B042 S1, the stacked relative clause and the "which is what" payoff: split in two, with "so" for the cause.
- B042 S2 is his own sentence from 6 November, which read Human at High; the panel's calls on it ("more risk, but
  also more benefit", the "though ... so" pivot) are his words and stay.
- Both panels called the rhythm too even, every sentence a finished point: each draft now carries one short sentence.

  python3 articles/neuro-de-armoring/humanize/fix-20261107/hum/drafts_hum2.py
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as R  # noqa: E402
import drafts_hum as H  # noqa: E402

D = [
    dict(name='B038h2', starts='The Signal Dial',
         text=('The Signal Dial (GluD Receptors): So if NMDA is the spark, what sets the level? Well, Johns Hopkins '
               'researchers recently found that GluD receptors, until now just the things that help build synapses, '
               'are channels themselves, and what opens them is D-serine (one of the tools below) and GABA, the '
               'chemical that quiets a cell down, not glutamate ([Wang, et al, 2025](%s)). In people, what turns up is '
               'a leak. The mutation behind one inherited ataxia leaves the channel stuck open, and a gene variant '
               'that raises the risk of schizophrenia does too ([Allen, et al, 2023](%s)), so the synapse never gets '
               'quiet. My guess is that an armored state jams it the same way, stuck part-way on, so you never come '
               'down to a baseline, which from the inside is hyper-vigilance. Nobody has tested that in trauma, so it '
               'stays a guess, though the lab already has a drug that shuts these leaking channels.'
               % (H.WANG, H.ALLEN)),
         rows=[('the question the paragraph answers: what sets the level once NMDA has fired',
                'it follows the NMDA paragraph, which it names as the spark', None),
               ('what GluD receptors turn out to be, and that D-serine, one of the tools below, opens them',
                'it answers the question just asked', 'Well, Johns Hopkins researchers recently found'),
               ('that what goes wrong with these channels in people is a leak',
                'it turns from what the receptor is to what goes wrong with it', 'In people'),
               ('the two cases where the leak has been seen, and what it does to the synapse',
                'it gives the cases for the leak just named', 'The mutation'),
               ('what the armor guess is, and what it would feel like',
                'it carries the leak over to the armored state', 'jams it the same way'),
               ('that it is untested, so they hold it as a guess', 'it says what the guess still needs',
                'Nobody has tested that')],
         opens='it asks the reader\'s own next question after the NMDA paragraph: what sets the level',
         checked=[dict(point='GluD is a master volume knob, jammed High (ataxia, hyper-vigilance) or Low (apathy, '
                             'schizotypy) in an armored state',
                       found='GluD2 is a channel opened by D-serine and GABA (Wang 2025); in people what is measured '
                             'is a channel stuck open, in the ataxia mutation and a schizophrenia-risk GluD1 variant '
                             '(Allen 2023); nothing puts a setting on "Low"',
                       still_needed='yes: D-serine is one of the protocol\'s tools, and the High guess has a '
                                    'mechanism', fate='changed')],
         q={'Q1': 'PASS: the question first, then the finding, the leak, its cases, the guess, what it still needs',
            'Q4': 'PASS: channels themselves, GABA as the chemical that quiets a cell down, ataxia as inherited, and '
                  'the leak said as never coming down to a baseline',
            'Q6': 'PASS: question, what it is, what goes wrong, where that was seen, the guess, what it needs'}),
    dict(name='B042h2', starts='The Repair (L-Serine)',
         text=('The Repair (L-Serine): Your brain makes D-Serine out of L-Serine ([Wolosker, et al, 1999](%s)). So '
               'taking L-Serine feeds the spot D-serine switches on, and maybe the GluD channels too, so a session '
               'that ends with the fear down and a sense of mastery has a better chance of sticking. The conversion '
               'isn\'t very efficient though, so some people take D-serine itself instead (more risk, but also more '
               'benefit).' % H.WOLOSKER),
         rows=[('where D-Serine comes from, which is why L-Serine is in the protocol',
                'it follows the Lock in the Fix list', None),
               ('what taking L-Serine does for their next therapy session',
                'it says what that conversion is good for', 'So taking L-Serine'),
               ('that the conversion is weak, so some take D-serine itself, with more risk',
                'it qualifies the sentence before', 'The conversion')],
         opens='it tells the reader where D-Serine comes from, which is why L-Serine is in the protocol at all',
         same='none: read the Fix list from its heading to section C for what each tool does; the Repair appears once',
         checked=[dict(point='L-Serine recalibrates the GluD "Volume Dial", and leucine tunes synaptic gain',
                       found='L-serine is made into D-serine (Wolosker 1999); there is no volume dial (Wang 2025); '
                             'nothing supports leucine here, and he cut it',
                       still_needed='yes for L-serine; no for leucine', fate='changed')],
         q={'Q1': 'PASS: each sentence opens on its point (where D-Serine comes from, what taking it does, the limit)',
            'Q4': 'PASS: the NMDA spot and GluD channels carried from the paragraphs before',
            'Q6': 'PASS: where it comes from, what it does, its limit'}),
]


def main():
    bad = 0
    items = []
    for d in D:
        text = H.plain(d['text'])
        r = H.receipt(d, text, 38 if d['name'].startswith('B038') else 42)
        probs = R.check(text, r)
        (HERE / (d['name'] + '.txt')).write_text(text + '\n', encoding='utf-8')
        (HERE / (d['name'] + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n',
                                                          encoding='utf-8')
        print(d['name'], len(text.split()), 'words', 'receipt ' + ('PASS' if not probs else 'PROBLEMS'))
        for p in probs:
            print('   ', p)
        bad += bool(probs)
        items.append([d['name'], text, hashlib.sha256(text.encode('utf-8')).hexdigest()])
    old = json.loads((HERE / 'ITEMS.json').read_text(encoding='utf-8'))
    keep = [x for x in old if x[0] in ('B037h', 'B039h', 'PAIR-040-041')]
    (HERE / 'ITEMS.json').write_text(json.dumps(keep + items, ensure_ascii=False) + '\n', encoding='utf-8')
    print('items to check:', [x[0] for x in keep + items])
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
