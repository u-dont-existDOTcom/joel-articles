#!/usr/bin/env python3
"""fill_receipts.py - the making-sense receipts of turn 61's serotonin steps, written from his round-50 answers (step 5's
tapping, step 6 from his QUIZ-2 notes, step 7 with his tested seizure line, step 8 with his DMSO answer and Epsom salt).
One round of the three fresh reads came first (reads/*-a5-ss.txt) on version one (TEST-a5-ss-v1.txt); the receipts cite
it, and every sentence it marked that is still in the text is kept with why.

  python3 fill_receipts.py        (makes each receipt with sense_receipt.py make, fills it, checks it)
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(HERE))
import make_reads as M  # noqa: E402

READ = 'a5-ss'
READER = ('a friend sitting with someone who took MDMA on top of their antidepressant and now has twitching muscles, '
          'sweating and a racing heart; they have called an ambulance and read what to do while they wait')
NEED = ('a fresh agent (Sonnet) given tools/humanization/needed_read_brief.md with the whole list, its heading, the line '
        'before it and what it is for (reads/need-%s.txt), on version one (TEST-a5-ss-v1.txt)' % READ)
HISF = ('a fresh agent (Sonnet) given tools/humanization/his_fixes_brief.md, its seventeen ways, with the whole list one '
        'sentence a line (reads/his-%s.txt), on version one' % READ)
FIT = ('a fresh agent (Sonnet) given tools/humanization/fit_read_brief.md, the universal version, with the whole list '
       '(reads/fit-%s.txt), on version one' % READ)
NEW = 'none: a new step, which the reader expects after the one before'
PAY = {
    "And if they have a seizure before the ambulance gets there": ('they do the seizure first aid and watch the breathing while they wait',
                                                    'the ambulance they are waiting for', 'And'),
    "If a seizure comes before the ambulance does": ('they do the seizure first aid while they wait',
                                                    'the ambulance they are waiting for', 'before the ambulance'),
    "And I'd keep track": ('they watch whether the breathing gets better or worse', 'the seizure first aid just named', 'And'),
    "Topical magnesium chloride if": ('they put it on the skin when their friend can\'t swallow, or Epsom salt',
                                      'the case just before, turned around', 'Topical'),
    "But if they feel a strong urge": ('they let their friend tap instead of pacing, which soothes the urge without more heat',
                                       'the urge to move, after the pacing just ruled out', 'But'),
    "If they still show the signs": ('they know when the stronger drink is needed and what it is', 'the drink just named',
                                     'still'),
    "Magnesium Alarm](": ('they know where the signs are', 'the sentence it finishes', 'Magnesium Alarm'),
    "That can be as simple as": ('they can make one from what they have', 'the drink just named', 'That'),
    "If you don't have the flakes": ('they use Epsom salt if that is what they have, knowing it loosens the bowels more',
                                     'the flakes just named', "If you don't have the flakes"),
    "Whatever you give": ('they give it slowly and watch, because potassium could be off either way', 'whatever they just '
                          'made', 'Whatever you give'),
    "MDMA can drain it": ('they know which way potassium can go', 'the colon before it: why their potassium could be low or '
                          'high', 'it'),
    "So I'd stick to food": ('they get potassium from the broth, not a pure powder', 'the risk just named', 'So'),
    "Then I'd tell the medics": ('they tell the medics how the breathing changed', 'the seizure first aid just named',
                                 'Then'),
    "While you wait, you might think of": ('they leave niacin out, knowing why it is unsafe here', 'what they may reach for '
                                           'while they wait', None),
    "[DMSO](": ('they start DMSO by smell or on the skin if there is any sign of an overdose', 'niacin, just ruled out',
                'though'),
    "Then I'd use more": ('they raise it a little at a time, knowing why to go slowly', 'the first use just named', 'Then'),
    "I'd also leave out this guide": ('they leave out the oil too', 'the remedies they may reach for', 'also'),
    "Magnesium chloride is the other one": ('they know magnesium is the other remedy to use, and why', 'DMSO, the first one',
                                            'the other one'),
    "If they're fully alert and able to swallow, I'd": ('they give it by mouth when their friend can swallow, sooner if the jaw '
                                                        'is tense or the muscles twitch, and know where the amounts are',
                                                        'how to give it', "If they're fully alert"),
    "If they're not able to swallow, I'd rub": ('they put it on the skin when their friend can\'t swallow, or Epsom salt',
                                               'the case just before, turned around', "If they're not able to swallow"),
}
CHECKED = {
    'a6-ss5': None, 'a6-ss7b': None, 'a6-ss7c': None, 'a6-ss8': None, 'a7-ss8': None, 'a8-ss8': None,
    'a5-ss5': [{'point': 'tapping the head with the fingertips (the Emotional Freedom Technique) can soothe the urge to keep moving',
                'found': 'his SS-ASKED-2 answer (e) of 2026-11-23 19:07 UTC: "then have them do Emotional Freedom Technique (fingers tapping the head)"',
                'still_needed': 'yes: they have something to give a friend who can\'t stop moving that makes no more heat',
                'fate': 'kept'}],
    'a5-ss6': [{'point': 'potatoes carry potassium; Epsom salt causes more diarrhea than magnesium chloride; potassium can run low or high after MDMA; too much pure potassium is dangerous',
                'found': ('his QUIZ-2 and SS-DRINK answers of 2026-11-23: "potato broth especially for potassium right?"; '
                          '"epsom salts ... do tend to cause more diarrhea than mag chloride but can be used still"; '
                          '"Hyperkalemia however is very common in mdma overdoses from rhabdomyolysis, although can also be hypo"; '
                          '"nobody should be directly consuming too much pure potassium, that\'s dangerous regardless"'),
                'still_needed': 'yes: they know what to make and how to give it',
                'fate': 'kept'}],
    'a5-ss7': [{'point': 'the CDC counts trouble breathing after a seizure as a reason to call 911',
                'found': 'CDC, First Aid for Seizures (cdc.gov/epilepsy/first-aid-for-seizures): call 911 if "They have trouble breathing or waking up after the seizure"',
                'still_needed': 'yes: they know what to tell the medics',
                'fate': 'kept'}],
    'a5-ss8': [{'point': 'DMSO may help prevent seizures; start by smell or on the skin, mixed with about 30% water if it itches, and raise it slowly',
                'found': ('his SS-ASKED-2 answer (c) of 2026-11-23 19:07 UTC: "it looks possible that DMSO could actually help during a seizure -- definitely seems to prevent seizures, so i\'d give it before a seizure if there\'s any indication of an overdose, starting with smelling it and/or rubbing it on a clean patch of skin (add 30% water if it makes skin itchy), and just follow the general guidance of seeing if it helps as you slowly increase the dose"'),
                'still_needed': 'yes: they know how to start it and how to go on',
                'fate': 'kept'},
               {'point': 'seizures have happened during stem cell infusions with DMSO in them',
                'found': 'A case of dimethyl sulfoxide-induced seizure in multiple myeloma (PMC11880447): a seizure during the infusion of DMSO-cryopreserved stem cells; his answer: "stem cell transfusions with more dmso had more seizures"',
                'still_needed': 'yes: they go slowly because of it',
                'fate': 'kept'}],
}
KEPT = {
    "But if they feel a strong urge": 'his remedy (answer e), his ending ("without the over-activity risk"); the term after its plain words, as he puts terms',
    "If they still show the signs": 'his pointer to his MDMA section, as he asked ("we already discussed this before in the guide right?"), and his bold',
    "Magnesium Alarm](": 'the link\'s second half',
    "That can be as simple as": 'his recipe (potato broth, magnesium); the amounts are a question to him on round 51',
    "If you don't have the flakes": 'his trade-off in his words ("can be used still")',
    "Whatever you give": 'his "slowly to see how it affects them" and the direction he asked to have said ("not clear ... whether potassium would be depleted or increased")',
    "MDMA can drain it": 'the direction he asked for, said plainly',
    "So I'd stick to food": 'his limit ("too much pure potassium"), said as what to do',
    "Then I'd tell the medics": 'his act and reason, in his order; the action is telling the medics',
    "And if they have a seizure before the ambulance gets there": 'tied to the ambulance already coming, his "I\'d" and his breathing line',
    "If a seizure comes before the ambulance does": 'tied to the ambulance already coming, his "I\'d"',
    "And I'd keep track": 'his breathing line from round 49, with the seizure now one they had',
    "Topical magnesium chloride if": 'his fragment as he wrote it, with his Epsom salt answer',
    "While you wait, you might think of": 'his niacin reason (answer c of round 49), the list of three as he gave it',
    "[DMSO](": 'his answer (c), in his order: the reason, the condition, how to start',
    "Then I'd use more": 'his "slowly increase the dose", with the reason he gave',
    "I'd also leave out this guide": 'his oil answer is still open (round 51 asks again); this line read Human High in step 8 (a3c02dd9)',
    "Magnesium chloride is the other one": 'his line with one word changed now that DMSO is used',
    "If they're fully alert and able to swallow, I'd": ('his remedy and its condition, the amounts in his MDMA section; why the '
                                                        'jaw and the muscles matter said where the reader asks (his section '
                                                        'treats jaw tension as the earliest warning the body needs more)'),
    "If they're not able to swallow, I'd rub": 'his topical line made a sentence, with his Epsom salt answer',
}
Q = {
    'Q1': 'PASS: each sentence opens on why it is there: the urge, the drink, what to do if, how to give it, the remedy',
    'Q2': 'PASS: every instruction is something the friend does or leaves out, with why',
    'Q3': 'PASS: which drink, which salt, which remedy, what to tell the medics',
    'Q4': 'PASS: the remedies are this guide\'s own, linked to their sections; terms come after their plain words',
    'Q5': 'PASS: each sentence ties to the one before at its start (But, still, That, If you don\'t have, Whatever, So, Then, though, the other one)',
    'Q6': 'PASS: in the order a helper needs it',
    'Q7': 'PASS: every fact is one he gave or a source says',
    'Q8': 'PASS: one remedy a sentence or two',
    'Q9': 'PASS: the payoff first',
}
HISF_FILES = {'a6-ss5': ('HIS-ss5.txt', 'his own: his step 5 of round 48 (card TEACH-SS-STEPS), its first two sentences as he wrote them'),
              'a6-ss7b': ('HIS-ss7b.txt', 'his own: his step 7 of round 49 (QUIZ-1), its first two sentences'),
              'a6-ss7c': ('HIS-ss7b.txt', 'his own: his step 7 of round 49 (QUIZ-1), its first two sentences'),
              'a5-ss5': ('HIS-ss5.txt', 'his own: his step 5 of round 48 (card TEACH-SS-STEPS), its first two sentences as he wrote them'),
              'a5-ss6': ('HIS-ss6.txt', 'his own: his step 6 of round 48, its first sentence as he wrote it'),
              'a5-ss7': ('HIS-ss7.txt', 'his own: his step 7 of round 49 (QUIZ-1) and his seizure line as he checked it on round 50 (1351e4b8)')}
PLACE = {'a8-ss8': 'step 8 of the eight steps under "Act Now on SS" (B136), the last', 'a7-ss8': 'step 8 of the eight steps under "Act Now on SS" (B136), the last', 'a6-ss5': 'step 5 of the eight steps under "Act Now on SS" (B136)', 'a6-ss7b': 'step 7 of the eight steps under "Act Now on SS" (B136)', 'a6-ss7c': 'step 7 of the eight steps under "Act Now on SS" (B136)', 'a6-ss8': 'step 8 of the eight steps under "Act Now on SS" (B136), the last',
         'a5-ss5': 'step 5 of the eight steps under "Act Now on SS" (B136)', 'a5-ss6': 'step 6 of the eight steps under "Act Now on SS" (B136)',
         'a5-ss7': 'step 7 of the eight steps under "Act Now on SS" (B136)', 'a5-ss8': 'step 8 of the eight steps under "Act Now on SS" (B136), the last'}
WHY = {'a8-ss8': 'it tells the friend which of this guide\'s remedies to leave out and which to use while they wait', 'a7-ss8': 'it tells the friend which of this guide\'s remedies to leave out and which to use while they wait', 'a6-ss5': 'it tells the friend how to calm someone overstimulated without making more heat', 'a6-ss7b': 'it tells the friend what the ER doctors will need, and what to do if a seizure comes', 'a6-ss7c': 'it tells the friend what the ER doctors will need, and what to do if a seizure comes', 'a6-ss8': 'it tells the friend which of this guide\'s remedies to leave out and which to use while they wait',
       'a5-ss5': 'it tells the friend how to calm someone overstimulated without making more heat',
       'a5-ss6': 'it tells the friend what to drink and how to give it',
       'a5-ss7': 'it tells the friend what the ER doctors will need, and what to do if a seizure comes',
       'a5-ss8': 'it tells the friend which of this guide\'s remedies to leave out and which to use while they wait'}


def first(s, body=''):
    for k in PAY:
        if s.startswith(k):
            return k
    for sent in re.split(r'(?<=[.!?])\s+', body):
        if s in sent and not sent.startswith(s):
            return first(sent)
    return None


def marks(rs):
    his, fit, need = [], [], []
    for line in (HERE / 'reads' / ('his-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+)(?:/S?(\d+))?[^:]*:\s*([\d, ]+)\s*[—-]', line)
        if m:
            for n in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1):
                his.append({'s': rs[n - 1], 'difference': m.group(3).strip()})
    for line in (HERE / 'reads' / ('fit-%s.txt' % READ)).read_text(encoding='utf-8').splitlines():
        m = re.match(r'\s*-\s*S(\d+):\s*(.*)$', line)
        if m:
            found = [q for q in ('ANYWAY', "CAN'T TELL", 'FROM', 'MISREAD') if re.search(re.escape(q) + r' yes', m.group(2))]
            if found:
                fit.append({'s': rs[int(m.group(1)) - 1], 'found': ', '.join(found)})
    return his, fit, need


def fill(key):
    text, out = HERE / ('TEST-%s.txt' % key), HERE / ('TEST-%s.receipt.json' % key)
    cmd = [sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--out', str(out),
           '--section', 'Act Now on SS', '--reader', READER]
    if key in HISF_FILES:
        cmd += ['--his', str(HERE / HISF_FILES[key][0]), '--whose', HISF_FILES[key][1]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(key, 'make:', (r.stdout + r.stderr)[-600:]); return 1
    d = json.loads(out.read_text(encoding='utf-8'))
    body = ' '.join(s['s'] for s in d['sentences'])
    for s in d['sentences']:
        if s.get('his'):
            continue
        k = first(s['s'], body)
        if not k:
            print(key, 'no PAY for:', s['s'][:80]); return 1
        pay, fol, link = PAY[k]
        s['payoff'], s['follows'] = pay, fol
        if 'link' in s:
            s['link'] = link or NEW
    d['checked'] = CHECKED.get(key) or CHECKED[{'a6-ss5': 'a5-ss5', 'a6-ss7b': 'a5-ss7', 'a6-ss7c': 'a5-ss7', 'a6-ss8': 'a5-ss8', 'a7-ss8': 'a5-ss8', 'a8-ss8': 'a5-ss8'}[key]]
    d['placement'] = PLACE[key]
    d['opens']['why_reading'] = WHY[key]
    d['same_point'] = ('none: read the section from its heading to the next (Serotonin Syndrome (SS)?, How to Check for SS, '
                       'Act Now on SS); the signs and the magnesium amounts are linked to MDMA: Magnesium Alarm, not said again')
    rs = M.sentences((HERE / ('TEST-%s-v1.txt' % READ)).read_text(encoding='utf-8').strip())
    his, fit, need = marks(rs)
    mine = [s['s'] for s in d['sentences'] if not s.get('his')]
    hiss = [s['s'] for s in d['sentences'] if s.get('his')]
    HIS_OWN = 'his own words, kept as he wrote them'
    def kept_for(lst):
        out = {}
        for x in lst:
            if x in hiss:
                out[x] = HIS_OWN
            elif x in mine:
                out[x] = KEPT.get(first(x, body)) or 'changed in version two'
        return out
    d['needed'] = {'reader': NEED, 'unneeded': [], 'kept': {}}
    hm = [m for m in his if m['s'] in mine or m['s'] in hiss]
    fm = [m for m in fit if m['s'] in mine or m['s'] in hiss]
    d['his_fixes'] = {'reader': HISF, 'marked': hm, 'kept': kept_for([m['s'] for m in hm])}
    d['fit'] = {'reader': FIT, 'marked': fm, 'kept': kept_for([m['s'] for m in fm])}
    d['questions'] = Q
    out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    res = (r.stdout + r.stderr).strip()
    print(key, 'receipt check:', res[-1500:] if r.returncode else res.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(fill(k) for k in (sys.argv[1:] or ('a5-ss5', 'a5-ss6', 'a5-ss7', 'a5-ss8'))))
