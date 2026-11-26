#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts (tools/humanization/sense_receipt.py) for the three additions of
2026-11-26, one per new paragraph and heading, filled from my reading of each sentence and from the fresh reads in reads/.

  python3 articles/somatic-therapies/experiments/additions-20261126/fill_receipts.py

Reads ADDITIONS-5.json and texts/*.txt (one file per paragraph, the paragraph as a reader reads it, links as their words),
remakes each receipt with sense_receipt.py make, fills it, and runs sense_receipt.py check on it. The marks of the fourth
draft's reads are copied from reads/drafts4-numbered.txt, the text those readers had.
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SR = ROOT / 'tools' / 'humanization' / 'sense_receipt.py'
REL = 'articles/somatic-therapies/experiments/additions-20261126/'

D4 = {}
for line in (HERE / 'reads' / 'drafts4-numbered.txt').read_text(encoding='utf-8').splitlines():
    m = re.match(r'^(A\d-S\d+): (.*)$', line)
    if m:
        D4[m.group(1)] = m.group(2)

HIS = ('a fresh reader (Sonnet, 2026-11-26) given tools/humanization/his_fixes_brief.md, the live guide and the three additions '
       'one sentence a line, as they stood in the fourth draft (%sreads/READ-HIS-FIXES-4.md; earlier rounds '
       'READ-HIS-FIXES-1.md and READ-HIS-FIXES-3.md, each acted on)' % REL)
NEEDED = ('a fresh reader (Sonnet, 2026-11-26) given tools/humanization/needed_read_brief.md and fit_read_brief.md, the live '
          'guide and the three additions one sentence a line, as they stood in the fourth draft (%sreads/READ-NEEDED-FIT-4.md, '
          'which lists no unneeded sentence; the third draft\'s read, READ-NEEDED-FIT-3.md, listed the clause "These overlap a '
          'lot," which is cut)' % REL)
FIT = ('the same fresh reader as the needed read, given tools/humanization/fit_read_brief.md (%sreads/READ-NEEDED-FIT-4.md, '
       'parts 2 and 3)' % REL)

A1R = ('an adult working through the guide who can feel their body by now but slides away from feelings in therapy sessions, '
       'deciding whether to look for one of these therapists, and which one')
A2R = ('an adult with one scene from their childhood that still leaves them helpless, who has just read that going straight '
       'into a trauma memory with EMDR can re-traumatize, deciding whether imagery rescripting fits them')
A3R = ('an adult whose pain has lasted months with no injury or disease found to explain it, who came to the guide partly for '
       'that pain, deciding whether one of two pain therapies fits them, and which')

ISTDP = ('Abbass 2021, Tidsskrift for Norsk Psykologforening (https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-'
         'dynamic-psychotherapy-methods-evidence-indications-and)')
APT = ('Schanche, Hjeltnes, Berggraf and Ulvenes 2013, same journal (https://psykologtidsskriftet.no/node/15971/pdf); '
       'McCullough et al. 2003 (Guilford)')
AEDP = 'APA video and description, Fosha (https://www.apa.org/pubs/videos/4310759)'
IMRS = 'Boterhoven de Haan et al. 2020, British Journal of Psychiatry 217(5):609-615 (https://pubmed.ncbi.nlm.nih.gov/32892758/)'
PRT = ('Ashar et al. 2022, JAMA Psychiatry 79(1):13-23 (https://pmc.ncbi.nlm.nih.gov/articles/PMC8482298); NIH Research '
       'Matters, 2021-11-02 (https://www.nih.gov/news-events/nih-research-matters/retraining-brain-treat-chronic-pain)')
EAET = 'Yarns et al. 2024, JAMA Network Open (https://clinicaltrials.gov/study/NCT03918642)'

Q_HEAD = {q: 'N/A: a heading of a few words, read in the narrow contents sidebar and above its section; it makes no claim, '
             'gives no instruction and holds no list' for q in ('Q2', 'Q5', 'Q6', 'Q8', 'Q9')}

R = {}

R['A1-H'] = dict(
    section="Can't Stay With a Feeling? (new, in Layer 3 after Brainspotting)", reader=A1R,
    s=[("a reader who slides away from feelings finds the section in the contents sidebar and knows it is for them",
        "it starts a new section after Brainspotting's further reading, the last thing in Layer 3", None)],
    checked=[],
    placement=("an h2 at the end of Layer 3, after Brainspotting and before Layer 4's memory work: these therapies are for a "
               "reader who can feel the body by now, which Layers 1 to 3 build, and who isn't ready for a specific memory"),
    opens="they see their own trouble named as a question, so they know whether to read the section",
    same=("none: no other heading in the guide names this trouble; Layer 3's heading is about exploring trauma feelings "
          "before the story comes in, which this section's reader can do with their body but not with a therapist"),
    q=dict(Q_HEAD, Q1='PASS: the trouble is the whole heading', Q3='PASS: "a feeling" is the feeling coming up in a session, '
           'which the first sentence says', Q4='PASS: plain words only', Q7='PASS: it names the reader\'s own trouble'),
    his=[], fit=[])

R['A1-P1'] = dict(
    section="Can't Stay With a Feeling?", reader=A1R,
    s=[("they recognize their own pattern by its two common shapes, explaining the feeling or agreeing with the therapist",
        "it opens the section on the trouble the heading asks about", None),
       ("they know what to look for: a therapist who catches the slide and keeps them with the feeling",
        "it answers the case the sentence before describes", "If that's you"),
       ("they learn there are therapies built for this, so they can ask for one by name",
        "it says where such a therapist is found, which the next paragraph names", "A few talk therapies")],
    checked=[],
    placement="first under the new heading, before the paragraphs naming the therapies",
    opens="the first sentence describes the moment they slide away, in their own experience, so they can tell if it is them",
    same="none: read the section from its heading to Layer 4 for who it is for, the three therapies, and what to ask",
    q=dict(Q1='PASS: each sentence opens on the reader\'s case or the act', Q2='PASS: "look for a therapist who catches you '
           'sliding away" says what it is for (to stay with the feeling)', Q3='PASS: "a real feeling ... in a session"',
           Q4='PASS: "talk therapies" is plain', Q5='PASS: "If that\'s you" turns on the pattern; the third names who does it',
           Q6='PASS: pattern, what to look for, where to find it', Q7='PASS: every fact is about their own trouble in therapy',
           Q8='N/A: no group or list', Q9='PASS: one step a sentence'),
    his=['A1-S2'], fit=['A1-S1', 'A1-S2'],
    kept_fit={D4['A1-S1']: ('it names two ways of sliding away a reader can check in themselves (explaining the feeling, '
                            'agreeing with the therapist), and the question in the last paragraph lets a therapist say it '
                            'too, so a reader who can\'t see it alone still has a way in')})

R['A1-P2'] = dict(
    section="Can't Stay With a Feeling?", reader=A1R,
    s=[("they learn what the first therapy does in a session, so they can judge whether being caught at each slide suits them",
        "it names the first of the therapies the paragraph before promised", "In Intensive Short-Term Dynamic Psychotherapy"),
       ("they learn a reader who overwhelms easily gets a slower version, so this therapy isn't ruled out for them",
        "it answers the worry the first sentence raises (being pushed at each slide)", "Most people who come to this therapy"),
       ("a reader afraid of one feeling, like grief, learns which therapy goes at that fear slowly",
        "it turns to the second therapy and the narrower case it fits", "Then there's")],
    checked=[dict(point='ISTDP points out the avoidance as it happens and tracks anxiety in the body', found=ISTDP,
                  still_needed='yes: they picture a session and judge whether it suits them', fate='kept'),
             dict(point='most people who come to ISTDP have low anxiety tolerance and get a graded, supportive version',
                  found=ISTDP + ': in clinics using ISTDP most patients have low anxiety tolerance and get a graded format',
                  still_needed='yes: they know a slower version exists if they overwhelm easily', fate='changed'),
             dict(point='Affect Phobia Therapy treats fear of a feeling with graded exposure to it',
                  found=APT + ': phobic reactions toward one\'s own feelings; gradual exposure to the avoided feeling',
                  still_needed='yes: they see it goes at their pace, which the guide\'s worry about exposure needs',
                  fate='changed')],
    placement="after the paragraph that says such therapies exist, naming the first two; kindness gets its own paragraph next",
    opens="it names the therapy and what it does with the very slide they recognized, so they know what they'd get",
    same="none: A1's other paragraphs say who it is for, the third therapy, and what to ask",
    q=dict(Q1='PASS: each sentence opens on the therapy or the reader\'s case', Q2='N/A: no instruction here; the act is in the '
           'last paragraph', Q3='PASS: each therapy is named in full', Q4='PASS: each named therapy is said in what it does, '
           'in the sentence that names it', Q5='PASS: "Most people who come to this therapy" and "Then there\'s" turn on the '
           'sentence before', Q6='PASS: the first therapy, its slower version, then the narrower case', Q7='PASS: each fact '
           'is about the therapies they are choosing among', Q8='N/A: no list', Q9='PASS: one therapy or step a sentence'),
    his=['A1-S3', 'A1-S4', 'A1-S5'], fit=[],
    kept_his={D4['A1-S3']: ('the name comes after the paragraph before has said a few talk therapies do this, so the reader '
                            'is already asking which; they need the name to look the therapy up, and what it does follows '
                            'in the same sentence; the second and third readers did not mark it')})

R['A1-P3'] = dict(
    section="Can't Stay With a Feeling?", reader=A1R,
    s=[("a reader who can't take in kindness recognizes their own case",
        "it adds a third kind of trouble after the two the paragraph before covered", "And"),
       ("they learn the third therapy starts by keeping them company in the feeling, then follows it in the body",
        "it answers the case just named", "For them")],
    checked=[dict(point='AEDP undoes aloneness first and follows the felt sense of emotion in the body', found=AEDP,
                  still_needed='yes: they know the therapy starts where their trouble is', fate='kept')],
    placement="after the two therapies for sliding away and for a feared feeling, before the question to ask",
    opens="it names the trouble of not letting kindness in, so a reader with it knows this paragraph is theirs",
    same="none: A1's other paragraphs cover sliding away and one feared feeling",
    q=dict(Q1='PASS: the trouble first, then the therapy', Q2='N/A: no instruction', Q3='PASS: "being treated kindly"',
           Q4='PASS: the therapy is said in what it does', Q5='PASS: "For them" turns on the case before', Q6='PASS: case, '
           'then therapy', Q7='PASS: their own trouble', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A1-S6', 'A1-S7'], fit=['A1-S6', 'A1-S7'])

R['A1-P4'] = dict(
    section="Can't Stay With a Feeling?", reader=A1R,
    s=[("they have the question to ask a therapist before booking",
        "it closes the section on the act, after the three therapies", "As with water therapy"),
       ("they know which answers mean keep looking: no room to slow down or to disagree",
        "it says what to do with the answer to the question before", "If the answer")],
    checked=[dict(point='the water therapy section asks a therapist a question before booking',
                  found='the live guide: "I would ask a water therapist about that before I booked"',
                  still_needed='yes: they hear the same habit the guide already taught', fate='kept')],
    placement="last in the section: the act after the choice; the cut sentence about Layers 4 and 5 is gone",
    opens="it gives them the words to say to a therapist, which they can use before their first session",
    same=("the water therapy section asks a similar question before booking; this one names it (\"As with water therapy\") "
          "rather than repeating it"),
    q=dict(Q1='PASS: the act first', Q2='PASS: the question is theirs to ask, for knowing whether the therapist will let '
           'them slow down', Q3='PASS: "moving away from a feeling", "overwhelmed"', Q4='PASS: plain words',
           Q5='PASS: "If the answer" turns on the question', Q6='PASS: question, then what to do with the answer',
           Q7='PASS: it is the step before they book', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A1-S8'], fit=['A1-S8'])

R['A2-H'] = dict(
    section='Imagery Rescripting (new, in Layer 4 after EMDR)', reader=A2R,
    s=[("a reader finds the therapy by its name in the contents sidebar", "it starts a new section after EMDR", None)],
    checked=[], placement="an h2 in Layer 4 after EMDR and before hypnosis: a memory therapy beside the other memory therapy",
    opens="they see the name a therapist would use, so they can look for it",
    same="none: no other heading names it",
    q=dict(Q_HEAD, Q1='PASS: the name is the heading', Q3='PASS: the therapy\'s own name', Q4='PASS: the first sentence says '
           'what it is', Q7='PASS: it is one of the memory therapies of Layer 4'),
    his=[], fit=[])

R['A2-P1'] = dict(
    section='Imagery Rescripting', reader=A2R,
    s=[("they know who it is for (one childhood scene that still leaves them helpless) and that it goes back into it with help",
        "it opens the section on the reader's case", None),
       ("they picture what happens: the scene again, with someone protecting them",
        "it says what going back with help means", "You picture the scene again"),
       ("they know who steps in, the therapist first and their own adult self later",
        "it answers who the somebody is", "At first"),
       ("they can tie it to the guide's sister practice in his inner child guide and read it there",
        "it says where they have met this before", "It's close to")],
    checked=[dict(point='the therapist intervenes in the imagined scene first and the patient\'s adult self later', found=IMRS,
                  still_needed='yes: they know what a session asks of them', fate='kept'),
             dict(point='his inner child guide has a section on reliving trauma memories in a better way',
                  found=('the inner child guide as live on 2026-11-25, section "Re-do Trauma Memories" '
                         '(https://ibogaqueen.substack.com/i/189761959/re-do-trauma-memories)'),
                  still_needed='yes: they can go to his own version of it', fate='kept')],
    placement="first in the section, right after the EMDR paragraph that warns going straight into memory can re-traumatize",
    opens="it names the scene that still leaves them helpless, so they know the section is for them",
    same="none: the section's second paragraph is about the evidence and the care to take",
    q=dict(Q1='PASS: the case first', Q2='N/A: no instruction', Q3='PASS: "one scene from your childhood"', Q4='PASS: '
           'imagery rescripting is said in what it does in the sentence that names it', Q5='PASS: each sentence answers '
           'the one before (what, who, where else)', Q6='PASS: who, what happens, who steps in, where else',
           Q7='PASS: all about their scene', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A2-S3'], fit=['A2-S3'])

R['A2-P2'] = dict(
    section='Imagery Rescripting', reader=A2R,
    s=[("they learn whom the evidence is for, so they can tell how far it reaches their case",
        "it turns from what it is to whether it works", "As for whether it works"),
       ("they learn it does about as well as EMDR, and on what that rests",
        "it gives the finding for the adults just named", "For them"),
       ("they know the imagined scene doesn't change what they remember happened",
        "it answers a worry the made-up scene raises", "You know the new scene is imagined"),
       ("they know when to stop and to ground themselves afterward",
        "it gives the care the EMDR paragraph above asks for", "Like EMDR")],
    checked=[dict(point='155 adults with PTSD from childhood trauma; imagery rescripting and EMDR both effective, neither better',
                  found=IMRS, still_needed='yes: they weigh it against EMDR', fate='changed'),
             dict(point='after EMDR, ground yourself', found='the live guide\'s EMDR section: "After an EMDR session, it\'s a '
                  'good idea to do some grounding activities."', still_needed='yes: they ground themselves afterward',
                  fate='kept')],
    placement="after the paragraph saying what it is, last in the section",
    opens="it says whether the evidence covers someone like them",
    same="none: the section's first paragraph says what it is",
    q=dict(Q1='PASS: each sentence opens on its point', Q2='PASS: "I\'d stop whenever it starts to feel like too much" is '
           'theirs to do, for not being overwhelmed', Q3='PASS: "adults whose PTSD started in childhood"', Q4='PASS: EMDR '
           'and PTSD are used in the live guide before this', Q5='PASS: "As for", "For them", "so" each turn on the clause '
           'before', Q6='PASS: whom the evidence is for, the finding, the worry, the care', Q7='PASS: each fact is about the '
           'therapy they are weighing', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A2-S4', 'A2-S5', 'A2-S6', 'A2-S7'], fit=['A2-S4', 'A2-S6'])

R['A3-H'] = dict(
    section="Pain That Won't Quit? (new, after Layer 5)", reader=A3R,
    s=[("a reader in pain finds the section in the contents sidebar", "it starts a new branch after Layer 5", None)],
    checked=[], placement=("an h1 after Layer 5 and before the optional high-intensity practices: a branch for pain, not "
                           "a sixth layer; the sentence that tied it to Layer 5 is cut, so the h1 has nothing to contradict"),
    opens="they see their pain named as a question, so they know the section is theirs",
    same="none: no other heading is about pain",
    q=dict(Q_HEAD, Q1='PASS: the pain is the heading', Q3='PASS: "Pain That Won\'t Quit"', Q4='PASS: plain words',
           Q7='PASS: their own pain'),
    his=[], fit=['A3-S1'])

R['A3-P1'] = dict(
    section="Pain That Won't Quit?", reader=A3R,
    s=[("a reader who came for pain hears that the section is for them", "it opens the branch on the reader's case", None),
       ("they know the two conditions (months, a doctor found no cause) and that two therapies follow",
        "it says which pain the section means", "If yours")],
    checked=[], placement="first in the new branch",
    opens="it asks whether pain brought them here, so a reader in pain reads on",
    same="none: read the branch from its heading to the next h1 for the two therapies and how to choose",
    q=dict(Q1='PASS: the case first', Q2='N/A: no instruction', Q3='PASS: "lasted months", "no injury or disease"',
           Q4='PASS: plain words', Q5='PASS: "If yours" turns on the pain just named', Q6='PASS: case, then conditions',
           Q7='PASS: their own pain', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A3-S1', 'A3-S2'], fit=['A3-S2'])

R['A3-P2'] = dict(
    section="Pain That Won't Quit?", reader=A3R,
    s=[("they learn what the first therapy teaches (the pain is a false alarm) and how (attention to the body)",
        "it names the first of the two therapies", "In Pain Reprocessing Therapy"),
       ("they learn the second step, going back to what they avoid, slowly, with an example",
        "it is the step after learning the pain is a false alarm", "Then, a little at a time")],
    checked=[dict(point='PRT teaches pain as non-dangerous brain activity with cognitive, somatic and exposure techniques',
                  found=PRT, still_needed='yes: they know what the therapy asks of them', fate='changed')],
    placement="after the paragraph naming the case, before its evidence",
    opens="it says what they would learn about their own pain",
    same="none: the next paragraph gives its evidence",
    q=dict(Q1='PASS: the therapy and what it teaches first', Q2='N/A: what the therapy does, not an instruction',
           Q3='PASS: "things you\'ve been avoiding because of it, like going for walks"', Q4='PASS: "false alarm" is said '
           'in the same sentence as the brain signaling danger where there isn\'t any', Q5='PASS: "Then" is the next step',
           Q6='PASS: what it teaches, then what you do', Q7='PASS: their pain', Q8='N/A: no list',
           Q9='PASS: one step a sentence'),
    his=['A3-S3', 'A3-S4'], fit=['A3-S4'])

R['A3-P3'] = dict(
    section="Pain That Won't Quit?", reader=A3R,
    s=[("they learn the evidence is only for mild to moderate back pain, so they know how far it reaches their pain",
        "it turns from what the therapy is to its evidence, limit first", "Pain Reprocessing Therapy's first big trial"),
       ("they learn how many ended up nearly pain-free, against placebo, and that it lasted",
        "it gives the result of the trial just named", "There")],
    checked=[dict(point='66% vs 20% at 0 or 1 out of 10 after 4 weeks, largely maintained at a year; mild or moderate pain',
                  found=PRT, still_needed='yes: they weigh it for their own pain', fate='changed')],
    placement="after what the therapy is, before the second therapy",
    opens="it says whether the evidence covers their kind of pain",
    same="none: the EAET evidence is the fifth paragraph, about another therapy",
    q=dict(Q1='PASS: the limit first', Q2='N/A: no instruction', Q3='PASS: "mild to moderate chronic back pain", "0 or 1 '
           'out of 10", "a placebo shot"', Q4='PASS: plain words', Q5='PASS: "There" is the trial', Q6='PASS: limit, '
           'result', Q7='PASS: the therapy they weigh', Q8='N/A: no list', Q9='PASS: no units with spaces'),
    his=['A3-S5'], fit=[])

R['A3-P4'] = dict(
    section="Pain That Won't Quit?", reader=A3R,
    s=[("they learn which pain the second therapy is for", "it turns to the second of the two therapies", "The second therapy"),
       ("they learn its name and that it works on those feelings", "it names the therapy for that pain", None),
       ("they picture what a session asks: letting out held-back feelings and rehearsing a hard conversation",
        "it says what working on those feelings means", "Much of the therapy")],
    checked=[dict(point='EAET: writing about stress, role playing difficult relationships, expressing anger and other feelings',
                  found=EAET, still_needed='yes: they picture what it asks of them', fate='changed')],
    placement="after the first therapy and its evidence",
    opens="it says which pain the therapy is for, so they can tell if it is theirs",
    same="none: the first therapy is in the second and third paragraphs",
    q=dict(Q1='PASS: the case first', Q2='N/A: what the therapy does', Q3='PASS: "stress and feelings about the people in '
           'your life"', Q4='PASS: plain words', Q5='PASS: "The second therapy", "those feelings", "Much of the therapy"',
           Q6='PASS: case, name, what it asks', Q7='PASS: their pain', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A3-S6', 'A3-S7'], fit=[])
R['A3-P4']['s'][1] = ("they learn its name and that it works on those feelings", "it names the therapy for that pain",
                      "none: it names the therapy for the case the sentence before just set out, the step the reader expects")

R['A3-P5'] = dict(
    section="Pain That Won't Quit?", reader=A3R,
    s=[("they learn whom the evidence is for and the result against CBT", "it gives this therapy's evidence, limit first",
        "In a 2024 trial"),
       ("they don't set the two trials' numbers side by side", "it heads off the comparison the two numbers invite",
        "That's a lower bar")],
    checked=[dict(point='126 veterans aged 60 to 95; 63% vs 17% with at least 30% less pain', found=EAET,
                  still_needed='yes: they weigh it for their own pain and age', fate='changed')],
    placement="after what the second therapy is",
    opens="it says whom the evidence covers",
    same="none: the PRT evidence is in the third paragraph; this one says the two can't be compared",
    q=dict(Q1='PASS: the trial\'s people first', Q2='N/A: no instruction', Q3='PASS: "veterans aged 60 and up"',
           Q4='PASS: CBT is used in the live guide', Q5='PASS: "That\'s a lower bar" turns on the result', Q6='PASS: result, '
           'then why not to compare', Q7='PASS: the therapy they weigh', Q8='N/A: no list', Q9='PASS: no units with spaces'),
    his=['A3-S8'], fit=['A3-S8'])

R['A3-P6'] = dict(
    section="Pain That Won't Quit?", reader=A3R,
    s=[("they know no trial says which of the two is better", "it closes the branch on the choice", None),
       ("they know which to start with, by whether their pain seems tied to stress or people",
        "it gives the way to choose that the missing comparison leaves", "So"),
       ("they know to ask about training and to track it as the guide's last section says",
        "it gives the steps after choosing", "I'd also")],
    checked=[dict(point='no trial compares PRT and EAET', found='the research lane\'s search and mine, 2026-11-26: none found',
                  still_needed='yes: they choose by their own pain instead of by a winner', fate='kept')],
    placement="last in the branch, before the optional high-intensity practices",
    opens="it says no trial has picked a winner, so they read on for how to choose",
    same="none: the branch's other paragraphs say what each therapy is and its evidence",
    q=dict(Q1='PASS: the missing comparison first', Q2='PASS: start with the one that fits, ask about training, track it',
           Q3='PASS: "the second" and "the first" are the two therapies just described', Q4='PASS: plain words',
           Q5='PASS: "So" turns on the missing comparison', Q6='PASS: no winner, how to choose, what next',
           Q7='PASS: their choice', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A3-S9', 'A3-S10'], fit=['A3-S9', 'A3-S10'])
R['A3-P6']['s'][0] = ("they know no trial says which of the two is better", "it closes the branch on the choice",
                      "none: the first sentence of the closing paragraph, after the two therapies' evidence, a step the reader expects")

HIS_NOTES = {}
for line in (HERE / 'reads' / 'READ-HIS-FIXES-4.md').read_text(encoding='utf-8').splitlines():
    m = re.match(r'^- (A\d-S\d+): ([\d, ()a-z]+) — (.*)$', line)
    if m:
        HIS_NOTES[m.group(1)] = '%s: %s' % (m.group(2).strip(), m.group(3)[:200])
FIT_NOTES = {
    'A1-S1': 'a reader who slides away may not notice it; add a cue they can check',
    'A1-S2': 'contradiction: "short-term talk therapies" against keeping the same therapist through two layers (A1-S8)',
    'A1-S6': '"that feeling" has no referent', 'A1-S7': '"that feeling" has no referent',
    'A1-S8': ('contradiction: all three go into memories, to readers who overwhelm easily, against the EMDR section\'s '
              'warning that going straight into memory can re-traumatize'),
    'A2-S3': '"my inner child guide" and the order therapist then adult self need checking',
    'A2-S4': 'cites PTSD evidence, but the reader may only have one stuck scene',
    'A2-S6': '"so" doesn\'t follow from "make up", and a made-up scene can read as false memory',
    'A3-S1': 'heading level: an h1, but the sentence says "Layer 5"',
    'A3-S2': ('the guide is about trauma, not pain; and contradiction: "two newer therapies" against the guide\'s joke '
              'about 50 new kinds of therapies a year'),
    'A3-S4': '"false alarm" and doing the avoided things could read as dismissive or as pushing through pain',
    'A3-S8': '"main trial so far" needs checking against sources', 'A3-S9': '"nobody has tested the two" needs checking',
    'A3-S10': '"judge it the way I describe at the end": what "it" is'}


def main():
    probs = 0
    for pid, r in R.items():
        txt = HERE / 'texts' / ('%s.txt' % pid)
        out = HERE / 'receipts' / ('%s.receipt.json' % pid)
        subprocess.run([sys.executable, str(SR), 'make', str(txt), '--section', r['section'], '--reader', r['reader'],
                        '--out', str(out)], check=True, capture_output=True)
        rec = json.loads(out.read_text(encoding='utf-8'))
        if len(rec['sentences']) != len(r['s']):
            sys.exit('%s: %d sentences in the text, %d filled' % (pid, len(rec['sentences']), len(r['s'])))
        for x, (pay, fol, link) in zip(rec['sentences'], r['s']):
            x['payoff'], x['follows'] = pay, fol
            if 'link' in x:
                x['link'] = link or 'none: it starts the paragraph on a new step the reader expects'
        rec['checked'] = r['checked']
        rec['placement'] = r['placement']
        rec['opens']['why_reading'] = r['opens']
        same = r['same']
        if same.startswith('none:') and not re.search(r'\bread\b', same):
            same = 'none: read the section from its heading to the next; ' + same[len('none:'):].strip()
        rec['same_point'] = same
        rec['needed'] = {'reader': NEEDED, 'unneeded': [], 'kept': {}}
        rec['his_fixes'] = {'reader': HIS, 'marked': [{'s': D4[k], 'difference': HIS_NOTES.get(k, '?')} for k in r['his']],
                            'kept': r.get('kept_his', {})}
        rec['fit'] = {'reader': FIT, 'marked': [{'s': D4[k], 'found': FIT_NOTES[k]} for k in r['fit']],
                      'kept': r.get('kept_fit', {})}
        rec['questions'] = r['q']
        out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        res = subprocess.run([sys.executable, str(SR), 'check', str(txt), str(out)], capture_output=True, text=True)
        ok = res.returncode == 0
        probs += not ok
        print(pid, 'PASS' if ok else res.stdout.strip())
    return probs


# The section receipts: each addition's paragraphs as one text (no heading), the text Pangram reads, its receipt merged
# from the paragraph receipts above. The first sentence of each later paragraph gets the tie it makes to the paragraph
# before.
SEC_LINKS = {
    'A1-P2': 'In Intensive Short-Term Dynamic Psychotherapy', 'A1-P3': 'And', 'A1-P4': 'As with water therapy',
    'A2-P2': 'As for whether it works', 'A3-P2': 'In Pain Reprocessing Therapy',
    'A3-P3': "Pain Reprocessing Therapy's first big trial", 'A3-P4': 'The second therapy',
    'A3-P5': ('none: it gives the second therapy\'s evidence, the step the reader expects after the first therapy\'s '
              'evidence'),
    'A3-P6': ('none: the closing paragraph turns from the two therapies\' evidence to choosing between them, the step '
              'the reader expects'),
}


def sections():
    adds = json.loads((HERE / 'ADDITIONS-5.json').read_text(encoding='utf-8'))
    bad = 0
    for a in adds:
        n = len(a['paragraphs'])
        pids = ['%s-P%d' % (a['id'], i) for i in range(1, n + 1)]
        recs = [json.loads((HERE / 'receipts' / ('%s.receipt.json' % p)).read_text(encoding='utf-8')) for p in pids]
        text = a['text']
        txt = HERE / 'texts' / ('%s-SEC.txt' % a['id'])
        txt.write_text(text + '\n', encoding='utf-8')
        out = HERE / 'receipts' / ('%s-SEC.receipt.json' % a['id'])
        subprocess.run([sys.executable, str(SR), 'make', str(txt), '--section', recs[0]['section'], '--reader',
                        recs[0]['reader'], '--out', str(out)], check=True, capture_output=True)
        rec = json.loads(out.read_text(encoding='utf-8'))
        merged = []
        for p, r in zip(pids, recs):
            for k, x in enumerate(r['sentences']):
                y = {'s': x['s'], 'payoff': x['payoff'], 'follows': x['follows']}
                if merged:
                    y['link'] = x.get('link') if k else SEC_LINKS[p]
                merged.append(y)
        if [x['s'] for x in rec['sentences']] != [x['s'] for x in merged]:
            sys.exit('%s: the section\'s sentences differ from its paragraphs\'' % a['id'])
        rec['sentences'] = merged
        rec['checked'] = [c for r in recs for c in r['checked']]
        rec['placement'] = 'the whole new section, %s; %s' % (R['%s-H' % a['id']]['placement'],
                                                            ' '.join('%s: %s.' % (p, r['placement']) for p, r in zip(pids, recs)))
        rec['opens']['why_reading'] = recs[0]['opens']['why_reading']
        rec['same_point'] = ('none: read the section from its heading to the next; each paragraph makes its own point '
                             '(%s)' % '; '.join('%s: %s' % (p, r['same_point'][:80]) for p, r in zip(pids, recs)))
        rec['needed'] = {'reader': NEEDED, 'unneeded': [], 'kept': {}}
        rec['his_fixes'] = {'reader': HIS, 'marked': [m for r in recs for m in r['his_fixes']['marked']],
                            'kept': {k: v for r in recs for k, v in r['his_fixes']['kept'].items()}}
        rec['fit'] = {'reader': FIT, 'marked': [m for r in recs for m in r['fit']['marked']],
                      'kept': {k: v for r in recs for k, v in r['fit']['kept'].items()}}
        qs = {}
        for q in rec['questions']:
            passes = [r['questions'][q] for r in recs if r['questions'][q].startswith('PASS')]
            qs[q] = ('PASS: ' + ' / '.join(x[len('PASS:'):].strip() for x in passes)) if passes else recs[0]['questions'][q]
        rec['questions'] = qs
        out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        res = subprocess.run([sys.executable, str(SR), 'check', str(txt), str(out)], capture_output=True, text=True)
        bad += res.returncode != 0
        print(a['id'] + '-SEC', 'PASS' if res.returncode == 0 else res.stdout.strip())
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() + sections() else 0)
