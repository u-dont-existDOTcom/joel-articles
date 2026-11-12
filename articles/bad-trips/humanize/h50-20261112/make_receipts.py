#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's carries (gate E365), with the needed read (NEEDED.json),
the read against his fixes (HIS-FIXES.json, gate bad-trips-2026-11-12g) and the fit read (FIT.json, gate
bad-trips-2026-11-12j).

  python3 make_receipts.py KEY...
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8'))
HISFIX = json.loads((HERE / 'HIS-FIXES.json').read_text(encoding='utf-8'))
FIT = json.loads((HERE / 'FIT.json').read_text(encoding='utf-8'))
HIS = 'none: his line (5e41c575, 19:44 UTC), the next one in his list'
R = {
 'rescue-c8': {
  'section': 'Active Seizure',
  'reader': ('someone whose friend is having a seizure right now, deciding what to do while it lasts, when to call medics, '
             'and whether to give a rescue medicine they have'),
  'mine': [
   ('they know this part is for a seizure happening now', 'the heading', 'none: the section heading itself'),
   ('they time the seizure and do the steps below while it lasts', 'his lead-in', 'none: the first sentence under its heading'),
   ('they move dangerous objects away, especially hard or sharp ones', 'his first step', HIS),
   ('they don\'t restrain the person, and put pillows under their head', 'his next step', HIS),
   ('they loosen tight clothing', 'his next step', HIS),
   ('they turn the person gently onto their side to help them breathe', 'his next step', HIS),
   ('they keep everything out of the person\'s mouth', 'his last step', HIS),
   ('they know the lines below are when to call medics', 'his second lead-in', 'Call medics if'),
   ('they call medics for a convulsive seizure over 5 minutes', 'his first sign', HIS),
   ('they call medics when breathing gets slow and shallow', 'his next sign', HIS),
   ('they call medics when the lips turn blue or gray', 'his next sign', HIS),
   ('they call medics for dangerous heat', 'his next sign', HIS),
   ('they call medics for a head injury, a broken bone or bleeding that won\'t stop', 'his last sign', HIS),
   ('they give a rescue medicine for seizures, if there is one, when and how its label says', 'what else to do, after when to call',
    'If there\'s a rescue medicine'),
   ('they know it is a benzodiazepine, the drug doctors give first for a seizure that won\'t stop', 'what the medicine is',
    'These are benzodiazepines'),
   ('they know the forms that don\'t need swallowing, since a pill is no use during a seizure', 'what form it comes in',
    'They come in forms'),
   ('they recognize an intramuscular shot as a rescue medicine too', 'the last form', 'A few are'),
   ('they keep watching the person\'s breathing after giving it, more closely if opioids or alcohol were taken too',
    'what to do after giving it, and why', 'After giving it'),
  ],
  'placement': ('Active Seizure, its rescue medicine paragraph (B110), after his first aid and call list, before What Else May '
                'Help'),
  'why_reading': 'it tells someone with a rescue medicine on hand to give it as its label says, and what to watch for after',
  'same_point': ('none: read the section from its heading to What Else May Help for the rescue medicine; the call list says '
                 'when to call medics and this paragraph what to give, and its breathing sign is the call list\'s own words'),
  'questions': {
   'Q1': 'PASS: the paragraph opens on what to do with a rescue medicine on hand, then what it is, its forms, and what to watch',
   'Q2': 'PASS: "follow its label for when and how to give it", "keep watching their breathing": the helper\'s acts',
   'Q3': 'PASS: "a rescue medicine for seizures", "like one they carry for epilepsy", "a nasal spray or a rectal gel"',
   'Q4': 'PASS: "respiratory depressants" said with what they are ("like opioids or alcohol")',
   'Q5': 'PASS: "These are", "because", "since", "especially if" say each relation, no connector twice in my sentences',
   'Q6': 'PASS: what to do, what it is, its forms, what to watch after',
   'Q7': 'PASS: each sentence bears on giving a rescue medicine now',
   'Q8': 'PASS: one paragraph on the rescue medicine',
   'Q9': 'PASS: one point a sentence, the breathing sentence with its reason',
  }},
 'brainev-c1': {
  'section': 'If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid + Electrolytes First',
  'reader': 'someone whose friend says their brain feels damaged, deciding whether to trust DMSO for it',
  'mine': [
   ('they know this part is for someone who says their brain feels damaged', 'the heading', 'none: the section heading, his'),
   ('they know he trusts DMSO for stroke and acute brain damage more than anything else at hand', 'his belief, first',
    'none: the first sentence of the paragraph'),
   ('they know his judgment goes further than the studies, and the studies point the same way', 'how far the evidence goes',
    'that evidence'),
   ('they know people after a clot stroke may have recovered better on DMSO in a preliminary trial', 'the first study',
    'People who\'d had a stroke'),
   ('they know doctors used it to bring down dangerous pressure inside the skull', 'the second study', 'Doctors have also'),
   ('they know it may still help if they start late, from animal stroke research', 'the third study and what it means for them',
    'And animal stroke research'),
   ('they know it protects brain cells from the overexcitation that kills them after a stroke', 'how it works',
    'It also suppresses'),
  ],
  'placement': ('If Someone Says "My Brain Feels Damaged", its evidence paragraph (B105), after his checks and closing line, before '
                'the bleed paragraph (B106)'),
  'why_reading': 'it tells someone giving DMSO for a brain-damage feeling why he trusts it, and how far the evidence goes',
  'same_point': ('none: read the section from its heading to Active Seizure for why DMSO; B103 says to give it first, this '
                 'paragraph says why he trusts it'),
  'questions': {
   'Q1': 'PASS: his belief first, then how far the evidence goes, then each study',
   'Q2': 'PASS: the reader acts on it by trusting DMSO, and by starting it even when late',
   'Q3': 'PASS: "a stroke from a clot", "dangerous pressure inside the skull", "the area of the brain that died"',
   'Q4': 'PASS: "intracranial hypertension", "infarct" and "ischemia" said plainly; "NMDA- and AMPA-mediated excitotoxicity" explained where used',
   'Q5': 'PASS: "but", "also", "And", "so", "It also" say each relation',
   'Q6': 'PASS: belief, how far the evidence goes, the studies, how it works',
   'Q7': 'PASS: each study bears on trusting DMSO for a damaged brain',
   'Q8': 'PASS: one paragraph on why DMSO',
   'Q9': 'PASS: one study a sentence',
  }},
}


# rescue-c9 and brainev-c2: the next drafts, after rescue-c8 (ed4fe070) and brainev-c1 (a8a986e7) read AI.
R['rescue-c9'] = dict(R['rescue-c8'])
R['rescue-c9']['mine'] = R['rescue-c8']['mine'][:13] + [
   ('they give a rescue medicine for seizures, if there is one, when and how its label says', 'what else to do, after when to call',
    'If there\'s a rescue medicine'),
   ('they know what they hold is a benzodiazepine, what doctors give first for a seizure that won\'t stop', 'what the medicine is',
    'It\'s a benzodiazepine'),
   ('they know it will be a nasal spray, a rectal gel or a shot, since a pill is no use during a seizure', 'what form it comes in',
    'Because a pill is no use'),
   ('they keep watching the person\'s breathing after giving it, more closely if opioids or alcohol were taken too',
    'what to do after giving it, and why', 'After giving it'),
]
R['rescue-c9']['questions'] = dict(R['rescue-c8']['questions'],
   Q1='PASS: the paragraph opens on what to do with a rescue medicine on hand, then what it is, its forms, and what to watch',
   Q5='PASS: "which is what", "Because", "since", "especially if" say each relation, no connector twice in my sentences',
   Q9='PASS: one point a sentence, the forms with their reason first, the breathing sentence with its reason')
R['brainev-c2'] = dict(R['brainev-c1'])
R['brainev-c2']['mine'] = R['brainev-c1']['mine'][:2] + [
   ('they know his judgment goes further than the studies, and the studies point the same way', 'how far the evidence goes',
    'That\'s more than'),
   ('they know from animal stroke research that it may still help after the damage has started', 'the finding they can act on',
    'In animal stroke research'),
   ('they know the evidence in people: a preliminary trial after clot strokes, and a small series for pressure in the skull',
    'the human evidence', 'A preliminary trial'),
   ('they know it calms the nerve signaling that kills brain cells after a stroke', 'how it works', 'It also calms'),
]
R['brainev-c2']['questions'] = dict(R['brainev-c1']['questions'],
   Q1='PASS: his belief first, then how far the evidence goes, then the finding the reader can act on, then the rest',
   Q2='PASS: the reader acts on it by trusting DMSO, and by starting it even after the damage has started',
   Q4='PASS: "intracranial hypertension", "infarct" and "ischemia" said plainly; "NMDA- and AMPA-mediated excitotoxicity" in brackets after the plain words',
   Q5='PASS: "but", "so", "and", "It also" say each relation',
   Q9='PASS: one point a sentence, the two findings in people in one sentence of two shapes')

R['rescuep-c9'] = dict(R['rescue-c9'], mine=[(a, b, c if i else 'none: the first sentence of the paragraph, tested by itself')
                                            for i, (a, b, c) in enumerate(R['rescue-c9']['mine'][13:])],
                       same_point=R['rescue-c9']['same_point'] + '; checked here by itself, as the ledger asks after a section reads Mixed')

R['rescue-c10'] = dict(R['rescue-c9'])
R['rescue-c10']['mine'] = R['rescue-c9']['mine'][:13] + [
   ('they give a rescue medicine for seizures, if the person has one, when and how its label says, as he would',
    'what else to do, after when to call', 'If they have a rescue medicine'),
   ('they know what they hold is a benzodiazepine, what doctors give first for a seizure that won\'t stop', 'what the medicine is',
    'It\'s a benzodiazepine'),
   ('they know it will be a nasal spray, a rectal gel or a shot, since a pill is no use during a seizure', 'what form it comes in',
    'A pill is no use'),
   ('they keep a close eye on the person\'s breathing after giving it, more closely if opioids or alcohol were taken too',
    'what to do after giving it, and why', 'After giving it'),
]
R['rescue-c10']['questions'] = dict(R['rescue-c9']['questions'],
   Q2='PASS: "I\'d give it when and how its label says", "I\'d keep a close eye on their breathing": the acts, in his voice',
   Q5='PASS: "the kind of drug", "so", "since", "especially if" say each relation, no connector twice in my sentences')
R['rescuep-c10'] = dict(R['rescue-c10'], mine=[(a, b, c if i else 'none: the first sentence of the paragraph, tested by itself')
                                              for i, (a, b, c) in enumerate(R['rescue-c10']['mine'][13:])],
                        same_point=R['rescue-c10']['same_point'] + '; checked here by itself, as the ledger asks after a section reads Mixed')


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
        print(key, 'has', len(rc['sentences']), 'sentences and', len(d['mine']), 'entries')
        for x in rc['sentences']:
            print('  ', x['s'][:80])
        return
    for i, (s, (payoff, follows, link)) in enumerate(zip(rc['sentences'], d['mine'])):
        s['payoff'], s['follows'] = payoff, follows
        if i:
            s['link'] = link
    rc['placement'], rc['same_point'], rc['questions'] = d['placement'], d['same_point'], d['questions']
    rc['opens']['why_reading'] = d['why_reading']
    src = {'rescuep-c9': 'rescue-c9', 'rescuep-c10': 'rescue-c10'}.get(key, key)
    rc['needed'], rc['his_fixes'], rc['fit'] = NEEDED[src], HISFIX[src], FIT[src]
    out.write_text(json.dumps(rc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    o = (c.stdout + c.stderr).strip()
    print(key, o.splitlines()[-1] if o else c.returncode)
    if c.returncode:
        print(o)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(R):
        fill(k)
