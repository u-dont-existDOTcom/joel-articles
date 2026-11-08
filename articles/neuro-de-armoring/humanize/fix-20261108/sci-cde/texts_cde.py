"""Science fixes for sections C, D and E, and flag F-4 in Part 1 (2026-11-08, after his answers of 11:03 UTC).

Each entry: the block's opening (to find it), the new Markdown, and what the paragraph is for (the needed read's
WHAT IT IS FOR). Sources in SCIENCE-CDE.md beside this file.
"""
import re

PERRY = 'https://issuu.com/familyjusticegroup/docs/20230629_journal_final/s/27001732'
HERTZBERG = 'https://scholars.duke.edu/publication/759904'
VADOD = 'https://pubmed.ncbi.nlm.nih.gov/38408360/'
GOODWIN = 'https://www.psych.ox.ac.uk/publications/702415'
VERMETTEN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3233762'
SHIMAZU = 'https://escholarship.org/uc/item/4w889738'
WHITTLE = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3961057'
ROBISON = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8879420'
HE = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1193648'
SHAO = 'https://pubmed.ncbi.nlm.nih.gov/34228959/'
JEONG = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6820768'
CUNNANE = 'https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2016.00053/text'
CHOWANADISAI = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC2804159'
IYADURAI = 'https://ora.ox.ac.uk/objects/uuid:111fe953-8e08-465a-b490-a596b9f0e7e0'
JAMES = 'https://pubmed.ncbi.nlm.nih.gov/26133572/'
HOLMES10 = 'https://pubmed.ncbi.nlm.nih.gov/21085661/'

T = [
    dict(key='S24', start='We are operating on less than 1/24th',
         md='We are operating on about one-sixteenth of the relational density our biology requires ([Perry, 2023](%s)). '
            'The "Void" you feel is real. Once you have de-armored, you cannot simply return to a lonely life. You must '
            'aggressively engineer a "High-Density" social environment (A Tribe), or the brain will eventually reach for '
            'the armor again just to survive the cold.' % PERRY,
         for_='the reader understands why, after de-armoring, they need many more people around them'),
    dict(key='S47', start='Why Standard Meds Failed You',
         md='Why Standard Meds Failed You If you have tried SSRIs (antidepressants) and failed, you are not crazy. In a '
            'small trial of male combat veterans with severe, long-term PTSD, Prozac did no better than a placebo '
            '([Hertzberg, et al, 2000](%s)). Trials in veterans have been mixed since, and the VA still recommends '
            'sertraline and paroxetine ([VA/DoD, 2023](%s)), so they help some people, just not everyone. And the side '
            'effects are well-known, including anhedonia, zombification, and sexual dysfunction.' % (HERTZBERG, VADOD),
         for_='the reader who tried SSRIs and was let down understands it was not their failing, and what those drugs do '
              'and do not do'),
    dict(key='S48', start="Why don't these drugs work on calcified PTSD?",
         md="Why don't these drugs work for everyone? Nobody knows for sure. This protocol tries something else. The "
            "ketone BHB blocks enzymes called HDACs ([Shimazu, et al, 2013](%s)), and in mice that couldn't hold on to "
            "extinction learning (learning that a cue is now safe), an HDAC blocker made the new learning last "
            "([Whittle & Singewald, 2014](%s)). Whether ketosis does that in people hasn't been tested." % (SHIMAZU, WHITTLE),
         for_='the reader understands why the protocol uses ketones when SSRIs did not work for them'),
    dict(key='S50', start='The Fix (The Unlock):',
         md='The Fix (The Unlock): DeltaFosB does fade on its own, but [slowly](%s), and the same fears keep making '
            'more. So we use '
            '"System Reformats" (Shrooms/Iboga). Iboga raised GDNF, a growth factor that protects dopamine neurons, in '
            'rats ([He, et al, 2005](%s)), and one dose of psilocybin grew new connections in mouse brains that lasted a '
            "month ([Shao, et al, 2021](%s)). Whether either loosens DeltaFosB's hold hasn't been tested." % (ROBISON, HE, SHAO),
         for_='the reader understands why the guide turns to iboga and psilocybin for the "hardened" DeltaFosB state '
              'instead of waiting it out'),
    dict(key='S52', start='The Problem: "Brain Fog" is often a fuel crisis.',
         md='The Problem: "Brain Fog" may partly be a fuel problem. In brain scans of people with PTSD, some regions burn '
            'less glucose (sugar), and the less they burn, the worse the symptoms ([Jeong, et al, 2019](%s)).' % JEONG,
         for_='the reader understands whether their brain fog might be a fuel problem'),
    dict(key='S53', start='The Fix: If the brain cannot burn sugar',
         md='The Fix: If the brain is burning less sugar, we give it another fuel. Ketones are its backup fuel, and brains '
            'that take up less glucose (as in early Alzheimer\'s) still take up ketones normally ([Cunnane, et al, '
            '2016](%s)). PQQ made mouse cells build more mitochondria, the parts of the cell that burn fuel '
            '([Chowanadisai, et al, 2010](%s)); whether it does that in the human brain hasn\'t been shown.' % (CUNNANE, CHOWANADISAI),
         for_='the reader understands what ketones and PQQ are in the protocol for'),
    dict(key='S56', start='The Fix ("The Jammer"):',
         md='The Fix ("The Jammer"): Memories require visual processing power to be restored. If you occupy the '
            'Visual-Spatial Working Memory (e.g., playing Tetris) during the critical window *after* a flashback, the '
            'brain fails to "save" the visual details as strongly, and the memory flashes back less often. In the lab, a '
            'reminder of a day-old memory followed by Tetris cut its flashbacks, and neither one alone did '
            '([James, et al, 2015](%s)).' % JAMES,
         for_='the reader decides whether to play Tetris after a flashback, and knows what it does'),
    dict(key='S57', start='Instead of Tetris (which requires app/phone)',
         md='Instead of Tetris (which requires app/phone), you can use the "Color-Path Connect" method. It hasn\'t been '
            'tested the way Tetris has, but it is built on the same idea: it makes your brain map 3D space, which '
            'competes with the visual "saving" of a traumatic memory. Skip counting and word games, though: in the lab, '
            'a verbal quiz game after a trauma film led to more flashbacks, not fewer ([Holmes, et al, 2010](%s)).' % HOLMES10,
         for_='the reader decides whether to use the no-phone alternative to Tetris, and what to avoid'),
]


def plain(md):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md))
