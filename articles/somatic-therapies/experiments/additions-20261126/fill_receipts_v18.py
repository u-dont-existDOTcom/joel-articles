#!/usr/bin/env python3
"""fill_receipts_v18.py - the making-sense receipts (tools/humanization/sense_receipt.py) for draft 16 of the somatic
additions (A1 and A3, ADDITIONS-18.json, the turn of 19:25 UTC) and the inner child sentences' eighth draft (INNER-CHILD-ADDS-8.json), one per text
that goes to Pangram this turn, filled from my reading of each sentence and from the fresh reads of drafts 9 to 12 in reads/.

  python3 articles/somatic-therapies/experiments/additions-20261126/fill_receipts_v18.py

Each sentence is filled once (ANN); a text is a list of paragraphs, and its receipt takes each sentence's fill, with the
tie to what comes before for every sentence but the text's first. Writes texts/v18/<KEY>.txt and receipts/v18/<KEY>.receipt.json
and runs sense_receipt.py check on each.
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt  # noqa: E402

SR = ROOT / 'tools' / 'humanization' / 'sense_receipt.py'
REL = 'articles/somatic-therapies/experiments/additions-20261126/'


def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t).strip()


ADDS = {a['id']: a for a in json.loads((HERE / 'ADDITIONS-18.json').read_text(encoding='utf-8'))}
IC = json.loads((HERE / 'INNER-CHILD-ADDS-8.json').read_text(encoding='utf-8'))

PARAS = {}
for aid in ('A1', 'A3'):
    for i, p in enumerate(ADDS[aid]['paragraphs'], 1):
        PARAS['%s-P%d' % (aid, i)] = plain(p)
PARAS['J'] = IC['IC1']['his_before']
PARAS['IC1'] = plain(IC['IC1']['add'])
PARAS['IC2'] = plain(IC['IC2']['add'])
PARAS['H'] = IC['IC2']['his_before']

# sentence ids in reading order
SID = {}
for prefix, keys in (('A1', ['A1-P%d' % i for i in range(1, 6)]), ('A3', ['A3-P%d' % i for i in range(1, 7)]),
                     ('J', ['J']), ('IC1', ['IC1']), ('IC2', ['IC2']), ('H', ['H'])):
    n = 0
    for k in keys:
        for s in sense_receipt.sentences(PARAS[k]):
            n += 1
            SID['%s-S%d' % (prefix, n)] = s
BYS = {v: k for k, v in SID.items()}

N1 = 'none: it opens a new paragraph on '
# (payoff, follows, tie to what comes before when the sentence isn't the text's first)
ANN = {
    'A1-S1': ("they recognize whether they are the one who can feel their body but slips away from a feeling in a session, "
              "how it shows, and the therapy for it", "it opens the section on the reader's case, after the layers before",
              N1 + 'a new section, on the reader\'s case after the layers before'),
    'A1-S2': ("they picture what its therapist does when they slip away", "it says what the therapy just named does",
              'The therapist catches you at it'),
    'A1-S3': ("they learn that anxiety about the feeling is behind the slipping away, and that the therapist watches for it "
              "so it doesn't get to be too much", "it says what the therapy watches while it presses toward the feeling",
              "It's usually anxiety about the feeling"),
    'A1-S4': ("they know a slower version exists, that it's the usual one, and what it does when the anxiety climbs",
              "it says what happens when the anxiety the sentence before named is too much",
              'If you can only take a little of that anxiety'),
    'A1-S5': ("they recognize the second case, one feared feeling, and get the therapy for it and how it works",
              "it turns from slipping away from any feeling to fearing one",
              N1 + 'the next case, the second of the therapies the section promised'),
    'A1-S6': ("they recognize the third case, kindness that bounces off, and get the therapy's name",
              "it gives the next case after the feared feeling", 'And if'),
    'A1-S7': ("they picture what a session asks of them and how it works on the kindness that bounces off",
              "it says what the therapy just named does", 'The therapist'),
    'A1-S8': ("they learn the risk the three share: being steered back to feelings can get to be too much",
              "after the three therapies, it says what they have in common that matters before booking",
              N1 + 'what the three have in common, after each was described'),
    'A1-S9': ("they get the two questions to ask before booking, in the guide's water-therapy form: overwhelm, and "
               "being told they're dodging a feeling when they don't think they are",
               "it says what to ask because of the risk the sentence before named", 'So before booking'),
    'A1-S10': ("they know which answer to look for", "it says how to judge the answer to the question", "I'd want them"),
    'A3-S1': ("readers in physical pain recognize that this section is for them, check whether their pain fits, and learn "
              "two therapies are coming", "it opens the section on the reader's own reason for being here",
              N1 + 'a new section, on the reader\'s own reason for being here'),
    'A3-S2': ("they learn what the first therapy teaches about their pain, told it is real and where the false alarm rests",
              "it names the first of the two therapies the paragraph before promised",
              N1 + 'the first of the two therapies the paragraph before promised'),
    'A3-S3': ("they learn the first thing they'd do in it, and how it differs from the noticing they already do",
              "it says how the learning the sentence before named happens", 'Part of how you learn that'),
    'A3-S4': ("they learn the second thing they'd do: go back to what they have been avoiding",
              "it gives the next step after the attention", 'Then'),
    'A3-S5': ("they learn whether the evidence covers their kind of pain",
              "after what the therapy is, the limit of its evidence", N1 + 'the evidence, naming the therapy again'),
    'A3-S6': ("they see how big the effect was and that it mostly lasted", "it gives the trial's result", 'There'),
    'A3-S7': ("they learn which pain the second therapy is for", "it turns to the second of the two therapies",
              'The second therapy'),
    'A3-S8': ("they learn its name and that it works on the feelings", "it names the therapy for the case just set out",
              'none: it names the therapy for the case the sentence before set out, the step the reader expects'),
    'A3-S9': ("they picture what a session asks: letting out held-back feelings and rehearsing a hard conversation",
               "it says what working on the feelings means", 'Much of the therapy'),
    'A3-S10': ("they learn whom the evidence covers and the result against CBT", "after what the therapy is, its evidence",
               N1 + 'the second therapy\'s evidence, the step the reader expects after what it is'),
    'A3-S11': ("they don't set the two trials' numbers side by side", "it heads off the comparison the two numbers invite",
               'A 30% drop'),
    'A3-S12': ("they know no trial says which of the two is better", "it closes the evidence with the missing comparison",
               N1 + 'choosing between the two, after both therapies\' evidence'),
    'A3-S13': ("they know which to start with, by what their pain seems tied to",
               "with no trial between them, it gives the way to choose", 'So'),
    'A3-S14': ("they know to ask about training and to track it as the guide's last section says",
               "it gives the steps after choosing", "I'd also"),
    'J-S1': ("they know the step: set the memory beside its corrected version", "it carries on the section's way of "
             "redoing a memory", N1 + 'the redo itself, after the example of his spanking'),
    'J-S2': ("they see what a corrected version can be, in a friend's case", "it gives an example of the corrected "
             "version", 'For my friend J.'),
    'J-S3': ("they know a correction that looks easy can still take years", "it says what the example might hide",
             'Ok, that one'),
    'IC1-S1': ("they learn that for a memory too big to redo alone there is a clinical therapy that does this, with its "
               "name and a link", "after a correction that can take years, it says where to get help",
               'If a memory feels too big'),
    'IC1-S2': ("they know what the therapist does in it and that it ends with them doing it themselves",
               "it says what the therapy just named does", 'The therapist'),
    'IC2-S1': ("they get two therapies to look into while the tests keep coming back normal, without stopping the search, "
               "and hear that neither calls the pain imaginary", "it follows the advice not to stop investigating with what "
               "to do meanwhile", 'While the investigation goes on'),
    'IC2-S2': ("they learn what each therapy has them do, with the false alarm said in a way that keeps the pain real and "
               "the investigation open", "it says what the two therapies just mentioned are", 'In Pain Reprocessing Therapy'),
    'IC2-S3': ("they know where to read about both, their trials and how far they reach", "it points to the details, in his "
               "own pointer form from the same section", 'More on both'),
    'H-S1': ("they know what to ask a specialist for, including when to go to the ER, and not to stop looking for the cause",
             "it is his advice on the pain the section describes", N1 + 'his advice, after the attacks he describes'),
}

ISTDP = ('Abbass 2021, Tidsskrift for Norsk Psykologforening (https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-'
         'term-dynamic-psychotherapy-methods-evidence-indications-and)')
APT = 'Schanche, Hjeltnes, Berggraf and Ulvenes 2013 (https://psykologtidsskriftet.no/node/15971/pdf)'
AEDP = ('APA, Fosha (https://www.apa.org/pubs/videos/4310759); AEDP Institute, "enhancing receptive capacity" and "processing '
        'relational affects" (https://aedpinstitute.org/?p=552), "focusing on the physical experience of emotion" '
        '(https://aedpinstitute.org/?p=254), the patient\'s capacity "to take in the therapist\'s presence, support and care" '
        '(https://aedpinstitute.org/journal/making-good-use-of-suffering-intra-relational-work-with-pathogenic-affects/)')
IMRS = 'Boterhoven de Haan et al. 2020, British Journal of Psychiatry 217(5):609-615 (https://pubmed.ncbi.nlm.nih.gov/32892758/)'
PRT = ('Ashar et al. 2022, JAMA Psychiatry 79(1):13-23 (https://pmc.ncbi.nlm.nih.gov/articles/PMC8482298): "guided reappraisal '
       'of pain sensations", "fear- and avoidance-inducing beliefs"; NIH Research Matters, 2021-11-02')
EAET = 'Yarns et al. 2024, JAMA Network Open (https://clinicaltrials.gov/study/NCT03918642)'
REAL = ('VA Eastern Colorado, "All Pain is Real" (https://www.va.gov/eastern-colorado-health-care/programs/understanding-chronic-'
        'pain-what-you-need-to-know/); Lumley and Schubiner 2019, EAET for chronic pain (https://pmc.ncbi.nlm.nih.gov/articles/'
        'PMC7309024): the brain generates or amplifies primary pain')

C = {
    'istdp': dict(point='ISTDP points out avoidance as it happens and turns the patient back toward the feeling; anxiety about '
                  'the feeling drives the avoidance; the therapist watches it in tense muscles, sighing and foggy thinking; '
                  'most patients have low anxiety tolerance and get a graded, slower format', found=ISTDP,
                  still_needed='yes: they picture a session and know they won\'t be pushed past what they can take',
                  fate='changed'),
    'apt': dict(point='APT treats fear of one\'s own feelings like a phobia, with gradual exposure to the feeling', found=APT,
                still_needed='yes: they recognize their case and know the pace is set by what they can bear', fate='kept'),
    'aedp': dict(point='AEDP undoes aloneness, helps the patient take in the therapist\'s care, asks about taking it in, and '
                 'tracks the feeling in the body', found=AEDP,
                 still_needed='yes: they picture what the therapy does with care that bounces off', fate='changed'),
    'prt': dict(point='PRT: reappraisal of pain sensations and of the beliefs that the pain means harm; a graded return to '
                'feared activities; mild to moderate chronic back pain; 66% vs 20% pain-free or nearly, gains largely held at '
                'one year', found=PRT, still_needed='yes: they weigh it for their own pain', fate='changed'),
    'eaet': dict(point='EAET: emotional expression and role-play of hard conversations; 126 veterans aged 60 to 95 with '
                 'muscle and joint pain; 63% vs 17% with at least 30% less pain', found=EAET,
                 still_needed='yes: they weigh it for their own pain and age', fate='kept'),
    'none': dict(point='no trial compares PRT and EAET', found='the research lane\'s search and mine, 2026-11-26: none found',
                 still_needed='yes: they choose by their own pain instead of by a winner', fate='kept'),
    'imrs': dict(point='Imagery Rescripting: the therapist intervenes in the imagined scene first, the patient\'s adult self '
                 'later', found=IMRS, still_needed='yes: they know what the therapy would ask of them and that it ends '
                 'with them doing it', fate='changed'),
    'real': dict(point='both therapies tell patients the pain is real, made by the brain', found=REAL,
                 still_needed='yes: they hear the guide is not calling their pain imaginary', fate='kept'),
    'scope': dict(point='the two trials: mild to moderate chronic back pain (PRT); older veterans\' muscle and joint pain '
                  '(EAET)', found=PRT + '; ' + EAET, still_needed='yes: they see what kinds of pain the evidence covers',
                  fate='changed'),
}

HIS_READS = ('fresh readers (Fable, 2026-11-27) given tools/humanization/his_fixes_brief.md, the live guide and the text one '
             'sentence a line: %sreads/READ-HIS-FIXES-10.md, -11.md, READ-12.md, READ-14.md and READ-16.md (draft 9\'s marks on A3 in '
             'READ-HIS-FIXES-9.md, by Sonnet); each acted on' % REL)
NEEDED_READS = ('fresh readers (Fable, 2026-11-27) given tools/humanization/needed_read_brief.md, the live guide and the text '
                'one sentence a line: %sreads/READ-NEEDED-FIT-10.md, -11.md, READ-12.md, READ-14.md and READ-16.md; none found a sentence its '
                'reader doesn\'t need' % REL)
FIT_READS = ('the same fresh readers, given tools/humanization/fit_read_brief.md and a contradictions check (%sreads/'
             'READ-NEEDED-FIT-10.md, -11.md, READ-12.md, READ-14.md and READ-16.md; draft 9\'s in READ-NEEDED-FIT-9.md)' % REL)

NEAR = ('A3 is the near miss he approved on the card (Mostly Human, 3% AI, https://www.pangram.com/history/2ead9bf4-482d-487d-'
        'bb34-b40ceb60f1e3): one or two words a check (lesson bad-trips-2026-11-19b)')
# marks still in the text, with why each stays (the marks whose sentences changed need no reason: they are gone)
KEEP_HIS = {
    'A3-S11': ('READ-14 marked it with the sentence after it, for "the two" that follows "the two trials\' numbers"; the fix '
               'went into that sentence ("the two therapies"), one word, since A3 is the near miss'),
    'A1-S5': ('marked in READ-HIS-FIXES-10 (way 21, "the anxiety is doing the handling"): it read Human High by itself in the '
              'near miss of 26 November (https://www.pangram.com/history/b4f0fea6-06e1-4076-a6a6-a0589c7d82e1), and "a pace '
              'your anxiety can handle" is the plain idiom; it stays word for word (gut-2026-11-06c)'),
    'A3-S6': NEAR + '; it sat in a Human High window there, so it stays word for word',
    'A3-S12': NEAR + '; it sat in the Medium window of 34 words, whose turn comes after the Low windows',
    'A3-S13': NEAR + '; it sat in the Medium window of 34 words; the readers\' fix (naming the two therapies) is the next '
                     'change for that window once the Low windows read High',
    'A3-S14': NEAR + '; it sat in a Human High window there ("that therapy" is the one you picked, as the sentence before says)',
}
KEEP_FIT = {
    'A1-S5': ('READ-NEEDED-FIT-10, 7 (exposure, which the guide says can re-traumatize): the guide\'s worry is exposure to '
              'memories faster than the body can take; this is gradual exposure to a feeling "at a pace your anxiety can '
              'handle", the pace being what answers it; it read Human High as it is'),
    'A3-S13': NEAR + '; READ-NEEDED-FIT-9, 11 (the "So", and back pain only): the choice rests on the sentence before (no '
                     'trial between them) and on what each is for, said in each paragraph; the next small change in its window',
}
# the sentences each read marked, as they stood in the text it read
MARKS_HIS = {
    'A3-S11': SID['A3-S11'],
    'A1-S5': SID['A1-S5'],
    'A3-S6': SID['A3-S6'], 'A3-S12': SID['A3-S12'], 'A3-S13': SID['A3-S13'], 'A3-S14': SID['A3-S14'],
}
MARKS_HIS_GONE = [
    ("It's usually anxiety that makes you slip away, so the therapist also watches for its signs, like tense muscles, sighing, "
     "or your thinking going foggy, to tell when it's getting to be too much for you.", 'READ-12: "anxiety" with no object'),
    ("Part of how you learn it is by paying close attention to how the pain feels in your body.",
     'READ-12: ways 14 and 11, the attention they already pay all day, and the means first'),
    ("The therapist also watches for signs of the anxiety that's making you slip away, like tense muscles, sighing, or your "
     "thinking going foggy.", 'READ-HIS-FIXES-11: anxiety comes in as if said; the watching\'s purpose comes later'),
    ("Most people who try this therapy can't take much of that anxiety, so they get a slower version, where the therapist "
     "stops to help them settle whenever it climbs.", 'READ-HIS-FIXES-11: "most people ... they" leaves the reader outside'),
]
MARKS_FIT = {'A1-S5': SID['A1-S5'], 'A3-S13': SID['A3-S13']}

Q = {
    'A1': dict(Q1='PASS: each sentence opens on the reader\'s case ("If you can feel your body just fine by now but still slip away", "If '
                  'it\'s one feeling", "And if what you can\'t let in") or on what the therapy does', Q2='PASS: look into the '
                  'therapy; ask what happens if you get overwhelmed or are told you are dodging a feeling when you '
                  'don\'t think you are; want to hear they would slow down and listen', Q3='PASS: the anxiety is "about the feeling"; the signs are '
                  'named; "their answer" is to those questions', Q4='PASS: each therapy is said by what it does in the '
                  'sentence that names it', Q5='PASS: "The therapist catches you at it", "If you can '
                  'only take", "And if", "So before booking", "I\'d want them"', Q6='PASS: the case, then three therapies by '
                  'case, then how to vet one', Q7='PASS: each therapy is for a case the reader can recognize', Q8='PASS: the '
                  'three signs are anxiety signs the source names', Q9='PASS: one step a sentence'),
    'A3': dict(Q1='PASS: the case first, then each therapy by what you do in it, its evidence limit first', Q2='PASS: start '
                  'with the one that fits; ask about training; track it', Q3='PASS: "mild to moderate chronic back pain", '
                  '"veterans aged 60 and up", "getting your pain down to 0 or 1 out of 10"', Q4='PASS: "false alarm" is said '
                  'in the sentence that uses it', Q5='PASS: "Part of how you learn that", "Then", "There", "The second '
                  'therapy", "So"', Q6='PASS: whose pain, therapy one and its evidence, therapy two and its evidence, how to '
                  'choose', Q7='PASS: their pain and their choice', Q8='N/A: no list of items', Q9='PASS: the false alarm '
                  'and how you learn it are two sentences'),
    'IC1': dict(Q1='PASS: the reader\'s case first ("If a memory feels too big to redo on your own"), then the therapy',
                Q2='PASS: the act is to look into the therapy, named and linked, when a memory is too big to redo alone',
                Q3='PASS: "a clinical therapy for this", "the adult you needed"', Q4='PASS: what the therapist does is said in '
                   'the sentence after the name, before any other use', Q5='PASS: "If a memory feels too big" picks up the '
                   'years J. might need; "The therapist" is the therapy\'s', Q6='PASS: when it helps, the '
                   'therapy, what it does, how it ends', Q7='PASS: the reader redoing a memory', Q8='N/A: no list',
                Q9='PASS: two sentences, one thought each'),
    'IC2': dict(Q1='PASS: when first ("While the investigation goes on, if the tests keep coming back normal"), then the act',
                Q2='PASS: ask a specialist for a plan; look into the two; read more in the somatic guide', Q3='PASS: "two '
                   'talk therapies", named', Q4='PASS: "talk therapies that treat the pain as real" says what kind of thing '
                   'they are', Q5='PASS: "While the investigation goes on" picks up his sentence before; "More on both" the '
                   'two named', Q6='PASS: his advice, then what to do meanwhile, then where to read more', Q7='PASS: the reader whose tests come back normal', Q8='N/A: no list', Q9='PASS: one step a '
                   'sentence'),
}

A1R = ('an adult working through the guide who can feel their body by now but slips away from feelings in therapy sessions, '
       'deciding whether to look for one of these therapists, which one, and how to vet one')
A3R = ('an adult whose pain has lasted months with no injury or disease found to explain it, who came to the guide partly for '
       'that pain, deciding whether one of two pain therapies fits them, and which')
ICR1 = ('an adult reading the inner child guide\'s way of redoing a painful memory with a corrected version, deciding whether '
        'to do it alone or with help')
ICR2 = ('an adult with pain attacks that tests keep explaining away, reading the inner child guide\'s Physical Pain section, '
        'deciding what to try while the doctors keep looking')

TEXTS = {
    'A1-P1': dict(paras=['A1-P1'], part='A1', reader=A1R, checked=['istdp'],
                  placement='first in the new section at the end of Layer 3, after Brainspotting\'s further reading',
                  same='none: read the section from its heading to the next; the other paragraphs say how ISTDP keeps it '
                       'bearable, the other two therapies, and what to ask'),
    'A1-P5': dict(paras=['A1-P5'], part='A1', reader=A1R, checked=['istdp', 'apt', 'aedp'],
                  placement='last in the section, after the three therapies; "All three" points to them',
                  same='none: read the section from its heading to the next; the questions are asked once, here'),
    'IC1': dict(paras=['IC1'], part='IC1', reader=ICR1, checked=['imrs'],
                placement='a paragraph of its own at the end of Re-do Trauma Memories, after his J. paragraph, so his '
                          '"For example" story still follows the reliving it illustrates',
                same='none: read the section from its heading to the next; no other paragraph names the clinical therapy'),
    'IC2': dict(paras=['IC2'], part='IC2', reader=ICR2, checked=['real', 'prt', 'eaet'],
                placement='a paragraph of its own at the end of Physical Pain?, after his advice not to stop the '
                          'investigation; its "While the investigation goes on" points to that',
                same='none: read the section from its heading to the next; no other paragraph names these therapies'),
    'A3-P1P2': dict(paras=['A3-P1', 'A3-P2'], part='A3', reader=A3R, checked=['prt'],
                    placement='the opening of the new section (37 words, so checked with the paragraph after it) and the '
                              'first therapy', same='none: read the section from its heading to the next; only these say '
                              'whose pain it is for and what PRT does'),
}



def main():
    bad = 0
    tdir, rdir = HERE / 'texts' / 'v18', HERE / 'receipts' / 'v18'
    tdir.mkdir(parents=True, exist_ok=True)
    rdir.mkdir(parents=True, exist_ok=True)
    for key, t in TEXTS.items():
        text = '\n\n'.join(PARAS[p] for p in t['paras'])
        txt = tdir / ('%s.txt' % key)
        txt.write_text(text + '\n', encoding='utf-8')
        out = rdir / ('%s.receipt.json' % key)
        section = {'A1': "Can't Stay With a Feeling?", 'A3': "Pain That Won't Quit?",
                   'IC1': 'Re-do Trauma Memories (inner child guide)', 'IC2': 'Physical Pain? (inner child guide)'}[t['part']]
        subprocess.run([sys.executable, str(SR), 'make', str(txt), '--section', section, '--reader', t['reader'],
                        '--out', str(out)], check=True, capture_output=True)
        rec = json.loads(out.read_text(encoding='utf-8'))
        ids = []
        for x in rec['sentences']:
            sid = BYS[x['s']]
            ids.append(sid)
            pay, fol, link = ANN[sid]
            x['payoff'], x['follows'] = pay, fol
            if 'link' in x:
                x['link'] = link
        rec['checked'] = [C[c] for c in t['checked']]
        rec['placement'] = t['placement']
        rec['opens']['why_reading'] = ANN[ids[0]][0]
        rec['same_point'] = t['same']
        rec['needed'] = {'reader': NEEDED_READS, 'unneeded': [], 'kept': {}}
        his_marked = [{'s': MARKS_HIS[i], 'difference': 'see KEEP'} for i in ids if i in MARKS_HIS]
        his_marked += [{'s': s, 'difference': d} for s, d in MARKS_HIS_GONE]
        rec['his_fixes'] = {'reader': HIS_READS, 'marked': his_marked,
                            'kept': {MARKS_HIS[i]: KEEP_HIS[i] for i in ids if i in MARKS_HIS}}
        rec['fit'] = {'reader': FIT_READS,
                      'marked': [{'s': MARKS_FIT[i], 'found': 'see kept'} for i in ids if i in MARKS_FIT],
                      'kept': {MARKS_FIT[i]: KEEP_FIT[i] for i in ids if i in MARKS_FIT}}
        rec['questions'] = Q[t['part']]
        out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        res = subprocess.run([sys.executable, str(SR), 'check', str(txt), str(out)], capture_output=True, text=True)
        ok = res.returncode == 0
        bad += not ok
        print(key, len(text.split()), 'words', 'PASS' if ok else res.stdout.strip() + res.stderr.strip())
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
