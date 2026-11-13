#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of this turn's three texts of mine (sense_receipt.py), with the three fresh
reads (reads/: need-, his-, fit-) and what each marked line's fate is (READS below, filled once the reads were in).

  python3 fill_receipts.py && python3 ../../../../tools/humanization/sense_receipt.py check TEST-KEY.txt TEST-KEY.receipt.json
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent

PASS_COMMON = {
    'Q2': 'N/A: an evidence paragraph, no instruction in it',
    'Q8': 'N/A: no list or group in it',
}

R = {
 'brainev-m1': dict(
   payoffs=[
    ("they know why the author gives DMSO first for a brain that feels damaged: his and others' experience, and the books he has read",
     "the checks and the call line before it end on when to call; this says why DMSO comes first meanwhile", None),
    ("they know how far the evidence goes before they read it", "it weighs the belief before it", "it leans this way"),
    ("they know DMSO limited the brain damage after a stroke in animals, and that this is good",
     "the first of the studies the belief leans on", "In animals, when given after a stroke"),
    ("they know the human evidence is small: one trial, and a small series for pressure in the skull",
     "the human studies after the animal one", "In one human trial"),
    ("they know the evidence closest to their friend's case: DMSO protected brain cells from the glutamate damage an "
     "overdose brings, and that it was rat cells in a dish",
     "it turns from strokes to the drug overdose case, his frame", "But more relevant to the drug overdose issue this article deals with"),
   ],
   checked=[{'point': 'Lu & Mattson 2001 (PubMed 11421595), the study his paragraph links for "NMDA- and AMPA-mediated excitotoxicity"',
             'found': ('in rat hippocampal neurons in culture, DMSO at 0.5 to 1.5% quickly and reversibly suppressed the currents '
                       'and calcium influx glutamate brings through NMDA and AMPA receptors, and protected the neurons from '
                       'glutamate-induced death (as his DMSO text and the neuro lane\'s card X1112C have it)'),
             'still_needed': 'yes: they know the evidence nearest their friend\'s overdose is from rat cells in a dish',
             'fate': 'changed'}],
   placement=("My Brain Feels Damaged, the evidence paragraph after the checks and the call line, before what DMSO can't tell; "
              "the study is said once, here, where his paragraph makes it the evidence for the overdose case (his 14:59 UTC "
              "message), and goes from the DMSO section"),
   why_reading=("it tells someone deciding whether to trust DMSO for a friend's damaged-feeling brain that the author rates it "
                "above anything else at hand, and on what"),
   same_point=("merged here; the DMSO section's description of the same study (the first two sentences of its third evidence "
               "paragraph, R39B-DMSO-3) is deleted (his 14:59 UTC message: \"maybe we can merge that?\")"),
   questions={
    'Q1': 'PASS: his belief opens; the overdose sentence leads on its frame ("more relevant to the drug overdose issue") and says what DMSO did before where',
    'Q3': 'PASS: "in rat brain cells in a dish", "the signals glutamate sends through its NMDA and AMPA receptors"',
    'Q4': 'PASS: the term "NMDA- and AMPA-mediated excitotoxicity" said as what it is ("the signals glutamate sends through its NMDA and AMPA receptors ... kept glutamate from killing them")',
    'Q5': 'PASS: "this way", "In animals", "In one human trial", "But more relevant" each say what they turn on',
    'Q6': 'PASS: belief, how far the evidence goes, animal, human, then the case closest to the reader\'s',
    'Q7': 'PASS: each study bears on trusting DMSO for brain damage; the last on the overdose case itself',
    'Q9': 'PASS: one finding a clause; "quickly" and "kept ... from killing them" carry the relation'}),
 'dmso-h1': dict(
   payoffs=[
    ("they know DMSO calmed psychiatric inpatients in a 1967 study, and what hasn't been tested yet",
     "the evidence part of the profile opens after his experience and the ozonated-charcoal water", None),
    ("they know people are given DMSO routinely, so it has a long record in humans",
     "a second line of human use", "It's routinely used in humans"),
    ("they know more DMSO brings more side effects, so they keep the dose down",
     "the transplant use's downside", "too much DMSO"),
    ("they know the risk to brain cells is in long exposure and in young brains, so they keep it short",
     "a second downside, to brain cells", "DMSO also appears to kill brain cells"),
    ("they weigh the mouse finding as uncertain for people", "it weighs the finding before it", "mouse research"),
   ],
   checked=[{'point': 'Hanslick et al. 2009 (PubMed 19100327)',
             'found': ('DMSO caused widespread apoptosis in the developing brains of mice from birth to 30 days old, worst at '
                       '7 days, from 0.3 ml/kg, and neuron loss in rat hippocampal cultures at 0.5% and 1.0% (the abstract, '
                       'read 2026-11-13; his "healthy mice neurons" said as what it found, which he said yes to at 14:56 UTC)'),
             'still_needed': 'yes: they keep the exposure short, and know young brains were the ones harmed',
             'fate': 'changed'}],
   placement=("the DMSO section, after his experience and the ozonated-charcoal water, before Side effects: what the research "
              "says it does, then its risks"),
   why_reading="it tells someone weighing DMSO what people have used it for and what the research says it does",
   same_point=("the rat brain cells in a dish (Lu & Mattson) are said once, in My Brain Feels Damaged's evidence paragraph; "
               "their sentences here are deleted (his 14:59 UTC ask)"),
   questions={
    'Q1': 'PASS: each finding leads its sentence; the Hanslick sentence leads on what DMSO did ("appears to kill brain cells")',
    'Q3': 'PASS: "stem cell transplants", "baby mice (from birth to 30 days old)", "a dish of rat neurons"',
    'Q4': 'PASS: no term a reader wouldn\'t know is left unexplained; "neurotoxic" said as "kill brain cells"',
    'Q5': 'PASS: "It\'s routinely used", "too much DMSO", "DMSO also", "mouse research" say what they turn on',
    'Q6': 'PASS: human uses, then the side effects of too much, then the risk to brain cells, then how far it carries',
    'Q7': 'PASS: each bears on whether and how to use DMSO',
    'Q9': 'PASS: one finding a sentence'}),
 'cp-c3': dict(
   payoffs=[
    ("they know how far the heart evidence goes, and that it points the same way as his angina story",
     "his angina story before it; this says what the research adds", None),
    ("they know DMSO protected heart muscle in rats, given before the heart attack",
     "the first finding the research leans on", "In rats given DMSO before a heart attack"),
    ("they know why the clotting finding bears on chest pain, and that it held in human cells",
     "the second finding, with why it bears on a heart attack first", "Most heart attacks come from a clot"),
   ],
   checked=[{'point': 'the three studies the guide links (PubMed 19904216, 17000906, 20035720)',
             'found': ('rats given DMSO before blood flow to the heart was cut lost about three quarters less heart muscle; '
                       'DMSO slowed tissue factor, platelet activation and clotting in arteries; and it slowed human platelets '
                       '(as the guide\'s paragraph had them)'),
             'still_needed': 'yes: they know what the research behind the author\'s story shows, and in what',
             'fate': 'kept'}],
   placement=("Chest Pain and Injury, after his angina story and before what to do (DMSO and magnesium chloride on the chest "
              "for steady mild pain, and the signs to call medics for)"),
   why_reading="it tells someone whose friend has chest pain whether the research backs the author's story",
   same_point="none: read the section from its heading to the next for the heart evidence",
   questions={
    'Q1': 'PASS: how far the evidence goes opens; the clotting sentence says why clotting matters before the finding',
    'Q3': 'PASS: "rats given DMSO before a heart attack", "human platelets"',
    'Q4': 'PASS: "platelets" a common word; the clot\'s part in a heart attack said',
    'Q5': 'PASS: "the same way" turns on his story; "too" on the rats',
    'Q6': 'PASS: how far it goes, then the rats, then clotting',
    'Q7': 'PASS: each bears on whether DMSO is worth using for chest pain',
    'Q9': 'PASS: one finding a sentence'}),
}

# The three fresh reads, and each marked line's fate (filled once the reads were in).
READS = {}


# The second drafts (build_tests.py, TESTS2), each marked sentence of mine changed after the reads of the first.
B105_HIS = [R['brainev-m1']['payoffs'][i] for i in range(4)]
R['brainev-m2'] = dict(R['brainev-m1'], payoffs=B105_HIS + [
    ("they know the evidence closest to their friend's case: DMSO calmed glutamate's overstimulation, which kills brain "
     "cells, and that it was rat cells in a dish", "it turns from strokes to the drug overdose case, his frame",
     "But more relevant to the drug overdose issue this article deals with")])
R['brainev-m2']['questions'] = dict(R['brainev-m1']['questions'], Q4=('PASS: the term "NMDA- and AMPA-mediated excitotoxicity" '
    'said as what it is ("the overstimulation by glutamate (through its NMDA and AMPA receptors) that kills brain cells")'))
D_HIS = R['dmso-h1']['payoffs']
R['dmso-h2'] = dict(R['dmso-h1'], payoffs=D_HIS[:3] + [
    ("they know young brains are the ones the research found at risk, even at a low dose, so they weigh it for anyone young",
     "a second risk, to brain cells, after the side effects of too much", "Young brains may be at risk from DMSO"),
    D_HIS[4]])
R['dmso-h2']['checked'] = [dict(R['dmso-h1']['checked'][0], found=(
    'PubMed 19100327\'s abstract, read 2026-11-13: mice from birth to 30 days old given DMSO had widespread apoptosis at '
    'every age, worst at 7 days, from the lowest dose tested (0.3 ml/kg); rat hippocampal neurons in a dish were lost at 0.5% '
    'and 1.0%; nothing about how long the exposure lasted, so "when they are exposed for too long" became "young brains"'),
    still_needed='yes: they know young brains were the ones harmed, even at a low dose')]
R['dmso-h2']['questions'] = dict(R['dmso-h1']['questions'], Q3=('PASS: "stem cell transplants", "mice up to a month old", '
    '"a dish of rat neurons"'), Q1='PASS: each finding leads its sentence; the Hanslick sentence leads on who is at risk')
R['cp-c4'] = dict(R['cp-c3'], payoffs=[
    ("they know how far the heart evidence goes: animals and lab dishes", "his angina story before it; this says what research there is", None),
    ("they know DMSO protected heart muscle in rats given it for days before, and that it wasn't tried once an attack had started",
     "the first finding", "Rats given DMSO for three days before a heart attack"),
    ("they know why the clotting finding bears on chest pain, and that it held in mice and in human platelets in a dish",
     "the second finding, with why it bears on a heart attack first", "Most heart attacks come from a clot")])
R['cp-c4']['checked'] = [dict(R['cp-c3']['checked'][0], found=(
    'PubMed 19904216\'s abstract, read 2026-11-13: rats given DMSO into the belly for 3 days before the artery was tied lost '
    'heart muscle 4.46% against 18.75% (about three quarters less), pretreatment only; 17000906: tissue factor and arterial '
    'clots in mice and human cells; 20035720: human platelets'))]
R['cp-c4']['questions'] = dict(R['cp-c3']['questions'], Q1=('PASS: where the research was done opens; the clotting sentence '
    'says why clotting bears on a heart attack before the finding'), Q4='PASS: "platelets (the blood cells that start clots)"',
    Q5='PASS: "though" turns on before the attack; "so" says why the clotting finding is good', Q6='PASS: what research there is, then the rats, then clotting')

NEED = 'a fresh agent given tools/humanization/needed_read_brief.md with only the paragraph, its heading and what it is for (reads/need-%s.txt)'
HISF = 'a fresh agent given tools/humanization/his_fixes_brief.md with the text, one sentence a line (reads/his-%s.txt)'
FIT = 'a fresh agent given tools/humanization/fit_read_brief.md, the universal version (reads/fit-%s.txt)'
T1 = B105_HIS_S = None
import re as _re
def _sents(key):
    return [x['s'] for x in json.loads((HERE / ('TEST-%s.receipt.json' % key)).read_text())['sentences']]

def reads_for(key, first):
    S = _sents(key)
    his_b105 = ("his sentence, from his round-39 version (Human High 137 by itself, 5b09da6c): they know %s")
    if key == 'brainev-m2':
        s1, s2, s3, s4 = S[:4]
        return {
         'needed': {'reader': NEED % first, 'unneeded': [s3], 'kept': {s3: 'they know DMSO limited the brain damage after a stroke in animals, the first evidence his belief rests on; his sentence (5b09da6c, Human High)'}},
         'his_fixes': {'reader': HISF % first, 'marked': [
             {'s': s1, 'difference': '4', 'draft': first}, {'s': s2, 'difference': '3, 4', 'draft': first},
             {'s': s3, 'difference': '4', 'draft': first}, {'s': s4, 'difference': '1, 2, 8', 'draft': first},
             {'s': 'But more relevant to the drug overdose issue this article deals with, DMSO quickly turned down the signals glutamate sends through its NMDA and AMPA receptors in rat brain cells in a dish, and kept glutamate from killing them.', 'difference': '1, 4, 7', 'draft': first}],
           'kept': {s1: 'they know the author rates DMSO first and on what; his sentence (5b09da6c, Human High), his to change',
                    s2: 'they know how far the evidence goes; his sentence, his device ("incomplete, but it leans this way")',
                    s3: 'they know DMSO limited brain damage after a stroke in animals; his sentence, his "(which is a good thing)"',
                    s4: 'they know the human evidence is small; his sentence (5b09da6c, Human High)'}},
         'fit': {'reader': FIT % first, 'marked': [], 'kept': {}}}
    if key == 'dmso-h2':
        s1, s2, s3, s4, s5 = S
        return {
         'needed': {'reader': NEED % first, 'unneeded': [s1, s3, s5], 'kept': {
             s1: 'they know DMSO calmed psychiatric inpatients in 1967; his sentence, and its two "although"s go to him (the paper had anxiety patients)',
             s3: 'they know more DMSO brought more side effects in people, so they keep the dose down; his sentence',
             s5: 'they weigh the mouse finding as uncertain for people; his sentence'}},
         'his_fixes': {'reader': HISF % first, 'marked': [
             {'s': s1, 'difference': '8', 'draft': first}, {'s': s3, 'difference': '4, 7', 'draft': first},
             {'s': "DMSO also appears to kill brain cells when they're exposed to it for too long, as it did in baby mice (from birth to 30 days old) and in a dish of rat neurons (Hanslick, et al, 2009).", 'difference': '4', 'draft': first},
             {'s': s5, 'difference': '6, 7', 'draft': first}],
           'kept': {s1: 'they know the 1967 result; his sentence, his to change ("One famous" his)',
                    s3: 'they know too much DMSO brought more side effects; his sentence and his numbers (a fidelity key)',
                    s5: 'they weigh the mouse finding for people; his sentence'}},
         'fit': {'reader': FIT % first, 'marked': [
             {'s': s1, 'found': 'MISREAD'}, {'s': s2, 'found': 'MISREAD'}, {'s': s3, 'found': "CAN'T TELL"},
             {'s': "DMSO also appears to kill brain cells when they're exposed to it for too long, as it did in baby mice (from birth to 30 days old) and in a dish of rat neurons (Hanslick, et al, 2009).", 'found': "CAN'T TELL"}],
           'kept': {s1: 'they know the 1967 result; his sentence: the misreading the reader names (its two "although"s) goes to him with the anxiety patients the paper had',
                    s2: 'they know people are given DMSO routinely; his sentence, "cell preservative" after "stem cell transplants" says it keeps the transplanted cells',
                    s3: 'they know too much DMSO brought more side effects; his sentence and his numbers (a fidelity key)'}}}
    if key == 'cp-c4':
        return {
         'needed': {'reader': NEED % first, 'unneeded': [], 'kept': {}},
         'his_fixes': {'reader': HISF % first, 'marked': [
             {'s': 'The heart research on DMSO is only in animals and lab dishes so far, but it leans the same way.', 'difference': '3, 4', 'draft': first},
             {'s': 'In rats given DMSO before a heart attack, about three quarters less heart muscle died than in rats without it.', 'difference': '7', 'draft': first},
             {'s': 'Most heart attacks come from a clot blocking an artery, and DMSO slowed clotting too, including in human platelets.', 'difference': '4, 8', 'draft': first}],
           'kept': {}},
         'fit': {'reader': FIT % first, 'marked': [
             {'s': 'In rats given DMSO before a heart attack, about three quarters less heart muscle died than in rats without it.', 'found': 'MISREAD'}],
           'kept': {}}}


for _k, _first in (('brainev-m2', 'brainev-m1'), ('dmso-h2', 'dmso-h1'), ('cp-c4', 'cp-c3')):
    READS[_k] = None


def fill(key):
    p = HERE / ('TEST-%s.receipt.json' % key)
    r = json.loads(p.read_text(encoding='utf-8'))
    spec = R[key]
    assert len(r['sentences']) == len(spec['payoffs']), (key, len(r['sentences']))
    for s, (pay, fol, link) in zip(r['sentences'], spec['payoffs']):
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            assert link and link in s['s'], (key, s['s'], link)
            s['link'] = link
    r['checked'] = spec['checked']
    r['placement'] = spec['placement']
    r['opens']['why_reading'] = spec['why_reading']
    r['same_point'] = spec['same_point']
    q = dict(PASS_COMMON)
    q.update(spec['questions'])
    r['questions'] = {k: q[k] for k in sorted(q)}
    if key in READS:
        rd = reads_for(key, {'brainev-m2': 'brainev-m1', 'dmso-h2': 'dmso-h1', 'cp-c4': 'cp-c3'}[key])
        for f in ('needed', 'his_fixes', 'fit'):
            r[f] = rd[f]
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('filled', key)


if __name__ == '__main__':
    for k in ('brainev-m2', 'dmso-h2', 'cp-c4'):
        fill(k)
