#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 57's first try at the serotonin steps (B136, "Do this immediately
when serotonin toxicity is reasonably suspected:"), the whole list and its four pairs of steps, each a text of its own for
Pangram. One table of payoffs serves all five: the pairs are slices of the whole.

The three fresh reads read my first draft of the whole list (reads/read-text-g1-ss-steps-2.txt); every sentence of mine
they marked was changed before this text was made, so only his and the two his answers fix stay marked, each with why.

  python3 fill_receipts.py [KEY...]      then sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

READ = 'g1-ss-steps-2'
NEED = ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md with only the whole list as I first drafted '
        'it, its heading and what it is for (reads/need-%s.txt; the draft it read: reads/read-text-%s.txt)' % (READ, READ))
HISF = ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, the twelve ways, with the whole first draft one '
        'sentence a line (reads/his-%s.txt; the draft it read: reads/read-text-%s.txt)' % (READ, READ))
FIT = ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md, the universal version, with the whole first draft '
       '(reads/fit-%s.txt; the draft it read: reads/read-text-%s.txt)' % (READ, READ))
OWN2 = ('his own words: step 2 as he sent it in round 41 (card TEACH-CYP, his check cc5e6563, Human High 58 alone; '
        'OWNER-EDITS r41-cyp-his)')
C1 = ('his C1 answer a (chat, 2026-11-20 22:40 UTC) fixed this step\'s opening as "3. **Call emergency help and arrange '
      'transport.** Don\'t drive yourself." (OWNER-EDITS c1-ss-call-any, which the guide must contain exactly)')
NEW = 'none: a new step, which the reader expects after the one before'

# sentence -> (payoff, follows, link words quoted from it, or None for a new step)
PAY = {
    "Stop every suspected serotonergic substance, meaning anything that raises serotonin.": (
        'they stop giving anything that raises serotonin, the first thing to do, and know what "serotonergic" means',
        'the heading says do this as soon as serotonin toxicity is suspected, and the line before it ends "So if you see '
        'any of these patterns, call medics."; stopping more of the cause comes first', None),
    "If they're on an antidepressant (an SSRI, SNRI or MAOI), give them no more of it, and the same goes for tramadol, a painkiller, and for the antibiotic linezolid.": (
        'they check the medicines their friend takes and give no more of these, knowing what an SSRI, tramadol and '
        'linezolid are', 'it names the medicines the first sentence means', "If they're on"),
    "No more MDMA or stimulant redoses either, and none of the supplements 5-HTP, St John's wort or SAM-e.": (
        'they hold back the next dose of MDMA or a stimulant, and the supplements that raise serotonin',
        'after the medicines, the drugs and supplements that count too', 'either'),
    "Any harmala or ayahuasca-type MAOI counts too, and so does DXM cough syrup.": (
        'they give no ayahuasca brew or harmala, and no cough syrup with DXM in it',
        'the last of what counts, ending on the everyday one', 'counts too'),
    "Call emergency help and arrange transport.": (
        'they call for emergency help and get their friend on the way to a hospital',
        'his step 2 ends "I wouldn\'t wait to see whether it does before doing the other steps"; this is the next one',
        None),
    "Don't drive yourself.": (
        'they let the ambulance, or someone else, drive their friend', 'how to arrange the transport just named',
        'none: it says how to do the step just named, as his C1 answer fixed it'),
    "If you can't tell what your friend mixed, a poison control line can help you work out the combination, so call one too once emergency help is on its way.": (
        'when they don\'t know the mix, they call poison control as well, after emergency help, not instead of it',
        'another call to make, once the first is made', 'too once emergency help is on its way'),
    "Cool them down without holding up transport: if they're hot, get them into a cool room and take off their extra clothing.": (
        'they start cooling their friend while transport comes, with the room and the clothes first',
        'after the calls, what to do while help comes', 'without holding up transport'),
    "Then cool their skin with a fan and damp cloths, and put ice packs wrapped in cloth at their neck, armpits or groin.": (
        'the next ways to cool them, and where the ice packs go', 'the next part of cooling', 'Then'),
    "Don't put them in a cool bath, though, if they're confused, seizing or very weak, since they could slip under the water.": (
        'they don\'t use a bath to cool a friend who is confused, seizing or very weak, and know why',
        'the one way of cooling not to use, after the ways to use', 'though'),
    "If you're thinking of a fever reducer, it won't help here: fever reducers do not bring down heat generated by muscles working this hard, so keep cooling them from the outside.": (
        'they don\'t rely on a fever reducer, and keep cooling', 'the other thing a helper may reach for to bring heat down',
        "If you're thinking of"),
    "Keep the room calm and keep them still, since they're already overstimulated.": (
        'they make the room quiet and keep their friend from moving about, knowing why', 'the next step, after cooling',
        None),
    "That means no crowds or arguments around them, and no pacing or exercise to \"burn it off.\"": (
        'they keep crowds and arguments away, and stop pacing and exercise', 'what keeping calm and still means',
        'That means'),
    "If they feel a strong urge to keep moving, which is called akathisia, help them stay put anyway, because every bit of muscle work adds heat.": (
        'they hold their friend back from moving even when the urge is strong, and know the name for it',
        'the case where staying still is hard', 'anyway'),
    "It also raises their risk of rhabdomyolysis, where damaged muscle leaks into the blood and can hurt the kidneys.": (
        'they know the second danger of moving, explained, so they keep at it', 'the second reason, after the heat',
        'It also'),
    "Give fluids only if they're fully alert and not vomiting, and then just small sips of an electrolyte drink, like oral rehydration salts mixed in water.": (
        'they know when they can give a drink, which one, and how much', 'the next step, after keeping them still', None),
    "Someone who is confused, sleepy or vomiting, or at risk of a seizure, could breathe in whatever you give them, so don't force fluids, food, pills or charcoal on them.": (
        'they give nothing by mouth to a friend who is confused, sleepy, vomiting or at risk of a seizure, and know why',
        'the case the step before leaves out: when they can\'t give fluids', 'so'),
    "Gather what the ER will need: bring their pill bottles and packages, and write down exactly what they took.": (
        'they bring the bottles and packages and write down what was taken', 'the next step, while they wait', None),
    "For each substance, note the dose and when they took it, which dose was the last, and any dose they recently raised, then list any supplements or recreational drugs.": (
        'they know exactly what to write about what was taken', 'what "exactly what they took" means', 'For each substance'),
    "If you can take their temperature, pulse and blood pressure, write those down as well.": (
        'they add the body\'s numbers if they can take them', 'the last of what to write down', 'as well'),
    "While you wait, leave out niacin and DMSO.": (
        'they give neither niacin nor DMSO', 'the last step, for the time they wait', 'While you wait'),
    "Niacin may be this guide's trip killer, but it is unsafe with serotonin syndrome, and DMSO isn't one of these steps either.": (
        'they know why niacin comes up here, the trip killer they may reach for, and that it is unsafe now',
        'why the step before names those two', "this guide's trip killer"),
    "Once they're fully alert, I'd consider magnesium chloride by mouth instead, as in the MDMA section above, especially when MDMA has their jaw clenched or their muscles twitching.": (
        'they know the remedy he would consider instead, when, and where its amounts are', 'what to use in their place',
        'instead'),
}

CHECKED = [
    {'point': 'rhabdomyolysis, said as damaged muscle leaking into the blood and hurting the kidneys',
     'found': ('MedlinePlus (medlineplus.gov/ency/article/000473.htm): the breakdown of muscle tissue that releases muscle '
               'fiber contents into the blood, which are harmful to the kidney and often cause kidney damage'),
     'still_needed': 'yes: they know the second danger of moving, so they keep their friend still', 'fate': 'kept'},
    {'point': 'akathisia, said as a strong urge to keep moving',
     'found': ('MedGen (ncbi.nlm.nih.gov/medgen/C0392156): motor restlessness, often with an inner sense of restlessness '
               'and an urge to move'),
     'still_needed': 'yes: they see their friend\'s urge to move as part of the state and help them stay put', 'fate': 'kept'},
]

KEEP_NEED = {5: ('they know cyproheptadine is unproven, so they don\'t wait on it, which his next line says; ' + OWN2 +
                 ', kept as he sent it')}
KEEP_HIS = {6: OWN2 + '; he fixed this sentence\'s "it" himself in round 41, and "whether it does" is his',
            8: C1 + ', so the two stay two'}
KEEP_FIT = {4: (OWN2 + '; a friend without cyproheptadine goes on to the next steps, which his next line says not to wait '
                'on it for')}

SECTION_POINTS = ('Suspected Serotonin Syndrome (SS), from its heading to My Acute Rescue Hierarchy of Remedies: serotonin '
                  'syndrome overlaps with the branches above; the Hunter patterns; "So if you see any of these patterns, '
                  'call medics."; these eight steps')
PLACE = ('the steps under "Do this immediately when serotonin toxicity is reasonably suspected:" (B136), after the Hunter '
         'patterns and "So if you see any of these patterns, call medics." and before My Acute Rescue Hierarchy of Remedies, '
         'in place of the eight steps as they are; the hospital line ("Hospitals may use benzodiazepines, ...") is cut: '
         'the needed read of the list as it stands (../h62-20261120/reads/need-c1-ss-steps-1.txt) found the reader '
         'does nothing with it, and the call and transport steps already send them there')
KEYS = {
    'g1-ss-steps-2': ('the whole list', 'it tells the friend who has just read the signs the first thing to do: stop '
                      'anything that raises serotonin'),
    'g1a-ss12-2': ('steps 1 and 2', 'it tells the friend who has just read the signs the first thing to do: stop anything '
                   'that raises serotonin'),
    'g1b-ss34-2': ('steps 3 and 4', 'it tells the friend to call for help and get their friend to a hospital, the step '
                   'after stopping the cause'),
    'g1c-ss56-2': ('steps 5 and 6', 'it tells the friend, while help comes, to keep the room calm and their friend still, '
                   'and why'),
    'g1d-ss78-2': ('steps 7 and 8', 'it tells the friend what the ER will need from them, so they gather it while they '
                   'wait'),
}
Q = {
    'Q1': ('PASS: each step opens on what to do (stop, call, cool, keep still, give fluids only if, gather, leave out), and '
           'each term is explained where it is first used (serotonergic, SSRI as an antidepressant, tramadol, linezolid, '
           'akathisia, rhabdomyolysis, oral rehydration salts)'),
    'Q2': ('PASS: every instruction is something the friend does ("give them no more of it", "call one too", "help them '
           'stay put", "write those down"), with what it is for ("since they could slip under the water", "could breathe '
           'in whatever you give them")'),
    'Q3': ('PASS: which substances, which body places for the ice packs, which drink, what to write down and which numbers; '
           '"a poison control line" named instead of "it"'),
    'Q4': ('PASS: serotonergic ("anything that raises serotonin"), the antidepressants, tramadol ("a painkiller"), '
           'linezolid ("the antibiotic"), akathisia ("a strong urge to keep moving") and rhabdomyolysis ("damaged muscle '
           'leaks into the blood and can hurt the kidneys") explained where first used; niacin and magnesium chloride are '
           'the guide\'s own remedies, explained in their sections'),
    'Q5': ('PASS: each sentence says how it follows: "either", "counts too", "too once emergency help is on its way", '
           '"Then", "though", "If you\'re thinking of", "That means", "anyway", "It also", "so", "For each substance", "as '
           'well", "While you wait", "instead"'),
    'Q6': ('PASS: stop the cause, his med, call, cool, keep still, fluids, gather for the ER, what to leave out while '
           'waiting: the order of the list as it stands'),
    'Q7': ('PASS: every fact is for a friend facing serotonin syndrome now; the hospital line, which they can\'t act on, is '
           'cut'),
    'Q8': ('PASS: the medicines together, then the drugs and supplements, then the MAOI brews and cough syrup; the cooling '
           'ways together; the substance notes, then the body\'s numbers'),
    'Q9': 'PASS: one step a numbered item, each item\'s sentences one point each, as the reads asked',
}


def parse():
    rs = M.sentences((HERE / 'reads' / ('read-text-%s.txt' % READ)).read_text(encoding='utf-8').strip())
    S = lambda n: rs[n - 1]
    his = []
    for line in (HERE / 'reads' / ('his-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*([\d, ]+)\s*[—-]', line)
        if m:
            his.append({'s': S(int(m.group(1))), 'difference': m.group(2).strip(), 'n': int(m.group(1))})
    fit = []
    for line in (HERE / 'reads' / ('fit-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            if found:
                fit.append({'s': S(int(m.group(1))), 'found': ', '.join(found), 'n': int(m.group(1))})
    need = []
    t = (HERE / 'reads' / ('need-%s.txt' % READ)).read_text(encoding='utf-8')
    for line in t.split('UNNEEDED:', 1)[-1].splitlines():
        m = re.match(r'\s*-\s*S(\d+):', line)
        if m:
            need.append((int(m.group(1)), S(int(m.group(1)))))
    return his, fit, need


def fill(key):
    p = HERE / ('TEST-%s.receipt.json' % key)
    d = json.loads(p.read_text(encoding='utf-8'))
    for s in d['sentences']:
        if s.get('his'):
            continue
        pay, fol, link = PAY[s['s']]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link or NEW
    d['checked'] = [c for c in CHECKED if any(c['point'].split(',')[0] in s['s'] for s in d['sentences'])]
    what, why = KEYS[key]
    d['placement'] = '%s of %s' % (what, PLACE) if what != 'the whole list' else PLACE
    d['opens']['why_reading'] = why
    d['same_point'] = ('none: read the section from its heading to the next for the points (%s); the call to medics is in '
                       '"So if you see any of these patterns, call medics." and step 3 says how, which his C1 answer a made '
                       'agree' % SECTION_POINTS)
    his, fit, need = parse()
    d['needed'] = {'reader': NEED, 'unneeded': [s for n, s in need],
                   'kept': {s: KEEP_NEED[n] for n, s in need if n in KEEP_NEED}}
    d['his_fixes'] = {'reader': HISF, 'marked': [{'s': m['s'], 'difference': m['difference']} for m in his],
                      'kept': {m['s']: KEEP_HIS[m['n']] for m in his if m['n'] in KEEP_HIS}}
    d['fit'] = {'reader': FIT, 'marked': [{'s': m['s'], 'found': m['found']} for m in fit],
                'kept': {m['s']: KEEP_FIT[m['n']] for m in fit if m['n'] in KEEP_FIT}}
    d['questions'] = Q
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    for k in sys.argv[1:] or list(KEYS):
        fill(k)
        print('filled', k)
