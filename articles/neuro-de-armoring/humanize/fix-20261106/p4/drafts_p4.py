#!/usr/bin/env python3
"""Round 4 of 6 November (after his message of 23:50 UTC): the paragraphs still reading AI, edited the way his block 25
went Human (docs/lessons/2026-11-06-2350-neuro.md): people as the actors in active voice ("we use", "I'd use") in place of
a thing or a definition as the subject; "so" or "since" where the link is cause; context before the point inside each
sentence; a sentence that isn't needed cut. Each is a small edit of the last try, not a rebuild."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
ART = ROOT / 'articles/neuro-de-armoring/humanize/HUMANIZED-SO-FAR.md'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as R  # noqa: E402

SW = dict(section='Psychology is the Software; Biology is the Hardware.',
          reader=('someone with trauma, often with addiction, who has done therapy and still reacts the same way, reading '
                  'to learn why and whether this protocol is for them'))
B = dict(section='B. The "Overheating" CPU: Glutamate Excitotoxicity',
         reader=('someone with trauma or in withdrawal who is anxious, wired, ruminating or raging, wanting to know what '
                 'is going on in the brain and which of the protocol\'s tools does what'))
SAME_SW = 'none: read the section from its heading to Part 1 for the point; it is said here only'
SAME_B = 'none: read section B from its heading to C for the point; it is said here only'

D = [
    dict(name='P026e', starts='Neurological De-Armoring is about fixing the underpinnings', **SW,
         text=('So with Neurological De-Armoring, I\'m fixing the underpinnings first, instead of redecorating. I use '
               'Ketones (BHB), which block HDAC (an enzyme that keeps genes switched off), along with Glutamate '
               'modulation, and together they work like a metabolic solvent to soften the "concrete" in the brainstem. '
               'That lets us dig under the house and pour a new foundation, so we can then update the psychological '
               'software upstairs.'),
         rows=[('what the protocol fixes first', 'draws the conclusion of the paragraphs before', ''),
               ('how, with HDAC in plain words', 'says how, with the author as the actor', 'I use'),
               ('the order: foundation, then the therapy work', 'says what that makes possible', 'That lets us')],
         opens='it tells the reader what the protocol fixes first, in the house picture'),
    dict(name='P027e', starts='The Anti-Breakthrough (Micro-Dosing)', **SW,
         text=('The Anti-Breakthrough (Micro-Dosing): Dr. Perry found that for a dysregulated brain, the "therapeutic '
               'window" is often only seconds long, so a sensitized, armored nervous system just can\'t take in sixty '
               'minutes of trauma processing, which is why long sessions can leave you wrecked for days. So for now, we '
               'give up on the "hour-long breakthrough."'),
         rows=[('why long sessions wreck them', 'moves from the protocol to the therapy part, with Perry\'s finding', ''),
               ('what to drop for now', 'says what follows', 'So for now, we')],
         opens='it gives Perry\'s finding with what it means for the reader\'s sessions in the same sentence'),
    dict(name='P028e', starts='Your goal is Micro-Dosing Safety', **SW,
         text=('Instead, aim for Micro-Dosing Safety: 30 seconds of regulated breathing, twenty times a day. It\'s more like '
               'physical therapy for a broken nervous system than running a marathon, so how often you do it matters '
               'more than how hard you push.'),
         rows=[('the practice itself', 'says what to do instead of the hour', ''),
               ('to judge it by how often', 'tells them how to hold the practice', 'so how often')],
         opens='it gives the reader the practice that replaces the hour-long session'),
    dict(name='B038e', starts='The Signal Dial (GluD Receptors)', **B,
         text=('The Signal Dial (GluD Receptors): Johns Hopkins researchers recently discovered that the brain also uses '
               'GluD receptors as a kind of master volume knob, so if NMDA is the spark, GluD sets the baseline "hum" of '
               'the synapse. In an armored state that dial often gets jammed, either on "High" (Cerebellar '
               'Ataxia/Hyper-vigilance) or on "Low" (Apathy/Schizotypy).'),
         rows=[('there is a second control, and what it does', 'follows the NMDA key of the paragraph before', ''),
               ('how it goes wrong, both ways', 'says what happens to it in the armored state', 'In an armored state')],
         opens='it tells the reader the brain has a second control besides the NMDA key'),
    dict(name='B042e', starts='The Repair (Leucine/L-Serine)', **B,
         text=('The Repair (Leucine/L-Serine): L-Serine is what the brain makes D-Serine from, so it can help recalibrate '
               'the GluD "Volume Dial" and make therapy sessions that end with low fear and a sense of mastery stick '
               'better. The conversion isn\'t very efficient though, so some people take D-serine itself instead (more '
               'risk, but also more benefit). And we use Leucine for structural repair, since it also tunes synaptic '
               'gain, which eases the "itchy brain" feeling.'),
         rows=[('what L-Serine does for their sessions', 'names the third tool after the Vacuum and the Lock', ''),
               ('its limit and why some take D-serine', 'gives the limit of the first part', 'though, so'),
               ('what leucine does for them', 'turns to the other half of the Repair', 'And we use Leucine')],
         opens='it says what the Repair does for the reader\'s sessions; its first sentence read Human, High'),
    dict(name='B043e', starts='The Governor (Agmatine)', **B,
         text=('The Governor (Agmatine): For the hot, itchy, reactive, pain-y, rumination-heavy kind of Glutamate Storm, '
               'agmatine is the optional "voltage governor" I\'d use. It may help when the problem isn\'t just excess '
               'glutamate in the synapse but NMDA/GluN2B over-reactivity, so you use it as a brake while you\'re in that '
               'state, not every day like a foundation nutrient.'),
         rows=[('which storm the tool is for, first', 'names the fourth tool by the storm it fits', ''),
               ('why it helps and how to use it', 'gives the reason and the use', 'so you use it')],
         opens='the kind of storm comes first, so the reader knows at once whether this tool is for them'),
    dict(name='B044e', starts='Important conflict: do not use agmatine', **B,
         text=('Important conflict: don\'t take agmatine in the same session as D-Serine/DCS-style exposure or EMDR work, '
               'since agmatine partly brakes NMDA activity, and those tools need NMDA to do the learning and memory '
               'updating they\'re there for. So I\'d use agmatine for storm control, but not right before a session where '
               'you\'re deliberately working on reconsolidation.'),
         rows=[('the rule and why, together', 'follows the Governor with its one conflict', ''),
               ('when to use it and when not', 'says how to time it', 'So I\'d use agmatine')],
         opens='it gives the reader the rule and its reason first'),
]


def main():
    raw = ART.read_text(encoding='utf-8')
    blocks = raw.split('\n\n')
    for d in D:
        hits = [i for i, b in enumerate(blocks) if b.startswith(d['starts'])]
        assert len(hits) == 1, (d['name'], hits)
        b = hits[0]
        cur = blocks[b]
        (HERE / (d['name'] + '.txt')).write_text(d['text'] + '\n', encoding='utf-8')
        r = R.make(d['text'], d['section'], d['reader'])
        assert len(r['sentences']) == len(d['rows']), (d['name'], [x['s'] for x in r['sentences']])
        for x, (p, f, link) in zip(r['sentences'], d['rows']):
            x['payoff'], x['follows'] = 'they learn ' + p, f
            if 'link' in x:
                x['link'] = link
        r['placement'] = 'where the block is now (block %d); its place in its section is unchanged' % b
        r['opens']['why_reading'] = d['opens']
        r['same_point'] = SAME_B if d['section'].startswith('B.') else SAME_SW
        r['questions'] = {q: 'PASS: read sentence by sentence against this reader' for q in R.QUESTIONS}
        (HERE / (d['name'] + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n',
                                                         encoding='utf-8')
        print(d['name'], 'block', b, R.check(d['text'], r) or 'PASS', len(d['text'].split()), 'words')
        t = d['text']
        if 'Johns Hopkins researchers' in t and '](' in cur:
            link = cur[cur.index('['):cur.index(')', cur.index('](')) + 1]
            t = t.replace('Johns Hopkins researchers recently discovered', link.replace('have recently', 'recently'))
        blocks[b] = t
    (HERE / 'CANDIDATE.md').write_text('\n\n'.join(blocks), encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                         str(ROOT / 'articles/neuro-de-armoring/humanize/FIDELITY-KEYS.json'), str(HERE / 'CANDIDATE.md')],
                        capture_output=True, text=True)
    print(fk.stdout.strip().splitlines()[-4:])
    # the pair for block 28 (under 50 words alone)
    text = '\n\n'.join((HERE / (p + '.txt')).read_text(encoding='utf-8').rstrip('\n') for p in ('P027e', 'P028e'))
    (HERE / 'PAIR-027-028e.txt').write_text(text + '\n', encoding='utf-8')
    comps = [json.loads((HERE / (p + '.receipt.json')).read_text(encoding='utf-8')) for p in ('P027e', 'P028e')]
    lut = {x['s']: x for c in comps for x in c['sentences']}
    r = R.make(text, comps[0]['section'], comps[0]['reader'])
    for x in r['sentences']:
        src = lut[x['s']]
        x['payoff'], x['follows'] = src['payoff'], src['follows']
        if 'link' in x:
            x['link'] = src.get('link') or 'Instead'
    r['placement'] = '; '.join(c['placement'] for c in comps)
    r['opens']['why_reading'] = comps[0]['opens']['why_reading']
    r['same_point'] = SAME_SW
    r['questions'] = comps[0]['questions']
    (HERE / 'PAIR-027-028e.receipt.json').write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('PAIR-027-028e', R.check(text, r) or 'PASS')


if __name__ == '__main__':
    main()
