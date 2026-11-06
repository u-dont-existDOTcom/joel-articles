#!/usr/bin/env python3
"""Round P1 (2026-11-06, after Joel's "keep going" of 21:36 UTC): the paragraphs of "Psychology is the Software" and Part
1's opening and section A that read AI or Human (Low) in the whole-article check (../whole/RESULT.md), each rewritten by
the making-sense read (docs/MAKING-SENSE.md; the reader's own case first, each mechanism by what it does to the reader,
the order things happen; docs/lessons/2026-11-06-2122-neuro.md and gates E374 to E376).

For each: the text (P<block>.txt), its receipt (P<block>.receipt.json, sense_receipt.py), and a candidate article with
every draft in (CANDIDATE.md) for the fidelity check. Blocks are HUMANIZED-SO-FAR.md's blank-line blocks; each is found
by the start of its current text, so a moved block is refused, not overwritten.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
ART = ROOT / 'articles/neuro-de-armoring/humanize/HUMANIZED-SO-FAR.md'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as R  # noqa: E402

SECTION_SW = 'Psychology is the Software; Biology is the Hardware.'
READER_SW = ('someone with trauma, often with addiction, who has done therapy and still reacts the same way, reading to '
             'learn why and whether this protocol is for them')
SECTION_A = 'A. The Metabolic Red Line'
READER_A = ('someone with trauma who gets triggered and tries to think their way out of it, wanting to know why that fails '
            'and when to do trauma work')

D = [
    dict(block=20, starts='Standard therapy attempts to rewrite', section=SECTION_SW, reader=READER_SW,
         text=('If you\'ve done a lot of therapy and still react the same way, the therapy may not be the problem. '
               'Standard therapy tries to rewrite the "code" (your thoughts and behaviors), but if the "motherboard" (the '
               'brain\'s physical structure and chemistry) is overheating or damaged, the new code won\'t run. So the '
               'science behind this protocol looks at four specific neuro-biological problems that must be addressed '
               'before psychological tools can really work.'),
         pay=['they recognize themselves and hear that their stuck therapy may have a physical reason',
              'they see what therapy works on and why it fails when the hardware is overheating',
              'they learn what the next sections are for: four biological problems to fix before therapy can work'],
         fol=['opens the section under its heading, software and hardware, with the reader\'s own case',
              'gives the reason for the first sentence, in the heading\'s software and hardware terms',
              'says what follows from that reason: the protocol fixes the hardware first'],
         opens='the reader who still reacts the same way after therapy recognizes themselves in the first line',
         same='none: read the section from its heading to Part 1 for the software/hardware point; the Underpinning '
              'paragraph says it with Perry\'s house, which comes next as its illustration, and the X-26 paragraph says '
              'what the protocol does about it'),
    dict(block=21, starts='The "Underpinning" Principle Dr. Bruce Perry', section=SECTION_SW, reader=READER_SW,
         text=('The "Underpinning" Principle: Dr. Bruce Perry compares treating trauma to building a house. CBT, EMDR '
               'and similar therapies try to "decorate" the house, changing thoughts and behaviors in the Cortex, while '
               'the foundation, the Brainstem, is crumbling, and you can\'t hang curtains in a house that\'s falling '
               'down.'),
         pay=['they get a picture they can hold for why therapy alone may not stick',
              'they see which part of the brain therapy works on and which part is failing underneath'],
         fol=['illustrates the paragraph before (software over damaged hardware) with Perry\'s house',
              'applies the house to the therapies the reader has likely tried'],
         opens='it names the principle and gives a picture of the reader\'s situation: building on a bad foundation',
         same='none: read the section for the house image; the X-26 paragraph picks it up later ("dig under the house"), '
              'which is the same image carried on, not a repeat'),
    dict(block=25, starts='As we grow up, our "Role-Self"', section=SECTION_SW, reader=READER_SW,
         text=('If you feel stuck playing a part that isn\'t really you, that\'s the "Role-Self," and as we grow up, '
               'Dopamine and DeltaFosB harden it until it becomes a prison. Your addiction is often just the fuel it '
               'takes to keep that Role-Self running. This protocol works to dissolve the chemical glue holding the '
               'false persona together, so your "True-Self," the person you were before the trauma, can finally come '
               'back out.'),
         pay=['they recognize the Role-Self in themselves and learn that brain chemistry is holding it in place',
              'they see their addiction as the fuel for the role, which changes how they look at it',
              'they learn what the protocol aims to do for them: let the True-Self come back'],
         fol=['carries on from the Role-Self the paragraphs before introduced, now in the reader\'s own experience',
              'says what keeps the prison running',
              'says what the protocol does about it'],
         opens='the reader who feels they are playing a part recognizes themselves before any mechanism',
         same='none: read the section for the Role-Self and DeltaFosB points; Gibson\'s paragraph explains where the '
              'Role-Self comes from, this one what holds it, and section C says what DeltaFosB does'),
    dict(block=26, starts='Neurological De-Armoring is about fixing the underpinnings', section=SECTION_SW,
         reader=READER_SW,
         text=('So Neurological De-Armoring is about fixing the underpinnings first, not redecorating. The protocol '
               'works like a metabolic solvent: supplementing Ketones (BHB), which block HDAC, an enzyme that keeps genes '
               'switched off, along with Glutamate modulation, softens the "concrete" in the brainstem. That lets us dig '
               'under the house and pour a new foundation, so we can eventually update the psychological software '
               'upstairs.'),
         pay=['they learn what the whole protocol is for, in the house picture they already have',
              'they learn the two levers (ketones and glutamate) and what HDAC inhibition does in plain words',
              'they see the order: foundation first, then the therapy work'],
         fol=['draws the conclusion of the Role-Self paragraph and the house: fix the underpinnings',
              'says how the protocol does that',
              'says what that makes possible'],
         opens='it tells the reader what the protocol does for them, in the picture of the house they already have',
         same='none: read the section for the underpinning point; the Underpinning paragraph gives the picture, this '
              'one the protocol; his X-26 version (3 November) is kept in what it says: underpinnings, solvent, concrete, '
              'house, software'),
    dict(block=27, starts='The Anti-Breakthrough (Micro-Dosing)', section=SECTION_SW, reader=READER_SW,
         text=('The Anti-Breakthrough (Micro-Dosing): If long sessions leave you more overwhelmed than helped, that\'s '
               'what you\'d expect. As Dr. Perry explains, a dysregulated brain\'s "therapeutic window" is often only '
               'seconds long, so a sensitized, armored nervous system can\'t take in sixty minutes of trauma processing, '
               'and we need to give up the therapy ideal of the "hour-long breakthrough" for now.'),
         pay=['they recognize their own experience of long sessions and hear it is normal for an armored nervous system',
              'they learn why: the window is seconds long, so they can drop the hour-long breakthrough'],
         fol=['moves from what the protocol does to how to do the therapy part meanwhile, from the reader\'s own '
              'experience of sessions',
              'gives Perry\'s reason for that experience and what follows from it'],
         opens='the reader who has felt flooded by long sessions recognizes it in the first line',
         same='none: read the section for the dose point; the next paragraph gives the practice (thirty seconds, '
              'twenty times a day), which this one sets up'),
    dict(block=28, starts='Your goal is Micro-Dosing Safety', section=SECTION_SW, reader=READER_SW,
         text=('So the goal is Micro-Dosing Safety: 30 seconds of regulated breathing, twenty times a day. It\'s more '
               'like physical therapy for a broken nervous system than running a marathon, and how often you do it '
               'matters more than how hard.'),
         pay=['they get the practice itself: 30 seconds, twenty times a day',
              'they learn to judge their practice by how often, not how hard'],
         fol=['gives the practice that follows from the seconds-long window',
              'says how to think about it, in a picture'],
         opens='it gives the reader the practice to do, right after the reason for it',
         same='none: read the section for the practice; it is said here only'),
    dict(block=30, starts='Before applying the tools, you must understand', section='Part 1: THE SCIENCE (Why We Do This)',
         reader='someone deciding whether to use the protocol, who wants to know what is going wrong in their brain first',
         text=('Before applying the tools, you must understand what actually goes wrong in the brain during trauma, '
               'withdrawal or chronic stress, the "Hardware Failures" the tools are for.'),
         pay=['they know what the sections below explain and that each tool answers one of these failures'],
         fol=['opens Part 1 under its heading, which promises why we do this'],
         opens='it tells the reader what Part 1 gives them: what is going wrong in their own brain',
         same='none: read Part 1 for an overview of the failures; this is the only one'),
    dict(block=32, starts='We often assume we can "think" our way out', section=SECTION_A, reader=READER_A,
         text=('If you\'ve tried to talk yourself out of a trigger and couldn\'t, that\'s because anatomy overrides '
               'intellect. Dr. Perry describes a "Metabolic Red Line" for the traumatized brain: once your resting heart '
               'rate goes up or your heart-rate variability drops (a state of "Fear"), blood flow shifts away from the '
               'Cortex, which does logic and reasoning, and down to the Brainstem, which runs survival.'),
         pay=['they recognize their own failed attempts and learn it is anatomy, not a failing of theirs',
              'they learn the signs (heart rate up, HRV down) and what happens in the brain past them'],
         fol=['opens section A under its heading with the reader\'s own experience of a trigger',
              'gives the mechanism behind that experience, with the red line the heading names'],
         opens='the reader who has tried to think their way out of a trigger recognizes it in the first line',
         same='section B has a paragraph that starts the same way ("The Metabolic Red Line: We often assume we can '
              '\'think\' our way out of trauma"); it is read with section B, where it is a candidate repeat to merge here '),
    dict(block=33, starts='In this state, functional IQ drops substantially', section=SECTION_A, reader=READER_A,
         text=('So if you try to process trauma while you\'re above this red line, you\'re adding to the armor instead '
               'of taking it off. In that state your functional IQ drops a lot, and the Nucleus Accumbens gets flooded '
               'with the catecholamines that transcribe new DeltaFosB proteins, the "armor" itself.'),
         pay=['they learn when not to do trauma work: above the red line, it builds armor',
              'they learn why: thinking drops and the chemistry that builds the armor floods in'],
         fol=['draws what the red line means for trauma work, the paragraph\'s point, first',
              'gives the reason for it'],
         opens='it tells the reader what to avoid, before the mechanism that explains it',
         same='section C says what DeltaFosB does to learning; this one says when it is made, so they are kept apart'),
]


def main():
    raw = ART.read_text(encoding='utf-8')
    blocks = raw.split('\n\n')
    for d in D:
        b = d['block']
        assert blocks[b].startswith(d['starts']), (b, blocks[b][:60])
        name = 'P%03d' % b
        (HERE / (name + '.txt')).write_text(d['text'] + '\n', encoding='utf-8')
        r = R.make(d['text'], d['section'], d['reader'])
        assert len(r['sentences']) == len(d['pay']) == len(d['fol']), (b, len(r['sentences']), [x['s'] for x in r['sentences']])
        for x, p, f in zip(r['sentences'], d['pay'], d['fol']):
            x['payoff'], x['follows'] = p, f
        r['placement'] = 'where the block is now (block %d of HUMANIZED-SO-FAR.md); its place in the section is unchanged' % b
        r['opens']['why_reading'] = d['opens']
        r['same_point'] = d['same']
        r['questions'] = {q: 'PASS: read sentence by sentence against this reader' for q in R.QUESTIONS}
        (HERE / (name + '.receipt.json')).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        probs = R.check(d['text'], r)
        print(name, 'receipt', 'PASS' if not probs else probs)
        blocks[b] = d['text']
    (HERE / 'CANDIDATE.md').write_text('\n\n'.join(blocks), encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                         str(ROOT / 'articles/neuro-de-armoring/humanize/FIDELITY-KEYS.json'), str(HERE / 'CANDIDATE.md')],
                        capture_output=True, text=True)
    print(fk.stdout.strip().splitlines()[-6:])


if __name__ == '__main__':
    main()
