#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's carries (gate E365), as in ../h45-20261112/make_receipts.py,
now with the read against his fixes (gate bad-trips-2026-11-12g, HIS-FIXES.json) beside the needed read (NEEDED.json).

  python3 make_receipts.py KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8')) if (HERE / 'NEEDED.json').exists() else {}
HISFIX = json.loads((HERE / 'HIS-FIXES.json').read_text(encoding='utf-8')) if (HERE / 'HIS-FIXES.json').exists() else {}
LIST = 'none: a list line, a new sign the reader expects after the line before'
CHECK = 'none: a list line, the next check the reader expects after the one before'
R = {
 'chest-c2': {
  'section': 'Chest Pain and Injury',
  'reader': ('someone with a person who has chest pain during or after a trip, deciding whether DMSO alone is enough or they '
             'need to call medics too'),
  'mine': [
   ('they know this part is what to do for chest pain', 'the heading', 'none: the section heading itself, typed with the test'),
   ('they use DMSO alone for chest pain that is mild, familiar and steady, in someone fully alert',
    'it opens the paragraph under its heading', 'none: the first sentence under its heading'),
   ('they know the lines below are what makes chest pain serious', 'after the mild case, the serious one', "It's more serious if"),
   ('they treat severe pain, or pain they have never had before, as serious', 'the first sign', LIST),
   ("they treat pain that won't let up or keeps getting worse as serious", 'the next sign', LIST),
   ('they treat pain that came on with physical effort as serious', 'the next sign', LIST),
   ('they treat pain spreading into an arm or the jaw as serious', 'the next sign', LIST),
   ('they treat shortness of breath or sweating with the pain as serious', 'the next sign', LIST),
   ('they treat any stroke sign from the brain checks as serious, like slurred speech or a drooping face', 'the next sign',
    'from the brain checks above'),
   ('they treat feeling faint or collapsing as serious', 'the last sign', LIST),
   ('they use DMSO and call medics at the same time for serious pain', 'what to do once it is serious', 'Then'),
   ("they treat pain they can't place as the serious kind", 'the case the reader is unsure about', "When you're unsure"),
   ('they let the medics check them even when the pain fades, since DMSO can block pain', 'why the call stands once DMSO works',
    'so if the pain fades'),
  ],
  'placement': ('Chest Pain and Injury, its third paragraph (B124), after his angina story and the cardiovascular science, '
                'before Recent Oral Toxic Ingestion'),
  'why_reading': 'it tells someone with a person in chest pain when DMSO alone is enough, before they read the serious signs',
  'same_point': ('none: read the section from its heading to the next (Recent Oral Toxic Ingestion) for when chest pain is '
                 'serious; the Call medics list\'s chest-pain line names the signs for calling, and this paragraph says how to '
                 'tell the two kinds apart and what to do with DMSO, each its own job (lesson 12d)'),
  'questions': {
   'Q1': 'PASS: the paragraph opens on the mild case and what to do; each line is one sign',
   'Q2': 'PASS: "I\'d just use DMSO", "call medics", "treat it as the serious kind", "let the medics check them": the reader\'s acts',
   'Q3': 'PASS: each sign says which (an arm or the jaw; slurred speech or a drooping face)',
   'Q4': 'PASS: "radiating", "exertional", "persistent" and "neurological changes" said as what the reader sees, with no terms left',
   'Q5': 'PASS: "It\'s more serious if", "Then", "When you\'re unsure", "so if the pain fades" say each relation',
   'Q6': 'PASS: the mild case, the serious signs, what to do, the unsure case, why the call stands',
   'Q7': 'PASS: each line bears on whether to call medics',
   'Q8': 'PASS: all about chest pain during or after a trip',
   'Q9': 'PASS: one sign a line',
  }},
 'brain-c2': {
  'section': 'If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid First',
  'reader': ('someone whose friend says their brain feels damaged, giving DMSO and checking them for signs of a stroke or other '
             'brain injury, to decide whether to call medics'),
  'mine': [
   ('they know this part is for someone who says their brain feels damaged', 'the heading',
    'none: the section heading itself, typed with the test'),
   ('they check the person over while the DMSO works', 'it opens the paragraph under its heading',
    'none: the first sentence under its heading'),
   ('they know several of the checks are recognized stroke warning signs', 'why these checks', 'these checks'),
   ('they check the person is awake', 'the first check', 'First'),
   ('they check breathing and whether the person is very hot', 'the rest of the first check',
    'none: the same first check, its other two parts, which the reader expects'),
   ('they check for slurred speech and a drooping face', 'the next check', CHECK),
   ('they have the person hold both arms out', 'the next check', CHECK),
   ('they know an arm drifting down is a warning sign', 'what the arm check shows', 'If an arm drifts down'),
   ('they watch the person stand and walk, if that is safe', 'the next check', CHECK),
   ('they know losing balance, or bladder or bowel control, counts', 'what the walking check shows', 'counts, and so does'),
   ('they look out for a seizure', 'the next check', CHECK),
   ('they know vomiting again and again is a sign too', 'the next sign', 'as well'),
   ('they ask about a really bad headache and chest pain', 'the next check', CHECK),
   ('they check for a change in vision', 'the last check', CHECK),
   ('they keep up the DMSO while someone calls medics when a check shows a stroke-like sign',
    'what to do when a check shows a sign', 'For objective stroke-like signs'),
   ("they count it as a warning sign when the person can't answer or do the checks", 'the case where the checks cannot be done',
    "When they're too out of it"),
   ('they keep going with DMSO and check again soon when every check passes but the feeling stays',
    'the case where every check passes', 'If everything checks out'),
  ],
  'placement': ('If Someone Says "My Brain Feels Damaged", its second paragraph (B104), after "Do not dismiss that report" and '
                'DMSO first, before his belief in DMSO for stroke (B105); B106\'s first sentence moves here'),
  'why_reading': 'it tells someone giving DMSO to a friend whose brain feels damaged what to check, and what each check shows',
  'same_point': ('merged here: B106\'s first sentence ("For objective stroke-like signs, I would use DMSO immediately while '
                 'someone calls medics."), every word kept, moves here so what to do sits with the checks (both fresh readers '
                 'of the first draft found it missing); B106 keeps the rest'),
  'questions': {
   'Q1': 'PASS: the paragraph opens on checking them over while the DMSO works; each line is one check and what it shows',
   'Q2': 'PASS: "check", "Have them talk and smile", "Ask them", "Watch them", "Look out for", "count that as a warning sign": the reader\'s acts',
   'Q3': 'PASS: which side, which arm, bladder or bowels, vision',
   'Q4': ('PASS: "facial symmetry", "bodily control" and "neurological status" said as what the reader sees ("one side of the '
          'face drooping", "losing control of their bladder or bowels", "what\'s happening in their brain"); "objective '
          'stroke-like signs" is the moved sentence\'s own term, with the checks above it saying which'),
   'Q5': 'PASS: "First", "If an arm drifts down", "and so does", "as well", "When they\'re too out of it", "If everything checks out" say each relation',
   'Q6': 'PASS: the checks, what to do when one shows a sign, the case they can\'t be done, the case they all pass',
   'Q7': 'PASS: each line bears on whether to call medics',
   'Q8': 'PASS: all about checking someone whose brain feels damaged',
   'Q9': 'PASS: one check a line',
  }},
}


# The third drafts (TESTS3 in build_tests.py), the ones checked
import copy  # noqa: E402
R['chest-c3'] = copy.deepcopy(R['chest-c2'])
R['chest-c3']['mine'][5] = ('they treat pain that came on with hard movement, like dancing or climbing stairs, as serious',
                            'the next sign', LIST)
R['chest-c3']['questions']['Q4'] = ('PASS: "radiating", "exertional", "persistent" and "neurological changes" said as what the '
                                    'reader sees ("spreads into an arm or the jaw", "hard movement ... like dancing or '
                                    'climbing stairs", "won\'t let up", "slurred speech or a drooping face")')
R['brain-c3'] = copy.deepcopy(R['brain-c2'])
R['brain-c3']['mine'] = [
 R['brain-c2']['mine'][0], R['brain-c2']['mine'][1],
 ('they know several of the checks look for recognized stroke warning signs', 'why these checks', 'these checks'),
 ('they check the person is awake and breathing normally', 'the first check', 'First'),
 ('they feel whether the person is very hot', 'the next check', CHECK),
 ('they have the person talk and smile', 'the next check', CHECK),
 ('they listen for slurred speech and look for one side of the face drooping', 'what talking and smiling show',
  'Is their speech slurred'),
 ('they have the person hold both arms out and see if one drifts down', 'the next check', CHECK),
 ('they see whether the person keeps their balance walking a few steps, if that is safe', 'the next check', CHECK),
 ('they know wetting or soiling themselves is another sign to watch for', 'what else walking may show', 'another sign'),
 ('they watch for a seizure, and for vomiting that keeps coming back', 'the next signs', CHECK),
 ('they ask about a really bad headache or chest pain', 'the next check', CHECK),
 ('they check whether their vision has changed', 'the last check', CHECK),
 ('they keep the DMSO going while someone calls medics when they see any of these signs', 'what to do when a check shows a sign',
  'So if you see any of these signs'),
 ("they count it as a sign when the person can't answer or do the checks", 'the case where the checks cannot be done',
  "When they're too out of it"),
 R['brain-c2']['mine'][16],
]
R['brain-c3']['same_point'] = ('merged here: B106\'s first sentence ("For objective stroke-like signs, I would use DMSO '
                               'immediately while someone calls medics.") said here as what to do with the checks ("So if you '
                               'see any of these signs, keep the DMSO going while someone calls medics."), since both fresh '
                               'readers of the first draft found it missing; B106 keeps the rest')
R['brain-c3']['questions']['Q4'] = ('PASS: "facial symmetry", "bodily control" and "neurological status" said as what the reader '
                                    'sees ("one side of their face droop", "Wetting or soiling themselves", "too out of it to '
                                    'answer you or do the checks"); no term left')
R['brain-c3']['questions']['Q5'] = ('PASS: "First", "Is their speech slurred", "another sign to watch for", "So if you '
                                    'see", "When they\'re too out of it", "If everything checks out" say each relation')


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
        print(key, 'has', len(rc['sentences']), 'sentences and', len(d['mine']), 'entries:')
        for x in rc['sentences']:
            print('  ', x['s'])
        return
    mine = iter(d['mine'])
    for i, s in enumerate(rc['sentences']):
        payoff, follows, link = next(mine)
        s['payoff'], s['follows'] = payoff, follows
        if i:
            s['link'] = link
    rc['placement'], rc['same_point'], rc['questions'] = d['placement'], d['same_point'], d['questions']
    rc['opens']['why_reading'] = d['why_reading']
    if key in NEEDED:
        rc['needed'] = NEEDED[key]
    if key in HISFIX:
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
