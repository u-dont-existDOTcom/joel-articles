#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 45's texts (sense_receipt.py), with the three fresh reads (reads/)
and each marked line's fate.

  python3 fill_receipts.py [KEY...] && python3 ../../../../tools/humanization/sense_receipt.py check TEST-K.txt TEST-K.receipt.json
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent

NEED = ('a fresh agent given tools/humanization/needed_read_brief.md with only the text, its heading and what it is for '
        '(reads/need-%s.txt)')
HISF = 'a fresh agent given tools/humanization/his_fixes_brief.md with the text, one sentence a line (reads/his-%s.txt)'
FIT = 'a fresh agent given tools/humanization/fit_read_brief.md, the universal version (reads/fit-%s.txt)'


def sents(key):
    return [x['s'] for x in json.loads((HERE / ('TEST-%s.receipt.json' % key)).read_text())['sentences']]


R = {}
# ---- the cyproheptadine step (B136, item 2) ----
CYP_CHECKED = [
    {'point': 'the case series the step links (PubMed 9696181, Graudins et al. 1998)',
     'found': ('five patients given 4-8 mg by mouth, three with no signs left within 2 h, the other two after a repeat dose; '
               '"it is unknown whether cyproheptadine modifies patient outcome"; "an adjunct to supportive care"'),
     'still_needed': ('yes: they know the evidence for it is case reports, which is how much they can lean on it; the '
                      'series itself goes (the three reads: no use to the reader, and it reads as proof)'),
     'fate': 'changed'},
    {'point': 'the systematic review the step links (PubMed 39791184, King & Rotella 2025)',
     'found': ('twelve reports from 2003 on (eleven case reports, one series), every one very low evidence and at high risk of '
               'bias; "a lack of evidence to support the efficacy of cyproheptadine"'),
     'still_needed': 'yes: they know the reports are too weak to show it works, so they do the other steps without waiting',
     'fate': 'changed'}]
R['cyp-c3'] = dict(
    payoffs=[
        ("they give cyproheptadine early if the person is fully alert and can swallow, and know why: it blocks the serotonin "
         "that's in excess", "step 1 stopped the serotonergic substances; this is the next thing to do", None),
        ("they know how far to lean on it: the evidence is case reports, which a recent review found too weak to show it "
         "works", "the limit that decides how much the step's remedy can be counted on, said first (lesson 19a)",
         "So far, the evidence for it"),
        ("they go on with the other steps (calling help, cooling) without waiting for it to work",
         "what the weak evidence means for what they do now", "I wouldn't wait")],
    checked=CYP_CHECKED,
    placement=("Suspected Serotonin Syndrome's immediate steps, step 2, after stopping all serotonergic substances and before "
               "calling emergency help and cooling"),
    why_reading="it tells someone whose friend shows serotonin toxicity what to give right after stopping the substances",
    same_point=("none: read Suspected Serotonin Syndrome from its heading to the next for cyproheptadine and its "
                "evidence: only this step names it"),
    questions={
        'Q1': 'PASS: the step leads; the limit of its evidence opens the next sentence',
        'Q2': 'PASS: give it, and don\'t wait on it: the helper\'s acts',
        'Q3': 'PASS: "fully alert and able to swallow", "case reports", "the other steps"',
        'Q4': 'PASS: "blocks serotonin receptors" says what it does in a line; no other term',
        'Q5': 'PASS: "since", "So far", "I wouldn\'t wait to see whether it does" turns on the review',
        'Q6': 'PASS: what to give, how far it goes, what to do meanwhile',
        'Q7': 'PASS: each bears on whether to give it and how much to count on it',
        'Q8': 'N/A: no list or group in it',
        'Q9': 'PASS: one idea a sentence'})
# ---- the MDMA paragraph after his second wife's story (B119) ----
MD_CHECKED = [
    {'point': 'the trial the paragraph links (PubMed 39546312, Atila et al. 2024)',
     'found': ('four placebo-controlled trials, 96 healthy volunteers given one 100 or 125 mg dose; low sodium in 30 (31%), all '
               'of them among the 81 whose drinking was not limited, none of the 15 whose drinking was'),
     'still_needed': ('yes: they know one normal dose can drop sodium when someone drinks a lot of plain water, so they '
                      'have them sip an electrolyte drink; the number goes (the needed read)'),
     'fate': 'changed'},
    {'point': 'the kidney review the paragraph linked (PubMed 27917269, Bora et al. 2016)',
     'found': ('acute kidney injury from rhabdomyolysis, malignant hypertension and necrotizing vasculitis; fatal cases from '
               'hyponatremia, hyperthermia and rhabdomyolysis'),
     'still_needed': ('yes: they know MDMA can injure the kidneys, which the next paragraph (B120) says with the same review '
                      'now linked on its "acute kidney injury"; here it went, so the paragraphs don\'t say it twice'),
     'fate': 'changed'}]
MD_Q = {
    'Q1': 'PASS: the last dose and what to do first; the water line opens on "Even a single normal dose", which bears on '
          'the reader\'s friend (lesson 19a); each sign with what to do',
    'Q2': 'PASS: get them to slow down and cool off, have them sip, call medics: the helper\'s acts',
    'Q3': 'PASS: "an electrolyte drink", "when they\'re thirsty", "keeps getting worse", "keeps coming back"',
    'Q4': 'PASS: no term left unexplained ("palpitations" a word the guide uses throughout)',
    'Q5': 'PASS: each sign leads to what to do; the seizure line turns on "And if"',
    'Q6': 'PASS: stop and cool, then water, then the signs from milder to the seizure',
    'Q7': 'PASS: each bears on a friend on MDMA with a tense jaw',
    'Q8': 'PASS: the sodium signs together, the potassium signs together',
    'Q9': 'PASS: one sign group a sentence'}
R['mdma-c3'] = dict(
    payoffs=[
        ("they stop the MDMA at the jaw tension and get their friend to slow down and cool off",
         "his paragraph before: magnesium is the first thing for jaw tension; this is what else to do", None),
        ("they have their friend sip an electrolyte drink when thirsty, not drink a lot of plain water, since with a lot of "
         "it even one normal dose can drop sodium", "the first thing that can go wrong next, what decides it first (lesson "
         "19a), then what to do", "If they drink"),
        ("they call medics when a headache keeps getting worse, the vomiting keeps coming back or the confusion grows",
         "the signs that sodium is already low, after the risk", "If a headache"),
        ("they call medics too when their muscles keep getting weaker or palpitations stronger, low potassium like his "
         "second wife's", "the second electrolyte, his story's", "Do the same"),
        ("they call medics right away for a seizure or a collapse, which overheating or MDMA toxicity can also cause",
         "the most serious signs last", "A seizure or collapse")],
    checked=MD_CHECKED,
    placement=("MDMA: Jaw Tension Is the Magnesium Alarm, after his second wife's story (B118) and before the kidney paragraph "
               "(B120)"),
    why_reading="it tells someone whose friend's jaw has tensed on MDMA what to do now and which signs mean medics",
    same_point=("B120 says MDMA can cause acute kidney injury, with the review linked there now; the guide's call list names a "
                "seizure and a collapse in general; this paragraph says them for MDMA with what each can mean"),
    questions=MD_Q)
R['mdma-c4'] = dict(
    payoffs=[
        R['mdma-c3']['payoffs'][0],
        ("they check whether a headache keeps getting worse, the vomiting keeps coming back or the confusion grows",
         "the first signs to watch, as his triage asks them", "Is a headache"),
        ("they call medics for those signs, since sodium may be low", "what those signs can mean, and what to do",
         "Their sodium"),
        ("they have their friend sip an electrolyte drink when thirsty, since with a lot of plain water even one normal dose "
         "raises that risk", "the same risk, what decides it first (lesson 19a), then what they can do", "If they've been"),
        ("they check whether their muscles are getting weaker or palpitations stronger", "the second electrolyte's signs",
         "Are their muscles"),
        ("they call medics for those too: low potassium, like his second wife's", "what they can mean", "That can mean"),
        ("they call medics right away for a seizure or a collapse, which overheating or MDMA toxicity can also cause",
         "the most serious signs last", "A seizure or collapse")],
    checked=MD_CHECKED, placement=None, why_reading=None, same_point=None,
    questions=dict(MD_Q, Q1='PASS: the last dose first; each sign group asked, then what it can mean and what to do; the '
                            'water line opens on "Even a single normal dose" (lesson 19a)'))
for f in ('placement', 'why_reading', 'same_point'):
    R['mdma-c4'][f] = R['mdma-c3'][f]
# ---- My Brain Feels Damaged's DMSO-and-bleeding paragraph (B106) ----
HIS = "his line (KEEP-AS-IS K4, his message of 2026-11-03 22:04 UTC)"
R['b106-c2'] = dict(
    payoffs=[
        ("they weigh skipping DMSO when a bleed is the worry", "his lines first: the limit that decides whether DMSO is for "
         "this reader at all (lesson 19a)", None),
        ("they know how strongly DMSO thins blood", HIS, 'none: ' + HIS),
        ("they know his experience and where he'd think again", HIS, 'none: ' + HIS),
        ("they don't stand down when DMSO makes their friend feel better", "what feeling better can hide, after the bleed "
         "lines", "They can feel better"),
        ("they call medics right away if any stroke check fails, before the window for treating a stroke closes",
         "what to do about it", "So if any")],
    checked=[],
    placement=("My Brain Feels Damaged, after the evidence for DMSO (B105) and before the section's numbered steps: his bleed "
               "lines, then what feeling better can hide"),
    why_reading="it tells someone who gave DMSO to a friend whose brain feels damaged whether DMSO suits a possible bleed",
    same_point=("none: read My Brain Feels Damaged from its heading to the next for DMSO and bleeding, and for "
                "feeling better hiding a stroke: only this paragraph says either (SF-8 cut the interactions line; KEEP-AS-IS C2)"),
    questions={
        'Q1': 'PASS: his bleed decision first; what feeling better can hide, then what to do',
        'Q2': 'PASS: "call medics right away": the helper\'s act',
        'Q3': 'PASS: "a clot or a bleed", "the checks above"',
        'Q4': 'PASS: no term left unexplained',
        'Q5': 'PASS: "So if any" turns on what feeling better can hide',
        'Q6': 'PASS: whether DMSO suits a bleed, then the checks that still decide',
        'Q7': 'PASS: each bears on DMSO for a friend who may have a clot or a bleed',
        'Q8': 'N/A: no list or group in it',
        'Q9': 'PASS: one idea a sentence'})


def reads_for(key):
    if key == 'cyp-c3':
        old = sents('cyp-c1'); S = sents('cyp-c3')
        return {
         'needed': {'reader': NEED % 'cyp-c1', 'unneeded': [old[2]], 'kept': {}},
         'his_fixes': {'reader': (HISF % 'cyp-c1') + '; and of cyp-c2 (reads/his-cyp-c2.txt: none marked)', 'marked': [
             {'s': old[0], 'difference': '4, 7', 'draft': 'cyp-c1'}, {'s': old[1], 'difference': '4', 'draft': 'cyp-c1'},
             {'s': old[2], 'difference': '7', 'draft': 'cyp-c1'}],
           'kept': {old[0]: ('they know when to give it: fully alert and able to swallow, the guide\'s own test in steps 6 and '
                             '8 of the same list, kept so the steps share one; the amount, which the guide never gave, goes '
                             'to him as a question'),
                    S[0]: ('they know when to give it and why: fully alert and able to swallow, the test steps 6 and 8 use; '
                           'the read of cyp-c2 marked nothing in this wording')}},
         'fit': {'reader': FIT % 'cyp-c1', 'marked': [{'s': old[2], 'found': 'MISREAD'}], 'kept': {}}}
    if key in ('mdma-c3', 'mdma-c4'):
        o1 = sents('mdma-c1'); o2 = sents('mdma-c2')
        his2 = (HERE / 'reads' / 'his-mdma-c2.txt')
        return {
         'needed': {'reader': NEED % 'mdma-c1', 'unneeded': [o1[5]], 'kept': {}},
         'his_fixes': {'reader': (HISF % 'mdma-c1') + ('; and of mdma-c2 (reads/his-mdma-c2.txt)' if his2.exists() else ''),
                       'marked': [{'s': o1[i], 'difference': d, 'draft': 'mdma-c1'}
                                  for i, d in ((0, '4'), (1, '7'), (2, '2, 7'), (3, '1, 5'), (6, '4'))] +
                                 [{'s': o2[i], 'difference': d, 'draft': 'mdma-c2'}
                                  for i, d in ((1, '5'), (2, '7, 9'), (3, '4, 9'), (4, '2, 3, 4, 7'), (5, '2, 6'))], 'kept': {}},
         'fit': {'reader': (FIT % 'mdma-c1') + '; and of mdma-c2 (reads/fit-mdma-c2.txt)', 'marked': [
             {'s': o1[1], 'found': "ANYWAY, CAN'T TELL"}, {'s': o1[2], 'found': "ANYWAY, CAN'T TELL"},
             {'s': o1[5], 'found': 'MISREAD'}, {'s': o1[6], 'found': "CAN'T TELL, FROM, MISREAD"},
             {'s': o2[2], 'found': "ANYWAY, CAN'T TELL, MISREAD"}, {'s': o2[3], 'found': "CAN'T TELL, MISREAD"},
             {'s': o2[4], 'found': "ANYWAY, CAN'T TELL"}, {'s': o2[5], 'found': 'MISREAD'}], 'kept': {}}}
    if key == 'b106-c2':
        S = sents('b106-c2'); old = sents('b106-c1')
        his = 'they know %s; his sentence (KEEP-AS-IS K4), his to change: what the reads found goes to him on a card'
        return {
         'needed': {'reader': NEED % 'b106-c1', 'unneeded': [S[2]], 'kept': {S[2]: his % 'his experience of DMSO and bleeding'}},
         'his_fixes': {'reader': HISF % 'b106-c1', 'marked': [
             {'s': S[0], 'difference': '4, 7', 'draft': 'b106-c1'}, {'s': S[1], 'difference': '3, 9', 'draft': 'b106-c1'},
             {'s': S[2], 'difference': '4, 7, 9', 'draft': 'b106-c1'}, {'s': old[4], 'difference': '2', 'draft': 'b106-c1'}],
           'kept': {S[0]: his % 'he would skip DMSO if a bleed is the worry', S[1]: his % 'how strongly DMSO thins blood',
                    S[2]: his % 'his experience of DMSO and bleeding'}},
         'fit': {'reader': FIT % 'b106-c1', 'marked': [
             {'s': S[0], 'found': "CAN'T TELL, MISREAD"}, {'s': S[1], 'found': 'FROM, MISREAD'},
             {'s': S[2], 'found': "CAN'T TELL, MISREAD"}],
           'kept': {S[0]: his % 'he would skip DMSO if a bleed is the worry', S[1]: his % 'how strongly DMSO thins blood',
                    S[2]: his % 'his experience of DMSO and bleeding'}}}


# ---- cyp-c4, after h55a ----
R['cyp-c4'] = dict(
    payoffs=[
        ("they give cyproheptadine right away if the person is fully alert and can swallow, and know why: it blocks the "
         "serotonin that's in excess", "step 1 stopped the serotonergic substances; this is the next thing to do", None),
        ("they know how far to lean on it: only case reports, with no one to compare against", "the limit that decides how "
         "much the step's remedy can be counted on, said first (lesson 19a)", "So far, the evidence for it"),
        ("they know what to expect (signs gone within two hours in three of five, longer in two) and keep going with the "
         "other steps meanwhile", "the finding the limit was about, with what it means for what they do now",
         "When doctors gave it")],
    checked=CYP_CHECKED[:1] + [dict(CYP_CHECKED[1], fate='kept', still_needed=(
        'yes: they know the evidence is case reports only, which the review counted; its link is on "case reports"'))],
    placement=R['cyp-c3']['placement'], why_reading=R['cyp-c3']['why_reading'], same_point=R['cyp-c3']['same_point'],
    questions=dict(R['cyp-c3']['questions'], **{
        'Q1': 'PASS: the step leads; the limit of its evidence opens the next sentence; the finding ends on what to do',
        'Q3': 'PASS: "fully alert and able to swallow", "case reports", "five patients", "within two hours"',
        'Q5': 'PASS: "since", "So far", "so keep going" turns on the finding',
        'Q6': 'PASS: what to give, how far the evidence goes, what it did and what to do meanwhile'}))
_reads_for_h55a = reads_for


def reads_for(key):
    if key != 'cyp-c4':
        return _reads_for_h55a(key)
    S = sents('cyp-c4')
    rt = [x.strip() for x in __import__('re').split(r'(?<=[.!?])\s+', (HERE / 'reads' / 'read-text-cyp-c4.txt').read_text().strip())]
    return {
     'needed': {'reader': NEED % 'cyp-c4' + ' (it read the text before the read against his fixes: reads/read-text-cyp-c4.txt)',
                'unneeded': [], 'kept': {S[2]: ('they know what to expect and keep going with the other steps meanwhile; '
                                               'the needed read of cyp-c4 found it needed, as against c1\'s bare series')}},
     'his_fixes': {'reader': HISF % 'cyp-c4' + ' (reads/read-text-cyp-c4.txt)', 'marked': [
         {'s': rt[0], 'difference': '4', 'draft': 'cyp-c4 as read'}, {'s': rt[3], 'difference': '6, 4', 'draft': 'cyp-c4 as read'}],
       'kept': {}},
     'fit': {'reader': FIT % 'cyp-c4' + ' (reads/read-text-cyp-c4.txt)', 'marked': [
         {'s': rt[2], 'found': "CAN'T TELL, FROM, MISREAD"}],
       'kept': {S[2]: ('they know what to expect, in hours; the second dose it read as an instruction is gone ("took longer"), '
                       'the limit before it says nobody could compare, and the dose, which the guide never gave, goes to him '
                       'as a question')}}}

# ---- mdma-c4b, after h55a ----
R['mdma-c4b'] = dict(
    payoffs=[
        R['mdma-c3']['payoffs'][0],
        ("they have their friend sip an electrolyte drink when thirsty, since with a lot of plain water even one normal dose "
         "raises the risk of low sodium", "what decides the risk first (lesson 19a), then the finding, then what he'd do",
         "If they're drinking"),
        ("they call medics when a headache gets worse and worse, often with throwing up or confusion", "how the low sodium "
         "just named shows up, and what to do", "A headache"),
        ("they call medics too for muscles getting weaker and weaker or a heart skipping beats", "the second electrolyte, "
         "his story's in the paragraph before", "The same goes for"),
        ("they get medics there right away for a seizure or a collapse", "the most serious signs last, as his paragraph "
         "before names the toxicity", "And a seizure")],
    checked=MD_CHECKED, placement=R['mdma-c3']['placement'], why_reading=R['mdma-c3']['why_reading'],
    same_point=R['mdma-c3']['same_point'],
    questions=dict(MD_Q, Q1='PASS: the last dose first; what decides the sodium risk before the finding (lesson 19a); each '
                            'sign group with what it can mean and what to do',
                   Q5='PASS: "so I\'d", "and it\'s time", "The same goes for", "And a seizure"'))
_reads_for_c4 = reads_for


def reads_for(key):
    if key != 'mdma-c4b':
        return _reads_for_c4(key)
    import re as _re
    rt = [x.strip() for x in _re.split(r'(?<=[.!?])\s+', (HERE / 'reads' / 'read-text-mdma-c4b.txt').read_text().strip())]
    base = _reads_for_c4('mdma-c3')
    note = ' (it read the text before the fixes below: reads/read-text-mdma-c4b.txt)'
    return {
     'needed': {'reader': NEED % 'mdma-c4b' + note, 'unneeded': [], 'kept': {}},
     'his_fixes': {'reader': HISF % 'mdma-c4b' + note + '; and of mdma-c1 and mdma-c2', 'marked':
                   [{'s': rt[3], 'difference': '1, 3, 4', 'draft': 'mdma-c4b as read'},
                    {'s': rt[4], 'difference': '2, 7', 'draft': 'mdma-c4b as read'}] + base['his_fixes']['marked'], 'kept': {}},
     'fit': {'reader': FIT % 'mdma-c4b' + note + '; and of mdma-c1 and mdma-c2', 'marked':
             [{'s': rt[2], 'found': 'MISREAD'}, {'s': rt[3], 'found': "ANYWAY, CAN'T TELL, MISREAD"}] + base['fit']['marked'],
             'kept': {}}}

# ---- cyp-c5, after h55c ----
R['cyp-c5'] = dict(
    payoffs=[
        ("they give cyproheptadine right away if the person is fully alert and can swallow, and know what it is: an old "
         "allergy medicine that also blocks serotonin receptors", "step 1 stopped the serotonergic substances; this is the "
         "next thing to do, the drug explained where it is first named", None),
        ("they know how far to lean on it (only case reports, nobody compared) and what it did in the one small series",
         "the limit first (lesson 19a), then the finding", "The evidence for it"),
        ("they keep cooling them down and get help now for moderate or severe signs, without waiting on it",
         "what the limit means for what they do now", "Keep cooling them down")],
    checked=R['cyp-c4']['checked'], placement=R['cyp-c3']['placement'], why_reading=R['cyp-c3']['why_reading'],
    same_point=R['cyp-c3']['same_point'],
    questions=dict(R['cyp-c3']['questions'], **{
        'Q1': 'PASS: the step leads; the limit of its evidence opens the next sentence; the last line opens on what keeps going',
        'Q4': 'PASS: cyproheptadine explained in the sentence that names it ("an old allergy medicine that also blocks serotonin receptors")',
        'Q5': 'PASS: "but in a small series" turns on the limit; "either way" on what the series can\'t settle',
        'Q6': 'PASS: what to give and what it is, how far the evidence goes, what to do meanwhile'}))
_reads_for_c4b = reads_for


def reads_for(key):
    if key != 'cyp-c5':
        return _reads_for_c4b(key)
    import re as _re
    rt = [x.strip() for x in _re.split(r'(?<=[.!?])\s+', (HERE / 'reads' / 'read-text-cyp-c5.txt').read_text().strip())]
    S = sents('cyp-c5')
    note = ' (it read the text before the fixes below: reads/read-text-cyp-c5.txt)'
    dose = ('they know when to give it and what it is; the amount, which the guide has never given, goes to him as a question '
            'on round 41\'s card (cyproheptadine is a prescription drug in many countries, and the dose is his call)')
    return {
     'needed': {'reader': NEED % 'cyp-c5' + note, 'unneeded': [rt[1]], 'kept': {
         S[0]: ('they know what cyproheptadine is where it is first named, a term a high-school graduate wouldn\'t know '
                '(gates E368 and E369); the mechanism clause the read found unneeded ("which is why it can help here") is cut')}},
     'his_fixes': {'reader': HISF % 'cyp-c5' + note, 'marked': [
         {'s': rt[0], 'difference': '7', 'draft': 'cyp-c5 as read'}, {'s': rt[1], 'difference': '8', 'draft': 'cyp-c5 as read'},
         {'s': rt[2], 'difference': '4', 'draft': 'cyp-c5 as read'}, {'s': rt[3], 'difference': '5, 4', 'draft': 'cyp-c5 as read'}],
       'kept': {rt[0]: dose, S[0]: dose}},
     'fit': {'reader': FIT % 'cyp-c5' + note, 'marked': [{'s': rt[2], 'found': 'MISREAD'}], 'kept': {}}}

# ---- mdma-c5, after h55c ----
R['mdma-c5'] = dict(
    payoffs=[
        ("they make the jaw tension their friend's last dose and get them to slow down and cool off, knowing more MDMA only "
         "adds to the toxicity", "his paragraph before: magnesium first for jaw tension, and the toxicity he names; this is "
         "what else to do", None),
        ("they keep an eye on how much plain water their friend drinks", "the first risk after the dose, in his first person",
         "I'd also watch"),
        ("they give an electrolyte drink to sip when thirsty if their friend is downing bottle after bottle, since even one "
         "normal dose can then drop sodium", "what decides the risk first (lesson 19a), then the finding, then what to do",
         "If they're downing"),
        ("they know how low sodium and low potassium tend to show up, past what MDMA does anyway",
         "the signs of the two risks, sodium's just named and potassium's from his paragraph before", "Low sodium tends"),
        ("they call medics for any of these, and get them there right away for a seizure or collapse", "one call for every "
         "sign above, the most serious last", "Call medics")],
    checked=MD_CHECKED, placement=R['mdma-c3']['placement'], why_reading=R['mdma-c3']['why_reading'],
    same_point=R['mdma-c3']['same_point'],
    questions=dict(MD_Q, Q1='PASS: the last dose and why first; what decides the sodium risk before the finding (lesson '
                            '19a); the signs, then one call', Q9='PASS: one idea a sentence; the two electrolytes\' signs '
                            'side by side in one'))
_reads_for_c5 = reads_for


def reads_for(key):
    if key != 'mdma-c5':
        return _reads_for_c5(key)
    import re as _re
    rt = [x.strip() for x in _re.split(r'(?<=[.!?])\s+', (HERE / 'reads' / 'read-text-mdma-c5.txt').read_text().strip())]
    S = sents('mdma-c5')
    note = ' (it read the text before the fixes below: reads/read-text-mdma-c5.txt)'
    return {
     'needed': {'reader': NEED % 'mdma-c5' + note, 'unneeded': [], 'kept': {}},
     'his_fixes': {'reader': HISF % 'mdma-c5' + note, 'marked': [
         {'s': rt[1], 'difference': '1, 4', 'draft': 'mdma-c5 as read'}, {'s': rt[2], 'difference': '2', 'draft': 'mdma-c5 as read'},
         {'s': rt[3], 'difference': '1, 2, 4', 'draft': 'mdma-c5 as read'}, {'s': rt[4], 'difference': '2, 6', 'draft': 'mdma-c5 as read'}],
       'kept': {}},
     'fit': {'reader': FIT % 'mdma-c5' + note, 'marked': [
         {'s': rt[0], 'found': 'ANYWAY'}, {'s': rt[1], 'found': "CAN'T TELL"}, {'s': rt[2], 'found': 'ANYWAY'},
         {'s': rt[3], 'found': "ANYWAY, CAN'T TELL"}],
       'kept': {}}}

def fill(key):
    p = HERE / ('TEST-%s.receipt.json' % key)
    r = json.loads(p.read_text(encoding='utf-8'))
    spec = R[key]
    assert len(r['sentences']) == len(spec['payoffs']), (key, len(r['sentences']), len(spec['payoffs']))
    for s, (pay, fol, link) in zip(r['sentences'], spec['payoffs']):
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link if link and (link.startswith('none:') or link in s['s']) else 'none: %s' % fol
    for f in ('checked', 'placement', 'same_point', 'questions'):
        r[f] = spec[f]
    r['opens']['why_reading'] = spec['why_reading']
    rd = reads_for(key)
    for f in ('needed', 'his_fixes', 'fit'):
        r[f] = rd[f]
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    import sys
    for k in sys.argv[1:] or R:
        fill(k)
        print('filled', k)
