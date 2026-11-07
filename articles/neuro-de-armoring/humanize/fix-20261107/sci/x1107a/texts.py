"""Section B's science pass (2026-11-07): each changed paragraph as it would read with its claims corrected.

These are claim corrections, made as small edits to the article's paragraph (block 38: to Joel's own humanized version
of 7 November 01:00 UTC). They have not had a humanizing pass, so they go to no Pangram check (gate neuro-2026-11-07c);
the humanizing comes after he approves the claims. The sources are in ../SCIENCE-B37-B38.md and in SCIENCE-SECTION-B.md
beside this file, every link opened on 7 November.
"""
SATTLER = 'https://link.springer.com/article/10.1385/MN:24:1-3:107'
WANG = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12520249/'
ITOH = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11295041'
JHU = ('https://www.hopkinsmedicine.org/news/newsroom/news-releases/2025/09/'
       'scientists-find-potential-new-drug-target-for-psychiatric-and-neurological-disorders')
WOLOSKER = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC23961'
MATAIX = 'https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2599177'
SMITS = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3747985'
MORAN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1413952'
JALALI = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6333211'
AMICO = 'https://pubmed.ncbi.nlm.nih.gov/21504727/'

TEXTS = {
    'B37': (
        'The Mechanism: Excess Glutamate over-activates NMDA receptors, the doors on brain cells that glutamate unlocks, '
        'acting like a key stuck in the "On" position, so too much calcium pours into the cells. In extreme cases, like '
        'a stroke or a brain injury, that calcium overload kills them, which is what "excitotoxicity" means '
        '([Sattler & Tymianski, 2001](%s)). The anxiety, rage or "itchy brain" you feel in a glutamate storm is more '
        'likely the over-excitement itself than a sign your neurons are dying.' % SATTLER),
    'B38': (
        'The Signal Dial (GluD Receptors): So if NMDA is the spark, is anything else turning the signal up or down? Well '
        'according to a recent finding by Johns Hopkins researchers, GluD receptors, mainly known for helping build '
        'synapses, are also channels themselves, gates that let current into the cell, and what opens them is D-serine '
        '(one of the tools below) and GABA, the brain\'s main calming chemical, rather than glutamate '
        '([Wang, et al, 2025](%s)). Other researchers\' tests the year before found no sign of that, so it\'s still being '
        'argued over ([Itoh, et al, 2024](%s)). A mutation that causes cerebellar ataxia, a movement and balance '
        'disorder, leaves the channel leaking when it should be shut, and in schizophrenia GluDs seem to be less active '
        'than normal ([Johns Hopkins, 2025](%s)). Whether an armored state jams it too, on "High" as hyper-vigilance or '
        'on "Low" as apathy and schizotypy (odd, schizophrenia-like thinking), nobody has tested, so that part is a '
        'hypothesis.' % (WANG, ITOH, JHU)),
    'B39': (
        'D-serine may help therapy update old memories, because it switches on a spot on the NMDA receptor that this '
        'kind of learning needs ([Wolosker, et al, 1999](%s)), and it may also open the GluD channels. The drug that\'s '
        'actually been tested with exposure therapy (facing the feared thing in small, safe doses) is a different one, '
        'D-cycloserine (DCS), which works on that same spot, and across 21 trials with over 1,000 patients it gave '
        'exposure therapy a small boost ([Mataix-Cols, et al, 2017](%s)). It does not erase fear directly; it appears '
        'to strengthen whatever learning occurs during or after the exposure session. This is why session quality '
        'matters: if the exposure produces corrective learning and ends with reduced fear or mastery, DCS (and possibly '
        'D-serine also) may help consolidate that new memory; if the exposure is overwhelming or ends badly, it may '
        'consolidate the wrong association ([Smits, et al, 2013](%s)).' % (WOLOSKER, MATAIX, SMITS)),
    'B40': (
        'The Fix ("Lock, Stock, and Barrel"):The Vacuum (NAC): It works less like a vacuum than a brake. NAC gives the '
        'brain\'s support cells cystine (an amino acid), which they swap for glutamate, and in rat studies that '
        'glutamate outside the synapse trips a brake (the mGluR2/3 receptors) that cuts how much glutamate gets fired '
        'into the synapse ([Moran, et al, 2005](%s)).' % MORAN),
    'B41': (
        'The Lock (Zinc/Magnesium): Magnesium physically plugs the NMDA receptor\'s channel while the cell is at rest '
        '([Jalali-Yazdi, et al, 2018](%s)), and zinc mostly makes the channel open less often, with a weaker plug of '
        'its own ([Amico-Ruvio, et al, 2011](%s)), so less of the voltage gets through.' % (JALALI, AMICO)),
    'B42': (
        'The Repair (L-Serine): L-Serine is what the brain makes D-Serine from ([Wolosker, et al, 1999](%s)), so it can '
        'feed the spot on the NMDA receptor (and maybe the GluD channels) that D-serine switches on, and help therapy '
        'sessions that end with low fear and a sense of mastery stick better. The conversion isn\'t very efficient '
        'though, so some people take D-serine itself instead (more risk, but also more benefit).' % WOLOSKER),
    'B119': 'NAC: 1.8g – 2.4g (divided doses). *Turns down glutamate release.*',
    'B148': (
        'Use D-Serine for acute sessions where you need to "force" memory reconsolidation. '
        '[Best price from LifeLab](https://www.lifelabsupplements.com/d-serine). You should take it 45 minutes or so '
        'after taking PQQ & Ketones so that your brain is fueled when the D-serine starts working.'),
}
