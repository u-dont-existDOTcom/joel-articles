#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 59's serotonin steps 1, 3, 4, 7 and 8 (B136, under "Act Now on
SS"), each a text of its own for Pangram, written his way after his round-48 version of steps 5 and 6 (lesson
bad-trips-2026-11-21d: sense first, Pangram after). Four rounds of the three fresh reads (reads/*-v1, v2, v3 and v5) came
before the check; the receipts cite the last round, of version five, and every sentence it marked in version six is kept
with why (the others were changed).

  python3 fill_receipts.py        then sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json, for each key
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

READ = 'v5-ss-steps'
ROUNDS = 'reads/*-v1-ss-steps.txt, *-v2-*, *-v3-* and *-v5-*'
NEED = ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md with the whole list as version five had it, '
        'its heading, the line before it and what it is for (reads/need-%s.txt; the earlier rounds: %s)' % (READ, ROUNDS))
HISF = ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, its seventeen ways (13 to 17 from his fix of '
        'steps 5 and 6), with version five one sentence a line (reads/his-%s.txt; the earlier rounds: %s)' % (READ, ROUNDS))
FIT = ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md, the universal version, with version five '
       '(reads/fit-%s.txt; the earlier rounds: %s)' % (READ, ROUNDS))
READER = ('the friend of someone who shows signs of serotonin syndrome (say MDMA on top of an antidepressant: twitching '
          'muscles, sweating, a racing heart), who has just read "So if you see any of these patterns, call medics." and '
          'now does these steps while help comes')
NEW = 'none: a new step, which the reader expects after the one before'

# first words of a sentence -> (payoff, follows, link words quoted from it, or None for a step's first sentence)
PAY = {
    'Serotonin syndrome comes from': ('they stop anything that adds serotonin, knowing why, and know the word for those things',
                                      'the first step after "call medics": stop more of the cause', None),
    'No more MDMA or other': ('they hold back MDMA and stimulants, and the three drugs people don\'t think of, each named with what it is',
                              'what "anything suspected of adding more" means, the obvious ones first', 'of course, but also'),
    "I'd hold off on even": ('they keep back their friend\'s own antidepressant until a doctor restarts it, and can tell the kinds by name',
                             'the hardest one to hold back, after the obvious ones', 'even'),
    'Ayahuasca and other harmala': ('they know ayahuasca and Syrian rue count as MAOIs too', 'the brews that belong with the MAOI just named', 'too'),
    "And don't forget the": ('they check for 5-HTP, St John\'s wort and SAM-e, which they might not think of', 'the last of what to stop', "And don't forget"),
    'When you call medics': ('they ask for an ambulance, knowing why', 'the line before the steps says to call medics; this says how', None),
    'Paramedics can start': ('they don\'t drive their friend themselves, even when it seems faster', 'the other half of why: what the ambulance brings', 'so'),
    'You can also call poison': ('they call poison control too, after the ambulance, knowing what it can and can\'t do', 'another call, after the first', 'also'),
    'Their twitching and tense': ('they see why cooling comes first: the heat from the muscles is the danger', 'what they are seeing while they wait', None),
    'So while you wait for': ('they cool their friend: a cool place, fewer clothes, a fan and damp cloths', 'what to do about the heat', 'So'),
    "If they're hot to the touch": ('they put wrapped ice packs where they cool fastest, knowing why there', 'the next way to cool, when they are hot', 'also'),
    'A cold bath would cool': ('they don\'t put a confused, seizing or very weak friend in a bath, knowing why', 'the way to cool they may think of next', 'but'),
    'And though fever reducers': ('they don\'t count on Tylenol or ibuprofen, knowing why it won\'t help', 'the other thing a helper reaches for', 'And though'),
    'Before the ambulance comes': ('they gather the bottles and packages for the ER', 'what to do with the rest of the wait', None),
    "Then I'd write down": ('they write down how much of each was taken and when, street drugs and supplements included', 'the next thing to bring', 'Then'),
    'Mark any dose they raised': ('they note a raised dose, knowing it can be what set this off', 'one detail of what they write', 'since'),
    'If you can take their': ('they write down the numbers with the time, knowing what the doctors do with them', 'the last thing to write down', 'If you can'),
    'While you wait, you might': ('they leave niacin and DMSO out, knowing why those come up and that niacin is unsafe', 'the remedies they may reach for while they wait', 'While you wait'),
    'For MDMA-related jaw': ('they know the one remedy he would consider, when, and where its amounts are', 'the remedy that does fit, after the two that don\'t', 'though'),
}
CHECKED = [
    {'point': 'fever reducers like Tylenol or ibuprofen do not help, because this heat is generated by their muscles',
     'found': ('Vanderbilt poison control (vumc.org/poison-control/node/842): the increased muscle activity is the primary '
               'cause of the hyperthermia, and drug-caused hyperthermia does not respond to ibuprofen or Tylenol; cooling '
               '"wet and windy" comes first'),
     'still_needed': 'yes: they don\'t give a fever reducer, which a helper reaches for when someone is this hot', 'fate': 'kept'},
    {'point': 'ice packs at the neck, armpits or groin, where big blood vessels run close to the skin',
     'found': ('Healthwise, Placement of Ice Bags for Heatstroke (healthlinkbc.ca/healthwise/placement-ice-bags-heatstroke): '
               'ice packs against the neck, under the arms and in the groin, where large blood vessels lie close to the '
               'skin surface'),
     'still_needed': 'yes: they put the packs where they cool fastest', 'fate': 'kept'},
    {'point': 'a raised dose can be enough to set off serotonin syndrome',
     'found': ('Mayo Clinic (mayoclinic.org/diseases-conditions/serotonin-syndrome/symptoms-causes/syc-20354758): serotonin '
               'syndrome can occur when you increase the dose of certain medications or start taking a new drug'),
     'still_needed': 'yes: they mark the raised dose, knowing why it matters', 'fate': 'kept'},
    {'point': 'ayahuasca and other harmala brews, like Syrian rue, act as MAOIs',
     'found': ('Herraiz and others, Food Chem Toxicol 2010 (pubmed.ncbi.nlm.nih.gov/20036304): harmaline and harmine in '
               'Peganum harmala (Syrian rue) seeds inhibit MAO-A; harmine and harmaline are also in ayahuasca\'s '
               'Banisteriopsis caapi'),
     'still_needed': 'yes: they keep Syrian rue or ayahuasca away from their friend', 'fate': 'kept'},
    {'point': 'an SSRI like Prozac or Zoloft, Effexor or another SNRI',
     'found': ('Mayo Clinic (same page): SSRIs include fluoxetine (Prozac) and sertraline (Zoloft); venlafaxine (Effexor) '
               'is an SNRI'),
     'still_needed': 'yes: they match the names on their friend\'s bottles', 'fate': 'kept'},
]
KEPT_HIS = {
    'No more MDMA or other': ('each drug comes with what it is (cough syrup, painkiller, antibiotic), and the friend needs '
                              'the names to check what was taken; the obvious ones come first, then "but also" the ones '
                              'people don\'t think of, so the run of names leads somewhere'),
    'For MDMA-related jaw': ('his own remedy and its condition, from his MDMA: Magnesium Alarm section, which gives the '
                             'amounts and the caution for impaired kidneys; the readers\' question about kidneys goes to him '
                             'on the page (card SS-STEPS)'),
}
KEPT_FIT = {
    'For MDMA-related jaw': ('the amounts stay in his MDMA: Magnesium Alarm section, linked here, above in this guide: '
                             'repeating his dosing in an emergency step would make the step longer than the reader can use'),
}
Q = {
    'Q1': ('PASS: each step opens on why the reader is reading it (serotonin syndrome comes from too much serotonin; the call '
           'the line before asked for; the heat the muscles make; the wait before the ambulance; the remedies they may '
           'reach for), and each term is explained where first used (serotonergic, SSRI, SNRI, harmala, the drugs)'),
    'Q2': 'PASS: every instruction is something the friend does, with what it is for',
    'Q3': 'PASS: which drugs and supplements, which body places, which numbers, which remedies',
    'Q4': ('PASS: serotonergic ("anything suspected of adding more"), the antidepressant kinds with their brand names, '
           'tramadol ("the painkiller"), linezolid ("the antibiotic"), harmala ("brews, like Syrian rue") explained where '
           'first used; niacin, DMSO and magnesium chloride are this guide\'s own remedies, in their sections'),
    'Q5': 'PASS: each sentence says how it follows ("of course, but also", "even", "too", "so", "also", "Then", "though")',
    'Q6': 'PASS: the order of the list as it stands (stop, his med, call, cool, his calm and fluids, gather, leave out)',
    'Q7': ('PASS: every fact is for a friend facing serotonin syndrome now; the hospital line, which the reader can\'t act '
           'on, is out (two needed reads; a proposal on his card, since it was in his guide)'),
    'Q8': 'PASS: the drugs together, the cooling ways together, what to write down together',
    'Q9': 'PASS: one step a numbered item, his way: the reason first or right after the act, said once',
}
STEPS = {1: 'step 1', 3: 'step 3', 4: 'step 4', 7: 'step 7', 8: 'step 8'}
PLACE = ('%s of the eight steps under "Act Now on SS" (B136), after the Hunter patterns and "So if you see any of these '
         'patterns, call medics." and before My Acute Rescue Remedies, with his steps 2, 5 and 6 as he wrote them; the '
         'hospital line ("Hospitals may use benzodiazepines, ...") is out, a proposal on his card')
WHY = {1: 'it tells the friend the first thing to do, stop anything that adds serotonin, and why',
       3: 'it tells the friend how to make the call the line before asked for, and why an ambulance',
       4: 'it tells the friend why the heat is the danger and how to cool their friend while help comes',
       7: 'it tells the friend what the ER will need, so they gather it while they wait',
       8: 'it tells the friend which of this guide\'s remedies to leave out, and the one he would consider'}


def first(s, body=''):
    for k in PAY:
        if s.startswith(k):
            return k
    for sent in re.split(r'(?<=[.!?])\s+', body):
        if s in sent and not sent.startswith(s):
            return first(sent)
    return None


def marks():
    rs = M.sentences((HERE / ('TEST-%s.txt' % READ)).read_text(encoding='utf-8').strip())
    his, fit = [], []
    for line in (HERE / 'reads' / ('his-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*([\d, ]+)\s*[—-]', line)
        if m:
            his.append({'s': rs[int(m.group(1)) - 1], 'difference': m.group(2).strip()})
    for line in (HERE / 'reads' / ('fit-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            if found:
                fit.append({'s': rs[int(m.group(1)) - 1], 'found': ', '.join(found)})
    t = (HERE / 'reads' / ('need-%s.txt' % READ)).read_text(encoding='utf-8')
    need = [rs[int(m.group(1)) - 1] for m in re.finditer(r'^\s*-\s*S(\d+):', t.split('UNNEEDED:', 1)[-1], re.M)]
    return his, fit, need


def fill(n):
    key = 'v6-ss%d' % n
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--section',
                    'Act Now on SS', '--reader', READER, '--out', str(out)], check=True, capture_output=True)
    d = json.loads(out.read_text(encoding='utf-8'))
    for s in d['sentences']:
        pay, fol, link = PAY[first(s['s'])]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link or NEW
    body = ' '.join(s['s'] for s in d['sentences'])
    d['checked'] = [c for c in CHECKED if any(w in body for w in (c['point'].split(',')[0][:18],))]
    d['placement'] = PLACE % STEPS[n]
    d['opens']['why_reading'] = WHY[n]
    d['same_point'] = ('none: read the section from its heading to the next (Serotonin Syndrome (SS)?, How to Check for SS, '
                       'Act Now on SS): the call to medics is in "So if you see any of these patterns, call medics." and '
                       'step 3 says how to make it')
    his, fit, need = marks()
    here = lambda s: s in body
    d['needed'] = {'reader': NEED, 'unneeded': need, 'kept': {}}
    d['his_fixes'] = {'reader': HISF, 'marked': [{'s': m['s'], 'difference': m['difference']} for m in his],
                      'kept': {m['s']: KEPT_HIS[first(m['s'], body)] for m in his if here(m['s'])}}
    d['fit'] = {'reader': FIT, 'marked': [{'s': m['s'], 'found': m['found']} for m in fit],
                'kept': {m['s']: KEPT_FIT[first(m['s'], body)] for m in fit if here(m['s']) and first(m['s'], body) in KEPT_FIT}}
    d['questions'] = Q
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    print(key, 'receipt check:', (r.stdout + r.stderr).strip().splitlines()[-1][:300] if (r.stdout + r.stderr).strip() else r.returncode)
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(n) for n in (1, 3, 4, 7, 8)))
