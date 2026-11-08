"""Science fixes for Parts 2 and 3: flag F-1 (block 97, protein and ketosis) and flag F-11 (blocks 106 and 115, potassium and
the KCNQ "brakes") of ../../fix-20261105/facts/FACTS.md (2026-11-08, after his answers of 15:08 UTC).

Each entry: the block's opening (to find it), the new Markdown, and what the paragraph is for (the needed read's WHAT IT
IS FOR). Sources in SCIENCE-P23.md beside this file. Only the sentences a flag touches change; the rest is copied from the
article by the builder, not retyped here, except where a sentence of the block is rewritten (lessons neuro-2026-11-08g
to i: no benefit the sources don't show, the answer kept where the argument holds, and what the reader is left to act on).
"""
import re

FROMENTIN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3636601'
BILSBOROUGH = 'https://pubmed.ncbi.nlm.nih.gov/16779921/'
BROWN = 'https://pubmed.ncbi.nlm.nih.gov/6314140/'
KUWABARA = 'https://pubmed.ncbi.nlm.nih.gov/12210395/'
CAMPESE = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6340902'

# (old sentence, new sentence) inside the block; the builder checks each old sentence occurs once
T = [
    dict(key='SP97', start='For the long run there\'s Strategy B',
         swap=[("Don't fill up on lean protein like chicken breast instead, because your body turns the extra protein into "
                "sugar through gluconeogenesis, and that keeps you out of ketosis.",
                "Don't fill up on lean protein like chicken breast instead, since your body can only take so much protein: "
                "past about a third of your calories it can make you sick ([Bilsborough & Mann, 2006](%s)), so the rest of "
                "your energy has to come from fat." % BILSBOROUGH)],
         for_='the reader on the long-run keto plan knows what to eat, what not to fill up on and why'),
    dict(key='SP106', start='The Science: Your neurons have "brakes" called KCNQ channels',
         swap=[('The Science: Your neurons have "brakes" called KCNQ channels that stop them from firing uncontrollably. '
                'These brakes run on Potassium ions. If you are low on potassium (common in high stress), your brakes fail. '
                'You can push the pedal (breathe), but the car won\'t stop.',
                'The Science: Your neurons have "brakes" called KCNQ channels, which keep a neuron from firing over and '
                'over by letting potassium out of it. Stress does lower the potassium in your blood, since adrenaline pushes it '
                'into your cells ([Brown, et al, 1983](%s)), but with less potassium outside them, nerve cells rest farther '
                'from firing, not closer ([Kuwabara, et al, 2002](%s)).' % (BROWN, KUWABARA))],
         for_='the reader understands what potassium has to do with an anxious, easily triggered nervous system, before '
              'the target and the foods'),
    dict(key='SP115', start='The Strategy: Eat 2 large potatoes',
         swap=[(' This saturates your cells, lowering your "resting voltage" so you become physically harder to trigger.', '')],
         for_='the reader knows how to reach the potassium target with food'),
]


def plain(md):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md))
