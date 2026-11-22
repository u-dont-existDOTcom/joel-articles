#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's carries (gate E365), as in ../h48-20261112/make_receipts.py,
with the read against his fixes (gate bad-trips-2026-11-12g, HIS-FIXES.json) and the needed read (NEEDED.json).

  python3 make_receipts.py KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8'))
HISFIX = json.loads((HERE / 'HIS-FIXES.json').read_text(encoding='utf-8'))
SIGN = 'none: a list line, the next sign the lead-in says the list holds'
STEP = 'none: a list line, the next step the lead-in says the list holds'
HIS = 'none: his line (round 38, 4739068c), the next one in his list'
R = {
 'brainopen-c1': {
  'section': 'If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid + Electrolytes First',
  'reader': ('someone whose friend says their brain feels damaged, deciding what to do first and whether to call medics'),
  'mine': [
   ('they know this part is for someone who says their brain feels damaged, and what comes first', 'the heading',
    'none: the section heading, his (round 38)'),
   ('they take the report seriously even when the person is high or can\'t explain it', 'it opens the section under its heading',
    'none: the first sentence under its heading'),
   ('they give DMSO first while they ask about the symptoms', 'what to do, after taking it seriously', 'DMSO is my first'),
   ('they know within about a minute whether the DMSO is helping', 'what to expect from it', 'whether it is helping'),
   ('they try smelling or tasting a little humic acid too', 'the next remedy the heading names', 'can also help'),
   ('they give electrolytes too, knowing why and that they are not enough alone', 'the last remedy the heading names',
    'I add electrolytes too'),
   ('they check for stroke warning signs while the DMSO works, and call medics for any', 'his lead-in to the checks',
    'While the DMSO is working'),
   ('they look for unconsciousness or abnormal breathing', 'his first sign', HIS),
   ('they feel whether the person is very hot', 'his next sign', HIS),
   ('they have the person talk and smile', 'his next check', HIS),
   ('they listen for slurred speech and look for a drooping face', 'what talking and smiling show', 'Is their speech slurred'),
   ('they have the person hold both arms out and see if one drifts down', 'his next check', HIS),
   ('they check balance on a few steps while holding the person', 'his next check', HIS),
   ('they watch for wetting or soiling', 'his next sign', HIS),
   ('they watch for a seizure and for vomiting that keeps coming back', 'his next signs', HIS),
   ('they ask about a really bad headache or chest pain', 'his next check', HIS),
   ('they check whether vision has changed', 'his last check', HIS),
   ('they call for help when the checks can\'t be done or the feeling stays despite treatment', 'his last line',
    "When they're too out of it"),
  ],
  'placement': ('If Someone Says "My Brain Feels Damaged", its first paragraph (B103) before his checks (round 38); B105\'s '
                'belief in DMSO for stroke after them'),
  'why_reading': 'it tells someone whose friend says their brain feels damaged to take it seriously and what to give first',
  'same_point': ('none: read the section from its heading to the next (Active Seizure) for taking the report seriously and '
                 'what to give first; B103\'s three opening sentences are said once here, his checks and closing line say when '
                 'to call, and B106\'s first sentence, which said it again, is gone (round 38)'),
  'questions': {
   'Q1': 'PASS: the paragraph opens on what to do with the report ("Don\'t dismiss ..."), the remedies right after',
   'Q2': 'PASS: "Don\'t dismiss", "DMSO is my first immediate remedy", "I add electrolytes too": the reader\'s acts',
   'Q3': 'PASS: "someone who says their brain feels damaged" says who; the remedies are named',
   'Q4': 'PASS: "acute neurological dysfunction" said as "something could really be going wrong in their brain"; no term left',
   'Q5': 'PASS: "just because", "since", "while", "too", "because" say each relation',
   'Q6': 'PASS: take it seriously, what to give, then his checks and when to call',
   'Q7': 'PASS: each sentence bears on what to do for someone whose brain feels damaged',
   'Q8': 'PASS: one section, the brain report',
   'Q9': 'PASS: the opening is one step; his lines are his',
  }},
 'seize-c3': {
  'section': 'Active Seizure',
  'reader': 'someone whose friend is having a seizure right now, deciding what to do while it lasts and when to call medics',
  'mine': [
   ('they know this part is for a seizure happening now', 'the heading', 'none: the section heading itself'),
   ('they time the seizure and do the steps below while it lasts', 'it opens the section under its heading',
    'none: the first sentence under its heading'),
   ('they move dangerous objects, especially hard or sharp ones, away from the person', 'the first step', STEP),
   ('they loosen tight clothing', 'the next step', STEP),
   ('they turn the person gently onto their side to help them breathe', 'the next step', STEP),
   ('they don\'t restrain the person, since that can cause injuries', 'the next step, a don\'t with its reason', STEP),
   ('they keep everything out of the person\'s mouth while they\'re convulsing or not fully conscious', 'the last step', STEP),
   ('they know the lines below are when to call medics', 'after what to do, when to get help', 'Call medics if'),
   ('they call medics for a convulsive seizure of about five minutes, which is why they timed it', 'the first sign', SIGN),
   ('they call medics when another seizure starts before recovery', 'the next sign', SIGN),
   ('they call medics when breathing gets slow and shallow', 'the next sign', SIGN),
   ('they call medics for blue or gray lips', 'the next sign', SIGN),
   ('they call medics for dangerous heat, not just sweating', 'the next sign', SIGN),
   ('they call medics for a serious injury, like bleeding that won\'t stop or a possible head injury', 'the next sign', SIGN),
   ('they call medics for a first seizure or one unlike their usual ones', 'the last sign', SIGN),
  ],
  'placement': ('Active Seizure, its first paragraph (B109) and its call-medics line (B112) moved to follow it, before the '
                'rescue medicine (B110) and What Else May Help'),
  'why_reading': 'it tells someone with a friend in a seizure what to do while it lasts, then when to call medics',
  'same_point': ('kept: the Call medics list at the top holds these signs too, and the lane\'s locks keep a call-for-help line '
                 'where the reader acts in an emergency (lesson bad-trips-2026-11-12b names this one); its lines say what '
                 'counts the way the Call medics list does ("not just regular sweating", "blue or gray")'),
  'questions': {
   'Q1': 'PASS: the section opens on what to do while it lasts; the call list says its action first',
   'Q2': 'PASS: each line is something the helper does, or a sign that has them call',
   'Q3': 'PASS: "hard or sharp", "slow and shallow", "blue or gray", "bleeding that won\'t stop or a possible head injury"',
   'Q4': 'PASS: no term left; "respiratory" said as breathing',
   'Q5': 'PASS: "and while it lasts:", "Call medics if any of these happen:" say what each list is',
   'Q6': 'PASS: time it, what to do while it lasts, when to call',
   'Q7': 'PASS: each line bears on a seizure happening now',
   'Q8': 'PASS: the steps are steps and the signs are signs',
   'Q9': 'PASS: one step or sign a line',
  }},
}

import copy  # noqa: E402
R['seize-c4'] = copy.deepcopy(R['seize-c3'])
R['seize-c4']['mine'][11] = ('they call medics for lips turning blue or gray, knowing it means too little air', 'the next sign', SIGN)

R['seize-c5'] = copy.deepcopy(R['seize-c3'])
R['seize-c5']['mine'][11] = ('they call medics when the lips turn blue or gray', 'the next sign', SIGN)

R['er-c1'] = {
 'section': 'Acute Medical and Neurological Rescue',
 'reader': 'someone with a friend in a severe trip, deciding whether to handle it themselves or take them to an emergency room',
 'mine': [
  ('they know this part is about medical and neurological rescue', 'the heading', 'none: the section heading itself'),
  ('they calm and stabilize the trip where the person is, unless a Call medics sign shows up or they can\'t keep them from '
   'getting hurt', 'it opens the section under its heading (acute-c1, in the guide)', 'none: the first sentence under its heading'),
  ('they know staying can bring the person down faster than an ambulance and hours in an emergency room', 'why stay',
   'that way'),
  ('they know a scared, psychotic-feeling person will often get a benzodiazepine in an emergency room',
   'what the emergency room would do, after why stay', 'In an emergency room'),
  ('they know a benzodiazepine only sometimes helps psychosis and can bring on more agitation or fear',
   'what that drug does', 'Those'),
  ('they know antipsychotics carry their own risks and the staff may not know what was taken',
   'the other drug they may get there', 'Antipsychotics'),
 ],
 'placement': ('Acute Medical and Neurological Rescue, its emergency room paragraph (B77) after its opening (B100, acute-c1), '
               'before the image and My Brain Feels Damaged'),
 'why_reading': 'it tells someone deciding against the emergency room what a scared person would likely get there',
 'same_point': ('merged here: B77\'s first sentence ("The emergency room is not magic, and for a physiologically stable '
                'psychedelic or practice-induced crisis it may be a poor environment.") says what acute-c1\'s last sentence '
                'says, so it goes'),
 'questions': {
  'Q1': 'PASS: the paragraph opens on what happens in an emergency room, the reason the opening gives for staying',
  'Q2': 'PASS: the reader acts on it by staying; each sentence says what the staff would do',
  'Q3': 'PASS: "a benzodiazepine", "antipsychotics", "the staff giving them"',
  'Q4': 'PASS: "paradoxical" said right where it is used ("more agitation or fear instead, a paradoxical reaction")',
  'Q5': 'PASS: "Those", "but", "and" say each relation',
  'Q6': 'PASS: what they would get, what it does, the other drug',
  'Q7': 'PASS: each sentence bears on whether to go to the emergency room',
  'Q8': 'PASS: one paragraph on the emergency room',
  'Q9': 'PASS: one drug a sentence',
 }}

R['er-c2'] = copy.deepcopy(R['er-c1'])
R['er-c2']['mine'] = R['er-c1']['mine'][:4] + [
  ('they don\'t count on the benzodiazepine helping, since it can bring on more agitation or fear', 'what that drug does',
   "Don't count on it"),
  ('they know antipsychotics may work better but carry their own risks and interactions', 'the other drug they may get there',
   'Antipsychotics'),
  ('they tell the staff what was taken if they do end up there', 'what to do with that, last', 'so if you do end up there'),
]
R['er-c2']['questions']['Q2'] = 'PASS: "Don\'t count on it", "tell them": the reader\'s acts'
R['er-c2']['questions']['Q5'] = 'PASS: "since", "but", "also", "so" say each relation'
R['er-c2']['questions']['Q6'] = 'PASS: what they would get, what it does, the other drug, what to do there'

R['er-c3'] = copy.deepcopy(R['er-c2'])
R['er-c3']['mine'][4] = ('they don\'t count on the benzodiazepine helping, since it can bring on a paradoxical reaction, more '
                         'agitation or fear', 'what that drug does', "Don't count on it")


def fill(key):
    text = HERE / ('TEST-%s.txt' % key)
    out = HERE / ('TEST-%s.receipt.json' % key)
    d = R[key]
    r = subprocess.run([sys.executable, str(SR), 'make', str(text), '--section', d['section'], '--reader', d['reader'], '--out',
                        str(out)], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout, r.stderr); return
    rc = json.loads(out.read_text(encoding='utf-8'))
    if len(rc['sentences']) != len(d['mine']):
        print(key, 'has', len(rc['sentences']), 'sentences and', len(d['mine']), 'entries'); return
    for i, (s, (payoff, follows, link)) in enumerate(zip(rc['sentences'], d['mine'])):
        s['payoff'], s['follows'] = payoff, follows
        if i:
            s['link'] = link
    rc['placement'], rc['same_point'], rc['questions'] = d['placement'], d['same_point'], d['questions']
    rc['opens']['why_reading'] = d['why_reading']
    rc['needed'] = NEEDED[key]
    rc['his_fixes'] = HISFIX[key]
    out.write_text(json.dumps(rc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    o = (c.stdout + c.stderr).strip()
    print(key, o.splitlines()[-1] if o else c.returncode)
    if c.returncode:
        print(o)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
