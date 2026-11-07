#!/usr/bin/env python3
"""Section B's humanizing pass, 7 November, once the science was settled (his answers of 13:10 and 13:49 UTC).

Each paragraph is the approved science, rewritten the way his own fixes work (SKILL.md, "Writing for Pangram"; lessons
neuro-2026-11-06b to f and 2026-11-07b): the payoff first in every sentence, each term explained inside the sentence
that first uses it, short sentences joined, people as the actors in active voice, "so" or "since" where the link is
cause, the plain word kept, and a conversational opener where the sentence would otherwise start formally.

  python3 articles/neuro-de-armoring/humanize/fix-20261107/hum/drafts_hum.py
Writes <name>.txt, <name>.receipt.json, PAIR-040-041.*, ITEMS.json and CANDIDATE.md here.
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as R  # noqa: E402
import suggestion_review as sr  # noqa: E402

ART = ROOT / 'articles/neuro-de-armoring/humanize/HUMANIZED-SO-FAR.md'
SATTLER = 'https://link.springer.com/article/10.1385/MN:24:1-3:107'
WILSON = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4721288'
BOYLE = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3670432'
WANG = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12520249/'
ALLEN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10840383/'
WOLOSKER = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC23961'
MATAIX = 'https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2599177'
SMITS = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3747985'
MORAN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1413952'
JALALI = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6333211'
AMICO = 'https://pubmed.ncbi.nlm.nih.gov/21504727/'

SECTION = 'B. The "Overheating" CPU: Glutamate Excitotoxicity'
READER = ('someone with trauma or in withdrawal who is anxious, wired, ruminating or raging, wanting to know what is '
          'going on in their brain and which of the protocol\'s tools does what')
SAME_B = ('none: read section B from its heading to section C for the glutamate mechanism, GluD, D-serine and the '
          'fixes; each point here is made once in the section')

D = [
    dict(name='B037h', starts='The Mechanism:',
         text=('The Mechanism: When glutamate floods in, it jams open the NMDA receptors, the doors glutamate opens on '
               'a brain cell, like a key stuck in the "On" position, and calcium pours in through them. Calcium that '
               'high kills the cell only in extremes, a stroke or a brain injury, and that killing is what '
               '"excitotoxicity" means ([Sattler & Tymianski, 2001](%s)), so a storm doesn\'t mean your neurons are '
               'dying. What you feel comes from where the glutamate lands, and under stress it rises in the amygdala, '
               'the part that flags threats ([Wilson, 2015](%s)), so an amygdala firing too hard hands you threat: '
               'anxiety, rage, the "itchy brain", and never joy. Block the NMDA receptors there and anxious behaviour '
               'drops in animals ([Boyle, 2013](%s)).' % (SATTLER, WILSON, BOYLE)),
         rows=[('what a glutamate flood does at the receptor, with NMDA receptors named in plain words',
                'it opens the paragraph after the Problem names the flood', None),
               ('that cells die only in extremes, so their own storm isn\'t brain damage',
                'it says what that calcium does when it goes far enough', 'Calcium that high'),
               ('why the storm feels like threat and not like excitement: the circuit it lands in',
                'it answers what the reader actually feels, after what the cells do',
                'What you feel comes from where the glutamate lands'),
               ('that the claim has a test behind it', 'it gives the evidence for the sentence before',
                'the NMDA receptors there')],
         opens='it tells the reader what a glutamate flood does inside their brain cells, which is the state the '
               'section is about',
         checked=[dict(point='excitotoxicity is "literally vibrating cells to death", and the feeling is the '
                             'over-excitement itself',
                       found='the cell dies of calcium overload in extremes (Sattler & Tymianski 2001); the feeling '
                             'follows the circuit, and stress raises glutamate in the amygdala (Wilson 2015), where '
                             'NMDA blockers lower anxious behaviour (Boyle 2013)',
                       still_needed='yes: it is what the reader feels', fate='changed')],
         q={'Q1': 'PASS: each sentence opens on its own subject (the flood, calcium that high, what you feel, the test)',
            'Q4': 'PASS: NMDA receptors as the doors glutamate opens, the amygdala as the part that flags threats, '
                  'excitotoxicity in the sentence that names it',
            'Q6': 'PASS: what happens, when it kills, what it feels like and why, the evidence'}),
    dict(name='B038h', starts='The Signal Dial',
         text=('The Signal Dial (GluD Receptors): So if NMDA is the spark, what sets the level? Well, Johns Hopkins '
               'researchers recently found that GluD receptors, which everyone had taken for scaffolding that helps '
               'build synapses, are channels in their own right, and what opens them is D-serine (one of the tools '
               'below) and GABA, the calming chemical, not glutamate ([Wang, et al, 2025](%s)). Everything measured in '
               'people so far points one way: the channel sticks open and leaks, so the synapse never gets quiet. '
               'That\'s what the mutation behind one inherited ataxia does, and a gene variant that raises the risk of '
               'schizophrenia does it too ([Allen, et al, 2023](%s)). My guess is that an armored state jams the dial '
               'the same way, stuck part-way on, which is what hyper-vigilance would be inside a single synapse: a '
               'floor the signal can\'t drop below. Nobody has tested that in trauma, and someone can, because a drug '
               'that shuts these leaking channels already works in the lab.' % (WANG, ALLEN)),
         rows=[('the question the paragraph answers: what sets the level once NMDA has fired',
                'it follows the NMDA paragraph, which it names as the spark', None),
               ('what GluD receptors turn out to be, and that D-serine, one of the tools below, opens them',
                'it answers the question just asked', 'Well, Johns Hopkins researchers recently found'),
               ('the one pattern measured in people: the channel sticks open and leaks',
                'it moves from what the receptor is to what goes wrong with it', 'Everything measured in people'),
               ('the two cases where that has been seen', 'it names the cases for the pattern just stated',
                "That's what"),
               ('what the armor guess is and why it makes sense: a floor the signal can\'t drop below',
                'it carries the measured pattern over to the armored state', 'jams the dial the same way'),
               ('that it is untested and testable, so they hold it as a guess',
                'it says what the guess still needs', 'Nobody has tested that')],
         opens='it asks the reader\'s own next question after the NMDA paragraph: what sets the level',
         checked=[dict(point='GluD is a master volume knob, jammed High (ataxia, hyper-vigilance) or Low (apathy, '
                             'schizotypy) in an armored state',
                       found='GluD2 is a channel opened by D-serine and GABA (Wang 2025); what is measured in people '
                             'is a channel stuck open, in the ataxia mutation and a schizophrenia-risk GluD1 variant '
                             '(Allen 2023); nothing puts a setting on "Low"',
                       still_needed='yes: D-serine is one of the protocol\'s tools, and the High guess has a '
                                    'mechanism', fate='changed')],
         q={'Q1': 'PASS: the question first, then the finding, the pattern, its cases, the guess and its test',
            'Q4': 'PASS: channels in their own right, GABA as the calming chemical, ataxia as inherited, and the leak '
                  'said as a floor the signal can\'t drop below',
            'Q6': 'PASS: question, what it is, what goes wrong, where that was seen, the guess, what would test it'}),
    dict(name='B039h', starts='D-serine may help',
         text=('D-serine may help therapy rewrite old memories, since it switches on the spot on the NMDA receptor '
               'that this kind of learning runs through ([Wolosker, et al, 1999](%s)), and it may open the GluD '
               'channels as well. The drug actually tested alongside exposure therapy, where you face the feared thing '
               'in small safe doses, is a different one, D-cycloserine (DCS), working on that same spot, and across 21 '
               'trials with over 1,000 patients it gave the therapy a small push ([Mataix-Cols, et al, 2017](%s)). It '
               'doesn\'t erase fear, it strengthens whatever you learn in the session, which is why how the session '
               'ends matters so much: finish with the fear down and a sense of mastery and DCS helps that stick, and '
               'probably D-serine too, but finish overwhelmed and it can cement the fear instead '
               '([Smits, et al, 2013](%s)).' % (WOLOSKER, MATAIX, SMITS)),
         rows=[('why D-serine is in the protocol at all', 'it picks up D-serine from the GluD paragraph before it',
                None),
               ('that the tested drug is a different one, and how much it helped',
                'it says what has actually been tested for what the sentence before proposes', 'a different one'),
               ('what to do with that: end the session with the fear down, because a bad session gets strengthened too',
                'it says how the push works, and what follows for the reader\'s own sessions',
                "It doesn't erase fear")],
         opens='it tells the reader why D-serine is in the protocol: it may help therapy rewrite old memories',
         checked=[dict(point='"The specific drug form studied is D-cycloserine", with evidence as an augmenter',
                       found='DCS is a different drug at the same NMDA spot (Smits 2013); 21 trials, 1,047 patients, '
                             'a small effect (Mataix-Cols 2017); it helped after sessions that ended with low fear',
                       still_needed='yes: it is the evidence for the session rule', fate='changed')],
         q={'Q1': 'PASS: each sentence opens on its point (D-serine may help, the tested drug, what it does)',
            'Q4': 'PASS: exposure therapy explained where it is first used; the NMDA spot carried from the paragraphs '
                  'before',
            'Q6': 'PASS: the proposal, the evidence, what it means for a session'}),
    dict(name='B040h', starts='The Fix ("Lock',
         text=('The Fix ("Lock, Stock, and Barrel"):The Brake (NAC): NAC hands the brain\'s support cells cystine, an '
               'amino acid they swap out for glutamate, and in rats that glutamate sitting outside the synapse trips a '
               'brake, the mGluR2/3 receptors, which cut how much glutamate gets fired in '
               '([Moran, et al, 2005](%s)).' % MORAN),
         rows=[('how NAC turns glutamate release down, step by step', 'it opens the Fix list, under its label', None)],
         opens='it tells the reader what NAC does for them: it cuts how much glutamate is fired into the synapse',
         same='none: read the Fix list from its heading to section C for what each tool does; NAC appears once in it',
         checked=[dict(point='NAC "clears the flood by exchanging glutamate for cystine" (the Vacuum)',
                       found='the swap raises glutamate outside the synapse, which trips mGluR2/3 and cuts release '
                             'into it (Moran 2005, rats)',
                       still_needed='yes: it is the first fix', fate='changed')],
         q={'Q1': 'PASS: the label says what it is, then the sentence says how, in order',
            'Q4': 'PASS: cystine as an amino acid, mGluR2/3 named as the brake, support cells for glia',
            'Q6': 'PASS: the swap, what it trips, what that cuts'}),
    dict(name='B041h', starts='The Lock (Zinc',
         text=('The Lock (Zinc/Magnesium): Magnesium sits in the NMDA channel and plugs it while the cell is resting '
               '([Jalali-Yazdi, et al, 2018](%s)), and zinc mostly makes the channel open less often, with a weaker '
               'plug of its own ([Amico-Ruvio, et al, 2011](%s)), so less of the voltage gets through either way.'
               % (JALALI, AMICO)),
         rows=[('what magnesium and zinc each do at the receptor they are taking them for',
                'it follows NAC in the Fix list', None)],
         opens='it tells the reader what the two minerals in the Lock actually do',
         same='none: read the Fix list from its heading to section C for what each tool does; the Lock appears once',
         checked=[dict(point='zinc and magnesium "physically block the receptor channel to stop the voltage"',
                       found='magnesium plugs the pore, a block voltage lifts (Jalali-Yazdi 2018); zinc mainly '
                             'inhibits at GluN2A, with a weaker pore block (Amico-Ruvio 2011)',
                       still_needed='yes', fate='changed')],
         q={'Q1': 'PASS: the sentence opens on magnesium, the one that plugs',
            'Q4': 'PASS: the NMDA channel carried from the paragraphs before; no new term',
            'Q6': 'PASS: magnesium first because it plugs, then zinc, which mostly does less'}),
    dict(name='B042h', starts='The Repair (L-Serine)',
         text=('The Repair (L-Serine): Your brain makes D-Serine out of L-Serine ([Wolosker, et al, 1999](%s)), so '
               'taking L-Serine feeds the NMDA spot, and maybe the GluD channels too, that D-serine switches on, which '
               'is what helps a session that ends with low fear and some mastery stick. The conversion isn\'t very '
               'efficient though, so some people take D-serine itself instead (more risk, but also more benefit).'
               % WOLOSKER),
         rows=[('why L-Serine is in the protocol, and what taking it feeds',
                'it follows the Lock in the Fix list', None),
               ('that the conversion is weak, so some take D-serine itself, with more risk',
                'it qualifies the sentence before', 'The conversion')],
         opens='it tells the reader why L-Serine is in the protocol: their brain makes D-Serine out of it',
         same='none: read the Fix list from its heading to section C for what each tool does; the Repair appears once',
         checked=[dict(point='L-Serine recalibrates the GluD "Volume Dial", and leucine tunes synaptic gain',
                       found='L-serine is made into D-serine (Wolosker 1999); there is no volume dial (Wang 2025); '
                             'nothing supports leucine here, and he cut it',
                       still_needed='yes for L-serine; no for leucine', fate='changed')],
         q={'Q1': 'PASS: each sentence opens on its point (your brain makes it, the conversion)',
            'Q4': 'PASS: the NMDA spot and GluD channels carried from the paragraphs before',
            'Q6': 'PASS: what it does, then its limit'}),
]
PASS_ALL = {
    'Q2': 'N/A: no instruction in this paragraph; it explains a mechanism',
    'Q3': 'PASS: each thing is named exactly (NMDA receptors, calcium, the amygdala, GluD channels, cystine, zinc)',
    'Q5': 'PASS: each "so", "and" and "since" turns on the clause before it',
    'Q7': 'PASS: each fact is about the chemistry the reader is about to change with the protocol',
    'Q8': 'N/A: no group or list inside this paragraph',
    'Q9': 'PASS: one step a clause, with the small words that carry the relation kept',
}


def plain(t):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t))


def receipt(d, text, block):
    r = R.make(text, SECTION, READER)
    assert len(r['sentences']) == len(d['rows']), (d['name'], [x['s'][:50] for x in r['sentences']])
    for x, (pay, fol, link) in zip(r['sentences'], d['rows']):
        x['payoff'], x['follows'] = 'they learn ' + pay, fol
        if 'link' in x:
            x['link'] = link if link else 'none: it opens on its own subject, the next tool in the list'
    r['placement'] = ('where the block is now (block %d of section B); its place in the section is unchanged' % block)
    r['opens']['why_reading'] = d['opens']
    r['same_point'] = d.get('same', SAME_B)
    r['checked'] = d['checked']
    q = dict(PASS_ALL)
    q.update(d['q'])
    r['questions'] = q
    return r


def main():
    md = ART.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    items, bad = [], 0
    for d in D:
        text = plain(d['text'])
        (i,) = [k for k, b in enumerate(raw) if b.startswith(d['starts'])]
        (block,) = [b['i'] for b in bl if b['text'].startswith(d['starts'])]
        r = receipt(d, text, block)
        probs = R.check(text, r)
        (HERE / (d['name'] + '.txt')).write_text(text + '\n', encoding='utf-8')
        (HERE / (d['name'] + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n',
                                                          encoding='utf-8')
        print(d['name'], 'block', block, len(text.split()), 'words',
              'receipt ' + ('PASS' if not probs else 'PROBLEMS'))
        for p in probs:
            print('   ', p)
        bad += bool(probs)
        raw[i] = d['text']
        if len(text.split()) >= 50:
            items.append([d['name'], text, hashlib.sha256(text.encode('utf-8')).hexdigest()])
    # blocks 40 and 41 are short, so the pair is what Pangram reads (one is 47 words)
    pair = '\n\n'.join(plain(x['text']) for x in D if x['name'] in ('B040h', 'B041h'))
    (HERE / 'PAIR-040-041.txt').write_text(pair + '\n', encoding='utf-8')
    comps = [json.loads((HERE / (n + '.receipt.json')).read_text(encoding='utf-8')) for n in ('B040h', 'B041h')]
    lut = {x['s']: x for c in comps for x in c['sentences']}
    rp = R.make(pair, SECTION, READER)
    for x in rp['sentences']:
        src = lut[x['s']]
        x['payoff'], x['follows'] = src['payoff'], src['follows']
        if 'link' in x:
            x['link'] = src.get('link') or 'none: the next tool in the list, which opens on its own subject'
    rp['placement'] = '; '.join(c['placement'] for c in comps)
    rp['opens']['why_reading'] = comps[0]['opens']['why_reading']
    rp['same_point'] = comps[0]['same_point']
    rp['checked'] = comps[0]['checked'] + comps[1]['checked']
    rp['questions'] = comps[0]['questions']
    (HERE / 'PAIR-040-041.receipt.json').write_text(json.dumps(rp, ensure_ascii=False, indent=1) + '\n',
                                                    encoding='utf-8')
    probs = R.check(pair, rp)
    print('PAIR-040-041', len(pair.split()), 'words', 'receipt ' + ('PASS' if not probs else str(probs)))
    bad += bool(probs)
    items.append(['PAIR-040-041', pair, hashlib.sha256(pair.encode('utf-8')).hexdigest()])
    (HERE / 'ITEMS.json').write_text(json.dumps(items, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / 'CANDIDATE.md').write_text('\n\n'.join(raw) + '\n', encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                         str(ROOT / 'articles/neuro-de-armoring/humanize/FIDELITY-KEYS.json'),
                         str(HERE / 'CANDIDATE.md')], capture_output=True, text=True)
    print('fidelity on the candidate:', fk.stdout.strip().splitlines()[-1] if fk.stdout.strip() else fk.stderr[-200:])
    print('items to check:', [x[0] for x in items])
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
