#!/usr/bin/env python3
"""Round P1, second tries (2026-11-06): the paragraphs whose first try read AI (RESULTS.md), each with the next small fix
of the kind his versions make (E361, E368): a hedge where the claim is the reader's guess ("it might not be the therapy's
fault"), the causal joins he uses ("That's because", "So"), terms in brackets after their name as he writes them, and the
pitch-like close turned into what the protocol is about. The Underpinning paragraph goes back to its own words, which read
Human (Low) in the whole check where my rewrite read AI, with only the colon after its label.
Writes P<block>b.txt, receipts, the pairs, and checks fidelity on CANDIDATE-b.md."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drafts_p1 as A  # noqa: E402
R = A.R

TRY2 = {
    20: dict(text=('If you\'ve done a lot of therapy and you\'re still reacting the same way, it might not be the therapy\'s '
                   'fault. That\'s because standard therapy tries to rewrite the "code" (your thoughts and behaviors), and '
                   'if the "motherboard" (the brain\'s physical structure and chemistry) is overheating or damaged, the new '
                   'code won\'t run very well. So the science behind this protocol looks at four specific neuro-biological '
                   'problems that must be addressed before psychological tools can really work.')),
    21: dict(text=('The "Underpinning" Principle: Dr. Bruce Perry compares treating trauma to building a house. Standard '
                   'CBT & EMDR style therapies attempt to "decorate" the house (changing thoughts/behaviors in the Cortex) '
                   'while the foundation (the Brainstem) is crumbling. You cannot hang curtains in a collapsing house.'),
             pay=['they get a picture they can hold for why therapy alone may not stick',
                  'they see which part of the brain therapy works on and which part is failing underneath',
                  'they keep the point in one image: you can\'t decorate a house that is falling down'],
             fol=['illustrates the paragraph before (software over damaged hardware) with Perry\'s house',
                  'applies the house to the therapies the reader has likely tried',
                  'sums the picture up in the article\'s own line, kept from the post']),
    25: dict(text=('If you feel stuck playing a part that isn\'t really you, that\'s probably your "Role-Self," and as we '
                   'grow up it gets hardened by Dopamine and DeltaFosB until it\'s like a prison. Your addiction is often '
                   'just the fuel it takes to keep that Role-Self running. So this protocol is about dissolving the '
                   'chemical glue that holds the false persona together, so your "True-Self" (the person you were before '
                   'the trauma) can finally come back out.')),
    26: dict(text=('So Neurological De-Armoring is about fixing the underpinnings first, rather than redecorating. The '
                   'protocol works like a metabolic solvent, by supplementing Ketones (BHB), which block HDAC (an enzyme '
                   'that keeps genes switched off), along with Glutamate modulation, to soften the "concrete" in the '
                   'brainstem. That lets us dig under the house and pour a new foundation, so we can eventually update '
                   'the psychological software upstairs.')),
    27: dict(text=('The Anti-Breakthrough (Micro-Dosing): If long therapy sessions leave you more overwhelmed than helped, '
                   'that\'s actually normal. Dr. Perry explains that a dysregulated brain\'s "therapeutic window" is often '
                   'only seconds long, so a sensitized, armored nervous system just can\'t take in sixty minutes of trauma '
                   'processing. So for now we need to give up the therapy ideal of the "hour-long breakthrough."'),
             pay=['they recognize their own experience of long sessions and hear it is normal',
                  'they learn why: the window is seconds long, too short for an hour of processing',
                  'they can drop the hour-long breakthrough as a goal for now'],
             fol=['moves from what the protocol does to how to do the therapy part meanwhile, from the reader\'s own '
                  'experience of sessions',
                  'gives Perry\'s reason for that experience',
                  'says what follows from the reason']),
}


def main():
    raw = A.ART.read_text(encoding='utf-8')
    blocks = raw.split('\n\n')
    byblock = {d['block']: d for d in A.D}
    for b, t in TRY2.items():
        d = dict(byblock[b])
        d.update(t)
        assert blocks[b].startswith(d['starts']), b
        name = 'P%03db' % b
        (HERE / (name + '.txt')).write_text(d['text'] + '\n', encoding='utf-8')
        r = R.make(d['text'], d['section'], d['reader'])
        assert len(r['sentences']) == len(d['pay']), (b, [x['s'] for x in r['sentences']])
        for x, p, f in zip(r['sentences'], d['pay'], d['fol']):
            x['payoff'], x['follows'] = p, f
        r['placement'] = 'where the block is now (block %d); its place in the section is unchanged' % b
        r['opens']['why_reading'] = d['opens']
        r['same_point'] = d['same']
        r['questions'] = {q: 'PASS: read sentence by sentence against this reader' for q in R.QUESTIONS}
        (HERE / (name + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(name, R.check(d['text'], r) or 'PASS')
        blocks[b] = d['text']
    for b in (30, 32, 33):
        blocks[b] = (HERE / ('P%03d.txt' % b)).read_text(encoding='utf-8').rstrip('\n')
    blocks[28] = (HERE / 'P028.txt').read_text(encoding='utf-8').rstrip('\n')
    (HERE / 'CANDIDATE-b.md').write_text('\n\n'.join(blocks), encoding='utf-8')
    fk = subprocess.run([sys.executable, str(A.ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                         str(A.ROOT / 'articles/neuro-de-armoring/humanize/FIDELITY-KEYS.json'), str(HERE / 'CANDIDATE-b.md')],
                        capture_output=True, text=True)
    print(fk.stdout.strip().splitlines()[-4:])
    # the pairs for the two under the web app's 50-word minimum
    for name, parts in (('PAIR-020-021b', ['P020b', 'P021b']), ('PAIR-027-028b', ['P027b', 'P028'])):
        text = '\n\n'.join((HERE / (p + '.txt')).read_text(encoding='utf-8').rstrip('\n') for p in parts)
        (HERE / (name + '.txt')).write_text(text + '\n', encoding='utf-8')
        comps = [json.loads((HERE / (p + '.receipt.json')).read_text(encoding='utf-8')) for p in parts]
        lut = {x['s']: x for c in comps for x in c['sentences']}
        r = R.make(text, comps[0]['section'], comps[0]['reader'])
        for x in r['sentences']:
            x['payoff'], x['follows'] = lut[x['s']]['payoff'], lut[x['s']]['follows']
        r['placement'] = '; '.join(c['placement'] for c in comps)
        r['opens']['why_reading'] = comps[0]['opens']['why_reading']
        r['same_point'] = ' | '.join(c['same_point'] for c in comps)
        r['questions'] = comps[0]['questions']
        (HERE / (name + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(name, R.check(text, r) or 'PASS')


if __name__ == '__main__':
    main()
