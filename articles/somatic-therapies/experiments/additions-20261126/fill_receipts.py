#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts (tools/humanization/sense_receipt.py) for the three additions of
2026-11-26, one per new paragraph and heading, filled from my reading of each sentence and from the fresh reads in reads/.

  python3 articles/somatic-therapies/experiments/additions-20261126/fill_receipts.py

Reads ADDITIONS-5.json and texts/*.txt (one file per paragraph, the paragraph as a reader reads it, links as their words),
remakes each receipt with sense_receipt.py make, fills it, and runs sense_receipt.py check on it. The marks of the sixth
draft's reads are copied from reads/drafts6-numbered.txt, the text those readers had (D below).
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

D = {}
for line in (HERE / 'reads' / 'drafts6-numbered.txt').read_text(encoding='utf-8').splitlines():
    m = re.match(r'^(A\d-S\d+): (.*)$', line)
    if m:
        D[m.group(1)] = m.group(2)

HIS = ('a fresh reader (Sonnet, 2026-11-26) given tools/humanization/his_fixes_brief.md, the live guide and the three additions '
       'one sentence a line, as they stood in the sixth draft (%sreads/READ-HIS-FIXES-6.md; earlier rounds '
       'READ-HIS-FIXES-1.md, -3.md and -4.md, each acted on)' % REL)
NEEDED = ('a fresh reader (Sonnet, 2026-11-26) given tools/humanization/needed_read_brief.md and fit_read_brief.md, the live '
          'guide and the three additions one sentence a line, as they stood in the sixth draft (%sreads/READ-NEEDED-FIT-6.md; '
          'earlier rounds READ-NEEDED-FIT-1.md, -3.md and -4.md, each acted on)' % REL)
FIT = ('the same fresh reader as the needed read, given tools/humanization/fit_read_brief.md (%sreads/READ-NEEDED-FIT-6.md, '
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

NEAR = ('the section read Human (Mostly Human, 3%% AI, https://www.pangram.com/history/2ead9bf4-482d-487d-bb34-b40ceb60f1e3), so '
        'this try changes only what a reader could take two ways, a word or two (lesson bad-trips-2026-11-19b); %s')

R['A1-P1'] = dict(
    section="Can't Stay With a Feeling?", reader=A1R,
    s=[("they recognize the moment they slide away, now that they can feel their body",
        "it opens the section on the trouble the heading asks about", None),
       ("they recognize the two shapes it takes: explaining the feeling, or agreeing with the therapist",
        "it says what sliding away looks like", "Maybe"),
       ("they know what helps (a therapist who brings them back to the feeling) and that some therapies are built for it",
        "it answers the trouble the two sentences before describe", "What helps then")],
    checked=[],
    placement="first under the new heading, before the paragraphs naming the therapies",
    opens="the first sentence describes the moment they slide away, in their own experience, so they can tell if it is them",
    same="none: read the section from its heading to Layer 4 for who it is for, the three therapies, and what to ask",
    q=dict(Q1='PASS: each sentence opens on the reader\'s case or what helps', Q2='N/A: what helps, not an instruction; the act '
           'is in the last paragraph', Q3='PASS: "a real feeling ... in a session"', Q4='PASS: "talk therapies" is plain',
           Q5='PASS: "Maybe" and "What helps then" turn on the sentence before', Q6='PASS: the moment, its shapes, what helps',
           Q7='PASS: every fact is about their own trouble in therapy', Q8='N/A: no group or list',
           Q9='PASS: one step a sentence'),
    his=['A1-S3'], fit=['A1-S4'], unneeded=['A1-S3'],
    kept_fit={D['A1-S4']: ('the new section sits at the end of Layer 3 and its first sentence says the reader can feel their '
                           'body by now: these talk therapies work on a feeling as it comes up in the room, which the next '
                           'paragraph shows, not on the story Layer 5 rebuilds')})

R['A1-P2'] = dict(
    section="Can't Stay With a Feeling?", reader=A1R,
    s=[("they learn what the first therapy does with the very slide they recognized",
        "it names the first of the therapies the paragraph before promised", "In Intensive Short-Term Dynamic Psychotherapy"),
       ("they learn the therapist watches their body for anxiety, with three signs, to see how much they can take",
        "it says what keeps that from being too much", "All the while"),
       ("a reader who overwhelms easily learns they would usually get a slower version, so this therapy isn't ruled out",
        "it answers the worry the first two sentences raise", "Most people who come to it")],
    checked=[dict(point='ISTDP points out the avoidance as it happens and turns the patient back toward the feeling', found=ISTDP,
                  still_needed='yes: they picture a session and judge whether it suits them', fate='kept'),
             dict(point='ISTDP watches anxiety in tense muscles, sighing and in thinking (vision, concentration)',
                  found=ISTDP + ': "voluntary muscle tension (tense muscles, sighing ...), smooth muscle ..., and '
                  'cognitive-perceptual function (affecting vision, hearing, concentration, memory ...)"',
                  still_needed='yes: they know the therapist is watching for when it is too much', fate='kept'),
             dict(point='most people who come to ISTDP overwhelm easily and get its graded version',
                  found=ISTDP + ': in clinics using ISTDP most patients have low anxiety tolerance and get a graded format; '
                  'the 2023 article in the same journal: a graded format for patients easily overwhelmed',
                  still_needed='yes: they know a slower version exists if they overwhelm easily', fate='kept')],
    placement="after the paragraph that says such therapies exist; the other two follow in the next paragraph",
    opens="it names the therapy and what it does with the very slide they recognized, so they know what they'd get",
    same="none: A1's other paragraphs say who it is for, the other two therapies, and what to ask",
    q=dict(Q1='PASS: each sentence opens on the therapy or its watching', Q2='N/A: no instruction', Q3='PASS: the three signs '
           'are named', Q4='PASS: the therapy is said in what it does in the sentence that names it', Q5='PASS: "All the '
           'while" and "Most people who come to it" turn on the sentence before', Q6='PASS: what it does, how it keeps it '
           'bearable, the slower version', Q7='PASS: the therapy they weigh', Q8='PASS: the three signs are all anxiety '
           'signs the source names', Q9='PASS: one step a sentence'),
    his=['A1-S5', 'A1-S6'], fit=['A1-S5'], unneeded=[])

R['A1-P3'] = dict(
    section="Can't Stay With a Feeling?", reader=A1R,
    s=[("a reader afraid of one feeling, like grief, learns which therapy goes at that fear slowly",
        "it turns to the second therapy and the narrower case it fits", None),
       ("a reader who can't let kindness in recognizes their case and the therapy for it",
        "it names the third therapy and its case, after the second", None),
       ("they learn what that therapist does first and then", "it says what the third therapy does", "The therapist first")],
    checked=[dict(point='Affect Phobia Therapy treats fear of a feeling like a phobia, with graded exposure to it',
                  found=APT + ': phobic reactions toward one\'s own feelings, "just as one can develop phobias towards external '
                  'objects"; gradual exposure', still_needed='yes: they see it goes at their pace', fate='kept'),
             dict(point='AEDP undoes aloneness first and follows the felt sense of emotion in the body', found=AEDP,
                  still_needed='yes: they know the therapy starts where their trouble is', fate='kept')],
    placement="after the first therapy, before the question to ask",
    opens="it names the one feeling that scares them, so a reader with that fear knows the sentence is theirs",
    same="none: A1's other paragraphs cover sliding away, the first therapy and what to ask",
    q=dict(Q1='PASS: the case first, then the therapy', Q2='N/A: no instruction', Q3='PASS: "one feeling ... like grief", '
           '"letting kindness in"', Q4='PASS: each therapy is said in what it does', Q5='PASS: "The therapist first" turns on '
           'the therapy just named', Q6='PASS: second therapy, third therapy, what the third does', Q7='PASS: their own '
           'trouble', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A1-S7', 'A1-S8'], fit=[], unneeded=[],
    kept_his={D['A1-S7']: ('the mark was its frame matching the next sentence, which is now built differently ("... is for when '
                           'you can\'t let kindness in"), so the two no longer share the frame')})
R['A1-P3']['s'][1] = ("a reader who can't let kindness in recognizes their case and the therapy for it",
                      "it names the third therapy and its case, after the second",
                      "none: it names the third therapy, the step the reader expects after the second")

R['A1-P4'] = dict(
    section="Can't Stay With a Feeling?", reader=A1R,
    s=[("they have the question to ask a therapist before booking",
        "it closes the section on the act, after the three therapies", "As with water therapy"),
       ("they know which answers mean keep looking: no room to slow down or to disagree",
        "it says what to do with the answer to the question before", "If the answer")],
    checked=[dict(point='the water therapy section asks a therapist a question before booking',
                  found='the live guide: "I would ask a water therapist about that before I booked"',
                  still_needed='yes: they hear the same habit the guide already taught', fate='kept')],
    placement="last in the section: the act after the choice",
    opens="it gives them the words to say to a therapist, which they can use before their first session",
    same=("the water therapy section asks a similar question before booking; this one names it (\"As with water therapy\") "
          "rather than repeating it"),
    q=dict(Q1='PASS: the act first', Q2='PASS: the question is theirs to ask, for knowing whether the therapist will let '
           'them slow down', Q3='PASS: "moving away from a feeling", "overwhelmed"', Q4='PASS: plain words',
           Q5='PASS: "If the answer" turns on the question', Q6='PASS: question, then what to do with the answer',
           Q7='PASS: it is the step before they book', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=[], fit=[], unneeded=[])

R['A2-H'] = dict(
    section='Imagery Rescripting (new, in Layer 4 after EMDR)', reader=A2R,
    s=[("a reader finds the therapy by its name in the contents sidebar", "it starts a new section after EMDR", None)],
    checked=[], placement="an h2 in Layer 4 after EMDR and before hypnosis: a memory therapy beside the other memory therapy",
    opens="they see the name a therapist would use, so they can look for it",
    same="none: no other heading names it",
    q=dict(Q_HEAD, Q1='PASS: the name is the heading', Q3='PASS: the therapy\'s own name', Q4='PASS: the first sentence says '
           'what it is', Q7='PASS: it is one of the memory therapies of Layer 4'),
    his=[], fit=[], unneeded=[])

R['A2-P1'] = dict(
    section='Imagery Rescripting', reader=A2R,
    s=[("they know who it is for (one childhood scene that still leaves them small and helpless) and that they go back with help",
        "it opens the section on the reader's case", None),
       ("they picture what happens and who steps in, the therapist first and later their adult self",
        "it says what going back with backup means", "You picture the scene again"),
       ("they can tie it to his own way of re-doing memories and read it there",
        "it says where they have met this before", "Rescripting is a lot like")],
    checked=[dict(point='the therapist intervenes in the imagined scene first and the patient\'s adult self later', found=IMRS,
                  still_needed='yes: they know what a session asks of them', fate='kept'),
             dict(point='his inner child guide has a section on reliving trauma memories in a better way',
                  found=('the inner child guide, "Inner Child Self-Love Reparenting Guide", as live on 2026-11-25, section '
                         '"Re-do Trauma Memories" (https://ibogaqueen.substack.com/i/189761959/re-do-trauma-memories)'),
                  still_needed='yes: they can go to his own version of it', fate='kept')],
    placement="first in the section, right after the EMDR paragraph that warns going straight into memory can re-traumatize",
    opens="it names the scene that still leaves them helpless, so they know the section is for them",
    same="none: the section's second paragraph is about the evidence and the care to take",
    q=dict(Q1='PASS: the case first', Q2='N/A: no instruction', Q3='PASS: "one scene from your childhood"', Q4='PASS: '
           'imagery rescripting is said in what it does in the sentence that names it', Q5='PASS: each sentence answers '
           'the one before (what happens, where else)', Q6='PASS: who, what happens, where else',
           Q7='PASS: all about their scene', Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A2-S3', 'A2-S4'], fit=['A2-S4'], unneeded=[],
    late_ok={'Rescripting': ('the short form of "imagery rescripting", which the first sentence names and says in what it '
                             'does; this sentence compares it with his own way, it doesn\'t explain it')})

R['A2-P2'] = dict(
    section='Imagery Rescripting', reader=A2R,
    s=[("they hear the question they are asking", "it turns from what it is to whether it works", "Does it work"),
       ("they learn whom it works for and how well, against EMDR", "it answers the question", None),
       ("they learn what that rests on: a trial of 155 such adults with symptoms down about equally",
        "it gives the evidence for the answer", "A trial"),
       ("they know the imagined version won't tell them what happened, and what it does change",
        "it answers the worry a made-up scene raises", "The new version"),
       ("they know to stop when it's too much and to ground themselves afterward",
        "it gives the care the EMDR paragraph above asks for", "Because rescripting takes you back")],
    checked=[dict(point='155 adults with PTSD from childhood trauma; imagery rescripting and EMDR both effective, neither better',
                  found=IMRS, still_needed='yes: they weigh it against EMDR', fate='changed'),
             dict(point='after EMDR, ground yourself', found='the live guide\'s EMDR section: "After an EMDR session, it\'s a '
                  'good idea to do some grounding activities."', still_needed='yes: they ground themselves afterward',
                  fate='kept')],
    placement="after the paragraph saying what it is, last in the section",
    opens="it asks the question the reader has once they know what the therapy is",
    same="none: the section's first paragraph says what it is",
    q=dict(Q1='PASS: the question, then its answer first', Q2='PASS: "stop when it\'s too much, and ground yourself afterward" '
           'is theirs to do, for not being overwhelmed', Q3='PASS: "adults whose PTSD started in childhood"', Q4='PASS: EMDR '
           'and PTSD are used in the live guide before this', Q5='PASS: each sentence answers the one before',
           Q6='PASS: question, answer, evidence, the worry, the care', Q7='PASS: each fact is about the therapy they weigh',
           Q8='N/A: no list', Q9='PASS: one step a sentence'),
    his=['A2-S5', 'A2-S6', 'A2-S7', 'A2-S8'], fit=['A2-S7'], unneeded=['A2-S5'],
    kept_his={D['A2-S5']: ('it is the reader\'s own question at the turn from what the therapy is to whether it works; the '
                           'answer comes in the next sentence, so it stands as the question itself')},
    kept_needed={D['A2-S5']: ('they hear the question they are asking at this point, so the answer that follows lands as the '
                              'answer to it')})

R['A3-H'] = dict(
    section="Pain That Won't Quit? (new, after Layer 5)", reader=A3R,
    s=[("a reader in pain finds the section in the contents sidebar", "it starts a new branch after Layer 5", None)],
    checked=[], placement=("an h1 after Layer 5 and before the optional high-intensity practices: a branch for pain, not "
                           "a sixth layer; the sentence that tied it to Layer 5 is cut, so the h1 has nothing to contradict"),
    opens="they see their pain named as a question, so they know the section is theirs",
    same="none: no other heading is about pain",
    q=dict(Q_HEAD, Q1='PASS: the pain is the heading', Q3='PASS: "Pain That Won\'t Quit"', Q4='PASS: plain words',
           Q7='PASS: their own pain'),
    his=[], fit=['A3-S1'], unneeded=[],
    kept_fit={D['A3-S1']: ('the heading stays an h1: a branch for pain after the five layers, not a layer of its own, and no '
                           'sentence in it says "Layer 5" any more; the near-miss rule keeps the section as it read Human')})

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
    his=['A3-S1'], fit=['A3-S1'], unneeded=[])

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
    his=['A3-S3'], fit=['A3-S3'], unneeded=[])

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
    his=['A3-S6'], fit=[], unneeded=[],
    kept_his={D['A3-S6']: NEAR % 'its numbers have one reading each, and its window read High'})

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
    his=['A3-S8'], fit=[], unneeded=[],
    kept_his={D['A3-S8']: NEAR % '"those feelings" are the stress and feelings about people the sentence before names, so it has one reading'})
R['A3-P4']['s'][1] = ("they learn its name and that it works on those feelings", "it names the therapy for that pain",
                      "none: it names the therapy for the case the sentence before just set out, the step the reader expects")

R['A3-P5'] = dict(
    section="Pain That Won't Quit?", reader=A3R,
    s=[("they learn whom the evidence is for and the result against CBT", "it gives this therapy's evidence, limit first",
        "In a 2024 trial"),
       ("they don't set the two trials' numbers side by side", "it heads off the comparison the two numbers invite",
        "A 30% drop")],
    checked=[dict(point='126 veterans aged 60 to 95; 63% vs 17% with at least 30% less pain', found=EAET,
                  still_needed='yes: they weigh it for their own pain and age', fate='changed')],
    placement="after what the second therapy is",
    opens="it says whom the evidence covers",
    same="none: the PRT evidence is in the third paragraph; this one says the two can't be compared",
    q=dict(Q1='PASS: the trial\'s people first', Q2='N/A: no instruction', Q3='PASS: "veterans aged 60 and up"',
           Q4='PASS: CBT is used in the live guide', Q5='PASS: "That\'s a lower bar" turns on the result', Q6='PASS: result, '
           'then why not to compare', Q7='PASS: the therapy they weigh', Q8='N/A: no list', Q9='PASS: no units with spaces'),
    his=['A3-S10', 'A3-S11'], fit=[], unneeded=[],
    kept_his={D['A3-S10']: NEAR % 'its numbers have one reading each', D['A3-S11']: NEAR % 'the reason not to compare is in it (a 30% drop is a lower bar than 0 or 1 out of 10), and the two numbers sit close enough (66% and 63%) that a reader would compare them'})

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
    his=['A3-S12', 'A3-S13', 'A3-S14'], fit=['A3-S13'], unneeded=['A3-S12'],
    kept_his={D['A3-S12']: NEAR % 'it has one reading; that the search was mine, not his, is on the card for him'},
    kept_needed={D['A3-S12']: 'they learn no trial picks a winner, which is why the next sentence has them choose by their own pain'})
R['A3-P6']['s'][0] = ("they know no trial says which of the two is better", "it closes the branch on the choice",
                      "none: the first sentence of the closing paragraph, after the two therapies' evidence, a step the reader expects")

HIS_NOTES = {}
for line in (HERE / 'reads' / 'READ-HIS-FIXES-6.md').read_text(encoding='utf-8').splitlines():
    m = re.match(r'^- (A\d-S\d+): ([\d, ()a-z]+) — (.*)$', line)
    if m:
        HIS_NOTES[m.group(1)] = '%s: %s' % (m.group(2).strip(), m.group(3)[:200])
FIT_NOTES = {
    'A1-S4': '"talk therapies" in a layer titled "before the story comes in"; the guide files talk therapy under story work',
    'A1-S5': 'calling out each slide reads confrontational against Layer 3\'s gentle promise; the anxiety signs are for the therapist',
    'A2-S4': '"my inner child guide" is not a name the guide uses',
    'A2-S7': '"Since you know the new version is imagined, it changes how the memory feels" doesn\'t follow',
    'A3-S1': ('"pain is what brought you to this guide" doesn\'t fit a trauma guide; and the h1 right after Layer 5 with no '
              'bridge reads as another layer'),
    'A3-S3': ('"false alarm" can read as "your pain isn\'t real"; and contradiction: a reframe against the guide\'s caution '
              'that cognitive-behavioral patterns suppress fear responses'),
    'A3-S13': '"the second" and "the first" are unclear after the trial numbers'}


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
        rec['needed'] = {'reader': NEEDED, 'unneeded': [D[k] for k in r.get('unneeded', [])],
                         'kept': r.get('kept_needed', {})}
        rec['his_fixes'] = {'reader': HIS, 'marked': [{'s': D[k], 'difference': HIS_NOTES.get(k, '?')} for k in r['his']],
                            'kept': r.get('kept_his', {})}
        rec['fit'] = {'reader': FIT, 'marked': [{'s': D[k], 'found': FIT_NOTES[k]} for k in r['fit']],
                      'kept': r.get('kept_fit', {})}
        rec['questions'] = r['q']
        if r.get('late_ok'):
            rec['late_ok'] = r['late_ok']
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
    'A1-P2': 'In Intensive Short-Term Dynamic Psychotherapy', 'A1-P3': "If it's one feeling", 'A1-P4': 'As with water therapy',
    'A2-P2': 'Does it work', 'A3-P2': 'In Pain Reprocessing Therapy',
    'A3-P3': "Pain Reprocessing Therapy's first big trial", 'A3-P4': 'The second therapy',
    'A3-P5': ('none: it gives the second therapy\'s evidence, the step the reader expects after the first therapy\'s '
              'evidence'),
    'A3-P6': ('none: the closing paragraph turns from the two therapies\' evidence to choosing between them, the step '
              'the reader expects'),
}


def sections():
    adds = json.loads((HERE / 'ADDITIONS-7.json').read_text(encoding='utf-8'))
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
        rec['needed'] = {'reader': NEEDED, 'unneeded': [u for r in recs for u in r['needed']['unneeded']],
                         'kept': {k: v for r in recs for k, v in r['needed']['kept'].items()}}
        rec['his_fixes'] = {'reader': HIS, 'marked': [m for r in recs for m in r['his_fixes']['marked']],
                            'kept': {k: v for r in recs for k, v in r['his_fixes']['kept'].items()}}
        rec['fit'] = {'reader': FIT, 'marked': [m for r in recs for m in r['fit']['marked']],
                      'kept': {k: v for r in recs for k, v in r['fit']['kept'].items()}}
        qs = {}
        for q in rec['questions']:
            passes = [r['questions'][q] for r in recs if r['questions'][q].startswith('PASS')]
            qs[q] = ('PASS: ' + ' / '.join(x[len('PASS:'):].strip() for x in passes)) if passes else recs[0]['questions'][q]
        rec['questions'] = qs
        lo = {k: v for r in recs for k, v in (r.get('late_ok') or {}).items()}
        if lo:
            rec['late_ok'] = lo
        out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        res = subprocess.run([sys.executable, str(SR), 'check', str(txt), str(out)], capture_output=True, text=True)
        bad += res.returncode != 0
        print(a['id'] + '-SEC', 'PASS' if res.returncode == 0 else res.stdout.strip())
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() + sections() else 0)
