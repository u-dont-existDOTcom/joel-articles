#!/usr/bin/env python3
"""fill_h76.py - the making-sense receipts of turn 68's two texts of mine: the charcoal and poison control paragraphs of
Swallowed Too Much? (B127, B128) and the opening paragraph of Serotonin Syndrome (SS)? (B130), each one try from his
post's text. Each text was read twice by fresh readers before its check: the three reads and the tell panel on the text
as it stands (reads/*-asis-*.txt, panel-b127/, panel-b130/), then the three reads on my first draft in its section
(reads/*-a1-*.txt, TEST-a1-*.txt); the text checked (a2) changes every sentence those reads marked, or says here why one
stays.

  python3 fill_h76.py a2-b127-b128 a2-b130
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
POST = 'his post as of 2026-11-03 (original.md), the paragraph as it stood in the guide before this turn'
REVIEW = ('the review the paragraph cites (Zellner and others 2019, Deutsches Aerzteblatt International, PMC6620762), read '
          'on 2026-11-25')
CFG = {
    'b127': dict(
        section='Swallowed Too Much?',
        reader=('the friend of someone who swallowed too much of a drug about an hour ago, with activated charcoal in their '
                'bag and a phone, deciding what to do next'),
        place=('the second and third paragraphs of Swallowed Too Much? (B127, B128), after his paragraph on working out what '
               'was swallowed, how long ago and what the body is doing, and before Serotonin Syndrome (SS)?'),
        why='it tells the friend when charcoal can help, when not to give it, and what poison control is for',
        same=('none: read the section from its heading to the next; when to give charcoal and what poison control is for are '
              'said only here. The remedy entry on activated charcoal further down (not this section) says again that it '
              'adsorbs medication somebody depends on, with what to do about it, and this paragraph links to it'),
        reads='swallowed-sec', panel='panel-b127'),
    'b130': dict(
        section='Serotonin Syndrome (SS)?',
        reader=('somebody sitting with a person who drank ayahuasca while taking an antidepressant, who is shaking and '
                'sweating, reading to find out whether this is serotonin syndrome and what to do'),
        place=('the opening paragraph of Serotonin Syndrome (SS)? (B130), after Swallowed Too Much? and before How to Check '
               'for SS'),
        why='it tells the friend when to suspect serotonin syndrome, before the checks and the steps that follow',
        same=('none within the opening: read the section from its heading to the next. Step 1 of Act Now on SS names the same '
              'substances again, each as something to stop; here they are what to ask about, so both stay (the remedy '
              'glosses, "the painkiller tramadol", "the antibiotic linezolid", "DXM cough syrup", are step 1\'s own words, '
              'brought up to the first mention)'),
        reads='ss-open', panel='panel-b130'),
}
# sentence start -> (payoff, follows, link)
PAY = {
    'If they swallowed it [within': ('they know whether charcoal is still worth giving: within about the last hour, longer for slow-release pills, and why it works',
                                     'his paragraph before it, which has them work out what was swallowed and how long ago', None),
    'It only helps with what binds': ('they know charcoal is no use for alcohol or lithium, and that it takes up medication the person needs too',
                                      'what charcoal binds, just said', 'It only helps'),
    "I'd only give it to somebody": ('they know who can be given charcoal and who can\'t, and what happens if they give it anyway',
                                     'the charcoal, just described', "I'd only give it"),
    "If you're unsure charcoal would": ('they know who to ask when they can\'t tell whether charcoal is worth giving',
                                        'the charcoal decision the paragraph before it sets out', 'charcoal would be of any value'),
    "They're also who to ask": ('they know the other cases poison control is for: an unknown substance, a combination, a delayed risk',
                                'poison control, just named', "They're also"),
    "I don't treat calling poison control": ('they know the writer doesn\'t call every time, and why: it depends on the country and on who answers',
                                             'the cases for calling, just given', 'calling poison control'),
    'And what they give you is help': ('they know the call is for deciding, and that the first aid goes on while they talk',
                                       'how useful the call is, just said', 'And what they give you'),
    'Serotonin syndrome can look like': ('they know serotonin syndrome can show up as a seizure or dangerous overheating, like the emergencies in the sections before',
                                         'the sections above, each on one emergency', None),
    'But the rescue measures in those': ('they know those sections\' rescue measures may not treat it, so they check for it whenever something that raises serotonin was taken',
                                         'the emergencies above, just named', 'But the rescue measures'),
    'That includes ayahuasca': ('they know which substances to ask about', 'something that raises serotonin, just said', 'That includes'),
    'That includes anything that works': ('they know which substances to ask about, the MAOIs together first', 'something that raises serotonin, just said', 'That includes'),
    'Too much of any one of them': ('they know the three ways it comes on, and that two of those substances together is the case to suspect most',
                                             'the substances, just listed', 'any one of them'),
}
SRC = {
    'b127': [
        {'point': 'activated charcoal may help after a recent oral ingestion of something that binds to it, in a person fully alert enough to swallow',
         'found': (POST + ', where "recent" and "when the substance binds to it" give the reader nothing to go by; ' + REVIEW +
                   ': give it "as soon as possible, within the first hour of the ingestion", timed-release preparations up to 6 '
                   'hours after; its Box 1 lists what is adsorbed insufficiently or not at all, alcohols and lithium among them. '
                   'The hour, the slow-release note and the two examples are new in the paragraph, from its own source, so the '
                   'card asks him'),
         'still_needed': 'yes: they decide whether charcoal is worth giving from how long ago it was swallowed and what it was', 'fate': 'changed'},
        {'point': 'charcoal does not bind every toxin and can adsorb necessary medication',
         'found': POST + '; ' + REVIEW + ' (Box 1); the remedy entry on activated charcoal says the medication point again with what to do',
         'still_needed': 'yes: they know charcoal is no use for some things and takes up medication the person needs', 'fate': 'changed'},
        {'point': 'aspiration risk in somebody who is vomiting, sedated, seizing or unable to protect the airway',
         'found': (POST + '; ' + REVIEW + ' (contraindications: impaired consciousness with an inadequate swallowing reflex, the '
                   'danger of seizures, repeated vomiting). All four cases stay, each a warning of his post, now with what happens '
                   '("could breathe it into their lungs") and the term after it'),
         'still_needed': 'yes: they know who must not be given charcoal', 'fate': 'changed'},
        {'point': 'poison control may be useful when the substance, the combination, a delayed risk or the value of charcoal is unclear',
         'found': POST + '; fidelity key W033 holds "delayed", "risk" and "value". The four cases stay, the charcoal one first, since it ties the call to the paragraph before',
         'still_needed': 'yes: they know when a call to poison control can help them decide', 'fate': 'changed'},
        {'point': 'he does not treat poison control as a mandatory ritual; its usefulness varies by country and by whoever answers',
         'found': POST + ' (his stance, in the post\'s words); the review he cites says a poison control centre or a doctor should be contacted before a layperson gives charcoal, which the card tells him',
         'still_needed': 'yes: they judge the call by where they are and who picks up', 'fate': 'kept'},
        {'point': 'poison control is decision support, not first aid',
         'found': POST + ', where it is a closing line set against a foil; said here as what the reader does (go on with any first aid while talking to them)',
         'still_needed': 'yes: they keep doing the first aid while they call', 'fate': 'changed'},
    ],
    'b130': [
        {'point': 'serotonin syndrome overlaps with several symptoms above, and the rescue measures in the other branches do not necessarily treat it',
         'found': (POST + '; fidelity key W035 holds "do not", "serotonin", "branches" and "measures". The symptoms are named with '
                   'the words of his paragraph in Swallowed Too Much? ("symptoms of serotonin toxicity, like seizure, dangerous '
                   'overheating, tremor"); tremor is left to How to Check for SS, where it is part of a pattern'),
         'still_needed': 'yes: they check for serotonin syndrome too, and don\'t rely on the other sections\' remedies alone', 'fate': 'changed'},
        {'point': 'it can follow serotonergic medication changes, combinations, or excessive exposure',
         'found': POST + ', where the three are category words; said here as what happened (too much of one, a medication just started or its dose raised, two combined)',
         'still_needed': 'yes: they ask what was taken, how much, and whether anything was started or combined', 'fate': 'changed'},
        {'point': 'ayahuasca and other MAOI brews, MDMA, DXM, many antidepressants, tramadol, linezolid, other MAOIs and some opioids can contribute, especially in combinations',
         'found': (POST + '; every substance stays; "cough syrup", "the painkiller" and "the antibiotic" are step 1\'s own glosses of the same three, brought up to their first mention. '
                   'From try 3 the MAOIs stand together: the post had "linezolid, other MAOIs" side by side, and linezolid is "a reversible monoamine oxidase inhibitor (MAOI)" '
                   '(FDA Drug Safety Communication on linezolid, 2011, read 2026-11-25); tramadol is an opioid, so "some opioids" is "some other opioids" beside it'),
         'still_needed': 'yes: they match what the person took against the list', 'fate': 'changed'},
    ],
}
# what the reads on my first draft (a1) marked that the checked text keeps, and why
KEPT_NOTE = {
    'b127': ('the his-fixes read of my first draft marked the aspiration sentence (the condition said, then its cases) and the '
             'stance sentence ("mandatory ritual", a label); both keep their content: the four cases are warnings of his post '
             'and the stance is his, with "calling poison control" named so "them" can\'t be the medics (the fit read\'s mark)'),
    'b130': ('the his-fixes read of my first draft marked the substance list (a run of names); every substance is his post\'s '
             'and stays, built in two groups; its other marks are changed: the opening is two sentences with two symptoms, '
             '"It" is "Serotonin syndrome", and the change in a medication says what kind'),
}
UNNEEDED = {
    'b127': {"I don't treat calling poison control as a mandatory ritual, though, since how useful they are varies by country and by whoever answers.":
             ('they know the writer doesn\'t call poison control every time and why, so they judge the call by where they are and who '
              'picks up; it is his stance in the post, which stays where it bears on what the reader does')},
    'b130': {},
}


def first(s):
    for k in PAY:
        if s.startswith(k):
            return k
    return None


def fill(key):
    block = key.split('-')[1]
    c = CFG[block]
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--out', str(out),
                        '--section', c['section'], '--reader', c['reader']], capture_output=True, text=True)
    if r.returncode:
        print(key, 'make:', (r.stdout + r.stderr)[-600:]); return 1
    d = json.loads(out.read_text(encoding='utf-8'))
    for s in d['sentences']:
        k = first(s['s'])
        if not k:
            print(key, 'no PAY for:', s['s'][:80]); return 1
        pay, fol, link = PAY[k]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link
    d['checked'] = SRC[block]
    d['placement'] = c['place']
    d['opens']['why_reading'] = c['why']
    d['same_point'] = c['same']
    who = 'a fresh agent (Sonnet) given tools/humanization/%s (reads/%s-a1-%s.txt), on my first draft in its section (TEST-a1-%s.txt); the checked text answers its marks'
    d['needed'] = {'reader': who % ('needed_read_brief.md', 'need', c['reads'], c['reads']),
                   'unneeded': list(UNNEEDED[block]), 'kept': UNNEEDED[block]}
    d['his_fixes'] = {'reader': who % ('his_fixes_brief.md', 'his', c['reads'], c['reads']), 'marked': [], 'kept': {}}
    d['fit'] = {'reader': who % ('fit_read_brief.md', 'fit', c['reads'], c['reads']), 'marked': [], 'kept': {}}
    q = ('PASS: read against the three fresh reads and the tell panel on the text as it stands (reads/*-asis-%s.txt, %s/PANEL.md) '
         'and the three fresh reads on my first draft (reads/*-a1-%s.txt); %s' % (c['reads'], c['panel'], c['reads'], KEPT_NOTE[block]))
    d['questions'] = {k: q for k in d['questions']}
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1800:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in sys.argv[1:]))
