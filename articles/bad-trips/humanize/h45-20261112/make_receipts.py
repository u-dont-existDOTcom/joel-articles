#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's tests (gate E365), as in ../h44-20261112/make_receipts.py.
Neither test has a sentence he wrote himself: both carry his round-35 moves (lesson bad-trips-2026-11-12e) in my words, so
every sentence has a payoff, a follows and a link of mine.

  python3 make_receipts.py KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8')) if (HERE / 'NEEDED.json').exists() else {}
R = {
 'ss-r1': {
  'section': 'Suspected Serotonin Syndrome (SS): Recognizing serotonin toxicity',
  'reader': ('someone with a person who may have taken too much of a serotonergic substance (MDMA, an MAOI brew, '
             'antidepressants), checking whether it looks like serotonin toxicity and when to get medical help'),
  'mine': [
   ('they know this part is how to tell whether it looks like serotonin toxicity', 'the sub-heading',
    'none: the sub-heading itself, typed with the test'),
   ('they know any one of the patterns below is enough to suspect serotonin toxicity',
    'it opens the part under its sub-heading', 'none: the first sentence under its sub-heading'),
   ('they check whether the muscles jerk in a rhythm on their own (spontaneous clonus)', 'the first of the patterns',
    'none: the first of the patterns the sentence before announces, asked as a question'),
   ('they check whether the rhythm starts when a muscle is stretched, with agitation or sweating (inducible clonus)',
    'the same rhythm, brought on', 'Or does that rhythm'),
   ('they check the eyes for a fast rhythm with agitation or sweating (ocular clonus)', 'the same rhythm in the eyes',
    'again with agitation or sweating'),
   ('they check for shaking with abnormally brisk reflexes (tremor and hyperreflexia)', 'the next pattern',
    'none: the next pattern in the list, a new question the reader expects'),
   ('they check for rigid muscles with a temperature over 38°C (100.4°F) and eye or inducible clonus (hypertonia and fever)',
    'the last pattern', 'Or are their muscles'),
   ("they act without waiting to see every pattern", 'after the patterns, what to do with them', 'though'),
   ('they get medical help for dangerous heat, rigidity, clonus, confusion or rapid worsening', 'what to act on',
    'none: it names what to act on, which the sentence before said not to wait for'),
  ],
  'placement': ('Suspected Serotonin Syndrome, under its sub-heading Recognizing serotonin toxicity, after the paragraph on '
                'what can cause it and before what to do immediately (B131 to B134)'),
  'why_reading': ('it tells someone worried about serotonin toxicity that any one of these patterns is enough to suspect it, '
                  'before they work through the patterns'),
  'same_point': ('none: read the section from its heading to the next (Do this immediately) for the patterns and when to '
                 'act; the Call medics list names "clonus with fever" and "severe rigidity" as reasons to call, and this '
                 'part says how to recognize them, so each stays where it does its job (lesson 12d)'),
  'questions': {
   'Q1': 'PASS: the part opens on "any one of these patterns makes serotonin toxicity more likely"; each question names the sign before its term',
   'Q2': "PASS: each question is something the reader checks on the person; the last two lines say what to do",
   'Q3': 'PASS: each pattern says which muscles, eyes or reflexes, and the temperature in both units',
   'Q4': 'PASS: clonus, hyperreflexia and hypertonia each said in plain words where first used, the term in brackets after',
   'Q5': 'PASS: "Or does that rhythm", "again", "Or are their muscles", "though" say each relation',
   'Q6': 'PASS: the patterns, then not waiting for all of them, then what to act on',
   'Q7': 'PASS: each pattern bears on whether it looks like serotonin toxicity',
   'Q8': 'PASS: all about recognizing serotonin toxicity and when to get help',
   'Q9': 'PASS: one pattern a question',
  }},
 'acute-r1': {
  'section': 'Acute Medical and Neurological Rescue',
  'reader': ('someone with a person in a severe altered state, deciding whether they can calm and stabilize it where they '
             'are or need an ambulance'),
  'mine': [
   ('they know this part is the medical and neurological emergencies', 'the heading',
    'none: the section heading itself, typed with the test'),
   ('they act now, and know the fastest help may be right where they are', 'it opens the section under its heading',
    'none: the first sentence under its heading'),
   ('they know a physically stable person may come down sooner with their help than after an ambulance ride and hours in an '
    'emergency room', 'why the fastest help may be where they are', 'Someone who\'s severely altered but physically stable'),
   ('they check the body before deciding', 'how to tell if they are physically stable', 'So'),
   ('they check breathing and temperature', 'the first check', 'none: the first of the checks the sentence before announces'),
   ('they check for seizures and any sign of a brain injury', 'the next check',
    'none: the next check, a new question the reader expects'),
   ('they check the person is awake enough to work with them and can be kept physically safe', 'the last check',
    'none: the last check, a new question the reader expects'),
   ('they calm and stabilize the trip where they are when every check passes', 'what the checks decide', "If all of that's true"),
  ],
  'placement': ('Acute Medical and Neurological Rescue, the medical part\'s first two paragraphs (B100 and B76), after the '
                'tripsitting part and before why the emergency room may be a poor place for a stable crisis (B77)'),
  'why_reading': ('it tells someone facing a severe altered state to act now, and that the fastest help may be right where '
                  'they are'),
  'same_point': ('none: read the section from its heading to the next (If Someone Says "My Brain Feels Damaged") for when '
                 'calming the trip where they are may be enough; B77 says why the emergency room may be a poor place for '
                 'it, and the Call medics list says when to call, each doing its own job'),
  'questions': {
   'Q1': 'PASS: the section opens on acting now and where the fastest help may be; the checks open on "So check the body first"',
   'Q2': "PASS: each check is something the reader asks of the person or of themselves",
   'Q3': 'PASS: breathing, temperature, seizures, a brain injury, wakefulness and physical safety: each check says which',
   'Q4': 'PASS: "physically stable" is said by the checks that follow; "neurological-injury concern" said as anything suggesting a brain injury',
   'Q5': 'PASS: "So" and "If all of that\'s true" say each relation; the checks are a list the reader expects',
   'Q6': 'PASS: acting now, why the fastest help may be here, then how to tell',
   'Q7': 'PASS: each line bears on whether to calm the trip here or call',
   'Q8': 'PASS: all about deciding between help where they are and an ambulance',
   'Q9': 'PASS: one check a question',
  }},
}


# The second tries (h45b): the same units, their sentences said again
import copy  # noqa: E402
R['ss-r1-fix2'] = copy.deepcopy(R['ss-r1'])
R['ss-r1-fix2']['mine'] = [
 R['ss-r1']['mine'][0], R['ss-r1']['mine'][1],
 ('they check whether the muscles jerk in a rhythm on their own, and know that is clonus', 'the first of the patterns',
  'none: the first of the patterns the sentence before announces, asked as a question'),
 ('they check whether the jerking starts when a muscle is stretched, with agitation or sweating', 'the same jerking, brought on',
  'Does the jerking'),
 ('they check the eyes for a rhythm with agitation or sweating', 'the same rhythm in the eyes', 'again with agitation or sweating'),
 ('they check for shaking with reflexes that are too brisk', 'the next pattern',
  'none: the next pattern in the list, a new question the reader expects'),
 ('they check for rigid muscles with a temperature over 38°C (100.4°F) and eye or stretch-triggered clonus', 'the last pattern',
  'that eye or stretch-triggered clonus'),
 R['ss-r1']['mine'][7], R['ss-r1']['mine'][8],
]
R['ss-r1-fix2']['questions']['Q4'] = ('PASS: clonus said in plain words and named once, where first used ("that\'s called '
                                      'clonus"); the other signs said only in plain words, since the reader acts on the signs')
R['ss-r1-fix2']['questions']['Q5'] = 'PASS: "Does the jerking", "again", "that eye or stretch-triggered clonus", "though" say each relation'
R['acute-r1-fix2'] = copy.deepcopy(R['acute-r1'])
R['acute-r1-fix2']['mine'] = [
 R['acute-r1']['mine'][0],
 R['acute-r1']['mine'][1],
 ('they know they may bring a physically stable person down faster themselves than an ambulance ride and hours in an '
  'emergency room would', 'when helping them where they are is the faster help', "If they're severely altered but physically stable"),
 R['acute-r1']['mine'][3], R['acute-r1']['mine'][4],
 ('they check for seizures and anything that looks like a brain injury', 'the next check',
  'none: the next check, a new question the reader expects'),
 ('they check the person is awake enough to work with them and can be kept from getting hurt', 'the last check',
  'none: the last check, a new question the reader expects'),
 ('they calm and stabilize the trip where they are when every check passes', 'what the checks decide', 'If all that checks out'),
]
R['acute-r1-fix2']['questions']['Q4'] = ('PASS: "physically stable" said by the checks that follow; "neurological-injury concern" '
                                         'said as anything that looks like a brain injury, "conscious enough to cooperate" as '
                                         'awake enough to work with you')
R['acute-r1-fix2']['questions']['Q5'] = 'PASS: "If", "So" and "If all that checks out" say each relation'


def fill(key):
    text = HERE / ('TEST-%s.txt' % key)
    out = HERE / ('TEST-%s.receipt.json' % key)
    d = R[key]
    cmd = [sys.executable, str(SR), 'make', str(text), '--section', d['section'], '--reader', d['reader'], '--out', str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); return
    rc = json.loads(out.read_text(encoding='utf-8'))
    mine = iter(d['mine'])
    first = True
    for s in rc['sentences']:
        payoff, follows, link = next(mine)
        s['payoff'], s['follows'] = payoff, follows
        if not first:
            s['link'] = link
        first = False
    rc['placement'], rc['same_point'], rc['questions'] = d['placement'], d['same_point'], d['questions']
    rc['opens']['why_reading'] = d['why_reading']
    if key in NEEDED:
        rc['needed'] = NEEDED[key]
    out.write_text(json.dumps(rc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    o = (c.stdout + c.stderr).strip()
    print(key, o.splitlines()[-1] if o else c.returncode)
    if c.returncode:
        print(o)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
