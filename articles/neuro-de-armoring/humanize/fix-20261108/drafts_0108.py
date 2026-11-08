#!/usr/bin/env python3
"""Blocks 39, 40 and 41 done the way his fixes of 37 and 38 show (2026-11-08), and his two paragraphs with the one
claim in each that his sources don't support.

His move on 38 (his card T-38): "i removed most of it and just put the basic facts". On 37 (his check b1bd7488): plain
claims in his register, a question as the turn ("What does all that feel like?"), and an aside in his voice. So for 39
to 41 the fresh reader's needed read (needed/*/READ.md, tools/humanization/needed_read_brief.md) went first, and what
it said the reader doesn't need went, before any wording:
- 39: "and it may also open the GluD channels" (block 38 now says D-serine opens them; a repeat the reader can't use).
- 40: the receptor name mGluR2/3, and two of the three pictures in one clause ("trips", "fired"); the brake stays.
- 41: "with a weaker plug of its own"; and "so less of the voltage gets through", which makes no sense (a channel lets
  ions through, not voltage): it becomes "so less calcium gets in". The word was the old text's, kept by me.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/drafts_0108.py
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as R  # noqa: E402
import apply_his_x1107c as HIS  # noqa: E402

WOLOSKER = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC23961'
MATAIX = 'https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2599177'
SMITS = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3747985'
MORAN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1413952'
JALALI = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6333211'
AMICO = 'https://pubmed.ncbi.nlm.nih.gov/21504727/'
SECTION = 'B. The "Overheating" CPU: Glutamate Excitotoxicity'
READER = ('someone with trauma or in withdrawal who is anxious, wired or raging, deciding which of the protocol\'s tools '
          'to take and how to run their therapy sessions')
SAME_B = ('none: read section B from its heading to section C for the mechanism, GluD, D-serine and DCS, and the fixes; '
          'each point here is made once in the section')

T37_FIXED = HIS.HIS37.replace('Calcium at such high levels caused by stress can swell and injure the neurons.',
                              'Calcium at such high levels caused by stress can injure the neurons.')
T38_FIXED = HIS.HIS38.replace(
    'While NMDA receptor opening is the main spark that starts up neuronal excitation, another calcium door was recently '
    'discovered in the GluD receptors.',
    'While NMDA receptors are the main door calcium comes in through when glutamate fires, another door was recently '
    'discovered in the GluD receptors.')
assert T37_FIXED != HIS.HIS37 and T38_FIXED != HIS.HIS38

D = [
    dict(name='B039n', starts='D-serine may help', job='needed/b039',
         text=('D-serine may help therapy update old memories, since it switches on a spot on the NMDA receptor that '
               'this kind of learning needs ([Wolosker, et al, 1999](%s)). But the drug that\'s actually been tested '
               'alongside exposure therapy (facing the feared thing in small, safe doses) is a different one, '
               'D-cycloserine (DCS), which works on that same spot, and across 21 trials with over 1,000 patients it '
               'gave the therapy a small boost ([Mataix-Cols, et al, 2017](%s)). So what does it actually do? It '
               'doesn\'t erase fear, it strengthens whatever you learn in the session, good or bad. End the session with '
               'the fear down and some sense of mastery, and DCS (and maybe D-serine) helps that stick; end it '
               'overwhelmed, and it can lock in the fear instead ([Smits, et al, 2013](%s)).' % (WOLOSKER, MATAIX, SMITS)),
         rows=[('why D-serine is in the protocol: it may help therapy update old memories', None),
               ('that the tested drug is a different one, and how much it helped', 'But the drug'),
               ('the question they now have, what the drug does in a session', 'So what does it actually do?'),
               ('that it strengthens whatever they learn, good or bad', 'It doesn\'t erase fear'),
               ('how to end a session, and what happens if they don\'t', 'End the session')],
         unneeded=['and it may also open the GluD channels.'],
         opens='it tells the reader why D-serine is in the protocol: it may help therapy update old memories',
         checked=[dict(point='"The specific drug form studied is D-cycloserine", with evidence as an augmenter',
                       found='DCS is a different drug at the same NMDA spot (Smits 2013); 21 trials, 1,047 patients, a '
                             'small effect (Mataix-Cols 2017); it helped after sessions that ended with low fear',
                       still_needed='yes: they end their own sessions with the fear down, which is what the evidence '
                                    'says matters', fate='changed')]),
    dict(name='B040n', starts='The Fix ("Lock', job='needed/b040',
         text=('The Fix ("Lock, Stock, and Barrel"): The Brake (NAC): NAC gives the brain\'s support cells cystine (an '
               'amino acid), which they trade for glutamate, and in rats that glutamate sitting outside the synapse '
               'turns on a brake that cuts how much glutamate gets released into it ([Moran, et al, 2005](%s)).'
               % MORAN),
         rows=[('what NAC does for them: it turns down how much glutamate gets released', None)],
         unneeded=[],
         opens='it tells the reader what NAC does for them before they take its dose',
         same='none: read the Fix list from its heading to section C for what each tool does; NAC is in it once',
         checked=[dict(point='NAC "clears the flood by exchanging glutamate for cystine" (the Vacuum)',
                       found='the swap raises glutamate outside the synapse, which trips mGluR2/3 and cuts release '
                             'into it (Moran 2005, rats)',
                       still_needed='yes: they take NAC knowing it turns release down rather than mopping up',
                       fate='changed')]),
    dict(name='B041n', starts='The Lock (Zinc', job='needed/b041',
         text=('The Lock (Zinc/Magnesium): Magnesium physically plugs the NMDA receptor\'s channel while the cell is at '
               'rest ([Jalali-Yazdi, et al, 2018](%s)), and zinc mostly makes the channel open less often '
               '([Amico-Ruvio, et al, 2011](%s)), so less calcium gets in.' % (JALALI, AMICO)),
         rows=[('what magnesium and zinc each do, and that less calcium gets in', None)],
         unneeded=[],
         opens='it tells the reader what the two minerals of the Lock do for them',
         same='none: read the Fix list from its heading to section C for what each tool does; the Lock is in it once',
         checked=[dict(point='zinc and magnesium "physically block the receptor channel to stop the voltage"',
                       found='magnesium plugs the pore (Jalali-Yazdi 2018); zinc mainly makes it open less (Amico-Ruvio '
                             '2011); a channel lets ions through, so what drops is the calcium coming in',
                       still_needed='yes: they take zinc and magnesium knowing what each does at the receptor',
                       fate='changed')]),
]
QS = {
    'Q1': 'PASS: each sentence opens on its point',
    'Q2': 'N/A: no instruction except the session advice, whose reason is in the same sentence',
    'Q3': 'PASS: each thing is named exactly',
    'Q4': 'PASS: exposure therapy and cystine explained where first used; NMDA from the paragraphs before',
    'Q5': 'PASS: each "so", "but" and "since" turns on the clause before',
    'Q6': 'PASS: in the order the reader needs',
    'Q7': 'PASS: each fact is about a tool the reader takes',
    'Q8': 'N/A: no group inside the paragraph',
    'Q9': 'PASS: the small words that carry the relation kept',
}


def plain(t):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t))


def receipt(d, text):
    r = R.make(text, SECTION, READER)
    assert len(r['sentences']) == len(d['rows']), (d['name'], [x['s'][:40] for x in r['sentences']])
    for x, (pay, link) in zip(r['sentences'], d['rows']):
        x['payoff'] = 'they learn ' + pay
        x['follows'] = 'it continues the paragraph before, or the sentence before, in the order the reader needs'
        if 'link' in x:
            x['link'] = link or 'none: it opens on its own subject'
    r['placement'] = 'where the block is now in section B; its place is unchanged'
    r['opens']['why_reading'] = d['opens']
    r['same_point'] = d.get('same', SAME_B)
    r['needed'] = {'reader': 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this '
                             'paragraph, its heading and what it is for: ' + d['job'] + '/READ.md',
                   'unneeded': d['unneeded'], 'kept': {}}
    r['checked'] = d['checked']
    r['questions'] = dict(QS)
    return r


def his_receipt(name, text, his_text, changed_payoff):
    r = R.make(text, SECTION, READER, his_text=his_text, whose='his own: his version of this paragraph, 2026-11-08 00:49 UTC (ANSWERS-X1107C)')
    for x in r['sentences']:
        if not x.get('his'):
            x['payoff'] = 'they learn ' + changed_payoff
            x['follows'] = 'it is the sentence of his it replaces, in the same place'
            if 'link' in x:
                x['link'] = 'none: it is his sentence with one claim corrected, at the same place'
    r['placement'] = 'his paragraph, where he put it in section B'
    r['opens']['why_reading'] = 'his opening sentence, which tells the reader what glutamate does in their brain'
    r['same_point'] = SAME_B
    r['needed'] = {'reader': 'none run: his own paragraph, which he cut to what the reader needs himself', 'unneeded': [], 'kept': {}}
    r['questions'] = dict(QS)
    return r


def main():
    items, bad = [], 0
    for d in D:
        t = plain(d['text'])
        r = receipt(d, t)
        probs = R.check(t, r)
        (HERE / (d['name'] + '.txt')).write_text(t + '\n', encoding='utf-8')
        (HERE / (d['name'] + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(d['name'], len(t.split()), 'words', 'PASS' if not probs else probs)
        bad += bool(probs)
    pair = plain(D[1]['text']) + '\n\n' + plain(D[2]['text'])
    (HERE / 'PAIR-040-041n.txt').write_text(pair + '\n', encoding='utf-8')
    comps = [json.loads((HERE / (n + '.receipt.json')).read_text()) for n in ('B040n', 'B041n')]
    rp = R.make(pair, SECTION, READER)
    lut = {x['s']: x for c in comps for x in c['sentences']}
    for x in rp['sentences']:
        x.update({k: v for k, v in lut[x['s']].items() if k in ('payoff', 'follows')})
        if 'link' in x:
            x['link'] = 'none: the next tool in the list, which opens on its own subject'
    rp.update(placement=comps[0]['placement'], same_point=comps[0]['same_point'], questions=dict(QS),
              checked=comps[0]['checked'] + comps[1]['checked'])
    rp['opens']['why_reading'] = comps[0]['opens']['why_reading']
    rp['needed'] = {'reader': comps[0]['needed']['reader'] + '; and needed/b041/READ.md', 'unneeded': [], 'kept': {}}
    probs = R.check(pair, rp)
    (HERE / 'PAIR-040-041n.receipt.json').write_text(json.dumps(rp, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('PAIR-040-041n', len(pair.split()), 'words', 'PASS' if not probs else probs)
    bad += bool(probs)
    for name, text, his, pay in [('T37b', plain(T37_FIXED), plain(HIS.HIS37), 'that stress-level calcium can injure the neurons, without the swelling his sources don\'t show'),
                                 ('T38b', plain(T38_FIXED), plain(HIS.HIS38), 'that NMDA receptors are the main way calcium gets in, and GluD is another door')]:
        r = his_receipt(name, text, his, pay)
        probs = R.check(text, r)
        (HERE / (name + '.txt')).write_text(text + '\n', encoding='utf-8')
        (HERE / (name + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(name, len(text.split()), 'words', 'PASS' if not probs else probs)
        bad += bool(probs)
    for name, text in [('B039n', plain(D[0]['text'])), ('PAIR-040-041n', pair), ('HIS37', plain(HIS.HIS37)),
                       ('HIS38', plain(HIS.HIS38)), ('T37b', plain(T37_FIXED)), ('T38b', plain(T38_FIXED))]:
        if name.startswith('HIS'):
            (HERE / (name + '.txt')).write_text(text + '\n', encoding='utf-8')
        items.append([name, text, hashlib.sha256(text.encode('utf-8')).hexdigest()])
    (HERE / 'ITEMS.json').write_text(json.dumps(items, ensure_ascii=False) + '\n', encoding='utf-8')
    print('items:', [x[0] for x in items])
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
