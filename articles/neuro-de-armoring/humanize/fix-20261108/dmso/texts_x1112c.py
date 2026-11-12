"""SC-DMSO: DMSO in the Glutamate Shield, after his message of 2026-11-12 21:37 UTC ("i'm thinking we should include DMSO
in the protocol as well, i know it works wonders for many people", with Lu & Mattson 2001). DMSO is already in the
protocol in three places: the safety note at the top (block 7), the Fog table, an image (Scenario B: "Smell DMSO
(99.9%)", "Inhale deeply"), and the timeline ("If Foggy: Inhale DMSO + Drink BHB."). Nowhere does the text say what it
does. So a new item goes after Magnesium in "2. The Glutamate Shield (Anxiety)", the protocol's glutamate tools, with
his study at its strength and the other side (DMSO-PTSD.md).
"""
import re

LU = 'https://pubmed.ncbi.nlm.nih.gov/11421595/'
HANSLICK = 'https://pubmed.ncbi.nlm.nih.gov/19100327/'
BEFORE = 'The Dynorphin Bridge (Apathy / DAWS-pattern Void)'   # the new item goes just before this block
AFTER = 'Magnesium Glycinate: 400mg (Night).'                  # and just after this one
S1 = 'DMSO (99.9%): Smell it, as in the Fog table below.'
S2 = ('In rat brain cells in a dish, DMSO at 0.5 to 1.5% quickly turned down the signals glutamate sends through its NMDA '
      'and AMPA receptors, and the calcium they let in.')
S3 = 'It also kept glutamate from killing the cells ([Lu & Mattson, 2001](%s)).' % LU
S4 = ('In another lab, DMSO at 0.5%% and 1%% killed rat brain cells in a dish by itself, and injected into young mice, it '
      'set off widespread cell death in their brains ([Hanslick, et al, 2009](%s)).' % HANSLICK)
S5 = 'So keep it away from pregnancy and children.'
S6 = 'How much reaches your brain when you smell it hasn\'t been measured.'
S7 = ('No trial has tested it for anxiety or PTSD, so whether it helps rests on what people report, and many say it '
      'does.')
# the version the two fresh reads saw (needed/spdmso, his-fixes/spdmso), before their marks were acted on
READ = ['DMSO (99.9%): Smell it, as in the Fog table below.',
        'In rat brain cells in a dish, it quickly turned down the NMDA and AMPA glutamate signals and the calcium they let '
        'in, and kept glutamate from killing the cells (Lu & Mattson, 2001).',
        'In another lab, the same strengths killed rat brain cells in a dish on their own, and DMSO injected into young '
        'mice set off widespread cell death in their brains (Hanslick, et al, 2009), so keep it away from pregnancy and '
        'children.',
        'How much reaches your brain when you smell it hasn\'t been measured, and no trial has tested it for anxiety or '
        'PTSD, though many people say it helps.']
NEW = ' '.join([S1, S2, S3, S4, S5, S6, S7])
FOR = ('the reader with anxiety and glutamate storms learns what DMSO, which the protocol has them smell, does to the '
       'glutamate signals, how far that evidence goes, and who should keep away from it')


def plain(md):
    return re.sub(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', md)
