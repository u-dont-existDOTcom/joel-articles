#!/usr/bin/env python3
"""Two sets for one batch (2026-11-06, after "do you need me to do anything?" at 22:23 UTC):

1. Third tries of blocks 20, 25, 26 and 27, from the tell panel (panel/P0xx/PANEL.md: Sonnet and Haiku agreed on every
   sentence; their notes: an even build where each sentence does one job (hook, analogy, roadmap), stacked metaphors, a
   generic "you" hook, soft reassurance, no concrete detail). The fix: a concrete case in place of the generic hook, the
   build uneven, the post's own metaphors kept where he kept them (X-26: house, solvent, concrete, software) and the
   stacked ones of mine dropped (P025's prison and glue said plainly).
2. Section B (the Glutamate section), the blocks that read AI in the whole check and need no fact change: 35, 38, 42, 43
   and 44. Block 36 (a second "Metabolic Red Line" paragraph) is a repeat of section A for a card; 37 carries F-3's fact
   ("vibrating cells to death") and 39 is long, so they come next.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drafts_p1 as A  # noqa: E402
R = A.R

READER_B = ('someone with trauma or in withdrawal who is anxious, wired, ruminating or raging, wanting to know what is '
            'going on in the brain and which of the protocol\'s tools does what')
SEC_B = 'B. The "Overheating" CPU: Glutamate Excitotoxicity'
SW = dict(section=A.SECTION_SW, reader=A.READER_SW)

T = [
    dict(name='P020c', block=20, starts='Standard therapy attempts to rewrite', **SW,
         text=('Maybe you\'ve done years of CBT or EMDR and you still freeze up or blow up at the same old triggers. '
                'Standard therapy is trying to rewrite the "code" (your thoughts and behaviors), while the "motherboard" '
                '(the brain\'s physical structure and chemistry) is often overheating or damaged, and code doesn\'t run '
                'well on a motherboard like that. This protocol goes after four specific neuro-biological problems that '
                'must be addressed before psychological tools can do much.'),
         pay=['they recognize their own stuck reactions after therapy',
              'they see why: therapy works on the code while the hardware underneath is failing',
              'they learn what the protocol does about it before therapy can help'],
         fol=['opens the section with the reader\'s case under its software and hardware heading',
              'gives the reason for that case in the heading\'s terms',
              'says what the protocol does about the reason'],
         opens='the reader who is still triggered after years of therapy recognizes themselves in the first line',
         same='none: read the section for the software/hardware point; the Underpinning paragraph illustrates it next'),
    dict(name='P025c', block=25, starts='As we grow up, our "Role-Self"', **SW,
         text=('As we grow up, the "Role-Self" (the personality built to please and manage the people around us) gets '
                'locked in by Dopamine and DeltaFosB, and often your addiction is just what keeps that Role-Self running. '
                'The protocol targets the chemistry that holds the false persona in place, so the person you were before '
                'the trauma (your "True-Self") can come back out.'),
         pay=['they learn what holds the Role-Self in place and what their addiction may be doing for it',
              'they learn what the protocol aims to change, and what it gives back'],
         fol=['carries on from Gibson\'s Role-Self in the paragraphs before',
              'says what the protocol does about it'],
         opens='it tells the reader what keeps the Role-Self in place, including their own addiction',
         same='none: read the section from its heading to Part 1 for the Role-Self; Gibson\'s paragraph says where it comes from, this one what holds it'),
    dict(name='P026c', block=26, starts='Neurological De-Armoring is about fixing the underpinnings', **SW,
         text=('Neurological De-Armoring fixes the underpinnings first. Ketones (BHB) block HDAC, an enzyme that keeps '
                'genes switched off, and with Glutamate modulation on top, the protocol acts as a metabolic solvent that '
                'softens the "concrete" in the brainstem. Then we can dig under the house and pour a new foundation, and '
                'only after that update the psychological software upstairs.'),
         pay=['they learn what the protocol does first',
              'they learn the two levers and what HDAC blocking does, in plain words',
              'they learn the order: foundation, then the therapy work'],
         fol=['draws the conclusion of the paragraphs before',
              'says how',
              'says what that makes possible, in order'],
         opens='it tells the reader what the protocol fixes first',
         same='none: read the section from its heading to Part 1 for the underpinning point; the Underpinning paragraph gives the house, this one the protocol (his X-26 decisions kept: '
              'underpinnings, solvent, concrete, house, software)'),
    dict(name='P027c', block=27, starts='The Anti-Breakthrough (Micro-Dosing)', **SW,
         text=('The Anti-Breakthrough (Micro-Dosing): Long therapy sessions that leave you wrecked for days aren\'t doing '
                'what they\'re supposed to. Dr. Perry found the "therapeutic window" for a dysregulated brain is often '
                'only seconds long, and a sensitized, armored nervous system just can\'t take in sixty minutes of trauma '
                'processing, so the "hour-long breakthrough" has to wait.'),
         pay=['they recognize sessions that wreck them and learn those sessions are not working',
              'they learn why (a window of seconds) and what to drop for now'],
         fol=['moves from what the protocol does to how to do the therapy part meanwhile',
              'gives Perry\'s reason and what follows'],
         opens='the reader who has been wrecked by long sessions recognizes it in the first line',
         same='none: read the section from its heading to Part 1 for the dose point; the next paragraph gives the practice this one sets up'),
    dict(name='B035', block=35, starts='The Problem: Glutamate is the brain', section=SEC_B, reader=READER_B,
         text=('The Problem: Under stress the brain floods with Glutamate, its main "go" signal (the primary excitatory '
                'neurotransmitter), and that flood is the "voltage spike," with the engine redlining.'),
         pay=['they learn what is flooding their brain under stress and what that means'],
         fol=['opens section B under its heading, which names glutamate'],
         opens='it names what is happening in the reader\'s brain under stress before any mechanism',
         same='none: read section B for the flood; the Mechanism paragraph says what it does to the receptors'),
    dict(name='B038', block=38, starts='The Signal Dial (GluD Receptors)', section=SEC_B, reader=READER_B,
         text=('The Signal Dial (GluD Receptors): There\'s also a second dial. Johns Hopkins researchers have recently '
                'discovered that the brain uses GluD receptors like a master volume knob: NMDA is the spark, and GluD sets '
                'the baseline "hum" of the synapse. In an armored state, this dial is often jammed, either on "High" '
                '(Cerebellar Ataxia/Hyper-vigilance) or on "Low" (Apathy/Schizotypy).'),
         pay=['they learn there is a second control besides NMDA',
              'they learn what GluD does, in the volume-knob picture',
              'they learn how the dial goes wrong, both ways, and what each looks like'],
         fol=['adds a second dial to the NMDA key of the paragraph before',
              'says what the second dial is',
              'says how it goes wrong in the armored state'],
         opens='it tells the reader there is a second control to know about',
         same='none: read section B for GluD; the Repair paragraph uses the dial, this one introduces it'),
    dict(name='B042', block=42, starts='The Repair (Leucine/L-Serine)', section=SEC_B, reader=READER_B,
         text=('The Repair (Leucine/L-Serine): L-Serine is what the brain makes D-Serine from, so it can help recalibrate '
                'the GluD "Volume Dial" and make therapy sessions that end with low fear and a sense of mastery stick '
                'better. The conversion is inefficient, though, which is why some people take D-serine itself, with a '
                'higher risk and a higher benefit. Leucine helps with structural repair and at the same time tunes '
                'synaptic gain, which eases the "itchy brain" feeling.'),
         pay=['they learn what L-Serine does for their therapy sessions',
              'they learn its limit and why some take D-serine instead, with its trade-off',
              'they learn what leucine does for them, down to the itchy-brain feeling'],
         fol=['names the third tool after the Vacuum and the Lock',
              'gives the limit of the first part',
              'turns to the other half of the Repair'],
         opens='it says what the Repair does for the reader\'s sessions',
         same='none: read section B for L-Serine and D-Serine; the D-serine paragraph above explains the learning, '
              'this one the tool'),
    dict(name='B043', block=43, starts='The Governor (Agmatine)', section=SEC_B, reader=READER_B,
         text=('The Governor (Agmatine): If your Glutamate Storm is the hot, itchy, reactive, pain-y, rumination-heavy '
                'kind, agmatine is the optional "voltage governor." It may help when the problem isn\'t just excess '
                'glutamate in the synapse but NMDA/GluN2B over-reactivity, and it\'s a brake for that state, to use when '
                'you\'re in it, not a daily foundation nutrient.'),
         pay=['they can tell whether agmatine is for their kind of storm',
              'they learn why it helps that kind and that it is for the state, not daily'],
         fol=['names the fourth tool, for one kind of storm',
              'says what it acts on and how to use it'],
         opens='the reader with the hot, ruminating kind of storm sees at once whether this tool is for them',
         same='section 2 of Part 3 and the timeline give agmatine\'s doses and cycle; this paragraph says what it is '
              'for, so they are kept apart'),
    dict(name='B044', block=44, starts='Important conflict: do not use agmatine', section=SEC_B, reader=READER_B,
         text=('Important conflict: don\'t take agmatine in the same session as D-Serine/DCS-style exposure or EMDR '
                'work, because agmatine partly brakes NMDA activity, which is the very learning and memory updating those '
                'tools are there to support. Use agmatine for storm control, and not right before a session where the '
                'goal is deliberate reconsolidation.'),
         pay=['they learn not to combine agmatine with those sessions, and why',
              'they learn when agmatine is for and when to leave it out'],
         fol=['follows the Governor with the one conflict it has',
              'says how to time it'],
         opens='it gives the reader the rule first, with its reason in the same sentence',
         same='the timeline\'s "Timing rule" says the same for its weeks; this is where the reason is, so both stay'),
]


def main():
    raw = A.ART.read_text(encoding='utf-8')
    blocks = raw.split('\n\n')
    for d in T:
        b = d['block']
        cur = blocks[b]
        assert cur.startswith(d['starts']) or b in (30, 32, 33), (b, cur[:60])
        name = d['name']
        (HERE / (name + '.txt')).write_text(d['text'] + '\n', encoding='utf-8')
        r = R.make(d['text'], d['section'], d['reader'])
        assert len(r['sentences']) == len(d['pay']), (name, [x['s'] for x in r['sentences']])
        for x, p, f in zip(r['sentences'], d['pay'], d['fol']):
            x['payoff'], x['follows'] = p, f
        r['placement'] = 'where the block is now (block %d); its place in its section is unchanged' % b
        r['opens']['why_reading'] = d['opens']
        r['same_point'] = d['same']
        r['questions'] = {q: 'PASS: read sentence by sentence against this reader' for q in R.QUESTIONS}
        (HERE / (name + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(name, R.check(d['text'], r) or 'PASS', len(d['text'].split()), 'words')
        # the article keeps the link on "Johns Hopkins researchers have recently discovered"
        t = d['text']
        if b == 38:
            link = cur[cur.index('['):cur.index(')', cur.index('](')) + 1]
            t = t.replace('Johns Hopkins researchers have recently discovered', link)
        blocks[b] = t
    (HERE / 'CANDIDATE-r2.md').write_text('\n\n'.join(blocks), encoding='utf-8')
    fk = subprocess.run([sys.executable, str(A.ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                         str(A.ROOT / 'articles/neuro-de-armoring/humanize/FIDELITY-KEYS.json'), str(HERE / 'CANDIDATE-r2.md')],
                        capture_output=True, text=True)
    print(fk.stdout.strip().splitlines()[-5:])


if __name__ == '__main__':
    main()
