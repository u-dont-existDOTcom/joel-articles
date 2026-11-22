#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 44's texts (sense_receipt.py), with the three fresh reads
(reads/) and each marked line's fate (READS, filled once the reads were in).

  python3 fill_receipts.py && for each: python3 ../../../../tools/humanization/sense_receipt.py check TEST-K.txt TEST-K.receipt.json
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
HISLINK = 'none: his sentence, the next in his paragraph'

Q_EVID = {'Q2': 'N/A: an evidence paragraph, no instruction in it', 'Q8': 'N/A: no list or group in it'}

R = {}
R['dmso-h3'] = dict(
    payoffs=[
        ("they know DMSO calmed psychiatric inpatients in 1967, anxious ones among them, and that PTSD hasn't been tested",
         "the evidence part of the profile opens after his experience and the ozonated-charcoal water", None),
        ("they know people are given DMSO routinely, so it has a long record in humans", "a second line of human use",
         "It's routinely used in humans"),
        ("they know more DMSO brought more side effects, so they keep the dose down", "the transplant use's downside",
         "too much DMSO"),
        ("they know young brains are the ones the research found at risk, even at a low dose", "a second risk, to brain cells",
         "Young brains may be at risk from DMSO"),
        ("they weigh the mouse finding as uncertain for people", "it weighs the finding before it", "mouse research")],
    checked=[{'point': 'Ramirez & Luza 1967 (Annals of the New York Academy of Sciences 141: 655-667)',
              'found': ('42 inpatients in Lima, five with severe anxiety states and four with obsessive-compulsive neurosis among '
                        'them; in the anxiety states one or two vials a day "caused decrease in the anxiety symptoms"; no PTSD '
                        '(the neuro lane read it in full: articles/neuro-de-armoring/humanize/fix-20261108/dmso/DMSO-PTSD.md)'),
              'still_needed': 'yes: they know DMSO has calmed anxious people, which is what a bad trip brings',
              'fate': 'changed'}],
    placement=("the DMSO section, after his experience and the ozonated-charcoal water, before Side effects: what the research "
               "says it does, then its risks"),
    why_reading="it tells someone weighing DMSO that it calmed psychiatric inpatients, anxious ones among them",
    same_point="none: read the DMSO section from its heading to the next for the 1967 study and the anxiety point",
    questions=dict(Q_EVID, **{
        'Q1': 'PASS: each finding leads its sentence; the anxiety patients said where the study is',
        'Q3': 'PASS: "patients with severe anxiety", "stem cell transplants", "mice up to a month old"',
        'Q4': 'PASS: no term left unexplained',
        'Q5': 'PASS: "and that included", "though", "too much DMSO", "Young brains ... though"',
        'Q6': 'PASS: the human uses, the side effects of too much, the risk to young brains, how far it carries',
        'Q7': 'PASS: each bears on whether and how to use DMSO in a trip',
        'Q9': 'PASS: one finding a clause'}))
R['remedies-c2'] = dict(
    payoffs=[
        ("they know what the entry is and that creatine is good for the brain", "the next stabilizer after humic acid, another "
         "thing to smell that his sniffer now holds", None),
        ("they know smelling creatine helps the brain while high on psychedelics, in the author's experience",
         "the heading's claim said as his experience", "Smelling creatine"),
        ("they smell it and don't snort it", "the misreading his readers make, answered where it would happen",
         "When I say smell, I mean smell"),
        ("they know what it does for them: bliss, and posture", "what smelling it does", "It's very blissful"),
        ("they know why it's good for the brain, and that it works like DMSO", "the brain health the entry opens on",
         "Like DMSO"),
        ("they know the next entry is mango leaf tea, and that it calms without ending the trip", "another thing to smell", None),
        ("they brew it and smell it hot", "the action first, as in his entries", "Brew mango leaf tea"),
        ("they know what it does: relaxes and is blissful", "why they'd smell it", "It's a super relaxing herbal remedy")],
    checked=[],
    placement=("Mental Stabilizers That Don't Abort the Trip, after Humic Acid and before the essential oils: the three things "
               "of his sniffer's formula that can be bought on Amazon, which the sniffer's last sentence now names"),
    why_reading="it tells someone looking for something to smell in a hard trip that creatine calms and helps the brain",
    same_point=("none: the sniffer's paragraph names both as now in its formula, which is said there once; read the part from "
                "its heading to the next for creatine and mango leaf tea"),
    questions={
        'Q1': 'PASS: each entry opens on what to do or what it does; the snorting misreading answered right after "smelling"',
        'Q2': 'PASS: "Brew mango leaf tea and smell it while it\'s hot": the reader\'s acts',
        'Q3': 'PASS: creatine, smell not snort, mango leaf tea while hot',
        'Q4': 'PASS: "neuroprotective" and "neuroinflammation" as his words beside DMSO, which the guide explains',
        'Q5': 'PASS: "When I say smell", "Like DMSO", "It\'s a super relaxing" each turn on the line before',
        'Q6': 'PASS: what it is, how to take it, what it does, why',
        'Q7': 'PASS: each line bears on what to get or use in a hard trip',
        'Q8': 'PASS: both are things to smell that calm a trip without ending it, in this part',
        'Q9': 'PASS: one thing a sentence'})
R['sniffer-c1'] = dict(
    payoffs=[("they know what the sniffer does: peace for 30-60 minutes even sober", "his entry opens the part", None),
             ("they know people say it saved them from crippling anxiety", "his", HISLINK),
             ("they know where to post or read about it", "his", HISLINK),
             ("they know on ayahuasca it also opens the heart", "his", HISLINK),
             ("they know it made the love part reliable for him", "his", HISLINK),
             ("they know it turns ayahuasca into loveyhuasca", "his", HISLINK),
             ("they know they can get it from him", "his", HISLINK),
             ("they know the formula now has creatine and mango leaf tea, so with the sniffer they need nothing else",
              "what is in what they'd get from him", "It's a bunch of stuff in the formula"),
             ("they know which three things in it to buy on Amazon without the sniffer: the next three entries",
              "for those without it, his original line", "If not")],
    checked=[],
    placement="the part's first entry; its last sentence leads into the three entries after it (humic acid, creatine, mango leaf tea)",
    why_reading="it tells someone in a hard trip that this stick calms people within minutes, even sober",
    same_point="none: read the part for the sniffer's formula; creatine and mango leaf tea have their own entries after it",
    questions={
        'Q1': 'PASS: his entry opens on what the sniffer does; the formula line says first what changed',
        'Q2': 'N/A: his entry tells what it does; the buying is said as a choice',
        'Q3': 'PASS: "creatine and mango leaf tea", "three of the things in it"',
        'Q4': 'N/A: no new term',
        'Q5': 'PASS: "so if you have one", "If not"',
        'Q6': 'PASS: what it is, where to get it, what is in it, what to buy without it',
        'Q7': 'PASS: each bears on getting it or its parts',
        'Q8': 'N/A: no list',
        'Q9': 'PASS: one step a sentence'})
B105_PAY = [
    ("they know why the author gives DMSO first for a brain that feels damaged", "the checks and call line before it", None),
    ("they know how far the evidence goes", "it weighs the belief before it", HISLINK),
    ("they know DMSO limited brain damage after a stroke in animals", "the first study", HISLINK),
    ("they know the human evidence is small", "the human studies", HISLINK)]
B105_Q = dict(Q_EVID, **{
    'Q1': 'PASS: his frame leads; where the finding was made closes the sentence',
    'Q3': 'PASS: "rat brain cells in a dish"',
    'Q5': 'PASS: "But more relevant" turns from strokes to the overdose case',
    'Q6': 'PASS: belief, how far, animals, people, the overdose case',
    'Q7': 'PASS: each study bears on trusting DMSO for brain damage',
    'Q9': 'PASS: one finding a clause'})
R['brainev-m3'] = dict(
    payoffs=B105_PAY + [("they know DMSO calmed the excitotoxicity an overdose brings, and that it was in rat cells in a dish",
                         "the overdose case after the strokes, his frame", "But more relevant to the drug overdose issue")],
    checked=[], placement=("My Brain Feels Damaged, the evidence paragraph after the checks and the call line: his sentence with "
                           "where the study was done added"),
    why_reading="it tells someone deciding whether to trust DMSO for a damaged-feeling brain that the author rates it first, and on what",
    same_point="none: Lu & Mattson is said here only (turn 43); read the section for the study",
    questions=dict(B105_Q, Q4='PASS: his term, as in his version (he kept it: 5b09da6c, Human High)'))
R['brainev-m4'] = dict(
    payoffs=B105_PAY + [("they know what excitotoxicity is (glutamate overload that kills brain cells), that DMSO calmed it, and "
                         "that it was in rat cells in a dish", "the overdose case after the strokes, his frame",
                         "But more relevant to the drug overdose issue")],
    checked=[], placement=R['brainev-m3']['placement'].replace('where the study was done added',
                                                                'the term said as what it is, with "via" as he did'),
    why_reading=R['brainev-m3']['why_reading'], same_point=R['brainev-m3']['same_point'],
    questions=dict(B105_Q, Q4='PASS: "excitotoxicity, the glutamate overload via NMDA and AMPA receptors that kills brain cells"'))
CP_CHECKED = [{'point': 'the three studies the guide links (PubMed 19904216, 17000906, 20035720)',
               'found': ('19904216: rats given DMSO into the belly for three days before the artery was tied lost heart muscle '
                         '4.46% against 18.75%, pretreatment only; 17000906: tissue factor and clots in arteries, mice and human '
                         'cells; 20035720: human platelets'),
               'still_needed': 'yes: they know what the research behind the author\'s story shows, and in what', 'fate': 'kept'}]
CP_Q = dict(Q_EVID, **{
    'Q3': 'PASS: "rats given it for three days before a heart attack", "human platelets ... in a dish"',
    'Q4': 'PASS: "platelets (the blood cells that start clots)"',
    'Q6': 'PASS: each finding beside what it means for the friend',
    'Q7': 'PASS: each bears on whether DMSO is worth using for chest pain',
    'Q9': 'PASS: one finding a sentence'})
R['cp-c5'] = dict(
    payoffs=[("they know the research is only animals and dishes, and that it points the way his story does",
              "his angina story before it: the question it leaves", None),
             ("they know DMSO protected heart muscle in rats given it for days before, and not after the attack started",
              "the first finding", "Rats given it"),
             ("they know why clotting bears on a heart attack, and that DMSO slowed it in mice and human platelets",
              "the second finding", "And since most heart attacks come from a clot")],
    checked=CP_CHECKED, placement="Chest Pain and Injury, after his angina story and before what to do",
    why_reading="it answers whether the author's angina story was just him, for someone deciding on DMSO for a friend's chest pain",
    same_point="none: read the section from its heading to the next for the heart evidence",
    questions=dict(CP_Q, Q1='PASS: it opens on the question his story leaves the reader with', Q5='PASS: "that way", "And since"'))
R['cp-c6'] = dict(
    payoffs=[("they know why clotting bears on a heart attack and that DMSO slows it, in mice and human platelets",
              "his angina story before it; the reader's worry first", None),
             ("they know DMSO protected heart muscle in rats given it before, and not after the attack started",
              "the second finding", "In rats given it"),
             ("they know how far the research goes", "it weighs the two findings", "That's all animal and lab-dish research")],
    checked=CP_CHECKED, placement=R['cp-c5']['placement'], why_reading=("it tells someone whose friend has chest pain that DMSO "
                                                                         "slows clotting, which is what blocks the artery"),
    same_point=R['cp-c5']['same_point'],
    questions=dict(CP_Q, Q1='PASS: it opens on the clot, the reader\'s worry', Q5='PASS: "and DMSO slows clotting", "though", "That\'s all"'))

READS = {}   # filled once the reads were in: {key: {'needed': ..., 'his_fixes': ..., 'fit': ...}}


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
    if key in READS:
        for f in ('needed', 'his_fixes', 'fit'):
            r[f] = READS[key][f]
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    import sys
    for k in sys.argv[1:] or R:
        fill(k)
        print('filled', k)


# ---- turn 44's final texts, after the reads of the earlier drafts (reads/), each marked line changed or kept with why ----
import copy as _copy

def _sents(key):
    return [x['s'] for x in json.loads((HERE / ('TEST-%s.receipt.json' % key)).read_text())['sentences']]

NEED = 'a fresh agent given tools/humanization/needed_read_brief.md with only the text, its heading and what it is for (reads/need-%s.txt)'
HISF = 'a fresh agent given tools/humanization/his_fixes_brief.md with the text, one sentence a line (reads/his-%s.txt)'
FIT = 'a fresh agent given tools/humanization/fit_read_brief.md, the universal version (reads/fit-%s.txt)'

R['dmso-h4'] = _copy.deepcopy(R['dmso-h3'])
R['dmso-h4']['payoffs'][3] = ("they know children's brains are the ones the research found at risk, even at a low dose",
                              "a second risk, to brain cells", "Children's brains may be at risk from DMSO")
R['remedies-c4'] = _copy.deepcopy(R['remedies-c2'])
R['remedies-c4']['payoffs'] = (R['remedies-c2']['payoffs'][:2] +
    [("they hold the open container near the nose and breathe in gently", "how to smell it, right after what it does",
      "Hold the open container"),
     ("they don't snort it", "the misreading his readers make, answered after the how", "When I say smell, I mean smell")] +
    R['remedies-c2']['payoffs'][3:5] + [R['remedies-c2']['payoffs'][5],
     ("they brew it and smell it hot, for its relaxing bliss", "the reason first, joined with so, as his fixes do",
      "Mango leaf tea is super relaxing")])
R['sniffer-c2'] = _copy.deepcopy(R['sniffer-c1'])
R['sniffer-c2']['payoffs'][7] = ("they know a sniffer from him now has creatine and mango leaf tea in it, so they need nothing "
                                 "else", "what is in what they'd get from him", "It's a bunch of stuff in the formula")
R['sniffer-c2']['payoffs'][8] = ("they know which three things in it to buy on Amazon without one: the next three entries",
                                 "for those without it, his line", "If you don't have one")
R['cp-c7'] = dict(
    payoffs=[("they know the author uses DMSO for some chest pain", "his section opens", None),
             ("they know his angina", "his", HISLINK), ("they know it went within a minute and stayed gone", "his", HISLINK),
             ("they know why DMSO's effect on clotting bears on chest pain, said first", "what the research adds to his story",
              "Chest pain can come from a clot"),
             ("they know where it slowed clotting and how far that research goes", "the finding the first sentence leans on",
              "It did in mice")],
    checked=[{'point': 'the two clotting studies the guide links (PubMed 17000906, 20035720), and the rat study (19904216)',
              'found': ('17000906: DMSO slowed tissue factor and clots in arteries, in mice and human cells; 20035720: human '
                        'platelets; 19904216: rats given DMSO for three days before the artery was tied, pretreatment only'),
              'still_needed': ('yes: they know DMSO slows clotting, in mice and human platelets; the rats go, as the reader '
                               'can\'t give it days before'),
              'fate': 'changed'}],
    placement="Chest Pain and Injury, after his angina story (checked with it, the paragraph being under 50 words) and before what to do",
    why_reading="it tells someone whose friend has chest pain why DMSO might help: clots, which it slows",
    same_point="none: read the section from its heading to the next for the heart evidence",
    questions=dict(CP_Q, Q1='PASS: what chest pain can come from first, then the finding', Q5='PASS: "so", "though"'))


def _marks(old, idx, field):
    S = _sents(old)
    return [S[i] for i in idx]


def reads_for(key):
    if key == 'dmso-h4':
        S = _sents('dmso-h4'); s1, s2, s3, s4, s5 = S
        return {
         'needed': {'reader': NEED % 'dmso-h3', 'unneeded': [s2, s5], 'kept': {
             s2: 'they know people are given DMSO routinely, so it has a long record in humans; his sentence',
             s5: 'they weigh the mouse finding as uncertain for people; his sentence'}},
         'his_fixes': {'reader': HISF % 'dmso-h3', 'marked': [
             {'s': s1, 'difference': '1, 8', 'draft': 'dmso-h3'}, {'s': s2, 'difference': '7', 'draft': 'dmso-h3'},
             {'s': s3, 'difference': '4, 5, 7', 'draft': 'dmso-h3'},
             {'s': _sents('dmso-h3')[3], 'difference': '4, 7', 'draft': 'dmso-h3'},
             {'s': s5, 'difference': '6, 7', 'draft': 'dmso-h3'}],
           'kept': {s1: 'they know the 1967 result with its anxiety patients; his sentence, in the wording he said yes to',
                    s2: 'they know DMSO has a long record in people; his sentence',
                    s3: 'they know too much DMSO brought more side effects; his sentence and numbers (a fidelity key)',
                    s5: 'they weigh the mouse finding for people; his sentence'}},
         'fit': {'reader': FIT % 'dmso-h3', 'marked': [
             {'s': s1, 'found': 'MISREAD'}, {'s': s2, 'found': 'MISREAD'}, {'s': s3, 'found': "CAN'T TELL, FROM"},
             {'s': _sents('dmso-h3')[3], 'found': "CAN'T TELL"}, {'s': s5, 'found': 'MISREAD'}],
           'kept': {s1: 'they know the 1967 result; his sentence, the wording he said yes to (the antipsychotics his)',
                    s2: 'they know people are given DMSO routinely; his sentence',
                    s3: 'they know more DMSO brought more side effects; his sentence and his numbers',
                    s5: 'they weigh the mouse finding for people; his sentence'}}}
    if key == 'remedies-c4':
        old = _sents('remedies-c2'); S = _sents('remedies-c4')
        return {
         'needed': {'reader': NEED % 'remedies-c2', 'unneeded': [S[4], old[4]], 'kept': {
             S[4]: 'they know what smelling it does for them in a trip, bliss and posture: his reasons, from his message'}},
         'his_fixes': {'reader': HISF % 'remedies-c2', 'marked': [
             {'s': S[1], 'difference': '4', 'draft': 'remedies-c2'}, {'s': old[4], 'difference': '1', 'draft': 'remedies-c2'},
             {'s': old[7], 'difference': '2, 6, 8', 'draft': 'remedies-c2'}],
           'kept': {S[1]: 'they know it helps the brain while high, his words ("incredible for brain health"); what it does follows'}},
         'fit': {'reader': FIT % 'remedies-c2', 'marked': [
             {'s': S[1], 'found': 'FROM'}, {'s': old[2], 'found': "CAN'T TELL"}, {'s': old[4], 'found': 'FROM'}],
           'kept': {S[1]: 'they know it helps his brain while high: his experience, said as his, from his message'}}}
    if key == 'sniffer-c2':
        S = _sents('sniffer-c2'); old = _sents('sniffer-c1')
        his = ('they know %s; his sentence, which stays as he wrote it')
        return {
         'needed': {'reader': NEED % 'sniffer-c1', 'unneeded': [S[1], S[2], S[4], S[5]], 'kept': {
             S[1]: his % 'people say it saved them from crippling anxiety', S[2]: his % 'where people post about it',
             S[4]: his % 'it made the love part reliable for him', S[5]: his % 'what it does on ayahuasca'}},
         'his_fixes': {'reader': HISF % 'sniffer-c1', 'marked': [
             {'s': S[0], 'difference': '5', 'draft': 'sniffer-c1'}, {'s': S[2], 'difference': '4, 7', 'draft': 'sniffer-c1'},
             {'s': S[3], 'difference': '3', 'draft': 'sniffer-c1'}, {'s': S[5], 'difference': '8', 'draft': 'sniffer-c1'},
             {'s': old[7], 'difference': '4', 'draft': 'sniffer-c1'}],
           'kept': {S[0]: his % 'what the stick does', S[2]: his % 'where people post about it',
                    S[3]: his % 'what it does on ayahuasca', S[5]: his % 'what it does on ayahuasca'}},
         'fit': {'reader': FIT % 'sniffer-c1', 'marked': [
             {'s': S[4], 'found': 'FROM'}, {'s': S[5], 'found': 'FROM'}],
           'kept': {S[4]: his % 'it made the love part reliable for him', S[5]: his % 'what it does on ayahuasca'}}}
    if key in ('brainev-m3', 'brainev-m4'):
        S = _sents(key)
        his = 'they know %s; his sentence (5b09da6c, Human High), his to change'
        return {
         'needed': {'reader': NEED % key, 'unneeded': [S[3]], 'kept': {S[3]: his % 'the human evidence is small'}},
         'his_fixes': {'reader': HISF % key, 'marked': [
             {'s': S[1], 'difference': '3, 4', 'draft': key}, {'s': S[3], 'difference': '1, 2, 8', 'draft': key},
             {'s': S[4], 'difference': '1, 4, 7', 'draft': key}],
           'kept': {S[1]: his % 'how far the evidence goes', S[3]: his % 'the human evidence is small',
                    S[4]: ('they know the overdose evidence, in his integrated wording (his round-39 move: the term '
                           'integrated, not in brackets, read Human High), with where it was found added')}},
         'fit': {'reader': FIT % key, 'marked': [], 'kept': {}}}
    if key == 'cp-c7':
        return {
         'needed': {'reader': NEED % 'cp-c5 and cp-c6', 'unneeded': [_sents('cp-c5')[1], _sents('cp-c6')[1]], 'kept': {}},
         'his_fixes': {'reader': HISF % 'cp-c5 and cp-c6', 'marked': [
             {'s': _sents('cp-c5')[0], 'difference': '3', 'draft': 'cp-c5'},
             {'s': _sents('cp-c6')[0], 'difference': '5, 8', 'draft': 'cp-c6'},
             {'s': _sents('cp-c6')[2], 'difference': '6', 'draft': 'cp-c6'}], 'kept': {}},
         'fit': {'reader': FIT % 'cp-c5 and cp-c6', 'marked': [], 'kept': {}}}


def fill2(key):
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
    r['reader'] = {'dmso-h4': R['dmso-h3'], 'remedies-c4': R['remedies-c2'], 'sniffer-c2': R['sniffer-c1']}.get(key, {}).get('reader', r['reader'])
    r['opens']['why_reading'] = spec['why_reading']
    rd = reads_for(key)
    for f in ('needed', 'his_fixes', 'fit'):
        r[f] = rd[f]
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
