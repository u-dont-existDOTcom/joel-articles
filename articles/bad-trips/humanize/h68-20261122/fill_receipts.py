#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 60's additions to the serotonin steps from his SS-ASKED answers:
step 2 with a line on getting cyproheptadine (his answer a) and step 8 with niacin's reason (c), the Syrian rue oil (e) and
magnesium's reason (d). Two rounds of the three fresh reads came first (reads/*-a1-ss-steps.txt, *-a2-ss-steps.txt); the
receipts cite the second, and every sentence it marked that is still in the text is kept with why.

  python3 fill_receipts.py        then sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

READ = 'a2-ss-steps'
NEED = ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md with the whole list, his versions and my two '
        'additions, its heading, the line before it and what it is for (reads/need-%s.txt; the round before: '
        'reads/need-a1-ss-steps.txt)' % READ)
HISF = ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, its seventeen ways, with the whole list one '
        'sentence a line (reads/his-%s.txt; the round before: reads/his-a1-ss-steps.txt)' % READ)
FIT = ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md, the universal version, with the whole list '
       '(reads/fit-%s.txt; the round before: reads/fit-a1-ss-steps.txt)' % READ)
NEW = 'none: a new step, which the reader expects after the one before'
PAY = {
    "And most people won't have it": ('they know they probably won\'t have it, so they go on with the other steps, and how it '
                                      'can be got', 'why not to wait on it, after "I wouldn\'t wait"', 'And'),
    "While you wait, you might think": ('they leave niacin and DMSO out, knowing why those come up here', 'the remedies they '
                                        'may reach for while they wait', None),
    'Niacin is actually unsafe': ('they know niacin is unsafe here and what it would do to their friend', 'why not niacin, '
                                  'the one just named', 'Niacin'),
    "I'd also leave out this guide's Syrian rue": ('they leave out the Syrian rue oil too, knowing it is different from the '
                                                   'brews of step 1 but unstudied with MDMA', 'the other remedy of this '
                                                   'guide they may reach for', 'also'),
    'Magnesium chloride is the one': ('they know magnesium is the remedy he would consider here, and why', 'the remedy that '
                                      'fits, after the ones to leave out', 'Magnesium chloride is the one'),
    "If they're fully alert and able to swallow, I'd": ('they give it by mouth when their friend can swallow, and know where '
                                                        'the amounts are', 'how to give it', "If they're fully alert"),
}
CHECKED = {
    'a3-ss2': [{'point': 'cyproheptadine needs a prescription in the US, and only some countries sell it without one',
                'found': ('his SS-ASKED answer of 2026-11-22 17:21 UTC: "they can\'t get it day or night unless it\'s sold '
                          'without an Rx at the pharmacy, which currently it is not in the US, but in other countries may '
                          'be. well, perahps via telehealth they could get it Rx\'d rapidly"'),
                'still_needed': 'yes: they don\'t go looking for it, and go on with the other steps',
                'fate': 'kept'}],
    'a3-ss8': [{'point': 'niacin at trip-ending doses can cause flushing, dizziness and low blood pressure',
                'found': ('NIH Office of Dietary Supplements, Niacin fact sheet for consumers (ods.od.nih.gov/factsheets/'
                          'Niacin-Consumer/): 30 mg or more of nicotinic acid can cause flushing and dizziness; doses of '
                          '1,000 mg a day or more can cause low blood pressure'),
                'still_needed': 'yes: they leave niacin out, knowing what it would do',
                'fate': 'kept'},
               {'point': 'many people with serotonin syndrome run low on magnesium',
                'found': ('Horn, Jordan, Davis and Thompson, "Serotonin syndrome: When medications don\'t mix", Nursing '
                          'Made Incredibly Easy 2013 (doi.org/10.1097/01.NME.0000432871.59839.f3), which he sent: "many '
                          'patients with serotonin syndrome are prone to episodes of hypomagnesemia"'),
                'still_needed': 'yes: they see why magnesium, of all the remedies, is the one to consider',
                'fate': 'kept'}],
}
KEPT_NEED = {
    'Niacin is actually unsafe': ('they leave niacin out even though this guide praises it, because they now know what it '
                                  'would do to their friend; readers asked why in every round, and his SS-ASKED answer (c) '
                                  'gives the reason'),
}
KEPT_HIS = {
    "While you wait, you might think": ('it read Human High by itself as part of step 8 (6f055cb9); DMSO\'s reason is a '
                                        'question to him on round 50 (I don\'t have one)'),
    'Magnesium chloride is the one': ('the finding is the reason he gave (his SS-ASKED answer d, with the nursing review he '
                                      'sent), and the sentence opens on its payoff, the remedy to consider'),
    "If they're fully alert and able to swallow, I'd": ('his remedy and its condition; the amounts and the kidney caution '
                                                        'are in his MDMA: Magnesium Alarm section, linked'),
}
KEPT_FIT = {
    "If they're fully alert and able to swallow, I'd": ('the amounts stay in his MDMA: Magnesium Alarm section, linked; '
                                                        'repeating his dosing here would repeat the guide, which he said '
                                                        'not to do ("make sure we are not repeating the same stuff")'),
}
Q = {
    'Q1': 'PASS: each sentence opens on why it is there: what they may reach for, the reason, the remedy that fits',
    'Q2': 'PASS: every instruction is something the friend does or leaves out, with why',
    'Q3': 'PASS: which remedies, which oil, which form of magnesium, where the amounts are',
    'Q4': 'PASS: the remedies are this guide\'s own, named by what the guide uses them for; harmala explained in step 1',
    'Q5': 'PASS: each sentence ties to the one before at its start ("And", "Niacin", "also", "Magnesium chloride is the one")',
    'Q6': 'PASS: what to leave out, then what to consider, then how',
    'Q7': 'PASS: every fact is one a reader asked about, answered from his answers',
    'Q8': 'PASS: the remedies to leave out together, then magnesium',
    'Q9': 'PASS: one point a sentence, his payoff first',
}
PLACE = {'a3-ss2': ('step 2 of the eight steps under "Act Now on SS" (B136), his own step with one line after it from his '
                    'SS-ASKED answer (a)'),
         'a3-ss8': ('step 8 of the eight steps under "Act Now on SS" (B136), the last, with his line on topical magnesium '
                    'at its end; a proposal on round 50, since it frames his answers in my words')}
WHY = {'a3-ss2': 'it tells the friend to give cyproheptadine early if they can, how little to count on it, and that they '
                 'probably won\'t have it',
       'a3-ss8': 'it tells the friend which of this guide\'s remedies to leave out while they wait, and the one he would '
                 'consider'}


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
        m = re.match(r'\s*-\s*S(\d+)(?:-S?(\d+))?[^:]*:\s*([\d, ]+)\s*[—-]', line)
        if m:
            for n in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1):
                his.append({'s': rs[n - 1], 'difference': m.group(3).strip()})
    for line in (HERE / 'reads' / ('fit-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            if found:
                fit.append({'s': rs[int(m.group(1)) - 1], 'found': ', '.join(found)})
    t = (HERE / 'reads' / ('need-%s.txt' % READ)).read_text(encoding='utf-8')
    need = []
    for m in re.finditer(r'^\s*-\s*S(\d+)(?: and S(\d+))?', t.split('UNNEEDED:', 1)[-1], re.M):
        for n in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1):
            need.append(rs[n - 1])
    return his, fit, need


def fill(key):
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    d = json.loads(out.read_text(encoding='utf-8'))
    for s in d['sentences']:
        if s.get('his'):
            continue
        pay, fol, link = PAY[first(s['s'])]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link or NEW
    body = ' '.join(s['s'] for s in d['sentences'])
    mine = ' '.join(s['s'] for s in d['sentences'] if not s.get('his'))
    d['checked'] = CHECKED[key]
    d['placement'] = PLACE[key]
    d['opens']['why_reading'] = WHY[key]
    d['same_point'] = ('none: read the section from its heading to the next (Serotonin Syndrome (SS)?, How to Check for SS, '
                       'Act Now on SS); this guide\'s remedies are named only here in the steps')
    his, fit, need = marks()
    here = lambda s: s in mine
    hiss = [x['s'] for x in d['sentences'] if x.get('his')]
    HIS_OWN = ('his own words: %s, kept as he wrote them' % (d.get('his_whose') or 'his line'))
    for t in hiss:
        for k in ('need', 'his', 'fit'):
            pass
    d['needed'] = {'reader': NEED, 'unneeded': need,
                   'kept': dict({s: KEPT_NEED[first(s, body)] for s in need if here(s) and first(s, body) in KEPT_NEED},
                                **{s: HIS_OWN for s in need if s in hiss})}
    d['his_fixes'] = {'reader': HISF, 'marked': [{'s': m['s'], 'difference': m['difference']} for m in his],
                      'kept': dict({m['s']: KEPT_HIS[first(m['s'], body)] for m in his
                                    if here(m['s']) and first(m['s'], body) in KEPT_HIS},
                                   **{m['s']: HIS_OWN for m in his if m['s'] in hiss})}
    d['fit'] = {'reader': FIT, 'marked': [{'s': m['s'], 'found': m['found']} for m in fit],
                'kept': dict({m['s']: KEPT_FIT[first(m['s'], body)] for m in fit
                              if here(m['s']) and first(m['s'], body) in KEPT_FIT},
                             **{m['s']: HIS_OWN for m in fit if m['s'] in hiss})}
    d['questions'] = Q
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-900:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in ('a3-ss2', 'a3-ss8')))
