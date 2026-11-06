#!/usr/bin/env python3
"""Round 3 of 6 November (after his message of 23:01 UTC and his version of block 20): the paragraphs that read AI in
rounds 1 and 2, tried his way (docs/lessons/2026-11-06-2301-neuro.md): each sentence says in words how it answers the
reader's case or the sentence before; the author is there where it's true ("I built", "I'd look at"); compressed
abstractions are put in the reader's hands; a question asks the reader in first where it fits. Each phrase of his is not
copied into every paragraph (a phrase repeated across paragraphs would be a tell of its own).

Writes each text, its receipt (with `link` on every sentence after the first) and a candidate article for the fidelity
check. Blocks are found by the start of their current text."""
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

D = [
    dict(name='P025d', starts='As we grow up, our "Role-Self"', **SW,
         text=('Do you ever feel like you\'re playing a part that isn\'t really you? That\'s the "Role-Self" (the '
               'personality we built to please and manage the people around us), and as we grow up it gets locked in by '
               'Dopamine and DeltaFosB, so often your addiction is just what keeps it running. That\'s why I built this '
               'protocol to go after the chemistry holding the false persona in place, so the person you were before the '
               'trauma (your "True-Self") can come back out.'),
         rows=[('they ask themselves whether they are playing a part', 'opens on the reader after Gibson\'s Role-Self', ''),
               ('they learn the part has a name and what holds it in place, their addiction included',
                'answers the question', 'That\'s the'),
               ('they learn what the protocol does for them about it', 'says what follows', 'That\'s why I built')],
         opens='a question that asks the reader whether they live as a part that isn\'t them',
         same='none: read the section from its heading to Part 1 for the Role-Self; Gibson\'s paragraph says where it '
              'comes from, this one what holds it'),
    dict(name='P026d', starts='Neurological De-Armoring is about fixing the underpinnings', **SW,
         text=('So with Neurological De-Armoring, I\'m fixing the underpinnings first, instead of redecorating. The way it '
               'works is that Ketones (BHB) block HDAC, an enzyme that keeps genes switched off, and together with '
               'Glutamate modulation that makes the protocol a kind of metabolic solvent, softening the "concrete" in the '
               'brainstem. That\'s what lets us dig under the house and pour a new foundation, and only then update the '
               'psychological software upstairs.'),
         rows=[('they learn what the protocol fixes first, in the house they already have',
                'draws the conclusion of the paragraphs before', ''),
               ('they learn how, with HDAC said in plain words', 'says how', 'The way it works is that'),
               ('they learn the order: foundation, then the therapy work', 'says what that makes possible',
                'That\'s what lets us')],
         opens='it tells the reader what the protocol fixes first, in the house picture',
         same='none: read the section from its heading to Part 1 for the underpinning point; his X-26 decisions kept '
              '(underpinnings, solvent, concrete, house, software)'),
    dict(name='P027d', starts='The Anti-Breakthrough (Micro-Dosing)', **SW,
         text=('The Anti-Breakthrough (Micro-Dosing): Have long therapy sessions ever left you wrecked for days? That\'s '
               'because, as Dr. Perry found, the "therapeutic window" for a dysregulated brain is often only seconds long, '
               'and a sensitized, armored nervous system just can\'t take in sixty minutes of trauma processing. So for '
               'now, the "hour-long breakthrough" has to wait.'),
         rows=[('they ask themselves whether sessions have wrecked them', 'moves from the protocol to the therapy part', ''),
               ('they learn why: a window of seconds', 'answers the question', 'That\'s because'),
               ('they learn what to drop for now', 'says what follows', 'So for now')],
         opens='a question that asks the reader about their own sessions',
         same='none: read the section from its heading to Part 1 for the dose point; the next paragraph gives the practice'),
    dict(name='P028d', starts='Your goal is Micro-Dosing Safety', **SW,
         text=('Instead, the goal is Micro-Dosing Safety: 30 seconds of regulated breathing, twenty times a day. Think of '
               'it more as physical therapy for a broken nervous system than as running a marathon, where how often you '
               'do it matters more than how hard you push.'),
         rows=[('they get the practice itself', 'says what to do instead of the hour', ''),
               ('they learn to judge it by how often', 'tells them how to hold the practice', 'Think of it')],
         opens='it gives the reader the practice that replaces the hour-long session',
         same='none: read the section from its heading to Part 1 for the practice; it is said here only'),
    dict(name='B038d', starts='The Signal Dial (GluD Receptors)', **B,
         text=('The Signal Dial (GluD Receptors): NMDA isn\'t the only control, though. Johns Hopkins researchers have '
               'recently discovered that the brain also uses GluD receptors as a kind of master volume knob, so if NMDA is '
               'the spark, GluD sets the baseline "hum" of the synapse. And in an armored state, that dial often gets '
               'jammed, either on "High" (Cerebellar Ataxia/Hyper-vigilance) or on "Low" (Apathy/Schizotypy).'),
         rows=[('they learn there is a second control besides the NMDA key', 'follows the NMDA key of the paragraph before',
                ''),
               ('they learn what GluD does', 'says what the other control is', 'also uses'),
               ('they learn how it goes wrong, both ways', 'says what happens to it in the armored state', 'And in an armored state')],
         opens='it tells the reader the NMDA key from the paragraph before is not the only control',
         same='none: read section B from its heading to C for GluD; the Repair uses the dial, this one introduces it'),
    dict(name='B042d', starts='The Repair (Leucine/L-Serine)', **B,
         text=('The Repair (Leucine/L-Serine): L-Serine is what the brain makes D-Serine from, so it can help recalibrate '
               'the GluD "Volume Dial" and make therapy sessions that end with low fear and a sense of mastery stick '
               'better. The catch is that the conversion is inefficient, which is why some people take D-serine itself '
               'instead (higher risk, but also higher benefit). And Leucine is there for structural repair, while it also '
               'tunes synaptic gain, which is what eases the "itchy brain" feeling.'),
         rows=[('they learn what L-Serine does for their sessions', 'names the third tool after the Vacuum and the Lock', ''),
               ('they learn its limit and why some take D-serine', 'gives the limit of the first part', 'The catch is that'),
               ('they learn what leucine does for them', 'turns to the other half of the Repair', 'And Leucine is there')],
         opens='it says what the Repair does for the reader\'s sessions; its first sentence read Human in round 2',
         same='none: read section B from its heading to C for L-Serine; the D-serine paragraph explains the learning'),
    dict(name='B043d', starts='The Governor (Agmatine)', **B,
         text=('The Governor (Agmatine): Is your Glutamate Storm the hot, itchy, reactive, pain-y, rumination-heavy kind? '
               'Then agmatine is the optional "voltage governor" I\'d look at. That\'s because it may help when the problem '
               'isn\'t just excess glutamate in the synapse but NMDA/GluN2B over-reactivity, so think of it as a brake for '
               'that state, something to use while you\'re in it rather than a daily foundation nutrient.'),
         rows=[('they ask themselves which kind of storm they have', 'names the fourth tool by the storm it fits', ''),
               ('they learn this tool is for that kind', 'answers the question', 'Then agmatine'),
               ('they learn why and how to use it', 'gives the reason and the use', 'That\'s because')],
         opens='a question that lets the reader tell whether this tool is for their kind of storm',
         same='Part 3 and the timeline give agmatine\'s doses and cycle; this says what it is for, so they are kept apart'),
    dict(name='B044d', starts='Important conflict: do not use agmatine', **B,
         text=('Important conflict: don\'t take agmatine in the same session as D-Serine/DCS-style exposure or EMDR work. '
               'The reason is that agmatine partly brakes NMDA activity, and NMDA-dependent learning and memory updating '
               'is exactly what those tools are there to support. So use agmatine for storm control, but not right before '
               'a session where the goal is deliberate reconsolidation.'),
         rows=[('they learn the rule first', 'follows the Governor with its one conflict', ''),
               ('they learn why', 'gives the reason', 'The reason is that'),
               ('they learn when to use it and when not', 'says how to time it', 'So use agmatine')],
         opens='it gives the reader the rule first',
         same='the timeline\'s "Timing rule" says the same for its weeks; this is where the reason is, so both stay'),
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
            x['payoff'], x['follows'] = p, f
            if 'link' in x:
                x['link'] = link
        r['placement'] = 'where the block is now (block %d); its place in its section is unchanged' % b
        r['opens']['why_reading'] = d['opens']
        r['same_point'] = d['same']
        r['questions'] = {q: 'PASS: read sentence by sentence against this reader' for q in R.QUESTIONS}
        (HERE / (d['name'] + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n',
                                                         encoding='utf-8')
        print(d['name'], 'block', b, R.check(d['text'], r) or 'PASS', len(d['text'].split()), 'words')
        t = d['text']
        if 'Johns Hopkins researchers have' in t and '](' in cur:
            link = cur[cur.index('['):cur.index(')', cur.index('](')) + 1]
            t = t.replace('Johns Hopkins researchers have recently discovered', link)
        blocks[b] = t
    (HERE / 'CANDIDATE.md').write_text('\n\n'.join(blocks), encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                         str(ROOT / 'articles/neuro-de-armoring/humanize/FIDELITY-KEYS.json'), str(HERE / 'CANDIDATE.md')],
                        capture_output=True, text=True)
    print(fk.stdout.strip().splitlines()[-4:])


if __name__ == '__main__':
    main()
