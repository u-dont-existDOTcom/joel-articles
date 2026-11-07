"""His three answers of 2026-11-07 13:10 UTC that needed another version, as the paragraphs would read.

SB-38 and SB-40 he marked revise; SB-37 he approved with a question its last sentence didn't answer. None of these has
had a humanizing pass, so none goes to Pangram (gate neuro-2026-11-07c): that comes after he settles the claims.
"""
SATTLER = 'https://link.springer.com/article/10.1385/MN:24:1-3:107'
BOYLE = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3670432'
WILSON = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4721288'
WANG = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12520249/'
ALLEN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10840383/'
MORAN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1413952'

TEXTS = {
    'B37b': (
        'The Mechanism: Excess Glutamate over-activates NMDA receptors, the doors on brain cells that glutamate '
        'unlocks, acting like a key stuck in the "On" position, so too much calcium pours into the cells. In extreme '
        'cases, like a stroke or a brain injury, that calcium overload kills them, which is what "excitotoxicity" '
        'means ([Sattler & Tymianski, 2001](%s)). What you feel from a glutamate storm depends on which circuit is '
        'firing too hard, and under stress the rise reaches the amygdala, the part of the brain that flags threats '
        '([Wilson, 2015](%s)), so the feeling it produces is threat: anxiety, rage, the "itchy brain", not pleasure. '
        'Block the NMDA receptors there and anxious behaviour goes down in animals ([Boyle, 2013](%s)).'
        % (SATTLER, WILSON, BOYLE)),
    'B38b': (
        'The Signal Dial (GluD Receptors): So if NMDA is the spark, is anything else turning the signal up or down? '
        'Well according to a recent finding by Johns Hopkins researchers, GluD receptors, until now known for helping '
        'build synapses, are channels in their own right, and what opens them is D-serine (one of the tools below) and '
        'GABA, the brain\'s calming chemical, rather than glutamate ([Wang, et al, 2025](%s)). What has been measured '
        'in people so far all points one way: the channel sticks open and leaks, so the synapse never gets quiet. '
        'That is what the mutation behind one inherited ataxia does, and a gene variant that raises the risk of '
        'schizophrenia does the same ([Allen, et al, 2023](%s)). So my guess for the armored state is that it jams the '
        'dial the same way, stuck part-way on, which is what hyper-vigilance would be at the level of one synapse: a '
        'floor the signal can\'t drop below. Nobody has tested that in trauma yet, and it can be tested, because a '
        'drug that shuts these leaking channels already works in the lab.' % (WANG, ALLEN)),
    'B40b': (
        'The Fix ("Lock, Stock, and Barrel"):The Brake (NAC): NAC gives the brain\'s support cells cystine (an amino '
        'acid), which they swap for glutamate, and in rat studies that glutamate outside the synapse trips a brake '
        '(the mGluR2/3 receptors) that cuts how much glutamate gets fired into the synapse '
        '([Moran, et al, 2005](%s)).' % MORAN),
    'B119b': 'NAC: 1.8g – 2.4g (divided doses). *Turns down glutamate release.*',
}
