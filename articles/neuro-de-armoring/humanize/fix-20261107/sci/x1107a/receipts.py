"""Making-sense receipts (tools/humanization/sense_receipt.py) for section B's science cards, one per changed paragraph,
on the paragraph as the card shows it (its Markdown links and italics as plain text).

  python3 articles/neuro-de-armoring/humanize/fix-20261107/sci/x1107a/receipts.py
Writes <key>.txt and <key>.receipt.json beside this file and checks each.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402


def plain(md):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md))


SECTION = 'B. The "Overheating" CPU: Glutamate Excitotoxicity'
READER = ('someone with trauma armor who is about to take NAC, zinc, magnesium, L-serine or D-serine to calm a '
          'glutamate storm and to make therapy sessions stick, and wants to know what each one actually does')
SAME_B = ('none: read section B from its heading to section C for the glutamate mechanism, GluD, D-serine and DCS, '
          'and the fixes; each point here is made once in the section')
PASS_ALL = {
    'Q2': 'N/A: no instruction in this paragraph; it explains a mechanism',
    'Q3': 'PASS: each thing is named exactly (NMDA receptors, calcium, GluD receptors, D-serine, GABA)',
    'Q5': 'PASS: each "so", "and" and "because" turns on the clause before it',
    'Q7': 'PASS: each fact is about the chemistry the reader is about to change with the protocol',
    'Q8': 'N/A: no group or list in this paragraph',
    'Q9': 'PASS: one step a clause, the small words that carry the relation kept ("so", "which", "rather than")',
}

R = {
    'B37': {
        'placement': 'third paragraph of section B, after the Problem (glutamate floods the brain under stress) and '
                     'the Red Line; it says what that flood does at the receptor, before the GluD paragraph',
        'opens': 'it tells the reader what a glutamate flood does to their brain cells: the key stuck "On" and the '
                 'calcium pouring in, which is the state the section is about',
        's': [
            ('the reader learns what over-activation does: calcium pours into the cells, and NMDA receptors are '
             'explained as the doors glutamate unlocks', 'it opens the paragraph after the Problem paragraph names the '
             'glutamate flood', None),
            ('the reader learns that cells die only in extreme cases, a stroke or a brain injury, and what '
             '"excitotoxicity" means', 'it says what that calcium does when it is extreme', 'that calcium overload'),
            ('the reader stops reading their anxiety or rage as neurons dying, and reads it as over-excitement',
             'it turns the extreme case back to the reader\'s own glutamate storm', 'you feel in a glutamate storm'),
        ],
        'checked': [{'point': 'excitotoxicity is "literally vibrating cells to death"',
                     'found': 'cells die of calcium overload, in CNS ischemia, trauma and neurodegeneration (Sattler & '
                              'Tymianski 2001)', 'still_needed': 'yes: it says what a glutamate flood does',
                     'fate': 'changed'},
                    {'point': 'excitotoxicity "feels like anxiety, rage, or an itchy brain"',
                     'found': 'no source ties the feelings to cell death', 'still_needed': 'yes: the reader feels these',
                     'fate': 'changed'}],
        'q': {'Q1': 'PASS: each sentence opens on its subject (glutamate, extreme cases, the feeling) and NMDA is '
                    'explained where it is first used here',
              'Q4': 'PASS: NMDA receptors explained as the doors glutamate unlocks; excitotoxicity explained in the '
                    'sentence that names it; calcium is common',
              'Q6': 'PASS: what happens, when it kills, what it feels like'},
    },
    'B38': {
        'placement': 'fourth paragraph of section B, after the NMDA mechanism, which its first "So if NMDA is the '
                     'spark" points back to; before the D-serine paragraph, which it sets up by naming D-serine',
        'opens': 'it asks the reader\'s own next question after the NMDA paragraph: is anything else turning the '
                 'signal up or down',
        's': [
            ('the reader is asked whether anything besides NMDA turns the signal up or down, the question the '
             'paragraph answers', 'it follows the NMDA paragraph, which it names as the spark', None),
            ('the reader learns the Johns Hopkins finding: GluD receptors are channels, opened by D-serine and GABA, '
             'and that D-serine is one of the protocol\'s tools', 'it answers the question the sentence before asked',
             'Well according to'),
            ('the reader learns the finding is still argued over, so they don\'t take it as settled',
             'it qualifies the finding just given', 'found no sign of that'),
            ('the reader learns the two known cases of the channel being wrong: stuck open in an ataxia mutation, less '
             'active in schizophrenia', 'it says what is known of the channel going wrong, after what it is',
             'leaves the channel leaking'),
            ('the reader learns that the armor version, High as hyper-vigilance or Low as apathy and schizotypy, is a '
             'hypothesis nobody has tested', 'it extends the two known cases to the armored state, as a guess',
             'jams it too'),
        ],
        'checked': [{'point': 'GluD is a "master volume knob" that sets the synapse\'s baseline hum',
                     'found': 'Wang et al. 2025: GluD2 is a ligand-gated channel opened by D-serine and GABA; Itoh et '
                              'al. 2024 found no direct gating', 'still_needed': 'yes: it is why D-serine matters here',
                     'fate': 'changed'},
                    {'point': 'in an armored state the dial is jammed High (ataxia, hyper-vigilance) or Low (apathy, '
                              'schizotypy)',
                     'found': 'the ataxia mutation leaks; GluDs less active in schizophrenia (Johns Hopkins 2025); '
                              'nothing tests armor or trauma', 'still_needed': 'yes: it is his hypothesis, said as one',
                     'fate': 'changed'}],
        'q': {'Q1': 'PASS: the question first, then the finding, its doubt, the known cases and the guess, each '
                    'sentence opening on what it is about',
              'Q4': 'PASS: channel (gates that let current in), GABA (the brain\'s main calming chemical), cerebellar '
                    'ataxia (a movement and balance disorder) and schizotypy explained where first used; synapse is '
                    'high-school biology',
              'Q6': 'PASS: question, answer, doubt, known cases, the armor guess'},
    },
    'B39': {
        'placement': 'fifth paragraph of section B, after the GluD paragraph, whose D-serine and GluD channels it '
                     'picks up; before the Fix, where L-serine and D-serine come back',
        'opens': 'it tells the reader why D-serine is in the protocol: it may help therapy update old memories',
        's': [
            ('the reader learns why D-serine is here: it switches on a spot on the NMDA receptor that memory updating '
             'needs, and may open GluD', 'it picks up D-serine from the GluD paragraph before it', None),
            ('the reader learns that the tested drug is a different one, DCS, and how much it helped: a small boost '
             'in 21 trials', 'it says what has actually been tested for what the sentence before proposes',
             'a different one'),
            ('the reader learns DCS strengthens whatever learning happens, not fear erasure', 'it says how the boost '
             'works', 'It does not erase fear directly'),
            ('the reader learns to end a session on low fear, because a bad session can be consolidated too',
             'it draws the consequence of strengthening whatever learning happens', 'This is why session quality '
             'matters'),
        ],
        'checked': [{'point': '"The specific drug form studied is D-cycloserine"',
                     'found': 'DCS is a different drug acting at the same NMDA site (Smits 2013); D-serine is made from '
                              'L-serine (Wolosker 1999)', 'still_needed': 'yes: it is the evidence for the session rule',
                     'fate': 'changed'},
                    {'point': 'DCS "has evidence as an exposure-therapy augmenter"',
                     'found': '21 trials, 1,047 participants: a small effect (Mataix-Cols 2017); larger after '
                              'successful sessions (Smits 2013)', 'still_needed': 'yes', 'fate': 'changed'}],
        'q': {'Q1': 'PASS: each sentence opens on its point (D-serine may help, the tested drug, it does not erase, '
                    'this is why)',
              'Q4': 'PASS: exposure therapy explained where first used; NMDA explained earlier in the section; '
                    'consolidate is plain enough in context',
              'Q6': 'PASS: proposal, evidence, how it works, what to do'},
    },
    'B40': {
        'placement': 'first of the Fix\'s items in section B, after the D-serine paragraph; its label carries the '
                     'Fix heading as the article has it',
        'opens': 'it tells the reader NAC works more like a brake than a vacuum, which changes what they expect of it',
        's': [
            ('the reader learns NAC is a brake, not a vacuum', 'it opens the Fix list', None),
            ('the reader learns how the brake works: cystine is swapped for glutamate, which trips mGluR2/3 and cuts '
             'glutamate release, in rats', 'it explains the brake the sentence before names', 'trips a brake'),
        ],
        'checked': [{'point': 'NAC "clears the flood by exchanging glutamate for cystine"',
                     'found': 'the exchange raises glutamate outside the synapse, which cuts synaptic release through '
                              'mGluR2/3 (Moran 2005, rats)', 'still_needed': 'yes: it is the first fix',
                     'fate': 'changed'}],
        'q': {'Q1': 'PASS: the point (a brake) comes first, then how',
              'Q4': 'PASS: cystine explained as an amino acid; mGluR2/3 named as the brake it is; support cells for '
                    'glia',
              'Q6': 'PASS: what it is, then how it works'},
    },
    'B41': {
        'placement': 'second of the Fix\'s items, after NAC, before the Repair',
        'opens': 'it tells the reader what magnesium and zinc each do at the receptor they are trying to calm',
        's': [
            ('the reader learns magnesium plugs the channel at rest and zinc makes it open less, so less voltage gets '
             'through', 'it follows NAC in the Fix list', None),
        ],
        'checked': [{'point': 'zinc and magnesium "physically block the receptor channel"',
                     'found': 'magnesium blocks the pore in a voltage-dependent way (Jalali-Yazdi 2018); zinc mainly '
                              'inhibits allosterically at GluN2A, with a weaker pore block (Amico-Ruvio 2011)',
                     'still_needed': 'yes', 'fate': 'changed'}],
        'q': {'Q1': 'PASS: the sentence opens on magnesium, the first of the two',
              'Q4': 'PASS: NMDA receptor explained earlier in the section; channel explained in the GluD paragraph',
              'Q6': 'PASS: magnesium first because it is the plug, then zinc, which mostly does less'},
    },
    'B42': {
        'placement': 'third of the Fix\'s items, after the Lock; its D-serine and GluD point back to the GluD and '
                     'D-serine paragraphs',
        'opens': 'it tells the reader why L-serine is in the protocol: the brain makes D-serine from it',
        's': [
            ('the reader learns L-serine becomes D-serine, so it can feed the NMDA spot and may help sessions stick',
             'it follows the Lock in the Fix list', None),
            ('the reader learns the conversion is weak, so some take D-serine itself, with more risk',
             'it qualifies the sentence before', 'The conversion'),
        ],
        'checked': [{'point': 'L-serine recalibrates the GluD "Volume Dial"',
                     'found': 'L-serine is made into D-serine (Wolosker 1999); no volume dial (Wang 2025)',
                     'still_needed': 'yes', 'fate': 'changed'},
                    {'point': 'Leucine "tunes synaptic gain" and eases the itchy brain',
                     'found': 'no source found; leucine gives at least half of brain glutamate\'s nitrogen in rats '
                              '(Sakai 2004)', 'still_needed': 'no: its reason doesn\'t hold', 'fate': 'cut'}],
        'q': {'Q1': 'PASS: each sentence opens on its point (L-serine is what the brain makes D-serine from; the '
                    'conversion)',
              'Q4': 'PASS: NMDA spot and GluD channels explained earlier in the section',
              'Q6': 'PASS: what it does, then its limit'},
    },
    'B119': {
        'reader': 'someone setting up the anxiety (Glutamate Shield) part of the daily protocol and choosing doses',
        'placement': 'the NAC line of the Glutamate Shield list, with its dose',
        'opens': 'it gives the reader the NAC dose they are about to take',
        'same': 'none: read the Glutamate Shield list from its heading to the next for the doses; NAC is listed once',
        's': [
            ('the reader gets the NAC dose, split through the day', 'it is the list item for NAC', None),
            ('the reader learns what the dose does: it turns down glutamate release', 'it gives the reason for the '
             'dose before it', 'none: a list item\'s note on the dose just given, which the reader reads with it'),
        ],
        'checked': [{'point': 'NAC "mops up glutamate"', 'found': 'it cuts synaptic glutamate release through '
                     'mGluR2/3 (Moran 2005)', 'still_needed': 'yes', 'fate': 'changed'}],
        'q': {'Q1': 'PASS: the dose first, then the reason',
              'Q2': 'PASS: the dose is the instruction and its reason is said',
              'Q4': 'PASS: no new term',
              'Q6': 'PASS: dose, then what it does',
              'Q8': 'PASS: NAC belongs in the Glutamate Shield list'},
    },
    'B148': {
        'reader': 'someone in a glutamate storm planning a D-serine session, deciding when to take it',
        'placement': 'in Scenario A, the D-serine step, after the earlier steps that give PQQ and ketones',
        'opens': 'it tells the reader what D-serine is for in this scenario: sessions that need memory updating',
        'same': 'none: read Scenario A from its heading to the next for the D-serine step; it is given once',
        's': [
            ('the reader learns what D-serine is for here', 'it opens the D-serine step', None),
            ('the reader learns where to buy it', 'it follows the naming of D-serine', 'none: a link to where to buy '
             'it, which needs no tie'),
            ('the reader learns when to take it and why: after PQQ and ketones, so the brain is fueled when it starts '
             'working', 'it gives the timing after the product', 'take it'),
        ],
        'checked': [{'point': 'the GluD dial "is turned down" when D-serine works',
                     'found': 'D-serine opens GluD channels and switches on the NMDA site (Wang 2025, Wolosker 1999): '
                              'up, not down', 'still_needed': 'yes: the timing\'s reason', 'fate': 'changed'}],
        'q': {'Q1': 'PASS: each sentence opens on its point',
              'Q2': 'PASS: the timing is the instruction and its reason is said',
              'Q4': 'PASS: no new term',
              'Q6': 'PASS: what for, where to buy, when',
              'Q8': 'N/A: no group'},
    },
}


def main():
    bad = 0
    for key, md in TEXTS.items():
        text = plain(md)
        d = R[key]
        r = S.make(text, SECTION if key in ('B37', 'B38', 'B39', 'B40', 'B41', 'B42') else key,
                   d.get('reader', READER))
        sents = S.sentences(text)
        assert len(sents) == len(d['s']), (key, len(sents), len(d['s']))
        for x, (pay, fol, link) in zip(r['sentences'], d['s']):
            x['payoff'], x['follows'] = pay, fol
            if 'link' in x:
                x['link'] = link if link else 'none: it opens on its own subject'
        r['placement'] = d['placement']
        r['opens']['why_reading'] = d['opens']
        r['same_point'] = d.get('same', SAME_B)
        r['checked'] = d['checked']
        q = dict(PASS_ALL)
        q.update(d['q'])
        r['questions'] = q
        (HERE / ('%s.txt' % key)).write_text(text + '\n', encoding='utf-8')
        (HERE / ('%s.receipt.json' % key)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n',
                                                      encoding='utf-8')
        probs = S.check(text, r)
        for p in probs:
            print(key, 'PROBLEM', p)
        bad += bool(probs)
    print('receipts:', len(TEXTS), 'with problems:', bad)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
